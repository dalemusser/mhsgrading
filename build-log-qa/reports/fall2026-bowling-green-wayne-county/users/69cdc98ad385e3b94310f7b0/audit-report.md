# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b0

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b0
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7b0.jsonl
- **Records:** 3365 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7b0
- **Time span:** 2026-04-14T19:19:54.085000+00:00 .. 2026-04-24T20:10:18.106000+00:00 (240h 50m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b0\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 3365 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 69 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 2380 | 70.73 | 1 | 9 | 1637 | 2026-04-14T19:20:16.898000+00:00 | 2026-04-24T20:10:14.949000+00:00 | 240h 49m |
| PlayerPositionEvent | 688 | 20.45 | 1 | 9 | 0 | 2026-04-14T19:19:54.085000+00:00 | 2026-04-24T20:10:18.106000+00:00 | 240h 50m |
| questEvent | 90 | 2.67 | 1 | 9 | 90 | 2026-04-14T19:20:16.848000+00:00 | 2026-04-24T19:54:15.947000+00:00 | 240h 33m |
| argumentationNodeEvent | 41 | 1.22 | 1 | 3 | 0 | 2026-04-14T19:50:33.487000+00:00 | 2026-04-20T19:33:54.691000+00:00 | 143h 43m |
| Topographic Map Event | 36 | 1.07 | 1 | 2 | 0 | 2026-04-14T20:02:31.074000+00:00 | 2026-04-22T19:42:35.897000+00:00 | 191h 40m |
| WaterChamberEvent | 36 | 1.07 | 1 | 1 | 0 | 2026-04-24T19:44:49.511000+00:00 | 2026-04-24T19:50:12.502000+00:00 | 5m 22s |
| soilMachine | 25 | 0.74 | 1 | 1 | 0 | 2026-04-24T19:07:20.713000+00:00 | 2026-04-24T19:16:58.916000+00:00 | 9m 38s |
| TopographicMapEvent | 20 | 0.59 | 1 | 2 | 0 | 2026-04-16T19:12:00.540000+00:00 | 2026-04-22T19:40:55.182000+00:00 | 144h 28m |
| TerasGardenBox | 13 | 0.39 | 1 | 1 | 0 | 2026-04-24T19:35:27.259000+00:00 | 2026-04-24T19:37:55.321000+00:00 | 2m 28s |
| argumentationEvent | 11 | 0.33 | 1 | 5 | 0 | 2026-04-14T19:50:20.642000+00:00 | 2026-04-24T19:57:16.063000+00:00 | 240h 6m |
| argumentationToolEvent | 11 | 0.33 | 1 | 4 | 0 | 2026-04-20T19:02:41.677000+00:00 | 2026-04-24T19:58:30.913000+00:00 | 96h 55m |
| Soil Key Puzzle | 8 | 0.24 | 1 | 3 | 0 | 2026-04-16T19:40:29.967000+00:00 | 2026-04-22T19:52:06.287000+00:00 | 144h 11m |
| EndOfUnit | 5 | 0.15 | 1 | 4 | 0 | 2026-04-14T19:56:11.306000+00:00 | 2026-04-24T19:41:59.631000+00:00 | 239h 45m |
| crash | 1 | 0.03 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173845.902s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.016s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 124.706s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.049s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.186s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.979s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.866s median 
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
  - Observed: 5.647s median 
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
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 36 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 41 records 
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
  - Observed: C 
  - Expected: may simply not have been exercised — review
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
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.0x vs baseline. 
  - Observed: 25 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 17 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[72] _id=69de9b187957a33870f3a785 ts=2026-04-14T19:52:56.3050000Z`; `69cdc98ad385e3b94310f7b0.jsonl[195] _id=69e135c11724f0c9e2f6afc0 ts=2026-04-16T19:17:20.2530000Z`; `69cdc98ad385e3b94310f7b0.jsonl[1727] _id=69e135c11724f0c9e2f6afc2 ts=2026-04-16T19:17:20.3070000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 36 records, TopographicMapEvent: 20 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 6 records, data.boxId: 7 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2379 | 0.0 | 2.324 | 364.438 | 35.423 | 340858.407 | 0.16 | 619 | 4 |
| PlayerPositionEvent | 674 | 29.787 | 30.016 | 1285.854 | 35.566 | 340850.744 | 0.05 | 0 | 4 |
| questEvent | 89 | 0.004 | 172.806 | 9730.776 | 1152.864 | 341926.608 | 0.01 | 12 | 12 |
| argumentationNodeEvent | 40 | 1.047 | 4.979 | 12935.03 | 158.174 | 515319.986 | 0.0 | 0 | 2 |
| Topographic Map Event | 35 | 3.942 | 17.749 | 19714.424 | 168559.72 | 343589.2 | 0.0 | 0 | 7 |
| WaterChamberEvent | 35 | 0.815 | 4.186 | 9.228 | 24.235 | 42.951 | 6.5 | 0 | 0 |
| soilMachine | 24 | 0.219 | 5.647 | 24.092 | 86.643 | 258.094 | 2.49 | 0 | 0 |
| TopographicMapEvent | 19 | 0.473 | 7.049 | 27375.507 | 185956.648 | 347745.536 | 0.0 | 0 | 4 |
| TerasGardenBox | 12 | 1.574 | 6.272 | 12.339 | 39.116 | 55.015 | 4.86 | 0 | 0 |
| argumentationEvent | 10 | 0.091 | 119.927 | 86441.542 | 438812.825 | 515309.748 | 0.0 | 0 | 4 |
| argumentationToolEvent | 10 | 0.006 | 2.866 | 34894.924 | 190769.939 | 345406.398 | 0.0 | 1 | 3 |
| Soil Key Puzzle | 7 | 15.811 | 124.706 | 74156.617 | 292906.937 | 345368.299 | 0.0 | 0 | 3 |
| EndOfUnit | 4 | 0.0 | 173845.902 | 215787.081 | 464406.234 | 515456.522 | 0.0 | 1 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.016s (p5 29.95s, p95 35.57s, n=674) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc98ad385e3b94310f7b0.jsonl[1496] _id=69de9bdb7957a33870f3aa77 ts=2026-04-14T19:56:11.3060000Z ~ 69cdc98ad385e3b94310f7b0.jsonl[1497] _id=69de9bf47957a33870f3ab61 ts=2026-04-14T19:56:11.306Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `91ms: 69cdc98ad385e3b94310f7b0.jsonl[434] _id=69e67fa41724f0c9e2f8e643 ts=2026-04-20T19:33:56.1020000Z ~ 69cdc98ad385e3b94310f7b0.jsonl[2650] _id=69e67fa51724f0c9e2f8e64d ts=2026-04-20T19:33:56.1930000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 69cdc98ad385e3b94310f7b0.jsonl[847] _id=69ebc4811724f0c9e2fbbdbd ts=2026-04-24T19:29:05.5630000Z ~ 69cdc98ad385e3b94310f7b0.jsonl[866] _id=69ebc4811724f0c9e2fbbdbf ts=2026-04-24T19:29:05.5690000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `401ms: 69cdc98ad385e3b94310f7b0.jsonl[3255] _id=69ebc1681724f0c9e2fbb84d ts=2026-04-24T19:15:52.7390000Z ~ 69cdc98ad385e3b94310f7b0.jsonl[735] _id=69ebc1691724f0c9e2fbb84f ts=2026-04-24T19:15:53.1400000Z`; `291ms: 69cdc98ad385e3b94310f7b0.jsonl[735] _id=69ebc1691724f0c9e2fbb84f ts=2026-04-24T19:15:53.1400000Z ~ 69cdc98ad385e3b94310f7b0.jsonl[736] _id=69ebc1691724f0c9e2fbb851 ts=2026-04-24T19:15:53.4310000Z`; `257ms: 69cdc98ad385e3b94310f7b0.jsonl[736] _id=69ebc1691724f0c9e2fbb851 ts=2026-04-24T19:15:53.4310000Z ~ 69cdc98ad385e3b94310f7b0.jsonl[3256] _id=69ebc1691724f0c9e2fbb853 ts=2026-04-24T19:15:53.6880000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc98ad385e3b94310f7b0.jsonl[351] _id=69e141bc1724f0c9e2f712ee ts=2026-04-16T20:08:28.6890000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2202] _id=69e675371724f0c9e2f8b73f ts=2026-04-20T18:49:27.0960000Z; 46h 55m: 69cdc98ad385e3b94310f7b0.jsonl[3203] _id=69e929961724f0c9e2fac355 ts=2026-04-22T20:03:34.0360000Z -> 69cdc98ad385e3b94310f7b0.jsonl[634] _id=69ebbd7e1724f0c9e2fbb329 ts=2026-04-24T18:59:10.4710000Z; 46h 44m: 69cdc98ad385e3b94310f7b0.jsonl[1560] _id=69de9e547957a33870f3b52d ts=2026-04-14T20:06:44.0930000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1600] _id=69e12f8a1724f0c9e2f68f48 ts=2026-04-16T18:50:50.6970000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 619 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7b0.jsonl[1093] _id=69ebc7871724f0c9e2fbc2f1 ts=2026-04-24T19:41:59.6570000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1100] _id=69ebc7991724f0c9e2fbc317 ts=2026-04-24T19:41:59.657Z; 0ms: 69cdc98ad385e3b94310f7b0.jsonl[373] _id=69e6795c1724f0c9e2f8c8e9 ts=2026-04-20T19:07:07.8540000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2383] _id=69e6796d1724f0c9e2f8c92f ts=2026-04-20T19:07:07.854Z; 3ms: 69cdc98ad385e3b94310f7b0.jsonl[1253] _id=69ebcbb41724f0c9e2fbca07 ts=2026-04-24T19:59:48.3480000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1254] _id=69ebcbb41724f0c9e2fbca09 ts=2026-04-24T19:59:48.3510000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 10m 
  - Evidence: 143h 10m: 69cdc98ad385e3b94310f7b0.jsonl[1497] _id=69de9bf47957a33870f3ab61 ts=2026-04-14T19:56:11.306Z -> 69cdc98ad385e3b94310f7b0.jsonl[2379] _id=69e6795c1724f0c9e2f8c8e5 ts=2026-04-20T19:07:07.8280000Z; 48h 38m: 69cdc98ad385e3b94310f7b0.jsonl[2379] _id=69e6795c1724f0c9e2f8c8e5 ts=2026-04-20T19:07:07.8280000Z -> 69cdc98ad385e3b94310f7b0.jsonl[3122] _id=69e9256d1724f0c9e2fab4b3 ts=2026-04-22T19:45:49.0990000Z; 47h 56m: 69cdc98ad385e3b94310f7b0.jsonl[3122] _id=69e9256d1724f0c9e2fab4b3 ts=2026-04-22T19:45:49.0990000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1092] _id=69ebc7871724f0c9e2fbc2ee ts=2026-04-24T19:41:59.6310000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7b0.jsonl[1496] _id=69de9bdb7957a33870f3aa77 ts=2026-04-14T19:56:11.3060000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1497] _id=69de9bf47957a33870f3ab61 ts=2026-04-14T19:56:11.306Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc98ad385e3b94310f7b0.jsonl[2156] _id=69e141a91724f0c9e2f712aa ts=2026-04-16T20:08:09.4690000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2194] _id=69e6751c1724f0c9e2f8b71b ts=2026-04-20T18:49:00.2130000Z; 46h 54m: 69cdc98ad385e3b94310f7b0.jsonl[3208] _id=69e929c71724f0c9e2fac40f ts=2026-04-22T20:04:22.4700000Z -> 69cdc98ad385e3b94310f7b0.jsonl[3218] _id=69ebbd731724f0c9e2fbb31b ts=2026-04-24T18:58:58.8630000Z; 46h 41m: 69cdc98ad385e3b94310f7b0.jsonl[112] _id=69de9ef27957a33870f3b73d ts=2026-04-14T20:09:22.7120000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1598] _id=69e12f851724f0c9e2f68f44 ts=2026-04-16T18:50:45.7700000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 69cdc98ad385e3b94310f7b0.jsonl[1914] _id=69e13b581724f0c9e2f6f6f4 ts=2026-04-16T19:41:12.8900000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2688] _id=69e680711724f0c9e2f8e9b9 ts=2026-04-20T19:37:21.1890000Z; 47h 21m: 69cdc98ad385e3b94310f7b0.jsonl[2694] _id=69e680d81724f0c9e2f8eb67 ts=2026-04-20T19:39:03.9930000Z -> 69cdc98ad385e3b94310f7b0.jsonl[524] _id=69e91ad91724f0c9e2fa8d0d ts=2026-04-22T19:00:41.0860000Z; 49m 4s: 69cdc98ad385e3b94310f7b0.jsonl[2964] _id=69e91b561724f0c9e2fa8ef9 ts=2026-04-22T19:02:45.7920000Z -> 69cdc98ad385e3b94310f7b0.jsonl[3144] _id=69e926d71724f0c9e2fab8f7 ts=2026-04-22T19:51:50.4760000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 69cdc98ad385e3b94310f7b0.jsonl[2065] _id=69e13ea81724f0c9e2f70582 ts=2026-04-16T19:55:20.7900000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2505] _id=69e67cce1724f0c9e2f8d897 ts=2026-04-20T19:21:49.9900000Z; 47h 9m: 69cdc98ad385e3b94310f7b0.jsonl[1539] _id=69de9d607957a33870f3b1c3 ts=2026-04-14T20:02:40.4940000Z -> 69cdc98ad385e3b94310f7b0.jsonl[176] _id=69e134781724f0c9e2f6a716 ts=2026-04-16T19:11:52.0550000Z; 46h 40m: 69cdc98ad385e3b94310f7b0.jsonl[2899] _id=69e688af1724f0c9e2f904e3 ts=2026-04-20T20:12:31.2460000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2941] _id=69e919201724f0c9e2fa85f5 ts=2026-04-22T18:53:20.1770000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 35m 
  - Evidence: 96h 35m: 69cdc98ad385e3b94310f7b0.jsonl[1849] _id=69e1391a1724f0c9e2f6dc9c ts=2026-04-16T19:31:38.3290000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2868] _id=69e6877c1724f0c9e2f90081 ts=2026-04-20T20:07:23.8650000Z; 46h 39m: 69cdc98ad385e3b94310f7b0.jsonl[499] _id=69e688ae1724f0c9e2f904df ts=2026-04-20T20:12:29.8930000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2937] _id=69e918da1724f0c9e2fa84d1 ts=2026-04-22T18:52:09.9980000Z; 48m 39s: 69cdc98ad385e3b94310f7b0.jsonl[2938] _id=69e918dd1724f0c9e2fa84e3 ts=2026-04-22T18:52:12.7550000Z -> 69cdc98ad385e3b94310f7b0.jsonl[3065] _id=69e924451724f0c9e2fab00b ts=2026-04-22T19:40:52.6100000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 8m 
  - Evidence: 143h 8m: 69cdc98ad385e3b94310f7b0.jsonl[1467] _id=69de9b187957a33870f3a783 ts=2026-04-14T19:52:56.2570000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2319] _id=69e678061724f0c9e2f8c287 ts=2026-04-20T19:01:26.0050000Z; 95h 55m: 69cdc98ad385e3b94310f7b0.jsonl[2650] _id=69e67fa51724f0c9e2f8e64d ts=2026-04-20T19:33:56.1930000Z -> 69cdc98ad385e3b94310f7b0.jsonl[867] _id=69ebc4881724f0c9e2fbbdcb ts=2026-04-24T19:29:12.7780000Z; 28m 30s: 69cdc98ad385e3b94310f7b0.jsonl[2332] _id=69e6785a1724f0c9e2f8c3df ts=2026-04-20T19:02:50.6770000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2603] _id=69e67f091724f0c9e2f8e31d ts=2026-04-20T19:31:20.9210000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 8m 
  - Evidence: 143h 8m: 69cdc98ad385e3b94310f7b0.jsonl[1465] _id=69de9b137957a33870f3a769 ts=2026-04-14T19:52:51.2790000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2321] _id=69e6780b1724f0c9e2f8c29f ts=2026-04-20T19:01:31.2650000Z; 28m 40s: 69cdc98ad385e3b94310f7b0.jsonl[2331] _id=69e678591724f0c9e2f8c3d7 ts=2026-04-20T19:02:48.7210000Z -> 69cdc98ad385e3b94310f7b0.jsonl[400] _id=69e67f111724f0c9e2f8e33b ts=2026-04-20T19:31:29.5410000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 69cdc98ad385e3b94310f7b0.jsonl[2623] _id=69e67f431724f0c9e2f8e425 ts=2026-04-20T19:32:19.1650000Z -> 69cdc98ad385e3b94310f7b0.jsonl[847] _id=69ebc4811724f0c9e2fbbdbd ts=2026-04-24T19:29:05.5630000Z; 29m 29s: 69cdc98ad385e3b94310f7b0.jsonl[358] _id=69e678551724f0c9e2f8c3c3 ts=2026-04-20T19:02:45.3140000Z -> 69cdc98ad385e3b94310f7b0.jsonl[402] _id=69e67f3f1724f0c9e2f8e413 ts=2026-04-20T19:32:15.1370000Z; 29m 20s: 69cdc98ad385e3b94310f7b0.jsonl[866] _id=69ebc4811724f0c9e2fbbdbf ts=2026-04-24T19:29:05.5690000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1228] _id=69ebcb621724f0c9e2fbc9a3 ts=2026-04-24T19:58:26.2380000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 69cdc98ad385e3b94310f7b0.jsonl[847] _id=69ebc4811724f0c9e2fbbdbd ts=2026-04-24T19:29:05.5630000Z -> 69cdc98ad385e3b94310f7b0.jsonl[866] _id=69ebc4811724f0c9e2fbbdbf ts=2026-04-24T19:29:05.5690000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 94h 58m 
  - Evidence: 94h 58m: 69cdc98ad385e3b94310f7b0.jsonl[2005] _id=69e13d791724f0c9e2f70199 ts=2026-04-16T19:50:18.0620000Z -> 69cdc98ad385e3b94310f7b0.jsonl[2191] _id=69e675211724f0c9e2f8b71f ts=2026-04-20T18:49:04.6700000Z; 46h 56m: 69cdc98ad385e3b94310f7b0.jsonl[3195] _id=69e929461724f0c9e2fac217 ts=2026-04-22T20:02:13.7530000Z -> 69cdc98ad385e3b94310f7b0.jsonl[3219] _id=69ebbd751724f0c9e2fbb31d ts=2026-04-24T18:59:01.5550000Z; 46h 51m: 69cdc98ad385e3b94310f7b0.jsonl[100] _id=69de9c807957a33870f3ae39 ts=2026-04-14T19:58:56.6880000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1599] _id=69e12f891724f0c9e2f68f46 ts=2026-04-16T18:50:49.1710000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.004s..0.009s shown 
  - Evidence: 4ms: 69cdc98ad385e3b94310f7b0.jsonl[50] _id=69de9a487957a33870f3a36b ts=2026-04-14T19:49:28.5500000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1438] _id=69de9a497957a33870f3a36d ts=2026-04-14T19:49:28.5540000Z; 8ms: 69cdc98ad385e3b94310f7b0.jsonl[671] _id=69ebbe691724f0c9e2fbb49b ts=2026-04-24T19:03:05.4830000Z -> 69cdc98ad385e3b94310f7b0.jsonl[667] _id=69ebbe691724f0c9e2fbb49f ts=2026-04-24T19:03:05.4910000Z; 9ms: 69cdc98ad385e3b94310f7b0.jsonl[1136] _id=69ebc8801724f0c9e2fbc49d ts=2026-04-24T19:46:07.7890000Z -> 69cdc98ad385e3b94310f7b0.jsonl[1137] _id=69ebc8801724f0c9e2fbc49f ts=2026-04-24T19:46:07.7980000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc98ad385e3b94310f7b0.jsonl:69cdc98ad385e3b94310f7b0, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[1914] _id=69e13b581724f0c9e2f6f6f4 ts=2026-04-16T19:41:12.8900000Z`; `69cdc98ad385e3b94310f7b0.jsonl[2694] _id=69e680d81724f0c9e2f8eb67 ts=2026-04-20T19:39:03.9930000Z`; `69cdc98ad385e3b94310f7b0.jsonl[2964] _id=69e91b561724f0c9e2fa8ef9 ts=2026-04-22T19:02:45.7920000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 20 record(s) match the trigger in 69cdc98ad385e3b94310f7b0.jsonl:69cdc98ad385e3b94310f7b0, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[179] _id=69e134801724f0c9e2f6a736 ts=2026-04-16T19:12:00.5400000Z`; `69cdc98ad385e3b94310f7b0.jsonl[1696] _id=69e134861724f0c9e2f6a756 ts=2026-04-16T19:12:06.2900000Z`; `69cdc98ad385e3b94310f7b0.jsonl[244] _id=69e138951724f0c9e2f6d9a6 ts=2026-04-16T19:29:25.6290000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[295] _id=69e13db91724f0c9e2f70274 ts=2026-04-16T19:51:21.7060000Z`; `69cdc98ad385e3b94310f7b0.jsonl[2451] _id=69e67b7d1724f0c9e2f8d22f ts=2026-04-20T19:16:12.9420000Z`; `69cdc98ad385e3b94310f7b0.jsonl[382] _id=69e67c561724f0c9e2f8d5cf ts=2026-04-20T19:19:50.1690000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[2650] _id=69e67fa51724f0c9e2f8e64d ts=2026-04-20T19:33:56.1930000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[847] _id=69ebc4811724f0c9e2fbbdbd ts=2026-04-24T19:29:05.5630000Z`; `69cdc98ad385e3b94310f7b0.jsonl[866] _id=69ebc4811724f0c9e2fbbdbf ts=2026-04-24T19:29:05.5690000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[2930] _id=69e918721724f0c9e2fa8345 ts=2026-04-22T18:50:26.1290000Z`; `69cdc98ad385e3b94310f7b0.jsonl[526] _id=69e91b5f1724f0c9e2fa8f21 ts=2026-04-22T19:02:55.1800000Z`; `69cdc98ad385e3b94310f7b0.jsonl[571] _id=69e924541724f0c9e2fab055 ts=2026-04-22T19:41:07.7150000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[1094] _id=69ebc7891724f0c9e2fbc2f9 ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7b0.jsonl[1229] _id=69ebcb641724f0c9e2fbc9a7 ts=2026-04-24T19:58:28.3330000Z`; `69cdc98ad385e3b94310f7b0.jsonl[1230] _id=69ebcb651724f0c9e2fbc9ab ts=2026-04-24T19:58:29.7510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 284 unmatched 'DialogueStartEvent' (totals: 511 start, 232 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 5 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 52 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.17s, min -25.58s, max +0.23s over 3364 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b0\coverage.yaml

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
  - Observed: 36 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2380 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (824); Unit 3 Dev (458); Unit 3 Dungeon Dev (286); Unit 4 Dev (265); Unit 1 Dev (210); Unit 4 Dev - Dungeon (128); Unit 4 Dev - Anderson Base (112); Unit 5 Dev (71); Unit 5 Dev - Dungeon (26)
- **eventKey:** present on 1637 of 2380 records
- **Intervals:** median 2.32s (p5 0.01s / p95 35.42s, n=2379)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1637; [conversationId, dialogueEventType] x743
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2380/2380 records)
    numeric range 8 .. 114 (48 unique)
data.dialogueEventType  (string, 2380/2380 records)
    "DialogueNodeEvent"  x1637
    "DialogueStartEvent"  x511
    "DialogueFinishEvent"  x232
data.nodeId  (number, 1637/2380 records)
    numeric range 0 .. 290 (234 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 688 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (215); Unit 3 Dev (119); Unit 3 Dungeon Dev (104); Unit 1 Dev (72); Unit 4 Dev - Dungeon (55); Unit 4 Dev (49); Unit 5 Dev (39); Unit 4 Dev - Anderson Base (18); Unit 5 Dev - Dungeon (17)
- **Intervals:** median 30.02s (p5 29.95s / p95 35.57s, n=674)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 688/688 records)
data.position.x  (number, 688/688 records)
    numeric range -754.689 .. 1558.82 (408 unique)
data.position.y  (number, 688/688 records)
    numeric range -115.127 .. 217.708 (294 unique)
data.position.z  (number, 688/688 records)
    numeric range -1205.81 .. 1761 (408 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 90 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 3 Dev (15); Unit 1 Dev (14); Unit 4 Dev - Dungeon (12); Unit 4 Dev (11); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (6); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (2)
- **eventKey:** present on 90 of 90 records
- **Intervals:** median 172.81s (p5 0.01s / p95 1152.86s, n=89)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 90/90 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x38
data.questID  (string, 90/90 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 90/90 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/90 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 41 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (23); Unit 1 Dev (11); Unit 2 Prod (Refactor) (7)
- **Intervals:** median 4.98s (p5 1.25s / p95 158.17s, n=40)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "argumentationNodeAdd"  x26
    "argumentationNodeRemove"  x15
data.argumentationTitle  (string, 41/41 records)
    "Unit 3 - Pollution Upstream"  x23
    "Unit 1 - Freshwater"  x9
    "Unit 2 – Watershed"  x7
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 41/41 records)
    "B"  x11
    "A"  x9
    "1"  x5
    "3"  x4
    "II"  x3
    "2"  x2
    "4"  x2
    "D"  x2
    "I"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 36 records

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 17.75s (p5 5.34s / p95 168559.72s, n=35)
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
data.featureUsed  (string, 36/36 records)
    "Map"  x36
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 36 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (36)
- **Intervals:** median 4.19s (p5 0.95s / p95 24.24s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "On"  x23
    "Off"  x13
data.floor  (string, 36/36 records)
    "4"  x17
    "3"  x13
    "2"  x4
    "1"  x2
data.machineNumber  (string, 36/36 records)
    "One"  x35
    "Two"  x1
data.machineType  (string, 36/36 records)
    "Condenser"  x22
    "Evaporator"  x7
    "VentSwitch"  x4
    "DualChamber_Evaporator"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 36/36 records)
    "2"  x14
    "1"  x12
    "3"  x8
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 25 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (25)
- **Intervals:** median 5.65s (p5 0.25s / p95 86.64s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "ChangeCanister"  x25
data.canisterType  (string, 25/25 records)
    "Bedrock"  x13
    "Clay"  x8
    "Gravel"  x3
    "Sand"  x1
data.floor  (string, 25/25 records)
    "5"  x20
    "4"  x4
    "3"  x1
data.machine  (string, 25/25 records)
    "1"  x24
    "2"  x1
data.row  (string, 25/25 records)
    "BottomRow"  x15
    "TopRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 20 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (14); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 7.05s (p5 0.60s / p95 185956.65s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "dragEnd"  x10
    "dragStart"  x10
data.featureUsed  (string, 20/20 records)
    "waypoint"  x20
data.location  (object, 20/20 records)
data.location.x  (number, 20/20 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 20/20 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 20/20 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `TerasGardenBox` — 13 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (13)
- **Intervals:** median 6.27s (p5 1.58s / p95 39.12s, n=12)
- **`data` key-set variants:** [actionType, boxId, soilType] x7; [actionType, boxID, soilType] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "cameraPlaced"  x7
    "soilSelected"  x6
data.boxID  (string, 6/13 records)
    "1"  x3
    "0"  x2
    "2"  x1
data.boxId  (string, 7/13 records)
    "0"  x3
    "1"  x2
    "2"  x2
data.soilType  (string, 13/13 records)
    "Gravel"  x7
    "None"  x4
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 11 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 119.93s (p5 21.20s / p95 438812.82s, n=10)
- **Open findings:** 1 — see sections 5-8
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

### `argumentationToolEvent` — 11 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 5 Dev (5); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 2.87s (p5 0.04s / p95 190769.94s, n=10)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x5
data.argumentationTitle  (string, 11/11 records)
    "Unit 5"  x5
    "Unit 2 – Watershed"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 4 - Flooding"  x2
data.toolName  (string, 11/11 records)
    "BackingInfoPanel - Evaporation Flow Diagram"  x5
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Soil Flow Rates"  x2
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (2); Unit 4 Dev (2)
- **Intervals:** median 124.71s (p5 23.94s / p95 292906.94s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 3 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 173845.90s (p5 25885.58s / p95 464406.23s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x2
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TerasGardenBox` data.soilType: "None" (4x)
- `TopographicMapEvent` data.actionType: "dragStart" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (15x)
- `soilMachine` data.canisterType: "Bedrock" (13x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*