# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77c
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f77c.jsonl
- **Records:** 2179 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f77c
- **Time span:** 2026-04-14T13:53:48.995000+00:00 .. 2026-04-24T14:34:38.722000+00:00 (240h 40m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2179 records, 8 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 65 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 1479 | 67.88 | 1 | 8 | 991 | 2026-04-14T13:54:07.168000+00:00 | 2026-04-24T14:34:29.173000+00:00 | 240h 40m |
| PlayerPositionEvent | 515 | 23.63 | 1 | 8 | 0 | 2026-04-14T13:53:48.995000+00:00 | 2026-04-24T14:34:38.722000+00:00 | 240h 40m |
| questEvent | 60 | 2.75 | 1 | 8 | 60 | 2026-04-14T13:54:07.153000+00:00 | 2026-04-24T14:34:37.928000+00:00 | 240h 40m |
| TopographicMapEvent | 30 | 1.38 | 1 | 2 | 0 | 2026-04-16T14:00:09.658000+00:00 | 2026-04-22T13:44:19.498000+00:00 | 143h 44m |
| Topographic Map Event | 22 | 1.01 | 1 | 2 | 0 | 2026-04-16T13:56:16.465000+00:00 | 2026-04-22T13:45:29.221000+00:00 | 143h 49m |
| argumentationToolEvent | 18 | 0.83 | 1 | 1 | 0 | 2026-04-24T14:10:20.063000+00:00 | 2026-04-24T14:15:29.950000+00:00 | 5m 9s |
| argumentationNodeEvent | 16 | 0.73 | 1 | 2 | 0 | 2026-04-14T14:15:54.371000+00:00 | 2026-04-20T14:25:03.506000+00:00 | 144h 9m |
| Soil Key Puzzle | 8 | 0.37 | 1 | 3 | 0 | 2026-04-16T14:15:22.526000+00:00 | 2026-04-22T13:57:30.283000+00:00 | 143h 42m |
| TerasGardenBox | 8 | 0.37 | 1 | 1 | 0 | 2026-04-24T14:21:43.996000+00:00 | 2026-04-24T14:22:46.798000+00:00 | 1m 2s |
| argumentationEvent | 8 | 0.37 | 1 | 3 | 0 | 2026-04-14T14:15:41.373000+00:00 | 2026-04-24T14:10:23.127000+00:00 | 239h 54m |
| soilMachine | 7 | 0.32 | 1 | 1 | 0 | 2026-04-22T14:12:45.115000+00:00 | 2026-04-22T14:26:54.020000+00:00 | 14m 8s |
| WaterChamberEvent | 5 | 0.23 | 1 | 1 | 0 | 2026-04-24T14:33:08.606000+00:00 | 2026-04-24T14:34:12.863000+00:00 | 1m 4s |
| EndOfUnit | 3 | 0.14 | 1 | 3 | 0 | 2026-04-14T14:21:43.967000+00:00 | 2026-04-24T14:28:32.576000+00:00 | 240h 6m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 432204.304s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.018s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 258.767s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 9.62s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.852s median 
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
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
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
  - Observed: 22 records this build 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 5 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `WaterChamberEvent` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineNumber` — baseline categorical value(s) not seen this build. 
  - Observed: Two 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Condenser; DualChamber_Evaporator; VentSwitch 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.room` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 16 records 
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
  - Observed: 2; 4; C; D; II 
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
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 44; 45; 52; 53; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 6 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f77c.jsonl[521] _id=69de4c967957a33870f355c1 ts=2026-04-14T14:17:56.9070000Z`; `69cdc965d385e3b94310f77c.jsonl[791] _id=69e0eb5c7957a33870f522ee ts=2026-04-16T13:59:55.0540000Z`; `69cdc965d385e3b94310f77c.jsonl[1334] _id=69e637411724f0c9e2f8a8c5 ts=2026-04-20T14:25:04.9260000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 22 records, TopographicMapEvent: 30 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 4 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1478 | 0.003 | 2.562 | 586.212 | 47.349 | 341809.127 | 0.1 | 402 | 4 |
| PlayerPositionEvent | 504 | 29.78 | 30.018 | 1717.993 | 33.382 | 341803.108 | 0.03 | 0 | 4 |
| questEvent | 59 | 0.004 | 214.445 | 14685.267 | 168224.408 | 341993.657 | 0.0 | 9 | 11 |
| TopographicMapEvent | 29 | 0.325 | 3.188 | 17843.098 | 932.778 | 515453.344 | 0.0 | 0 | 2 |
| Topographic Map Event | 21 | 2.736 | 24.14 | 24654.893 | 1408.687 | 515492.576 | 0.0 | 0 | 2 |
| argumentationToolEvent | 17 | 0.003 | 0.852 | 18.229 | 114.961 | 198.199 | 3.29 | 1 | 0 |
| argumentationNodeEvent | 15 | 1.282 | 9.62 | 34596.609 | 155678.977 | 518742.701 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 7 | 21.657 | 258.767 | 73903.965 | 291222.325 | 342930.731 | 0.0 | 0 | 3 |
| TerasGardenBox | 7 | 1.935 | 5.507 | 8.972 | 21.638 | 25.536 | 6.69 | 0 | 0 |
| argumentationEvent | 7 | 0.103 | 49.22 | 123383.108 | 466523.811 | 518726.246 | 0.0 | 0 | 2 |
| soilMachine | 6 | 21.195 | 118.706 | 141.484 | 294.807 | 316.374 | 0.42 | 0 | 0 |
| WaterChamberEvent | 4 | 2.116 | 14.69 | 16.064 | 31.814 | 32.761 | 3.74 | 0 | 0 |
| EndOfUnit | 2 | 175182.486 | 432204.304 | 432204.305 | 663523.941 | 689226.123 | 0.0 | 0 | 2 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.018s (p5 29.95s, p95 33.38s, n=504) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `103ms: 69cdc965d385e3b94310f77c.jsonl[1330] _id=69e637411724f0c9e2f8a8c3 ts=2026-04-20T14:25:04.8960000Z ~ 69cdc965d385e3b94310f77c.jsonl[103] _id=69e637421724f0c9e2f8a8cf ts=2026-04-20T14:25:04.9990000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 69cdc965d385e3b94310f77c.jsonl[1937] _id=69eb79cc1724f0c9e2fb85f7 ts=2026-04-24T14:10:20.0630000Z ~ 69cdc965d385e3b94310f77c.jsonl[1938] _id=69eb79cc1724f0c9e2fb85f9 ts=2026-04-24T14:10:20.0660000Z`; `768ms: 69cdc965d385e3b94310f77c.jsonl[240] _id=69eb7a941724f0c9e2fb8a11 ts=2026-04-24T14:13:40.1290000Z ~ 69cdc965d385e3b94310f77c.jsonl[1967] _id=69eb7a951724f0c9e2fb8a15 ts=2026-04-24T14:13:40.8970000Z`; `99ms: 69cdc965d385e3b94310f77c.jsonl[1967] _id=69eb7a951724f0c9e2fb8a15 ts=2026-04-24T14:13:40.8970000Z ~ 69cdc965d385e3b94310f77c.jsonl[1971] _id=69eb7a961724f0c9e2fb8a1b ts=2026-04-24T14:13:40.9960000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 56m 
  - Evidence: 94h 56m: 69cdc965d385e3b94310f77c.jsonl[1008] _id=69e0f3b07957a33870f558f7 ts=2026-04-16T14:35:28.1150000Z -> 69cdc965d385e3b94310f77c.jsonl[1011] _id=69e62ae31724f0c9e2f85c93 ts=2026-04-20T13:32:17.2420000Z; 47h 30m: 69cdc965d385e3b94310f77c.jsonl[1818] _id=69e8db1e1724f0c9e2fa745d ts=2026-04-22T14:28:45.6250000Z -> 69cdc965d385e3b94310f77c.jsonl[1829] _id=69eb77321724f0c9e2fb7841 ts=2026-04-24T13:59:13.6030000Z; 47h 6m: 69cdc965d385e3b94310f77c.jsonl[627] _id=69de4fbd7957a33870f36a80 ts=2026-04-14T14:31:23.8780000Z -> 69cdc965d385e3b94310f77c.jsonl[632] _id=69e0e6547957a33870f5023f ts=2026-04-16T13:38:15.3990000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 402 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f77c.jsonl[141] _id=69e8cf881724f0c9e2fa2ce1 ts=2026-04-22T13:39:20.1170000Z -> 69cdc965d385e3b94310f77c.jsonl[1516] _id=69e8cf881724f0c9e2fa2ce3 ts=2026-04-22T13:39:20.1200000Z; 3ms: 69cdc965d385e3b94310f77c.jsonl[19] _id=69de4cfe7957a33870f357c1 ts=2026-04-14T14:19:40.2160000Z -> 69cdc965d385e3b94310f77c.jsonl[542] _id=69de4cfe7957a33870f357c3 ts=2026-04-14T14:19:40.2190000Z; 3ms: 69cdc965d385e3b94310f77c.jsonl[2046] _id=69eb7bf41724f0c9e2fb90bb ts=2026-04-24T14:19:31.7770000Z -> 69cdc965d385e3b94310f77c.jsonl[2042] _id=69eb7bf41724f0c9e2fb90bd ts=2026-04-24T14:19:31.7800000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 27m 
  - Evidence: 191h 27m: 69cdc965d385e3b94310f77c.jsonl[567] _id=69de4d797957a33870f35b09 ts=2026-04-14T14:21:43.9670000Z -> 69cdc965d385e3b94310f77c.jsonl[177] _id=69e8d1c21724f0c9e2fa3db9 ts=2026-04-22T13:48:50.0900000Z; 48h 39m: 69cdc965d385e3b94310f77c.jsonl[177] _id=69e8d1c21724f0c9e2fa3db9 ts=2026-04-22T13:48:50.0900000Z -> 69cdc965d385e3b94310f77c.jsonl[2146] _id=69eb7e101724f0c9e2fb9add ts=2026-04-24T14:28:32.5760000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 56m 
  - Evidence: 94h 56m: 69cdc965d385e3b94310f77c.jsonl[1009] _id=69e0f3b37957a33870f55901 ts=2026-04-16T14:35:31.1100000Z -> 69cdc965d385e3b94310f77c.jsonl[1013] _id=69e62ade1724f0c9e2f85c7b ts=2026-04-20T13:32:14.2180000Z; 47h 28m: 69cdc965d385e3b94310f77c.jsonl[1821] _id=69e8db611724f0c9e2fa74e1 ts=2026-04-22T14:29:53.0070000Z -> 69cdc965d385e3b94310f77c.jsonl[1822] _id=69eb77051724f0c9e2fb775d ts=2026-04-24T13:58:29.1670000Z; 47h 7m: 69cdc965d385e3b94310f77c.jsonl[623] _id=69de4fad7957a33870f36a16 ts=2026-04-14T14:31:07.6370000Z -> 69cdc965d385e3b94310f77c.jsonl[630] _id=69e0e6437957a33870f501f1 ts=2026-04-16T13:38:10.3190000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 15m 
  - Evidence: 95h 15m: 69cdc965d385e3b94310f77c.jsonl[896] _id=69e0efeb7957a33870f53d0f ts=2026-04-16T14:19:22.2120000Z -> 69cdc965d385e3b94310f77c.jsonl[67] _id=69e62b7d1724f0c9e2f861a3 ts=2026-04-20T13:34:52.9430000Z; 47h 22m: 69cdc965d385e3b94310f77c.jsonl[1396] _id=69e639681724f0c9e2f8b3c3 ts=2026-04-20T14:34:15.5010000Z -> 69cdc965d385e3b94310f77c.jsonl[179] _id=69e8d3b11724f0c9e2fa45b9 ts=2026-04-22T13:57:04.8770000Z; 54m 42s: 69cdc965d385e3b94310f77c.jsonl[1051] _id=69e62c801724f0c9e2f86991 ts=2026-04-20T13:39:11.7100000Z -> 69cdc965d385e3b94310f77c.jsonl[1394] _id=69e639521724f0c9e2f8b277 ts=2026-04-20T14:33:53.8440000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 11m 
  - Evidence: 143h 11m: 69cdc965d385e3b94310f77c.jsonl[971] _id=69e0f2917957a33870f54e95 ts=2026-04-16T14:30:40.8940000Z -> 69cdc965d385e3b94310f77c.jsonl[1553] _id=69e8d0351724f0c9e2fa32ef ts=2026-04-22T13:42:13.4700000Z; 23m 28s: 69cdc965d385e3b94310f77c.jsonl[834] _id=69e0ecef7957a33870f52ad3 ts=2026-04-16T14:06:38.2460000Z -> 69cdc965d385e3b94310f77c.jsonl[963] _id=69e0f26f7957a33870f54d95 ts=2026-04-16T14:30:06.9330000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 10m 
  - Evidence: 143h 10m: 69cdc965d385e3b94310f77c.jsonl[966] _id=69e0f28b7957a33870f54e41 ts=2026-04-16T14:30:34.4930000Z -> 69cdc965d385e3b94310f77c.jsonl[1543] _id=69e8d0081724f0c9e2fa315d ts=2026-04-22T13:41:27.8370000Z; 23m 38s: 69cdc965d385e3b94310f77c.jsonl[831] _id=69e0ece87957a33870f52a9d ts=2026-04-16T14:06:31.3050000Z -> 69cdc965d385e3b94310f77c.jsonl[932] _id=69e0f2737957a33870f54da9 ts=2026-04-16T14:30:10.2340000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 5m 
  - Evidence: 144h 5m: 69cdc965d385e3b94310f77c.jsonl[523] _id=69de4c967957a33870f355bf ts=2026-04-14T14:17:56.8860000Z -> 69cdc965d385e3b94310f77c.jsonl[1312] _id=69e636db1724f0c9e2f8a595 ts=2026-04-20T14:23:23.1320000Z; 95h 45m: 69cdc965d385e3b94310f77c.jsonl[103] _id=69e637421724f0c9e2f8a8cf ts=2026-04-20T14:25:04.9990000Z -> 69cdc965d385e3b94310f77c.jsonl[1939] _id=69eb79cf1724f0c9e2fb860d ts=2026-04-24T14:10:23.1270000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 5m 
  - Evidence: 144h 5m: 69cdc965d385e3b94310f77c.jsonl[520] _id=69de4c927957a33870f3559b ts=2026-04-14T14:17:52.3730000Z -> 69cdc965d385e3b94310f77c.jsonl[1314] _id=69e636e71724f0c9e2f8a61b ts=2026-04-20T14:23:35.0740000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f77c.jsonl[1937] _id=69eb79cc1724f0c9e2fb85f7 ts=2026-04-24T14:10:20.0630000Z -> 69cdc965d385e3b94310f77c.jsonl[1938] _id=69eb79cc1724f0c9e2fb85f9 ts=2026-04-24T14:10:20.0660000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 59m 
  - Evidence: 94h 59m: 69cdc965d385e3b94310f77c.jsonl[977] _id=69e0f2f97957a33870f552ca ts=2026-04-16T14:32:24.7870000Z -> 69cdc965d385e3b94310f77c.jsonl[65] _id=69e62ae31724f0c9e2f85c97 ts=2026-04-20T13:32:18.4440000Z; 47h 30m: 69cdc965d385e3b94310f77c.jsonl[1813] _id=69e8daeb1724f0c9e2fa72bb ts=2026-04-22T14:27:55.4610000Z -> 69cdc965d385e3b94310f77c.jsonl[1824] _id=69eb77081724f0c9e2fb7761 ts=2026-04-24T13:58:31.2060000Z; 47h 14m: 69cdc965d385e3b94310f77c.jsonl[579] _id=69de4df77957a33870f35df0 ts=2026-04-14T14:23:49.4810000Z -> 69cdc965d385e3b94310f77c.jsonl[631] _id=69e0e6547957a33870f5023b ts=2026-04-16T13:38:13.8170000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.004s..0.008s shown 
  - Evidence: 4ms: 69cdc965d385e3b94310f77c.jsonl[8] _id=69de4bc47957a33870f34e85 ts=2026-04-14T14:14:26.3800000Z -> 69cdc965d385e3b94310f77c.jsonl[491] _id=69de4bc47957a33870f34e87 ts=2026-04-14T14:14:26.3840000Z; 8ms: 69cdc965d385e3b94310f77c.jsonl[196] _id=69e8d6761724f0c9e2fa58e5 ts=2026-04-22T14:08:53.6190000Z -> 69cdc965d385e3b94310f77c.jsonl[197] _id=69e8d6761724f0c9e2fa58e9 ts=2026-04-22T14:08:53.6270000Z; 8ms: 69cdc965d385e3b94310f77c.jsonl[386] _id=69de48dd7957a33870f33959 ts=2026-04-14T14:02:03.1600000Z -> 69cdc965d385e3b94310f77c.jsonl[3] _id=69de48dd7957a33870f3395b ts=2026-04-14T14:02:03.1680000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc965d385e3b94310f77c.jsonl:69cdc965d385e3b94310f77c, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f77c.jsonl[896] _id=69e0efeb7957a33870f53d0f ts=2026-04-16T14:19:22.2120000Z`; `69cdc965d385e3b94310f77c.jsonl[1396] _id=69e639681724f0c9e2f8b3c3 ts=2026-04-20T14:34:15.5010000Z`; `69cdc965d385e3b94310f77c.jsonl[1655] _id=69e8d3ca1724f0c9e2fa462d ts=2026-04-22T13:57:30.2830000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 30 record(s) match the trigger in 69cdc965d385e3b94310f77c.jsonl:69cdc965d385e3b94310f77c, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f77c.jsonl[794] _id=69e0eb6a7957a33870f52337 ts=2026-04-16T14:00:09.6580000Z`; `69cdc965d385e3b94310f77c.jsonl[795] _id=69e0eb6a7957a33870f52339 ts=2026-04-16T14:00:09.9830000Z`; `69cdc965d385e3b94310f77c.jsonl[807] _id=69e0ec367957a33870f526a3 ts=2026-04-16T14:03:33.5340000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f77c.jsonl[1128] _id=69e630d71724f0c9e2f88063 ts=2026-04-20T13:57:42.3300000Z`; `69cdc965d385e3b94310f77c.jsonl[82] _id=69e631681724f0c9e2f88383 ts=2026-04-20T14:00:06.4990000Z`; `69cdc965d385e3b94310f77c.jsonl[1856] _id=69eb77b31724f0c9e2fb7ae5 ts=2026-04-24T14:01:22.9340000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f77c.jsonl[103] _id=69e637421724f0c9e2f8a8cf ts=2026-04-20T14:25:04.9990000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f77c.jsonl[1937] _id=69eb79cc1724f0c9e2fb85f7 ts=2026-04-24T14:10:20.0630000Z`; `69cdc965d385e3b94310f77c.jsonl[1938] _id=69eb79cc1724f0c9e2fb85f9 ts=2026-04-24T14:10:20.0660000Z`; `69cdc965d385e3b94310f77c.jsonl[1971] _id=69eb7a961724f0c9e2fb8a1b ts=2026-04-24T14:13:40.9960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f77c.jsonl[1051] _id=69e62c801724f0c9e2f86991 ts=2026-04-20T13:39:11.7100000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 187 unmatched 'DialogueStartEvent' (totals: 336 start, 152 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 5 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 36 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.72s, min -34.47s, max -0.40s over 2179 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77c\coverage.yaml

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
  - Observed: 22 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1479 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (383); Unit 2 Prod (Refactor) (353); Unit 4 Dev (231); Unit 1 Dev (176); Unit 4 Dev - Anderson Base (148); Unit 4 Dev - Dungeon (94); Unit 3 Dungeon Dev (78); Unit 5 Dev - Dungeon (16)
- **eventKey:** present on 991 of 1479 records
- **Intervals:** median 2.56s (p5 0.01s / p95 47.35s, n=1478)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x991; [conversationId, dialogueEventType] x488
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1479/1479 records)
    numeric range 10 .. 114 (42 unique)
data.dialogueEventType  (string, 1479/1479 records)
    "DialogueNodeEvent"  x991
    "DialogueStartEvent"  x336
    "DialogueFinishEvent"  x152
data.nodeId  (number, 991/1479 records)
    numeric range 0 .. 289 (206 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 515 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (144); Unit 3 Dev (110); Unit 4 Dev (63); Unit 1 Dev (56); Unit 4 Dev - Dungeon (55); Unit 3 Dungeon Dev (50); Unit 4 Dev - Anderson Base (25); Unit 5 Dev - Dungeon (12)
- **Intervals:** median 30.02s (p5 29.95s / p95 33.38s, n=504)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 515/515 records)
data.position.x  (number, 515/515 records)
    numeric range -729.08 .. 1557.57 (288 unique)
data.position.y  (number, 515/515 records)
    numeric range -114.326 .. 156.601 (232 unique)
data.position.z  (number, 515/515 records)
    numeric range -1114.81 .. 2118.86 (288 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 60 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (3); Unit 5 Dev - Dungeon (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 60 of 60 records
- **Intervals:** median 214.44s (p5 0.01s / p95 168224.41s, n=59)
- **`data` key-set variants:** [questEventType, questID, questName] x36; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Fields under `data`:**

```text
data.questEventType  (string, 60/60 records)
    "questActiveEvent"  x36
    "questFinishEvent"  x24
data.questID  (string, 60/60 records)
    27 unique values (see csv/event_unique_values.csv)
data.questName  (string, 60/60 records)
    27 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/60 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 30 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 3 Dev (14)
- **Intervals:** median 3.19s (p5 0.66s / p95 932.78s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "dragEnd"  x15
    "dragStart"  x15
data.featureUsed  (string, 30/30 records)
    "waypoint"  x30
data.location  (object, 30/30 records)
data.location.x  (number, 30/30 records)
    numeric range -770.79 .. 10.9789 (16 unique)
data.location.y  (number, 30/30 records)
    numeric range -314.494 .. 132.434 (17 unique)
data.location.z  (number, 30/30 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Topographic Map Event` — 22 records

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (10)
- **Intervals:** median 24.14s (p5 3.63s / p95 1408.69s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "MapCloseEvent"  x11
    "MapOpenEvent"  x11
data.featureUsed  (string, 22/22 records)
    "Map"  x22
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationToolEvent` — 18 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (18)
- **Intervals:** median 0.85s (p5 0.06s / p95 114.96s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationToolClose"  x11
    "argumentationToolOpen"  x7
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x18
data.toolName  (string, 18/18 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x12
    "BackingInfoPanel - Soil Flow Rates"  x6
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationNodeEvent` — 16 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (11); Unit 1 Dev (5)
- **Intervals:** median 9.62s (p5 2.13s / p95 155678.98s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationNodeAdd"  x12
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 16/16 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 16/16 records)
    "A"  x4
    "I"  x4
    "B"  x3
    "1"  x2
    "3"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 258.77s (p5 22.78s / p95 291222.32s, n=7)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Started"  x5
    "Finished"  x3
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 5.51s (p5 2.22s / p95 21.64s, n=7)
- **`data` key-set variants:** [actionType, boxID, soilType] x4; [actionType, boxId, soilType] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "cameraPlaced"  x4
    "soilSelected"  x4
data.boxID  (string, 4/8 records)
    "1"  x2
    "0"  x1
    "2"  x1
data.boxId  (string, 4/8 records)
    "1"  x2
    "0"  x1
    "2"  x1
data.soilType  (string, 8/8 records)
    "Clay"  x4
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 49.22s (p5 11.58s / p95 466523.81s, n=7)
- **Open findings:** 1 — see sections 5-8
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

### `soilMachine` — 7 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (7)
- **Intervals:** median 118.71s (p5 26.85s / p95 294.81s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "ChangeCanister"  x7
data.canisterType  (string, 7/7 records)
    "Gravel"  x3
    "Clay"  x2
    "Bedrock"  x1
    "Sand"  x1
data.floor  (string, 7/7 records)
    "5"  x5
    "3"  x1
    "4"  x1
data.machine  (string, 7/7 records)
    "1"  x5
    "2"  x2
data.row  (string, 7/7 records)
    "TopRow"  x6
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 5 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (5)
- **Intervals:** median 14.69s (p5 2.24s / p95 31.81s, n=4)
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "On"  x3
    "Off"  x2
data.floor  (string, 5/5 records)
    "1"  x5
data.machineNumber  (string, 5/5 records)
    "One"  x5
data.machineType  (string, 5/5 records)
    "Condenser"  x4
    "Evaporator"  x1
data.room  (string, 5/5 records)
    "3"  x4
    "2"  x1
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 432204.30s (p5 200884.67s / p95 663523.94s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
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
- `TopographicMapEvent` data.actionType: "dragStart" (15x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*