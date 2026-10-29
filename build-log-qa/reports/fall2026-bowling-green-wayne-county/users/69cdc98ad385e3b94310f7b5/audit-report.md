# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b5

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b5
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7b5.jsonl
- **Records:** 2703 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7b5
- **Time span:** 2026-04-14T19:32:44.186000+00:00 .. 2026-04-24T19:32:21.407000+00:00 (239h 59m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b5\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2703 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 65 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 1816 | 67.18 | 1 | 9 | 1258 | 2026-04-14T19:33:02.763000+00:00 | 2026-04-24T19:32:21.407000+00:00 | 239h 59m |
| PlayerPositionEvent | 615 | 22.75 | 1 | 9 | 0 | 2026-04-14T19:32:44.186000+00:00 | 2026-04-24T19:32:06.263000+00:00 | 239h 59m |
| questEvent | 94 | 3.48 | 1 | 9 | 94 | 2026-04-14T19:33:02.746000+00:00 | 2026-04-24T19:31:36.215000+00:00 | 239h 58m |
| Topographic Map Event | 38 | 1.41 | 1 | 2 | 0 | 2026-04-16T19:07:52.130000+00:00 | 2026-04-20T19:54:39.986000+00:00 | 96h 46m |
| TopographicMapEvent | 34 | 1.26 | 1 | 2 | 0 | 2026-04-16T19:37:33.375000+00:00 | 2026-04-20T19:54:37.799000+00:00 | 96h 17m |
| WaterChamberEvent | 29 | 1.07 | 1 | 1 | 0 | 2026-04-24T18:59:27.940000+00:00 | 2026-04-24T19:07:44.364000+00:00 | 8m 16s |
| argumentationNodeEvent | 15 | 0.55 | 1 | 2 | 0 | 2026-04-14T19:49:30.992000+00:00 | 2026-04-20T19:22:48.756000+00:00 | 143h 33m |
| Soil Key Puzzle | 14 | 0.52 | 1 | 3 | 0 | 2026-04-16T19:57:31.964000+00:00 | 2026-04-22T18:50:01.976000+00:00 | 142h 52m |
| argumentationEvent | 14 | 0.52 | 1 | 4 | 0 | 2026-04-14T19:48:12.923000+00:00 | 2026-04-24T19:19:01.150000+00:00 | 239h 30m |
| soilMachine | 11 | 0.41 | 1 | 1 | 0 | 2026-04-22T19:16:07.712000+00:00 | 2026-04-22T19:25:15.362000+00:00 | 9m 7s |
| argumentationToolEvent | 10 | 0.37 | 1 | 1 | 0 | 2026-04-22T19:44:20.630000+00:00 | 2026-04-22T19:47:26.111000+00:00 | 3m 5s |
| TerasGardenBox | 7 | 0.26 | 1 | 1 | 0 | 2026-04-22T19:52:38.927000+00:00 | 2026-04-22T19:53:52.782000+00:00 | 1m 13s |
| EndOfUnit | 4 | 0.15 | 1 | 4 | 0 | 2026-04-14T20:06:33.717000+00:00 | 2026-04-24T19:31:27.347000+00:00 | 239h 24m |
| crash | 2 | 0.07 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172506.008s median 
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
  - Observed: 221.615s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 10.836s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 11.634s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 9.041s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.48s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.193s median 
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
  - Observed: 7.202s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` — field(s) not present in baseline schema. 
  - Observed: data.boxID
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: soilSelected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 38 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 15 records 
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
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[35] _id=69de9a7a7957a33870f3a463 ts=2026-04-14T19:50:17.8240000Z`; `69cdc98ad385e3b94310f7b5.jsonl[1120] _id=69de9d587957a33870f3b1a1 ts=2026-04-14T20:02:32.2830000Z`; `69cdc98ad385e3b94310f7b5.jsonl[1508] _id=69e13c571724f0c9e2f6fb80 ts=2026-04-16T19:45:26.3490000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 38 records, TopographicMapEvent: 34 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1815 | 0.002 | 2.507 | 476.01 | 54.697 | 323669.687 | 0.13 | 459 | 8 |
| PlayerPositionEvent | 603 | 29.777 | 30.005 | 1422.132 | 49.105 | 323658.233 | 0.04 | 0 | 6 |
| questEvent | 93 | 0.002 | 155.68 | 9289.392 | 6244.684 | 323687.532 | 0.01 | 15 | 15 |
| Topographic Map Event | 37 | 4.235 | 35.703 | 9416.429 | 1733.577 | 342061.944 | 0.01 | 0 | 4 |
| TopographicMapEvent | 33 | 1.15 | 11.634 | 10503.77 | 1499.102 | 341932.114 | 0.01 | 0 | 3 |
| WaterChamberEvent | 28 | 1.883 | 9.041 | 17.729 | 48.244 | 93.18 | 3.38 | 0 | 0 |
| argumentationNodeEvent | 14 | 1.304 | 8.48 | 36914.126 | 181049.182 | 515918.853 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 13 | 28.545 | 221.615 | 39565.386 | 231784.246 | 323775.882 | 0.0 | 0 | 5 |
| argumentationEvent | 13 | 0.121 | 68.601 | 66326.787 | 310806.824 | 515897.704 | 0.0 | 0 | 4 |
| soilMachine | 10 | 0.485 | 7.202 | 54.765 | 211.598 | 269.152 | 1.1 | 0 | 0 |
| argumentationToolEvent | 9 | 0.002 | 4.193 | 20.609 | 87.624 | 126.812 | 2.91 | 1 | 0 |
| TerasGardenBox | 6 | 1.385 | 10.836 | 12.309 | 24.79 | 24.914 | 4.87 | 0 | 0 |
| EndOfUnit | 3 | 170957.841 | 172506.008 | 287297.877 | 483837.404 | 518429.781 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.97s, p95 49.10s, n=603) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `121ms: 69cdc98ad385e3b94310f7b5.jsonl[2001] _id=69e67d171724f0c9e2f8da29 ts=2026-04-20T19:23:02.9430000Z ~ 69cdc98ad385e3b94310f7b5.jsonl[337] _id=69e67d181724f0c9e2f8da31 ts=2026-04-20T19:23:03.0640000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc98ad385e3b94310f7b5.jsonl[2508] _id=69e925151724f0c9e2fab32f ts=2026-04-22T19:44:20.6300000Z ~ 69cdc98ad385e3b94310f7b5.jsonl[2507] _id=69e925151724f0c9e2fab331 ts=2026-04-22T19:44:20.6320000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 69cdc98ad385e3b94310f7b5.jsonl[754] _id=69ebc2461724f0c9e2fbb95f ts=2026-04-24T19:19:33.8550000Z ~ 69cdc98ad385e3b94310f7b5.jsonl[741] _id=69ebc2461724f0c9e2fbb961 ts=2026-04-24T19:19:33.8620000Z`; `5ms: 69cdc98ad385e3b94310f7b5.jsonl[804] _id=69ebc4071724f0c9e2fbbca1 ts=2026-04-24T19:27:03.2340000Z ~ 69cdc98ad385e3b94310f7b5.jsonl[805] _id=69ebc4071724f0c9e2fbbca3 ts=2026-04-24T19:27:03.2390000Z`; `2ms: 69cdc98ad385e3b94310f7b5.jsonl[565] _id=69ebc5191724f0c9e2fbbeb9 ts=2026-04-24T19:31:36.2130000Z ~ 69cdc98ad385e3b94310f7b5.jsonl[873] _id=69ebc5191724f0c9e2fbbebb ts=2026-04-24T19:31:36.2150000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `485ms: 69cdc98ad385e3b94310f7b5.jsonl[294] _id=69e91f861724f0c9e2faa002 ts=2026-04-22T19:20:38.2450000Z ~ 69cdc98ad385e3b94310f7b5.jsonl[1722] _id=69e91f871724f0c9e2faa005 ts=2026-04-22T19:20:38.7300000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 89h 54m 
  - Evidence: 89h 54m: 69cdc98ad385e3b94310f7b5.jsonl[290] _id=69e16c781724f0c9e2f717b6 ts=2026-04-16T23:10:47.7830000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1745] _id=69e65ccf1724f0c9e2f8b5df ts=2026-04-20T17:05:17.4700000Z; 46h 48m: 69cdc98ad385e3b94310f7b5.jsonl[2684] _id=69e929ba1724f0c9e2fac3cd ts=2026-04-22T20:04:09.8580000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2694] _id=69ebbc041724f0c9e2fbb045 ts=2026-04-24T18:52:51.5400000Z; 46h 43m: 69cdc98ad385e3b94310f7b5.jsonl[72] _id=69de9f057957a33870f3b75f ts=2026-04-14T20:09:41.3450000Z -> 69cdc98ad385e3b94310f7b5.jsonl[74] _id=69e130061724f0c9e2f690e0 ts=2026-04-16T18:52:53.0720000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 459 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc98ad385e3b94310f7b5.jsonl[1670] _id=69e141cd1724f0c9e2f712f8 ts=2026-04-16T20:08:44.4420000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1665] _id=69e141cd1724f0c9e2f712fa ts=2026-04-16T20:08:44.4440000Z; 2ms: 69cdc98ad385e3b94310f7b5.jsonl[894] _id=69ebc53d1724f0c9e2fbbefb ts=2026-04-24T19:32:12.3780000Z -> 69cdc98ad385e3b94310f7b5.jsonl[895] _id=69ebc53d1724f0c9e2fbbefd ts=2026-04-24T19:32:12.3800000Z; 3ms: 69cdc98ad385e3b94310f7b5.jsonl[1082] _id=69de9ac17957a33870f3a5d7 ts=2026-04-14T19:51:29.3450000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1086] _id=69de9ac17957a33870f3a5d9 ts=2026-04-14T19:51:29.3480000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 69cdc98ad385e3b94310f7b5.jsonl[1161] _id=69de9e497957a33870f3b4f9 ts=2026-04-14T20:06:33.7170000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2264] _id=69e687671724f0c9e2f9001d ts=2026-04-20T20:07:03.4980000Z; 47h 55m: 69cdc98ad385e3b94310f7b5.jsonl[2264] _id=69e687671724f0c9e2f9001d ts=2026-04-20T20:07:03.4980000Z -> 69cdc98ad385e3b94310f7b5.jsonl[560] _id=69e929411724f0c9e2fac1f9 ts=2026-04-22T20:02:09.5060000Z; 47h 29m: 69cdc98ad385e3b94310f7b5.jsonl[560] _id=69e929411724f0c9e2fac1f9 ts=2026-04-22T20:02:09.5060000Z -> 69cdc98ad385e3b94310f7b5.jsonl[884] _id=69ebc50f1724f0c9e2fbbeaf ts=2026-04-24T19:31:27.3470000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 89h 54m 
  - Evidence: 89h 54m: 69cdc98ad385e3b94310f7b5.jsonl[291] _id=69e16c811724f0c9e2f717ba ts=2026-04-16T23:10:56.6290000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1737] _id=69e65ccb1724f0c9e2f8b5dd ts=2026-04-20T17:05:14.8620000Z; 46h 47m: 69cdc98ad385e3b94310f7b5.jsonl[2687] _id=69e929de1724f0c9e2fac43b ts=2026-04-22T20:04:46.6030000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2688] _id=69ebbbf01724f0c9e2fbb03f ts=2026-04-24T18:52:31.1190000Z; 46h 43m: 69cdc98ad385e3b94310f7b5.jsonl[1173] _id=69de9ef67957a33870f3b747 ts=2026-04-14T20:09:26.6560000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1190] _id=69e130021724f0c9e2f690c4 ts=2026-04-16T18:52:48.5480000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 89h 56m 
  - Evidence: 89h 56m: 69cdc98ad385e3b94310f7b5.jsonl[287] _id=69e16c711724f0c9e2f717ae ts=2026-04-16T23:10:41.0710000Z -> 69cdc98ad385e3b94310f7b5.jsonl[300] _id=69e65d311724f0c9e2f8b5ff ts=2026-04-20T17:06:56.9530000Z; 47h 20m: 69cdc98ad385e3b94310f7b5.jsonl[2044] _id=69e67e5f1724f0c9e2f8dff1 ts=2026-04-20T19:28:30.9780000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2306] _id=69e918371724f0c9e2fa8297 ts=2026-04-22T18:49:27.4660000Z; 2h 21m: 69cdc98ad385e3b94310f7b5.jsonl[300] _id=69e65d311724f0c9e2f8b5ff ts=2026-04-20T17:06:56.9530000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2042] _id=69e67e421724f0c9e2f8df75 ts=2026-04-20T19:28:02.4330000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 1m 
  - Evidence: 95h 1m: 69cdc98ad385e3b94310f7b5.jsonl[144] _id=69e13e411724f0c9e2f70458 ts=2026-04-16T19:53:36.8130000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1796] _id=69e6766f1724f0c9e2f8bb2f ts=2026-04-20T18:54:38.7570000Z; 36m 25s: 69cdc98ad385e3b94310f7b5.jsonl[1940] _id=69e67b851724f0c9e2f8d255 ts=2026-04-20T19:16:21.4940000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2178] _id=69e6840e1724f0c9e2f8f6ed ts=2026-04-20T19:52:46.6450000Z; 27m 0s: 69cdc98ad385e3b94310f7b5.jsonl[79] _id=69e133901724f0c9e2f6a168 ts=2026-04-16T19:07:59.4370000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1436] _id=69e139e51724f0c9e2f6ec9d ts=2026-04-16T19:35:00.1210000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 58m 
  - Evidence: 94h 58m: 69cdc98ad385e3b94310f7b5.jsonl[1561] _id=69e13e3f1724f0c9e2f70451 ts=2026-04-16T19:53:34.8230000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1782] _id=69e675eb1724f0c9e2f8b9b3 ts=2026-04-20T18:52:26.9370000Z; 35m 35s: 69cdc98ad385e3b94310f7b5.jsonl[1939] _id=69e67b821724f0c9e2f8d247 ts=2026-04-20T19:16:17.7980000Z -> 69cdc98ad385e3b94310f7b5.jsonl[392] _id=69e683d91724f0c9e2f8f657 ts=2026-04-20T19:51:53.0420000Z; 17m 55s: 69cdc98ad385e3b94310f7b5.jsonl[1802] _id=69e676b21724f0c9e2f8bc5b ts=2026-04-20T18:55:45.9200000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1916] _id=69e67ae51724f0c9e2f8cf67 ts=2026-04-20T19:13:40.9280000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 18m 
  - Evidence: 143h 18m: 69cdc98ad385e3b94310f7b5.jsonl[1119] _id=69de9d587957a33870f3b19f ts=2026-04-14T20:02:32.2640000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1981] _id=69e67c921724f0c9e2f8d741 ts=2026-04-20T19:20:49.9680000Z; 48h 21m: 69cdc98ad385e3b94310f7b5.jsonl[337] _id=69e67d181724f0c9e2f8da31 ts=2026-04-20T19:23:03.0640000Z -> 69cdc98ad385e3b94310f7b5.jsonl[471] _id=69e925161724f0c9e2fab33d ts=2026-04-22T19:44:22.6340000Z; 47h 33m: 69cdc98ad385e3b94310f7b5.jsonl[471] _id=69e925161724f0c9e2fab33d ts=2026-04-22T19:44:22.6340000Z -> 69cdc98ad385e3b94310f7b5.jsonl[725] _id=69ebc1c81724f0c9e2fbb8ad ts=2026-04-24T19:17:27.8090000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 18m 
  - Evidence: 143h 18m: 69cdc98ad385e3b94310f7b5.jsonl[1122] _id=69de9d567957a33870f3b193 ts=2026-04-14T20:02:30.6320000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1983] _id=69e67ca51724f0c9e2f8d7c1 ts=2026-04-20T19:21:09.4850000Z; 12m 14s: 69cdc98ad385e3b94310f7b5.jsonl[1071] _id=69de9a747957a33870f3a449 ts=2026-04-14T19:50:12.5330000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1115] _id=69de9d537957a33870f3b17d ts=2026-04-14T20:02:27.2770000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc98ad385e3b94310f7b5.jsonl[2508] _id=69e925151724f0c9e2fab32f ts=2026-04-22T19:44:20.6300000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2507] _id=69e925151724f0c9e2fab331 ts=2026-04-22T19:44:20.6320000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 89h 54m 
  - Evidence: 89h 54m: 69cdc98ad385e3b94310f7b5.jsonl[1714] _id=69e16c671724f0c9e2f717a4 ts=2026-04-16T23:10:30.8080000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1738] _id=69e65cd01724f0c9e2f8b5e3 ts=2026-04-20T17:05:18.3400000Z; 46h 49m: 69cdc98ad385e3b94310f7b5.jsonl[2669] _id=69e929641724f0c9e2fac295 ts=2026-04-22T20:02:44.5560000Z -> 69cdc98ad385e3b94310f7b5.jsonl[2689] _id=69ebbbf21724f0c9e2fbb041 ts=2026-04-24T18:52:33.3290000Z; 46h 43m: 69cdc98ad385e3b94310f7b5.jsonl[1089] _id=69de9f017957a33870f3b757 ts=2026-04-14T20:09:36.8800000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1191] _id=69e130041724f0c9e2f690d6 ts=2026-04-16T18:52:51.6800000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc98ad385e3b94310f7b5.jsonl[565] _id=69ebc5191724f0c9e2fbbeb9 ts=2026-04-24T19:31:36.2130000Z -> 69cdc98ad385e3b94310f7b5.jsonl[873] _id=69ebc5191724f0c9e2fbbebb ts=2026-04-24T19:31:36.2150000Z; 3ms: 69cdc98ad385e3b94310f7b5.jsonl[1043] _id=69de99dc7957a33870f3a16b ts=2026-04-14T19:47:40.0480000Z -> 69cdc98ad385e3b94310f7b5.jsonl[21] _id=69de99dc7957a33870f3a16d ts=2026-04-14T19:47:40.0510000Z; 3ms: 69cdc98ad385e3b94310f7b5.jsonl[1097] _id=69de9d337957a33870f3b0d1 ts=2026-04-14T20:01:55.1110000Z -> 69cdc98ad385e3b94310f7b5.jsonl[1104] _id=69de9d337957a33870f3b0d3 ts=2026-04-14T20:01:55.1140000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7b5.jsonl:69cdc98ad385e3b94310f7b5, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[1589] _id=69e13f811724f0c9e2f708dc ts=2026-04-16T19:58:56.4430000Z`; `69cdc98ad385e3b94310f7b5.jsonl[2044] _id=69e67e5f1724f0c9e2f8dff1 ts=2026-04-20T19:28:30.9780000Z`; `69cdc98ad385e3b94310f7b5.jsonl[2314] _id=69e9185a1724f0c9e2fa82c9 ts=2026-04-22T18:50:01.9760000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 34 record(s) match the trigger in 69cdc98ad385e3b94310f7b5.jsonl:69cdc98ad385e3b94310f7b5, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[1451] _id=69e13a7e1724f0c9e2f6f368 ts=2026-04-16T19:37:33.3750000Z`; `69cdc98ad385e3b94310f7b5.jsonl[1453] _id=69e13a7f1724f0c9e2f6f374 ts=2026-04-16T19:37:34.6640000Z`; `69cdc98ad385e3b94310f7b5.jsonl[1449] _id=69e13a871724f0c9e2f6f392 ts=2026-04-16T19:37:42.9250000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[310] _id=69e6781e1724f0c9e2f8c2e5 ts=2026-04-20T19:01:50.0210000Z`; `69cdc98ad385e3b94310f7b5.jsonl[1863] _id=69e678f81724f0c9e2f8c6c1 ts=2026-04-20T19:05:27.4690000Z`; `69cdc98ad385e3b94310f7b5.jsonl[2422] _id=69e921fa1724f0c9e2faa6fd ts=2026-04-22T19:31:05.6430000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[337] _id=69e67d181724f0c9e2f8da31 ts=2026-04-20T19:23:03.0640000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[2508] _id=69e925151724f0c9e2fab32f ts=2026-04-22T19:44:20.6300000Z`; `69cdc98ad385e3b94310f7b5.jsonl[2507] _id=69e925151724f0c9e2fab331 ts=2026-04-22T19:44:20.6320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[2340] _id=69e91a101724f0c9e2fa89a1 ts=?`; `69cdc98ad385e3b94310f7b5.jsonl[2693] _id=69ebbc1d1724f0c9e2fbb059 ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7b5.jsonl[177] _id=69e15b671724f0c9e2f7166e ts=2026-04-16T21:57:58.3420000Z`; `69cdc98ad385e3b94310f7b5.jsonl[195] _id=69e15c3f1724f0c9e2f7169e ts=2026-04-16T22:01:34.5840000Z`; `69cdc98ad385e3b94310f7b5.jsonl[254] _id=69e15ced1724f0c9e2f716ce ts=2026-04-16T22:04:28.9770000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 187 unmatched 'DialogueStartEvent' (totals: 371 start, 187 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'Started' (totals: 11 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 30 unmatched 'questActiveEvent' (totals: 62 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.51s, min -3.59s, max -0.14s over 2701 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b5\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=complete 
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
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 38 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1816 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (508); Unit 3 Dev (315); Unit 4 Dev (229); Unit 1 Dev (219); Unit 5 Dev (194); Unit 4 Dev - Anderson Base (107); Unit 3 Dungeon Dev (97); Unit 4 Dev - Dungeon (92); Unit 5 Dev - Dungeon (55)
- **eventKey:** present on 1258 of 1816 records
- **Intervals:** median 2.51s (p5 0.01s / p95 54.70s, n=1815)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1258; [conversationId, dialogueEventType] x558
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1816/1816 records)
    numeric range 10 .. 114 (47 unique)
data.dialogueEventType  (string, 1816/1816 records)
    "DialogueNodeEvent"  x1258
    "DialogueStartEvent"  x371
    "DialogueFinishEvent"  x187
data.nodeId  (number, 1258/1816 records)
    numeric range 0 .. 289 (211 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 615 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (181); Unit 3 Dev (108); Unit 4 Dev (78); Unit 4 Dev - Dungeon (59); Unit 1 Dev (57); Unit 5 Dev (46); Unit 3 Dungeon Dev (33); Unit 5 Dev - Dungeon (30); Unit 4 Dev - Anderson Base (23)
- **Intervals:** median 30.00s (p5 29.97s / p95 49.10s, n=603)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 615/615 records)
data.position.x  (number, 615/615 records)
    numeric range -707.73 .. 1621.62 (362 unique)
data.position.y  (number, 615/615 records)
    numeric range -114.326 .. 217.936 (299 unique)
data.position.z  (number, 615/615 records)
    numeric range -1110.7 .. 2121.41 (362 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 94 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (29); Unit 1 Dev (17); Unit 3 Dev (9); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev (9); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 94 of 94 records
- **Intervals:** median 155.68s (p5 0.01s / p95 6244.68s, n=93)
- **`data` key-set variants:** [questEventType, questID, questName] x62; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Fields under `data`:**

```text
data.questEventType  (string, 94/94 records)
    "questActiveEvent"  x62
    "questFinishEvent"  x32
data.questID  (string, 94/94 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 94/94 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/94 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 38 records

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (16)
- **Intervals:** median 35.70s (p5 6.30s / p95 1733.58s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "MapCloseEvent"  x19
    "MapOpenEvent"  x19
data.featureUsed  (string, 38/38 records)
    "Map"  x38
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 34 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (16)
- **Intervals:** median 11.63s (p5 1.32s / p95 1499.10s, n=33)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "dragEnd"  x17
    "dragStart"  x17
data.featureUsed  (string, 34/34 records)
    "waypoint"  x34
data.location  (object, 34/34 records)
data.location.x  (number, 34/34 records)
    numeric range -770.79 .. 276.611 (18 unique)
data.location.y  (number, 34/34 records)
    numeric range -307.4 .. 180.45 (18 unique)
data.location.z  (number, 34/34 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `WaterChamberEvent` — 29 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (29)
- **Intervals:** median 9.04s (p5 2.84s / p95 48.24s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "On"  x19
    "Off"  x10
data.floor  (string, 29/29 records)
    "4"  x16
    "3"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 29/29 records)
    "One"  x28
    "Two"  x1
data.machineType  (string, 29/29 records)
    "Condenser"  x12
    "Evaporator"  x12
    "VentSwitch"  x3
    "DualChamber_Condenser"  x1
    "DualChamber_Evaporator"  x1
data.room  (string, 29/29 records)
    "3"  x15
    "2"  x7
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 15 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (7)
- **Intervals:** median 8.48s (p5 1.34s / p95 181049.18s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationNodeAdd"  x12
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 15/15 records)
    "Unit 1 - Freshwater"  x8
    "Unit 3 - Pollution Upstream"  x7
data.nodeName  (string, 15/15 records)
    "A"  x5
    "B"  x4
    "I"  x3
    "1"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 14 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 221.62s (p5 32.12s / p95 231784.25s, n=13)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 14/14 records)
    "Started"  x11
    "Finished"  x3
data.Unit  (string, 14/14 records)
    "Unit 2 Prod (Refactor)"  x10
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 68.60s (p5 4.68s / p95 310806.82s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 14/14 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 11 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (11)
- **Intervals:** median 7.20s (p5 0.89s / p95 211.60s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "ChangeCanister"  x11
data.canisterType  (string, 11/11 records)
    "Bedrock"  x5
    "Clay"  x3
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 11/11 records)
    "5"  x10
    "4"  x1
data.machine  (string, 11/11 records)
    "1"  x9
    "2"  x2
data.row  (string, 11/11 records)
    "BottomRow"  x7
    "TopRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (10)
- **Intervals:** median 4.19s (p5 0.58s / p95 87.62s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x4
data.argumentationTitle  (string, 10/10 records)
    "Unit 4 - Flooding"  x10
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Soil Flow Rates"  x8
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 10.84s (p5 1.40s / p95 24.79s, n=6)
- **`data` key-set variants:** [actionType, boxId, soilType] x4; [actionType, boxID, soilType] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "cameraPlaced"  x4
    "soilSelected"  x3
data.boxID  (string, 3/7 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.boxId  (string, 4/7 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 7/7 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 172506.01s (p5 171112.66s / p95 483837.40s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Uncaught ReferenceError: onResize is not defined"  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit5:831:9)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x2
data.unitId  (string, 2/2 records)
    "unit4"  x1
    "unit5"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (10 records)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "dragStart" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*