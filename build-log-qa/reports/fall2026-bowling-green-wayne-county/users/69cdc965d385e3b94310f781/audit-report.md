# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f781

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f781
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f781.jsonl
- **Records:** 2727 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f781
- **Time span:** 2026-04-14T13:51:29.692000+00:00 .. 2026-04-24T14:35:43.585000+00:00 (240h 44m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f781\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2727 records, 9 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 61 INFO, 0 NOT_TESTED, 58 PASS.
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
| DialogueEvent | 1889 | 69.27 | 1 | 9 | 1300 | 2026-04-14T13:51:47.746000+00:00 | 2026-04-24T14:35:35.457000+00:00 | 240h 43m |
| PlayerPositionEvent | 542 | 19.88 | 1 | 9 | 0 | 2026-04-14T13:51:29.692000+00:00 | 2026-04-24T14:35:43.585000+00:00 | 240h 44m |
| questEvent | 70 | 2.57 | 1 | 9 | 70 | 2026-04-14T13:51:47.728000+00:00 | 2026-04-24T14:32:17.255000+00:00 | 240h 40m |
| Topographic Map Event | 44 | 1.61 | 1 | 2 | 0 | 2026-04-16T13:45:51.940000+00:00 | 2026-04-22T13:43:18.653000+00:00 | 143h 57m |
| WaterChamberEvent | 41 | 1.5 | 1 | 1 | 0 | 2026-04-24T14:24:20.963000+00:00 | 2026-04-24T14:30:45.185000+00:00 | 6m 24s |
| soilMachine | 34 | 1.25 | 1 | 1 | 0 | 2026-04-22T14:09:15.690000+00:00 | 2026-04-22T14:22:32.181000+00:00 | 13m 16s |
| TopographicMapEvent | 32 | 1.17 | 1 | 2 | 0 | 2026-04-16T13:50:47.307000+00:00 | 2026-04-22T13:43:17.550000+00:00 | 143h 52m |
| argumentationNodeEvent | 26 | 0.95 | 1 | 3 | 0 | 2026-04-14T14:10:24.573000+00:00 | 2026-04-20T14:18:48.991000+00:00 | 144h 8m |
| argumentationToolEvent | 14 | 0.51 | 1 | 1 | 0 | 2026-04-24T14:07:36.302000+00:00 | 2026-04-24T14:10:25.608000+00:00 | 2m 49s |
| argumentationEvent | 11 | 0.4 | 1 | 5 | 0 | 2026-04-14T14:10:15.245000+00:00 | 2026-04-24T14:34:45.886000+00:00 | 240h 24m |
| Soil Key Puzzle | 10 | 0.37 | 1 | 3 | 0 | 2026-04-14T14:30:30.561000+00:00 | 2026-04-22T13:57:59.161000+00:00 | 191h 27m |
| TerasGardenBox | 8 | 0.29 | 1 | 1 | 0 | 2026-04-24T14:14:53.112000+00:00 | 2026-04-24T14:15:33.152000+00:00 | 40.0s |
| EndOfUnit | 4 | 0.15 | 1 | 4 | 0 | 2026-04-14T14:15:41.441000+00:00 | 2026-04-24T14:20:19.570000+00:00 | 240h 4m |
| crash | 2 | 0.07 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 174772.063s median 
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
  - Observed: 56.82s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.76s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.236s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 138.503s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 11.489s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.934s median 
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
  - Observed: 3.449s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 10 records 
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
  - Observed: 44 records this build 
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
  - Observed: 2; 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 6.8x vs baseline. 
  - Observed: 34 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f781.jsonl[203] _id=69de4b5f7957a33870f34b79 ts=2026-04-14T14:12:46.2260000Z`; `69cdc965d385e3b94310f781.jsonl[547] _id=69e0ea147957a33870f51b0d ts=2026-04-16T13:54:27.6740000Z`; `69cdc965d385e3b94310f781.jsonl[1019] _id=69e62b571724f0c9e2f86029 ts=2026-04-20T13:34:14.2460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 44 records, TopographicMapEvent: 32 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 5 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1888 | 0.0 | 2.605 | 459.019 | 31.278 | 341002.91 | 0.13 | 516 | 4 |
| PlayerPositionEvent | 528 | 0.0 | 30.005 | 1639.901 | 33.555 | 341005.664 | 0.04 | 1 | 4 |
| questEvent | 69 | 0.002 | 155.527 | 12556.95 | 101812.844 | 341463.32 | 0.0 | 11 | 10 |
| Topographic Map Event | 43 | 0.928 | 27.255 | 12052.249 | 275.79 | 515318.055 | 0.0 | 0 | 1 |
| WaterChamberEvent | 40 | 0.682 | 4.236 | 9.606 | 30.097 | 40.846 | 6.25 | 0 | 0 |
| soilMachine | 33 | 0.273 | 3.449 | 24.136 | 119.088 | 248.259 | 2.49 | 0 | 0 |
| TopographicMapEvent | 31 | 1.596 | 6.76 | 16708.072 | 804.905 | 515358.061 | 0.0 | 0 | 3 |
| argumentationNodeEvent | 25 | 1.435 | 11.489 | 20756.177 | 1883.666 | 516184.606 | 0.0 | 0 | 2 |
| argumentationToolEvent | 13 | 0.003 | 1.934 | 13.024 | 53.05 | 94.211 | 4.61 | 3 | 0 |
| argumentationEvent | 10 | 0.109 | 138.503 | 86547.064 | 439113.467 | 516171.21 | 0.0 | 0 | 4 |
| Soil Key Puzzle | 9 | 3.011 | 56.82 | 76583.178 | 276452.836 | 346566.585 | 0.0 | 0 | 4 |
| TerasGardenBox | 7 | 1.101 | 2.904 | 5.72 | 14.5 | 16.157 | 10.49 | 0 | 0 |
| EndOfUnit | 3 | 173129.033 | 174772.063 | 288092.71 | 482216.536 | 516377.033 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.96s, p95 33.55s, n=528) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `109ms: 69cdc965d385e3b94310f781.jsonl[1562] _id=69e635ca1724f0c9e2f89e1b ts=2026-04-20T14:18:50.0720000Z ~ 69cdc965d385e3b94310f781.jsonl[1558] _id=69e635cb1724f0c9e2f89e23 ts=2026-04-20T14:18:50.1810000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 69cdc965d385e3b94310f781.jsonl[2289] _id=69eb79291724f0c9e2fb82a1 ts=2026-04-24T14:07:36.3020000Z ~ 69cdc965d385e3b94310f781.jsonl[2293] _id=69eb79291724f0c9e2fb82a3 ts=2026-04-24T14:07:36.3050000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `846ms: 69cdc965d385e3b94310f781.jsonl[2070] _id=69e8d8a31724f0c9e2fa66d1 ts=2026-04-22T14:18:11.1280000Z ~ 69cdc965d385e3b94310f781.jsonl[2071] _id=69e8d8a41724f0c9e2fa66d7 ts=2026-04-22T14:18:11.9740000Z`; `433ms: 69cdc965d385e3b94310f781.jsonl[2083] _id=69e8d8de1724f0c9e2fa6817 ts=2026-04-22T14:19:10.0280000Z ~ 69cdc965d385e3b94310f781.jsonl[2084] _id=69e8d8de1724f0c9e2fa6819 ts=2026-04-22T14:19:10.4610000Z`; `702ms: 69cdc965d385e3b94310f781.jsonl[2087] _id=69e8d9141724f0c9e2fa6947 ts=2026-04-22T14:20:04.2590000Z ~ 69cdc965d385e3b94310f781.jsonl[2089] _id=69e8d9151724f0c9e2fa6955 ts=2026-04-22T14:20:04.9610000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f781.jsonl[2691] _id=69e0f3b67957a33870f55905 ts=2026-04-16T14:35:33.1260000Z -> 69cdc965d385e3b94310f781.jsonl[899] _id=69e627c01724f0c9e2f84ba3 ts=2026-04-20T13:18:56.0360000Z; 47h 29m: 69cdc965d385e3b94310f781.jsonl[2159] _id=69e8db421724f0c9e2fa74af ts=2026-04-22T14:29:22.5060000Z -> 69cdc965d385e3b94310f781.jsonl[2166] _id=69eb77041724f0c9e2fb7755 ts=2026-04-24T13:58:27.5990000Z; 47h 2m: 69cdc965d385e3b94310f781.jsonl[345] _id=69de4fdb7957a33870f36ada ts=2026-04-14T14:31:54.1890000Z -> 69cdc965d385e3b94310f781.jsonl[349] _id=69e0e5577957a33870f4fa2f ts=2026-04-16T13:34:14.5100000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 516 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f781.jsonl[1142] _id=69e62d271724f0c9e2f86d73 ts=2026-04-20T13:41:58.4960000Z -> 69cdc965d385e3b94310f781.jsonl[1145] _id=69e62d5e1724f0c9e2f86e63 ts=2026-04-20T13:41:58.496Z; 0ms: 69cdc965d385e3b94310f781.jsonl[1877] _id=69e8d1701724f0c9e2fa3b8b ts=2026-04-22T13:47:27.5220000Z -> 69cdc965d385e3b94310f781.jsonl[1879] _id=69e8d1c61724f0c9e2fa3dd7 ts=2026-04-22T13:47:27.522Z; 2ms: 69cdc965d385e3b94310f781.jsonl[1651] _id=69e8caa91724f0c9e2fa0ded ts=2026-04-22T13:16:55.6350000Z -> 69cdc965d385e3b94310f781.jsonl[1648] _id=69e8caa91724f0c9e2fa0df3 ts=2026-04-22T13:16:55.6370000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 26m 
  - Evidence: 143h 26m: 69cdc965d385e3b94310f781.jsonl[2665] _id=69de4c0e7957a33870f35147 ts=2026-04-14T14:15:41.4410000Z -> 69cdc965d385e3b94310f781.jsonl[1141] _id=69e62d271724f0c9e2f86d71 ts=2026-04-20T13:41:58.4740000Z; 48h 32m: 69cdc965d385e3b94310f781.jsonl[1876] _id=69e8d1701724f0c9e2fa3b89 ts=2026-04-22T13:47:27.5070000Z -> 69cdc965d385e3b94310f781.jsonl[2520] _id=69eb7c231724f0c9e2fb9175 ts=2026-04-24T14:20:19.5700000Z; 48h 5m: 69cdc965d385e3b94310f781.jsonl[1141] _id=69e62d271724f0c9e2f86d71 ts=2026-04-20T13:41:58.4740000Z -> 69cdc965d385e3b94310f781.jsonl[1876] _id=69e8d1701724f0c9e2fa3b89 ts=2026-04-22T13:47:27.5070000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f781.jsonl[2689] _id=69e0f3a37957a33870f558cd ts=2026-04-16T14:35:14.6730000Z -> 69cdc965d385e3b94310f781.jsonl[897] _id=69e627b11724f0c9e2f84b55 ts=2026-04-20T13:18:40.3370000Z; 47h 28m: 69cdc965d385e3b94310f781.jsonl[2163] _id=69e8db3b1724f0c9e2fa74a3 ts=2026-04-22T14:29:14.6520000Z -> 69cdc965d385e3b94310f781.jsonl[2164] _id=69eb76d01724f0c9e2fb76b7 ts=2026-04-24T13:57:35.7780000Z; 47h 2m: 69cdc965d385e3b94310f781.jsonl[338] _id=69de4fd17957a33870f36ac2 ts=2026-04-14T14:31:44.9640000Z -> 69cdc965d385e3b94310f781.jsonl[346] _id=69e0e5537957a33870f4fa0f ts=2026-04-16T13:34:09.8980000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f781.jsonl[1655] _id=69e8caf81724f0c9e2fa0f77 ts=2026-04-22T13:19:51.3750000Z -> 69cdc965d385e3b94310f781.jsonl[1658] _id=69e8cc371724f0c9e2fa160d ts=2026-04-22T13:19:51.375Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 69cdc965d385e3b94310f781.jsonl[640] _id=69e0ece77957a33870f52a97 ts=2026-04-16T14:06:30.4920000Z -> 69cdc965d385e3b94310f781.jsonl[1606] _id=69e636ad1724f0c9e2f8a405 ts=2026-04-20T14:22:37.0770000Z; 47h 34m: 69cdc965d385e3b94310f781.jsonl[1610] _id=69e636c21724f0c9e2f8a4c9 ts=2026-04-20T14:22:58.3150000Z -> 69cdc965d385e3b94310f781.jsonl[1911] _id=69e8d3d51724f0c9e2fa467f ts=2026-04-22T13:57:40.5280000Z; 47h 9m: 69cdc965d385e3b94310f781.jsonl[328] _id=69de4f8a7957a33870f36944 ts=2026-04-14T14:30:33.5720000Z -> 69cdc965d385e3b94310f781.jsonl[404] _id=69e0e6b37957a33870f504a3 ts=2026-04-16T13:40:02.1130000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 8m 
  - Evidence: 143h 8m: 69cdc965d385e3b94310f781.jsonl[861] _id=69e0f30c7957a33870f5536d ts=2026-04-16T14:32:43.2600000Z -> 69cdc965d385e3b94310f781.jsonl[1790] _id=69e8d0011724f0c9e2fa310d ts=2026-04-22T13:41:21.3150000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 9m 
  - Evidence: 143h 9m: 69cdc965d385e3b94310f781.jsonl[855] _id=69e0f2e77957a33870f55253 ts=2026-04-16T14:32:06.3840000Z -> 69cdc965d385e3b94310f781.jsonl[1791] _id=69e8d0041724f0c9e2fa3143 ts=2026-04-22T13:41:24.4450000Z; 15m 7s: 69cdc965d385e3b94310f781.jsonl[719] _id=69e0ef577957a33870f53a6f ts=2026-04-16T14:16:54.8080000Z -> 69cdc965d385e3b94310f781.jsonl[856] _id=69e0f2e27957a33870f5521f ts=2026-04-16T14:32:01.9520000Z; 11m 42s: 69cdc965d385e3b94310f781.jsonl[623] _id=69e0ec8f7957a33870f5288d ts=2026-04-16T14:05:02.5160000Z -> 69cdc965d385e3b94310f781.jsonl[711] _id=69e0ef4e7957a33870f53a2f ts=2026-04-16T14:16:45.1820000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 22m 
  - Evidence: 143h 22m: 69cdc965d385e3b94310f781.jsonl[202] _id=69de4b5f7957a33870f34b75 ts=2026-04-14T14:12:46.1910000Z -> 69cdc965d385e3b94310f781.jsonl[1037] _id=69e62baa1724f0c9e2f86325 ts=2026-04-20T13:35:37.4010000Z; 95h 48m: 69cdc965d385e3b94310f781.jsonl[1558] _id=69e635cb1724f0c9e2f89e23 ts=2026-04-20T14:18:50.1810000Z -> 69cdc965d385e3b94310f781.jsonl[2291] _id=69eb792e1724f0c9e2fb82b9 ts=2026-04-24T14:07:41.9610000Z; 38m 43s: 69cdc965d385e3b94310f781.jsonl[1093] _id=69e62c7e1724f0c9e2f86971 ts=2026-04-20T13:39:10.2310000Z -> 69cdc965d385e3b94310f781.jsonl[1545] _id=69e635921724f0c9e2f89c99 ts=2026-04-20T14:17:53.6510000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 23m 
  - Evidence: 143h 23m: 69cdc965d385e3b94310f781.jsonl[201] _id=69de4b5e7957a33870f34b6f ts=2026-04-14T14:12:44.5720000Z -> 69cdc965d385e3b94310f781.jsonl[1042] _id=69e62bb51724f0c9e2f8635f ts=2026-04-20T13:35:49.1780000Z; 38m 55s: 69cdc965d385e3b94310f781.jsonl[1091] _id=69e62c7d1724f0c9e2f86957 ts=2026-04-20T13:39:08.7740000Z -> 69cdc965d385e3b94310f781.jsonl[1548] _id=69e6359c1724f0c9e2f89d05 ts=2026-04-20T14:18:04.1730000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.003s..0.020s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f781.jsonl[2289] _id=69eb79291724f0c9e2fb82a1 ts=2026-04-24T14:07:36.3020000Z -> 69cdc965d385e3b94310f781.jsonl[2293] _id=69eb79291724f0c9e2fb82a3 ts=2026-04-24T14:07:36.3050000Z; 17ms: 69cdc965d385e3b94310f781.jsonl[2323] _id=69eb79cb1724f0c9e2fb85ed ts=2026-04-24T14:10:19.0070000Z -> 69cdc965d385e3b94310f781.jsonl[2324] _id=69eb79cb1724f0c9e2fb85ef ts=2026-04-24T14:10:19.0240000Z; 20ms: 69cdc965d385e3b94310f781.jsonl[2325] _id=69eb79d01724f0c9e2fb8617 ts=2026-04-24T14:10:24.3870000Z -> 69cdc965d385e3b94310f781.jsonl[2327] _id=69eb79d01724f0c9e2fb861b ts=2026-04-24T14:10:24.4070000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc965d385e3b94310f781.jsonl[787] _id=69e0f1dd7957a33870f548f5 ts=2026-04-16T14:27:40.5820000Z -> 69cdc965d385e3b94310f781.jsonl[898] _id=69e627b51724f0c9e2f84b63 ts=2026-04-20T13:18:43.9020000Z; 47h 30m: 69cdc965d385e3b94310f781.jsonl[2139] _id=69e8dad91724f0c9e2fa723d ts=2026-04-22T14:27:36.6440000Z -> 69cdc965d385e3b94310f781.jsonl[2165] _id=69eb76d11724f0c9e2fb76bb ts=2026-04-24T13:57:36.9800000Z; 47h 3m: 69cdc965d385e3b94310f781.jsonl[327] _id=69de4fa67957a33870f369d6 ts=2026-04-14T14:31:01.3710000Z -> 69cdc965d385e3b94310f781.jsonl[347] _id=69e0e5567957a33870f4fa1b ts=2026-04-16T13:34:12.9560000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.002s..0.010s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f781.jsonl[169] _id=69de4a817957a33870f345ce ts=2026-04-14T14:09:04.4800000Z -> 69cdc965d385e3b94310f781.jsonl[170] _id=69de4a817957a33870f345d3 ts=2026-04-14T14:09:04.4820000Z; 7ms: 69cdc965d385e3b94310f781.jsonl[1932] _id=69e8d6bd1724f0c9e2fa5b79 ts=2026-04-22T14:10:05.0580000Z -> 69cdc965d385e3b94310f781.jsonl[1933] _id=69e8d6bd1724f0c9e2fa5b7b ts=2026-04-22T14:10:05.0650000Z; 10ms: 69cdc965d385e3b94310f781.jsonl[2696] _id=69eb7e3f1724f0c9e2fb9bd7 ts=2026-04-24T14:29:18.7760000Z -> 69cdc965d385e3b94310f781.jsonl[2695] _id=69eb7e3f1724f0c9e2fb9bdb ts=2026-04-24T14:29:18.7860000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc965d385e3b94310f781.jsonl:69cdc965d385e3b94310f781, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f781.jsonl[328] _id=69de4f8a7957a33870f36944 ts=2026-04-14T14:30:33.5720000Z`; `69cdc965d385e3b94310f781.jsonl[406] _id=69e0e6b67957a33870f504bf ts=2026-04-16T13:40:05.1320000Z`; `69cdc965d385e3b94310f781.jsonl[640] _id=69e0ece77957a33870f52a97 ts=2026-04-16T14:06:30.4920000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 32 record(s) match the trigger in 69cdc965d385e3b94310f781.jsonl:69cdc965d385e3b94310f781, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f781.jsonl[506] _id=69e0e9387957a33870f5155f ts=2026-04-16T13:50:47.3070000Z`; `69cdc965d385e3b94310f781.jsonl[504] _id=69e0e93f7957a33870f5158d ts=2026-04-16T13:50:54.5050000Z`; `69cdc965d385e3b94310f781.jsonl[509] _id=69e0e9637957a33870f51683 ts=2026-04-16T13:51:29.7330000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f781.jsonl[799] _id=69e0f2377957a33870f54bf3 ts=2026-04-16T14:29:10.6590000Z`; `69cdc965d385e3b94310f781.jsonl[1211] _id=69e62f291724f0c9e2f8779d ts=2026-04-20T13:50:32.5600000Z`; `69cdc965d385e3b94310f781.jsonl[1242] _id=69e630601724f0c9e2f87e0f ts=2026-04-20T13:55:43.0150000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f781.jsonl[1558] _id=69e635cb1724f0c9e2f89e23 ts=2026-04-20T14:18:50.1810000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f781.jsonl[2289] _id=69eb79291724f0c9e2fb82a1 ts=2026-04-24T14:07:36.3020000Z`; `69cdc965d385e3b94310f781.jsonl[2293] _id=69eb79291724f0c9e2fb82a3 ts=2026-04-24T14:07:36.3050000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc965d385e3b94310f781.jsonl[1642] _id=69e8ca1e1724f0c9e2fa0b5b ts=?`; `69cdc965d385e3b94310f781.jsonl[1878] _id=69e8d1701724f0c9e2fa3b8f ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 263 unmatched 'DialogueStartEvent' (totals: 424 start, 165 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 40 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.73s, min -320.37s, max -0.34s over 2725 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f781\coverage.yaml

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
  - Observed: 44 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1889 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (627); Unit 3 Dev (464); Unit 4 Dev (247); Unit 1 Dev (186); Unit 4 Dev - Dungeon (95); Unit 4 Dev - Anderson Base (94); Unit 3 Dungeon Dev (85); Unit 5 Dev (66); Unit 5 Dev - Dungeon (25)
- **eventKey:** present on 1300 of 1889 records
- **Intervals:** median 2.60s (p5 0.01s / p95 31.28s, n=1888)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1300; [conversationId, dialogueEventType] x589
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1889/1889 records)
    numeric range 8 .. 114 (49 unique)
data.dialogueEventType  (string, 1889/1889 records)
    "DialogueNodeEvent"  x1300
    "DialogueStartEvent"  x424
    "DialogueFinishEvent"  x165
data.nodeId  (number, 1300/1889 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 542 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (187); Unit 3 Dev (99); Unit 4 Dev (66); Unit 1 Dev (49); Unit 3 Dungeon Dev (48); Unit 4 Dev - Dungeon (45); Unit 5 Dev - Dungeon (21); Unit 4 Dev - Anderson Base (17); Unit 5 Dev (10)
- **Intervals:** median 30.01s (p5 29.96s / p95 33.55s, n=528)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 542/542 records)
data.position.x  (number, 542/542 records)
    numeric range -689.776 .. 1558.65 (289 unique)
data.position.y  (number, 542/542 records)
    numeric range -112.489 .. 217.459 (226 unique)
data.position.z  (number, 542/542 records)
    numeric range -1138.1 .. 2122.59 (289 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 70 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (12); Unit 4 Dev (11); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (1)
- **eventKey:** present on 70 of 70 records
- **Intervals:** median 155.53s (p5 0.01s / p95 101812.84s, n=69)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Fields under `data`:**

```text
data.questEventType  (string, 70/70 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x30
data.questID  (string, 70/70 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 70/70 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/70 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 44 records

- **Scenes:** Unit 2 Prod (Refactor) (36); Unit 3 Dev (8)
- **Intervals:** median 27.25s (p5 1.86s / p95 275.79s, n=43)
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "MapCloseEvent"  x22
    "MapOpenEvent"  x22
data.featureUsed  (string, 44/44 records)
    "Map"  x44
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 41 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (41)
- **Intervals:** median 4.24s (p5 0.95s / p95 30.10s, n=40)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "On"  x25
    "Off"  x16
data.floor  (string, 41/41 records)
    "3"  x22
    "4"  x9
    "2"  x7
    "1"  x3
data.machineNumber  (string, 41/41 records)
    "One"  x40
    "Two"  x1
data.machineType  (string, 41/41 records)
    "Condenser"  x15
    "Evaporator"  x9
    "DualChamber_Evaporator"  x8
    "DualChamber_Condenser"  x7
    "VentSwitch"  x2
data.room  (string, 41/41 records)
    "2"  x25
    "3"  x9
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 34 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (34)
- **Intervals:** median 3.45s (p5 0.37s / p95 119.09s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "ChangeCanister"  x34
data.canisterType  (string, 34/34 records)
    "Bedrock"  x15
    "Clay"  x9
    "Gravel"  x5
    "Sand"  x5
data.floor  (string, 34/34 records)
    "5"  x29
    "4"  x4
    "3"  x1
data.machine  (string, 34/34 records)
    "1"  x29
    "2"  x5
data.row  (string, 34/34 records)
    "TopRow"  x19
    "BottomRow"  x15
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 32 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (8)
- **Intervals:** median 6.76s (p5 2.22s / p95 804.90s, n=31)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "dragEnd"  x16
    "dragStart"  x16
data.featureUsed  (string, 32/32 records)
    "waypoint"  x32
data.location  (object, 32/32 records)
data.location.x  (number, 32/32 records)
    numeric range -770.79 .. 76.7954 (17 unique)
data.location.y  (number, 32/32 records)
    numeric range -314.487 .. 296.398 (17 unique)
data.location.z  (number, 32/32 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 26 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (8); Unit 3 Dev (5)
- **Intervals:** median 11.49s (p5 1.80s / p95 1883.67s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "argumentationNodeAdd"  x19
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 26/26 records)
    "Unit 2 – Watershed"  x13
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 26/26 records)
    "A"  x5
    "B"  x5
    "I"  x5
    "1"  x3
    "II"  x3
    "C"  x2
    "D"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (14)
- **Intervals:** median 1.93s (p5 0.01s / p95 53.05s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolClose"  x8
    "argumentationToolOpen"  x6
data.argumentationTitle  (string, 14/14 records)
    "Unit 4 - Flooding"  x14
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x8
    "BackingInfoPanel - Soil Flow Rates"  x6
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 11 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 138.50s (p5 13.86s / p95 439113.47s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationSessionOpen"  x6
    "argumentationSessionClose"  x5
data.argumentationDescription  (string, 11/11 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 4 - Flooding"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 56.82s (p5 3.01s / p95 276452.84s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/10 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/10 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 2.90s (p5 1.36s / p95 14.50s, n=7)
- **`data` key-set variants:** [actionType, boxID, soilType] x5; [actionType, boxId, soilType] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "soilSelected"  x5
    "cameraPlaced"  x3
data.boxID  (string, 5/8 records)
    "0"  x3
    "1"  x1
    "2"  x1
data.boxId  (string, 3/8 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 8/8 records)
    "Gravel"  x3
    "Sand"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 174772.06s (p5 173293.34s / p95 482216.54s, n=3)
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

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Cannot close a closed AudioContext."  x1
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x1
    "unhandled_rejection"  x1
data.unitId  (string, 2/2 records)
    "unit3"  x2
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
- `TopographicMapEvent` data.actionType: "dragStart" (16x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)
- `soilMachine` data.canisterType: "Bedrock" (15x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*