# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f734

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f734
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f734.jsonl
- **Records:** 2083 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f734
- **Time span:** 2026-04-13T17:53:07.999000+00:00 .. 2026-04-23T18:40:36.650000+00:00 (240h 47m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f734\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2083 records, 6 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 52 INFO, 2 NOT_TESTED, 34 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1385 | 66.49 | 1 | 6 | 965 | 2026-04-13T17:53:26.259000+00:00 | 2026-04-23T18:40:36.327000+00:00 | 240h 47m |
| PlayerPositionEvent | 447 | 21.46 | 1 | 6 | 0 | 2026-04-13T17:53:07.999000+00:00 | 2026-04-23T18:40:36.650000+00:00 | 240h 47m |
| Topographic Map Event | 78 | 3.74 | 1 | 3 | 0 | 2026-04-15T18:01:52.205000+00:00 | 2026-04-23T18:24:26.647000+00:00 | 192h 22m |
| questEvent | 45 | 2.16 | 1 | 6 | 45 | 2026-04-13T17:53:26.244000+00:00 | 2026-04-23T18:38:17.094000+00:00 | 240h 44m |
| TopographicMapEvent | 43 | 2.06 | 1 | 3 | 0 | 2026-04-15T18:02:20.943000+00:00 | 2026-04-23T18:24:26.043000+00:00 | 192h 22m |
| argumentationNodeEvent | 40 | 1.92 | 1 | 2 | 0 | 2026-04-13T18:30:28.782000+00:00 | 2026-04-21T18:30:02.245000+00:00 | 191h 59m |
| argumentationToolEvent | 20 | 0.96 | 1 | 1 | 0 | 2026-04-21T18:22:31.667000+00:00 | 2026-04-21T18:29:19.970000+00:00 | 6m 48s |
| Soil Key Puzzle | 12 | 0.58 | 1 | 3 | 0 | 2026-04-15T17:53:34.763000+00:00 | 2026-04-23T18:35:51.359000+00:00 | 192h 42m |
| argumentationEvent | 7 | 0.34 | 1 | 2 | 0 | 2026-04-13T18:30:22.491000+00:00 | 2026-04-21T18:30:04.128000+00:00 | 191h 59m |
| crash | 4 | 0.19 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.1 | 1 | 2 | 0 | 2026-04-13T18:36:18.128000+00:00 | 2026-04-23T18:29:53.811000+00:00 | 239h 53m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 863615.683s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.017s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 62.113s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.861s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 7.462s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.599s median 
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
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 12 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 78 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 40 records 
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
  - Observed: 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 47; 48; 49; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f734.jsonl[9] _id=69dd36977957a33870f28350 ts=2026-04-13T18:31:50.3390000Z`; `69cdc907d385e3b94310f734.jsonl[587] _id=69dfd3657957a33870f42bbb ts=2026-04-15T18:05:24.3710000Z`; `69cdc907d385e3b94310f734.jsonl[1136] _id=69e7b6121724f0c9e2f93df7 ts=2026-04-21T17:38:25.4160000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 78 records, TopographicMapEvent: 43 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1384 | 0.0 | 3.062 | 626.322 | 37.964 | 512077.921 | 0.1 | 353 | 5 |
| PlayerPositionEvent | 440 | 29.858 | 30.017 | 1969.664 | 41.223 | 512064.772 | 0.03 | 0 | 4 |
| Topographic Map Event | 77 | 0.794 | 20.799 | 8994.214 | 704.527 | 514758.36 | 0.01 | 0 | 5 |
| questEvent | 44 | 0.008 | 205.866 | 19697.519 | 144455.43 | 512821.387 | 0.0 | 3 | 8 |
| TopographicMapEvent | 42 | 0.533 | 4.861 | 16488.693 | 1180.225 | 516179.988 | 0.0 | 0 | 4 |
| argumentationNodeEvent | 39 | 1.244 | 7.462 | 17722.396 | 68.31 | 690529.003 | 0.0 | 0 | 1 |
| argumentationToolEvent | 19 | 0.024 | 1.599 | 21.49 | 62.566 | 252.385 | 2.79 | 1 | 0 |
| Soil Key Puzzle | 11 | 3.114 | 62.113 | 63066.963 | 343346.389 | 513794.911 | 0.0 | 0 | 5 |
| argumentationEvent | 6 | 0.091 | 33.551 | 115196.939 | 518034.14 | 690521.405 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 863615.683 | 863615.683 | 863615.683 | 863615.683 | 863615.683 | 0.0 | 0 | 1 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f734.jsonl[1676] _id=69e7c3ab1724f0c9e2f9a0b5 ts=? == 69cdc907d385e3b94310f734.jsonl[1786] _id=69ea60e21724f0c9e2fb18f5 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.017s (p5 29.95s, p95 41.22s, n=440) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `91ms: 69cdc907d385e3b94310f734.jsonl[103] _id=69e7c22c1724f0c9e2f9963b ts=2026-04-21T18:30:04.0370000Z ~ 69cdc907d385e3b94310f734.jsonl[106] _id=69e7c22d1724f0c9e2f99641 ts=2026-04-21T18:30:04.1280000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `964ms: 69cdc907d385e3b94310f734.jsonl[1539] _id=69e7c0981724f0c9e2f9893d ts=2026-04-21T18:23:20.1130000Z ~ 69cdc907d385e3b94310f734.jsonl[1542] _id=69e7c0991724f0c9e2f98943 ts=2026-04-21T18:23:21.0770000Z`; `898ms: 69cdc907d385e3b94310f734.jsonl[1592] _id=69e7c1e21724f0c9e2f99413 ts=2026-04-21T18:28:49.2420000Z ~ 69cdc907d385e3b94310f734.jsonl[1593] _id=69e7c1e21724f0c9e2f9941b ts=2026-04-21T18:28:50.1400000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 142h 14m 
  - Evidence: 142h 14m: 69cdc907d385e3b94310f734.jsonl[917] _id=69dfdbe17957a33870f466f9 ts=2026-04-15T18:41:36.9850000Z -> 69cdc907d385e3b94310f734.jsonl[922] _id=69e7ac2f1724f0c9e2f91681 ts=2026-04-21T16:56:14.9060000Z; 47h 20m: 69cdc907d385e3b94310f734.jsonl[1708] _id=69e7c4ab1724f0c9e2f9a791 ts=2026-04-21T18:40:42.2980000Z -> 69cdc907d385e3b94310f734.jsonl[1709] _id=69ea5e601724f0c9e2fb0561 ts=2026-04-23T18:01:02.5410000Z; 47h 5m: 69cdc907d385e3b94310f734.jsonl[413] _id=69dd389d7957a33870f29116 ts=2026-04-13T18:40:28.6480000Z -> 69cdc907d385e3b94310f734.jsonl[17] _id=69dfcee17957a33870f40bd5 ts=2026-04-15T17:46:07.9600000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 353 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f734.jsonl[1960] _id=69ea65221724f0c9e2fb3b09 ts=2026-04-23T18:29:53.8320000Z -> 69cdc907d385e3b94310f734.jsonl[132] _id=69ea65321724f0c9e2fb3b4f ts=2026-04-23T18:29:53.832Z; 2ms: 69cdc907d385e3b94310f734.jsonl[75] _id=69e7b8f21724f0c9e2f9518f ts=2026-04-21T17:50:41.5180000Z -> 69cdc907d385e3b94310f734.jsonl[76] _id=69e7b8f21724f0c9e2f95191 ts=2026-04-21T17:50:41.5200000Z; 3ms: 69cdc907d385e3b94310f734.jsonl[1271] _id=69e7b91c1724f0c9e2f95251 ts=2026-04-21T17:51:23.1820000Z -> 69cdc907d385e3b94310f734.jsonl[1270] _id=69e7b91c1724f0c9e2f95253 ts=2026-04-21T17:51:23.1850000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 239h 53m 
  - Evidence: 239h 53m: 69cdc907d385e3b94310f734.jsonl[376] _id=69dd37a37957a33870f289e2 ts=2026-04-13T18:36:18.1280000Z -> 69cdc907d385e3b94310f734.jsonl[2004] _id=69ea65221724f0c9e2fb3b07 ts=2026-04-23T18:29:53.8110000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 142h 14m 
  - Evidence: 142h 14m: 69cdc907d385e3b94310f734.jsonl[896] _id=69dfdbc97957a33870f466d9 ts=2026-04-15T18:41:12.7760000Z -> 69cdc907d385e3b94310f734.jsonl[918] _id=69e7ac0a1724f0c9e2f91623 ts=2026-04-21T16:55:37.5480000Z; 47h 20m: 69cdc907d385e3b94310f734.jsonl[1706] _id=69e7c49a1724f0c9e2f9a77f ts=2026-04-21T18:40:25.3780000Z -> 69cdc907d385e3b94310f734.jsonl[1710] _id=69ea5e5e1724f0c9e2fb0557 ts=2026-04-23T18:01:00.8060000Z; 47h 4m: 69cdc907d385e3b94310f734.jsonl[414] _id=69dd38d77957a33870f2920c ts=2026-04-13T18:41:26.9170000Z -> 69cdc907d385e3b94310f734.jsonl[416] _id=69dfcedd7957a33870f40bcd ts=2026-04-15T17:46:03.9200000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 142h 43m 
  - Evidence: 142h 43m: 69cdc907d385e3b94310f734.jsonl[696] _id=69dfd6527957a33870f43c71 ts=2026-04-15T18:17:53.0680000Z -> 69cdc907d385e3b94310f734.jsonl[978] _id=69e7ad541724f0c9e2f91d05 ts=2026-04-21T17:01:07.9790000Z; 48h 1m: 69cdc907d385e3b94310f734.jsonl[1660] _id=69e7c3111724f0c9e2f99c23 ts=2026-04-21T18:33:53.1320000Z -> 69cdc907d385e3b94310f734.jsonl[2030] _id=69ea66731724f0c9e2fb454f ts=2026-04-23T18:35:30.9980000Z; 49m 13s: 69cdc907d385e3b94310f734.jsonl[1196] _id=69e7b76d1724f0c9e2f9470d ts=2026-04-21T17:44:13.1480000Z -> 69cdc907d385e3b94310f734.jsonl[1658] _id=69e7c2f71724f0c9e2f99b57 ts=2026-04-21T18:33:26.6570000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 142h 59m 
  - Evidence: 142h 59m: 69cdc907d385e3b94310f734.jsonl[869] _id=69dfdab97957a33870f45f45 ts=2026-04-15T18:36:40.5540000Z -> 69cdc907d385e3b94310f734.jsonl[1103] _id=69e7b57f1724f0c9e2f936b5 ts=2026-04-21T17:35:58.9140000Z; 47h 53m: 69cdc907d385e3b94310f734.jsonl[1476] _id=69e7bf3f1724f0c9e2f97e01 ts=2026-04-21T18:17:35.0680000Z -> 69cdc907d385e3b94310f734.jsonl[1784] _id=69ea60d61724f0c9e2fb18b5 ts=2026-04-23T18:11:34.2940000Z; 19m 41s: 69cdc907d385e3b94310f734.jsonl[38] _id=69dfd60a7957a33870f43aad ts=2026-04-15T18:16:41.8970000Z -> 69cdc907d385e3b94310f734.jsonl[865] _id=69dfdaa87957a33870f45ebd ts=2026-04-15T18:36:23.5020000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 22m 
  - Evidence: 143h 22m: 69cdc907d385e3b94310f734.jsonl[34] _id=69dfd5317957a33870f43657 ts=2026-04-15T18:13:04.7590000Z -> 69cdc907d385e3b94310f734.jsonl[1106] _id=69e7b5851724f0c9e2f93709 ts=2026-04-21T17:36:04.7470000Z; 48h 13m: 69cdc907d385e3b94310f734.jsonl[1323] _id=69e7baa71724f0c9e2f95c9c ts=2026-04-21T17:57:59.2330000Z -> 69cdc907d385e3b94310f734.jsonl[1779] _id=69ea60bc1724f0c9e2fb17c3 ts=2026-04-23T18:11:07.7600000Z; 20m 7s: 69cdc907d385e3b94310f734.jsonl[1106] _id=69e7b5851724f0c9e2f93709 ts=2026-04-21T17:36:04.7470000Z -> 69cdc907d385e3b94310f734.jsonl[1304] _id=69e7ba3c1724f0c9e2f95911 ts=2026-04-21T17:56:12.2050000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 48m 
  - Evidence: 191h 48m: 69cdc907d385e3b94310f734.jsonl[321] _id=69dd36977957a33870f2834c ts=2026-04-13T18:31:50.2870000Z -> 69cdc907d385e3b94310f734.jsonl[1506] _id=69e7bff01724f0c9e2f983a9 ts=2026-04-21T18:20:31.6920000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 48m 
  - Evidence: 191h 48m: 69cdc907d385e3b94310f734.jsonl[325] _id=69dd36947957a33870f28336 ts=2026-04-13T18:31:47.9380000Z -> 69cdc907d385e3b94310f734.jsonl[1505] _id=69e7bff51724f0c9e2f983d6 ts=2026-04-21T18:20:36.9410000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.024s..0.024s shown 
  - Evidence: 24ms: 69cdc907d385e3b94310f734.jsonl[1592] _id=69e7c1e21724f0c9e2f99413 ts=2026-04-21T18:28:49.2420000Z -> 69cdc907d385e3b94310f734.jsonl[1590] _id=69e7c1e21724f0c9e2f99417 ts=2026-04-21T18:28:49.2660000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 142h 27m 
  - Evidence: 142h 27m: 69cdc907d385e3b94310f734.jsonl[800] _id=69dfd90f7957a33870f4500b ts=2026-04-15T18:29:34.0970000Z -> 69cdc907d385e3b94310f734.jsonl[927] _id=69e7ac441724f0c9e2f916ed ts=2026-04-21T16:56:35.4840000Z; 47h 26m: 69cdc907d385e3b94310f734.jsonl[1665] _id=69e7c3331724f0c9e2f99d0d ts=2026-04-21T18:34:27.0910000Z -> 69cdc907d385e3b94310f734.jsonl[1711] _id=69ea5e601724f0c9e2fb055d ts=2026-04-23T18:01:02.3010000Z; 47h 7m: 69cdc907d385e3b94310f734.jsonl[393] _id=69dd38427957a33870f28ea6 ts=2026-04-13T18:38:57.9820000Z -> 69cdc907d385e3b94310f734.jsonl[16] _id=69dfcedf7957a33870f40bd3 ts=2026-04-15T17:46:06.4760000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.008s..0.016s shown 
  - Evidence: 8ms: 69cdc907d385e3b94310f734.jsonl[229] _id=69dd33f17957a33870f27158 ts=2026-04-13T18:20:32.1860000Z -> 69cdc907d385e3b94310f734.jsonl[230] _id=69dd33f17957a33870f2715a ts=2026-04-13T18:20:32.1940000Z; 12ms: 69cdc907d385e3b94310f734.jsonl[291] _id=69dd35f57957a33870f27e92 ts=2026-04-13T18:29:08.4350000Z -> 69cdc907d385e3b94310f734.jsonl[293] _id=69dd35f57957a33870f27e94 ts=2026-04-13T18:29:08.4470000Z; 16ms: 69cdc907d385e3b94310f734.jsonl[193] _id=69dd2f1f7957a33870f25150 ts=2026-04-13T17:59:59.0310000Z -> 69cdc907d385e3b94310f734.jsonl[196] _id=69dd2f207957a33870f25152 ts=2026-04-13T17:59:59.0470000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc907d385e3b94310f734.jsonl:69cdc907d385e3b94310f734, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f734.jsonl[473] _id=69dfd0a27957a33870f41691 ts=2026-04-15T17:53:37.8770000Z`; `69cdc907d385e3b94310f734.jsonl[696] _id=69dfd6527957a33870f43c71 ts=2026-04-15T18:17:53.0680000Z`; `69cdc907d385e3b94310f734.jsonl[977] _id=69e7ad581724f0c9e2f91d0f ts=2026-04-21T17:01:11.1950000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 43 record(s) match the trigger in 69cdc907d385e3b94310f734.jsonl:69cdc907d385e3b94310f734, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f734.jsonl[551] _id=69dfd2ad7957a33870f426c3 ts=2026-04-15T18:02:20.9430000Z`; `69cdc907d385e3b94310f734.jsonl[556] _id=69dfd2b07957a33870f426db ts=2026-04-15T18:02:23.7540000Z`; `69cdc907d385e3b94310f734.jsonl[30] _id=69dfd3687957a33870f42bc9 ts=2026-04-15T18:05:27.6270000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f734.jsonl[818] _id=69dfd97d7957a33870f452fd ts=2026-04-15T18:31:24.9640000Z`; `69cdc907d385e3b94310f734.jsonl[1374] _id=69e7bc321724f0c9e2f96899 ts=2026-04-21T18:04:34.2330000Z`; `69cdc907d385e3b94310f734.jsonl[1405] _id=69e7bcce1724f0c9e2f96d1b ts=2026-04-21T18:07:09.2100000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f734.jsonl[106] _id=69e7c22d1724f0c9e2f99641 ts=2026-04-21T18:30:04.1280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f734.jsonl[1539] _id=69e7c0981724f0c9e2f9893d ts=2026-04-21T18:23:20.1130000Z`; `69cdc907d385e3b94310f734.jsonl[1542] _id=69e7c0991724f0c9e2f98943 ts=2026-04-21T18:23:21.0770000Z`; `69cdc907d385e3b94310f734.jsonl[1589] _id=69e7c1c51724f0c9e2f9934f ts=2026-04-21T18:28:20.5910000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `69cdc907d385e3b94310f734.jsonl[1258] _id=69e7b8e51724f0c9e2f95157 ts=?`; `69cdc907d385e3b94310f734.jsonl[1676] _id=69e7c3ab1724f0c9e2f9a0b5 ts=?`; `69cdc907d385e3b94310f734.jsonl[1786] _id=69ea60e21724f0c9e2fb18f5 ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f734.jsonl[1540] _id=69e7c0991724f0c9e2f9893f ts=2026-04-21T18:23:20.2540000Z`; `69cdc907d385e3b94310f734.jsonl[1584] _id=69e7c1b21724f0c9e2f992c5 ts=2026-04-21T18:28:01.8350000Z`; `69cdc907d385e3b94310f734.jsonl[1601] _id=69e7c1fd1724f0c9e2f994db ts=2026-04-21T18:29:16.3140000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 175 unmatched 'DialogueStartEvent' (totals: 296 start, 124 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationToolOpen' (totals: 10 open, 10 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 26 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.88s, min -17.10s, max -0.54s over 2079 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f734\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 78 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
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

### `DialogueEvent` — 1385 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (656); Unit 3 Dev (324); Unit 1 Dev (180); Unit 3 Dungeon Dev (171); Unit 4 Dev - Dungeon (33); Unit 4 Dev (21)
- **eventKey:** present on 965 of 1385 records
- **Intervals:** median 3.06s (p5 0.01s / p95 37.96s, n=1384)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x965; [conversationId, dialogueEventType] x420
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1385/1385 records)
    numeric range 8 .. 104 (35 unique)
data.dialogueEventType  (string, 1385/1385 records)
    "DialogueNodeEvent"  x965
    "DialogueStartEvent"  x296
    "DialogueFinishEvent"  x124
data.nodeId  (number, 965/1385 records)
    numeric range 0 .. 290 (214 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 447 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (227); Unit 3 Dev (93); Unit 1 Dev (55); Unit 3 Dungeon Dev (50); Unit 4 Dev (15); Unit 4 Dev - Dungeon (7)
- **Intervals:** median 30.02s (p5 29.95s / p95 41.22s, n=440)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 447/447 records)
data.position.x  (number, 447/447 records)
    numeric range -709.63 .. 1421.76 (206 unique)
data.position.y  (number, 447/447 records)
    numeric range -112.49 .. 165.8 (166 unique)
data.position.z  (number, 447/447 records)
    numeric range -1108.12 .. 1926 (207 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 78 records

- **Scenes:** Unit 3 Dev (40); Unit 2 Prod (Refactor) (36); Unit 3 Dungeon Dev (2)
- **Intervals:** median 20.80s (p5 1.64s / p95 704.53s, n=77)
- **Fields under `data`:**

```text
data.actionType  (string, 78/78 records)
    "MapCloseEvent"  x39
    "MapOpenEvent"  x39
data.featureUsed  (string, 78/78 records)
    "Map"  x78
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 45 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (12); Unit 3 Dev (9); Unit 3 Dungeon Dev (4); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **eventKey:** present on 45 of 45 records
- **Intervals:** median 205.87s (p5 0.83s / p95 144455.43s, n=44)
- **`data` key-set variants:** [questEventType, questID, questName] x26; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Fields under `data`:**

```text
data.questEventType  (string, 45/45 records)
    "questActiveEvent"  x26
    "questFinishEvent"  x19
data.questID  (string, 45/45 records)
    18 unique values (see csv/event_unique_values.csv)
data.questName  (string, 45/45 records)
    18 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/45 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 43 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 3 Dev (16); Unit 3 Dungeon Dev (6)
- **Intervals:** median 4.86s (p5 0.64s / p95 1180.23s, n=42)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "dragStart"  x22
    "dragEnd"  x21
data.featureUsed  (string, 43/43 records)
    "waypoint"  x43
data.location  (object, 43/43 records)
data.location.x  (number, 43/43 records)
    numeric range -801.72 .. 424.231 (22 unique)
data.location.y  (number, 43/43 records)
    numeric range -329.894 .. 330.882 (22 unique)
data.location.z  (number, 43/43 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 40 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (35); Unit 1 Dev (5)
- **Intervals:** median 7.46s (p5 1.72s / p95 68.31s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "argumentationNodeAdd"  x24
    "argumentationNodeRemove"  x16
data.argumentationTitle  (string, 40/40 records)
    "Unit 3 - Pollution Upstream"  x35
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 40/40 records)
    "A"  x10
    "B"  x9
    "5"  x7
    "1"  x5
    "I"  x3
    "2"  x2
    "3"  x2
    "II"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (20)
- **Intervals:** median 1.60s (p5 0.05s / p95 62.57s, n=19)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolClose"  x10
    "argumentationToolOpen"  x10
data.argumentationTitle  (string, 20/20 records)
    "Unit 3 - Pollution Upstream"  x20
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - Pollution Site Data"  x10
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Watershed Image"  x5
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 12 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 62.11s (p5 3.17s / p95 343346.39s, n=11)
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

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 33.55s (p5 5.24s / p95 518034.14s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 7/7 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "Uncaught ReferenceError: onResize is not defined"  x3
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 1 empty-string)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x2
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit2:831:9)"  x1
data.type  (string, 4/4 records)
    "runtime_error"  x3
    "unhandled_rejection"  x1
data.unitId  (string, 4/4 records)
    "unit3"  x3
    "unit2"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 863615.68s (p5 863615.68s / p95 863615.68s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `crash` : exact duplicate records (same timestamp, scene and data)

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TopographicMapEvent` data.actionType: "dragStart" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (16x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*