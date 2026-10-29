# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f720

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f720
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f720.jsonl
- **Records:** 2859 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f720
- **Time span:** 2026-04-13T17:53:59.981000+00:00 .. 2026-04-23T18:24:27.213000+00:00 (240h 30m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f720\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2859 records, 9 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 67 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 1947 | 68.1 | 1 | 9 | 1381 | 2026-04-13T17:54:18.378000+00:00 | 2026-04-23T18:24:08.211000+00:00 | 240h 29m |
| PlayerPositionEvent | 642 | 22.46 | 1 | 9 | 0 | 2026-04-13T17:53:59.981000+00:00 | 2026-04-23T18:24:27.213000+00:00 | 240h 30m |
| questEvent | 91 | 3.18 | 1 | 9 | 91 | 2026-04-13T17:54:18.353000+00:00 | 2026-04-23T18:23:56.733000+00:00 | 240h 29m |
| WaterChamberEvent | 47 | 1.64 | 1 | 1 | 0 | 2026-04-21T18:38:46.069000+00:00 | 2026-04-23T18:08:17.684000+00:00 | 47h 29m |
| Topographic Map Event | 29 | 1.01 | 1 | 2 | 0 | 2026-04-15T17:56:08.863000+00:00 | 2026-04-21T17:00:15.254000+00:00 | 143h 4m |
| soilMachine | 26 | 0.91 | 1 | 1 | 0 | 2026-04-21T17:51:51.954000+00:00 | 2026-04-21T17:59:54.351000+00:00 | 8m 2s |
| TopographicMapEvent | 23 | 0.8 | 1 | 2 | 0 | 2026-04-15T17:56:23.060000+00:00 | 2026-04-21T17:00:13.666000+00:00 | 143h 3m |
| argumentationNodeEvent | 19 | 0.66 | 1 | 3 | 0 | 2026-04-13T18:13:48.936000+00:00 | 2026-04-17T18:09:48.752000+00:00 | 95h 55m |
| Soil Key Puzzle | 12 | 0.42 | 1 | 3 | 0 | 2026-04-13T18:29:04.614000+00:00 | 2026-04-21T17:37:45.221000+00:00 | 191h 8m |
| argumentationEvent | 12 | 0.42 | 1 | 5 | 0 | 2026-04-13T18:13:39.238000+00:00 | 2026-04-23T18:14:41.995000+00:00 | 240h 1m |
| EndOfUnit | 5 | 0.17 | 1 | 5 | 0 | 2026-04-13T18:18:40.955000+00:00 | 2026-04-23T18:23:33.867000+00:00 | 240h 4m |
| TerasGardenBox | 3 | 0.1 | 1 | 1 | 0 | 2026-04-21T18:28:50.289000+00:00 | 2026-04-21T18:29:21.585000+00:00 | 31.3s |
| argumentationToolEvent | 2 | 0.07 | 1 | 1 | 0 | 2026-04-21T18:22:29.419000+00:00 | 2026-04-21T18:22:29.423000+00:00 | 0.0s |
| crash | 1 | 0.03 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 257716.982s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.006s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 43.981s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 15.648s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 19.613s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 3.423s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 9.181s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.004s median 
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
  - Observed: 2.72s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 12 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 11 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 29 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
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
  - Observed: 19 records 
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
  - Observed: 2; 3; 4; C 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationToolOpen 
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
  - Observed: BackingInfoPanel - Soil Flow Rates 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `soilMachine` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 20 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f720.jsonl[1127] _id=69dd32c37957a33870f26908 ts=2026-04-13T18:15:30.7560000Z`; `69cdc907d385e3b94310f720.jsonl[104] _id=69dd38357957a33870f28e2e ts=2026-04-13T18:38:45.2890000Z`; `69cdc907d385e3b94310f720.jsonl[161] _id=69dfd0a87957a33870f416d7 ts=2026-04-15T17:53:43.9630000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 29 records, TopographicMapEvent: 23 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1946 | 0.0 | 2.325 | 444.907 | 32.589 | 339581.771 | 0.13 | 469 | 6 |
| PlayerPositionEvent | 630 | 25.94 | 30.006 | 1373.604 | 33.174 | 339515.877 | 0.04 | 0 | 4 |
| questEvent | 90 | 0.002 | 124.375 | 9619.76 | 1979.126 | 339663.346 | 0.01 | 16 | 10 |
| WaterChamberEvent | 46 | 0.216 | 3.423 | 3716.774 | 29.296 | 170590.362 | 0.02 | 0 | 1 |
| Topographic Map Event | 28 | 1.844 | 30.621 | 18394.514 | 111248.779 | 339630.679 | 0.0 | 0 | 4 |
| soilMachine | 25 | 0.393 | 2.72 | 19.296 | 73.421 | 181.701 | 3.11 | 0 | 0 |
| TopographicMapEvent | 22 | 0.073 | 19.613 | 23410.482 | 162616.683 | 339600.956 | 0.0 | 0 | 4 |
| argumentationNodeEvent | 18 | 1.099 | 9.181 | 19186.656 | 54405.824 | 341416.618 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 11 | 2.958 | 43.981 | 62556.419 | 257889.049 | 343435.207 | 0.0 | 0 | 5 |
| argumentationEvent | 11 | 0.097 | 59.845 | 78551.16 | 343884.344 | 346364.65 | 0.0 | 0 | 4 |
| EndOfUnit | 4 | 5372.212 | 257716.982 | 216073.228 | 343453.5 | 343486.736 | 0.0 | 0 | 4 |
| TerasGardenBox | 2 | 14.636 | 15.648 | 15.648 | 16.559 | 16.66 | 3.83 | 0 | 0 |
| argumentationToolEvent | 1 | 0.004 | 0.004 | 0.004 | 0.004 | 0.004 | 15000.0 | 1 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.006s (p5 29.96s, p95 33.17s, n=630) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `216ms: 69cdc907d385e3b94310f720.jsonl[2688] _id=69ea5fee1724f0c9e2fb106c ts=2026-04-23T18:07:41.1040000Z ~ 69cdc907d385e3b94310f720.jsonl[2686] _id=69ea5fee1724f0c9e2fb106f ts=2026-04-23T18:07:41.3200000Z`; `305ms: 69cdc907d385e3b94310f720.jsonl[2686] _id=69ea5fee1724f0c9e2fb106f ts=2026-04-23T18:07:41.3200000Z ~ 69cdc907d385e3b94310f720.jsonl[2687] _id=69ea5fee1724f0c9e2fb1071 ts=2026-04-23T18:07:41.6250000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `97ms: 69cdc907d385e3b94310f720.jsonl[1980] _id=69e277701724f0c9e2f76bd7 ts=2026-04-17T18:09:52.1250000Z ~ 69cdc907d385e3b94310f720.jsonl[555] _id=69e277701724f0c9e2f76be0 ts=2026-04-17T18:09:52.2220000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 69cdc907d385e3b94310f720.jsonl[792] _id=69e7c0651724f0c9e2f98771 ts=2026-04-21T18:22:29.4190000Z ~ 69cdc907d385e3b94310f720.jsonl[793] _id=69e7c0651724f0c9e2f98773 ts=2026-04-21T18:22:29.4230000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 69cdc907d385e3b94310f720.jsonl[2763] _id=69ea61ca1724f0c9e2fb2125 ts=2026-04-23T18:15:38.0590000Z ~ 69cdc907d385e3b94310f720.jsonl[957] _id=69ea61cb1724f0c9e2fb212b ts=2026-04-23T18:15:38.0650000Z`; `5ms: 69cdc907d385e3b94310f720.jsonl[969] _id=69ea63131724f0c9e2fb2bdb ts=2026-04-23T18:21:07.2400000Z ~ 69cdc907d385e3b94310f720.jsonl[970] _id=69ea63141724f0c9e2fb2bdd ts=2026-04-23T18:21:07.2450000Z`; `2ms: 69cdc907d385e3b94310f720.jsonl[2855] _id=69ea63be1724f0c9e2fb307f ts=2026-04-23T18:23:56.7310000Z ~ 69cdc907d385e3b94310f720.jsonl[2856] _id=69ea63be1724f0c9e2fb3087 ts=2026-04-23T18:23:56.7330000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `393ms: 69cdc907d385e3b94310f720.jsonl[2380] _id=69e7ba421724f0c9e2f95935 ts=2026-04-21T17:56:18.4600000Z ~ 69cdc907d385e3b94310f720.jsonl[718] _id=69e7ba431724f0c9e2f9593b ts=2026-04-21T17:56:18.8530000Z`; `972ms: 69cdc907d385e3b94310f720.jsonl[2385] _id=69e7ba9f1724f0c9e2f95c3d ts=2026-04-21T17:57:51.6790000Z ~ 69cdc907d385e3b94310f720.jsonl[2386] _id=69e7baa01724f0c9e2f95c43 ts=2026-04-21T17:57:52.6510000Z`; `850ms: 69cdc907d385e3b94310f720.jsonl[2383] _id=69e7baa41724f0c9e2f95c6d ts=2026-04-21T17:57:56.4990000Z ~ 69cdc907d385e3b94310f720.jsonl[2389] _id=69e7baa51724f0c9e2f95c7b ts=2026-04-21T17:57:57.3490000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 19m 
  - Evidence: 94h 19m: 69cdc907d385e3b94310f720.jsonl[608] _id=69e27e8e1724f0c9e2f78d10 ts=2026-04-17T18:40:13.9350000Z -> 69cdc907d385e3b94310f720.jsonl[2157] _id=69e7ad0b1724f0c9e2f91b25 ts=2026-04-21T16:59:55.7060000Z; 47h 20m: 69cdc907d385e3b94310f720.jsonl[2643] _id=69e7c4921724f0c9e2f9a745 ts=2026-04-21T18:40:18.1790000Z -> 69cdc907d385e3b94310f720.jsonl[2648] _id=69ea5e3a1724f0c9e2fb04a1 ts=2026-04-23T18:00:26.1970000Z; 47h 5m: 69cdc907d385e3b94310f720.jsonl[142] _id=69dd38a67957a33870f29144 ts=2026-04-13T18:40:38.1790000Z -> 69cdc907d385e3b94310f720.jsonl[1291] _id=69dfced07957a33870f40ba7 ts=2026-04-15T17:45:52.6740000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 469 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f720.jsonl[2599] _id=69e7c31d1724f0c9e2f99c79 ts=2026-04-21T18:34:05.0920000Z -> 69cdc907d385e3b94310f720.jsonl[2602] _id=69e7c3451724f0c9e2f99d83 ts=2026-04-21T18:34:05.092Z; 0ms: 69cdc907d385e3b94310f720.jsonl[484] _id=69e271401724f0c9e2f744ca ts=2026-04-17T17:43:27.7160000Z -> 69cdc907d385e3b94310f720.jsonl[1854] _id=69e271581724f0c9e2f74568 ts=2026-04-17T17:43:27.716Z; 3ms: 69cdc907d385e3b94310f720.jsonl[1603] _id=69dfd8dd7957a33870f44ea5 ts=2026-04-15T18:28:45.1310000Z -> 69cdc907d385e3b94310f720.jsonl[1606] _id=69dfd8dd7957a33870f44ea7 ts=2026-04-15T18:28:45.1340000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 69cdc907d385e3b94310f720.jsonl[92] _id=69dd33817957a33870f26e76 ts=2026-04-13T18:18:40.9550000Z -> 69cdc907d385e3b94310f720.jsonl[1852] _id=69e2713f1724f0c9e2f744c8 ts=2026-04-17T17:43:27.6910000Z; 95h 21m: 69cdc907d385e3b94310f720.jsonl[1852] _id=69e2713f1724f0c9e2f744c8 ts=2026-04-17T17:43:27.6910000Z -> 69cdc907d385e3b94310f720.jsonl[2201] _id=69e7ae211724f0c9e2f92361 ts=2026-04-21T17:04:32.8540000Z; 47h 49m: 69cdc907d385e3b94310f720.jsonl[2598] _id=69e7c31d1724f0c9e2f99c76 ts=2026-04-21T18:34:05.0660000Z -> 69cdc907d385e3b94310f720.jsonl[2849] _id=69ea63a61724f0c9e2fb2ff3 ts=2026-04-23T18:23:33.8670000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 18m 
  - Evidence: 94h 18m: 69cdc907d385e3b94310f720.jsonl[2155] _id=69e27e8a1724f0c9e2f78d06 ts=2026-04-17T18:40:10.5980000Z -> 69cdc907d385e3b94310f720.jsonl[2156] _id=69e7acc71724f0c9e2f919a1 ts=2026-04-21T16:58:46.4750000Z; 47h 19m: 69cdc907d385e3b94310f720.jsonl[2644] _id=69e7c4a11724f0c9e2f9a78b ts=2026-04-21T18:40:33.1540000Z -> 69cdc907d385e3b94310f720.jsonl[2646] _id=69ea5e2b1724f0c9e2fb0471 ts=2026-04-23T18:00:10.2240000Z; 47h 5m: 69cdc907d385e3b94310f720.jsonl[143] _id=69dd38ab7957a33870f2915e ts=2026-04-13T18:40:43.7340000Z -> 69cdc907d385e3b94310f720.jsonl[1289] _id=69dfcecc7957a33870f40ba1 ts=2026-04-15T17:45:48.2720000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 69cdc907d385e3b94310f720.jsonl[2012] _id=69e278461724f0c9e2f77028 ts=2026-04-17T18:13:25.9740000Z -> 69cdc907d385e3b94310f720.jsonl[2276] _id=69e7b5d11724f0c9e2f93b85 ts=2026-04-21T17:37:21.1810000Z; 47h 52m: 69cdc907d385e3b94310f720.jsonl[1551] _id=69dfd6f87957a33870f4409f ts=2026-04-15T18:20:40.5170000Z -> 69cdc907d385e3b94310f720.jsonl[2011] _id=69e2782f1724f0c9e2f76fb0 ts=2026-04-17T18:13:03.4090000Z; 47h 23m: 69cdc907d385e3b94310f720.jsonl[112] _id=69dd35f37957a33870f27e80 ts=2026-04-13T18:29:07.5720000Z -> 69cdc907d385e3b94310f720.jsonl[1337] _id=69dfd06e7957a33870f4151d ts=2026-04-15T17:52:46.5640000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 20m 
  - Evidence: 94h 20m: 69cdc907d385e3b94310f720.jsonl[615] _id=69e27e6a1724f0c9e2f78c8a ts=2026-04-17T18:39:38.2630000Z -> 69cdc907d385e3b94310f720.jsonl[2159] _id=69e7ad191724f0c9e2f91b6f ts=2026-04-21T17:00:08.9420000Z; 47h 11m: 69cdc907d385e3b94310f720.jsonl[1658] _id=69dfda7b7957a33870f45d3b ts=2026-04-15T18:35:39.7790000Z -> 69cdc907d385e3b94310f720.jsonl[488] _id=69e2720b1724f0c9e2f74ac6 ts=2026-04-17T17:46:51.4080000Z; 39m 37s: 69cdc907d385e3b94310f720.jsonl[526] _id=69e274cb1724f0c9e2f75cba ts=2026-04-17T17:58:35.7580000Z -> 69cdc907d385e3b94310f720.jsonl[604] _id=69e27e151724f0c9e2f78a80 ts=2026-04-17T18:38:13.5290000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 20m 
  - Evidence: 94h 20m: 69cdc907d385e3b94310f720.jsonl[614] _id=69e27e691724f0c9e2f78c82 ts=2026-04-17T18:39:36.9770000Z -> 69cdc907d385e3b94310f720.jsonl[2161] _id=69e7acfa1724f0c9e2f91aa3 ts=2026-04-21T16:59:37.9330000Z; 47h 30m: 69cdc907d385e3b94310f720.jsonl[1511] _id=69dfd5f37957a33870f43a31 ts=2026-04-15T18:16:19.4870000Z -> 69cdc907d385e3b94310f720.jsonl[1874] _id=69e272161724f0c9e2f74b0b ts=2026-04-17T17:47:01.8940000Z; 42m 7s: 69cdc907d385e3b94310f720.jsonl[519] _id=69e274251724f0c9e2f758cc ts=2026-04-17T17:55:49.8020000Z -> 69cdc907d385e3b94310f720.jsonl[598] _id=69e27e051724f0c9e2f78a16 ts=2026-04-17T18:37:57.7240000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 23m 
  - Evidence: 47h 23m: 69cdc907d385e3b94310f720.jsonl[2638] _id=69e7c47d1724f0c9e2f9a6fd ts=2026-04-21T18:39:57.2050000Z -> 69cdc907d385e3b94310f720.jsonl[2658] _id=69ea5edc1724f0c9e2fb07e7 ts=2026-04-23T18:03:07.5670000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 69cdc907d385e3b94310f720.jsonl[555] _id=69e277701724f0c9e2f76be0 ts=2026-04-17T18:09:52.2220000Z -> 69cdc907d385e3b94310f720.jsonl[2498] _id=69e7c06d1724f0c9e2f987af ts=2026-04-21T18:22:36.8720000Z; 94h 50m: 69cdc907d385e3b94310f720.jsonl[1126] _id=69dd32c27957a33870f26906 ts=2026-04-13T18:15:30.7300000Z -> 69cdc907d385e3b94310f720.jsonl[1763] _id=69e2685e1724f0c9e2f733de ts=2026-04-17T17:05:34.7670000Z; 47h 51m: 69cdc907d385e3b94310f720.jsonl[2498] _id=69e7c06d1724f0c9e2f987af ts=2026-04-21T18:22:36.8720000Z -> 69cdc907d385e3b94310f720.jsonl[2747] _id=69ea61561724f0c9e2fb1c7d ts=2026-04-23T18:13:42.1500000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 50m 
  - Evidence: 94h 50m: 69cdc907d385e3b94310f720.jsonl[1125] _id=69dd32b87957a33870f268b6 ts=2026-04-13T18:15:20.0680000Z -> 69cdc907d385e3b94310f720.jsonl[428] _id=69e268601724f0c9e2f733ec ts=2026-04-17T17:05:36.6860000Z; 1h 2m: 69cdc907d385e3b94310f720.jsonl[443] _id=69e268a01724f0c9e2f735d0 ts=2026-04-17T17:06:40.4900000Z -> 69cdc907d385e3b94310f720.jsonl[1973] _id=69e2774d1724f0c9e2f76b20 ts=2026-04-17T18:09:17.3500000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.004s..0.004s shown 
  - Evidence: 4ms: 69cdc907d385e3b94310f720.jsonl[792] _id=69e7c0651724f0c9e2f98771 ts=2026-04-21T18:22:29.4190000Z -> 69cdc907d385e3b94310f720.jsonl[793] _id=69e7c0651724f0c9e2f98773 ts=2026-04-21T18:22:29.4230000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 21m 
  - Evidence: 94h 21m: 69cdc907d385e3b94310f720.jsonl[2147] _id=69e27dfa1724f0c9e2f789b6 ts=2026-04-17T18:37:46.7330000Z -> 69cdc907d385e3b94310f720.jsonl[621] _id=69e7acca1724f0c9e2f919b5 ts=2026-04-21T16:58:50.0790000Z; 47h 20m: 69cdc907d385e3b94310f720.jsonl[2641] _id=69e7c4831724f0c9e2f9a717 ts=2026-04-21T18:40:03.4230000Z -> 69cdc907d385e3b94310f720.jsonl[2647] _id=69ea5e2c1724f0c9e2fb0475 ts=2026-04-23T18:00:10.8570000Z; 47h 8m: 69cdc907d385e3b94310f720.jsonl[131] _id=69dd37d57957a33870f28afc ts=2026-04-13T18:37:08.5040000Z -> 69cdc907d385e3b94310f720.jsonl[1290] _id=69dfcecf7957a33870f40ba5 ts=2026-04-15T17:45:51.0950000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f720.jsonl[2640] _id=69e7c4831724f0c9e2f9a715 ts=2026-04-21T18:40:03.4210000Z -> 69cdc907d385e3b94310f720.jsonl[2641] _id=69e7c4831724f0c9e2f9a717 ts=2026-04-21T18:40:03.4230000Z; 2ms: 69cdc907d385e3b94310f720.jsonl[2855] _id=69ea63be1724f0c9e2fb307f ts=2026-04-23T18:23:56.7310000Z -> 69cdc907d385e3b94310f720.jsonl[2856] _id=69ea63be1724f0c9e2fb3087 ts=2026-04-23T18:23:56.7330000Z; 5ms: 69cdc907d385e3b94310f720.jsonl[969] _id=69ea63131724f0c9e2fb2bdb ts=2026-04-23T18:21:07.2400000Z -> 69cdc907d385e3b94310f720.jsonl[970] _id=69ea63141724f0c9e2fb2bdd ts=2026-04-23T18:21:07.2450000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc907d385e3b94310f720.jsonl:69cdc907d385e3b94310f720, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f720.jsonl[112] _id=69dd35f37957a33870f27e80 ts=2026-04-13T18:29:07.5720000Z`; `69cdc907d385e3b94310f720.jsonl[1338] _id=69dfd0717957a33870f41537 ts=2026-04-15T17:52:49.5360000Z`; `69cdc907d385e3b94310f720.jsonl[1451] _id=69dfd3847957a33870f42c87 ts=2026-04-15T18:05:56.3130000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 23 record(s) match the trigger in 69cdc907d385e3b94310f720.jsonl:69cdc907d385e3b94310f720, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f720.jsonl[1390] _id=69dfd1477957a33870f41c05 ts=2026-04-15T17:56:23.0600000Z`; `69cdc907d385e3b94310f720.jsonl[259] _id=69dfd43f7957a33870f43163 ts=2026-04-15T18:09:03.8620000Z`; `69cdc907d385e3b94310f720.jsonl[262] _id=69dfd4457957a33870f4317d ts=2026-04-15T18:09:09.3870000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f720.jsonl[1639] _id=69dfd9c07957a33870f45495 ts=2026-04-15T18:32:32.8290000Z`; `69cdc907d385e3b94310f720.jsonl[1901] _id=69e273491724f0c9e2f752f0 ts=2026-04-17T17:52:09.2780000Z`; `69cdc907d385e3b94310f720.jsonl[517] _id=69e273d61724f0c9e2f756b6 ts=2026-04-17T17:54:30.3680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f720.jsonl[555] _id=69e277701724f0c9e2f76be0 ts=2026-04-17T18:09:52.2220000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f720.jsonl[792] _id=69e7c0651724f0c9e2f98771 ts=2026-04-21T18:22:29.4190000Z`; `69cdc907d385e3b94310f720.jsonl[793] _id=69e7c0651724f0c9e2f98773 ts=2026-04-21T18:22:29.4230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc907d385e3b94310f720.jsonl[2601] _id=69e7c33c1724f0c9e2f99d41 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 186 unmatched 'DialogueStartEvent' (totals: 374 start, 192 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 54 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.17s, min -40.79s, max +0.01s over 2858 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f720\coverage.yaml

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
  - Observed: 29 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1947 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (779); Unit 3 Dev (265); Unit 4 Dev (221); Unit 1 Dev (188); Unit 5 Dev (158); Unit 4 Dev - Anderson Base (111); Unit 3 Dungeon Dev (91); Unit 4 Dev - Dungeon (90); Unit 5 Dev - Dungeon (44)
- **eventKey:** present on 1381 of 1947 records
- **Intervals:** median 2.32s (p5 0.01s / p95 32.59s, n=1946)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1381; [conversationId, dialogueEventType] x566
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1947/1947 records)
    numeric range 8 .. 114 (52 unique)
data.dialogueEventType  (string, 1947/1947 records)
    "DialogueNodeEvent"  x1381
    "DialogueStartEvent"  x374
    "DialogueFinishEvent"  x192
data.nodeId  (number, 1381/1947 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 642 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (247); Unit 4 Dev (101); Unit 3 Dev (74); Unit 1 Dev (50); Unit 4 Dev - Anderson Base (38); Unit 4 Dev - Dungeon (37); Unit 3 Dungeon Dev (35); Unit 5 Dev (31); Unit 5 Dev - Dungeon (29)
- **Intervals:** median 30.01s (p5 29.96s / p95 33.17s, n=630)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 642/642 records)
data.position.x  (number, 642/642 records)
    numeric range -696.29 .. 1552.99 (310 unique)
data.position.y  (number, 642/642 records)
    numeric range -114.326 .. 220.577 (249 unique)
data.position.z  (number, 642/642 records)
    numeric range -1107.6 .. 2127.96 (310 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 91 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (13); Unit 1 Dev (12); Unit 5 Dev - Dungeon (12); Unit 5 Dev (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 91 of 91 records
- **Intervals:** median 124.38s (p5 0.01s / p95 1979.13s, n=90)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Fields under `data`:**

```text
data.questEventType  (string, 91/91 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x37
data.questID  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/91 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 47 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (47)
- **Intervals:** median 3.42s (p5 0.46s / p95 29.30s, n=46)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "On"  x32
    "Off"  x15
data.floor  (string, 47/47 records)
    "4"  x24
    "1"  x9
    "3"  x8
    "2"  x6
data.machineNumber  (string, 47/47 records)
    "One"  x46
    "Two"  x1
data.machineType  (string, 47/47 records)
    "Condenser"  x25
    "Evaporator"  x15
    "VentSwitch"  x4
    "DualChamber_Evaporator"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 47/47 records)
    "3"  x28
    "2"  x12
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Topographic Map Event` — 29 records

- **Scenes:** Unit 3 Dev (16); Unit 2 Prod (Refactor) (13)
- **Intervals:** median 30.62s (p5 6.14s / p95 111248.78s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "MapOpenEvent"  x15
    "MapCloseEvent"  x14
data.featureUsed  (string, 29/29 records)
    "Map"  x29
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 2.72s (p5 0.86s / p95 73.42s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Bedrock"  x13
    "Clay"  x9
    "Gravel"  x3
    "Sand"  x1
data.floor  (string, 26/26 records)
    "5"  x24
    "3"  x1
    "4"  x1
data.machine  (string, 26/26 records)
    "1"  x24
    "2"  x2
data.row  (string, 26/26 records)
    "BottomRow"  x17
    "TopRow"  x9
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 23 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (16); Unit 2 Prod (Refactor) (7)
- **Intervals:** median 19.61s (p5 1.44s / p95 162616.68s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "dragStart"  x12
    "dragEnd"  x11
data.featureUsed  (string, 23/23 records)
    "waypoint"  x23
data.location  (object, 23/23 records)
data.location.x  (number, 23/23 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 23/23 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 23/23 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 19 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 2 Prod (Refactor) (7); Unit 3 Dev (3)
- **Intervals:** median 9.18s (p5 1.55s / p95 54405.82s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "argumentationNodeAdd"  x15
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 19/19 records)
    "Unit 1 - Freshwater"  x7
    "Unit 2 – Watershed"  x7
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 19/19 records)
    "A"  x7
    "1"  x3
    "II"  x3
    "D"  x2
    "I"  x2
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 12 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 43.98s (p5 2.96s / p95 257889.05s, n=11)
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

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 59.84s (p5 15.88s / p95 343884.34s, n=11)
- **Open findings:** 1 — see sections 5-8
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 257716.98s (p5 30391.70s / p95 343453.50s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 3 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (3)
- **Intervals:** median 15.65s (p5 14.74s / p95 16.56s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "cameraPlaced"  x3
data.boxId  (string, 3/3 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 3/3 records)
    "None"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 0.00s (p5 0.00s / p95 0.00s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 4 - Flooding"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Soil Flow Rates"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "dragStart" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (13x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*