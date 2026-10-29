# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f762

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f762
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f762.jsonl
- **Records:** 1891 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f762
- **Time span:** 2026-04-13T19:14:29.518000+00:00 .. 2026-04-23T20:10:26.658000+00:00 (240h 55m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f762\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 1891 records, 8 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 70 INFO, 0 NOT_TESTED, 48 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `WaterChamberEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1395 | 73.77 | 1 | 8 | 971 | 2026-04-13T19:14:48.133000+00:00 | 2026-04-23T20:10:26.658000+00:00 | 240h 55m |
| PlayerPositionEvent | 308 | 16.29 | 1 | 8 | 0 | 2026-04-13T19:14:29.518000+00:00 | 2026-04-23T20:10:16.080000+00:00 | 240h 55m |
| questEvent | 60 | 3.17 | 1 | 8 | 60 | 2026-04-13T19:14:48.037000+00:00 | 2026-04-23T20:07:42.537000+00:00 | 240h 52m |
| Topographic Map Event | 42 | 2.22 | 1 | 3 | 0 | 2026-04-15T19:36:42.744000+00:00 | 2026-04-23T20:06:37.114000+00:00 | 192h 29m |
| TopographicMapEvent | 24 | 1.27 | 1 | 2 | 0 | 2026-04-15T19:36:51.727000+00:00 | 2026-04-21T19:22:52.405000+00:00 | 143h 46m |
| soilMachine | 15 | 0.79 | 1 | 1 | 0 | 2026-04-23T19:43:26.022000+00:00 | 2026-04-23T19:50:36.177000+00:00 | 7m 10s |
| argumentationNodeEvent | 13 | 0.69 | 1 | 2 | 0 | 2026-04-15T19:21:19.189000+00:00 | 2026-04-21T19:34:54.103000+00:00 | 144h 13m |
| Soil Key Puzzle | 9 | 0.48 | 1 | 3 | 0 | 2026-04-15T19:31:19.754000+00:00 | 2026-04-23T19:37:03.930000+00:00 | 192h 5m |
| argumentationEvent | 8 | 0.42 | 1 | 3 | 0 | 2026-04-15T19:21:06.655000+00:00 | 2026-04-23T19:58:09.042000+00:00 | 192h 37m |
| TerasGardenBox | 7 | 0.37 | 1 | 1 | 0 | 2026-04-23T20:04:15.044000+00:00 | 2026-04-23T20:04:53.226000+00:00 | 38.2s |
| EndOfUnit | 4 | 0.21 | 1 | 3 | 0 | 2026-04-15T19:24:34.439000+00:00 | 2026-04-23T20:07:09.191000+00:00 | 192h 42m |
| argumentationToolEvent | 4 | 0.21 | 1 | 2 | 0 | 2026-04-21T19:20:44.150000+00:00 | 2026-04-23T19:58:05.051000+00:00 | 48h 37m |
| crash | 2 | 0.11 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.609s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173200.199s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.013s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 483.29s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
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
  - Observed: 29.836s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.655s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.631s median 
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
  - Observed: 3.699s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 308 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 9 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` — field(s) not present in baseline schema. 
  - Observed: data.boxID
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: soilSelected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 42 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 13 records 
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
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 44; 45; 51; 52; 53; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 14 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f762.jsonl[144] _id=69dfe55f7957a33870f4719b ts=2026-04-15T19:22:06.9020000Z`; `69cdc937d385e3b94310f762.jsonl[299] _id=69dfe96a7957a33870f481fd ts=2026-04-15T19:39:21.1710000Z`; `69cdc937d385e3b94310f762.jsonl[550] _id=69e7d1601724f0c9e2f9e111 ts=2026-04-21T19:34:55.1680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 42 records, TopographicMapEvent: 24 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 4 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1394 | 0.002 | 1.609 | 622.194 | 34.2 | 513972.772 | 0.1 | 354 | 3 |
| PlayerPositionEvent | 297 | 29.812 | 30.013 | 1189.037 | 41.799 | 172470.303 | 0.05 | 0 | 2 |
| questEvent | 59 | 0.009 | 105.764 | 14697.873 | 18071.763 | 514321.141 | 0.0 | 8 | 6 |
| Topographic Map Event | 41 | 0.544 | 11.811 | 16902.302 | 1815.451 | 515489.006 | 0.0 | 0 | 3 |
| TopographicMapEvent | 23 | 0.448 | 2.687 | 22502.638 | 431.509 | 516691.728 | 0.0 | 0 | 1 |
| soilMachine | 14 | 0.848 | 3.699 | 30.725 | 129.627 | 253.766 | 1.95 | 0 | 0 |
| argumentationNodeEvent | 12 | 0.808 | 4.655 | 43267.91 | 233624.531 | 519140.037 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 8 | 27.162 | 483.29 | 86443.022 | 396490.063 | 517133.894 | 0.0 | 0 | 4 |
| argumentationEvent | 7 | 0.108 | 29.836 | 99060.341 | 415647.906 | 519128.235 | 0.0 | 0 | 2 |
| TerasGardenBox | 6 | 0.11 | 2.103 | 6.364 | 17.683 | 18.943 | 9.43 | 0 | 0 |
| EndOfUnit | 3 | 0.0 | 173200.199 | 231251.584 | 485819.118 | 520554.553 | 0.0 | 1 | 2 |
| argumentationToolEvent | 3 | 0.002 | 1.631 | 58346.967 | 157535.504 | 175039.268 | 0.0 | 1 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.013s (p5 29.96s, p95 41.80s, n=297) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc937d385e3b94310f762.jsonl[188] _id=69dfe5f37957a33870f47443 ts=2026-04-15T19:24:34.4390000Z ~ 69cdc937d385e3b94310f762.jsonl[187] _id=69dfe6057957a33870f47495 ts=2026-04-15T19:24:34.439Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `110ms: 69cdc937d385e3b94310f762.jsonl[1856] _id=69ea7b3f1724f0c9e2fb67fd ts=2026-04-23T20:04:15.0440000Z ~ 69cdc937d385e3b94310f762.jsonl[1857] _id=69ea7b3f1724f0c9e2fb67ff ts=2026-04-23T20:04:15.1540000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `108ms: 69cdc937d385e3b94310f762.jsonl[549] _id=69e7d1601724f0c9e2f9e10f ts=2026-04-21T19:34:55.1300000Z ~ 69cdc937d385e3b94310f762.jsonl[551] _id=69e7d1601724f0c9e2f9e115 ts=2026-04-21T19:34:55.2380000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc937d385e3b94310f762.jsonl[1818] _id=69ea79cd1724f0c9e2fb63d1 ts=2026-04-23T19:58:05.0490000Z ~ 69cdc937d385e3b94310f762.jsonl[904] _id=69ea79cd1724f0c9e2fb63d5 ts=2026-04-23T19:58:05.0510000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `925ms: 69cdc937d385e3b94310f762.jsonl[797] _id=69ea765e1724f0c9e2fb5a49 ts=2026-04-23T19:43:26.0220000Z ~ 69cdc937d385e3b94310f762.jsonl[802] _id=69ea765f1724f0c9e2fb5a4b ts=2026-04-23T19:43:26.9470000Z`; `848ms: 69cdc937d385e3b94310f762.jsonl[1760] _id=69ea77b31724f0c9e2fb5d63 ts=2026-04-23T19:49:07.0660000Z ~ 69cdc937d385e3b94310f762.jsonl[1762] _id=69ea77b41724f0c9e2fb5d69 ts=2026-04-23T19:49:07.9140000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 142h 46m 
  - Evidence: 142h 46m: 69cdc937d385e3b94310f762.jsonl[1308] _id=69dff04a7957a33870f49ed9 ts=2026-04-15T20:08:41.5220000Z -> 69cdc937d385e3b94310f762.jsonl[1309] _id=69e7c7ff1724f0c9e2f9ae59 ts=2026-04-21T18:54:54.2940000Z; 47h 54m: 69cdc937d385e3b94310f762.jsonl[1112] _id=69dd40b87957a33870f293e1 ts=2026-04-13T19:15:04.4020000Z -> 69cdc937d385e3b94310f762.jsonl[3] _id=69dfe27f7957a33870f46743 ts=2026-04-15T19:09:50.9340000Z; 47h 29m: 69cdc937d385e3b94310f762.jsonl[1673] _id=69e7d8861724f0c9e2f9fe05 ts=2026-04-21T20:05:25.0870000Z -> 69cdc937d385e3b94310f762.jsonl[1675] _id=69ea74761724f0c9e2fb5567 ts=2026-04-23T19:35:18.1540000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 354 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f762.jsonl[159] _id=69dfe5977957a33870f47289 ts=2026-04-15T19:23:02.2450000Z -> 69cdc937d385e3b94310f762.jsonl[166] _id=69dfe5977957a33870f4728b ts=2026-04-15T19:23:02.2470000Z; 2ms: 69cdc937d385e3b94310f762.jsonl[1851] _id=69ea7afb1724f0c9e2fb671f ts=2026-04-23T20:03:06.5870000Z -> 69cdc937d385e3b94310f762.jsonl[1852] _id=69ea7afb1724f0c9e2fb6721 ts=2026-04-23T20:03:06.5890000Z; 3ms: 69cdc937d385e3b94310f762.jsonl[157] _id=69dfe58f7957a33870f47263 ts=2026-04-15T19:22:54.5660000Z -> 69cdc937d385e3b94310f762.jsonl[1163] _id=69dfe58f7957a33870f47265 ts=2026-04-15T19:22:54.5690000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 35m 
  - Evidence: 144h 35m: 69cdc937d385e3b94310f762.jsonl[187] _id=69dfe6057957a33870f47495 ts=2026-04-15T19:24:34.439Z -> 69cdc937d385e3b94310f762.jsonl[1663] _id=69e7d75d1724f0c9e2f9f96d ts=2026-04-21T20:00:28.9920000Z; 48h 6m: 69cdc937d385e3b94310f762.jsonl[1663] _id=69e7d75d1724f0c9e2f9f96d ts=2026-04-21T20:00:28.9920000Z -> 69cdc937d385e3b94310f762.jsonl[1086] _id=69ea7bed1724f0c9e2fb6a6d ts=2026-04-23T20:07:09.1910000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f762.jsonl[188] _id=69dfe5f37957a33870f47443 ts=2026-04-15T19:24:34.4390000Z -> 69cdc937d385e3b94310f762.jsonl[187] _id=69dfe6057957a33870f47495 ts=2026-04-15T19:24:34.439Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 54m 
  - Evidence: 47h 54m: 69cdc937d385e3b94310f762.jsonl[1113] _id=69dd40b67957a33870f293da ts=2026-04-13T19:15:02.0300000Z -> 69cdc937d385e3b94310f762.jsonl[2] _id=69dfe26d7957a33870f46729 ts=2026-04-15T19:09:32.3330000Z; 47h 29m: 69cdc937d385e3b94310f762.jsonl[758] _id=69e7d88d1724f0c9e2f9fe2f ts=2026-04-21T20:05:31.7330000Z -> 69cdc937d385e3b94310f762.jsonl[1674] _id=69ea74621724f0c9e2fb5557 ts=2026-04-23T19:34:57.5430000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 38m 
  - Evidence: 143h 38m: 69cdc937d385e3b94310f762.jsonl[437] _id=69dfeefb7957a33870f49869 ts=2026-04-15T20:03:06.5110000Z -> 69cdc937d385e3b94310f762.jsonl[1583] _id=69e7d3091724f0c9e2f9e8e9 ts=2026-04-21T19:42:00.4050000Z; 47h 53m: 69cdc937d385e3b94310f762.jsonl[601] _id=69e7d3301724f0c9e2f9e9a5 ts=2026-04-21T19:42:39.5350000Z -> 69cdc937d385e3b94310f762.jsonl[1685] _id=69ea74c51724f0c9e2fb55bf ts=2026-04-23T19:36:36.7680000Z; 14m 56s: 69cdc937d385e3b94310f762.jsonl[238] _id=69dfe7d77957a33870f47bcf ts=2026-04-15T19:32:39.1810000Z -> 69cdc937d385e3b94310f762.jsonl[353] _id=69dfeb597957a33870f48967 ts=2026-04-15T19:47:35.9700000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 11m 
  - Evidence: 143h 11m: 69cdc937d385e3b94310f762.jsonl[385] _id=69dfec147957a33870f48c1b ts=2026-04-15T19:50:43.6670000Z -> 69cdc937d385e3b94310f762.jsonl[1332] _id=69e7c9b51724f0c9e2f9b71b ts=2026-04-21T19:02:12.6730000Z; 48h 8m: 69cdc937d385e3b94310f762.jsonl[1643] _id=69e7d6a11724f0c9e2f9f65d ts=2026-04-21T19:57:20.5880000Z -> 69cdc937d385e3b94310f762.jsonl[1089] _id=69ea7bb51724f0c9e2fb69ad ts=2026-04-23T20:06:13.5640000Z; 30m 15s: 69cdc937d385e3b94310f762.jsonl[1459] _id=69e7cf3c1724f0c9e2f9d525 ts=2026-04-21T19:25:47.1840000Z -> 69cdc937d385e3b94310f762.jsonl[1636] _id=69e7d6531724f0c9e2f9f541 ts=2026-04-21T19:56:02.6350000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 31m 
  - Evidence: 143h 31m: 69cdc937d385e3b94310f762.jsonl[1251] _id=69dfea6a7957a33870f4862d ts=2026-04-15T19:43:37.2680000Z -> 69cdc937d385e3b94310f762.jsonl[1415] _id=69e7ccbd1724f0c9e2f9c9ed ts=2026-04-21T19:15:08.9960000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 69cdc937d385e3b94310f762.jsonl[143] _id=69dfe55f7957a33870f47199 ts=2026-04-15T19:22:06.8810000Z -> 69cdc937d385e3b94310f762.jsonl[536] _id=69e7d1381724f0c9e2f9dfe5 ts=2026-04-21T19:34:15.1160000Z; 48h 23m: 69cdc937d385e3b94310f762.jsonl[551] _id=69e7d1601724f0c9e2f9e115 ts=2026-04-21T19:34:55.2380000Z -> 69cdc937d385e3b94310f762.jsonl[907] _id=69ea79d11724f0c9e2fb63e7 ts=2026-04-23T19:58:09.0420000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 69cdc937d385e3b94310f762.jsonl[145] _id=69dfe5587957a33870f47187 ts=2026-04-15T19:21:59.6180000Z -> 69cdc937d385e3b94310f762.jsonl[540] _id=69e7d13c1724f0c9e2f9e01d ts=2026-04-21T19:34:19.6550000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 37m 
  - Evidence: 48h 37m: 69cdc937d385e3b94310f762.jsonl[1445] _id=69e7ce0e1724f0c9e2f9d0ae ts=2026-04-21T19:20:45.7810000Z -> 69cdc937d385e3b94310f762.jsonl[1818] _id=69ea79cd1724f0c9e2fb63d1 ts=2026-04-23T19:58:05.0490000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f762.jsonl[1818] _id=69ea79cd1724f0c9e2fb63d1 ts=2026-04-23T19:58:05.0490000Z -> 69cdc937d385e3b94310f762.jsonl[904] _id=69ea79cd1724f0c9e2fb63d5 ts=2026-04-23T19:58:05.0510000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 142h 52m 
  - Evidence: 142h 52m: 69cdc937d385e3b94310f762.jsonl[445] _id=69dff0447957a33870f49e9b ts=2026-04-15T20:08:35.3270000Z -> 69cdc937d385e3b94310f762.jsonl[463] _id=69e7c9551724f0c9e2f9b547 ts=2026-04-21T19:00:36.4680000Z; 47h 55m: 69cdc937d385e3b94310f762.jsonl[1107] _id=69dd40a87957a33870f293a6 ts=2026-04-13T19:14:48.0370000Z -> 69cdc937d385e3b94310f762.jsonl[0] _id=69dfe27f7957a33870f46741 ts=2026-04-15T19:09:50.9170000Z; 47h 30m: 69cdc937d385e3b94310f762.jsonl[755] _id=69e7d8371724f0c9e2f9fc59 ts=2026-04-21T20:04:06.4800000Z -> 69cdc937d385e3b94310f762.jsonl[1678] _id=69ea74641724f0c9e2fb5559 ts=2026-04-23T19:34:59.6860000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.009s..0.009s shown 
  - Evidence: 9ms: 69cdc937d385e3b94310f762.jsonl[129] _id=69dfe5107957a33870f47027 ts=2026-04-15T19:20:47.0800000Z -> 69cdc937d385e3b94310f762.jsonl[130] _id=69dfe5107957a33870f47029 ts=2026-04-15T19:20:47.0890000Z; 9ms: 69cdc937d385e3b94310f762.jsonl[811] _id=69ea768f1724f0c9e2fb5abb ts=2026-04-23T19:44:15.0000000Z -> 69cdc937d385e3b94310f762.jsonl[812] _id=69ea768f1724f0c9e2fb5abd ts=2026-04-23T19:44:15.0090000Z; 9ms: 69cdc937d385e3b94310f762.jsonl[819] _id=69ea77461724f0c9e2fb5c67 ts=2026-04-23T19:47:18.6420000Z -> 69cdc937d385e3b94310f762.jsonl[820] _id=69ea77471724f0c9e2fb5c69 ts=2026-04-23T19:47:18.6510000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc937d385e3b94310f762.jsonl:69cdc937d385e3b94310f762, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f762.jsonl[238] _id=69dfe7d77957a33870f47bcf ts=2026-04-15T19:32:39.1810000Z`; `69cdc937d385e3b94310f762.jsonl[1257] _id=69dfeb847957a33870f489cd ts=2026-04-15T19:48:19.3590000Z`; `69cdc937d385e3b94310f762.jsonl[601] _id=69e7d3301724f0c9e2f9e9a5 ts=2026-04-21T19:42:39.5350000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 24 record(s) match the trigger in 69cdc937d385e3b94310f762.jsonl:69cdc937d385e3b94310f762, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f762.jsonl[1220] _id=69dfe8d47957a33870f47fb3 ts=2026-04-15T19:36:51.7270000Z`; `69cdc937d385e3b94310f762.jsonl[1219] _id=69dfe8d67957a33870f47fbf ts=2026-04-15T19:36:53.8200000Z`; `69cdc937d385e3b94310f762.jsonl[1222] _id=69dfe8e37957a33870f47fe1 ts=2026-04-15T19:37:06.4830000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f762.jsonl[1361] _id=69e7caab1724f0c9e2f9bd55 ts=2026-04-21T19:06:18.5380000Z`; `69cdc937d385e3b94310f762.jsonl[476] _id=69e7cb441724f0c9e2f9c0a1 ts=2026-04-21T19:08:50.7020000Z`; `69cdc937d385e3b94310f762.jsonl[1781] _id=69ea788c1724f0c9e2fb5f4b ts=2026-04-23T19:52:43.9680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f762.jsonl[551] _id=69e7d1601724f0c9e2f9e115 ts=2026-04-21T19:34:55.2380000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f762.jsonl[1445] _id=69e7ce0e1724f0c9e2f9d0ae ts=2026-04-21T19:20:45.7810000Z`; `69cdc937d385e3b94310f762.jsonl[1818] _id=69ea79cd1724f0c9e2fb63d1 ts=2026-04-23T19:58:05.0490000Z`; `69cdc937d385e3b94310f762.jsonl[904] _id=69ea79cd1724f0c9e2fb63d5 ts=2026-04-23T19:58:05.0510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc937d385e3b94310f762.jsonl[740] _id=69e7d75f1724f0c9e2f9f979 ts=?`; `69cdc937d385e3b94310f762.jsonl[1665] _id=69e7d8051724f0c9e2f9fbe9 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 161 unmatched 'DialogueStartEvent' (totals: 291 start, 133 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 1 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 36 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.79s, min -18.63s, max -0.18s over 1889 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f762\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `WaterChamberEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 42 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1395 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (385); Unit 2 Prod (Refactor) (279); Unit 4 Dev (227); Unit 1 Dev (192); Unit 4 Dev - Anderson Base (115); Unit 4 Dev - Dungeon (90); Unit 3 Dungeon Dev (89); Unit 5 Dev - Dungeon (18)
- **eventKey:** present on 971 of 1395 records
- **Intervals:** median 1.61s (p5 0.01s / p95 34.20s, n=1394)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x971; [conversationId, dialogueEventType] x424
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1395/1395 records)
    numeric range 10 .. 114 (39 unique)
data.dialogueEventType  (string, 1395/1395 records)
    "DialogueNodeEvent"  x971
    "DialogueStartEvent"  x291
    "DialogueFinishEvent"  x133
data.nodeId  (number, 971/1395 records)
    numeric range 0 .. 289 (201 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 308 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (97); Unit 2 Prod (Refactor) (73); Unit 4 Dev (34); Unit 1 Dev (32); Unit 4 Dev - Dungeon (26); Unit 3 Dungeon Dev (24); Unit 4 Dev - Anderson Base (16); Unit 5 Dev - Dungeon (6)
- **Intervals:** median 30.01s (p5 29.96s / p95 41.80s, n=297)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 308/308 records)
data.position.x  (number, 308/308 records)
    numeric range -626.31 .. 1557.91 (173 unique)
data.position.y  (number, 308/308 records)
    numeric range -114.069 .. 155.22 (156 unique)
data.position.z  (number, 308/308 records)
    numeric range -1115.44 .. 2215.98 (174 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 60 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (13); Unit 2 Prod (Refactor) (12); Unit 3 Dev (12); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (1)
- **eventKey:** present on 60 of 60 records
- **Intervals:** median 105.76s (p5 0.01s / p95 18071.76s, n=59)
- **`data` key-set variants:** [questEventType, questID, questName] x36; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Fields under `data`:**

```text
data.questEventType  (string, 60/60 records)
    "questActiveEvent"  x36
    "questFinishEvent"  x24
data.questID  (string, 60/60 records)
    26 unique values (see csv/event_unique_values.csv)
data.questName  (string, 60/60 records)
    26 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/60 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 42 records

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (18); Unit 4 Dev (6)
- **Intervals:** median 11.81s (p5 0.85s / p95 1815.45s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "MapCloseEvent"  x21
    "MapOpenEvent"  x21
data.featureUsed  (string, 42/42 records)
    "Map"  x42
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 24 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (6)
- **Intervals:** median 2.69s (p5 0.48s / p95 431.51s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "dragEnd"  x12
    "dragStart"  x12
data.featureUsed  (string, 24/24 records)
    "waypoint"  x24
data.location  (object, 24/24 records)
data.location.x  (number, 24/24 records)
    numeric range -770.79 .. 240.834 (13 unique)
data.location.y  (number, 24/24 records)
    numeric range -307.4 .. 130.305 (13 unique)
data.location.z  (number, 24/24 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 15 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (15)
- **Intervals:** median 3.70s (p5 0.90s / p95 129.63s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "ChangeCanister"  x15
data.canisterType  (string, 15/15 records)
    "Sand"  x6
    "Clay"  x4
    "Bedrock"  x3
    "Gravel"  x2
data.floor  (string, 15/15 records)
    "5"  x9
    "3"  x5
    "4"  x1
data.machine  (string, 15/15 records)
    "1"  x13
    "2"  x2
data.row  (string, 15/15 records)
    "TopRow"  x12
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationNodeEvent` — 13 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (7); Unit 1 Dev (6)
- **Intervals:** median 4.65s (p5 1.38s / p95 233624.53s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 13/13 records)
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x1
data.nodeName  (string, 13/13 records)
    "I"  x4
    "B"  x3
    "1"  x2
    "II"  x2
    "5"  x1
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 9 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 483.29s (p5 31.35s / p95 396490.06s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/9 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/9 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 29.84s (p5 3.88s / p95 415647.91s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 8/8 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 2.10s (p5 0.34s / p95 17.68s, n=6)
- **`data` key-set variants:** [actionType, boxID, soilType] x4; [actionType, boxId, soilType] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "soilSelected"  x4
    "cameraPlaced"  x3
data.boxID  (string, 4/7 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.boxId  (string, 3/7 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 7/7 records)
    "Gravel"  x3
    "Clay"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 173200.20s (p5 17320.02s / p95 485819.12s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x2
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 1.63s (p5 0.16s / p95 157535.50s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x3
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 3 - Pollution Upstream"  x2
    "Unit 4 - Flooding"  x2
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Soil Flow Rates"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit3"  x1
    "unit4"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

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
- `WaterChamberEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (5 records)
- `TopographicMapEvent` data.actionType: "dragStart" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*