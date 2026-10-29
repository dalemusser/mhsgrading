# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72c
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f72c.jsonl
- **Records:** 1974 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f72c
- **Time span:** 2026-04-13T17:47:33.465000+00:00 .. 2026-04-23T18:42:07.158000+00:00 (240h 54m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 1974 records, 6 scenes.
- Findings: **0 FAIL**, **46 WARNING**, 68 INFO, 2 NOT_TESTED, 48 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowUnfocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1247 | 63.17 | 1 | 6 | 912 | 2026-04-13T17:47:51.742000+00:00 | 2026-04-23T18:42:07.158000+00:00 | 240h 54m |
| PlayerPositionEvent | 474 | 24.01 | 1 | 6 | 0 | 2026-04-13T17:47:33.465000+00:00 | 2026-04-23T18:41:47.890000+00:00 | 240h 54m |
| questEvent | 77 | 3.9 | 1 | 6 | 77 | 2026-04-13T17:47:51.724000+00:00 | 2026-04-23T18:42:03.538000+00:00 | 240h 54m |
| Topographic Map Event | 52 | 2.63 | 1 | 3 | 0 | 2026-04-13T18:11:35.651000+00:00 | 2026-04-21T18:37:03.154000+00:00 | 192h 25m |
| soilMachine | 29 | 1.47 | 1 | 1 | 0 | 2026-04-23T18:15:50.019000+00:00 | 2026-04-23T18:20:28.283000+00:00 | 4m 38s |
| TopographicMapEvent | 24 | 1.22 | 1 | 2 | 0 | 2026-04-13T18:37:49.772000+00:00 | 2026-04-21T18:36:44.200000+00:00 | 191h 58m |
| argumentationToolEvent | 20 | 1.01 | 1 | 2 | 0 | 2026-04-15T18:26:50.172000+00:00 | 2026-04-23T18:32:29.906000+00:00 | 192h 5m |
| crash | 15 | 0.76 | 1 | 1 | 0 |  |  | ? |
| argumentationNodeEvent | 11 | 0.56 | 1 | 2 | 0 | 2026-04-13T18:09:30.607000+00:00 | 2026-04-15T18:27:31.899000+00:00 | 48h 18m |
| Soil Key Puzzle | 8 | 0.41 | 1 | 2 | 0 | 2026-04-13T18:23:32.603000+00:00 | 2026-04-23T18:05:51.350000+00:00 | 239h 42m |
| argumentationEvent | 7 | 0.35 | 1 | 3 | 0 | 2026-04-13T18:09:16.369000+00:00 | 2026-04-23T18:30:54.156000+00:00 | 240h 21m |
| TerasGardenBox | 6 | 0.3 | 1 | 1 | 0 | 2026-04-23T18:36:28.693000+00:00 | 2026-04-23T18:36:55.245000+00:00 | 26.6s |
| EndOfUnit | 4 | 0.2 | 1 | 3 | 0 | 2026-04-13T18:14:07.183000+00:00 | 2026-04-23T18:42:07.132000+00:00 | 240h 27m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173799.495s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.033s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 42.544s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.027s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 10.665s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.215s median 
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
  - Observed: 0.615s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 3 Dungeon Dev; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
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
  - Observed: U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; C; D; II 
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
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 15 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 24; 25; 43; 44; 45; 51; 52; 53; 55; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.8x vs baseline. 
  - Observed: 29 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 286 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[716] _id=69dd31af7957a33870f26126 ts=2026-04-13T18:10:54.0890000Z`; `69cdc907d385e3b94310f72c.jsonl[42] _id=69dd37f27957a33870f28bc4 ts=2026-04-13T18:37:37.9450000Z`; `69cdc907d385e3b94310f72c.jsonl[1123] _id=69dfd5607957a33870f43763 ts=2026-04-15T17:55:02.2120000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'questActiveEvent:24' vs expected 'questActiveEvent:54' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[119] _id=69dfda317957a33870f4585b ts=2026-04-15T18:00:30.842Z`; `69cdc907d385e3b94310f72c.jsonl[107] _id=69dfda377957a33870f458c9 ts=2026-04-15T18:05:20.194Z`; `69cdc907d385e3b94310f72c.jsonl[1181] _id=69dfda457957a33870f4598f ts=2026-04-15T18:07:52.135Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 52 records, TopographicMapEvent: 24 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1246 | 0.0 | 2.596 | 696.032 | 28.989 | 688767.537 | 0.09 | 255 | 2 |
| PlayerPositionEvent | 466 | 0.0 | 30.033 | 1494.711 | 65.641 | 188444.888 | 0.04 | 1 | 5 |
| questEvent | 76 | 0.003 | 150.447 | 11411.208 | 144956.781 | 188717.223 | 0.01 | 8 | 9 |
| Topographic Map Event | 51 | 0.238 | 12.928 | 13582.892 | 85761.491 | 328325.399 | 0.0 | 0 | 6 |
| soilMachine | 28 | 0.167 | 0.615 | 9.938 | 61.801 | 116.483 | 6.04 | 0 | 0 |
| TopographicMapEvent | 23 | 0.251 | 4.027 | 30049.323 | 184130.933 | 191691.135 | 0.0 | 0 | 5 |
| argumentationToolEvent | 19 | 0.001 | 1.215 | 36396.828 | 69224.748 | 691410.046 | 0.0 | 1 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationNodeEvent | 10 | 0.944 | 10.665 | 17388.129 | 95585.334 | 173733.448 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 7 | 2.788 | 42.544 | 123276.964 | 535256.719 | 691439.355 | 0.0 | 0 | 2 |
| argumentationEvent | 6 | 22.287 | 63.541 | 144216.298 | 561977.935 | 691400.442 | 0.0 | 0 | 2 |
| TerasGardenBox | 5 | 1.202 | 2.864 | 5.31 | 10.555 | 10.616 | 11.3 | 0 | 0 |
| EndOfUnit | 3 | 0.0 | 173799.495 | 288559.983 | 640072.358 | 691880.454 | 0.0 | 1 | 2 |

- **WARNING / Medium** `DialogueEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[1123] _id=69dfd5607957a33870f43763 ts=2026-04-15T17:55:02.2120000Z == 69cdc907d385e3b94310f72c.jsonl[1126] _id=69dfd6377957a33870f43bb7 ts=2026-04-15T17:55:02.2120000Z`; `69cdc907d385e3b94310f72c.jsonl[1135] _id=69dfd6cb7957a33870f43fad ts=2026-04-15T17:55:20.1080000Z == 69cdc907d385e3b94310f72c.jsonl[1136] _id=69dfd7d57957a33870f44613 ts=2026-04-15T17:55:20.1080000Z`
- **WARNING / Medium** `PlayerPositionEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[1122] _id=69dfd0fe7957a33870f419c9 ts=2026-04-15T17:55:02.0930000Z == 69cdc907d385e3b94310f72c.jsonl[1124] _id=69dfd5607957a33870f43761 ts=2026-04-15T17:55:02.0930000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 12 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[1339] _id=69e7ac4a1724f0c9e2f91710 ts=? == 69cdc907d385e3b94310f72c.jsonl[1411] _id=69e7b5a71724f0c9e2f93959 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.033s (p5 29.96s, p95 65.64s, n=466) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc907d385e3b94310f72c.jsonl[765] _id=69dd326f7957a33870f266b4 ts=2026-04-13T18:14:07.1830000Z ~ 69cdc907d385e3b94310f72c.jsonl[766] _id=69dd32877957a33870f26740 ts=2026-04-13T18:14:07.183Z`
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `717ms: 69cdc907d385e3b94310f72c.jsonl[801] _id=69dd33587957a33870f26d4c ts=2026-04-13T18:18:00.2000000Z ~ 69cdc907d385e3b94310f72c.jsonl[800] _id=69dd33597957a33870f26d56 ts=2026-04-13T18:18:00.9170000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `944ms: 69cdc907d385e3b94310f72c.jsonl[1225] _id=69dfda667957a33870f45c23 ts=2026-04-15T18:26:42.341Z ~ 69cdc907d385e3b94310f72c.jsonl[383] _id=69dfda667957a33870f45c25 ts=2026-04-15T18:26:43.285Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `119ms: 69cdc907d385e3b94310f72c.jsonl[385] _id=69dfda677957a33870f45c29 ts=2026-04-15T18:26:52.551Z ~ 69cdc907d385e3b94310f72c.jsonl[274] _id=69dfda677957a33870f45c2b ts=2026-04-15T18:26:52.67Z`; `148ms: 69cdc907d385e3b94310f72c.jsonl[377] _id=69dfda677957a33870f45c31 ts=2026-04-15T18:27:01.642Z ~ 69cdc907d385e3b94310f72c.jsonl[378] _id=69dfda687957a33870f45c33 ts=2026-04-15T18:27:01.79Z`; `150ms: 69cdc907d385e3b94310f72c.jsonl[277] _id=69dfda697957a33870f45c4b ts=2026-04-15T18:27:19.564Z ~ 69cdc907d385e3b94310f72c.jsonl[380] _id=69dfda697957a33870f45c4d ts=2026-04-15T18:27:19.714Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `850ms: 69cdc907d385e3b94310f72c.jsonl[1635] _id=69ea61d71724f0c9e2fb21b1 ts=2026-04-23T18:15:51.0840000Z ~ 69cdc907d385e3b94310f72c.jsonl[1634] _id=69ea61d81724f0c9e2fb21b7 ts=2026-04-23T18:15:51.9340000Z`; `302ms: 69cdc907d385e3b94310f72c.jsonl[1634] _id=69ea61d81724f0c9e2fb21b7 ts=2026-04-23T18:15:51.9340000Z ~ 69cdc907d385e3b94310f72c.jsonl[459] _id=69ea61d81724f0c9e2fb21bb ts=2026-04-23T18:15:52.2360000Z`; `308ms: 69cdc907d385e3b94310f72c.jsonl[459] _id=69ea61d81724f0c9e2fb21bb ts=2026-04-23T18:15:52.2360000Z ~ 69cdc907d385e3b94310f72c.jsonl[460] _id=69ea61d81724f0c9e2fb21bd ts=2026-04-23T18:15:52.5440000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 19m 
  - Evidence: 191h 19m: 69cdc907d385e3b94310f72c.jsonl[1280] _id=69dfdbcb7957a33870f466e3 ts=2026-04-15T18:41:14.2420000Z -> 69cdc907d385e3b94310f72c.jsonl[1515] _id=69ea5e4a1724f0c9e2fb04e9 ts=2026-04-23T18:00:41.7790000Z; 47h 3m: 69cdc907d385e3b94310f72c.jsonl[1002] _id=69dd38df7957a33870f2921c ts=2026-04-13T18:41:34.7060000Z -> 69cdc907d385e3b94310f72c.jsonl[1005] _id=69dfce9b7957a33870f40b75 ts=2026-04-15T17:44:58.6750000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 255 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72c.jsonl[1123] _id=69dfd5607957a33870f43763 ts=2026-04-15T17:55:02.2120000Z -> 69cdc907d385e3b94310f72c.jsonl[1126] _id=69dfd6377957a33870f43bb7 ts=2026-04-15T17:55:02.2120000Z; 0ms: 69cdc907d385e3b94310f72c.jsonl[1135] _id=69dfd6cb7957a33870f43fad ts=2026-04-15T17:55:20.1080000Z -> 69cdc907d385e3b94310f72c.jsonl[1136] _id=69dfd7d57957a33870f44613 ts=2026-04-15T17:55:20.1080000Z; 0ms: 69cdc907d385e3b94310f72c.jsonl[1138] _id=69dfd7ee7957a33870f446ff ts=2026-04-15T17:55:25.0220000Z -> 69cdc907d385e3b94310f72c.jsonl[1150] _id=69dfda227957a33870f45773 ts=2026-04-15T17:55:25.022Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 192h 11m 
  - Evidence: 192h 11m: 69cdc907d385e3b94310f72c.jsonl[409] _id=69dfda727957a33870f45ce9 ts=2026-04-15T18:30:46.678Z -> 69cdc907d385e3b94310f72c.jsonl[518] _id=69ea67ff1724f0c9e2fb4e93 ts=2026-04-23T18:42:07.1320000Z; 48h 16m: 69cdc907d385e3b94310f72c.jsonl[766] _id=69dd32877957a33870f26740 ts=2026-04-13T18:14:07.183Z -> 69cdc907d385e3b94310f72c.jsonl[409] _id=69dfda727957a33870f45ce9 ts=2026-04-15T18:30:46.678Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72c.jsonl[765] _id=69dd326f7957a33870f266b4 ts=2026-04-13T18:14:07.1830000Z -> 69cdc907d385e3b94310f72c.jsonl[766] _id=69dd32877957a33870f26740 ts=2026-04-13T18:14:07.183Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 52h 20m 
  - Evidence: 52h 20m: 69cdc907d385e3b94310f72c.jsonl[1269] _id=69dfdbbf7957a33870f466bd ts=2026-04-15T18:41:03.2800000Z -> 69cdc907d385e3b94310f72c.jsonl[1284] _id=69e2bbdd1724f0c9e2f7ebd0 ts=2026-04-17T23:01:48.1680000Z; 51h 34m: 69cdc907d385e3b94310f72c.jsonl[451] _id=69e2c1391724f0c9e2f7f878 ts=2026-04-17T23:24:41.4910000Z -> 69cdc907d385e3b94310f72c.jsonl[1328] _id=69e596771724f0c9e2f84a3d ts=2026-04-20T02:59:03.1490000Z; 47h 3m: 69cdc907d385e3b94310f72c.jsonl[1003] _id=69dd38e37957a33870f29220 ts=2026-04-13T18:41:38.2720000Z -> 69cdc907d385e3b94310f72c.jsonl[1007] _id=69dfce967957a33870f40b69 ts=2026-04-15T17:44:53.7030000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72c.jsonl[1122] _id=69dfd0fe7957a33870f419c9 ts=2026-04-15T17:55:02.0930000Z -> 69cdc907d385e3b94310f72c.jsonl[1124] _id=69dfd5607957a33870f43761 ts=2026-04-15T17:55:02.0930000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 192h 3m 
  - Evidence: 192h 3m: 69cdc907d385e3b94310f72c.jsonl[134] _id=69dfda327957a33870f45877 ts=2026-04-15T18:01:29.704Z -> 69cdc907d385e3b94310f72c.jsonl[1540] _id=69ea5f691724f0c9e2fb0bef ts=2026-04-23T18:05:29.0590000Z; 47h 27m: 69cdc907d385e3b94310f72c.jsonl[834] _id=69dd34a87957a33870f275c0 ts=2026-04-13T18:23:35.3910000Z -> 69cdc907d385e3b94310f72c.jsonl[1051] _id=69dfcff67957a33870f41205 ts=2026-04-15T17:50:45.9590000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 91h 12m 
  - Evidence: 91h 12m: 69cdc907d385e3b94310f72c.jsonl[1325] _id=69e2c1491724f0c9e2f7f884 ts=2026-04-17T23:24:56.8950000Z -> 69cdc907d385e3b94310f72c.jsonl[1506] _id=69e7c3ce1724f0c9e2f9a247 ts=2026-04-21T18:37:02.2940000Z; 52h 42m: 69cdc907d385e3b94310f72c.jsonl[1279] _id=69dfdba47957a33870f465f5 ts=2026-04-15T18:40:36.2350000Z -> 69cdc907d385e3b94310f72c.jsonl[1318] _id=69e2c0cd1724f0c9e2f7f844 ts=2026-04-17T23:22:53.3530000Z; 47h 14m: 69cdc907d385e3b94310f72c.jsonl[992] _id=69dd387d7957a33870f29030 ts=2026-04-13T18:39:56.6480000Z -> 69cdc907d385e3b94310f72c.jsonl[1114] _id=69dfd0c37957a33870f417f1 ts=2026-04-15T17:54:10.4390000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 53h 14m 
  - Evidence: 53h 14m: 69cdc907d385e3b94310f72c.jsonl[186] _id=69dfda437957a33870f45977 ts=2026-04-15T18:07:14.255Z -> 69cdc907d385e3b94310f72c.jsonl[1315] _id=69e2c09d1724f0c9e2f7f82e ts=2026-04-17T23:22:05.3900000Z; 51h 34m: 69cdc907d385e3b94310f72c.jsonl[1324] _id=69e2c1481724f0c9e2f7f882 ts=2026-04-17T23:24:55.8420000Z -> 69cdc907d385e3b94310f72c.jsonl[1331] _id=69e596a51724f0c9e2f84a43 ts=2026-04-20T02:59:49.8380000Z; 47h 14m: 69cdc907d385e3b94310f72c.jsonl[994] _id=69dd387d7957a33870f2902e ts=2026-04-13T18:39:56.5480000Z -> 69cdc907d385e3b94310f72c.jsonl[1116] _id=69dfd0cc7957a33870f4183b ts=2026-04-15T17:54:19.9190000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 192h 3m 
  - Evidence: 192h 3m: 69cdc907d385e3b94310f72c.jsonl[393] _id=69dfda697957a33870f45c55 ts=2026-04-15T18:27:33.714Z -> 69cdc907d385e3b94310f72c.jsonl[1808] _id=69ea655e1724f0c9e2fb3c81 ts=2026-04-23T18:30:54.1560000Z; 48h 15m: 69cdc907d385e3b94310f72c.jsonl[699] _id=69dd31ae7957a33870f2611e ts=2026-04-13T18:10:54.0570000Z -> 69cdc907d385e3b94310f72c.jsonl[358] _id=69dfda657957a33870f45c0d ts=2026-04-15T18:26:04.472Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 15m 
  - Evidence: 48h 15m: 69cdc907d385e3b94310f72c.jsonl[712] _id=69dd31ac7957a33870f26104 ts=2026-04-13T18:10:51.2350000Z -> 69cdc907d385e3b94310f72c.jsonl[375] _id=69dfda667957a33870f45c19 ts=2026-04-15T18:26:24.683Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 192h 3m 
  - Evidence: 192h 3m: 69cdc907d385e3b94310f72c.jsonl[381] _id=69dfda697957a33870f45c4f ts=2026-04-15T18:27:21.151Z -> 69cdc907d385e3b94310f72c.jsonl[1807] _id=69ea655b1724f0c9e2fb3c65 ts=2026-04-23T18:30:51.1970000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 69cdc907d385e3b94310f72c.jsonl[1807] _id=69ea655b1724f0c9e2fb3c65 ts=2026-04-23T18:30:51.1970000Z -> 69cdc907d385e3b94310f72c.jsonl[485] _id=69ea655b1724f0c9e2fb3c67 ts=2026-04-23T18:30:51.1980000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 52h 25m 
  - Evidence: 52h 25m: 69cdc907d385e3b94310f72c.jsonl[1243] _id=69dfdab27957a33870f45f03 ts=2026-04-15T18:36:34.0480000Z -> 69cdc907d385e3b94310f72c.jsonl[1285] _id=69e2bbdf1724f0c9e2f7ebe0 ts=2026-04-17T23:01:51.2710000Z; 51h 40m: 69cdc907d385e3b94310f72c.jsonl[1309] _id=69e2bfc01724f0c9e2f7f7c2 ts=2026-04-17T23:18:24.2560000Z -> 69cdc907d385e3b94310f72c.jsonl[1326] _id=69e5967a1724f0c9e2f84a3f ts=2026-04-20T02:59:06.3760000Z; 47h 29m: 69cdc907d385e3b94310f72c.jsonl[1497] _id=69e7c3301724f0c9e2f99d05 ts=2026-04-21T18:34:24.4030000Z -> 69cdc907d385e3b94310f72c.jsonl[1524] _id=69ea5efb1724f0c9e2fb089f ts=2026-04-23T18:03:38.7720000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.003s..0.009s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f72c.jsonl[684] _id=69dd31197957a33870f25d26 ts=2026-04-13T18:08:24.4050000Z -> 69cdc907d385e3b94310f72c.jsonl[685] _id=69dd31197957a33870f25d28 ts=2026-04-13T18:08:24.4080000Z; 8ms: 69cdc907d385e3b94310f72c.jsonl[1619] _id=69ea617e1724f0c9e2fb1dcf ts=2026-04-23T18:14:21.8460000Z -> 69cdc907d385e3b94310f72c.jsonl[1617] _id=69ea617e1724f0c9e2fb1dd5 ts=2026-04-23T18:14:21.8540000Z; 9ms: 69cdc907d385e3b94310f72c.jsonl[562] _id=69dd2d597957a33870f249ea ts=2026-04-13T17:52:24.9720000Z -> 69cdc907d385e3b94310f72c.jsonl[556] _id=69dd2d5a7957a33870f249ec ts=2026-04-13T17:52:24.9810000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc907d385e3b94310f72c.jsonl:69cdc907d385e3b94310f72c, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[834] _id=69dd34a87957a33870f275c0 ts=2026-04-13T18:23:35.3910000Z`; `69cdc907d385e3b94310f72c.jsonl[1052] _id=69dfcff97957a33870f4121d ts=2026-04-15T17:50:48.9160000Z`; `69cdc907d385e3b94310f72c.jsonl[73] _id=69dfda317957a33870f45869 ts=2026-04-15T18:00:47.16Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 24 record(s) match the trigger in 69cdc907d385e3b94310f72c.jsonl:69cdc907d385e3b94310f72c, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[965] _id=69dd37fe7957a33870f28c36 ts=2026-04-13T18:37:49.7720000Z`; `69cdc907d385e3b94310f72c.jsonl[971] _id=69dd37ff7957a33870f28c40 ts=2026-04-13T18:37:50.3600000Z`; `69cdc907d385e3b94310f72c.jsonl[993] _id=69dd387d7957a33870f2902a ts=2026-04-13T18:39:56.2970000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[76] _id=69dfda247957a33870f45795 ts=2026-04-15T17:56:08.327Z`; `69cdc907d385e3b94310f72c.jsonl[1724] _id=69ea63811724f0c9e2fb2f29 ts=2026-04-23T18:22:57.2530000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Finished' preceded by 'Started' per Unit 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[73] _id=69dfda317957a33870f45869 ts=2026-04-15T18:00:47.16Z`; `69cdc907d385e3b94310f72c.jsonl[134] _id=69dfda327957a33870f45877 ts=2026-04-15T18:01:29.704Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[358] _id=69dfda657957a33870f45c0d ts=2026-04-15T18:26:04.472Z`; `69cdc907d385e3b94310f72c.jsonl[393] _id=69dfda697957a33870f45c55 ts=2026-04-15T18:27:33.714Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[384] _id=69dfda667957a33870f45c27 ts=2026-04-15T18:26:50.172Z`; `69cdc907d385e3b94310f72c.jsonl[385] _id=69dfda677957a33870f45c29 ts=2026-04-15T18:26:52.551Z`; `69cdc907d385e3b94310f72c.jsonl[274] _id=69dfda677957a33870f45c2b ts=2026-04-15T18:26:52.67Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[1181] _id=69dfda457957a33870f4598f ts=2026-04-15T18:07:52.135Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 15 records 
  - Examples: `69cdc907d385e3b94310f72c.jsonl[1339] _id=69e7ac4a1724f0c9e2f91710 ts=?`; `69cdc907d385e3b94310f72c.jsonl[1411] _id=69e7b5a71724f0c9e2f93959 ts=?`; `69cdc907d385e3b94310f72c.jsonl[1414] _id=69e7b5d51724f0c9e2f93bc7 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 99 unmatched 'DialogueStartEvent' (totals: 216 start, 119 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 3 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 34 unmatched 'questActiveEvent' (totals: 55 start, 22 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.78s, min -2325.64s, max +0.03s over 1959 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72c\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | partial |
| Unit4 | complete |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=partial, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=complete, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 52 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 15 records 
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

### `DialogueEvent` — 1247 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (643); Unit 4 Dev (206); Unit 1 Dev (196); Unit 4 Dev - Dungeon (95); Unit 4 Dev - Anderson Base (72); Unit 3 Dev (35)
- **eventKey:** present on 912 of 1247 records
- **Intervals:** median 2.60s (p5 0.01s / p95 28.99s, n=1246)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x912; [conversationId, dialogueEventType] x335
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1247/1247 records)
    numeric range 10 .. 114 (30 unique)
data.dialogueEventType  (string, 1247/1247 records)
    "DialogueNodeEvent"  x912
    "DialogueStartEvent"  x216
    "DialogueFinishEvent"  x119
data.nodeId  (number, 912/1247 records)
    numeric range 0 .. 284 (135 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 474 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (195); Unit 2 Prod (Refactor) (142); Unit 1 Dev (52); Unit 4 Dev (44); Unit 4 Dev - Dungeon (28); Unit 4 Dev - Anderson Base (13)
- **Intervals:** median 30.03s (p5 29.96s / p95 65.64s, n=466)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 474/474 records)
data.position.x  (number, 474/474 records)
    numeric range -105.92 .. 1558.11 (248 unique)
data.position.y  (number, 474/474 records)
    numeric range -114.631 .. 156.968 (233 unique)
data.position.z  (number, 474/474 records)
    numeric range -721.291 .. 1731.99 (249 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 77 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (29); Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 77 of 77 records
- **Intervals:** median 150.45s (p5 0.01s / p95 144956.78s, n=76)
- **`data` key-set variants:** [questEventType, questID, questName] x55; [questEventType, questID, questName, questSuccessOrFailure] x22
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 77/77 records)
    "questActiveEvent"  x55
    "questFinishEvent"  x22
data.questID  (string, 77/77 records)
    21 unique values (see csv/event_unique_values.csv)
data.questName  (string, 77/77 records)
    21 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 22/77 records)
    "Succeeded"  x22
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 52 records

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (16); Unit 1 Dev (2)
- **Intervals:** median 12.93s (p5 1.31s / p95 85761.49s, n=51)
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "MapCloseEvent"  x30
    "MapOpenEvent"  x22
data.featureUsed  (string, 52/52 records)
    "Map"  x52
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `soilMachine` — 29 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (29)
- **Intervals:** median 0.62s (p5 0.23s / p95 61.80s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "ChangeCanister"  x29
data.canisterType  (string, 29/29 records)
    "Sand"  x18
    "Clay"  x5
    "Bedrock"  x4
    "Gravel"  x2
data.floor  (string, 29/29 records)
    "3"  x18
    "5"  x10
    "4"  x1
data.machine  (string, 29/29 records)
    "1"  x28
    "2"  x1
data.row  (string, 29/29 records)
    "TopRow"  x23
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 24 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (12)
- **Intervals:** median 4.03s (p5 0.30s / p95 184130.93s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "dragEnd"  x12
    "dragStart"  x12
data.featureUsed  (string, 24/24 records)
    "waypoint"  x24
data.location  (object, 24/24 records)
data.location.x  (number, 24/24 records)
    numeric range -772.196 .. 184.075 (13 unique)
data.location.y  (number, 24/24 records)
    numeric range -314.43 .. 145.203 (13 unique)
data.location.z  (number, 24/24 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 4 Dev - Anderson Base (10)
- **Intervals:** median 1.22s (p5 0.06s / p95 69224.75s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolClose"  x16
    "argumentationToolOpen"  x4
data.argumentationTitle  (string, 20/20 records)
    "Unit 2 – Watershed"  x10
    "Unit 4 - Flooding"  x10
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - Waterfall Data"  x10
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 15 records

- **Scenes:** <missing sceneName> (15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 15/15 records)
    true  x15
data.message  (string, 15/15 records)
    "Uncaught ReferenceError: onResize is not defined"  x13
    "A user gesture is required to request Pointer Lock."  x1
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 15/15 records)
    "running"  x15
data.stack  (string, 15/15 records, 2 empty-string)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x13
    ""  x2
data.type  (string, 15/15 records)
    "runtime_error"  x13
    "unhandled_rejection"  x2
data.unitId  (string, 15/15 records)
    "unit3"  x14
    "unit4"  x1
data.workspace  (string, 15/15 records)
    "mhs"  x15
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationNodeEvent` — 11 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 1 Dev (4)
- **Intervals:** median 10.67s (p5 2.26s / p95 95585.33s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationNodeAdd"  x11
data.argumentationTitle  (string, 11/11 records)
    "Unit 2 – Watershed"  x7
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
data.nodeName  (string, 11/11 records)
    "A"  x7
    "1"  x2
    "B"  x1
    "I"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev (2)
- **Intervals:** median 42.54s (p5 2.84s / p95 535256.72s, n=7)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x5
    "Started"  x3
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 63.54s (p5 26.11s / p95 561977.94s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 7/7 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.86s (p5 1.27s / p95 10.55s, n=5)
- **`data` key-set variants:** [actionType, boxID, soilType] x3; [actionType, boxId, soilType] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "cameraPlaced"  x3
    "soilSelected"  x3
data.boxID  (string, 3/6 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.boxId  (string, 3/6 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1)
- **Intervals:** median 173799.49s (p5 17379.95s / p95 640072.36s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x2
    "2"  x1
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
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `DialogueEvent` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (12x)
- `soilMachine` data.canisterType: "Bedrock" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*