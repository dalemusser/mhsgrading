# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f727

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f727
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f727.jsonl
- **Records:** 2930 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f727
- **Time span:** 2026-04-13T17:57:36.676000+00:00 .. 2026-04-23T18:39:49.404000+00:00 (240h 42m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f727\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2930 records, 9 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 61 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 2040 | 69.62 | 1 | 9 | 1421 | 2026-04-13T17:57:54.768000+00:00 | 2026-04-23T18:39:49.404000+00:00 | 240h 41m |
| PlayerPositionEvent | 602 | 20.55 | 1 | 9 | 0 | 2026-04-13T17:57:36.676000+00:00 | 2026-04-23T18:39:37.072000+00:00 | 240h 42m |
| questEvent | 84 | 2.87 | 1 | 9 | 84 | 2026-04-13T17:57:54.747000+00:00 | 2026-04-23T18:39:03.459000+00:00 | 240h 41m |
| WaterChamberEvent | 59 | 2.01 | 1 | 1 | 0 | 2026-04-23T18:28:33.251000+00:00 | 2026-04-23T18:33:48.669000+00:00 | 5m 15s |
| Topographic Map Event | 52 | 1.77 | 1 | 2 | 0 | 2026-04-13T18:23:29.380000+00:00 | 2026-04-21T18:03:50.159000+00:00 | 191h 40m |
| argumentationNodeEvent | 26 | 0.89 | 1 | 3 | 0 | 2026-04-13T18:16:31.859000+00:00 | 2026-04-17T18:36:39.631000+00:00 | 96h 20m |
| soilMachine | 18 | 0.61 | 1 | 1 | 0 | 2026-04-21T18:31:04.389000+00:00 | 2026-04-21T18:36:49.149000+00:00 | 5m 44s |
| argumentationEvent | 12 | 0.41 | 1 | 5 | 0 | 2026-04-13T18:16:22.040000+00:00 | 2026-04-23T18:38:48.943000+00:00 | 240h 22m |
| TerasGardenBox | 10 | 0.34 | 1 | 1 | 0 | 2026-04-23T18:17:37.817000+00:00 | 2026-04-23T18:18:38.618000+00:00 | 1m 0s |
| argumentationToolEvent | 10 | 0.34 | 1 | 2 | 0 | 2026-04-17T17:06:27.619000+00:00 | 2026-04-23T18:13:10.829000+00:00 | 145h 6m |
| Soil Key Puzzle | 8 | 0.27 | 1 | 3 | 0 | 2026-04-13T18:31:47.587000+00:00 | 2026-04-21T18:16:20.240000+00:00 | 191h 44m |
| TopographicMapEvent | 5 | 0.17 | 1 | 1 | 0 | 2026-04-13T18:39:45.218000+00:00 | 2026-04-15T17:50:03.002000+00:00 | 47h 10m |
| EndOfUnit | 4 | 0.14 | 1 | 4 | 0 | 2026-04-13T18:22:26.427000+00:00 | 2026-04-23T18:24:09.164000+00:00 | 240h 1m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 343351.037s median 
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
  - Observed: 114.621s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.748s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.867s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 1.692s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 137.211s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 10.55s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.499s median 
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
  - Observed: 5.648s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
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
  - Observed: 52 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 26 records 
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
  - Observed: 2; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f727.jsonl[35] _id=69dd339e7957a33870f26f40 ts=2026-04-13T18:19:09.6700000Z`; `69cdc907d385e3b94310f727.jsonl[1098] _id=69dfd0987957a33870f4162b ts=2026-04-15T17:53:28.0180000Z`; `69cdc907d385e3b94310f727.jsonl[1526] _id=69e2689c1724f0c9e2f735ae ts=2026-04-17T17:06:35.2680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:25' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc907d385e3b94310f727.jsonl[1417] _id=69e265ee1724f0c9e2f7201a ts=2026-04-17T16:55:09.4700000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 52 records, TopographicMapEvent: 5 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 6 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2039 | 0.0 | 2.313 | 424.97 | 32.2 | 339424.003 | 0.14 | 530 | 7 |
| PlayerPositionEvent | 590 | 29.746 | 30.005 | 1468.106 | 33.542 | 339360.781 | 0.04 | 0 | 5 |
| questEvent | 83 | 0.002 | 130.422 | 10439.382 | 2738.86 | 339427.249 | 0.01 | 14 | 9 |
| WaterChamberEvent | 58 | 0.165 | 1.692 | 5.438 | 21.678 | 30.956 | 11.03 | 0 | 0 |
| Topographic Map Event | 51 | 0.448 | 17.608 | 13529.819 | 85338.019 | 344677.271 | 0.0 | 0 | 7 |
| argumentationNodeEvent | 25 | 1.087 | 10.55 | 13872.311 | 3019.286 | 341215.04 | 0.0 | 0 | 3 |
| soilMachine | 17 | 0.632 | 5.648 | 20.28 | 86.475 | 134.409 | 2.96 | 0 | 0 |
| argumentationEvent | 11 | 0.125 | 137.211 | 78667.9 | 429018.358 | 516848.95 | 0.0 | 0 | 5 |
| TerasGardenBox | 9 | 1.067 | 1.748 | 6.756 | 16.909 | 16.917 | 8.88 | 0 | 0 |
| argumentationToolEvent | 9 | 0.002 | 1.499 | 58044.801 | 313407.904 | 522251.254 | 0.0 | 1 | 1 |
| Soil Key Puzzle | 7 | 2.894 | 114.621 | 98610.379 | 411310.146 | 514070.41 | 0.0 | 0 | 3 |
| TopographicMapEvent | 4 | 0.381 | 5.867 | 42454.446 | 144335.858 | 169805.668 | 0.0 | 0 | 1 |
| EndOfUnit | 3 | 173702.759 | 343351.037 | 288034.246 | 346679.151 | 347048.941 | 0.0 | 0 | 3 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.95s, p95 33.54s, n=590) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 18 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `194ms: 69cdc907d385e3b94310f727.jsonl[2799] _id=69ea64e81724f0c9e2fb392b ts=2026-04-23T18:28:55.8830000Z ~ 69cdc907d385e3b94310f727.jsonl[2800] _id=69ea64e81724f0c9e2fb392d ts=2026-04-23T18:28:56.0770000Z`; `704ms: 69cdc907d385e3b94310f727.jsonl[581] _id=69ea64e71724f0c9e2fb3927 ts=2026-04-23T18:28:55.5790000Z ~ 69cdc907d385e3b94310f727.jsonl[582] _id=69ea64e91724f0c9e2fb392f ts=2026-04-23T18:28:56.2830000Z`; `470ms: 69cdc907d385e3b94310f727.jsonl[582] _id=69ea64e91724f0c9e2fb392f ts=2026-04-23T18:28:56.2830000Z ~ 69cdc907d385e3b94310f727.jsonl[2797] _id=69ea64e91724f0c9e2fb3931 ts=2026-04-23T18:28:56.7530000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `125ms: 69cdc907d385e3b94310f727.jsonl[1923] _id=69e27dba1724f0c9e2f78800 ts=2026-04-17T18:36:41.4030000Z ~ 69cdc907d385e3b94310f727.jsonl[355] _id=69e27dba1724f0c9e2f7880e ts=2026-04-17T18:36:41.5280000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc907d385e3b94310f727.jsonl[521] _id=69ea60a61724f0c9e2fb16f1 ts=2026-04-23T18:10:46.4490000Z ~ 69cdc907d385e3b94310f727.jsonl[2559] _id=69ea60a61724f0c9e2fb16f5 ts=2026-04-23T18:10:46.4510000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 69cdc907d385e3b94310f727.jsonl[1417] _id=69e265ee1724f0c9e2f7201a ts=2026-04-17T16:55:09.4700000Z ~ 69cdc907d385e3b94310f727.jsonl[226] _id=69e265ef1724f0c9e2f72028 ts=2026-04-17T16:55:09.4760000Z`; `7ms: 69cdc907d385e3b94310f727.jsonl[2913] _id=69ea67471724f0c9e2fb4b79 ts=2026-04-23T18:39:03.4520000Z ~ 69cdc907d385e3b94310f727.jsonl[2915] _id=69ea67481724f0c9e2fb4b82 ts=2026-04-23T18:39:03.4590000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `632ms: 69cdc907d385e3b94310f727.jsonl[2407] _id=69e7c35b1724f0c9e2f99dfb ts=2026-04-21T18:35:06.6550000Z ~ 69cdc907d385e3b94310f727.jsonl[2412] _id=69e7c35b1724f0c9e2f99dfd ts=2026-04-21T18:35:07.2870000Z`; `920ms: 69cdc907d385e3b94310f727.jsonl[2415] _id=69e7c3821724f0c9e2f99f21 ts=2026-04-21T18:35:46.0900000Z ~ 69cdc907d385e3b94310f727.jsonl[2416] _id=69e7c3831724f0c9e2f99f27 ts=2026-04-21T18:35:47.0100000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 17m 
  - Evidence: 94h 17m: 69cdc907d385e3b94310f727.jsonl[1946] _id=69e27e431724f0c9e2f78bb4 ts=2026-04-17T18:38:59.0270000Z -> 69cdc907d385e3b94310f727.jsonl[1954] _id=69e7ac231724f0c9e2f91651 ts=2026-04-21T16:56:03.0300000Z; 47h 20m: 69cdc907d385e3b94310f727.jsonl[2458] _id=69e7c47b1724f0c9e2f9a6ed ts=2026-04-21T18:39:54.6620000Z -> 69cdc907d385e3b94310f727.jsonl[2466] _id=69ea5e511724f0c9e2fb0517 ts=2026-04-23T18:00:49.2300000Z; 47h 1m: 69cdc907d385e3b94310f727.jsonl[1004] _id=69dd38c17957a33870f291ac ts=2026-04-13T18:41:05.4240000Z -> 69cdc907d385e3b94310f727.jsonl[1017] _id=69dfce087957a33870f40adb ts=2026-04-15T17:42:32.2820000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 530 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f727.jsonl[1646] _id=69e2719a1724f0c9e2f747be ts=2026-04-17T17:44:57.4780000Z -> 69cdc907d385e3b94310f727.jsonl[1648] _id=69e271a91724f0c9e2f74834 ts=2026-04-17T17:44:57.478Z; 0ms: 69cdc907d385e3b94310f727.jsonl[576] _id=69ea63c91724f0c9e2fb30c7 ts=2026-04-23T18:24:09.1840000Z -> 69cdc907d385e3b94310f727.jsonl[2770] _id=69ea63d71724f0c9e2fb311f ts=2026-04-23T18:24:09.184Z; 2ms: 69cdc907d385e3b94310f727.jsonl[1526] _id=69e2689c1724f0c9e2f735ae ts=2026-04-17T17:06:35.2680000Z -> 69cdc907d385e3b94310f727.jsonl[257] _id=69e2689c1724f0c9e2f735b2 ts=2026-04-17T17:06:35.2700000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 24m 
  - Evidence: 96h 24m: 69cdc907d385e3b94310f727.jsonl[1645] _id=69e2719a1724f0c9e2f747bc ts=2026-04-17T17:44:57.4640000Z -> 69cdc907d385e3b94310f727.jsonl[2248] _id=69e7bd421724f0c9e2f96fcf ts=2026-04-21T18:09:06.4050000Z; 95h 22m: 69cdc907d385e3b94310f727.jsonl[855] _id=69dd34627957a33870f27436 ts=2026-04-13T18:22:26.4270000Z -> 69cdc907d385e3b94310f727.jsonl[1645] _id=69e2719a1724f0c9e2f747bc ts=2026-04-17T17:44:57.4640000Z; 48h 15m: 69cdc907d385e3b94310f727.jsonl[2248] _id=69e7bd421724f0c9e2f96fcf ts=2026-04-21T18:09:06.4050000Z -> 69cdc907d385e3b94310f727.jsonl[2769] _id=69ea63c91724f0c9e2fb30c1 ts=2026-04-23T18:24:09.1640000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f727.jsonl[1948] _id=69e27e731724f0c9e2f78cae ts=2026-04-17T18:39:46.5040000Z -> 69cdc907d385e3b94310f727.jsonl[1953] _id=69e7ac141724f0c9e2f91633 ts=2026-04-21T16:55:47.2850000Z; 47h 20m: 69cdc907d385e3b94310f727.jsonl[2459] _id=69e7c47d1724f0c9e2f9a6ff ts=2026-04-21T18:39:56.9890000Z -> 69cdc907d385e3b94310f727.jsonl[2461] _id=69ea5e461724f0c9e2fb04dd ts=2026-04-23T18:00:37.8480000Z; 47h 1m: 69cdc907d385e3b94310f727.jsonl[73] _id=69dd38ae7957a33870f2916c ts=2026-04-13T18:40:46.0460000Z -> 69cdc907d385e3b94310f727.jsonl[1015] _id=69dfce057957a33870f40ad7 ts=2026-04-15T17:42:28.3270000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 142h 47m 
  - Evidence: 142h 47m: 69cdc907d385e3b94310f727.jsonl[1194] _id=69dfd5197957a33870f435d3 ts=2026-04-15T18:12:41.2970000Z -> 69cdc907d385e3b94310f727.jsonl[1984] _id=69e7ad301724f0c9e2f91c1b ts=2026-04-21T17:00:31.7070000Z; 47h 38m: 69cdc907d385e3b94310f727.jsonl[919] _id=69dd36967957a33870f2834a ts=2026-04-13T18:31:50.4810000Z -> 69cdc907d385e3b94310f727.jsonl[144] _id=69dfd4a77957a33870f433b3 ts=2026-04-15T18:10:46.6760000Z; 1h 15m: 69cdc907d385e3b94310f727.jsonl[1986] _id=69e7ad421724f0c9e2f91c9b ts=2026-04-21T17:00:50.1440000Z -> 69cdc907d385e3b94310f727.jsonl[2277] _id=69e7bed81724f0c9e2f97a85 ts=2026-04-21T18:15:52.3490000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 44m 
  - Evidence: 95h 44m: 69cdc907d385e3b94310f727.jsonl[1809] _id=69e2791b1724f0c9e2f773e6 ts=2026-04-17T18:16:58.7510000Z -> 69cdc907d385e3b94310f727.jsonl[2179] _id=69e7bb801724f0c9e2f9634d ts=2026-04-21T18:01:36.0220000Z; 47h 29m: 69cdc907d385e3b94310f727.jsonl[206] _id=69dfd9537957a33870f451d9 ts=2026-04-15T18:30:43.6110000Z -> 69cdc907d385e3b94310f727.jsonl[1735] _id=69e275431724f0c9e2f7601e ts=2026-04-17T18:00:34.7720000Z; 47h 9m: 69cdc907d385e3b94310f727.jsonl[994] _id=69dd38807957a33870f29050 ts=2026-04-13T18:39:59.9230000Z -> 69cdc907d385e3b94310f727.jsonl[128] _id=69dfcfc27957a33870f410ab ts=2026-04-15T17:49:53.9370000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 10m 
  - Evidence: 47h 10m: 69cdc907d385e3b94310f727.jsonl[71] _id=69dd387d7957a33870f29034 ts=2026-04-13T18:39:57.3340000Z -> 69cdc907d385e3b94310f727.jsonl[1074] _id=69dfcfcb7957a33870f410d5 ts=2026-04-15T17:50:03.0020000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 34m 
  - Evidence: 143h 34m: 69cdc907d385e3b94310f727.jsonl[355] _id=69e27dba1724f0c9e2f7880e ts=2026-04-17T18:36:41.5280000Z -> 69cdc907d385e3b94310f727.jsonl[519] _id=69ea60aa1724f0c9e2fb170b ts=2026-04-23T18:10:50.4780000Z; 94h 46m: 69cdc907d385e3b94310f727.jsonl[820] _id=69dd339e7957a33870f26f3c ts=2026-04-13T18:19:09.6460000Z -> 69cdc907d385e3b94310f727.jsonl[251] _id=69e268621724f0c9e2f733f4 ts=2026-04-17T17:05:37.4130000Z; 54m 12s: 69cdc907d385e3b94310f727.jsonl[277] _id=69e270cf1724f0c9e2f741d0 ts=2026-04-17T17:41:35.1080000Z -> 69cdc907d385e3b94310f727.jsonl[351] _id=69e27d841724f0c9e2f7868c ts=2026-04-17T18:35:47.4360000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc907d385e3b94310f727.jsonl[819] _id=69dd339a7957a33870f26f2c ts=2026-04-13T18:19:06.5700000Z -> 69cdc907d385e3b94310f727.jsonl[254] _id=69e2687a1724f0c9e2f734a6 ts=2026-04-17T17:06:01.6100000Z; 54m 26s: 69cdc907d385e3b94310f727.jsonl[1594] _id=69e270ce1724f0c9e2f741c4 ts=2026-04-17T17:41:33.6860000Z -> 69cdc907d385e3b94310f727.jsonl[1912] _id=69e27d901724f0c9e2f786ea ts=2026-04-17T18:36:00.0620000Z; 33m 50s: 69cdc907d385e3b94310f727.jsonl[1528] _id=69e268ac1724f0c9e2f7364c ts=2026-04-17T17:06:51.4470000Z -> 69cdc907d385e3b94310f727.jsonl[274] _id=69e2709b1724f0c9e2f74054 ts=2026-04-17T17:40:42.3720000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 145h 4m 
  - Evidence: 145h 4m: 69cdc907d385e3b94310f727.jsonl[1525] _id=69e2689b1724f0c9e2f735a8 ts=2026-04-17T17:06:35.1950000Z -> 69cdc907d385e3b94310f727.jsonl[521] _id=69ea60a61724f0c9e2fb16f1 ts=2026-04-23T18:10:46.4490000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f727.jsonl[521] _id=69ea60a61724f0c9e2fb16f1 ts=2026-04-23T18:10:46.4490000Z -> 69cdc907d385e3b94310f727.jsonl[2559] _id=69ea60a61724f0c9e2fb16f5 ts=2026-04-23T18:10:46.4510000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 17m 
  - Evidence: 94h 17m: 69cdc907d385e3b94310f727.jsonl[1944] _id=69e27e331724f0c9e2f78b48 ts=2026-04-17T18:38:43.1480000Z -> 69cdc907d385e3b94310f727.jsonl[1952] _id=69e7ac171724f0c9e2f9163f ts=2026-04-21T16:55:50.3970000Z; 47h 20m: 69cdc907d385e3b94310f727.jsonl[2460] _id=69e7c47b1724f0c9e2f9a6e9 ts=2026-04-21T18:39:54.6450000Z -> 69cdc907d385e3b94310f727.jsonl[2462] _id=69ea5e471724f0c9e2fb04df ts=2026-04-23T18:00:38.9160000Z; 47h 4m: 69cdc907d385e3b94310f727.jsonl[989] _id=69dd380c7957a33870f28cd2 ts=2026-04-13T18:38:04.2230000Z -> 69cdc907d385e3b94310f727.jsonl[1016] _id=69dfce077957a33870f40ad9 ts=2026-04-15T17:42:30.8830000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f727.jsonl[27] _id=69dd329f7957a33870f267f4 ts=2026-04-13T18:14:54.9680000Z -> 69cdc907d385e3b94310f727.jsonl[29] _id=69dd329f7957a33870f267f8 ts=2026-04-13T18:14:54.9700000Z; 6ms: 69cdc907d385e3b94310f727.jsonl[1417] _id=69e265ee1724f0c9e2f7201a ts=2026-04-17T16:55:09.4700000Z -> 69cdc907d385e3b94310f727.jsonl[226] _id=69e265ef1724f0c9e2f72028 ts=2026-04-17T16:55:09.4760000Z; 6ms: 69cdc907d385e3b94310f727.jsonl[2824] _id=69ea658a1724f0c9e2fb3dd3 ts=2026-04-23T18:31:37.9180000Z -> 69cdc907d385e3b94310f727.jsonl[609] _id=69ea658a1724f0c9e2fb3dd5 ts=2026-04-23T18:31:37.9240000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f727.jsonl:69cdc907d385e3b94310f727, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f727.jsonl[919] _id=69dd36967957a33870f2834a ts=2026-04-13T18:31:50.4810000Z`; `69cdc907d385e3b94310f727.jsonl[1194] _id=69dfd5197957a33870f435d3 ts=2026-04-15T18:12:41.2970000Z`; `69cdc907d385e3b94310f727.jsonl[1986] _id=69e7ad421724f0c9e2f91c9b ts=2026-04-21T17:00:50.1440000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc907d385e3b94310f727.jsonl:69cdc907d385e3b94310f727, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f727.jsonl[998] _id=69dd38717957a33870f28fd2 ts=2026-04-13T18:39:45.2180000Z`; `69cdc907d385e3b94310f727.jsonl[997] _id=69dd38717957a33870f28fd6 ts=2026-04-13T18:39:45.5990000Z`; `69cdc907d385e3b94310f727.jsonl[1001] _id=69dd38787957a33870f29012 ts=2026-04-13T18:39:52.5350000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f727.jsonl[1302] _id=69dfd8337957a33870f448d7 ts=2026-04-15T18:25:55.3430000Z`; `69cdc907d385e3b94310f727.jsonl[1700] _id=69e273f71724f0c9e2f7577a ts=2026-04-17T17:55:03.0920000Z`; `69cdc907d385e3b94310f727.jsonl[1727] _id=69e274a21724f0c9e2f75ba8 ts=2026-04-17T17:57:53.2710000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f727.jsonl[355] _id=69e27dba1724f0c9e2f7880e ts=2026-04-17T18:36:41.5280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f727.jsonl[521] _id=69ea60a61724f0c9e2fb16f1 ts=2026-04-23T18:10:46.4490000Z`; `69cdc907d385e3b94310f727.jsonl[2559] _id=69ea60a61724f0c9e2fb16f5 ts=2026-04-23T18:10:46.4510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc907d385e3b94310f727.jsonl[1949] _id=69e7ac291724f0c9e2f9165f ts=2026-04-21T16:56:09.4180000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 211 unmatched 'DialogueStartEvent' (totals: 413 start, 206 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 50 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.43s, min -15.86s, max +0.04s over 2930 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f727\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
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
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 52 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2040 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (704); Unit 3 Dev (383); Unit 4 Dev (244); Unit 1 Dev (174); Unit 3 Dungeon Dev (165); Unit 4 Dev - Anderson Base (122); Unit 5 Dev (112); Unit 4 Dev - Dungeon (105); Unit 5 Dev - Dungeon (31)
- **eventKey:** present on 1421 of 2040 records
- **Intervals:** median 2.31s (p5 0.01s / p95 32.20s, n=2039)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1421; [conversationId, dialogueEventType] x619
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2040/2040 records)
    numeric range 8 .. 114 (48 unique)
data.dialogueEventType  (string, 2040/2040 records)
    "DialogueNodeEvent"  x1421
    "DialogueStartEvent"  x413
    "DialogueFinishEvent"  x206
data.nodeId  (number, 1421/2040 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 602 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (244); Unit 3 Dev (120); Unit 4 Dev (55); Unit 3 Dungeon Dev (51); Unit 1 Dev (50); Unit 4 Dev - Dungeon (33); Unit 5 Dev - Dungeon (19); Unit 4 Dev - Anderson Base (18); Unit 5 Dev (12)
- **Intervals:** median 30.00s (p5 29.95s / p95 33.54s, n=590)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 602/602 records)
data.position.x  (number, 602/602 records)
    numeric range -687.486 .. 1647 (286 unique)
data.position.y  (number, 602/602 records)
    numeric range -115.127 .. 217.708 (241 unique)
data.position.z  (number, 602/602 records)
    numeric range -1106.44 .. 2308.91 (286 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (14); Unit 1 Dev (12); Unit 4 Dev - Dungeon (12); Unit 4 Dev (11); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (4); Unit 5 Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 130.42s (p5 0.01s / p95 2738.86s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x34
data.questID  (string, 84/84 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/84 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 59 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (59)
- **Intervals:** median 1.69s (p5 0.21s / p95 21.68s, n=58)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 59/59 records)
    "On"  x36
    "Off"  x23
data.floor  (string, 59/59 records)
    "1"  x26
    "4"  x19
    "3"  x11
    "2"  x3
data.machineNumber  (string, 59/59 records)
    "One"  x58
    "Two"  x1
data.machineType  (string, 59/59 records)
    "Condenser"  x45
    "Evaporator"  x10
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
    "DualChamber_Evaporator"  x1
data.room  (string, 59/59 records)
    "3"  x42
    "2"  x9
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Topographic Map Event` — 52 records

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 3 Dev (20)
- **Intervals:** median 17.61s (p5 1.27s / p95 85338.02s, n=51)
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "MapCloseEvent"  x26
    "MapOpenEvent"  x26
data.featureUsed  (string, 52/52 records)
    "Map"  x52
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 26 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (6); Unit 3 Dev (5)
- **Intervals:** median 10.55s (p5 1.30s / p95 3019.29s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "argumentationNodeAdd"  x19
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 26/26 records)
    "Unit 2 – Watershed"  x15
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 26/26 records)
    "I"  x7
    "1"  x3
    "A"  x3
    "B"  x3
    "II"  x3
    "3"  x2
    "C"  x2
    "D"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 18 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (18)
- **Intervals:** median 5.65s (p5 0.86s / p95 86.47s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "ChangeCanister"  x18
data.canisterType  (string, 18/18 records)
    "Clay"  x10
    "Bedrock"  x5
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 18/18 records)
    "5"  x16
    "3"  x1
    "4"  x1
data.machine  (string, 18/18 records)
    "1"  x17
    "2"  x1
data.row  (string, 18/18 records)
    "BottomRow"  x9
    "TopRow"  x9
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 137.21s (p5 17.24s / p95 429018.36s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 1.75s (p5 1.07s / p95 16.91s, n=9)
- **`data` key-set variants:** [actionType, boxID, soilType] x6; [actionType, boxId, soilType] x4
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "soilSelected"  x6
    "cameraPlaced"  x4
data.boxID  (string, 6/10 records)
    "0"  x4
    "1"  x1
    "2"  x1
data.boxId  (string, 4/10 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 10/10 records)
    "Sand"  x5
    "Clay"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev - Anderson Base (4)
- **Intervals:** median 1.50s (p5 0.02s / p95 313407.90s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x4
data.argumentationTitle  (string, 10/10 records)
    "Unit 2 – Watershed"  x6
    "Unit 4 - Flooding"  x4
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - Soil Flow Rates"  x2
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
    "BackingInfoPanel - Waterfall Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 114.62s (p5 7.56s / p95 411310.15s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 5 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (5)
- **Intervals:** median 5.87s (p5 1.04s / p95 144335.86s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "dragStart"  x3
    "dragEnd"  x2
data.featureUsed  (string, 5/5 records)
    "waypoint"  x5
data.location  (object, 5/5 records)
data.location.x  (number, 5/5 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/5 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/5 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 343351.04s (p5 190667.59s / p95 346679.15s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TopographicMapEvent` data.actionType: "dragStart" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*