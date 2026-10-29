# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75b
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f75b.jsonl
- **Records:** 2342 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f75b
- **Time span:** 2026-04-15T19:40:20.504000+00:00 .. 2026-04-23T20:11:00.874000+00:00 (192h 30m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **12 event types**, 2342 records, 7 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 58 INFO, 2 NOT_TESTED, 42 PASS.
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
| DialogueEvent | 1689 | 72.12 | 1 | 7 | 1182 | 2026-04-15T19:40:39.882000+00:00 | 2026-04-23T20:11:00.874000+00:00 | 192h 30m |
| PlayerPositionEvent | 412 | 17.59 | 1 | 7 | 0 | 2026-04-15T19:40:20.504000+00:00 | 2026-04-23T20:10:59.131000+00:00 | 192h 30m |
| questEvent | 64 | 2.73 | 1 | 7 | 64 | 2026-04-15T19:40:39.853000+00:00 | 2026-04-23T20:11:00.615000+00:00 | 192h 30m |
| Topographic Map Event | 40 | 1.71 | 1 | 2 | 0 | 2026-04-15T20:00:41.760000+00:00 | 2026-04-21T19:56:20.644000+00:00 | 143h 55m |
| TopographicMapEvent | 34 | 1.45 | 1 | 2 | 0 | 2026-04-17T19:23:11.321000+00:00 | 2026-04-21T19:56:19.225000+00:00 | 96h 33m |
| argumentationNodeEvent | 33 | 1.41 | 1 | 3 | 0 | 2026-04-15T19:55:54.296000+00:00 | 2026-04-21T19:34:16.418000+00:00 | 143h 38m |
| soilMachine | 26 | 1.11 | 1 | 1 | 0 | 2026-04-23T19:56:01.564000+00:00 | 2026-04-23T20:03:54.469000+00:00 | 7m 52s |
| argumentationToolEvent | 24 | 1.02 | 1 | 2 | 0 | 2026-04-21T19:07:47.422000+00:00 | 2026-04-21T19:33:34.920000+00:00 | 25m 47s |
| argumentationEvent | 9 | 0.38 | 1 | 3 | 0 | 2026-04-15T19:54:55.613000+00:00 | 2026-04-21T19:34:17.953000+00:00 | 143h 39m |
| Soil Key Puzzle | 6 | 0.26 | 1 | 3 | 0 | 2026-04-17T19:48:50.735000+00:00 | 2026-04-23T19:40:37.020000+00:00 | 143h 51m |
| EndOfUnit | 3 | 0.13 | 1 | 3 | 0 | 2026-04-15T19:59:39.870000+00:00 | 2026-04-21T20:00:06.020000+00:00 | 144h 0m |
| crash | 2 | 0.09 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 259213.075s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.014s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 152.216s median 
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
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.828s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.779s median 
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
  - Observed: 3.949s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 412 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 40 records this build 
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
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 33 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
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
  - Observed: 16 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[539] _id=69dfed5f7957a33870f49141 ts=2026-04-15T19:56:15.2900000Z`; `69cdc937d385e3b94310f75b.jsonl[782] _id=69e284811724f0c9e2f79b16 ts=2026-04-17T19:05:37.2490000Z`; `69cdc937d385e3b94310f75b.jsonl[973] _id=69e288811724f0c9e2f7abb0 ts=2026-04-17T19:22:40.9670000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 34 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1688 | 0.0 | 2.009 | 410.557 | 35.146 | 341071.772 | 0.15 | 428 | 3 |
| PlayerPositionEvent | 403 | 29.754 | 30.014 | 1719.069 | 44.385 | 341014.931 | 0.03 | 0 | 3 |
| questEvent | 63 | 0.003 | 135.828 | 11000.33 | 935.572 | 341311.921 | 0.01 | 7 | 8 |
| Topographic Map Event | 39 | 2.217 | 19.244 | 13285.612 | 18375.861 | 342512.559 | 0.0 | 0 | 6 |
| TopographicMapEvent | 33 | 0.256 | 3.197 | 10532.967 | 1342.329 | 343914.918 | 0.01 | 0 | 3 |
| argumentationNodeEvent | 32 | 0.956 | 4.828 | 16159.441 | 664.04 | 515464.856 | 0.0 | 0 | 2 |
| soilMachine | 25 | 0.151 | 3.949 | 18.916 | 83.425 | 144.838 | 3.17 | 0 | 0 |
| argumentationToolEvent | 23 | 0.038 | 0.779 | 67.283 | 20.907 | 1482.596 | 0.89 | 3 | 1 |
| argumentationEvent | 8 | 0.079 | 83.325 | 64645.293 | 335509.971 | 515428.239 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 5 | 13.855 | 152.216 | 103581.257 | 310491.205 | 344917.309 | 0.0 | 0 | 2 |
| EndOfUnit | 2 | 2888.653 | 259213.075 | 259213.075 | 489905.055 | 515537.497 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.014s (p5 29.96s, p95 44.38s, n=403) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `79ms: 69cdc937d385e3b94310f75b.jsonl[1816] _id=69e7d13a1724f0c9e2f9e007 ts=2026-04-21T19:34:17.8740000Z ~ 69cdc937d385e3b94310f75b.jsonl[1826] _id=69e7d13b1724f0c9e2f9e013 ts=2026-04-21T19:34:17.9530000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `817ms: 69cdc937d385e3b94310f75b.jsonl[1796] _id=69e7d0ed1724f0c9e2f9de29 ts=2026-04-21T19:33:00.1590000Z ~ 69cdc937d385e3b94310f75b.jsonl[1798] _id=69e7d0ed1724f0c9e2f9de33 ts=2026-04-21T19:33:00.9760000Z`; `827ms: 69cdc937d385e3b94310f75b.jsonl[1797] _id=69e7d0ed1724f0c9e2f9de2b ts=2026-04-21T19:33:00.1970000Z ~ 69cdc937d385e3b94310f75b.jsonl[1799] _id=69e7d0ed1724f0c9e2f9de35 ts=2026-04-21T19:33:01.0240000Z`; `722ms: 69cdc937d385e3b94310f75b.jsonl[323] _id=69e7d10c1724f0c9e2f9ded6 ts=2026-04-21T19:33:31.9570000Z ~ 69cdc937d385e3b94310f75b.jsonl[1805] _id=69e7d10d1724f0c9e2f9dedf ts=2026-04-21T19:33:32.6790000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `579ms: 69cdc937d385e3b94310f75b.jsonl[2259] _id=69ea7a471724f0c9e2fb6501 ts=2026-04-23T20:00:06.2610000Z ~ 69cdc937d385e3b94310f75b.jsonl[2260] _id=69ea7a471724f0c9e2fb6505 ts=2026-04-23T20:00:06.8400000Z`; `418ms: 69cdc937d385e3b94310f75b.jsonl[2260] _id=69ea7a471724f0c9e2fb6505 ts=2026-04-23T20:00:06.8400000Z ~ 69cdc937d385e3b94310f75b.jsonl[378] _id=69ea7a481724f0c9e2fb6509 ts=2026-04-23T20:00:07.2580000Z`; `266ms: 69cdc937d385e3b94310f75b.jsonl[378] _id=69ea7a481724f0c9e2fb6509 ts=2026-04-23T20:00:07.2580000Z ~ 69cdc937d385e3b94310f75b.jsonl[376] _id=69ea7a481724f0c9e2fb650b ts=2026-04-23T20:00:07.5240000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f75b.jsonl[1367] _id=69e293751724f0c9e2f7dc28 ts=2026-04-17T20:09:25.0890000Z -> 69cdc937d385e3b94310f75b.jsonl[1374] _id=69e7c7c51724f0c9e2f9ad67 ts=2026-04-21T18:53:56.8610000Z; 47h 32m: 69cdc937d385e3b94310f75b.jsonl[2083] _id=69e7d8371724f0c9e2f9fc57 ts=2026-04-21T20:04:06.3890000Z -> 69cdc937d385e3b94310f75b.jsonl[2097] _id=69ea74b21724f0c9e2fb55a9 ts=2026-04-23T19:36:17.5190000Z; 46h 36m: 69cdc937d385e3b94310f75b.jsonl[631] _id=69dff1147957a33870f49fb9 ts=2026-04-15T20:12:03.3280000Z -> 69cdc937d385e3b94310f75b.jsonl[636] _id=69e280831724f0c9e2f78d3a ts=2026-04-17T18:48:35.3650000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 428 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f75b.jsonl[1581] _id=69e7cbfe1724f0c9e2f9c4a9 ts=2026-04-21T19:11:57.3890000Z -> 69cdc937d385e3b94310f75b.jsonl[1583] _id=69e7cc171724f0c9e2f9c539 ts=2026-04-21T19:11:57.389Z; 2ms: 69cdc937d385e3b94310f75b.jsonl[1247] _id=69e291c81724f0c9e2f7d3b0 ts=2026-04-17T20:02:16.6440000Z -> 69cdc937d385e3b94310f75b.jsonl[1249] _id=69e291c91724f0c9e2f7d3b2 ts=2026-04-17T20:02:16.6460000Z; 3ms: 69cdc937d385e3b94310f75b.jsonl[1237] _id=69e2919f1724f0c9e2f7d326 ts=2026-04-17T20:01:35.1590000Z -> 69cdc937d385e3b94310f75b.jsonl[1236] _id=69e2919f1724f0c9e2f7d328 ts=2026-04-17T20:01:35.1620000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 12m 
  - Evidence: 143h 12m: 69cdc937d385e3b94310f75b.jsonl[573] _id=69dfee2c7957a33870f4949d ts=2026-04-15T19:59:39.8700000Z -> 69cdc937d385e3b94310f75b.jsonl[1582] _id=69e7cbfe1724f0c9e2f9c4a7 ts=2026-04-21T19:11:57.3670000Z; 48m 8s: 69cdc937d385e3b94310f75b.jsonl[1582] _id=69e7cbfe1724f0c9e2f9c4a7 ts=2026-04-21T19:11:57.3670000Z -> 69cdc937d385e3b94310f75b.jsonl[2075] _id=69e7d7461724f0c9e2f9f8e5 ts=2026-04-21T20:00:06.0200000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc937d385e3b94310f75b.jsonl[1368] _id=69e2937a1724f0c9e2f7dc36 ts=2026-04-17T20:09:29.8990000Z -> 69cdc937d385e3b94310f75b.jsonl[1371] _id=69e7c7921724f0c9e2f9ac85 ts=2026-04-21T18:53:04.8300000Z; 47h 29m: 69cdc937d385e3b94310f75b.jsonl[2092] _id=69e7d8c11724f0c9e2f9fed5 ts=2026-04-21T20:06:24.7910000Z -> 69cdc937d385e3b94310f75b.jsonl[2094] _id=69ea74981724f0c9e2fb558b ts=2026-04-23T19:35:51.8860000Z; 46h 36m: 69cdc937d385e3b94310f75b.jsonl[629] _id=69dff10f7957a33870f49fb5 ts=2026-04-15T20:11:59.3110000Z -> 69cdc937d385e3b94310f75b.jsonl[641] _id=69e280801724f0c9e2f78d36 ts=2026-04-17T18:48:31.0700000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 48m 
  - Evidence: 95h 48m: 69cdc937d385e3b94310f75b.jsonl[1177] _id=69e28ec71724f0c9e2f7c97e ts=2026-04-17T19:49:26.8510000Z -> 69cdc937d385e3b94310f75b.jsonl[1865] _id=69e7d21d1724f0c9e2f9e4f0 ts=2026-04-21T19:38:04.1600000Z; 47h 59m: 69cdc937d385e3b94310f75b.jsonl[1871] _id=69e7d22a1724f0c9e2f9e547 ts=2026-04-21T19:38:18.0150000Z -> 69cdc937d385e3b94310f75b.jsonl[2104] _id=69ea751d1724f0c9e2fb568f ts=2026-04-23T19:38:04.8040000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 8m 
  - Evidence: 95h 8m: 69cdc937d385e3b94310f75b.jsonl[265] _id=69e293711724f0c9e2f7dc10 ts=2026-04-17T20:09:21.5070000Z -> 69cdc937d385e3b94310f75b.jsonl[1626] _id=69e7cd621724f0c9e2f9cdbf ts=2026-04-21T19:17:54.0660000Z; 47h 2m: 69cdc937d385e3b94310f75b.jsonl[578] _id=69dfee777957a33870f49605 ts=2026-04-15T20:00:55.1160000Z -> 69cdc937d385e3b94310f75b.jsonl[758] _id=69e283e91724f0c9e2f798b8 ts=2026-04-17T19:03:04.9780000Z; 26m 43s: 69cdc937d385e3b94310f75b.jsonl[1707] _id=69e7cfa91724f0c9e2f9d6db ts=2026-04-21T19:27:36.6160000Z -> 69cdc937d385e3b94310f75b.jsonl[2005] _id=69e7d5ec1724f0c9e2f9f32d ts=2026-04-21T19:54:19.8100000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 69cdc937d385e3b94310f75b.jsonl[1135] _id=69e28d881724f0c9e2f7bf08 ts=2026-04-17T19:44:07.9390000Z -> 69cdc937d385e3b94310f75b.jsonl[1404] _id=69e7ccf31724f0c9e2f9cb81 ts=2026-04-21T19:16:02.8570000Z; 34m 46s: 69cdc937d385e3b94310f75b.jsonl[1628] _id=69e7cd691724f0c9e2f9cdf5 ts=2026-04-21T19:18:00.3020000Z -> 69cdc937d385e3b94310f75b.jsonl[1997] _id=69e7d58f1724f0c9e2f9f1b3 ts=2026-04-21T19:52:46.9470000Z; 14m 6s: 69cdc937d385e3b94310f75b.jsonl[980] _id=69e288b01724f0c9e2f7ac96 ts=2026-04-17T19:23:27.5010000Z -> 69cdc937d385e3b94310f75b.jsonl[169] _id=69e28bfd1724f0c9e2f7b85a ts=2026-04-17T19:37:33.6190000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 10m 
  - Evidence: 143h 10m: 69cdc937d385e3b94310f75b.jsonl[536] _id=69dfed5f7957a33870f4913f ts=2026-04-15T19:56:15.2600000Z -> 69cdc937d385e3b94310f75b.jsonl[280] _id=69e7cac41724f0c9e2f9bd99 ts=2026-04-21T19:06:43.4990000Z; 22m 56s: 69cdc937d385e3b94310f75b.jsonl[1527] _id=69e7cb521724f0c9e2f9c0fd ts=2026-04-21T19:09:04.9660000Z -> 69cdc937d385e3b94310f75b.jsonl[1774] _id=69e7d0b11724f0c9e2f9dc6d ts=2026-04-21T19:32:01.0120000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 11m 
  - Evidence: 143h 11m: 69cdc937d385e3b94310f75b.jsonl[534] _id=69dfed5a7957a33870f49131 ts=2026-04-15T19:56:10.5020000Z -> 69cdc937d385e3b94310f75b.jsonl[1503] _id=69e7cae41724f0c9e2f9be45 ts=2026-04-21T19:07:15.3580000Z; 23m 8s: 69cdc937d385e3b94310f75b.jsonl[1526] _id=69e7cb501724f0c9e2f9c0f3 ts=2026-04-21T19:09:03.5640000Z -> 69cdc937d385e3b94310f75b.jsonl[1776] _id=69e7d0bc1724f0c9e2f9dcd3 ts=2026-04-21T19:32:11.9250000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 24m 42s 
  - Evidence: 24m 42s: 69cdc937d385e3b94310f75b.jsonl[1505] _id=69e7cb161724f0c9e2f9bfb3 ts=2026-04-21T19:08:05.1270000Z -> 69cdc937d385e3b94310f75b.jsonl[318] _id=69e7d0e01724f0c9e2f9ddd9 ts=2026-04-21T19:32:47.7230000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.038s..0.048s shown 
  - Evidence: 38ms: 69cdc937d385e3b94310f75b.jsonl[1796] _id=69e7d0ed1724f0c9e2f9de29 ts=2026-04-21T19:33:00.1590000Z -> 69cdc937d385e3b94310f75b.jsonl[1797] _id=69e7d0ed1724f0c9e2f9de2b ts=2026-04-21T19:33:00.1970000Z; 48ms: 69cdc937d385e3b94310f75b.jsonl[1798] _id=69e7d0ed1724f0c9e2f9de33 ts=2026-04-21T19:33:00.9760000Z -> 69cdc937d385e3b94310f75b.jsonl[1799] _id=69e7d0ed1724f0c9e2f9de35 ts=2026-04-21T19:33:01.0240000Z; 48ms: 69cdc937d385e3b94310f75b.jsonl[1806] _id=69e7d1081724f0c9e2f9debd ts=2026-04-21T19:33:27.6340000Z -> 69cdc937d385e3b94310f75b.jsonl[1807] _id=69e7d1081724f0c9e2f9debf ts=2026-04-21T19:33:27.6820000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 48m 
  - Evidence: 94h 48m: 69cdc937d385e3b94310f75b.jsonl[1273] _id=69e292541724f0c9e2f7d634 ts=2026-04-17T20:04:35.9360000Z -> 69cdc937d385e3b94310f75b.jsonl[1372] _id=69e7c7951724f0c9e2f9aca3 ts=2026-04-21T18:53:07.8570000Z; 47h 31m: 69cdc937d385e3b94310f75b.jsonl[2086] _id=69e7d8351724f0c9e2f9fc4b ts=2026-04-21T20:04:04.4510000Z -> 69cdc937d385e3b94310f75b.jsonl[2093] _id=69ea749b1724f0c9e2fb558f ts=2026-04-23T19:35:54.2910000Z; 46h 46m: 69cdc937d385e3b94310f75b.jsonl[68] _id=69dfeeae7957a33870f496c9 ts=2026-04-15T20:01:49.7880000Z -> 69cdc937d385e3b94310f75b.jsonl[639] _id=69e280821724f0c9e2f78d38 ts=2026-04-17T18:48:33.7580000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.003s..0.010s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f75b.jsonl[519] _id=69dfecec7957a33870f48f33 ts=2026-04-15T19:54:19.9990000Z -> 69cdc937d385e3b94310f75b.jsonl[502] _id=69dfecec7957a33870f48f37 ts=2026-04-15T19:54:20.0020000Z; 10ms: 69cdc937d385e3b94310f75b.jsonl[2247] _id=69ea7a1f1724f0c9e2fb649b ts=2026-04-23T19:59:27.1220000Z -> 69cdc937d385e3b94310f75b.jsonl[2250] _id=69ea7a201724f0c9e2fb649d ts=2026-04-23T19:59:27.1320000Z; 10ms: 69cdc937d385e3b94310f75b.jsonl[455] _id=69dfeb267957a33870f488c1 ts=2026-04-15T19:46:46.2840000Z -> 69cdc937d385e3b94310f75b.jsonl[459] _id=69dfeb267957a33870f488c3 ts=2026-04-15T19:46:46.2940000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc937d385e3b94310f75b.jsonl:69cdc937d385e3b94310f75b, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[1177] _id=69e28ec71724f0c9e2f7c97e ts=2026-04-17T19:49:26.8510000Z`; `69cdc937d385e3b94310f75b.jsonl[1871] _id=69e7d22a1724f0c9e2f9e547 ts=2026-04-21T19:38:18.0150000Z`; `69cdc937d385e3b94310f75b.jsonl[2114] _id=69ea75b51724f0c9e2fb5863 ts=2026-04-23T19:40:37.0200000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 34 record(s) match the trigger in 69cdc937d385e3b94310f75b.jsonl:69cdc937d385e3b94310f75b, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[866] _id=69e288a01724f0c9e2f7ac4d ts=2026-04-17T19:23:11.3210000Z`; `69cdc937d385e3b94310f75b.jsonl[143] _id=69e288a21724f0c9e2f7ac56 ts=2026-04-17T19:23:13.6830000Z`; `69cdc937d385e3b94310f75b.jsonl[978] _id=69e288ad1724f0c9e2f7ac90 ts=2026-04-17T19:23:25.0400000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[228] _id=69e2925e1724f0c9e2f7d680 ts=2026-04-17T20:04:45.9750000Z`; `69cdc937d385e3b94310f75b.jsonl[310] _id=69e7ced11724f0c9e2f9d339 ts=2026-04-21T19:24:01.0680000Z`; `69cdc937d385e3b94310f75b.jsonl[313] _id=69e7cf461724f0c9e2f9d549 ts=2026-04-21T19:25:57.3020000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[1826] _id=69e7d13b1724f0c9e2f9e013 ts=2026-04-21T19:34:17.9530000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[1796] _id=69e7d0ed1724f0c9e2f9de29 ts=2026-04-21T19:33:00.1590000Z`; `69cdc937d385e3b94310f75b.jsonl[1798] _id=69e7d0ed1724f0c9e2f9de33 ts=2026-04-21T19:33:00.9760000Z`; `69cdc937d385e3b94310f75b.jsonl[320] _id=69e7d0f01724f0c9e2f9de41 ts=2026-04-21T19:33:03.7700000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[1441] _id=69e7c90e1724f0c9e2f9b45b ts=?`; `69cdc937d385e3b94310f75b.jsonl[1659] _id=69e7ce551724f0c9e2f9d173 ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f75b.jsonl[1797] _id=69e7d0ed1724f0c9e2f9de2b ts=2026-04-21T19:33:00.1970000Z`; `69cdc937d385e3b94310f75b.jsonl[1799] _id=69e7d0ed1724f0c9e2f9de35 ts=2026-04-21T19:33:01.0240000Z`; `69cdc937d385e3b94310f75b.jsonl[1804] _id=69e7d1071724f0c9e2f9deb9 ts=2026-04-21T19:33:25.8730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 193 unmatched 'DialogueStartEvent' (totals: 348 start, 159 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 12 open, 12 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 38 start, 26 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.77s, min -26.28s, max -0.20s over 2340 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=partial 
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
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 40 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
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

### `DialogueEvent` — 1689 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (953); Unit 3 Dev (289); Unit 1 Dev (174); Unit 4 Dev - Dungeon (100); Unit 4 Dev (87); Unit 3 Dungeon Dev (84); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 1182 of 1689 records
- **Intervals:** median 2.01s (p5 0.01s / p95 35.15s, n=1688)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1182; [conversationId, dialogueEventType] x507
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1689/1689 records)
    numeric range 8 .. 107 (39 unique)
data.dialogueEventType  (string, 1689/1689 records)
    "DialogueNodeEvent"  x1182
    "DialogueStartEvent"  x348
    "DialogueFinishEvent"  x159
data.nodeId  (number, 1182/1689 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 412 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (196); Unit 3 Dev (68); Unit 4 Dev - Dungeon (44); Unit 1 Dev (39); Unit 4 Dev (38); Unit 3 Dungeon Dev (26); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 30.01s (p5 29.96s / p95 44.38s, n=403)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 412/412 records)
data.position.x  (number, 412/412 records)
    numeric range -563.237 .. 1446.87 (254 unique)
data.position.y  (number, 412/412 records)
    numeric range -115.029 .. 158.756 (190 unique)
data.position.z  (number, 412/412 records)
    numeric range -1105.27 .. 2189.31 (254 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 64 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (5); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 64 of 64 records
- **Intervals:** median 135.83s (p5 0.01s / p95 935.57s, n=63)
- **`data` key-set variants:** [questEventType, questID, questName] x38; [questEventType, questID, questName, questSuccessOrFailure] x26
- **Fields under `data`:**

```text
data.questEventType  (string, 64/64 records)
    "questActiveEvent"  x38
    "questFinishEvent"  x26
data.questID  (string, 64/64 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 64/64 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 26/64 records)
    "Succeeded"  x26
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 3 Dev (14)
- **Intervals:** median 19.24s (p5 2.84s / p95 18375.86s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 34 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (20); Unit 2 Prod (Refactor) (14)
- **Intervals:** median 3.20s (p5 0.65s / p95 1342.33s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "dragEnd"  x17
    "dragStart"  x17
data.featureUsed  (string, 34/34 records)
    "waypoint"  x34
data.location  (object, 34/34 records)
data.location.x  (number, 34/34 records)
    numeric range -773.602 .. 342.688 (18 unique)
data.location.y  (number, 34/34 records)
    numeric range -311.618 .. 354.782 (18 unique)
data.location.z  (number, 34/34 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 33 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 3 Dev (11); Unit 1 Dev (5)
- **Intervals:** median 4.83s (p5 1.46s / p95 664.04s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "argumentationNodeAdd"  x21
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 33/33 records)
    "Unit 2 – Watershed"  x17
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x5
data.nodeName  (string, 33/33 records)
    "B"  x11
    "A"  x6
    "1"  x4
    "I"  x4
    "II"  x3
    "C"  x2
    "D"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 3.95s (p5 0.30s / p95 83.42s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Clay"  x13
    "Bedrock"  x7
    "Sand"  x4
    "Gravel"  x2
data.floor  (string, 26/26 records)
    "5"  x20
    "3"  x5
    "4"  x1
data.machine  (string, 26/26 records)
    "1"  x24
    "2"  x2
data.row  (string, 26/26 records)
    "BottomRow"  x15
    "TopRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 24 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (20); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 0.78s (p5 0.05s / p95 20.91s, n=23)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "argumentationToolClose"  x12
    "argumentationToolOpen"  x12
data.argumentationTitle  (string, 24/24 records)
    "Unit 3 - Pollution Upstream"  x20
    "Unit 2 – Watershed"  x4
data.toolName  (string, 24/24 records)
    "BackingInfoPanel - Pollution Site Data"  x12
    "BackingInfoPanel - "  x4
    "BackingInfoPanel - Watershed Image"  x4
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 83.32s (p5 7.60s / p95 335509.97s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 152.22s (p5 18.31s / p95 310491.20s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/6 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/6 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 259213.07s (p5 28521.10s / p95 489905.05s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
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
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit2:831:9)"  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x1
    "unit3"  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
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
- `TopographicMapEvent` data.actionType: "dragStart" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (7x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*