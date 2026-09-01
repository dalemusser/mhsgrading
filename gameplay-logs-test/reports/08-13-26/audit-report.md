# MHS Gameplay Log Audit Report — build 08-13-26

## 1. Build Information

- **Build ID:** 08-13-26
- **Game version string(s) in log:** 20260812-12180
- **Audit date:** 2026-08-26
- **Log file(s):** wenyi081326-1.stratalog.logdata.json
- **Records:** 4467 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6a7ccbfbd35a78a5b38a5963
- **Time span:** 2026-08-13T15:29:38.853000+00:00 .. 2026-08-13T17:21:34.561000+00:00 (1h 51m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\gameplay-logs-test\config\coverage\08-13-26.yaml
- **Baseline:** none supplied

## 2. Executive Summary

- **22 event types**, 4467 records, 11 scenes.
- Findings: **0 FAIL**, **18 WARNING**, 49 INFO, 0 NOT_TESTED, 105 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DialogueEvent`: eventKey does not match its documented format
  - WARNING/Medium `DaniEvent`: tool open/close: close without preceding open
  - WARNING/Medium `DialogueEvent`: dialogue lifecycle: finish without preceding start
  - WARNING/Medium `PuzzlePieceVisibleEvent`: piece visibility: close without preceding open
  - WARNING/Medium `argumentationEvent`: argumentation session: close without preceding open
  - WARNING/Medium `argumentationNodeEvent`: node hover: close without preceding open
  - WARNING/Medium `questEvent`: quest lifecycle: finish without preceding start

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1615 | 36.15 | 1 | 9 | 0 | 2026-08-13T15:31:55.585000+00:00 | 2026-08-13T17:21:34.561000+00:00 | 1h 49m |
| DialogueEvent | 1347 | 30.15 | 1 | 9 | 836 | 2026-08-13T15:30:02.355000+00:00 | 2026-08-13T17:21:28.957000+00:00 | 1h 51m |
| PlayerPositionEvent | 578 | 12.94 | 1 | 9 | 0 | 2026-08-13T15:29:44.783000+00:00 | 2026-08-13T17:21:25.688000+00:00 | 1h 51m |
| PuzzlePieceVisibleEvent | 346 | 7.75 | 1 | 3 | 0 | 2026-08-13T15:49:44.911000+00:00 | 2026-08-13T16:38:28.324000+00:00 | 48m 43s |
| argumentationNodeEvent | 154 | 3.45 | 1 | 5 | 0 | 2026-08-13T15:40:26.337000+00:00 | 2026-08-13T17:12:41.390000+00:00 | 1h 32m |
| DaniEvent | 91 | 2.04 | 1 | 9 | 0 | 2026-08-13T15:29:44.740000+00:00 | 2026-08-13T17:12:45.878000+00:00 | 1h 43m |
| ObjectInterEvent | 59 | 1.32 | 1 | 7 | 0 | 2026-08-13T15:32:18.646000+00:00 | 2026-08-13T17:06:29.449000+00:00 | 1h 34m |
| questEvent | 56 | 1.25 | 1 | 9 | 56 | 2026-08-13T15:30:02.351000+00:00 | 2026-08-13T17:19:35.203000+00:00 | 1h 49m |
| chatEvent | 32 | 0.72 | 1 | 2 | 0 | 2026-08-13T15:44:15.812000+00:00 | 2026-08-13T17:02:44.910000+00:00 | 1h 18m |
| TopographicMapEvent | 31 | 0.69 | 1 | 2 | 0 | 2026-08-13T15:43:26.071000+00:00 | 2026-08-13T16:20:14.212000+00:00 | 36m 48s |
| gameWindowUnfocusEvent | 31 | 0.69 | 1 | 9 | 0 | 2026-08-13T15:29:54.228000+00:00 | 2026-08-13T16:59:17.885000+00:00 | 1h 29m |
| gameWindowFocusEvent | 29 | 0.65 | 1 | 8 | 0 | 2026-08-13T15:30:13.387000+00:00 | 2026-08-13T16:59:45.307000+00:00 | 1h 29m |
| Soil Key Puzzle | 26 | 0.58 | 1 | 2 | 0 | 2026-08-13T16:07:21.052000+00:00 | 2026-08-13T16:28:52.222000+00:00 | 21m 31s |
| WaterChamberEvent | 21 | 0.47 | 1 | 1 | 0 | 2026-08-13T17:00:12.192000+00:00 | 2026-08-13T17:08:23.770000+00:00 | 8m 11s |
| argumentationToolEvent | 14 | 0.31 | 1 | 3 | 0 | 2026-08-13T15:40:22.468000+00:00 | 2026-08-13T17:12:45.809000+00:00 | 1h 32m |
| argumentationEvent | 12 | 0.27 | 1 | 4 | 0 | 2026-08-13T15:40:23.902000+00:00 | 2026-08-13T17:12:45.882000+00:00 | 1h 32m |
| TerasGardenBox | 6 | 0.13 | 1 | 1 | 0 | 2026-08-13T16:46:09.074000+00:00 | 2026-08-13T16:46:45.408000+00:00 | 36.3s |
| argumentationAnswerEvent | 5 | 0.11 | 1 | 4 | 0 | 2026-08-13T15:40:37.808000+00:00 | 2026-08-13T17:12:45.876000+00:00 | 1h 32m |
| gameStartEvent | 5 | 0.11 | 1 | 1 | 0 | 2026-08-13T15:29:38.853000+00:00 | 2026-08-13T16:55:31.496000+00:00 | 1h 25m |
| soilMachine | 5 | 0.11 | 1 | 1 | 0 | 2026-08-13T16:34:31.880000+00:00 | 2026-08-13T16:37:05.969000+00:00 | 2m 34s |
| DEBUGMenu | 2 | 0.04 | 1 | 1 | 0 | 2026-08-13T16:29:59.087000+00:00 | 2026-08-13T16:30:01.095000+00:00 | 2.0s |
| EndOfUnit | 2 | 0.04 | 1 | 2 | 0 | 2026-08-13T16:52:49.463000+00:00 | 2026-08-13T17:21:34.559000+00:00 | 28m 45s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

No baseline supplied — regression analysis skipped. Pass `--baseline <previous report folder>` to enable it.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 16 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4338] _id=6a7de43e485cab4c9538a0a1 ts=2026-08-13T15:35:26.3340000Z`; `wenyi081326-1.stratalog.logdata.json[4302] _id=6a7de4a3485cab4c9538a0e9 ts=2026-08-13T15:37:07.9470000Z`; `wenyi081326-1.stratalog.logdata.json[4274] _id=6a7de4b6485cab4c9538a121 ts=2026-08-13T15:37:26.9390000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 5 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 5} 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4466] _id=6a7de2e2485cab4c95389fa1 ts=2026-08-13T15:29:38.8530000Z`; `wenyi081326-1.stratalog.logdata.json[3996] _id=6a7de744485cab4c9538a34f ts=2026-08-13T15:48:20.6260000Z`; `wenyi081326-1.stratalog.logdata.json[3870] _id=6a7de84b485cab4c9538a44d ts=2026-08-13T15:52:43.3130000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 29 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 29} 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4456] _id=6a7de305485cab4c95389fb5 ts=2026-08-13T15:30:13.3870000Z`; `wenyi081326-1.stratalog.logdata.json[4451] _id=6a7de313485cab4c95389fbf ts=2026-08-13T15:30:27.5020000Z`; `wenyi081326-1.stratalog.logdata.json[4444] _id=6a7de338485cab4c95389fcd ts=2026-08-13T15:31:04.7700000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 31 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 31} 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4462] _id=6a7de2f2485cab4c95389fa9 ts=2026-08-13T15:29:54.2280000Z`; `wenyi081326-1.stratalog.logdata.json[4454] _id=6a7de306485cab4c95389fb9 ts=2026-08-13T15:30:14.9490000Z`; `wenyi081326-1.stratalog.logdata.json[4448] _id=6a7de31a485cab4c95389fc5 ts=2026-08-13T15:30:34.2170000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1614 | 0.016 | 0.567 | 4.076 | 11.307 | 292.835 | 14.72 | 68 | 0 |
| DialogueEvent | 1346 | 0.0 | 0.734 | 4.968 | 17.732 | 424.498 | 12.08 | 378 | 0 |
| PlayerPositionEvent | 566 | 9.966 | 10.005 | 10.944 | 10.006 | 301.357 | 5.48 | 0 | 0 |
| PuzzlePieceVisibleEvent | 345 | 0.0 | 0.031 | 8.474 | 1.711 | 1094.53 | 7.08 | 231 | 2 |
| argumentationNodeEvent | 153 | 0.014 | 0.351 | 36.177 | 14.113 | 1353.927 | 1.66 | 42 | 4 |
| DaniEvent | 90 | 0.0 | 1.859 | 68.679 | 435.647 | 1085.599 | 0.87 | 38 | 2 |
| ObjectInterEvent | 58 | 0.001 | 11.372 | 97.428 | 592.806 | 1425.888 | 0.62 | 1 | 3 |
| questEvent | 55 | 0.0 | 81.187 | 119.506 | 364.632 | 496.768 | 0.5 | 13 | 0 |
| chatEvent | 31 | 0.197 | 0.419 | 151.906 | 73.824 | 4547.011 | 0.39 | 0 | 1 |
| TopographicMapEvent | 30 | 0.55 | 2.55 | 73.605 | 340.568 | 1305.975 | 0.82 | 0 | 1 |
| gameWindowUnfocusEvent | 30 | 1.835 | 150.154 | 178.789 | 408.93 | 447.762 | 0.34 | 0 | 0 |
| gameWindowFocusEvent | 28 | 0.609 | 142.327 | 191.854 | 419.674 | 796.955 | 0.31 | 0 | 1 |
| Soil Key Puzzle | 25 | 0.15 | 0.466 | 51.647 | 6.593 | 1264.008 | 1.16 | 0 | 1 |
| WaterChamberEvent | 20 | 3.151 | 12.197 | 24.579 | 55.303 | 134.38 | 2.44 | 0 | 0 |
| argumentationToolEvent | 13 | 0.984 | 9.02 | 426.411 | 2409.7 | 4012.117 | 0.14 | 0 | 2 |
| argumentationEvent | 11 | 0.014 | 64.132 | 503.816 | 1971.918 | 2274.598 | 0.12 | 2 | 3 |
| TerasGardenBox | 5 | 0.968 | 3.267 | 7.267 | 17.031 | 18.192 | 8.26 | 0 | 0 |
| argumentationAnswerEvent | 4 | 26.712 | 1581.306 | 1382.017 | 2249.303 | 2338.744 | 0.04 | 0 | 3 |
| gameStartEvent | 4 | 262.687 | 1489.678 | 1288.161 | 1902.647 | 1910.6 | 0.05 | 0 | 3 |
| soilMachine | 4 | 19.743 | 35.166 | 38.522 | 61.975 | 64.013 | 1.56 | 0 | 0 |
| DEBUGMenu | 1 | 2.008 | 2.008 | 2.008 | 2.008 | 2.008 | 29.88 | 0 | 0 |
| EndOfUnit | 1 | 1725.096 | 1725.096 | 1725.096 | 1725.096 | 1725.096 | 0.03 | 0 | 1 |

- **WARNING / Medium** `DaniEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4029] _id=6a7de64b485cab4c9538a309 ts=2026-08-13T15:44:11.2750000Z == wenyi081326-1.stratalog.logdata.json[4030] _id=6a7de64b485cab4c9538a30b ts=2026-08-13T15:44:11.2750000Z`; `wenyi081326-1.stratalog.logdata.json[3994] _id=6a7de74a485cab4c9538a353 ts=2026-08-13T15:48:25.7270000Z == wenyi081326-1.stratalog.logdata.json[3993] _id=6a7de74a485cab4c9538a355 ts=2026-08-13T15:48:25.7270000Z`; `wenyi081326-1.stratalog.logdata.json[3800] _id=6a7de8f6485cab4c9538a4d7 ts=2026-08-13T15:55:34.3730000Z == wenyi081326-1.stratalog.logdata.json[3801] _id=6a7de8f6485cab4c9538a4d9 ts=2026-08-13T15:55:34.3730000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi081326-1.stratalog.logdata.json[202] _id=6a7dfb42485cab4c9538c15a ts=2026-08-13T17:13:38.3530000Z == wenyi081326-1.stratalog.logdata.json[203] _id=6a7dfb42485cab4c9538c15c ts=2026-08-13T17:13:38.3530000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi081326-1.stratalog.logdata.json[4008] _id=6a7de6e8485cab4c9538a335 ts=2026-08-13T15:46:48.4650000Z ~ wenyi081326-1.stratalog.logdata.json[4007] _id=6a7de6e8485cab4c9538a337 ts=2026-08-13T15:46:48.4660000Z`; `27ms: wenyi081326-1.stratalog.logdata.json[3993] _id=6a7de74a485cab4c9538a355 ts=2026-08-13T15:48:25.7270000Z ~ wenyi081326-1.stratalog.logdata.json[3992] _id=6a7de74a485cab4c9538a357 ts=2026-08-13T15:48:25.7540000Z`; `1ms: wenyi081326-1.stratalog.logdata.json[3992] _id=6a7de74a485cab4c9538a357 ts=2026-08-13T15:48:25.7540000Z ~ wenyi081326-1.stratalog.logdata.json[3991] _id=6a7de74a485cab4c9538a359 ts=2026-08-13T15:48:25.7550000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi081326-1.stratalog.logdata.json[4385] _id=6a7de382485cab4c9538a043 ts=2026-08-13T15:32:18.6460000Z ~ wenyi081326-1.stratalog.logdata.json[4384] _id=6a7de382485cab4c9538a045 ts=2026-08-13T15:32:18.6470000Z`; `150ms: wenyi081326-1.stratalog.logdata.json[4260] _id=6a7de4c4485cab4c9538a13d ts=2026-08-13T15:37:40.2920000Z ~ wenyi081326-1.stratalog.logdata.json[4258] _id=6a7de4c4485cab4c9538a141 ts=2026-08-13T15:37:40.4420000Z`; `134ms: wenyi081326-1.stratalog.logdata.json[4233] _id=6a7de4d9485cab4c9538a173 ts=2026-08-13T15:38:01.8520000Z ~ wenyi081326-1.stratalog.logdata.json[4231] _id=6a7de4d9485cab4c9538a177 ts=2026-08-13T15:38:01.9860000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `50ms: wenyi081326-1.stratalog.logdata.json[2376] _id=6a7df0f3485cab4c9538b061 ts=2026-08-13T16:29:39.5420000Z ~ wenyi081326-1.stratalog.logdata.json[2375] _id=6a7df0f3485cab4c9538b063 ts=2026-08-13T16:29:39.5920000Z`; `50ms: wenyi081326-1.stratalog.logdata.json[1699] _id=6a7df2ca485cab4c9538b5b1 ts=2026-08-13T16:37:30.0130000Z ~ wenyi081326-1.stratalog.logdata.json[1694] _id=6a7df2ca485cab4c9538b5b3 ts=2026-08-13T16:37:30.0630000Z`; `135ms: wenyi081326-1.stratalog.logdata.json[1621] _id=6a7df2d9485cab4c9538b647 ts=2026-08-13T16:37:44.5530000Z ~ wenyi081326-1.stratalog.logdata.json[1620] _id=6a7df2d9485cab4c9538b649 ts=2026-08-13T16:37:44.6880000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: wenyi081326-1.stratalog.logdata.json[3346] _id=6a7deb1c485cab4c9538a865 ts=2026-08-13T16:04:44.6640000Z ~ wenyi081326-1.stratalog.logdata.json[3342] _id=6a7deb1c485cab4c9538a86b ts=2026-08-13T16:04:44.6780000Z`; `14ms: wenyi081326-1.stratalog.logdata.json[1270] _id=6a7df43f485cab4c9538b901 ts=2026-08-13T16:43:43.4080000Z ~ wenyi081326-1.stratalog.logdata.json[1266] _id=6a7df43f485cab4c9538b907 ts=2026-08-13T16:43:43.4220000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `15ms: wenyi081326-1.stratalog.logdata.json[4162] _id=6a7de56c485cab4c9538a201 ts=2026-08-13T15:40:28.5560000Z ~ wenyi081326-1.stratalog.logdata.json[4161] _id=6a7de56c485cab4c9538a203 ts=2026-08-13T15:40:28.5710000Z`; `15ms: wenyi081326-1.stratalog.logdata.json[4156] _id=6a7de571485cab4c9538a20d ts=2026-08-13T15:40:33.1070000Z ~ wenyi081326-1.stratalog.logdata.json[4155] _id=6a7de571485cab4c9538a20f ts=2026-08-13T15:40:33.1220000Z`; `14ms: wenyi081326-1.stratalog.logdata.json[4152] _id=6a7de574485cab4c9538a215 ts=2026-08-13T15:40:36.2760000Z ~ wenyi081326-1.stratalog.logdata.json[4151] _id=6a7de574485cab4c9538a217 ts=2026-08-13T15:40:36.2900000Z`
- **INFO / Info** `chatEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `568ms: wenyi081326-1.stratalog.logdata.json[4021] _id=6a7de653485cab4c9538a31b ts=2026-08-13T15:44:19.9600000Z ~ wenyi081326-1.stratalog.logdata.json[4019] _id=6a7de654485cab4c9538a31f ts=2026-08-13T15:44:20.5280000Z`; `500ms: wenyi081326-1.stratalog.logdata.json[4019] _id=6a7de654485cab4c9538a31f ts=2026-08-13T15:44:20.5280000Z ~ wenyi081326-1.stratalog.logdata.json[4017] _id=6a7de654485cab4c9538a323 ts=2026-08-13T15:44:21.0280000Z`; `567ms: wenyi081326-1.stratalog.logdata.json[4017] _id=6a7de654485cab4c9538a323 ts=2026-08-13T15:44:21.0280000Z ~ wenyi081326-1.stratalog.logdata.json[4015] _id=6a7de655485cab4c9538a327 ts=2026-08-13T15:44:21.5950000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `609ms: wenyi081326-1.stratalog.logdata.json[2280] _id=6a7df13d485cab4c9538b11d ts=2026-08-13T16:30:53.4220000Z ~ wenyi081326-1.stratalog.logdata.json[2278] _id=6a7df13d485cab4c9538b121 ts=2026-08-13T16:30:54.0310000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi081326-1.stratalog.logdata.json[80] _id=6a7dfc9d485cab4c9538c250 ts=2026-08-13T17:19:25.8810000Z ~ wenyi081326-1.stratalog.logdata.json[79] _id=6a7dfc9d485cab4c9538c252 ts=2026-08-13T17:19:25.8820000Z`
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 18m 5s 
  - Evidence: 18m 5s: wenyi081326-1.stratalog.logdata.json[1242] _id=6a7df462485cab4c9538b93b ts=2026-08-13T16:44:17.7680000Z -> wenyi081326-1.stratalog.logdata.json[777] _id=6a7df89f485cab4c9538bcde ts=2026-08-13T17:02:23.3670000Z; 11m 1s: wenyi081326-1.stratalog.logdata.json[4464] _id=6a7de2ea485cab4c95389fa5 ts=2026-08-13T15:29:44.7660000Z -> wenyi081326-1.stratalog.logdata.json[4141] _id=6a7de57d485cab4c9538a22b ts=2026-08-13T15:40:46.0450000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 38 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi081326-1.stratalog.logdata.json[1241] _id=6a7df461485cab4c9538b939 ts=2026-08-13T16:44:17.7680000Z -> wenyi081326-1.stratalog.logdata.json[1242] _id=6a7df462485cab4c9538b93b ts=2026-08-13T16:44:17.7680000Z; 0ms: wenyi081326-1.stratalog.logdata.json[3800] _id=6a7de8f6485cab4c9538a4d7 ts=2026-08-13T15:55:34.3730000Z -> wenyi081326-1.stratalog.logdata.json[3801] _id=6a7de8f6485cab4c9538a4d9 ts=2026-08-13T15:55:34.3730000Z; 0ms: wenyi081326-1.stratalog.logdata.json[3994] _id=6a7de74a485cab4c9538a353 ts=2026-08-13T15:48:25.7270000Z -> wenyi081326-1.stratalog.logdata.json[3993] _id=6a7de74a485cab4c9538a355 ts=2026-08-13T15:48:25.7270000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 378 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi081326-1.stratalog.logdata.json[110] _id=6a7dfc78485cab4c9538c214 ts=2026-08-13T17:18:48.3150000Z -> wenyi081326-1.stratalog.logdata.json[109] _id=6a7dfc78485cab4c9538c216 ts=2026-08-13T17:18:48.3150000Z; 0ms: wenyi081326-1.stratalog.logdata.json[1214] _id=6a7df480485cab4c9538b971 ts=2026-08-13T16:44:48.5540000Z -> wenyi081326-1.stratalog.logdata.json[1213] _id=6a7df480485cab4c9538b973 ts=2026-08-13T16:44:48.5540000Z; 0ms: wenyi081326-1.stratalog.logdata.json[1220] _id=6a7df47d485cab4c9538b963 ts=2026-08-13T16:44:45.4700000Z -> wenyi081326-1.stratalog.logdata.json[1221] _id=6a7df47d485cab4c9538b965 ts=2026-08-13T16:44:45.4700000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 28m 45s 
  - Evidence: 28m 45s: wenyi081326-1.stratalog.logdata.json[988] _id=6a7df661485cab4c9538bb35 ts=2026-08-13T16:52:49.4630000Z -> wenyi081326-1.stratalog.logdata.json[1] _id=6a7dfd1e485cab4c9538c2ee ts=2026-08-13T17:21:34.5590000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 68 interval(s) ≤ 0.016s..0.016s shown 
  - Evidence: 16ms: wenyi081326-1.stratalog.logdata.json[2072] _id=6a7df1c6485cab4c9538b2bd ts=2026-08-13T16:33:10.7920000Z -> wenyi081326-1.stratalog.logdata.json[2071] _id=6a7df1c6485cab4c9538b2bf ts=2026-08-13T16:33:10.8080000Z; 16ms: wenyi081326-1.stratalog.logdata.json[2366] _id=6a7df0f6485cab4c9538b071 ts=2026-08-13T16:29:42.5110000Z -> wenyi081326-1.stratalog.logdata.json[2365] _id=6a7df0f6485cab4c9538b073 ts=2026-08-13T16:29:42.5270000Z; 16ms: wenyi081326-1.stratalog.logdata.json[2404] _id=6a7df0ef485cab4c9538b019 ts=2026-08-13T16:29:35.2740000Z -> wenyi081326-1.stratalog.logdata.json[2403] _id=6a7df0ef485cab4c9538b01b ts=2026-08-13T16:29:35.2900000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 23m 45s 
  - Evidence: 23m 45s: wenyi081326-1.stratalog.logdata.json[1744] _id=6a7df2a9485cab4c9538b54d ts=2026-08-13T16:36:57.2980000Z -> wenyi081326-1.stratalog.logdata.json[864] _id=6a7df83b485cab4c9538bc30 ts=2026-08-13T17:00:43.1860000Z; 17m 46s: wenyi081326-1.stratalog.logdata.json[3941] _id=6a7de78e485cab4c9538a3bd ts=2026-08-13T15:49:34.0710000Z -> wenyi081326-1.stratalog.logdata.json[3244] _id=6a7debb9485cab4c9538a931 ts=2026-08-13T16:07:21.0530000Z; 13m 16s: wenyi081326-1.stratalog.logdata.json[2800] _id=6a7ded97485cab4c9538ad0b ts=2026-08-13T16:15:19.3910000Z -> wenyi081326-1.stratalog.logdata.json[2436] _id=6a7df0b4485cab4c9538afe5 ts=2026-08-13T16:28:36.3820000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: wenyi081326-1.stratalog.logdata.json[4385] _id=6a7de382485cab4c9538a043 ts=2026-08-13T15:32:18.6460000Z -> wenyi081326-1.stratalog.logdata.json[4384] _id=6a7de382485cab4c9538a045 ts=2026-08-13T15:32:18.6470000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 18m 14s 
  - Evidence: 18m 14s: wenyi081326-1.stratalog.logdata.json[3051] _id=6a7decaa485cab4c9538aab7 ts=2026-08-13T16:11:20.3450000Z -> wenyi081326-1.stratalog.logdata.json[2410] _id=6a7df0ef485cab4c9538b01d ts=2026-08-13T16:29:34.8750000Z; 17m 53s: wenyi081326-1.stratalog.logdata.json[3922] _id=6a7de799485cab4c9538a3e5 ts=2026-08-13T15:49:45.0430000Z -> wenyi081326-1.stratalog.logdata.json[3219] _id=6a7debcb485cab4c9538a965 ts=2026-08-13T16:07:38.2540000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 231 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi081326-1.stratalog.logdata.json[1477] _id=6a7df304485cab4c9538b761 ts=2026-08-13T16:38:28.1250000Z -> wenyi081326-1.stratalog.logdata.json[1479] _id=6a7df304485cab4c9538b763 ts=2026-08-13T16:38:28.1250000Z; 0ms: wenyi081326-1.stratalog.logdata.json[1479] _id=6a7df304485cab4c9538b763 ts=2026-08-13T16:38:28.1250000Z -> wenyi081326-1.stratalog.logdata.json[1478] _id=6a7df304485cab4c9538b765 ts=2026-08-13T16:38:28.1250000Z; 0ms: wenyi081326-1.stratalog.logdata.json[1480] _id=6a7df304485cab4c9538b75f ts=2026-08-13T16:38:28.1250000Z -> wenyi081326-1.stratalog.logdata.json[1477] _id=6a7df304485cab4c9538b761 ts=2026-08-13T16:38:28.1250000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 21m 4s 
  - Evidence: 21m 4s: wenyi081326-1.stratalog.logdata.json[3232] _id=6a7debc4485cab4c9538a949 ts=2026-08-13T16:07:32.3730000Z -> wenyi081326-1.stratalog.logdata.json[2437] _id=6a7df0b4485cab4c9538afe3 ts=2026-08-13T16:28:36.3810000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 21m 45s 
  - Evidence: 21m 45s: wenyi081326-1.stratalog.logdata.json[3790] _id=6a7de91d485cab4c9538a4ed ts=2026-08-13T15:56:13.8410000Z -> wenyi081326-1.stratalog.logdata.json[2693] _id=6a7dee37485cab4c9538ade1 ts=2026-08-13T16:17:59.8160000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 38m 58s 
  - Evidence: 38m 58s: wenyi081326-1.stratalog.logdata.json[3348] _id=6a7deb1c485cab4c9538a861 ts=2026-08-13T16:04:44.6610000Z -> wenyi081326-1.stratalog.logdata.json[1272] _id=6a7df43f485cab4c9538b8fd ts=2026-08-13T16:43:43.4050000Z; 29m 2s: wenyi081326-1.stratalog.logdata.json[1272] _id=6a7df43f485cab4c9538b8fd ts=2026-08-13T16:43:43.4050000Z -> wenyi081326-1.stratalog.logdata.json[251] _id=6a7dfb0d485cab4c9538c0fa ts=2026-08-13T17:12:45.8760000Z; 23m 40s: wenyi081326-1.stratalog.logdata.json[4122] _id=6a7de590485cab4c9538a251 ts=2026-08-13T15:41:04.5200000Z -> wenyi081326-1.stratalog.logdata.json[3348] _id=6a7deb1c485cab4c9538a861 ts=2026-08-13T16:04:44.6610000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 37m 54s 
  - Evidence: 37m 54s: wenyi081326-1.stratalog.logdata.json[3342] _id=6a7deb1c485cab4c9538a86b ts=2026-08-13T16:04:44.6780000Z -> wenyi081326-1.stratalog.logdata.json[1315] _id=6a7df3ff485cab4c9538b8a7 ts=2026-08-13T16:42:39.2760000Z; 27m 49s: wenyi081326-1.stratalog.logdata.json[1266] _id=6a7df43f485cab4c9538b907 ts=2026-08-13T16:43:43.4220000Z -> wenyi081326-1.stratalog.logdata.json[310] _id=6a7dfac4485cab4c9538c084 ts=2026-08-13T17:11:32.6590000Z; 22m 18s: wenyi081326-1.stratalog.logdata.json[4120] _id=6a7de590485cab4c9538a255 ts=2026-08-13T15:41:04.5230000Z -> wenyi081326-1.stratalog.logdata.json[3407] _id=6a7deaca485cab4c9538a7eb ts=2026-08-13T16:03:22.5410000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.014s..0.014s shown 
  - Evidence: 14ms: wenyi081326-1.stratalog.logdata.json[1270] _id=6a7df43f485cab4c9538b901 ts=2026-08-13T16:43:43.4080000Z -> wenyi081326-1.stratalog.logdata.json[1266] _id=6a7df43f485cab4c9538b907 ts=2026-08-13T16:43:43.4220000Z; 14ms: wenyi081326-1.stratalog.logdata.json[3346] _id=6a7deb1c485cab4c9538a865 ts=2026-08-13T16:04:44.6640000Z -> wenyi081326-1.stratalog.logdata.json[3342] _id=6a7deb1c485cab4c9538a86b ts=2026-08-13T16:04:44.6780000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 22m 33s 
  - Evidence: 22m 33s: wenyi081326-1.stratalog.logdata.json[4124] _id=6a7de58d485cab4c9538a24d ts=2026-08-13T15:41:01.6190000Z -> wenyi081326-1.stratalog.logdata.json[3400] _id=6a7dead7485cab4c9538a7f9 ts=2026-08-13T16:03:35.5460000Z; 20m 38s: wenyi081326-1.stratalog.logdata.json[2512] _id=6a7def29485cab4c9538af4b ts=2026-08-13T16:22:02.0450000Z -> wenyi081326-1.stratalog.logdata.json[1312] _id=6a7df400485cab4c9538b8ad ts=2026-08-13T16:42:40.5920000Z; 19m 0s: wenyi081326-1.stratalog.logdata.json[1275] _id=6a7df42d485cab4c9538b8f7 ts=2026-08-13T16:43:25.0800000Z -> wenyi081326-1.stratalog.logdata.json[774] _id=6a7df8a1485cab4c9538bce4 ts=2026-08-13T17:02:25.3180000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 42 interval(s) ≤ 0.014s..0.015s shown 
  - Evidence: 14ms: wenyi081326-1.stratalog.logdata.json[4152] _id=6a7de574485cab4c9538a215 ts=2026-08-13T15:40:36.2760000Z -> wenyi081326-1.stratalog.logdata.json[4151] _id=6a7de574485cab4c9538a217 ts=2026-08-13T15:40:36.2900000Z; 15ms: wenyi081326-1.stratalog.logdata.json[4156] _id=6a7de571485cab4c9538a20d ts=2026-08-13T15:40:33.1070000Z -> wenyi081326-1.stratalog.logdata.json[4155] _id=6a7de571485cab4c9538a20f ts=2026-08-13T15:40:33.1220000Z; 15ms: wenyi081326-1.stratalog.logdata.json[4162] _id=6a7de56c485cab4c9538a201 ts=2026-08-13T15:40:28.5560000Z -> wenyi081326-1.stratalog.logdata.json[4161] _id=6a7de56c485cab4c9538a203 ts=2026-08-13T15:40:28.5710000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 1h 6m 
  - Evidence: 1h 6m: wenyi081326-1.stratalog.logdata.json[3352] _id=6a7deb19485cab4c9538a859 ts=2026-08-13T16:04:41.7600000Z -> wenyi081326-1.stratalog.logdata.json[307] _id=6a7dfac5485cab4c9538c08a ts=2026-08-13T17:11:33.8770000Z; 22m 21s: wenyi081326-1.stratalog.logdata.json[4123] _id=6a7de58e485cab4c9538a24f ts=2026-08-13T15:41:02.9190000Z -> wenyi081326-1.stratalog.logdata.json[3404] _id=6a7deacc485cab4c9538a7f1 ts=2026-08-13T16:03:24.3410000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 15m 
  - Evidence: 1h 15m: wenyi081326-1.stratalog.logdata.json[4009] _id=6a7de6e8485cab4c9538a333 ts=2026-08-13T15:46:48.4640000Z -> wenyi081326-1.stratalog.logdata.json[760] _id=6a7df8ab485cab4c9538bd00 ts=2026-08-13T17:02:35.4750000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 31m 50s 
  - Evidence: 31m 50s: wenyi081326-1.stratalog.logdata.json[2506] _id=6a7def8c485cab4c9538af59 ts=2026-08-13T16:23:40.8960000Z -> wenyi081326-1.stratalog.logdata.json[985] _id=6a7df703485cab4c9538bb3e ts=2026-08-13T16:55:31.4960000Z; 30m 57s: wenyi081326-1.stratalog.logdata.json[3870] _id=6a7de84b485cab4c9538a44d ts=2026-08-13T15:52:43.3130000Z -> wenyi081326-1.stratalog.logdata.json[2506] _id=6a7def8c485cab4c9538af59 ts=2026-08-13T16:23:40.8960000Z; 18m 41s: wenyi081326-1.stratalog.logdata.json[4466] _id=6a7de2e2485cab4c95389fa1 ts=2026-08-13T15:29:38.8530000Z -> wenyi081326-1.stratalog.logdata.json[3996] _id=6a7de744485cab4c9538a34f ts=2026-08-13T15:48:20.6260000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 13m 16s 
  - Evidence: 13m 16s: wenyi081326-1.stratalog.logdata.json[1184] _id=6a7df4aa485cab4c9538b9ad ts=2026-08-13T16:45:30.1050000Z -> wenyi081326-1.stratalog.logdata.json[954] _id=6a7df7c6485cab4c9538bb7c ts=2026-08-13T16:58:47.0600000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi081326-1.stratalog.logdata.json[202] _id=6a7dfb42485cab4c9538c15a ts=2026-08-13T17:13:38.3530000Z -> wenyi081326-1.stratalog.logdata.json[203] _id=6a7dfb42485cab4c9538c15c ts=2026-08-13T17:13:38.3530000Z; 0ms: wenyi081326-1.stratalog.logdata.json[4182] _id=6a7de55f485cab4c9538a1d7 ts=2026-08-13T15:40:15.3520000Z -> wenyi081326-1.stratalog.logdata.json[4183] _id=6a7de55f485cab4c9538a1d9 ts=2026-08-13T15:40:15.3520000Z; 1ms: wenyi081326-1.stratalog.logdata.json[1822] _id=6a7df278485cab4c9538b4b1 ts=2026-08-13T16:36:08.3930000Z -> wenyi081326-1.stratalog.logdata.json[1821] _id=6a7df278485cab4c9538b4b3 ts=2026-08-13T16:36:08.3940000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `wenyi081326-1.stratalog.logdata.json[3993] _id=6a7de74a485cab4c9538a355 ts=2026-08-13T15:48:25.7270000Z`; `wenyi081326-1.stratalog.logdata.json[3992] _id=6a7de74a485cab4c9538a357 ts=2026-08-13T15:48:25.7540000Z`; `wenyi081326-1.stratalog.logdata.json[3991] _id=6a7de74a485cab4c9538a359 ts=2026-08-13T15:48:25.7550000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4193] _id=6a7de550485cab4c9538a1c3 ts=2026-08-13T15:40:00.6260000Z`; `wenyi081326-1.stratalog.logdata.json[4112] _id=6a7de595485cab4c9538a265 ts=2026-08-13T15:41:09.7270000Z`; `wenyi081326-1.stratalog.logdata.json[3728] _id=6a7de9a6485cab4c9538a569 ts=2026-08-13T15:58:30.2550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi081326-1.stratalog.logdata.json[2375] _id=6a7df0f3485cab4c9538b063 ts=2026-08-13T16:29:39.5920000Z`; `wenyi081326-1.stratalog.logdata.json[1694] _id=6a7df2ca485cab4c9538b5b3 ts=2026-08-13T16:37:30.0630000Z`; `wenyi081326-1.stratalog.logdata.json[1690] _id=6a7df2cb485cab4c9538b5c1 ts=2026-08-13T16:37:30.1790000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi081326-1.stratalog.logdata.json[3342] _id=6a7deb1c485cab4c9538a86b ts=2026-08-13T16:04:44.6780000Z`; `wenyi081326-1.stratalog.logdata.json[1266] _id=6a7df43f485cab4c9538b907 ts=2026-08-13T16:43:43.4220000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4161] _id=6a7de56c485cab4c9538a203 ts=2026-08-13T15:40:28.5710000Z`; `wenyi081326-1.stratalog.logdata.json[4155] _id=6a7de571485cab4c9538a20f ts=2026-08-13T15:40:33.1220000Z`; `wenyi081326-1.stratalog.logdata.json[4151] _id=6a7de574485cab4c9538a217 ts=2026-08-13T15:40:36.2900000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `wenyi081326-1.stratalog.logdata.json[2585] _id=6a7deee6485cab4c9538aeb9 ts=2026-08-13T16:20:54.5470000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 22 occurrence(s) 
  - Examples: `wenyi081326-1.stratalog.logdata.json[4030] _id=6a7de64b485cab4c9538a30b ts=2026-08-13T15:44:11.2750000Z`; `wenyi081326-1.stratalog.logdata.json[4008] _id=6a7de6e8485cab4c9538a335 ts=2026-08-13T15:46:48.4650000Z`; `wenyi081326-1.stratalog.logdata.json[4007] _id=6a7de6e8485cab4c9538a337 ts=2026-08-13T15:46:48.4660000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 24 occurrence(s) 
  - Examples: `wenyi081326-1.stratalog.logdata.json[2354] _id=6a7df0f8485cab4c9538b089 ts=2026-08-13T16:29:44.1790000Z`; `wenyi081326-1.stratalog.logdata.json[2341] _id=6a7df0fa485cab4c9538b0a9 ts=2026-08-13T16:29:45.5960000Z`; `wenyi081326-1.stratalog.logdata.json[1702] _id=6a7df2ca485cab4c9538b5a3 ts=2026-08-13T16:37:29.9650000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `wenyi081326-1.stratalog.logdata.json[1293] _id=6a7df40f485cab4c9538b8d3 ts=2026-08-13T16:42:55.6330000Z`; `wenyi081326-1.stratalog.logdata.json[1291] _id=6a7df410485cab4c9538b8d7 ts=2026-08-13T16:42:56.1160000Z`; `wenyi081326-1.stratalog.logdata.json[285] _id=6a7dfae4485cab4c9538c0b6 ts=2026-08-13T17:12:04.1730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `wenyi081326-1.stratalog.logdata.json[3359] _id=6a7deb06485cab4c9538a84b ts=2026-08-13T16:04:22.6010000Z`; `wenyi081326-1.stratalog.logdata.json[3358] _id=6a7deb07485cab4c9538a84d ts=2026-08-13T16:04:23.6850000Z`; `wenyi081326-1.stratalog.logdata.json[3353] _id=6a7deb18485cab4c9538a857 ts=2026-08-13T16:04:40.4760000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'Open' (totals: 43 open, 48 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'DialogueStartEvent' (totals: 256 start, 255 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'BecameVisible' (totals: 127 open, 127 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 68 open, 71 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 12 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 32 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 44 of 4466 adjacent _id pairs reverse in client time; worst 3.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi081326-1.stratalog.logdata.json[1642] _id=6a7df2cd485cab4c9538b5fd ts=2026-08-13T16:37:33.9980000Z`; `wenyi081326-1.stratalog.logdata.json[1658] _id=6a7df2cd485cab4c9538b5ff ts=2026-08-13T16:37:30.8970000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.09s, min -3.23s, max +0.12s over 4467 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\gameplay-logs-test\config\coverage\08-13-26.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Unit 2 marked partial: only 125 records in 'Unit 2 Prod (Refactor)' and no Unit 2 EndOfUnit in the log (vs 2068 records on 08-25-26).; Manifest written retroactively on 2026-08-26 to serve as the baseline. |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=complete 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)

## 9. Event-Type Details

### `InputEvent` — 1615 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (388); Unit 3 Dev (325); Unit 5 Dev - Dungeon (312); Unit 3 Dungeon Dev (183); Unit 1 Dev (126); Unit 4 Dev (125); Unit 5 Dev (80); Unit 2 Prod (Refactor) (49); Unit 4 Dev - Anderson Base (27)
- **Intervals:** median 0.57s (p5 0.07s / p95 11.31s, n=1614)
- **Fields under `data`:**

```text
data.Value  (string, 1615/1615 records)
    "pressed"  x1615
data.actionType  (string, 1615/1615 records)
    "Move"  x1137
    "Interact"  x243
    "Sprint"  x199
    "Ascend"  x15
    "Hoverboard"  x8
    "Jump"  x5
    "Map"  x5
    "Pause"  x2
    "ToggleDebug"  x1
data.key  (string, 1615/1615 records, 1 empty-string)
    13 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1615/1615 records)
    "Player"  x1379
    "Drone"  x236
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1347 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (305); Unit 4 Dev (232); Unit 5 Dev (216); Unit 1 Dev (148); Unit 3 Dungeon Dev (118); Unit 4 Dev - Dungeon (114); Unit 5 Dev - Dungeon (100); Unit 4 Dev - Anderson Base (71); Unit 2 Prod (Refactor) (43)
- **eventKey:** present on 836 of 1347 records
- **Intervals:** median 0.73s (p5 0.00s / p95 17.73s, n=1346)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x836; [conversationId, dialogueEventType] x511
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1347/1347 records)
    numeric range 10 .. 118 (40 unique)
data.dialogueEventType  (string, 1347/1347 records)
    "DialogueNodeEvent"  x836
    "DialogueStartEvent"  x256
    "DialogueFinishEvent"  x255
data.nodeId  (number, 836/1347 records)
    numeric range 0 .. 273 (193 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 578 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (109); Unit 4 Dev (108); Unit 5 Dev - Dungeon (76); Unit 1 Dev (75); Unit 5 Dev (66); Unit 3 Dungeon Dev (57); Unit 4 Dev - Dungeon (44); Unit 4 Dev - Anderson Base (23); Unit 2 Prod (Refactor) (20)
- **Intervals:** median 10.01s (p5 9.99s / p95 10.01s, n=566)
- **Fields under `data`:**

```text
data.position  (object, 578/578 records)
data.position.x  (number, 578/578 records)
    numeric range -684.999 .. 1556.54 (266 unique)
data.position.y  (number, 578/578 records)
    numeric range -114.326 .. 219.303 (223 unique)
data.position.z  (number, 578/578 records)
    numeric range -1031.93 .. 1391.95 (266 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `PuzzlePieceVisibleEvent` — 346 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 4 Dev (240); Unit 3 Dungeon Dev (104); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.71s, n=345)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 346/346 records)
    "BecameInvisible"  x127
    "BecameVisible"  x127
    "BecameCameraCentered"  x46
    "BecameCameraUncentered"  x46
data.pieceId  (string, 346/346 records)
    15 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 346/346 records)
    245 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `argumentationNodeEvent` — 154 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (45); Unit 5 Dev (44); Unit 4 Dev - Anderson Base (33); Unit 1 Dev (26); Unit 5 Dev - Dungeon (6)
- **Intervals:** median 0.35s (p5 0.02s / p95 14.11s, n=153)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 154/154 records)
    "argumentationNodeHoverEnd"  x71
    "argumentationNodeHoverStart"  x68
    "argumentationNodeAdd"  x15
data.argumentationTitle  (string, 154/154 records)
    "Unit 5"  x50
    "Unit 3 - Pollution Upstream"  x45
    "Unit 4 - Flooding"  x33
    "Unit 1 - Argumentation Tutorial"  x15
    "Unit 1 - Freshwater"  x11
data.nodeName  (string, 154/154 records)
    "I"  x25
    "A"  x24
    "1"  x22
    "2"  x16
    "3"  x14
    "B"  x12
    "D"  x12
    "II"  x10
    "4"  x8
    "C"  x8
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `DaniEvent` — 91 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (25); Unit 1 Dev (20); Unit 5 Dev - Dungeon (14); Unit 4 Dev (12); Unit 2 Prod (Refactor) (6); Unit 4 Dev - Anderson Base (6); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (2); Unit 5 Dev (2)
- **Intervals:** median 1.86s (p5 0.00s / p95 435.65s, n=90)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 91/91 records)
    "Close"  x48
    "Open"  x43
data.toolName  (string, 91/91 records, 22 empty-string)
    "Argumentation"  x43
    ""  x22
    "Map"  x22
    "Chat"  x2
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `ObjectInterEvent` — 59 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (22); Unit 1 Dev (14); Unit 3 Dungeon Dev (14); Unit 5 Dev - Dungeon (5); Unit 2 Prod (Refactor) (2); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 11.37s (p5 1.54s / p95 592.81s, n=58)
- **Fields under `data`:**

```text
data.actionType  (string, 59/59 records)
    "Press E to Pick up"  x32
    "Press E to Install"  x11
    "E to Talk"  x6
    "TalkTo"  x6
    "Press E to Open Locker"  x2
    "Press E to Operate"  x2
data.objectName  (string, 59/59 records)
    "Powercube"  x32
    "Power Dock"  x11
    "Anderson"  x3
    "Aryn"  x3
    "Toppo"  x3
    "Player Locker"  x2
    "Soil Key Puzzle Soil"  x2
    "Tera"  x2
    "Jasper"  x1
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 56 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (11); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 2 Prod (Refactor) (1)
- **eventKey:** present on 56 of 56 records
- **Intervals:** median 81.19s (p5 0.00s / p95 364.63s, n=55)
- **`data` key-set variants:** [questEventType, questID, questName] x32; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 56/56 records)
    "questActiveEvent"  x32
    "questFinishEvent"  x24
data.questID  (string, 56/56 records)
    29 unique values (see csv/event_unique_values.csv)
data.questName  (string, 56/56 records)
    29 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/56 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `chatEvent` — 32 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 1 Dev (16); Unit 5 Dev - Dungeon (16)
- **Intervals:** median 0.42s (p5 0.22s / p95 73.82s, n=31)
- **`data` key-set variants:** [actionType, chatID] x18; [actionKey, chatID] x14
- **Fields under `data`:**

```text
data.actionKey  (string, 14/32 records)
    "ScrollStop"  x14
data.actionType  (string, 18/32 records)
    "ScrollStart"  x14
    "Close"  x2
    "Open"  x2
data.chatID  (string, 32/32 records)
    16 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `TopographicMapEvent` — 31 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (26); Unit 1 Dev (5)
- **Intervals:** median 2.55s (p5 0.61s / p95 340.57s, n=30)
- **`data` key-set variants:** [actionType, featureUsed] x16; [actionType, featureUsed, location] x15
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "dragEnd"  x15
    "MapCloseEvent"  x8
    "MapOpenEvent"  x8
data.featureUsed  (string, 31/31 records)
    "Map"  x16
    "waypoint"  x15
data.location  (object, 15/31 records)
data.location.x  (number, 15/31 records)
    9 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 15/31 records)
    numeric range -313.963 .. 87.6247 (13 unique)
data.location.z  (number, 15/31 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowUnfocusEvent` — 31 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (10); Unit 4 Dev (6); Unit 3 Dev (5); Unit 3 Dungeon Dev (3); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Transition (1); Unit 2 Prod (Refactor) (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 150.15s (p5 15.56s / p95 408.93s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 31/31 records)
    false  x31
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameWindowFocusEvent` — 29 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 1 Dev (9); Unit 4 Dev (6); Unit 3 Dev (5); Unit 3 Dungeon Dev (3); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Transition (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 142.33s (p5 7.68s / p95 419.67s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 29/29 records)
    true  x29
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 26 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (14); Unit 3 Dev (12)
- **Intervals:** median 0.47s (p5 0.15s / p95 6.59s, n=25)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x22; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/26 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/26 records)
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 22/26 records)
    "RightDrag"  x12
    "LeftDrag"  x10
data.currentSoilType  (string, 22/26 records)
    "CLAY"  x4
    "CLAYSAND"  x4
    "SAND"  x4
    "SANDGRAVEL"  x4
    "CLAYROCK"  x3
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 22/26 records)
    "false"  x18
    "true"  x4
data.waterLevelStatus  (string, 22/26 records)
    "TooLow"  x9
    "Proper"  x7
    "TooHigh"  x6
data.waterRetentionChange  (string, 22/26 records)
    "Decrease"  x12
    "Increase"  x6
    "NoChange"  x4
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 21 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (21)
- **Intervals:** median 12.20s (p5 4.99s / p95 55.30s, n=20)
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "On"  x15
    "Off"  x6
data.floor  (string, 21/21 records)
    "3"  x8
    "4"  x7
    "2"  x4
    "1"  x2
data.machineNumber  (string, 21/21 records)
    "One"  x20
    "Two"  x1
data.machineType  (string, 21/21 records)
    "Condenser"  x9
    "Evaporator"  x5
    "VentSwitch"  x4
    "DualChamber_Evaporator"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 21/21 records)
    "2"  x9
    "3"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (6); Unit 5 Dev (5); Unit 1 Dev (3)
- **Intervals:** median 9.02s (p5 1.04s / p95 2409.70s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolOpen"  x12
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 5"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 64.13s (p5 0.01s / p95 1971.92s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 3.27s (p5 1.08s / p95 17.03s, n=5)
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

### `argumentationAnswerEvent` — 5 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 1581.31s (p5 235.73s / p95 2249.30s, n=4)
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "submitAnswerEvent"  x5
data.answerSubmitted  (string, 5/5 records)
    "A,1,I"  x2
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "C,D,3,II"  x1
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
    "Unit 4 - Flooding"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 5 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (5)
- **Intervals:** median 1489.68s (p5 391.55s / p95 1902.65s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 5/5 records)
    true  x5
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 5 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (5)
- **Intervals:** median 35.17s (p5 19.77s / p95 61.97s, n=4)
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

### `DEBUGMenu` — 2 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (2)
- **Intervals:** median 2.01s (p5 2.01s / p95 2.01s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "DebugMenuStateChanged"  x2
data.isOpened  (bool, 2/2 records)
    false  x1
    true  x1
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1725.10s (p5 1725.10s / p95 1725.10s, n=1)
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

No baseline supplied — skipped.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `DaniEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DaniEvent` actionType: tool open/close: close without preceding open
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open
- `argumentationNodeEvent` actionType: node hover: close without preceding open
- `questEvent` questEventType: quest lifecycle: finish without preceding start
- `TerasGardenBox` : field-name variants that differ only in spelling/case
- `gameStartEvent` data.<empty>: field name is an empty string
- `gameWindowFocusEvent` data.<empty>: field name is an empty string
- `gameWindowUnfocusEvent` data.<empty>: field name is an empty string
- `DaniEvent` actionType: tool open/close: repeated open with no intervening close


---
*Generated by gameplay-logs-test / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*