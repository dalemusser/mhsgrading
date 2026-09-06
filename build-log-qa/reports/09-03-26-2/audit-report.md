# MHS Gameplay Log Audit Report — build 09-03-26-2

## 1. Build Information

- **Build ID:** 09-03-26-2
- **Game version string(s) in log:** 2.5.1, 2.5.8, 20260902-12353
- **Audit date:** 2026-09-06
- **Log file(s):** wenyi090326-2.stratalog.logdata.json
- **Records:** 5837 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6a9a063fe2ada9cb13ea75bc
- **Time span:** 2026-09-04T17:47:25.087000+00:00 .. 2026-09-04T20:04:07.223000+00:00 (2h 16m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-03-26-2.yaml
- **Baseline:** snapshot build-log-qa\reports\08-31-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 5837 records, 10 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 94 INFO, 0 NOT_TESTED, 104 PASS.
- Top items needing attention:
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DaniEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: baseline field(s) absent this build
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1737 | 29.76 | 1 | 9 | 1117 | 2026-09-04T17:47:44.446000+00:00 | 2026-09-04T20:04:05.054000+00:00 | 2h 16m |
| InputEvent | 1630 | 27.93 | 1 | 9 | 0 | 2026-09-04T17:48:30.814000+00:00 | 2026-09-04T20:04:07.223000+00:00 | 2h 15m |
| PuzzlePieceVisibleEvent | 1182 | 20.25 | 1 | 4 | 0 | 2026-09-04T18:03:05.416000+00:00 | 2026-09-04T19:30:22.626000+00:00 | 1h 27m |
| PlayerPositionEvent | 638 | 10.93 | 1 | 9 | 0 | 2026-09-04T17:47:27.846000+00:00 | 2026-09-04T20:04:04.019000+00:00 | 2h 16m |
| ObjectInterEvent | 178 | 3.05 | 1 | 9 | 0 | 2026-09-04T17:48:55.792000+00:00 | 2026-09-04T20:04:07.223000+00:00 | 2h 15m |
| argumentationNodeEvent | 133 | 2.28 | 1 | 5 | 0 | 2026-09-04T17:57:18.799000+00:00 | 2026-09-04T19:59:59.163000+00:00 | 2h 2m |
| questEvent | 69 | 1.18 | 1 | 9 | 69 | 2026-09-04T17:47:44.442000+00:00 | 2026-09-04T20:03:29.370000+00:00 | 2h 15m |
| TopographicMapEvent | 44 | 0.75 | 1 | 2 | 0 | 2026-09-04T18:03:23.291000+00:00 | 2026-09-04T18:53:41.732000+00:00 | 50m 18s |
| Soil Key Puzzle | 36 | 0.62 | 1 | 3 | 0 | 2026-09-04T18:05:50.695000+00:00 | 2026-09-04T19:03:51.691000+00:00 | 58m 0s |
| chatEvent | 32 | 0.55 | 1 | 3 | 0 | 2026-09-04T18:19:25.319000+00:00 | 2026-09-04T19:34:33.827000+00:00 | 1h 15m |
| gameWindowUnfocusEvent | 27 | 0.46 | 1 | 7 | 0 | 2026-09-04T17:49:01.823000+00:00 | 2026-09-04T20:02:49.690000+00:00 | 2h 13m |
| gameWindowFocusEvent | 26 | 0.45 | 1 | 7 | 0 | 2026-09-04T17:50:16.989000+00:00 | 2026-09-04T20:03:10.256000+00:00 | 2h 12m |
| argumentationToolEvent | 19 | 0.33 | 1 | 4 | 0 | 2026-09-04T17:57:24.935000+00:00 | 2026-09-04T19:59:39.154000+00:00 | 2h 2m |
| DaniEvent | 16 | 0.27 | 1 | 4 | 0 | 2026-09-04T18:19:24.350000+00:00 | 2026-09-04T19:58:38.762000+00:00 | 1h 39m |
| argumentationEvent | 14 | 0.24 | 1 | 5 | 0 | 2026-09-04T17:57:25.903000+00:00 | 2026-09-04T20:00:00.470000+00:00 | 2h 2m |
| WaterChamberEvent | 12 | 0.21 | 1 | 1 | 0 | 2026-09-04T19:30:30.236000+00:00 | 2026-09-04T19:33:51.112000+00:00 | 3m 20s |
| TerasGardenBox | 8 | 0.14 | 1 | 1 | 0 | 2026-09-04T19:23:11.477000+00:00 | 2026-09-04T19:24:23.277000+00:00 | 1m 11s |
| gameStartEvent | 7 | 0.12 | 1 | 1 | 0 | 2026-09-04T17:47:25.087000+00:00 | 2026-09-04T19:27:16.983000+00:00 | 1h 39m |
| DEBUGMenu | 6 | 0.1 | 1 | 3 | 0 | 2026-09-04T18:46:45.318000+00:00 | 2026-09-04T19:32:45.589000+00:00 | 46m 0s |
| argumentationAnswerEvent | 6 | 0.1 | 1 | 5 | 0 | 2026-09-04T17:57:35.207000+00:00 | 2026-09-04T20:00:00.463000+00:00 | 2h 2m |
| EndOfUnit | 5 | 0.09 | 1 | 5 | 0 | 2026-09-04T18:00:14.183000+00:00 | 2026-09-04T20:04:07.221000+00:00 | 2h 3m |
| soilMachine | 5 | 0.09 | 1 | 1 | 0 | 2026-09-04T19:10:08.170000+00:00 | 2026-09-04T19:12:51.514000+00:00 | 2m 43s |
| SolarStillDesignEvent | 4 | 0.07 | 1 | 1 | 0 | 2026-09-04T20:02:02.316000+00:00 | 2026-09-04T20:02:05.156000+00:00 | 2.8s |
| crash | 3 | 0.05 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DaniEvent` — median interval between records changed substantially. 
  - Observed: 2.369s median 
  - Expected: 14.09s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 1.067s median 
  - Expected: 2.334s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — baseline field(s) absent this build. 
  - Observed: data.boxID 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 0.232s median 
  - Expected: 721.885s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 95.131s median 
  - Expected: 199.213s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 107.559s median 
  - Expected: 216.72s in 08-31-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — event type not present in baseline 08-31-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `DaniEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: Argumentation; Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `DaniEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: ; Settings 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: backquote; tab 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to pick up 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to Insert; Press E to place 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — categorical value(s) not seen in baseline. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: soilSelected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` — field(s) not present in baseline schema. 
  - Observed: data.legendName
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Selected; Unselected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — categorical value(s) not seen in baseline. 
  - Observed: Legend 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineNumber` — baseline categorical value(s) not seen this build. 
  - Observed: Two 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Condenser 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.room` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeRemove 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 16.0x vs baseline. 
  - Observed: 32 records 
  - Expected: 2 in 08-31-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-102, 18-103, 18-105, 18-109, 18-110, 18-274]; [18-109, 18-110, 18-274, 18-112, 18-113, 18-114]; [18-112, 18-113, 18-114, 18-276, 18-277]; [18-114, 18-276, 18-277, 18-279, 18-116, 18-117]; [18-243, 18-118, 74-21, 23-1, 23-2, 23-3]; [18-279, 18-116, 18-117, 18-243, 18-118, 74-21]; [22-19, 22-20, 22-22, 22-46, 22-48, 22-27]; [22-46, 22-48, 22-27, 18-102, 18-103, 18-105]; [23-1, 23-2, 23-3, 23-4, 23-59, 23-61]; [23-17, 23-18, 23-20, 23-21, 23-70, 23-72]; [23-21, 23-70, 23-72, 23-73, 23-22, 23-24]; [23-59, 23-61, 23-63, 23-65, 23-67, 23-68]; [23-65, 23-67, 23-68, 23-69, 23-17, 23-18]; [23-73, 23-22, 23-24, 23-25, 23-27] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 08-31-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 15 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5721] _id=6a9b0506485cab4c953f88bd ts=2026-09-04T17:51:02.0550000Z`; `wenyi090326-2.stratalog.logdata.json[5674] _id=6a9b05b2485cab4c953f8db6 ts=2026-09-04T17:53:54.5040000Z`; `wenyi090326-2.stratalog.logdata.json[5653] _id=6a9b05c4485cab4c953f8e62 ts=2026-09-04T17:54:12.3280000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 7 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 7} 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5833] _id=6a9b042c485cab4c953f8586 ts=2026-09-04T17:47:25.0870000Z`; `wenyi090326-2.stratalog.logdata.json[5419] _id=6a9b0777485cab4c953f928e ts=2026-09-04T18:01:27.1580000Z`; `wenyi090326-2.stratalog.logdata.json[3524] _id=6a9b0ec2485cab4c953fa3da ts=2026-09-04T18:32:35.1500000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5753] _id=6a9b04d8485cab4c953f875a ts=2026-09-04T17:50:16.9890000Z`; `wenyi090326-2.stratalog.logdata.json[5693] _id=6a9b05a6485cab4c953f8d56 ts=2026-09-04T17:53:42.7990000Z`; `wenyi090326-2.stratalog.logdata.json[5598] _id=6a9b0605485cab4c953f8f8a ts=2026-09-04T17:55:17.9300000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5761] _id=6a9b048d485cab4c953f86e6 ts=2026-09-04T17:49:01.8230000Z`; `wenyi090326-2.stratalog.logdata.json[5700] _id=6a9b0567485cab4c953f8b0a ts=2026-09-04T17:52:40.1410000Z`; `wenyi090326-2.stratalog.logdata.json[5599] _id=6a9b0603485cab4c953f8f86 ts=2026-09-04T17:55:15.8180000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 3 of 44 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5303] _id=6a9b07eb485cab4c953f9326 ts=2026-09-04T18:03:23.2910000Z`; `wenyi090326-2.stratalog.logdata.json[5297] _id=6a9b07f2485cab4c953f9332 ts=2026-09-04T18:03:30.1930000Z`; `wenyi090326-2.stratalog.logdata.json[4641] _id=6a9b0922485cab4c953f98a2 ts=2026-09-04T18:08:34.7230000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1736 | 0.0 | 0.667 | 4.712 | 16.895 | 1369.972 | 12.73 | 477 | 1 |
| InputEvent | 1629 | 0.001 | 0.565 | 4.995 | 14.476 | 1348.626 | 12.01 | 47 | 1 |
| PuzzlePieceVisibleEvent | 1181 | 0.0 | 0.033 | 4.435 | 1.036 | 1669.0 | 13.53 | 707 | 4 |
| PlayerPositionEvent | 624 | 9.968 | 10.005 | 12.613 | 10.157 | 1358.161 | 4.76 | 0 | 1 |
| ObjectInterEvent | 177 | 0.0 | 6.466 | 45.827 | 203.359 | 1361.161 | 1.31 | 3 | 1 |
| argumentationNodeEvent | 132 | 0.031 | 0.383 | 55.76 | 34.571 | 2309.018 | 1.08 | 30 | 4 |
| questEvent | 68 | 0.0 | 74.645 | 119.778 | 361.677 | 1498.388 | 0.5 | 12 | 1 |
| TopographicMapEvent | 43 | 0.004 | 2.204 | 70.196 | 453.25 | 1108.562 | 0.85 | 4 | 2 |
| Soil Key Puzzle | 35 | 0.267 | 0.667 | 99.457 | 734.705 | 1783.553 | 0.6 | 0 | 2 |
| chatEvent | 31 | 0.001 | 0.232 | 145.436 | 217.837 | 4066.029 | 0.41 | 1 | 1 |
| gameWindowUnfocusEvent | 26 | 0.0 | 107.559 | 308.764 | 1373.606 | 1915.437 | 0.19 | 1 | 4 |
| gameWindowFocusEvent | 25 | 4.337 | 95.131 | 318.931 | 1402.723 | 1777.794 | 0.19 | 0 | 5 |
| argumentationToolEvent | 18 | 0.333 | 0.901 | 407.457 | 2281.16 | 4598.815 | 0.15 | 0 | 3 |
| DaniEvent | 15 | 0.001 | 2.369 | 396.961 | 2038.878 | 2043.311 | 0.15 | 2 | 3 |
| argumentationEvent | 13 | 0.031 | 52.427 | 565.736 | 2194.006 | 2302.847 | 0.11 | 2 | 4 |
| WaterChamberEvent | 11 | 1.534 | 13.039 | 18.261 | 40.434 | 40.503 | 3.29 | 0 | 0 |
| TerasGardenBox | 7 | 0.9 | 8.004 | 10.257 | 22.718 | 25.179 | 5.85 | 0 | 0 |
| gameStartEvent | 6 | 535.725 | 841.528 | 998.649 | 1712.188 | 1867.992 | 0.06 | 0 | 5 |
| DEBUGMenu | 5 | 3.784 | 7.86 | 552.054 | 1483.252 | 1557.208 | 0.11 | 0 | 2 |
| argumentationAnswerEvent | 5 | 25.712 | 1881.866 | 1469.051 | 2320.6 | 2327.159 | 0.04 | 0 | 4 |
| EndOfUnit | 4 | 1483.091 | 1864.391 | 1858.259 | 2172.961 | 2221.165 | 0.03 | 0 | 4 |
| soilMachine | 4 | 10.405 | 42.837 | 40.836 | 66.45 | 67.265 | 1.47 | 0 | 0 |
| SolarStillDesignEvent | 3 | 0.634 | 1.067 | 0.947 | 1.132 | 1.139 | 63.38 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-2.stratalog.logdata.json[1353] _id=6a9b1934485cab4c953fb4dc ts=2026-09-04T19:17:08.2900000Z == wenyi090326-2.stratalog.logdata.json[1352] _id=6a9b1934485cab4c953fb4de ts=2026-09-04T19:17:08.2900000Z`; `wenyi090326-2.stratalog.logdata.json[1319] _id=6a9b1959485cab4c953fb520 ts=2026-09-04T19:17:45.7410000Z == wenyi090326-2.stratalog.logdata.json[1318] _id=6a9b1959485cab4c953fb522 ts=2026-09-04T19:17:45.7410000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 19 group(s), 25 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5229] _id=6a9b0806485cab4c953f9422 ts=2026-09-04T18:03:45.2180000Z == wenyi090326-2.stratalog.logdata.json[5230] _id=6a9b0806485cab4c953f9424 ts=2026-09-04T18:03:45.2180000Z`; `wenyi090326-2.stratalog.logdata.json[5227] _id=6a9b0806485cab4c953f9426 ts=2026-09-04T18:03:45.2860000Z == wenyi090326-2.stratalog.logdata.json[5228] _id=6a9b0806485cab4c953f9428 ts=2026-09-04T18:03:45.2860000Z`; `wenyi090326-2.stratalog.logdata.json[4421] _id=6a9b0b1f485cab4c953f9a66 ts=2026-09-04T18:17:02.7670000Z == wenyi090326-2.stratalog.logdata.json[4426] _id=6a9b0b1f485cab4c953f9a68 ts=2026-09-04T18:17:02.7670000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5836] _id=6a9b14e9485cab4c953fac78 ts=? == wenyi090326-2.stratalog.logdata.json[5835] _id=6a9b16bf485cab4c953faee8 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-2.stratalog.logdata.json[212] _id=6a9b237f485cab4c953fc372 ts=2026-09-04T20:01:03.4260000Z == wenyi090326-2.stratalog.logdata.json[213] _id=6a9b237f485cab4c953fc374 ts=2026-09-04T20:01:03.4260000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi090326-2.stratalog.logdata.json[5766] _id=6a9b0487485cab4c953f86d8 ts=2026-09-04T17:48:55.7920000Z ~ wenyi090326-2.stratalog.logdata.json[5765] _id=6a9b0487485cab4c953f86da ts=2026-09-04T17:48:55.7930000Z`; `700ms: wenyi090326-2.stratalog.logdata.json[1664] _id=6a9b17fa485cab4c953fb26e ts=2026-09-04T19:11:55.1540000Z ~ wenyi090326-2.stratalog.logdata.json[1661] _id=6a9b17fb485cab4c953fb274 ts=2026-09-04T19:11:55.8540000Z`; `834ms: wenyi090326-2.stratalog.logdata.json[326] _id=6a9b2311485cab4c953fc286 ts=2026-09-04T19:59:13.2740000Z ~ wenyi090326-2.stratalog.logdata.json[324] _id=6a9b2311485cab4c953fc28a ts=2026-09-04T19:59:14.1080000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: wenyi090326-2.stratalog.logdata.json[5320] _id=6a9b0801485cab4c953f9388 ts=2026-09-04T18:03:06.4480000Z ~ wenyi090326-2.stratalog.logdata.json[5317] _id=6a9b0801485cab4c953f938a ts=2026-09-04T18:03:06.4500000Z`; `67ms: wenyi090326-2.stratalog.logdata.json[5313] _id=6a9b0801485cab4c953f9398 ts=2026-09-04T18:03:06.7140000Z ~ wenyi090326-2.stratalog.logdata.json[5312] _id=6a9b0801485cab4c953f939a ts=2026-09-04T18:03:06.7810000Z`; `67ms: wenyi090326-2.stratalog.logdata.json[5310] _id=6a9b0802485cab4c953f93a0 ts=2026-09-04T18:03:06.9140000Z ~ wenyi090326-2.stratalog.logdata.json[5309] _id=6a9b0802485cab4c953f93a2 ts=2026-09-04T18:03:06.9810000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `31ms: wenyi090326-2.stratalog.logdata.json[3125] _id=6a9b1132485cab4c953fa6f8 ts=2026-09-04T18:42:58.9450000Z ~ wenyi090326-2.stratalog.logdata.json[3121] _id=6a9b1132485cab4c953fa6fe ts=2026-09-04T18:42:58.9760000Z`; `32ms: wenyi090326-2.stratalog.logdata.json[1223] _id=6a9b1a29485cab4c953fb5e0 ts=2026-09-04T19:21:13.3070000Z ~ wenyi090326-2.stratalog.logdata.json[1219] _id=6a9b1a29485cab4c953fb5e6 ts=2026-09-04T19:21:13.3390000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `31ms: wenyi090326-2.stratalog.logdata.json[5543] _id=6a9b0688485cab4c953f9128 ts=2026-09-04T17:57:28.3050000Z ~ wenyi090326-2.stratalog.logdata.json[5542] _id=6a9b0688485cab4c953f912a ts=2026-09-04T17:57:28.3360000Z`; `801ms: wenyi090326-2.stratalog.logdata.json[5547] _id=6a9b0687485cab4c953f9120 ts=2026-09-04T17:57:27.6360000Z ~ wenyi090326-2.stratalog.logdata.json[5541] _id=6a9b0688485cab4c953f912c ts=2026-09-04T17:57:28.4370000Z`; `233ms: wenyi090326-2.stratalog.logdata.json[3999] _id=6a9b0bb7485cab4c953f9dc8 ts=2026-09-04T18:19:35.7210000Z ~ wenyi090326-2.stratalog.logdata.json[3997] _id=6a9b0bb7485cab4c953f9dcc ts=2026-09-04T18:19:35.9540000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `700ms: wenyi090326-2.stratalog.logdata.json[3616] _id=6a9b0df8485cab4c953fa2a2 ts=2026-09-04T18:29:12.6140000Z ~ wenyi090326-2.stratalog.logdata.json[3615] _id=6a9b0df9485cab4c953fa2a4 ts=2026-09-04T18:29:13.3140000Z`; `667ms: wenyi090326-2.stratalog.logdata.json[3614] _id=6a9b0df9485cab4c953fa2a6 ts=2026-09-04T18:29:14.1810000Z ~ wenyi090326-2.stratalog.logdata.json[3613] _id=6a9b0dfa485cab4c953fa2a8 ts=2026-09-04T18:29:14.8480000Z`; `534ms: wenyi090326-2.stratalog.logdata.json[3161] _id=6a9b10d1485cab4c953fa6b0 ts=2026-09-04T18:41:22.1280000Z ~ wenyi090326-2.stratalog.logdata.json[3160] _id=6a9b10d2485cab4c953fa6b2 ts=2026-09-04T18:41:22.6620000Z`
- **INFO / Info** `chatEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `533ms: wenyi090326-2.stratalog.logdata.json[4031] _id=6a9b0bae485cab4c953f9d88 ts=2026-09-04T18:19:26.4500000Z ~ wenyi090326-2.stratalog.logdata.json[4029] _id=6a9b0bae485cab4c953f9d8c ts=2026-09-04T18:19:26.9830000Z`; `534ms: wenyi090326-2.stratalog.logdata.json[4029] _id=6a9b0bae485cab4c953f9d8c ts=2026-09-04T18:19:26.9830000Z ~ wenyi090326-2.stratalog.logdata.json[4027] _id=6a9b0baf485cab4c953f9d90 ts=2026-09-04T18:19:27.5170000Z`; `534ms: wenyi090326-2.stratalog.logdata.json[4027] _id=6a9b0baf485cab4c953f9d90 ts=2026-09-04T18:19:27.5170000Z ~ wenyi090326-2.stratalog.logdata.json[4025] _id=6a9b0baf485cab4c953f9d94 ts=2026-09-04T18:19:28.0510000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: wenyi090326-2.stratalog.logdata.json[3023] _id=6a9b11f3485cab4c953fa7c6 ts=2026-09-04T18:46:11.6570000Z ~ wenyi090326-2.stratalog.logdata.json[3022] _id=6a9b120b485cab4c953fa7c8 ts=2026-09-04T18:46:11.657Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi090326-2.stratalog.logdata.json[84] _id=6a9b2406485cab4c953fc474 ts=2026-09-04T20:03:18.6310000Z ~ wenyi090326-2.stratalog.logdata.json[82] _id=6a9b2406485cab4c953fc476 ts=2026-09-04T20:03:18.6320000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 25m 57s 
  - Evidence: 25m 57s: wenyi090326-2.stratalog.logdata.json[2112] _id=6a9b16c4485cab4c953faeee ts=2026-09-04T19:06:44.5970000Z -> wenyi090326-2.stratalog.logdata.json[541] _id=6a9b1cd9485cab4c953fbb36 ts=2026-09-04T19:32:41.8050000Z; 19m 47s: wenyi090326-2.stratalog.logdata.json[3010] _id=6a9b121d485cab4c953fa7e2 ts=2026-09-04T18:46:53.1780000Z -> wenyi090326-2.stratalog.logdata.json[2113] _id=6a9b16c0485cab4c953faeec ts=2026-09-04T19:06:40.6060000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 34m 3s 
  - Evidence: 34m 3s: wenyi090326-2.stratalog.logdata.json[3994] _id=6a9b0bba485cab4c953f9dd2 ts=2026-09-04T18:19:38.4220000Z -> wenyi090326-2.stratalog.logdata.json[2543] _id=6a9b13b5485cab4c953fab88 ts=2026-09-04T18:53:41.7330000Z; 33m 56s: wenyi090326-2.stratalog.logdata.json[2390] _id=6a9b15b5485cab4c953facbe ts=2026-09-04T19:02:13.6260000Z -> wenyi090326-2.stratalog.logdata.json[384] _id=6a9b1daa485cab4c953fbc70 ts=2026-09-04T19:36:10.6040000Z; 22m 28s: wenyi090326-2.stratalog.logdata.json[384] _id=6a9b1daa485cab4c953fbc70 ts=2026-09-04T19:36:10.6040000Z -> wenyi090326-2.stratalog.logdata.json[372] _id=6a9b22ee485cab4c953fc1f2 ts=2026-09-04T19:58:38.7620000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: wenyi090326-2.stratalog.logdata.json[2392] _id=6a9b15b2485cab4c953facba ts=2026-09-04T19:02:10.6770000Z -> wenyi090326-2.stratalog.logdata.json[2391] _id=6a9b15b2485cab4c953facbc ts=2026-09-04T19:02:10.6780000Z; 1ms: wenyi090326-2.stratalog.logdata.json[2394] _id=6a9b15a6485cab4c953facb6 ts=2026-09-04T19:01:58.5860000Z -> wenyi090326-2.stratalog.logdata.json[2393] _id=6a9b15a6485cab4c953facb8 ts=2026-09-04T19:01:58.5870000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22m 49s 
  - Evidence: 22m 49s: wenyi090326-2.stratalog.logdata.json[387] _id=6a9b1d9f485cab4c953fbc6a ts=2026-09-04T19:35:59.5000000Z -> wenyi090326-2.stratalog.logdata.json[356] _id=6a9b22f9485cab4c953fc232 ts=2026-09-04T19:58:49.4720000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 477 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-2.stratalog.logdata.json[103] _id=6a9b23df485cab4c953fc44c ts=2026-09-04T20:02:39.9500000Z -> wenyi090326-2.stratalog.logdata.json[104] _id=6a9b23df485cab4c953fc44e ts=2026-09-04T20:02:39.9500000Z; 0ms: wenyi090326-2.stratalog.logdata.json[112] _id=6a9b23d9485cab4c953fc43a ts=2026-09-04T20:02:33.8480000Z -> wenyi090326-2.stratalog.logdata.json[113] _id=6a9b23d9485cab4c953fc43c ts=2026-09-04T20:02:33.8480000Z; 0ms: wenyi090326-2.stratalog.logdata.json[1171] _id=6a9b1a75485cab4c953fb646 ts=2026-09-04T19:22:29.5580000Z -> wenyi090326-2.stratalog.logdata.json[1172] _id=6a9b1a75485cab4c953fb648 ts=2026-09-04T19:22:29.5580000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 37m 1s 
  - Evidence: 37m 1s: wenyi090326-2.stratalog.logdata.json[911] _id=6a9b1b89485cab4c953fb850 ts=2026-09-04T19:27:06.0560000Z -> wenyi090326-2.stratalog.logdata.json[2] _id=6a9b2437485cab4c953fc518 ts=2026-09-04T20:04:07.2210000Z; 31m 39s: wenyi090326-2.stratalog.logdata.json[2443] _id=6a9b141e485cab4c953fac50 ts=2026-09-04T18:55:26.2480000Z -> wenyi090326-2.stratalog.logdata.json[911] _id=6a9b1b89485cab4c953fb850 ts=2026-09-04T19:27:06.0560000Z; 30m 28s: wenyi090326-2.stratalog.logdata.json[5420] _id=6a9b072e485cab4c953f928a ts=2026-09-04T18:00:14.1830000Z -> wenyi090326-2.stratalog.logdata.json[3526] _id=6a9b0e52485cab4c953fa3c4 ts=2026-09-04T18:30:43.1570000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22m 28s 
  - Evidence: 22m 28s: wenyi090326-2.stratalog.logdata.json[383] _id=6a9b1daa485cab4c953fbc72 ts=2026-09-04T19:36:10.6050000Z -> wenyi090326-2.stratalog.logdata.json[370] _id=6a9b22ef485cab4c953fc1f6 ts=2026-09-04T19:58:39.2310000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 47 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: wenyi090326-2.stratalog.logdata.json[1953] _id=6a9b1730485cab4c953fb02c ts=2026-09-04T19:08:32.9250000Z -> wenyi090326-2.stratalog.logdata.json[1952] _id=6a9b1730485cab4c953fb02e ts=2026-09-04T19:08:32.9260000Z; 1ms: wenyi090326-2.stratalog.logdata.json[2066] _id=6a9b16e1485cab4c953faf4a ts=2026-09-04T19:07:13.3520000Z -> wenyi090326-2.stratalog.logdata.json[2065] _id=6a9b16e1485cab4c953faf4c ts=2026-09-04T19:07:13.3530000Z; 1ms: wenyi090326-2.stratalog.logdata.json[2074] _id=6a9b16dd485cab4c953faf3a ts=2026-09-04T19:07:10.1190000Z -> wenyi090326-2.stratalog.logdata.json[2073] _id=6a9b16dd485cab4c953faf3c ts=2026-09-04T19:07:10.1200000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22m 41s 
  - Evidence: 22m 41s: wenyi090326-2.stratalog.logdata.json[388] _id=6a9b1d9d485cab4c953fbc68 ts=2026-09-04T19:35:58.0690000Z -> wenyi090326-2.stratalog.logdata.json[371] _id=6a9b22ef485cab4c953fc1f4 ts=2026-09-04T19:58:39.2300000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi090326-2.stratalog.logdata.json[1319] _id=6a9b1959485cab4c953fb520 ts=2026-09-04T19:17:45.7410000Z -> wenyi090326-2.stratalog.logdata.json[1318] _id=6a9b1959485cab4c953fb522 ts=2026-09-04T19:17:45.7410000Z; 0ms: wenyi090326-2.stratalog.logdata.json[1353] _id=6a9b1934485cab4c953fb4dc ts=2026-09-04T19:17:08.2900000Z -> wenyi090326-2.stratalog.logdata.json[1352] _id=6a9b1934485cab4c953fb4de ts=2026-09-04T19:17:08.2900000Z; 1ms: wenyi090326-2.stratalog.logdata.json[5766] _id=6a9b0487485cab4c953f86d8 ts=2026-09-04T17:48:55.7920000Z -> wenyi090326-2.stratalog.logdata.json[5765] _id=6a9b0487485cab4c953f86da ts=2026-09-04T17:48:55.7930000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22m 38s 
  - Evidence: 22m 38s: wenyi090326-2.stratalog.logdata.json[385] _id=6a9b1daa485cab4c953fbc6e ts=2026-09-04T19:36:10.5700000Z -> wenyi090326-2.stratalog.logdata.json[358] _id=6a9b22f8485cab4c953fc22c ts=2026-09-04T19:58:48.7310000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 27m 49s 
  - Evidence: 27m 49s: wenyi090326-2.stratalog.logdata.json[4046] _id=6a9b0b9b485cab4c953f9d70 ts=2026-09-04T18:19:05.8390000Z -> wenyi090326-2.stratalog.logdata.json[3007] _id=6a9b121f485cab4c953fa7e6 ts=2026-09-04T18:46:54.8390000Z; 16m 20s: wenyi090326-2.stratalog.logdata.json[2877] _id=6a9b1247485cab4c953fa8ec ts=2026-09-04T18:47:35.0890000Z -> wenyi090326-2.stratalog.logdata.json[2325] _id=6a9b161b485cab4c953fad32 ts=2026-09-04T19:03:55.8270000Z; 13m 18s: wenyi090326-2.stratalog.logdata.json[1449] _id=6a9b187e485cab4c953fb41c ts=2026-09-04T19:14:05.8650000Z -> wenyi090326-2.stratalog.logdata.json[898] _id=6a9b1b9c485cab4c953fb85e ts=2026-09-04T19:27:24.2820000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 707 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-2.stratalog.logdata.json[1457] _id=6a9b187d485cab4c953fb40c ts=2026-09-04T19:14:04.5670000Z -> wenyi090326-2.stratalog.logdata.json[1456] _id=6a9b187d485cab4c953fb40e ts=2026-09-04T19:14:04.5670000Z; 0ms: wenyi090326-2.stratalog.logdata.json[1462] _id=6a9b187c485cab4c953fb402 ts=2026-09-04T19:14:04.1990000Z -> wenyi090326-2.stratalog.logdata.json[1461] _id=6a9b187c485cab4c953fb404 ts=2026-09-04T19:14:04.1990000Z; 0ms: wenyi090326-2.stratalog.logdata.json[1463] _id=6a9b187c485cab4c953fb400 ts=2026-09-04T19:14:04.1990000Z -> wenyi090326-2.stratalog.logdata.json[1462] _id=6a9b187c485cab4c953fb402 ts=2026-09-04T19:14:04.1990000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 29m 43s 
  - Evidence: 29m 43s: wenyi090326-2.stratalog.logdata.json[4460] _id=6a9b0ae3485cab4c953f9a0c ts=2026-09-04T18:16:03.1700000Z -> wenyi090326-2.stratalog.logdata.json[3042] _id=6a9b11da485cab4c953fa79e ts=2026-09-04T18:45:46.7230000Z; 17m 36s: wenyi090326-2.stratalog.logdata.json[3029] _id=6a9b11e6485cab4c953fa7b8 ts=2026-09-04T18:45:58.8610000Z -> wenyi090326-2.stratalog.logdata.json[2351] _id=6a9b1606485cab4c953fad0c ts=2026-09-04T19:03:34.9490000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 18m 28s 
  - Evidence: 18m 28s: wenyi090326-2.stratalog.logdata.json[3472] _id=6a9b0f4c485cab4c953fa442 ts=2026-09-04T18:34:52.5940000Z -> wenyi090326-2.stratalog.logdata.json[2561] _id=6a9b13a0485cab4c953fab64 ts=2026-09-04T18:53:21.1560000Z; 10m 29s: wenyi090326-2.stratalog.logdata.json[3865] _id=6a9b0cd6485cab4c953f9f20 ts=2026-09-04T18:24:22.4260000Z -> wenyi090326-2.stratalog.logdata.json[3474] _id=6a9b0f4b485cab4c953fa43e ts=2026-09-04T18:34:51.9260000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.033s shown 
  - Evidence: 4ms: wenyi090326-2.stratalog.logdata.json[4637] _id=6a9b092c485cab4c953f98aa ts=2026-09-04T18:08:45.0610000Z -> wenyi090326-2.stratalog.logdata.json[4633] _id=6a9b092d485cab4c953f98b2 ts=2026-09-04T18:08:45.0650000Z; 30ms: wenyi090326-2.stratalog.logdata.json[4638] _id=6a9b092c485cab4c953f98a8 ts=2026-09-04T18:08:45.0310000Z -> wenyi090326-2.stratalog.logdata.json[4637] _id=6a9b092c485cab4c953f98aa ts=2026-09-04T18:08:45.0610000Z; 33ms: wenyi090326-2.stratalog.logdata.json[4536] _id=6a9b09cb485cab4c953f9974 ts=2026-09-04T18:11:23.6710000Z -> wenyi090326-2.stratalog.logdata.json[4534] _id=6a9b09cb485cab4c953f9978 ts=2026-09-04T18:11:23.7040000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 38m 47s 
  - Evidence: 38m 47s: wenyi090326-2.stratalog.logdata.json[1224] _id=6a9b1a29485cab4c953fb5de ts=2026-09-04T19:21:13.3040000Z -> wenyi090326-2.stratalog.logdata.json[263] _id=6a9b2340485cab4c953fc30e ts=2026-09-04T20:00:00.4630000Z; 38m 14s: wenyi090326-2.stratalog.logdata.json[3126] _id=6a9b1132485cab4c953fa6f6 ts=2026-09-04T18:42:58.9420000Z -> wenyi090326-2.stratalog.logdata.json[1224] _id=6a9b1a29485cab4c953fb5de ts=2026-09-04T19:21:13.3040000Z; 31m 21s: wenyi090326-2.stratalog.logdata.json[5503] _id=6a9b06a8485cab4c953f91e2 ts=2026-09-04T17:58:00.9190000Z -> wenyi090326-2.stratalog.logdata.json[3603] _id=6a9b0e02485cab4c953fa2c4 ts=2026-09-04T18:29:22.7850000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 38m 22s 
  - Evidence: 38m 22s: wenyi090326-2.stratalog.logdata.json[1219] _id=6a9b1a29485cab4c953fb5e6 ts=2026-09-04T19:21:13.3390000Z -> wenyi090326-2.stratalog.logdata.json[293] _id=6a9b2328485cab4c953fc2d0 ts=2026-09-04T19:59:36.1860000Z; 35m 21s: wenyi090326-2.stratalog.logdata.json[3121] _id=6a9b1132485cab4c953fa6fe ts=2026-09-04T18:42:58.9760000Z -> wenyi090326-2.stratalog.logdata.json[1286] _id=6a9b197c485cab4c953fb562 ts=2026-09-04T19:18:20.4210000Z; 30m 29s: wenyi090326-2.stratalog.logdata.json[5502] _id=6a9b06a8485cab4c953f91e4 ts=2026-09-04T17:58:00.9220000Z -> wenyi090326-2.stratalog.logdata.json[3636] _id=6a9b0dce485cab4c953fa228 ts=2026-09-04T18:28:30.3610000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.032s shown 
  - Evidence: 31ms: wenyi090326-2.stratalog.logdata.json[3125] _id=6a9b1132485cab4c953fa6f8 ts=2026-09-04T18:42:58.9450000Z -> wenyi090326-2.stratalog.logdata.json[3121] _id=6a9b1132485cab4c953fa6fe ts=2026-09-04T18:42:58.9760000Z; 32ms: wenyi090326-2.stratalog.logdata.json[1223] _id=6a9b1a29485cab4c953fb5e0 ts=2026-09-04T19:21:13.3070000Z -> wenyi090326-2.stratalog.logdata.json[1219] _id=6a9b1a29485cab4c953fb5e6 ts=2026-09-04T19:21:13.3390000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 38m 29s 
  - Evidence: 38m 29s: wenyi090326-2.stratalog.logdata.json[1226] _id=6a9b1a26485cab4c953fb5da ts=2026-09-04T19:21:10.8690000Z -> wenyi090326-2.stratalog.logdata.json[285] _id=6a9b232b485cab4c953fc2e2 ts=2026-09-04T19:59:39.8870000Z; 35m 28s: wenyi090326-2.stratalog.logdata.json[3130] _id=6a9b112f485cab4c953fa6ee ts=2026-09-04T18:42:55.4060000Z -> wenyi090326-2.stratalog.logdata.json[1282] _id=6a9b197f485cab4c953fb56a ts=2026-09-04T19:18:24.0230000Z; 21m 36s: wenyi090326-2.stratalog.logdata.json[5506] _id=6a9b06a6485cab4c953f91d8 ts=2026-09-04T17:57:59.0850000Z -> wenyi090326-2.stratalog.logdata.json[3999] _id=6a9b0bb7485cab4c953f9dc8 ts=2026-09-04T18:19:35.7210000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 30 interval(s) ≤ 0.031s..0.032s shown 
  - Evidence: 31ms: wenyi090326-2.stratalog.logdata.json[5532] _id=6a9b068d485cab4c953f9166 ts=2026-09-04T17:57:33.2750000Z -> wenyi090326-2.stratalog.logdata.json[5531] _id=6a9b068d485cab4c953f9168 ts=2026-09-04T17:57:33.3060000Z; 31ms: wenyi090326-2.stratalog.logdata.json[5543] _id=6a9b0688485cab4c953f9128 ts=2026-09-04T17:57:28.3050000Z -> wenyi090326-2.stratalog.logdata.json[5542] _id=6a9b0688485cab4c953f912a ts=2026-09-04T17:57:28.3360000Z; 32ms: wenyi090326-2.stratalog.logdata.json[1266] _id=6a9b19c8485cab4c953fb58a ts=2026-09-04T19:19:36.8250000Z -> wenyi090326-2.stratalog.logdata.json[1265] _id=6a9b19c8485cab4c953fb58c ts=2026-09-04T19:19:36.8570000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 1h 16m 
  - Evidence: 1h 16m: wenyi090326-2.stratalog.logdata.json[3127] _id=6a9b1132485cab4c953fa6f4 ts=2026-09-04T18:42:58.4410000Z -> wenyi090326-2.stratalog.logdata.json[290] _id=6a9b2329485cab4c953fc2d6 ts=2026-09-04T19:59:37.2560000Z; 31m 12s: wenyi090326-2.stratalog.logdata.json[5504] _id=6a9b06a8485cab4c953f91dc ts=2026-09-04T17:58:00.4520000Z -> wenyi090326-2.stratalog.logdata.json[3616] _id=6a9b0df8485cab4c953fa2a2 ts=2026-09-04T18:29:12.6140000Z; 12m 5s: wenyi090326-2.stratalog.logdata.json[3613] _id=6a9b0dfa485cab4c953fa2a8 ts=2026-09-04T18:29:14.8480000Z -> wenyi090326-2.stratalog.logdata.json[3163] _id=6a9b10d0485cab4c953fa6ac ts=2026-09-04T18:41:20.7940000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 7m 
  - Evidence: 1h 7m: wenyi090326-2.stratalog.logdata.json[4003] _id=6a9b0bb5485cab4c953f9dc0 ts=2026-09-04T18:19:33.2550000Z -> wenyi090326-2.stratalog.logdata.json[908] _id=6a9b1b97485cab4c953fb858 ts=2026-09-04T19:27:19.2840000Z
- **INFO / Info** `chatEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: wenyi090326-2.stratalog.logdata.json[4017] _id=6a9b0bb1485cab4c953f9da4 ts=2026-09-04T18:19:29.6870000Z -> wenyi090326-2.stratalog.logdata.json[4016] _id=6a9b0bb1485cab4c953f9da6 ts=2026-09-04T18:19:29.6880000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 31m 7s 
  - Evidence: 31m 7s: wenyi090326-2.stratalog.logdata.json[5419] _id=6a9b0777485cab4c953f928e ts=2026-09-04T18:01:27.1580000Z -> wenyi090326-2.stratalog.logdata.json[3524] _id=6a9b0ec2485cab4c953fa3da ts=2026-09-04T18:32:35.1500000Z; 20m 44s: wenyi090326-2.stratalog.logdata.json[2117] _id=6a9b16b7485cab4c953faee2 ts=2026-09-04T19:06:32.2080000Z -> wenyi090326-2.stratalog.logdata.json[909] _id=6a9b1b94485cab4c953fb856 ts=2026-09-04T19:27:16.9830000Z; 14m 2s: wenyi090326-2.stratalog.logdata.json[5833] _id=6a9b042c485cab4c953f8586 ts=2026-09-04T17:47:25.0870000Z -> wenyi090326-2.stratalog.logdata.json[5419] _id=6a9b0777485cab4c953f928e ts=2026-09-04T18:01:27.1580000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 29m 37s 
  - Evidence: 29m 37s: wenyi090326-2.stratalog.logdata.json[4506] _id=6a9b0a90485cab4c953f99b0 ts=2026-09-04T18:14:40.7290000Z -> wenyi090326-2.stratalog.logdata.json[3081] _id=6a9b1182485cab4c953fa750 ts=2026-09-04T18:44:18.5230000Z; 24m 22s: wenyi090326-2.stratalog.logdata.json[2121] _id=6a9b168d485cab4c953faed8 ts=2026-09-04T19:05:49.2440000Z -> wenyi090326-2.stratalog.logdata.json[693] _id=6a9b1c43485cab4c953fba06 ts=2026-09-04T19:30:11.9480000Z; 19m 22s: wenyi090326-2.stratalog.logdata.json[5598] _id=6a9b0605485cab4c953f8f8a ts=2026-09-04T17:55:17.9300000Z -> wenyi090326-2.stratalog.logdata.json[4506] _id=6a9b0a90485cab4c953f99b0 ts=2026-09-04T18:14:40.7290000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 31m 55s 
  - Evidence: 31m 55s: wenyi090326-2.stratalog.logdata.json[4526] _id=6a9b09f6485cab4c953f9988 ts=2026-09-04T18:12:06.3390000Z -> wenyi090326-2.stratalog.logdata.json[3083] _id=6a9b1171485cab4c953fa74c ts=2026-09-04T18:44:01.7760000Z; 24m 33s: wenyi090326-2.stratalog.logdata.json[2123] _id=6a9b166d485cab4c953faed4 ts=2026-09-04T19:05:17.2600000Z -> wenyi090326-2.stratalog.logdata.json[696] _id=6a9b1c2e485cab4c953fba00 ts=2026-09-04T19:29:51.0870000Z; 17m 52s: wenyi090326-2.stratalog.logdata.json[374] _id=6a9b1f1a485cab4c953fbe00 ts=2026-09-04T19:42:19.1540000Z -> wenyi090326-2.stratalog.logdata.json[253] _id=6a9b234b485cab4c953fc322 ts=2026-09-04T20:00:12.0990000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-2.stratalog.logdata.json[3023] _id=6a9b11f3485cab4c953fa7c6 ts=2026-09-04T18:46:11.6570000Z -> wenyi090326-2.stratalog.logdata.json[3022] _id=6a9b120b485cab4c953fa7c8 ts=2026-09-04T18:46:11.657Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 24m 58s 
  - Evidence: 24m 58s: wenyi090326-2.stratalog.logdata.json[424] _id=6a9b1d6e485cab4c953fbc20 ts=2026-09-04T19:35:10.4140000Z -> wenyi090326-2.stratalog.logdata.json[256] _id=6a9b2348485cab4c953fc31a ts=2026-09-04T20:00:08.8020000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi090326-2.stratalog.logdata.json[212] _id=6a9b237f485cab4c953fc372 ts=2026-09-04T20:01:03.4260000Z -> wenyi090326-2.stratalog.logdata.json[213] _id=6a9b237f485cab4c953fc374 ts=2026-09-04T20:01:03.4260000Z; 1ms: wenyi090326-2.stratalog.logdata.json[1654] _id=6a9b1800485cab4c953fb282 ts=2026-09-04T19:12:00.5240000Z -> wenyi090326-2.stratalog.logdata.json[1653] _id=6a9b1800485cab4c953fb284 ts=2026-09-04T19:12:00.5250000Z; 1ms: wenyi090326-2.stratalog.logdata.json[1767] _id=6a9b17b6485cab4c953fb1a0 ts=2026-09-04T19:10:46.4550000Z -> wenyi090326-2.stratalog.logdata.json[1766] _id=6a9b17b6485cab4c953fb1a2 ts=2026-09-04T19:10:46.4560000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5575] _id=6a9b066a485cab4c953f9006 ts=2026-09-04T17:56:58.7240000Z`; `wenyi090326-2.stratalog.logdata.json[5495] _id=6a9b06ad485cab4c953f91f2 ts=2026-09-04T17:58:05.7930000Z`; `wenyi090326-2.stratalog.logdata.json[4524] _id=6a9b09f9485cab4c953f998c ts=2026-09-04T18:12:10.0260000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5124] _id=6a9b0810485cab4c953f94e0 ts=2026-09-04T18:03:59.2570000Z`; `wenyi090326-2.stratalog.logdata.json[5064] _id=6a9b0817485cab4c953f9558 ts=2026-09-04T18:04:07.2610000Z`; `wenyi090326-2.stratalog.logdata.json[4838] _id=6a9b083a485cab4c953f9726 ts=2026-09-04T18:04:39.9440000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5316] _id=6a9b0801485cab4c953f938e ts=2026-09-04T18:03:06.5470000Z`; `wenyi090326-2.stratalog.logdata.json[5312] _id=6a9b0801485cab4c953f939a ts=2026-09-04T18:03:06.7810000Z`; `wenyi090326-2.stratalog.logdata.json[5214] _id=6a9b0807485cab4c953f943c ts=2026-09-04T18:03:46.1840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi090326-2.stratalog.logdata.json[3121] _id=6a9b1132485cab4c953fa6fe ts=2026-09-04T18:42:58.9760000Z`; `wenyi090326-2.stratalog.logdata.json[1219] _id=6a9b1a29485cab4c953fb5e6 ts=2026-09-04T19:21:13.3390000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5542] _id=6a9b0688485cab4c953f912a ts=2026-09-04T17:57:28.3360000Z`; `wenyi090326-2.stratalog.logdata.json[3628] _id=6a9b0dec485cab4c953fa27a ts=2026-09-04T18:29:00.3740000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `wenyi090326-2.stratalog.logdata.json[908] _id=6a9b1b97485cab4c953fb858 ts=2026-09-04T19:27:19.2840000Z`; `wenyi090326-2.stratalog.logdata.json[449] _id=6a9b1d49485cab4c953fbbee ts=2026-09-04T19:34:33.8270000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `wenyi090326-2.stratalog.logdata.json[3014] _id=6a9b121c485cab4c953fa7da ts=2026-09-04T18:46:53.1600000Z`; `wenyi090326-2.stratalog.logdata.json[2012] _id=6a9b170a485cab4c953fafb6 ts=2026-09-04T19:07:54.8730000Z`; `wenyi090326-2.stratalog.logdata.json[539] _id=6a9b1cda485cab4c953fbb3a ts=2026-09-04T19:32:43.1240000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5834] _id=6a9b11eb485cab4c953fa7c4 ts=?`; `wenyi090326-2.stratalog.logdata.json[5836] _id=6a9b14e9485cab4c953fac78 ts=?`; `wenyi090326-2.stratalog.logdata.json[5835] _id=6a9b16bf485cab4c953faee8 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 32 occurrence(s) 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5200] _id=6a9b0808485cab4c953f9452 ts=2026-09-04T18:03:49.7210000Z`; `wenyi090326-2.stratalog.logdata.json[5122] _id=6a9b0810485cab4c953f94e4 ts=2026-09-04T18:03:59.4910000Z`; `wenyi090326-2.stratalog.logdata.json[5121] _id=6a9b0810485cab4c953f94e6 ts=2026-09-04T18:03:59.7570000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 90 occurrence(s) 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5317] _id=6a9b0801485cab4c953f938a ts=2026-09-04T18:03:06.4500000Z`; `wenyi090326-2.stratalog.logdata.json[5309] _id=6a9b0802485cab4c953f93a2 ts=2026-09-04T18:03:06.9810000Z`; `wenyi090326-2.stratalog.logdata.json[5289] _id=6a9b0802485cab4c953f93a6 ts=2026-09-04T18:03:36.1970000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5505] _id=6a9b06a7485cab4c953f91da ts=2026-09-04T17:57:59.9180000Z`; `wenyi090326-2.stratalog.logdata.json[3615] _id=6a9b0df9485cab4c953fa2a4 ts=2026-09-04T18:29:13.3140000Z`; `wenyi090326-2.stratalog.logdata.json[3613] _id=6a9b0dfa485cab4c953fa2a8 ts=2026-09-04T18:29:14.8480000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 312 start, 308 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'BecameCameraCentered' (totals: 241 open, 242 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 23 unmatched 'BecameVisible' (totals: 357 open, 342 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 13 unmatched 'argumentationToolOpen' (totals: 16 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 8 unmatched 'questActiveEvent' (totals: 37 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 160 of 5833 adjacent _id pairs reverse in client time; worst 39.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi090326-2.stratalog.logdata.json[5223] _id=6a9b0801485cab4c953f9394 ts=2026-09-04T18:03:45.7520000Z`; `wenyi090326-2.stratalog.logdata.json[5314] _id=6a9b0801485cab4c953f9396 ts=2026-09-04T18:03:06.6480000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.17s, min -39.21s, max +0.24s over 5834 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-03-26-2.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Single full playthrough by one tester on 2026-09-04 (log shows EndOfUnit for units 1-5).; Debug menu opened briefly (DebugMenuStateChanged open/close toggles in Unit 3, Unit 4, and Unit 5 dungeon; no debug actions logged). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1737 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (490); Unit 3 Dev (265); Unit 4 Dev (241); Unit 5 Dev (222); Unit 1 Dev (187); Unit 3 Dungeon Dev (115); Unit 4 Dev - Dungeon (86); Unit 4 Dev - Anderson Base (71); Unit 5 Dev - Dungeon (60)
- **eventKey:** present on 1117 of 1737 records
- **Intervals:** median 0.67s (p5 0.00s / p95 16.89s, n=1736)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1117; [conversationId, dialogueEventType] x620
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1737/1737 records)
    numeric range 8 .. 118 (52 unique)
data.dialogueEventType  (string, 1737/1737 records)
    "DialogueNodeEvent"  x1117
    "DialogueStartEvent"  x312
    "DialogueFinishEvent"  x308
data.nodeId  (number, 1117/1737 records)
    numeric range 0 .. 290 (216 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `InputEvent` — 1630 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (369); Unit 2 Prod (Refactor) (351); Unit 3 Dev (222); Unit 4 Dev (160); Unit 5 Dev - Dungeon (159); Unit 3 Dungeon Dev (147); Unit 5 Dev (110); Unit 1 Dev (82); Unit 4 Dev - Anderson Base (30)
- **Intervals:** median 0.56s (p5 0.07s / p95 14.48s, n=1629)
- **Fields under `data`:**

```text
data.Value  (string, 1630/1630 records)
    "pressed"  x1630
data.actionType  (string, 1630/1630 records)
    "Move"  x1191
    "Interact"  x241
    "Sprint"  x127
    "Ascend"  x28
    "Hoverboard"  x12
    "Descend"  x11
    "Jump"  x8
    "Map"  x7
    "ToggleDebug"  x3
    "Pause"  x2
data.key  (string, 1630/1630 records, 2 empty-string)
    13 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1630/1630 records)
    "Player"  x1390
    "Drone"  x240
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 1182 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (720); Unit 4 Dev (202); Unit 5 Dev - Dungeon (170); Unit 3 Dungeon Dev (90)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.04s, n=1181)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1182/1182 records)
    "BecameVisible"  x357
    "BecameInvisible"  x342
    "BecameCameraUncentered"  x242
    "BecameCameraCentered"  x241
data.pieceId  (string, 1182/1182 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1182/1182 records)
    780 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 638 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (171); Unit 3 Dev (99); Unit 4 Dev (93); Unit 1 Dev (77); Unit 4 Dev - Dungeon (47); Unit 5 Dev - Dungeon (43); Unit 5 Dev (40); Unit 3 Dungeon Dev (34); Unit 4 Dev - Anderson Base (34)
- **Intervals:** median 10.01s (p5 9.97s / p95 10.16s, n=624)
- **Fields under `data`:**

```text
data.position  (object, 638/638 records)
data.position.x  (number, 638/638 records)
    numeric range -682.078 .. 1560.37 (291 unique)
data.position.y  (number, 638/638 records)
    numeric range -112.491 .. 222.005 (250 unique)
data.position.z  (number, 638/638 records)
    numeric range -1029.5 .. 1808.96 (291 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 178 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (58); Unit 2 Prod (Refactor) (31); Unit 3 Dungeon Dev (24); Unit 4 Dev (18); Unit 5 Dev (14); Unit 1 Dev (11); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 6.47s (p5 1.21s / p95 203.36s, n=177)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 178/178 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 178/178 records)
    102 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 133 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (41); Unit 1 Dev (26); Unit 2 Prod (Refactor) (25); Unit 3 Dev (21); Unit 5 Dev (20)
- **Intervals:** median 0.38s (p5 0.03s / p95 34.57s, n=132)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 133/133 records)
    "argumentationNodeHoverEnd"  x58
    "argumentationNodeHoverStart"  x56
    "argumentationNodeAdd"  x19
data.argumentationTitle  (string, 133/133 records)
    "Unit 4 - Flooding"  x41
    "Unit 2 – Watershed"  x25
    "Unit 3 - Pollution Upstream"  x21
    "Unit 5"  x20
    "Unit 1 - Argumentation Tutorial"  x15
    "Unit 1 - Freshwater"  x11
data.nodeName  (string, 133/133 records)
    "1"  x23
    "A"  x21
    "I"  x17
    "II"  x15
    "B"  x12
    "3"  x9
    "4"  x8
    "C"  x8
    "D"  x8
    "2"  x7
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 69 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (12); Unit 3 Dev (11); Unit 4 Dev (9); Unit 4 Dev - Dungeon (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (6); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 69 of 69 records
- **Intervals:** median 74.64s (p5 0.00s / p95 361.68s, n=68)
- **`data` key-set variants:** [questEventType, questID, questName] x37; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 69/69 records)
    "questActiveEvent"  x37
    "questFinishEvent"  x32
data.questID  (string, 69/69 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 69/69 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/69 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 44 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (36); Unit 3 Dev (8)
- **Intervals:** median 2.20s (p5 0.03s / p95 453.25s, n=43)
- **`data` key-set variants:** [actionType, featureUsed] x26; [actionType, featureUsed, location] x15; [actionType, featureUsed, legendName] x3
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "MapCloseEvent"  x13
    "MapOpenEvent"  x13
    "WaypointMoveEvent"  x10
    "WaypointSetEvent"  x3
    "Selected"  x2
    "WaypointResetEvent"  x2
    "Unselected"  x1
data.featureUsed  (string, 44/44 records)
    "Map"  x26
    "Waypoint"  x15
    "Legend"  x3
data.legendName  (string, 3/44 records)
    "0 ft"  x2
    "90 ft"  x1
data.location  (object, 15/44 records)
data.location.x  (number, 15/44 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 15/44 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 15/44 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 36 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (12); Unit 4 Dev (12)
- **Intervals:** median 0.67s (p5 0.32s / p95 734.70s, n=35)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x28; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/36 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/36 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 28/36 records)
    "RightDrag"  x17
    "LeftDrag"  x11
data.currentSoilType  (string, 28/36 records)
    "SAND"  x6
    "CLAY"  x5
    "CLAYSAND"  x5
    "SANDGRAVEL"  x5
    "CLAYROCK"  x4
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 28/36 records)
    "false"  x22
    "true"  x6
data.waterLevelStatus  (string, 28/36 records)
    "TooHigh"  x12
    "Proper"  x9
    "TooLow"  x7
data.waterRetentionChange  (string, 28/36 records)
    "Decrease"  x13
    "Increase"  x9
    "NoChange"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `chatEvent` — 32 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (30); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 0.23s (p5 0.12s / p95 217.84s, n=31)
- **`data` key-set variants:** [actionType, chatID] x18; [actionKey, chatID] x14
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 14/32 records)
    "ScrollStop"  x14
data.actionType  (string, 18/32 records)
    "ScrollStart"  x14
    "Close"  x3
    "Open"  x1
data.chatID  (string, 32/32 records)
    15 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `gameWindowUnfocusEvent` — 27 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 5 Dev (11); Unit 4 Dev (6); Unit 1 Dev (3); Unit 3 Dev (3); Unit 5 Dev - Dungeon (2); Unit 2 Prod (Refactor) (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 107.56s (p5 3.04s / p95 1373.61s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    false  x27
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameWindowFocusEvent` — 26 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 5 Dev (11); Unit 4 Dev (6); Unit 1 Dev (3); Unit 3 Dev (2); Unit 5 Dev - Dungeon (2); Unit 2 Prod (Refactor) (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 95.13s (p5 6.59s / p95 1402.72s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationToolEvent` — 19 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (6); Unit 1 Dev (5); Unit 2 Prod (Refactor) (4); Unit 5 Dev (4)
- **Intervals:** median 0.90s (p5 0.50s / p95 2281.16s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "argumentationToolOpen"  x16
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 19/19 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 2 – Watershed"  x4
    "Unit 5"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 19/19 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 16 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev (6); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 2.37s (p5 0.00s / p95 2038.88s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "Close"  x8
    "Open"  x8
data.toolName  (string, 16/16 records, 14 empty-string)
    ""  x14
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 52.43s (p5 0.03s / p95 2194.01s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `WaterChamberEvent` — 12 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (12)
- **Intervals:** median 13.04s (p5 1.62s / p95 40.43s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "On"  x10
    "Off"  x2
data.floor  (string, 12/12 records)
    "4"  x7
    "2"  x3
    "1"  x2
data.machineNumber  (string, 12/12 records)
    "One"  x12
data.machineType  (string, 12/12 records)
    "Evaporator"  x6
    "Condenser"  x5
    "VentSwitch"  x1
data.room  (string, 12/12 records)
    "3"  x6
    "2"  x4
    "1"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 8.00s (p5 1.20s / p95 22.72s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x4
data.boxId  (string, 8/8 records)
    "1"  x4
    "0"  x2
    "2"  x2
data.soilType  (string, 8/8 records)
    "Clay"  x4
    "Sand"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameStartEvent` — 7 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (7)
- **Intervals:** median 841.53s (p5 566.88s / p95 1712.19s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 7/7 records)
    true  x7
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DEBUGMenu` — 6 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 3 Dev (2); Unit 4 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 7.86s (p5 3.83s / p95 1483.25s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "DebugMenuStateChanged"  x6
data.isOpened  (bool, 6/6 records)
    false  x3
    true  x3
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 6 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 1881.87s (p5 183.80s / p95 2320.60s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "submitAnswerEvent"  x6
data.answerSubmitted  (string, 6/6 records)
    "A,1,I"  x2
    "A,1,II"  x1
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "C,D,3,II"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
    "Unit 4 - Flooding"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1864.39s (p5 1534.97s / p95 2172.96s, n=4)
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

### `soilMachine` — 5 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (5)
- **Intervals:** median 42.84s (p5 12.42s / p95 66.45s, n=4)
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "ChangeCanister"  x5
data.canisterType  (string, 5/5 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 5/5 records)
    "5"  x3
    "3"  x1
    "4"  x1
data.machine  (string, 5/5 records)
    "1"  x4
    "2"  x1
data.row  (string, 5/5 records)
    "TopRow"  x4
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 1.07s (p5 0.68s / p95 1.13s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted Out"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Cold"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Uncaught RuntimeError: memory access out of bounds"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 2 empty-string)
    ""  x2
    "RuntimeError: memory access out of bounds
    at wasm://wasm/0a8f363e:wasm-function[73291]:0x1563591
    at wasm://wasm/0a8f363e:wasm-function[73290]:0x15634d3
    at wasm://wasm/0a8f363e:wasm-function[59956]:0x11d11ac
    at wasm://wasm/0a8f363e:wasm-function[59957]:0x11d11f3
    at wasm://wasm/0a8f363e:wasm-function[80769]:0x16e045b
    at wasm://wasm/0a8f363e:wasm-function[83409]:0x1717ed2
    at wasm://wasm/0a8f363e:wasm-function[110254]:0x259781d
    at invoke_iiii (blob:https://dev.adroit.games/006cbe9d-0cce-4f43-9484-1fa69cb6c740:9:474038)
    at wasm://wasm/0a8f363e:wasm-function[83394]:0x1717572
    at wasm://wasm/0a8f363e:wasm-function[1942]:0xf57d9
    at wasm://wasm/0a8f363e:wasm-function[109911]:0x255e832
    at wasm://wasm/0a8f363e:wasm-function[106216]:0x24af5b6
    at wasm://wasm/0a8f363e:wasm-function[87318]:0x190fbf2
    at wasm://wasm/0a8f363e:wasm-function[102624]:0x2291c25
    at wasm://wasm/0a8f363e:wasm-function[105694]:0x245a569
    at wasm://wasm/0a8f363e:wasm-function[105709]:0x245ab0e
    at wasm://wasm/0a8f363e:wasm-function[104647]:0x23edaa7
    at wasm://wasm/0a8f363e:wasm-function[103118]:0x22d15fa
    at wasm://wasm/0a8f363e:wasm-function[86343]:0x18ae5bb
    at wasm://wasm/0a8f363e:wasm-function[103047]:0x22c2f96
    at wasm://wasm/0a8f363e:wasm-function[108883]:0x24f4871
    at wasm://wasm/0a8f363e:wasm-function[3934]:0x15e018
    at wasm://wasm/0a8f363e:wasm-function[110265]:0x25978c4
    at invoke_viiii (blob:https://dev.adroit.games/006cbe9d-0cce-4f43-9484-1fa69cb6c740:9:474821)
    at wasm://wasm/0a8f363e:wasm-function[30556]:0x8ef73a
    at wasm://wasm/0a8f363e:wasm-function[110258]:0x2597858
    at invoke_viii (blob:https://dev.adroit.games/006cbe9d-0cce-4f43-9484-1fa69cb6c740:9:474188)
    at wasm://wasm/0a8f363e:wasm-function[30543]:0x8e931b
    at wasm://wasm/0a8f363e:wasm-function[110258]:0x2597858
    at invoke_viii (blob:https://dev.adroit.games/006cbe9d-0cce-4f43-9484-1fa69cb6c740:9:474188)
    at wasm://wasm/0a8f363e:wasm-function[30537]:0x8e66c3
    at wasm://wasm/0a8f363e:wasm-function[3753]:0x15846a
    at wasm://wasm/0a8f363e:wasm-function[110265]:0x25978c4
    at invoke_viiii (blob:https://dev.adroit.games/006cbe9d-0cce-4f43-9484-1fa69cb6c740:9:474821)
    at wasm://wasm/0a8f363e:wasm-function[3789]:0x159d6b
    at wasm://wasm/0a8f363e:wasm-function[82090]:0x16fd557
    at wasm://wasm/0a8f363e:wasm-function[83409]:0x1717ed2
    at wasm://wasm/0a8f363e:wasm-function[110254]:0x259781d
    at invoke_iiii (blob:https://dev.adroit.games/006cbe9d-0cce-4f43-9484-1fa69cb6c740:9:474038)
    at wasm://wasm/0a8f363e:wasm-function[83394]:0x1717572
    at wasm://wasm/0a8f363e:wasm-function[1942]:0xf57d9
    at wasm://wasm/0a8f363e:wasm-function[109911]:0x255e832
    at wasm://wasm/0a8f363e:wasm-function[106216]:0x24af5b6
    at wasm://wasm/0a8f363e:wasm-function[106219]:0x24af67c
    at wasm://wasm/0a8f363e:wasm-function[84651]:0x1792b0b
    at wasm://wasm/0a8f363e:wasm-function[85941]:0x185d320
    at wasm://wasm/0a8f363e:wasm-function[103890]:0x234f7d5
    at wasm://wasm/0a8f363e:wasm-function[105636]:0x2457674
    at wasm://wasm/0a8f363e:wasm-function[105636]:0x24576e9
    at wasm://wasm/0a8f363e:wasm-function[109989]:0x2566c65"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x2
    "runtime_error"  x1
data.unitId  (string, 3/3 records)
    "unit4"  x2
    "unit3"  x1
data.workspace  (string, 3/3 records)
    "dev"  x3
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\08-31-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DaniEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TerasGardenBox` : baseline field(s) absent this build
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "Unselected" (1x); "WaypointMoveEvent" (10x); "WaypointResetEvent" (2x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (3x); "Waypoint" (15x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*