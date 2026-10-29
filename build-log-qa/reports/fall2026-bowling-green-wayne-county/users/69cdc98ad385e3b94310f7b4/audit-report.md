# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b4

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b4
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7b4.jsonl
- **Records:** 2268 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7b4
- **Time span:** 2026-04-14T19:22:07.767000+00:00 .. 2026-04-22T20:04:22.766000+00:00 (192h 42m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b4\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2268 records, 6 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 53 INFO, 2 NOT_TESTED, 42 PASS.
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
| DialogueEvent | 1507 | 66.45 | 1 | 6 | 1057 | 2026-04-14T19:22:26.604000+00:00 | 2026-04-22T20:02:47.395000+00:00 | 192h 40m |
| PlayerPositionEvent | 516 | 22.75 | 1 | 6 | 0 | 2026-04-14T19:22:07.767000+00:00 | 2026-04-22T20:04:22.766000+00:00 | 192h 42m |
| Topographic Map Event | 54 | 2.38 | 1 | 2 | 0 | 2026-04-14T19:50:58.807000+00:00 | 2026-04-22T19:15:41.816000+00:00 | 191h 24m |
| questEvent | 54 | 2.38 | 1 | 6 | 54 | 2026-04-14T19:22:26.561000+00:00 | 2026-04-22T20:02:42.539000+00:00 | 192h 40m |
| argumentationNodeEvent | 42 | 1.85 | 1 | 3 | 0 | 2026-04-14T19:44:58.405000+00:00 | 2026-04-20T19:36:58.786000+00:00 | 143h 52m |
| TopographicMapEvent | 36 | 1.59 | 1 | 2 | 0 | 2026-04-16T19:06:41.376000+00:00 | 2026-04-22T19:15:36.379000+00:00 | 144h 8m |
| soilMachine | 21 | 0.93 | 1 | 1 | 0 | 2026-04-22T19:44:09.789000+00:00 | 2026-04-22T19:58:50.635000+00:00 | 14m 40s |
| argumentationToolEvent | 16 | 0.71 | 1 | 2 | 0 | 2026-04-20T19:05:32.876000+00:00 | 2026-04-20T19:34:57.981000+00:00 | 29m 25s |
| Soil Key Puzzle | 10 | 0.44 | 1 | 3 | 0 | 2026-04-14T20:07:02.943000+00:00 | 2026-04-22T19:27:49.336000+00:00 | 191h 20m |
| argumentationEvent | 9 | 0.4 | 1 | 3 | 0 | 2026-04-14T19:44:49.744000+00:00 | 2026-04-20T19:37:07.187000+00:00 | 143h 52m |
| EndOfUnit | 3 | 0.13 | 1 | 3 | 0 | 2026-04-14T19:49:57.906000+00:00 | 2026-04-22T19:17:26.270000+00:00 | 191h 27m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 344624.182s median 
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
  - Observed: 42.886s median 
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
  - Observed: 7.385s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.777s median 
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
  - Observed: 1.337s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 10 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 54 records this build 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 42 records 
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
  - Observed: 4 
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
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 13 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7b4.jsonl[129] _id=69de99a87957a33870f3a079 ts=2026-04-14T19:46:48.1960000Z`; `69cdc98ad385e3b94310f7b4.jsonl[1242] _id=69e134071724f0c9e2f6a440 ts=2026-04-16T19:09:59.2640000Z`; `69cdc98ad385e3b94310f7b4.jsonl[1505] _id=69e1412e1724f0c9e2f71014 ts=2026-04-16T20:06:05.4230000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 54 records, TopographicMapEvent: 36 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1506 | 0.003 | 3.054 | 460.572 | 44.102 | 341252.443 | 0.13 | 378 | 3 |
| PlayerPositionEvent | 508 | 29.784 | 30.018 | 1365.195 | 39.145 | 341186.769 | 0.04 | 0 | 3 |
| Topographic Map Event | 53 | 0.89 | 18.882 | 13001.566 | 68571.366 | 342609.932 | 0.0 | 0 | 6 |
| questEvent | 53 | 0.005 | 208.153 | 13087.094 | 68215.717 | 341319.086 | 0.0 | 7 | 9 |
| argumentationNodeEvent | 41 | 0.718 | 7.385 | 12632.204 | 72.102 | 515935.977 | 0.0 | 0 | 2 |
| TopographicMapEvent | 35 | 0.545 | 3.4 | 14826.714 | 52103.204 | 345130.796 | 0.0 | 0 | 2 |
| soilMachine | 20 | 0.146 | 1.337 | 44.042 | 250.382 | 323.889 | 1.36 | 0 | 0 |
| argumentationToolEvent | 15 | 0.01 | 2.777 | 117.674 | 529.262 | 1696.932 | 0.51 | 1 | 1 |
| Soil Key Puzzle | 9 | 2.978 | 42.886 | 76538.488 | 276690.636 | 346562.731 | 0.0 | 0 | 4 |
| argumentationEvent | 8 | 0.15 | 103.5 | 64742.18 | 335895.972 | 515920.614 | 0.0 | 0 | 2 |
| EndOfUnit | 2 | 173168.683 | 344624.182 | 344624.182 | 498934.131 | 516079.681 | 0.0 | 0 | 2 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.018s (p5 29.96s, p95 39.15s, n=508) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `150ms: 69cdc98ad385e3b94310f7b4.jsonl[1878] _id=69e680631724f0c9e2f8e977 ts=2026-04-20T19:37:07.0370000Z ~ 69cdc98ad385e3b94310f7b4.jsonl[1880] _id=69e680641724f0c9e2f8e981 ts=2026-04-20T19:37:07.1870000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `682ms: 69cdc98ad385e3b94310f7b4.jsonl[832] _id=69e925111724f0c9e2fab315 ts=2026-04-22T19:44:17.1470000Z ~ 69cdc98ad385e3b94310f7b4.jsonl[833] _id=69e925121724f0c9e2fab319 ts=2026-04-22T19:44:17.8290000Z`; `216ms: 69cdc98ad385e3b94310f7b4.jsonl[833] _id=69e925121724f0c9e2fab319 ts=2026-04-22T19:44:17.8290000Z ~ 69cdc98ad385e3b94310f7b4.jsonl[834] _id=69e925121724f0c9e2fab31d ts=2026-04-22T19:44:18.0450000Z`; `685ms: 69cdc98ad385e3b94310f7b4.jsonl[834] _id=69e925121724f0c9e2fab31d ts=2026-04-22T19:44:18.0450000Z ~ 69cdc98ad385e3b94310f7b4.jsonl[827] _id=69e925131724f0c9e2fab31f ts=2026-04-22T19:44:18.7300000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 47m 
  - Evidence: 94h 47m: 69cdc98ad385e3b94310f7b4.jsonl[1537] _id=69e141751724f0c9e2f711dd ts=2026-04-16T20:07:16.2810000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1555] _id=69e676791724f0c9e2f8bb69 ts=2026-04-20T18:54:48.7240000Z; 46h 43m: 69cdc98ad385e3b94310f7b4.jsonl[2004] _id=69e687961724f0c9e2f900ff ts=2026-04-20T20:07:49.6990000Z -> 69cdc98ad385e3b94310f7b4.jsonl[2024] _id=69e918941724f0c9e2fa83d7 ts=2026-04-22T18:51:00.3250000Z; 46h 41m: 69cdc98ad385e3b94310f7b4.jsonl[1101] _id=69de9eee7957a33870f3b739 ts=2026-04-14T20:09:18.6200000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1143] _id=69e12f9a1724f0c9e2f68f6c ts=2026-04-16T18:51:05.7630000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 378 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7b4.jsonl[1188] _id=69e131561724f0c9e2f69574 ts=2026-04-16T18:58:29.8320000Z -> 69cdc98ad385e3b94310f7b4.jsonl[227] _id=69e131561724f0c9e2f69576 ts=2026-04-16T18:58:29.8350000Z; 3ms: 69cdc98ad385e3b94310f7b4.jsonl[152] _id=69de9a137957a33870f3a289 ts=2026-04-14T19:48:35.1950000Z -> 69cdc98ad385e3b94310f7b4.jsonl[995] _id=69de9a137957a33870f3a28b ts=2026-04-14T19:48:35.1980000Z; 3ms: 69cdc98ad385e3b94310f7b4.jsonl[2107] _id=69e91c5c1724f0c9e2fa93ab ts=2026-04-22T19:07:07.5500000Z -> 69cdc98ad385e3b94310f7b4.jsonl[2106] _id=69e91c5c1724f0c9e2fa93ad ts=2026-04-22T19:07:07.5530000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 21m 
  - Evidence: 143h 21m: 69cdc98ad385e3b94310f7b4.jsonl[1009] _id=69de9a667957a33870f3a3fb ts=2026-04-14T19:49:57.9060000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1691] _id=69e67a551724f0c9e2f8cd7f ts=2026-04-20T19:11:17.5870000Z; 48h 6m: 69cdc98ad385e3b94310f7b4.jsonl[1691] _id=69e67a551724f0c9e2f8cd7f ts=2026-04-20T19:11:17.5870000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1136] _id=69e91ec61724f0c9e2fa9d65 ts=2026-04-22T19:17:26.2700000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc98ad385e3b94310f7b4.jsonl[1538] _id=69e141951724f0c9e2f71268 ts=2026-04-16T20:07:49.3540000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1552] _id=69e676591724f0c9e2f8bae7 ts=2026-04-20T18:54:16.1230000Z; 46h 42m: 69cdc98ad385e3b94310f7b4.jsonl[2005] _id=69e6877d1724f0c9e2f90083 ts=2026-04-20T20:07:24.9120000Z -> 69cdc98ad385e3b94310f7b4.jsonl[732] _id=69e918661724f0c9e2fa82f1 ts=2026-04-22T18:50:13.2290000Z; 46h 42m: 69cdc98ad385e3b94310f7b4.jsonl[1096] _id=69de9ed77957a33870f3b711 ts=2026-04-14T20:08:54.8790000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1141] _id=69e12f961724f0c9e2f68f60 ts=2026-04-16T18:51:01.3910000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 69cdc98ad385e3b94310f7b4.jsonl[1308] _id=69e137cc1724f0c9e2f6c726 ts=2026-04-16T19:26:04.7690000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1908] _id=69e6818f1724f0c9e2f8eeb1 ts=2026-04-20T19:42:07.5000000Z; 47h 44m: 69cdc98ad385e3b94310f7b4.jsonl[1911] _id=69e681ad1724f0c9e2f8ef1d ts=2026-04-20T19:42:37.5680000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1993] _id=69e921181724f0c9e2faa349 ts=2026-04-22T19:27:20.0610000Z; 46h 50m: 69cdc98ad385e3b94310f7b4.jsonl[1076] _id=69de9e6a7957a33870f3b57d ts=2026-04-14T20:07:05.9210000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1180] _id=69e131091724f0c9e2f69485 ts=2026-04-16T18:57:13.2840000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 10m 
  - Evidence: 95h 10m: 69cdc98ad385e3b94310f7b4.jsonl[1426] _id=69e13ccf1724f0c9e2f6fe18 ts=2026-04-16T19:47:27.1930000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1591] _id=69e677211724f0c9e2f8be77 ts=2026-04-20T18:57:37.1250000Z; 47h 40m: 69cdc98ad385e3b94310f7b4.jsonl[1804] _id=69e67e491724f0c9e2f8df87 ts=2026-04-20T19:28:08.7600000Z -> 69cdc98ad385e3b94310f7b4.jsonl[2116] _id=69e91ccb1724f0c9e2fa9595 ts=2026-04-22T19:08:59.2740000Z; 47h 0m: 69cdc98ad385e3b94310f7b4.jsonl[1071] _id=69de9df67957a33870f3b3d3 ts=2026-04-14T20:05:10.3400000Z -> 69cdc98ad385e3b94310f7b4.jsonl[272] _id=69e132f01724f0c9e2f69e8c ts=2026-04-16T19:05:20.4480000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 69cdc98ad385e3b94310f7b4.jsonl[319] _id=69e136f51724f0c9e2f6b844 ts=2026-04-16T19:22:29.4930000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1707] _id=69e67b201724f0c9e2f8d059 ts=2026-04-20T19:14:40.2890000Z; 47h 51m: 69cdc98ad385e3b94310f7b4.jsonl[1726] _id=69e67bd01724f0c9e2f8d3b1 ts=2026-04-20T19:17:36.4190000Z -> 69cdc98ad385e3b94310f7b4.jsonl[2117] _id=69e91cd21724f0c9e2fa95b7 ts=2026-04-22T19:09:05.6520000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 18m 
  - Evidence: 143h 18m: 69cdc98ad385e3b94310f7b4.jsonl[134] _id=69de99a87957a33870f3a077 ts=2026-04-14T19:46:48.1680000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1640] _id=69e678f91724f0c9e2f8c6c7 ts=2026-04-20T19:05:28.7820000Z; 26m 4s: 69cdc98ad385e3b94310f7b4.jsonl[579] _id=69e679901724f0c9e2f8c9d5 ts=2026-04-20T19:08:00.2730000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1836] _id=69e67fad1724f0c9e2f8e67d ts=2026-04-20T19:34:04.7660000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 18m 
  - Evidence: 143h 18m: 69cdc98ad385e3b94310f7b4.jsonl[133] _id=69de99a37957a33870f3a063 ts=2026-04-14T19:46:43.3560000Z -> 69cdc98ad385e3b94310f7b4.jsonl[547] _id=69e679031724f0c9e2f8c6f3 ts=2026-04-20T19:05:39.3330000Z; 26m 35s: 69cdc98ad385e3b94310f7b4.jsonl[1657] _id=69e6798e1724f0c9e2f8c9cf ts=2026-04-20T19:07:58.5600000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1847] _id=69e67fca1724f0c9e2f8e725 ts=2026-04-20T19:34:34.3250000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 28m 16s 
  - Evidence: 28m 16s: 69cdc98ad385e3b94310f7b4.jsonl[1642] _id=69e679171724f0c9e2f8c787 ts=2026-04-20T19:05:59.0330000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1849] _id=69e67fb81724f0c9e2f8e6b9 ts=2026-04-20T19:34:15.9650000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.010s..0.010s shown 
  - Evidence: 10ms: 69cdc98ad385e3b94310f7b4.jsonl[551] _id=69e679111724f0c9e2f8c74f ts=2026-04-20T19:05:52.9870000Z -> 69cdc98ad385e3b94310f7b4.jsonl[552] _id=69e679111724f0c9e2f8c755 ts=2026-04-20T19:05:52.9970000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 48m 
  - Evidence: 94h 48m: 69cdc98ad385e3b94310f7b4.jsonl[1497] _id=69e1411d1724f0c9e2f70f7c ts=2026-04-16T20:05:47.7850000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1553] _id=69e676661724f0c9e2f8bb05 ts=2026-04-20T18:54:26.8710000Z; 47h 6m: 69cdc98ad385e3b94310f7b4.jsonl[1918] _id=69e681e71724f0c9e2f8f021 ts=2026-04-20T19:43:35.2640000Z -> 69cdc98ad385e3b94310f7b4.jsonl[2021] _id=69e918671724f0c9e2fa8301 ts=2026-04-22T18:50:14.6070000Z; 46h 43m: 69cdc98ad385e3b94310f7b4.jsonl[1077] _id=69de9e837957a33870f3b5dd ts=2026-04-14T20:07:30.7530000Z -> 69cdc98ad385e3b94310f7b4.jsonl[1145] _id=69e12f991724f0c9e2f68f66 ts=2026-04-16T18:51:04.2210000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.005s..0.010s shown 
  - Evidence: 5ms: 69cdc98ad385e3b94310f7b4.jsonl[120] _id=69de98e07957a33870f39d3d ts=2026-04-14T19:43:27.9880000Z -> 69cdc98ad385e3b94310f7b4.jsonl[121] _id=69de98e07957a33870f39d3f ts=2026-04-14T19:43:27.9930000Z; 9ms: 69cdc98ad385e3b94310f7b4.jsonl[841] _id=69e9257c1724f0c9e2fab4e5 ts=2026-04-22T19:46:04.0030000Z -> 69cdc98ad385e3b94310f7b4.jsonl[842] _id=69e9257c1724f0c9e2fab4e8 ts=2026-04-22T19:46:04.0120000Z; 10ms: 69cdc98ad385e3b94310f7b4.jsonl[2221] _id=69e926c51724f0c9e2fab8b9 ts=2026-04-22T19:51:32.5150000Z -> 69cdc98ad385e3b94310f7b4.jsonl[2225] _id=69e926c51724f0c9e2fab8bb ts=2026-04-22T19:51:32.5250000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc98ad385e3b94310f7b4.jsonl:69cdc98ad385e3b94310f7b4, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7b4.jsonl[1076] _id=69de9e6a7957a33870f3b57d ts=2026-04-14T20:07:05.9210000Z`; `69cdc98ad385e3b94310f7b4.jsonl[1185] _id=69e1312d1724f0c9e2f694fa ts=2026-04-16T18:57:49.5360000Z`; `69cdc98ad385e3b94310f7b4.jsonl[1308] _id=69e137cc1724f0c9e2f6c726 ts=2026-04-16T19:26:04.7690000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 36 record(s) match the trigger in 69cdc98ad385e3b94310f7b4.jsonl:69cdc98ad385e3b94310f7b4, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7b4.jsonl[1227] _id=69e133411724f0c9e2f69fee ts=2026-04-16T19:06:41.3760000Z`; `69cdc98ad385e3b94310f7b4.jsonl[274] _id=69e133421724f0c9e2f69ff4 ts=2026-04-16T19:06:41.9730000Z`; `69cdc98ad385e3b94310f7b4.jsonl[273] _id=69e133531724f0c9e2f6a05a ts=2026-04-16T19:06:58.3580000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7b4.jsonl[1380] _id=69e13b831724f0c9e2f6f7e4 ts=2026-04-16T19:41:55.3540000Z`; `69cdc98ad385e3b94310f7b4.jsonl[1749] _id=69e67ca81724f0c9e2f8d7d1 ts=2026-04-20T19:21:12.5430000Z`; `69cdc98ad385e3b94310f7b4.jsonl[633] _id=69e67d421724f0c9e2f8db1b ts=2026-04-20T19:23:46.0920000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7b4.jsonl[1880] _id=69e680641724f0c9e2f8e981 ts=2026-04-20T19:37:07.1870000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7b4.jsonl[666] _id=69e67fbe1724f0c9e2f8e6df ts=2026-04-20T19:34:22.1000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 154 unmatched 'DialogueStartEvent' (totals: 300 start, 150 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 8 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 8 unmatched 'questActiveEvent' (totals: 31 start, 23 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.33s, min -7.50s, max -0.13s over 2268 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b4\coverage.yaml

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
  - Observed: 54 records 
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

### `DialogueEvent` — 1507 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (742); Unit 3 Dev (281); Unit 1 Dev (185); Unit 3 Dungeon Dev (157); Unit 4 Dev - Dungeon (90); Unit 4 Dev (52)
- **eventKey:** present on 1057 of 1507 records
- **Intervals:** median 3.05s (p5 0.01s / p95 44.10s, n=1506)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1057; [conversationId, dialogueEventType] x450
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1507/1507 records)
    numeric range 8 .. 107 (38 unique)
data.dialogueEventType  (string, 1507/1507 records)
    "DialogueNodeEvent"  x1057
    "DialogueStartEvent"  x300
    "DialogueFinishEvent"  x150
data.nodeId  (number, 1057/1507 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 516 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (216); Unit 3 Dev (77); Unit 3 Dungeon Dev (74); Unit 1 Dev (56); Unit 4 Dev - Dungeon (56); Unit 4 Dev (37)
- **Intervals:** median 30.02s (p5 29.96s / p95 39.15s, n=508)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 516/516 records)
data.position.x  (number, 516/516 records)
    numeric range -688.507 .. 1423.49 (296 unique)
data.position.y  (number, 516/516 records)
    numeric range -115.127 .. 157.988 (224 unique)
data.position.z  (number, 516/516 records)
    numeric range -1118 .. 1817.01 (296 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 54 records

- **Scenes:** Unit 3 Dev (32); Unit 2 Prod (Refactor) (22)
- **Intervals:** median 18.88s (p5 3.84s / p95 68571.37s, n=53)
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "MapCloseEvent"  x27
    "MapOpenEvent"  x27
data.featureUsed  (string, 54/54 records)
    "Map"  x54
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 54 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (13); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 54 of 54 records
- **Intervals:** median 208.15s (p5 0.01s / p95 68215.72s, n=53)
- **`data` key-set variants:** [questEventType, questID, questName] x31; [questEventType, questID, questName, questSuccessOrFailure] x23
- **Fields under `data`:**

```text
data.questEventType  (string, 54/54 records)
    "questActiveEvent"  x31
    "questFinishEvent"  x23
data.questID  (string, 54/54 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 54/54 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 23/54 records)
    "Succeeded"  x23
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 42 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 3 Dev (15); Unit 1 Dev (6)
- **Intervals:** median 7.38s (p5 1.29s / p95 72.10s, n=41)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "argumentationNodeAdd"  x27
    "argumentationNodeRemove"  x15
data.argumentationTitle  (string, 42/42 records)
    "Unit 2 – Watershed"  x21
    "Unit 3 - Pollution Upstream"  x15
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 42/42 records)
    "I"  x11
    "B"  x7
    "1"  x5
    "A"  x5
    "C"  x4
    "II"  x3
    "2"  x2
    "3"  x2
    "D"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 36 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (26); Unit 2 Prod (Refactor) (10)
- **Intervals:** median 3.40s (p5 0.59s / p95 52103.20s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "dragEnd"  x18
    "dragStart"  x18
data.featureUsed  (string, 36/36 records)
    "waypoint"  x36
data.location  (object, 36/36 records)
data.location.x  (number, 36/36 records)
    numeric range -775.042 .. 379.363 (19 unique)
data.location.y  (number, 36/36 records)
    numeric range -307.4 .. 259.547 (19 unique)
data.location.z  (number, 36/36 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 1.34s (p5 0.15s / p95 250.38s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Sand"  x16
    "Clay"  x2
    "Gravel"  x2
    "Bedrock"  x1
data.floor  (string, 21/21 records)
    "3"  x15
    "5"  x5
    "4"  x1
data.machine  (string, 21/21 records)
    "1"  x19
    "2"  x2
data.row  (string, 21/21 records)
    "TopRow"  x19
    "BottomRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (8)
- **Intervals:** median 2.78s (p5 0.04s / p95 529.26s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolClose"  x8
    "argumentationToolOpen"  x8
data.argumentationTitle  (string, 16/16 records)
    "Unit 2 – Watershed"  x8
    "Unit 3 - Pollution Upstream"  x8
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - Pollution Site Data"  x6
    "BackingInfoPanel - Waterfall Data"  x4
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 42.89s (p5 13.50s / p95 276690.64s, n=9)
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

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 103.50s (p5 7.47s / p95 335895.97s, n=8)
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

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 344624.18s (p5 190314.23s / p95 498934.13s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
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
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (18x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (15x)
- `soilMachine` data.canisterType: "Bedrock" (1x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*