# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f755

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f755
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f755.jsonl
- **Records:** 3215 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f755
- **Time span:** 2026-04-13T19:25:12.823000+00:00 .. 2026-04-23T19:54:05.622000+00:00 (240h 28m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f755\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 3215 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 67 INFO, 0 NOT_TESTED, 55 PASS.
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
| DialogueEvent | 2339 | 72.75 | 1 | 9 | 1651 | 2026-04-13T19:25:31.062000+00:00 | 2026-04-23T19:54:00.224000+00:00 | 240h 28m |
| PlayerPositionEvent | 516 | 16.05 | 1 | 9 | 0 | 2026-04-13T19:25:12.823000+00:00 | 2026-04-23T19:53:38.833000+00:00 | 240h 28m |
| questEvent | 90 | 2.8 | 1 | 9 | 90 | 2026-04-13T19:25:31.045000+00:00 | 2026-04-23T19:53:05.620000+00:00 | 240h 27m |
| soilMachine | 63 | 1.96 | 1 | 1 | 0 | 2026-04-21T19:06:52.592000+00:00 | 2026-04-21T19:22:06.004000+00:00 | 15m 13s |
| WaterChamberEvent | 60 | 1.87 | 1 | 1 | 0 | 2026-04-23T19:37:47.397000+00:00 | 2026-04-23T19:42:17.826000+00:00 | 4m 30s |
| argumentationToolEvent | 36 | 1.12 | 1 | 4 | 0 | 2026-04-15T20:07:14.120000+00:00 | 2026-04-23T19:46:29.744000+00:00 | 191h 39m |
| argumentationNodeEvent | 27 | 0.84 | 1 | 3 | 0 | 2026-04-13T19:40:35.429000+00:00 | 2026-04-17T19:19:32.483000+00:00 | 95h 38m |
| Topographic Map Event | 24 | 0.75 | 1 | 2 | 0 | 2026-04-15T19:21:49.544000+00:00 | 2026-04-17T19:56:10.717000+00:00 | 48h 34m |
| TopographicMapEvent | 22 | 0.68 | 1 | 2 | 0 | 2026-04-15T19:21:58.236000+00:00 | 2026-04-17T19:56:09.281000+00:00 | 48h 34m |
| argumentationEvent | 14 | 0.44 | 1 | 5 | 0 | 2026-04-13T19:40:28.664000+00:00 | 2026-04-23T19:47:39.688000+00:00 | 240h 7m |
| Soil Key Puzzle | 12 | 0.37 | 1 | 3 | 0 | 2026-04-13T20:02:43.733000+00:00 | 2026-04-17T20:04:40.958000+00:00 | 96h 1m |
| EndOfUnit | 6 | 0.19 | 1 | 5 | 0 | 2026-04-13T19:45:24.291000+00:00 | 2026-04-23T19:54:05.622000+00:00 | 240h 8m |
| TerasGardenBox | 6 | 0.19 | 1 | 1 | 0 | 2026-04-21T19:41:50.047000+00:00 | 2026-04-21T19:57:07.105000+00:00 | 15m 17s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.672s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172473.416s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.005s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 149.165s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 13.279s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 2.117s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 9.841s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.032s median 
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
  - Observed: 4.406s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 12 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.boxId` — baseline categorical value(s) not seen this build. 
  - Observed: 0; 1 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 24 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 60 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 27 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; C 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 36 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Desert Delicacies 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 12.6x vs baseline. 
  - Observed: 63 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 306 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f755.jsonl[112] _id=69dd47167957a33870f2a4ab ts=2026-04-13T19:42:13.4480000Z`; `69cdc937d385e3b94310f755.jsonl[363] _id=69dfe6a67957a33870f477ab ts=2026-04-15T19:27:33.2600000Z`; `69cdc937d385e3b94310f755.jsonl[364] _id=69dfe6a67957a33870f477ad ts=2026-04-15T19:27:33.4380000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'questActiveEvent:41' vs expected 'questActiveEvent:56' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc937d385e3b94310f755.jsonl[1122] _id=69ea73fa1724f0c9e2fb5223 ts=2026-04-21T19:40:57.236Z`; `69cdc937d385e3b94310f755.jsonl[1168] _id=69ea73ff1724f0c9e2fb52a9 ts=2026-04-21T19:43:17.613Z`; `69cdc937d385e3b94310f755.jsonl[1362] _id=69ea740e1724f0c9e2fb542d ts=2026-04-21T19:56:16.826Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 24 records, TopographicMapEvent: 22 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2338 | 0.0 | 1.672 | 370.278 | 26.656 | 341113.711 | 0.16 | 559 | 4 |
| PlayerPositionEvent | 501 | 29.701 | 30.005 | 1385.223 | 33.11 | 341066.03 | 0.04 | 0 | 3 |
| questEvent | 89 | 0.003 | 125.757 | 9726.456 | 1048.403 | 341114.895 | 0.01 | 14 | 8 |
| soilMachine | 62 | 0.15 | 4.406 | 14.732 | 56.768 | 154.189 | 4.07 | 0 | 0 |
| WaterChamberEvent | 59 | 0.192 | 2.117 | 4.584 | 16.906 | 24.962 | 13.09 | 0 | 0 |
| argumentationToolEvent | 35 | 0.002 | 3.032 | 19713.018 | 169613.127 | 346444.681 | 0.0 | 4 | 5 |
| argumentationNodeEvent | 26 | 1.462 | 9.841 | 13243.733 | 126648.072 | 174344.496 | 0.0 | 0 | 3 |
| Topographic Map Event | 23 | 4.94 | 17.592 | 7602.66 | 1105.429 | 172471.915 | 0.01 | 0 | 2 |
| TopographicMapEvent | 21 | 1.195 | 3.214 | 8326.24 | 595.462 | 173651.703 | 0.01 | 0 | 1 |
| argumentationEvent | 13 | 0.085 | 124.611 | 66494.694 | 243142.234 | 346416.05 | 0.0 | 0 | 6 |
| Soil Key Puzzle | 11 | 2.761 | 149.165 | 31428.839 | 170717.607 | 171411.411 | 0.0 | 0 | 5 |
| EndOfUnit | 5 | 827.968 | 172473.416 | 172904.266 | 344515.835 | 344939.163 | 0.0 | 0 | 5 |
| TerasGardenBox | 5 | 9.586 | 13.279 | 183.412 | 697.969 | 868.544 | 0.33 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.96s, p95 33.11s, n=501) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `616ms: 69cdc937d385e3b94310f755.jsonl[1542] _id=69ea76111724f0c9e2fb5977 ts=2026-04-23T19:42:08.7490000Z ~ 69cdc937d385e3b94310f755.jsonl[1544] _id=69ea76121724f0c9e2fb597b ts=2026-04-23T19:42:09.3650000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `85ms: 69cdc937d385e3b94310f755.jsonl[2494] _id=69e287c91724f0c9e2f7a836 ts=2026-04-17T19:19:36.8820000Z ~ 69cdc937d385e3b94310f755.jsonl[2498] _id=69e287ca1724f0c9e2f7a83e ts=2026-04-17T19:19:36.9670000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `680ms: 69cdc937d385e3b94310f755.jsonl[2307] _id=69e282501724f0c9e2f792aa ts=2026-04-17T18:56:15.8590000Z ~ 69cdc937d385e3b94310f755.jsonl[613] _id=69e282511724f0c9e2f792b6 ts=2026-04-17T18:56:16.5390000Z`; `2ms: 69cdc937d385e3b94310f755.jsonl[959] _id=69ea73ee1724f0c9e2fb5107 ts=2026-04-21T19:33:05.334Z ~ 69cdc937d385e3b94310f755.jsonl[3117] _id=69ea73ee1724f0c9e2fb5109 ts=2026-04-21T19:33:05.336Z`; `37ms: 69cdc937d385e3b94310f755.jsonl[964] _id=69ea73f01724f0c9e2fb511b ts=2026-04-21T19:33:42.525Z ~ 69cdc937d385e3b94310f755.jsonl[965] _id=69ea73f01724f0c9e2fb511d ts=2026-04-21T19:33:42.562Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 69cdc937d385e3b94310f755.jsonl[3184] _id=69ea77661724f0c9e2fb5cbb ts=2026-04-23T19:47:50.1930000Z ~ 69cdc937d385e3b94310f755.jsonl[1598] _id=69ea77671724f0c9e2fb5cbe ts=2026-04-23T19:47:50.1980000Z`; `6ms: 69cdc937d385e3b94310f755.jsonl[1649] _id=69ea78921724f0c9e2fb5f55 ts=2026-04-23T19:52:50.3410000Z ~ 69cdc937d385e3b94310f755.jsonl[1650] _id=69ea78921724f0c9e2fb5f57 ts=2026-04-23T19:52:50.3470000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `866ms: 69cdc937d385e3b94310f755.jsonl[2896] _id=69e7cada1724f0c9e2f9be0d ts=2026-04-21T19:07:06.4930000Z ~ 69cdc937d385e3b94310f755.jsonl[2897] _id=69e7cadb1724f0c9e2f9be0f ts=2026-04-21T19:07:07.3590000Z`; `697ms: 69cdc937d385e3b94310f755.jsonl[2897] _id=69e7cadb1724f0c9e2f9be0f ts=2026-04-21T19:07:07.3590000Z ~ 69cdc937d385e3b94310f755.jsonl[2898] _id=69e7cadc1724f0c9e2f9be1d ts=2026-04-21T19:07:08.0560000Z`; `660ms: 69cdc937d385e3b94310f755.jsonl[902] _id=69e7cae41724f0c9e2f9be47 ts=2026-04-21T19:07:16.0450000Z ~ 69cdc937d385e3b94310f755.jsonl[903] _id=69e7cae51724f0c9e2f9be51 ts=2026-04-21T19:07:16.7050000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc937d385e3b94310f755.jsonl[2822] _id=69e2935d1724f0c9e2f7dba0 ts=2026-04-17T20:09:01.0150000Z -> 69cdc937d385e3b94310f755.jsonl[2826] _id=69e7c7d71724f0c9e2f9adb1 ts=2026-04-21T18:54:14.7260000Z; 47h 34m: 69cdc937d385e3b94310f755.jsonl[3128] _id=69ea74161724f0c9e2fb5507 ts=2026-04-21T19:59:32.265Z -> 69cdc937d385e3b94310f755.jsonl[1465] _id=69ea741e1724f0c9e2fb5511 ts=2026-04-23T19:33:49.6210000Z; 47h 0m: 69cdc937d385e3b94310f755.jsonl[255] _id=69dd4d6f7957a33870f2bc21 ts=2026-04-13T20:09:17.3350000Z -> 69cdc937d385e3b94310f755.jsonl[1829] _id=69dfe2667957a33870f4671f ts=2026-04-15T19:09:24.9880000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 559 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f755.jsonl[821] _id=69e2907e1724f0c9e2f7d01a ts=2026-04-17T19:56:45.0980000Z -> 69cdc937d385e3b94310f755.jsonl[2762] _id=69e2912b1724f0c9e2f7d14c ts=2026-04-17T19:56:45.098Z; 2ms: 69cdc937d385e3b94310f755.jsonl[131] _id=69dd47897957a33870f2a625 ts=2026-04-13T19:44:08.6420000Z -> 69cdc937d385e3b94310f755.jsonl[1724] _id=69dd47897957a33870f2a627 ts=2026-04-13T19:44:08.6440000Z; 3ms: 69cdc937d385e3b94310f755.jsonl[122] _id=69dd47567957a33870f2a587 ts=2026-04-13T19:43:17.7340000Z -> 69cdc937d385e3b94310f755.jsonl[1721] _id=69dd47567957a33870f2a589 ts=2026-04-13T19:43:17.7370000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 48m 
  - Evidence: 95h 48m: 69cdc937d385e3b94310f755.jsonl[820] _id=69e2907d1724f0c9e2f7d018 ts=2026-04-17T19:56:45.0750000Z -> 69cdc937d385e3b94310f755.jsonl[1097] _id=69ea74031724f0c9e2fb530d ts=2026-04-21T19:45:44.238Z; 95h 13m: 69cdc937d385e3b94310f755.jsonl[146] _id=69dd47d57957a33870f2a785 ts=2026-04-13T19:45:24.2910000Z -> 69cdc937d385e3b94310f755.jsonl[680] _id=69e282fb1724f0c9e2f7955a ts=2026-04-17T18:59:06.8150000Z; 47h 54m: 69cdc937d385e3b94310f755.jsonl[1453] _id=69ea74161724f0c9e2fb5505 ts=2026-04-21T19:59:32.206Z -> 69cdc937d385e3b94310f755.jsonl[3214] _id=69ea78de1724f0c9e2fb608b ts=2026-04-23T19:54:05.6220000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f755.jsonl[2825] _id=69e2937e1724f0c9e2f7dc44 ts=2026-04-17T20:09:33.8540000Z -> 69cdc937d385e3b94310f755.jsonl[2827] _id=69e7c7c81724f0c9e2f9ad79 ts=2026-04-21T18:53:59.8840000Z; 46h 59m: 69cdc937d385e3b94310f755.jsonl[259] _id=69dd4da87957a33870f2bcaf ts=2026-04-13T20:10:15.9560000Z -> 69cdc937d385e3b94310f755.jsonl[1827] _id=69dfe2627957a33870f4671b ts=2026-04-15T19:09:20.5400000Z; 46h 40m: 69cdc937d385e3b94310f755.jsonl[2240] _id=69dff0437957a33870f49e8f ts=2026-04-15T20:08:34.2340000Z -> 69cdc937d385e3b94310f755.jsonl[2249] _id=69e2809a1724f0c9e2f78d50 ts=2026-04-17T18:48:57.3270000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 47h 36m 
  - Evidence: 47h 36m: 69cdc937d385e3b94310f755.jsonl[2054] _id=69dfeae67957a33870f48811 ts=2026-04-15T19:45:42.0060000Z -> 69cdc937d385e3b94310f755.jsonl[2520] _id=69e2887a1724f0c9e2f7ab8c ts=2026-04-17T19:22:33.4170000Z; 47h 13m: 69cdc937d385e3b94310f755.jsonl[1818] _id=69dd4be77957a33870f2b6bd ts=2026-04-13T20:02:46.6850000Z -> 69cdc937d385e3b94310f755.jsonl[1861] _id=69dfe40f7957a33870f46c79 ts=2026-04-15T19:16:30.4890000Z; 40m 59s: 69cdc937d385e3b94310f755.jsonl[2536] _id=69e288a91724f0c9e2f7ac82 ts=2026-04-17T19:23:20.4670000Z -> 69cdc937d385e3b94310f755.jsonl[2781] _id=69e292451724f0c9e2f7d5ea ts=2026-04-17T20:04:20.2870000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 14m 28s 
  - Evidence: 14m 28s: 69cdc937d385e3b94310f755.jsonl[1146] _id=69ea73fd1724f0c9e2fb526b ts=2026-04-21T19:42:13.308Z -> 69cdc937d385e3b94310f755.jsonl[1375] _id=69ea74101724f0c9e2fb5455 ts=2026-04-21T19:56:41.852Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 54m 
  - Evidence: 47h 54m: 69cdc937d385e3b94310f755.jsonl[2143] _id=69dfedac7957a33870f492c7 ts=2026-04-15T19:57:31.9860000Z -> 69cdc937d385e3b94310f755.jsonl[2724] _id=69e28f641724f0c9e2f7cccc ts=2026-04-17T19:52:03.9010000Z; 19m 28s: 69cdc937d385e3b94310f755.jsonl[409] _id=69dfe9157957a33870f480a3 ts=2026-04-15T19:37:56.0580000Z -> 69cdc937d385e3b94310f755.jsonl[494] _id=69dfeda57957a33870f49299 ts=2026-04-15T19:57:24.6330000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 14m 
  - Evidence: 48h 14m: 69cdc937d385e3b94310f755.jsonl[410] _id=69dfe9147957a33870f480a1 ts=2026-04-15T19:37:55.9760000Z -> 69cdc937d385e3b94310f755.jsonl[807] _id=69e28f681724f0c9e2f7cce8 ts=2026-04-17T19:52:07.6790000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 13m 
  - Evidence: 96h 13m: 69cdc937d385e3b94310f755.jsonl[2498] _id=69e287ca1724f0c9e2f7a83e ts=2026-04-17T19:19:36.9670000Z -> 69cdc937d385e3b94310f755.jsonl[3118] _id=69ea73ee1724f0c9e2fb510d ts=2026-04-21T19:33:13.017Z; 48h 24m: 69cdc937d385e3b94310f755.jsonl[111] _id=69dd47167957a33870f2a4a9 ts=2026-04-13T19:42:13.4220000Z -> 69cdc937d385e3b94310f755.jsonl[543] _id=69dfefeb7957a33870f49ca3 ts=2026-04-15T20:07:06.4450000Z; 47h 51m: 69cdc937d385e3b94310f755.jsonl[1071] _id=69ea74081724f0c9e2fb53a9 ts=2026-04-21T19:53:49.244Z -> 69cdc937d385e3b94310f755.jsonl[1570] _id=69ea76df1724f0c9e2fb5b83 ts=2026-04-23T19:45:35.0770000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 48h 25m 
  - Evidence: 48h 25m: 69cdc937d385e3b94310f755.jsonl[106] _id=69dd47147957a33870f2a49f ts=2026-04-13T19:42:11.0630000Z -> 69cdc937d385e3b94310f755.jsonl[2232] _id=69dff01c7957a33870f49d93 ts=2026-04-15T20:07:55.5590000Z; 46h 47m: 69cdc937d385e3b94310f755.jsonl[546] _id=69dff0537957a33870f49f2f ts=2026-04-15T20:08:51.0030000Z -> 69cdc937d385e3b94310f755.jsonl[623] _id=69e282461724f0c9e2f79286 ts=2026-04-17T18:56:05.8100000Z; 21m 27s: 69cdc937d385e3b94310f755.jsonl[2309] _id=69e2826e1724f0c9e2f79340 ts=2026-04-17T18:56:45.1830000Z -> 69cdc937d385e3b94310f755.jsonl[2474] _id=69e287751724f0c9e2f7a6f8 ts=2026-04-17T19:18:13.0500000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 14m 
  - Evidence: 96h 14m: 69cdc937d385e3b94310f755.jsonl[2480] _id=69e287a51724f0c9e2f7a798 ts=2026-04-17T19:19:00.6530000Z -> 69cdc937d385e3b94310f755.jsonl[959] _id=69ea73ee1724f0c9e2fb5107 ts=2026-04-21T19:33:05.334Z; 47h 52m: 69cdc937d385e3b94310f755.jsonl[1290] _id=69ea74081724f0c9e2fb53a5 ts=2026-04-21T19:53:24.19Z -> 69cdc937d385e3b94310f755.jsonl[1583] _id=69ea770b1724f0c9e2fb5bdb ts=2026-04-23T19:46:19.0810000Z; 46h 47m: 69cdc937d385e3b94310f755.jsonl[2244] _id=69dff04b7957a33870f49edf ts=2026-04-15T20:08:42.4830000Z -> 69cdc937d385e3b94310f755.jsonl[2305] _id=69e282381724f0c9e2f79264 ts=2026-04-17T18:55:51.9970000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.002s..0.034s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f755.jsonl[959] _id=69ea73ee1724f0c9e2fb5107 ts=2026-04-21T19:33:05.334Z -> 69cdc937d385e3b94310f755.jsonl[3117] _id=69ea73ee1724f0c9e2fb5109 ts=2026-04-21T19:33:05.336Z; 7ms: 69cdc937d385e3b94310f755.jsonl[614] _id=69e282541724f0c9e2f792bc ts=2026-04-17T18:56:19.7240000Z -> 69cdc937d385e3b94310f755.jsonl[626] _id=69e282541724f0c9e2f792be ts=2026-04-17T18:56:19.7310000Z; 34ms: 69cdc937d385e3b94310f755.jsonl[1070] _id=69ea74081724f0c9e2fb53a3 ts=2026-04-21T19:53:24.156Z -> 69cdc937d385e3b94310f755.jsonl[1290] _id=69ea74081724f0c9e2fb53a5 ts=2026-04-21T19:53:24.19Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc937d385e3b94310f755.jsonl[882] _id=69e293501724f0c9e2f7db4e ts=2026-04-17T20:08:47.3190000Z -> 69cdc937d385e3b94310f755.jsonl[2828] _id=69e7c7ca1724f0c9e2f9ad7d ts=2026-04-21T18:54:02.2140000Z; 47h 34m: 69cdc937d385e3b94310f755.jsonl[1450] _id=69ea74161724f0c9e2fb54ff ts=2026-04-21T19:59:29.545Z -> 69cdc937d385e3b94310f755.jsonl[1464] _id=69ea74191724f0c9e2fb550f ts=2026-04-23T19:33:45.2490000Z; 47h 0m: 69cdc937d385e3b94310f755.jsonl[256] _id=69dd4d6d7957a33870f2bc1d ts=2026-04-13T20:09:15.5960000Z -> 69cdc937d385e3b94310f755.jsonl[1828] _id=69dfe2647957a33870f4671d ts=2026-04-15T19:09:23.2820000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f755.jsonl[71] _id=69dd468e7957a33870f2a2dd ts=2026-04-13T19:39:56.8180000Z -> 69cdc937d385e3b94310f755.jsonl[69] _id=69dd468e7957a33870f2a2df ts=2026-04-13T19:39:56.8210000Z; 5ms: 69cdc937d385e3b94310f755.jsonl[3138] _id=69ea75531724f0c9e2fb5731 ts=2026-04-23T19:38:59.1460000Z -> 69cdc937d385e3b94310f755.jsonl[1490] _id=69ea75531724f0c9e2fb5733 ts=2026-04-23T19:38:59.1510000Z; 5ms: 69cdc937d385e3b94310f755.jsonl[3184] _id=69ea77661724f0c9e2fb5cbb ts=2026-04-23T19:47:50.1930000Z -> 69cdc937d385e3b94310f755.jsonl[1598] _id=69ea77671724f0c9e2fb5cbe ts=2026-04-23T19:47:50.1980000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc937d385e3b94310f755.jsonl:69cdc937d385e3b94310f755, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f755.jsonl[1818] _id=69dd4be77957a33870f2b6bd ts=2026-04-13T20:02:46.6850000Z`; `69cdc937d385e3b94310f755.jsonl[1863] _id=69dfe4127957a33870f46c7d ts=2026-04-15T19:16:33.4510000Z`; `69cdc937d385e3b94310f755.jsonl[355] _id=69dfe6777957a33870f4768b ts=2026-04-15T19:26:46.6840000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 22 record(s) match the trigger in 69cdc937d385e3b94310f755.jsonl:69cdc937d385e3b94310f755, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f755.jsonl[323] _id=69dfe5577957a33870f47183 ts=2026-04-15T19:21:58.2360000Z`; `69cdc937d385e3b94310f755.jsonl[1903] _id=69dfe5587957a33870f47189 ts=2026-04-15T19:21:59.4330000Z`; `69cdc937d385e3b94310f755.jsonl[1976] _id=69dfe7ab7957a33870f47b4b ts=2026-04-15T19:31:54.8950000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f755.jsonl[2122] _id=69dfed597957a33870f4912b ts=2026-04-15T19:56:08.3670000Z`; `69cdc937d385e3b94310f755.jsonl[2377] _id=69e284971724f0c9e2f79b7a ts=2026-04-17T19:05:58.4130000Z`; `69cdc937d385e3b94310f755.jsonl[707] _id=69e285131724f0c9e2f79da4 ts=2026-04-17T19:08:02.3660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f755.jsonl[2498] _id=69e287ca1724f0c9e2f7a83e ts=2026-04-17T19:19:36.9670000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f755.jsonl[959] _id=69ea73ee1724f0c9e2fb5107 ts=2026-04-21T19:33:05.334Z`; `69cdc937d385e3b94310f755.jsonl[3117] _id=69ea73ee1724f0c9e2fb5109 ts=2026-04-21T19:33:05.336Z`; `69cdc937d385e3b94310f755.jsonl[3119] _id=69ea73ee1724f0c9e2fb5113 ts=2026-04-21T19:33:15.864Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f755.jsonl[620] _id=69e2822f1724f0c9e2f7924c ts=2026-04-17T18:55:42.9850000Z`; `69cdc937d385e3b94310f755.jsonl[1071] _id=69ea74081724f0c9e2fb53a9 ts=2026-04-21T19:53:49.244Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f755.jsonl[1585] _id=69ea77121724f0c9e2fb5beb ts=2026-04-23T19:46:26.1790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 213 unmatched 'DialogueStartEvent' (totals: 448 start, 240 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationSessionOpen' (totals: 8 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 14 open, 22 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 52 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.96s, min -172808.33s, max -0.31s over 3215 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f755\coverage.yaml

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
  - Observed: 24 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2339 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (801); Unit 4 Dev (356); Unit 3 Dev (300); Unit 4 Dev - Anderson Base (205); Unit 1 Dev (183); Unit 5 Dev (175); Unit 3 Dungeon Dev (152); Unit 4 Dev - Dungeon (146); Unit 5 Dev - Dungeon (21)
- **eventKey:** present on 1651 of 2339 records
- **Intervals:** median 1.67s (p5 0.01s / p95 26.66s, n=2338)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1651; [conversationId, dialogueEventType] x688
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2339/2339 records)
    numeric range 8 .. 109 (49 unique)
data.dialogueEventType  (string, 2339/2339 records)
    "DialogueNodeEvent"  x1651
    "DialogueStartEvent"  x448
    "DialogueFinishEvent"  x240
data.nodeId  (number, 1651/2339 records)
    numeric range 0 .. 290 (222 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 516 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (185); Unit 3 Dev (59); Unit 4 Dev - Dungeon (56); Unit 3 Dungeon Dev (55); Unit 4 Dev (53); Unit 1 Dev (41); Unit 4 Dev - Anderson Base (28); Unit 5 Dev (21); Unit 5 Dev - Dungeon (18)
- **Intervals:** median 30.00s (p5 29.96s / p95 33.11s, n=501)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 516/516 records)
data.position.x  (number, 516/516 records)
    numeric range -594.858 .. 1555.82 (309 unique)
data.position.y  (number, 516/516 records)
    numeric range -112.488 .. 221.286 (245 unique)
data.position.z  (number, 516/516 records)
    numeric range -1107.55 .. 2169.34 (309 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 90 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 4 Dev - Dungeon (14); Unit 1 Dev (12); Unit 4 Dev (12); Unit 3 Dev (9); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 90 of 90 records
- **Intervals:** median 125.76s (p5 0.01s / p95 1048.40s, n=89)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 90/90 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x38
data.questID  (string, 90/90 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 90/90 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/90 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 63 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (63)
- **Intervals:** median 4.41s (p5 0.66s / p95 56.77s, n=62)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 63/63 records)
    "ChangeCanister"  x63
data.canisterType  (string, 63/63 records)
    "Bedrock"  x36
    "Clay"  x22
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 63/63 records)
    "5"  x46
    "3"  x13
    "4"  x4
data.machine  (string, 63/63 records)
    "1"  x61
    "2"  x2
data.row  (string, 63/63 records)
    "TopRow"  x34
    "BottomRow"  x29
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 60 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (60)
- **Intervals:** median 2.12s (p5 0.27s / p95 16.91s, n=59)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "On"  x36
    "Off"  x24
data.floor  (string, 60/60 records)
    "3"  x29
    "4"  x25
    "1"  x3
    "2"  x3
data.machineNumber  (string, 60/60 records)
    "One"  x59
    "Two"  x1
data.machineType  (string, 60/60 records)
    "Condenser"  x36
    "DualChamber_Evaporator"  x8
    "Evaporator"  x8
    "DualChamber_Condenser"  x6
    "VentSwitch"  x2
data.room  (string, 60/60 records)
    "2"  x31
    "3"  x23
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 36 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 4 Dev - Anderson Base (10); Unit 5 Dev (4); Unit 3 Dev (2)
- **Intervals:** median 3.03s (p5 0.03s / p95 169613.13s, n=35)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "argumentationToolClose"  x22
    "argumentationToolOpen"  x14
data.argumentationTitle  (string, 36/36 records)
    "Unit 2 – Watershed"  x20
    "Unit 4 - Flooding"  x10
    "Unit 5"  x4
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 36/36 records)
    "BackingInfoPanel - Waterfall Data"  x12
    "BackingInfoPanel - Soil Flow Rates"  x10
    "BackingInfoPanel - Watershed Graph"  x8
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationNodeEvent` — 27 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (9); Unit 1 Dev (8)
- **Intervals:** median 9.84s (p5 2.43s / p95 126648.07s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "argumentationNodeAdd"  x21
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 27/27 records)
    "Unit 2 – Watershed"  x10
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 27/27 records)
    "A"  x7
    "1"  x4
    "3"  x4
    "I"  x4
    "D"  x3
    "II"  x3
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 24 records

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (10)
- **Intervals:** median 17.59s (p5 5.84s / p95 1105.43s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "MapCloseEvent"  x12
    "MapOpenEvent"  x12
data.featureUsed  (string, 24/24 records)
    "Map"  x24
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 22 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (12); Unit 2 Prod (Refactor) (10)
- **Intervals:** median 3.21s (p5 1.20s / p95 595.46s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "dragEnd"  x11
    "dragStart"  x11
data.featureUsed  (string, 22/22 records)
    "waypoint"  x22
data.location  (object, 22/22 records)
data.location.x  (number, 22/22 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 22/22 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 22/22 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (2)
- **Intervals:** median 124.61s (p5 15.08s / p95 243142.23s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionOpen"  x8
    "argumentationSessionClose"  x6
data.argumentationDescription  (string, 14/14 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 12 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 149.16s (p5 2.86s / p95 170717.61s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/12 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/12 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 4 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 172473.42s (p5 1354.03s / p95 344515.84s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "4"  x2
    "1"  x1
    "2"  x1
    "3"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 13.28s (p5 9.67s / p95 697.97s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "cameraPlaced"  x6
data.boxId  (string, 6/6 records)
    "2"  x6
data.soilType  (string, 6/6 records)
    "None"  x6
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

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
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TerasGardenBox` data.soilType: "None" (6x)
- `TopographicMapEvent` data.actionType: "dragStart" (11x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)
- `soilMachine` data.canisterType: "Bedrock" (36x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*