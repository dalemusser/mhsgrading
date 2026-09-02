# MHS Gameplay Log Audit Report — build 08-31-26

## 1. Build Information

- **Build ID:** 08-31-26
- **Game version string(s) in log:** 20260826-12286
- **Audit date:** 2026-09-01
- **Log file(s):** wenyi083126-1.stratalog.logdata.json
- **Records:** 5977 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6a95b79ce2ada9cb13ea6f13
- **Time span:** 2026-08-31T17:29:07.769000+00:00 .. 2026-09-01T00:41:38.454000+00:00 (7h 12m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\gameplay-logs-test\config\coverage\08-31-26.yaml
- **Baseline:** snapshot gameplay-logs-test\reports\08-25-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 5977 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 73 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DialogueEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: event type present in baseline 08-25-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1883 | 31.5 | 1 | 9 | 0 | 2026-08-31T17:30:30.288000+00:00 | 2026-09-01T00:41:38.454000+00:00 | 7h 11m |
| DialogueEvent | 1775 | 29.7 | 1 | 9 | 1136 | 2026-08-31T17:29:27.229000+00:00 | 2026-09-01T00:41:35.752000+00:00 | 7h 12m |
| PuzzlePieceVisibleEvent | 1018 | 17.03 | 1 | 3 | 0 | 2026-08-31T23:08:21.579000+00:00 | 2026-09-01T00:08:22.704000+00:00 | 1h 0m |
| PlayerPositionEvent | 655 | 10.96 | 1 | 9 | 0 | 2026-08-31T17:29:10.600000+00:00 | 2026-09-01T00:41:34.083000+00:00 | 7h 12m |
| ObjectInterEvent | 166 | 2.78 | 1 | 9 | 0 | 2026-08-31T17:30:52.964000+00:00 | 2026-09-01T00:41:38.454000+00:00 | 7h 10m |
| argumentationNodeEvent | 155 | 2.59 | 1 | 5 | 0 | 2026-08-31T17:37:56.618000+00:00 | 2026-09-01T00:35:51.117000+00:00 | 6h 57m |
| questEvent | 68 | 1.14 | 1 | 9 | 68 | 2026-08-31T17:29:27.225000+00:00 | 2026-09-01T00:41:03.655000+00:00 | 7h 11m |
| TopographicMapEvent | 63 | 1.05 | 1 | 2 | 0 | 2026-08-31T23:08:38.453000+00:00 | 2026-08-31T23:53:59.949000+00:00 | 45m 21s |
| DaniEvent | 42 | 0.7 | 1 | 5 | 0 | 2026-08-31T17:39:09.487000+00:00 | 2026-09-01T00:35:53.704000+00:00 | 6h 56m |
| Soil Key Puzzle | 32 | 0.54 | 1 | 3 | 0 | 2026-08-31T23:11:13.195000+00:00 | 2026-09-01T00:00:45.627000+00:00 | 49m 32s |
| WaterChamberEvent | 18 | 0.3 | 1 | 1 | 0 | 2026-09-01T00:25:19.116000+00:00 | 2026-09-01T00:32:44.737000+00:00 | 7m 25s |
| argumentationToolEvent | 18 | 0.3 | 1 | 4 | 0 | 2026-08-31T17:37:41.877000+00:00 | 2026-09-01T00:35:53.618000+00:00 | 6h 58m |
| gameWindowFocusEvent | 18 | 0.3 | 1 | 8 | 0 | 2026-08-31T17:29:34.400000+00:00 | 2026-09-01T00:39:37.327000+00:00 | 7h 10m |
| gameWindowUnfocusEvent | 18 | 0.3 | 1 | 8 | 0 | 2026-08-31T17:29:14.390000+00:00 | 2026-09-01T00:37:36.135000+00:00 | 7h 8m |
| argumentationEvent | 14 | 0.23 | 1 | 5 | 0 | 2026-08-31T17:37:42.994000+00:00 | 2026-09-01T00:35:53.707000+00:00 | 6h 58m |
| argumentationAnswerEvent | 7 | 0.12 | 1 | 5 | 0 | 2026-08-31T17:38:02.803000+00:00 | 2026-09-01T00:35:53.702000+00:00 | 6h 57m |
| TerasGardenBox | 6 | 0.1 | 1 | 1 | 0 | 2026-09-01T00:14:58.486000+00:00 | 2026-09-01T00:15:44.537000+00:00 | 46.1s |
| EndOfUnit | 5 | 0.08 | 1 | 5 | 0 | 2026-08-31T17:44:38.692000+00:00 | 2026-09-01T00:41:38.452000+00:00 | 6h 56m |
| gameStartEvent | 5 | 0.08 | 1 | 1 | 0 | 2026-08-31T17:29:07.769000+00:00 | 2026-09-01T00:21:19.596000+00:00 | 6h 52m |
| soilMachine | 5 | 0.08 | 1 | 1 | 0 | 2026-09-01T00:04:48.719000+00:00 | 2026-09-01T00:07:20.530000+00:00 | 2m 31s |
| SolarStillDesignEvent | 4 | 0.07 | 1 | 1 | 0 | 2026-09-01T00:39:50.271000+00:00 | 2026-09-01T00:39:57.497000+00:00 | 7.2s |
| chatEvent | 2 | 0.03 | 1 | 2 | 0 | 2026-09-01T00:21:21.531000+00:00 | 2026-09-01T00:33:23.416000+00:00 | 12m 1s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 08-25-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 4.718s median 
  - Expected: 1.951s in 08-25-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.101s median 
  - Expected: 6.502s in 08-25-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — baseline field(s) absent this build. 
  - Observed: data.actionKey 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 721.885s median 
  - Expected: 0.282s in 08-25-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 37.414s median 
  - Expected: 15.582s in 08-25-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: ; Chat; Settings 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Pause; ToggleDebug 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: backquote; tab 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to go down; Press E to inspect ; Press E to pick up; Press E to place canister; Press E to use; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: C,D,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 38 in 08-25-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Open; ScrollStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` `data.chatID` — baseline categorical value(s) not seen this build. 
  - Observed: [16-3, 18-1, 18-2, 18-4, 18-5, 18-7]; [16-3, 18-1, 18-2, 18-4, 18-5]; [17-19, 17-20, 17-22, 17-26, 18-21, 18-22]; [17-22, 17-26, 18-21, 18-22, 18-24, 18-25, 18-33]; [17-22, 17-26, 18-21, 18-22, 18-24]; [18-10, 17-17, 17-19, 17-20, 17-22, 17-26]; [18-22, 18-24, 18-25, 18-33, 18-34, 18-35]; [18-33, 18-34, 18-35, 18-36, 18-37, 18-38, 18-39]; [18-34, 18-35, 18-36, 18-37, 18-38, 18-39]; [18-37, 18-38, 18-39, 18-269, 18-271, 18-273]; [18-38, 18-39, 18-269, 18-271, 18-273]; [18-4, 18-5, 18-7, 18-8, 18-10, 17-17]; [18-4, 18-5, 18-7, 18-8, 18-10]; [18-8, 18-10, 17-17, 17-19, 17-20, 17-22] 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Bedrock 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 17 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5863] _id=6a95ba82485cab4c953d685e ts=2026-08-31T17:31:46.3760000Z`; `wenyi083126-1.stratalog.logdata.json[5813] _id=6a95bb25485cab4c953d68c2 ts=2026-08-31T17:34:29.1370000Z`; `wenyi083126-1.stratalog.logdata.json[5784] _id=6a95bb3e485cab4c953d68fc ts=2026-08-31T17:34:54.7820000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 5 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 5} 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5976] _id=6a95b9e3485cab4c953d6774 ts=2026-08-31T17:29:07.7690000Z`; `wenyi083126-1.stratalog.logdata.json[5475] _id=6a9608f4485cab4c953da5bf ts=2026-08-31T23:06:28.7800000Z`; `wenyi083126-1.stratalog.logdata.json[3651] _id=6a960f49485cab4c953db857 ts=2026-08-31T23:33:30.0900000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5968] _id=6a95b9fe485cab4c953d6788 ts=2026-08-31T17:29:34.4000000Z`; `wenyi083126-1.stratalog.logdata.json[5865] _id=6a95ba82485cab4c953d685a ts=2026-08-31T17:31:46.3650000Z`; `wenyi083126-1.stratalog.logdata.json[5665] _id=6a95bbf4485cab4c953d6a0a ts=2026-08-31T17:37:56.6070000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5974] _id=6a95b9ea485cab4c953d6778 ts=2026-08-31T17:29:14.3900000Z`; `wenyi083126-1.stratalog.logdata.json[5868] _id=6a95ba78485cab4c953d6854 ts=2026-08-31T17:31:36.5720000Z`; `wenyi083126-1.stratalog.logdata.json[5667] _id=6a95bbe8485cab4c953d6a02 ts=2026-08-31T17:37:44.4580000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1882 | 0.0 | 0.5 | 13.745 | 12.972 | 19394.171 | 4.37 | 103 | 1 |
| DialogueEvent | 1774 | 0.0 | 0.684 | 14.616 | 16.314 | 19316.787 | 4.11 | 494 | 1 |
| PuzzlePieceVisibleEvent | 1017 | 0.0 | 0.033 | 3.541 | 1.181 | 1394.689 | 16.94 | 627 | 2 |
| PlayerPositionEvent | 643 | 9.955 | 10.005 | 10.134 | 10.006 | 42.57 | 5.92 | 0 | 0 |
| ObjectInterEvent | 165 | 0.0 | 7.054 | 156.639 | 193.714 | 19449.932 | 0.38 | 3 | 2 |
| argumentationNodeEvent | 154 | 0.014 | 0.25 | 162.821 | 8.623 | 21198.833 | 0.37 | 38 | 4 |
| questEvent | 67 | 0.0 | 64.48 | 386.514 | 295.203 | 19419.033 | 0.16 | 13 | 1 |
| TopographicMapEvent | 62 | 0.004 | 2.484 | 43.895 | 283.281 | 817.674 | 1.37 | 4 | 2 |
| DaniEvent | 41 | 0.004 | 14.09 | 609.859 | 1115.594 | 19768.966 | 0.1 | 3 | 4 |
| Soil Key Puzzle | 31 | 0.351 | 0.617 | 95.885 | 653.452 | 1626.276 | 0.63 | 0 | 2 |
| WaterChamberEvent | 17 | 3.101 | 16.302 | 26.213 | 57.343 | 91.107 | 2.29 | 0 | 0 |
| argumentationToolEvent | 17 | 0.067 | 1.101 | 1475.985 | 6736.093 | 21192.495 | 0.04 | 0 | 3 |
| gameWindowFocusEvent | 17 | 6.748 | 199.213 | 1517.819 | 4858.528 | 20446.57 | 0.04 | 0 | 4 |
| gameWindowUnfocusEvent | 17 | 17.658 | 216.72 | 1511.867 | 4943.866 | 20430.283 | 0.04 | 0 | 4 |
| argumentationEvent | 13 | 0.014 | 36.299 | 1930.055 | 9522.776 | 21189.725 | 0.03 | 2 | 4 |
| argumentationAnswerEvent | 6 | 24.612 | 1006.195 | 4178.483 | 16353.309 | 21210.704 | 0.01 | 0 | 4 |
| TerasGardenBox | 5 | 1.334 | 4.718 | 9.21 | 19.77 | 20.194 | 6.51 | 0 | 0 |
| EndOfUnit | 4 | 1230.515 | 1432.505 | 6254.94 | 18015.451 | 20924.235 | 0.01 | 0 | 4 |
| gameStartEvent | 4 | 1336.382 | 1577.217 | 6182.957 | 17448.056 | 20241.011 | 0.01 | 0 | 4 |
| soilMachine | 4 | 8.355 | 37.414 | 37.953 | 65.129 | 68.628 | 1.58 | 0 | 0 |
| SolarStillDesignEvent | 3 | 2.123 | 2.334 | 2.409 | 2.726 | 2.769 | 24.91 | 0 | 0 |
| chatEvent | 1 | 721.885 | 721.885 | 721.885 | 721.885 | 721.885 | 0.08 | 0 | 1 |

- **WARNING / Medium** `DialogueEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi083126-1.stratalog.logdata.json[4718] _id=6a960afb485cab4c953dabdb ts=2026-08-31T23:15:07.4580000Z == wenyi083126-1.stratalog.logdata.json[4719] _id=6a960afb485cab4c953dabdd ts=2026-08-31T23:15:07.4580000Z`
- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi083126-1.stratalog.logdata.json[4903] _id=6a9609f5485cab4c953daa37 ts=2026-08-31T23:10:45.2300000Z == wenyi083126-1.stratalog.logdata.json[4902] _id=6a9609f5485cab4c953daa39 ts=2026-08-31T23:10:45.2300000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi083126-1.stratalog.logdata.json[1221] _id=6a961850485cab4c953dd1f7 ts=2026-09-01T00:12:00.4000000Z == wenyi083126-1.stratalog.logdata.json[1220] _id=6a961850485cab4c953dd1f9 ts=2026-09-01T00:12:00.4000000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 16 group(s), 20 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5404] _id=6a96098d485cab4c953da689 ts=2026-08-31T23:08:21.5790000Z == wenyi083126-1.stratalog.logdata.json[5407] _id=6a96098d485cab4c953da68b ts=2026-08-31T23:08:21.5790000Z`; `wenyi083126-1.stratalog.logdata.json[5397] _id=6a96098e485cab4c953da69f ts=2026-08-31T23:08:21.6120000Z == wenyi083126-1.stratalog.logdata.json[5395] _id=6a96098e485cab4c953da6a1 ts=2026-08-31T23:08:21.6120000Z`; `wenyi083126-1.stratalog.logdata.json[5393] _id=6a96098e485cab4c953da6a3 ts=2026-08-31T23:08:21.6290000Z == wenyi083126-1.stratalog.logdata.json[5392] _id=6a96098e485cab4c953da6a5 ts=2026-08-31T23:08:21.6290000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi083126-1.stratalog.logdata.json[191] _id=6a961e20485cab4c953ddacb ts=2026-09-01T00:36:48.2100000Z == wenyi083126-1.stratalog.logdata.json[192] _id=6a961e20485cab4c953ddacd ts=2026-09-01T00:36:48.2100000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: wenyi083126-1.stratalog.logdata.json[4779] _id=6a960aac485cab4c953dab55 ts=2026-08-31T23:13:48.1840000Z ~ wenyi083126-1.stratalog.logdata.json[4774] _id=6a960aac485cab4c953dab5d ts=2026-08-31T23:13:48.1880000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi083126-1.stratalog.logdata.json[5900] _id=6a95ba4c485cab4c953d6814 ts=2026-08-31T17:30:52.9640000Z ~ wenyi083126-1.stratalog.logdata.json[5899] _id=6a95ba4c485cab4c953d6816 ts=2026-08-31T17:30:52.9650000Z`; `167ms: wenyi083126-1.stratalog.logdata.json[5738] _id=6a95bb59485cab4c953d6958 ts=2026-08-31T17:35:22.0260000Z ~ wenyi083126-1.stratalog.logdata.json[5736] _id=6a95bb5a485cab4c953d695c ts=2026-08-31T17:35:22.1930000Z`; `1ms: wenyi083126-1.stratalog.logdata.json[1246] _id=6a961830485cab4c953dd171 ts=2026-09-01T00:11:28.8680000Z ~ wenyi083126-1.stratalog.logdata.json[1245] _id=6a961830485cab4c953dd173 ts=2026-09-01T00:11:28.8690000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `32ms: wenyi083126-1.stratalog.logdata.json[5182] _id=6a9609a1485cab4c953da813 ts=2026-08-31T23:09:20.1730000Z ~ wenyi083126-1.stratalog.logdata.json[5180] _id=6a9609a1485cab4c953da815 ts=2026-08-31T23:09:20.2050000Z`; `434ms: wenyi083126-1.stratalog.logdata.json[2992] _id=6a961276485cab4c953dc021 ts=2026-08-31T23:47:01.8000000Z ~ wenyi083126-1.stratalog.logdata.json[2987] _id=6a961276485cab4c953dc023 ts=2026-08-31T23:47:02.2340000Z`; `33ms: wenyi083126-1.stratalog.logdata.json[2973] _id=6a961279485cab4c953dc049 ts=2026-08-31T23:47:04.2680000Z ~ wenyi083126-1.stratalog.logdata.json[2970] _id=6a961279485cab4c953dc04b ts=2026-08-31T23:47:04.3010000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: wenyi083126-1.stratalog.logdata.json[4778] _id=6a960aac485cab4c953dab53 ts=2026-08-31T23:13:48.1840000Z ~ wenyi083126-1.stratalog.logdata.json[4773] _id=6a960aac485cab4c953dab5f ts=2026-08-31T23:13:48.1880000Z`; `15ms: wenyi083126-1.stratalog.logdata.json[4720] _id=6a960afb485cab4c953dabd9 ts=2026-08-31T23:15:07.4570000Z ~ wenyi083126-1.stratalog.logdata.json[4716] _id=6a960afb485cab4c953dabdf ts=2026-08-31T23:15:07.4720000Z`; `14ms: wenyi083126-1.stratalog.logdata.json[4676] _id=6a960b34485cab4c953dac81 ts=2026-08-31T23:16:04.8510000Z ~ wenyi083126-1.stratalog.logdata.json[4673] _id=6a960b34485cab4c953dac85 ts=2026-08-31T23:16:04.8650000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: wenyi083126-1.stratalog.logdata.json[3211] _id=6a9611a2485cab4c953dbd81 ts=2026-08-31T23:43:31.0360000Z ~ wenyi083126-1.stratalog.logdata.json[3207] _id=6a9611a2485cab4c953dbd87 ts=2026-08-31T23:43:31.0500000Z`; `14ms: wenyi083126-1.stratalog.logdata.json[1144] _id=6a961898485cab4c953dd2dd ts=2026-09-01T00:13:12.1590000Z ~ wenyi083126-1.stratalog.logdata.json[1141] _id=6a961898485cab4c953dd2e3 ts=2026-09-01T00:13:12.1730000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 25 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: wenyi083126-1.stratalog.logdata.json[5662] _id=6a95bbf4485cab4c953d6a10 ts=2026-08-31T17:37:56.7030000Z ~ wenyi083126-1.stratalog.logdata.json[5661] _id=6a95bbf4485cab4c953d6a12 ts=2026-08-31T17:37:56.7170000Z`; `632ms: wenyi083126-1.stratalog.logdata.json[5664] _id=6a95bbf4485cab4c953d6a0c ts=2026-08-31T17:37:56.6180000Z ~ wenyi083126-1.stratalog.logdata.json[5660] _id=6a95bbf5485cab4c953d6a14 ts=2026-08-31T17:37:57.2500000Z`; `584ms: wenyi083126-1.stratalog.logdata.json[5661] _id=6a95bbf4485cab4c953d6a12 ts=2026-08-31T17:37:56.7170000Z ~ wenyi083126-1.stratalog.logdata.json[5659] _id=6a95bbf5485cab4c953d6a16 ts=2026-08-31T17:37:57.3010000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `450ms: wenyi083126-1.stratalog.logdata.json[5609] _id=6a95bc22485cab4c953d6a80 ts=2026-08-31T17:38:42.9060000Z ~ wenyi083126-1.stratalog.logdata.json[5607] _id=6a95bc23485cab4c953d6a84 ts=2026-08-31T17:38:43.3560000Z`; `967ms: wenyi083126-1.stratalog.logdata.json[5608] _id=6a95bc23485cab4c953d6a82 ts=2026-08-31T17:38:43.2890000Z ~ wenyi083126-1.stratalog.logdata.json[5606] _id=6a95bc24485cab4c953d6a86 ts=2026-08-31T17:38:44.2560000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi083126-1.stratalog.logdata.json[75] _id=6a961f13485cab4c953ddbb5 ts=2026-09-01T00:40:51.6820000Z ~ wenyi083126-1.stratalog.logdata.json[74] _id=6a961f13485cab4c953ddbb7 ts=2026-09-01T00:40:51.6830000Z`
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 29m 
  - Evidence: 5h 29m: wenyi083126-1.stratalog.logdata.json[5587] _id=6a95bc3d485cab4c953d6ac6 ts=2026-08-31T17:39:09.4870000Z -> wenyi083126-1.stratalog.logdata.json[5365] _id=6a960976485cab4c953da651 ts=2026-08-31T23:08:38.4530000Z; 22m 41s: wenyi083126-1.stratalog.logdata.json[1145] _id=6a961898485cab4c953dd2db ts=2026-09-01T00:13:12.1580000Z -> wenyi083126-1.stratalog.logdata.json[240] _id=6a961de9485cab4c953dda6b ts=2026-09-01T00:35:53.7040000Z; 18m 35s: wenyi083126-1.stratalog.logdata.json[2515] _id=6a961417485cab4c953dc513 ts=2026-08-31T23:53:59.9500000Z -> wenyi083126-1.stratalog.logdata.json[1178] _id=6a961873485cab4c953dd28d ts=2026-09-01T00:12:35.5440000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.004s..0.016s shown 
  - Evidence: 4ms: wenyi083126-1.stratalog.logdata.json[4779] _id=6a960aac485cab4c953dab55 ts=2026-08-31T23:13:48.1840000Z -> wenyi083126-1.stratalog.logdata.json[4774] _id=6a960aac485cab4c953dab5d ts=2026-08-31T23:13:48.1880000Z; 15ms: wenyi083126-1.stratalog.logdata.json[4677] _id=6a960b34485cab4c953dac7f ts=2026-08-31T23:16:04.8500000Z -> wenyi083126-1.stratalog.logdata.json[4674] _id=6a960b34485cab4c953dac87 ts=2026-08-31T23:16:04.8650000Z; 16ms: wenyi083126-1.stratalog.logdata.json[4721] _id=6a960afb485cab4c953dabd7 ts=2026-08-31T23:15:07.4560000Z -> wenyi083126-1.stratalog.logdata.json[4717] _id=6a960afb485cab4c953dabe1 ts=2026-08-31T23:15:07.4720000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 5h 21m 
  - Evidence: 5h 21m: wenyi083126-1.stratalog.logdata.json[5477] _id=6a95bd84485cab4c953d6d06 ts=2026-08-31T17:44:36.2910000Z -> wenyi083126-1.stratalog.logdata.json[5473] _id=6a9608f8485cab4c953da5c3 ts=2026-08-31T23:06:33.0780000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 494 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi083126-1.stratalog.logdata.json[103] _id=6a961eee485cab4c953ddb7b ts=2026-09-01T00:40:14.1150000Z -> wenyi083126-1.stratalog.logdata.json[104] _id=6a961eee485cab4c953ddb7d ts=2026-09-01T00:40:14.1150000Z; 0ms: wenyi083126-1.stratalog.logdata.json[1093] _id=6a9618ce485cab4c953dd3bf ts=2026-09-01T00:14:06.9680000Z -> wenyi083126-1.stratalog.logdata.json[1092] _id=6a9618ce485cab4c953dd3c1 ts=2026-09-01T00:14:06.9680000Z; 0ms: wenyi083126-1.stratalog.logdata.json[1095] _id=6a9618cd485cab4c953dd3b7 ts=2026-09-01T00:14:05.7510000Z -> wenyi083126-1.stratalog.logdata.json[1096] _id=6a9618cd485cab4c953dd3b9 ts=2026-09-01T00:14:05.7510000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 48m 
  - Evidence: 5h 48m: wenyi083126-1.stratalog.logdata.json[5476] _id=6a95bd86485cab4c953d6d08 ts=2026-08-31T17:44:38.6920000Z -> wenyi083126-1.stratalog.logdata.json[3653] _id=6a960f42485cab4c953db851 ts=2026-08-31T23:33:22.9270000Z; 25m 32s: wenyi083126-1.stratalog.logdata.json[2431] _id=6a961477485cab4c953dc623 ts=2026-08-31T23:55:35.5950000Z -> wenyi083126-1.stratalog.logdata.json[845] _id=6a961a73485cab4c953dd5af ts=2026-09-01T00:21:07.9370000Z; 22m 12s: wenyi083126-1.stratalog.logdata.json[3653] _id=6a960f42485cab4c953db851 ts=2026-08-31T23:33:22.9270000Z -> wenyi083126-1.stratalog.logdata.json[2431] _id=6a961477485cab4c953dc623 ts=2026-08-31T23:55:35.5950000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 5h 23m 
  - Evidence: 5h 23m: wenyi083126-1.stratalog.logdata.json[5501] _id=6a95bd5b485cab4c953d6cc2 ts=2026-08-31T17:43:55.9890000Z -> wenyi083126-1.stratalog.logdata.json[5467] _id=6a96091d485cab4c953da5cf ts=2026-08-31T23:07:10.1600000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 103 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi083126-1.stratalog.logdata.json[4903] _id=6a9609f5485cab4c953daa37 ts=2026-08-31T23:10:45.2300000Z -> wenyi083126-1.stratalog.logdata.json[4902] _id=6a9609f5485cab4c953daa39 ts=2026-08-31T23:10:45.2300000Z; 1ms: wenyi083126-1.stratalog.logdata.json[1796] _id=6a9616a8485cab4c953dcc6f ts=2026-09-01T00:04:57.1060000Z -> wenyi083126-1.stratalog.logdata.json[1795] _id=6a9616a8485cab4c953dcc73 ts=2026-09-01T00:04:57.1070000Z; 1ms: wenyi083126-1.stratalog.logdata.json[4904] _id=6a9609f5485cab4c953daa35 ts=2026-08-31T23:10:45.2290000Z -> wenyi083126-1.stratalog.logdata.json[4903] _id=6a9609f5485cab4c953daa37 ts=2026-08-31T23:10:45.2300000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 5h 24m 
  - Evidence: 5h 24m: wenyi083126-1.stratalog.logdata.json[5500] _id=6a95bd5d485cab4c953d6cc4 ts=2026-08-31T17:43:57.2560000Z -> wenyi083126-1.stratalog.logdata.json[5431] _id=6a960957485cab4c953da617 ts=2026-08-31T23:08:07.1880000Z; 11m 16s: wenyi083126-1.stratalog.logdata.json[4604] _id=6a960bd2485cab4c953dade5 ts=2026-08-31T23:18:42.4410000Z -> wenyi083126-1.stratalog.logdata.json[3935] _id=6a960e76485cab4c953db61d ts=2026-08-31T23:29:58.8120000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi083126-1.stratalog.logdata.json[1221] _id=6a961850485cab4c953dd1f7 ts=2026-09-01T00:12:00.4000000Z -> wenyi083126-1.stratalog.logdata.json[1220] _id=6a961850485cab4c953dd1f9 ts=2026-09-01T00:12:00.4000000Z; 1ms: wenyi083126-1.stratalog.logdata.json[1246] _id=6a961830485cab4c953dd171 ts=2026-09-01T00:11:28.8680000Z -> wenyi083126-1.stratalog.logdata.json[1245] _id=6a961830485cab4c953dd173 ts=2026-09-01T00:11:28.8690000Z; 1ms: wenyi083126-1.stratalog.logdata.json[5900] _id=6a95ba4c485cab4c953d6814 ts=2026-08-31T17:30:52.9640000Z -> wenyi083126-1.stratalog.logdata.json[5899] _id=6a95ba4c485cab4c953d6816 ts=2026-08-31T17:30:52.9650000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23m 14s 
  - Evidence: 23m 14s: wenyi083126-1.stratalog.logdata.json[4145] _id=6a960cd9485cab4c953db327 ts=2026-08-31T23:23:04.1640000Z -> wenyi083126-1.stratalog.logdata.json[3099] _id=6a96124b485cab4c953dbf13 ts=2026-08-31T23:46:18.8530000Z; 13m 35s: wenyi083126-1.stratalog.logdata.json[2935] _id=6a961282485cab4c953dc09d ts=2026-08-31T23:47:12.9540000Z -> wenyi083126-1.stratalog.logdata.json[2349] _id=6a9615b0485cab4c953dc7d1 ts=2026-09-01T00:00:48.5120000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 627 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi083126-1.stratalog.logdata.json[1374] _id=6a961778485cab4c953dcfbd ts=2026-09-01T00:08:22.1900000Z -> wenyi083126-1.stratalog.logdata.json[1373] _id=6a961778485cab4c953dcfbf ts=2026-09-01T00:08:22.1900000Z; 0ms: wenyi083126-1.stratalog.logdata.json[1375] _id=6a961778485cab4c953dcfb7 ts=2026-09-01T00:08:22.1720000Z -> wenyi083126-1.stratalog.logdata.json[1378] _id=6a961778485cab4c953dcfb9 ts=2026-09-01T00:08:22.1720000Z; 0ms: wenyi083126-1.stratalog.logdata.json[1376] _id=6a961778485cab4c953dcfb3 ts=2026-09-01T00:08:22.1720000Z -> wenyi083126-1.stratalog.logdata.json[1377] _id=6a961778485cab4c953dcfb5 ts=2026-09-01T00:08:22.1720000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 27m 6s 
  - Evidence: 27m 6s: wenyi083126-1.stratalog.logdata.json[4593] _id=6a960bdf485cab4c953dae1b ts=2026-08-31T23:18:55.9470000Z -> wenyi083126-1.stratalog.logdata.json[3121] _id=6a96123a485cab4c953dbecf ts=2026-08-31T23:46:02.2230000Z; 14m 20s: wenyi083126-1.stratalog.logdata.json[3108] _id=6a961245485cab4c953dbefd ts=2026-08-31T23:46:13.7950000Z -> wenyi083126-1.stratalog.logdata.json[2365] _id=6a9615a2485cab4c953dc7ad ts=2026-09-01T00:00:34.4380000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 13m 37s 
  - Evidence: 13m 37s: wenyi083126-1.stratalog.logdata.json[3514] _id=6a9610a0485cab4c953dba1b ts=2026-08-31T23:39:12.3760000Z -> wenyi083126-1.stratalog.logdata.json[2587] _id=6a9613d1485cab4c953dc45d ts=2026-08-31T23:52:50.0500000Z; 11m 25s: wenyi083126-1.stratalog.logdata.json[4651] _id=6a960b74485cab4c953dacfb ts=2026-08-31T23:17:08.3790000Z -> wenyi083126-1.stratalog.logdata.json[4013] _id=6a960e21485cab4c953db581 ts=2026-08-31T23:28:33.4240000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.015s shown 
  - Evidence: 4ms: wenyi083126-1.stratalog.logdata.json[4778] _id=6a960aac485cab4c953dab53 ts=2026-08-31T23:13:48.1840000Z -> wenyi083126-1.stratalog.logdata.json[4773] _id=6a960aac485cab4c953dab5f ts=2026-08-31T23:13:48.1880000Z; 14ms: wenyi083126-1.stratalog.logdata.json[4676] _id=6a960b34485cab4c953dac81 ts=2026-08-31T23:16:04.8510000Z -> wenyi083126-1.stratalog.logdata.json[4673] _id=6a960b34485cab4c953dac85 ts=2026-08-31T23:16:04.8650000Z; 15ms: wenyi083126-1.stratalog.logdata.json[4720] _id=6a960afb485cab4c953dabd9 ts=2026-08-31T23:15:07.4570000Z -> wenyi083126-1.stratalog.logdata.json[4716] _id=6a960afb485cab4c953dabdf ts=2026-08-31T23:15:07.4720000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 53m 
  - Evidence: 5h 53m: wenyi083126-1.stratalog.logdata.json[5588] _id=6a95bc3d485cab4c953d6ac4 ts=2026-08-31T17:39:09.4850000Z -> wenyi083126-1.stratalog.logdata.json[3724] _id=6a960f17485cab4c953db7c3 ts=2026-08-31T23:32:40.1890000Z; 29m 41s: wenyi083126-1.stratalog.logdata.json[3213] _id=6a9611a2485cab4c953dbd7d ts=2026-08-31T23:43:31.0330000Z -> wenyi083126-1.stratalog.logdata.json[1146] _id=6a961897485cab4c953dd2d9 ts=2026-09-01T00:13:12.1560000Z; 22m 41s: wenyi083126-1.stratalog.logdata.json[1146] _id=6a961897485cab4c953dd2d9 ts=2026-09-01T00:13:12.1560000Z -> wenyi083126-1.stratalog.logdata.json[241] _id=6a961de9485cab4c953dda69 ts=2026-09-01T00:35:53.7020000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 53m 
  - Evidence: 5h 53m: wenyi083126-1.stratalog.logdata.json[5586] _id=6a95bc3d485cab4c953d6ac8 ts=2026-08-31T17:39:09.4880000Z -> wenyi083126-1.stratalog.logdata.json[3764] _id=6a960f03485cab4c953db773 ts=2026-08-31T23:32:19.2130000Z; 29m 4s: wenyi083126-1.stratalog.logdata.json[3207] _id=6a9611a2485cab4c953dbd87 ts=2026-08-31T23:43:31.0500000Z -> wenyi083126-1.stratalog.logdata.json[1176] _id=6a961873485cab4c953dd291 ts=2026-09-01T00:12:35.8600000Z; 21m 56s: wenyi083126-1.stratalog.logdata.json[1141] _id=6a961898485cab4c953dd2e3 ts=2026-09-01T00:13:12.1730000Z -> wenyi083126-1.stratalog.logdata.json[279] _id=6a961dbc485cab4c953dda1d ts=2026-09-01T00:35:08.5300000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.014s..0.014s shown 
  - Evidence: 14ms: wenyi083126-1.stratalog.logdata.json[1144] _id=6a961898485cab4c953dd2dd ts=2026-09-01T00:13:12.1590000Z -> wenyi083126-1.stratalog.logdata.json[1141] _id=6a961898485cab4c953dd2e3 ts=2026-09-01T00:13:12.1730000Z; 14ms: wenyi083126-1.stratalog.logdata.json[3211] _id=6a9611a2485cab4c953dbd81 ts=2026-08-31T23:43:31.0360000Z -> wenyi083126-1.stratalog.logdata.json[3207] _id=6a9611a2485cab4c953dbd87 ts=2026-08-31T23:43:31.0500000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 53m 
  - Evidence: 5h 53m: wenyi083126-1.stratalog.logdata.json[5591] _id=6a95bc38485cab4c953d6ab8 ts=2026-08-31T17:39:04.3990000Z -> wenyi083126-1.stratalog.logdata.json[3759] _id=6a960f07485cab4c953db77d ts=2026-08-31T23:32:23.2320000Z; 29m 8s: wenyi083126-1.stratalog.logdata.json[3214] _id=6a9611a0485cab4c953dbd79 ts=2026-08-31T23:43:28.9980000Z -> wenyi083126-1.stratalog.logdata.json[1173] _id=6a961874485cab4c953dd299 ts=2026-09-01T00:12:37.0940000Z; 22m 3s: wenyi083126-1.stratalog.logdata.json[1148] _id=6a961894485cab4c953dd2d5 ts=2026-09-01T00:13:08.5540000Z -> wenyi083126-1.stratalog.logdata.json[274] _id=6a961dbf485cab4c953dda27 ts=2026-09-01T00:35:12.1150000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 38 interval(s) ≤ 0.014s..0.015s shown 
  - Evidence: 14ms: wenyi083126-1.stratalog.logdata.json[5656] _id=6a95bbf6485cab4c953d6a1c ts=2026-08-31T17:37:58.5200000Z -> wenyi083126-1.stratalog.logdata.json[5655] _id=6a95bbf6485cab4c953d6a1e ts=2026-08-31T17:37:58.5340000Z; 14ms: wenyi083126-1.stratalog.logdata.json[5662] _id=6a95bbf4485cab4c953d6a10 ts=2026-08-31T17:37:56.7030000Z -> wenyi083126-1.stratalog.logdata.json[5661] _id=6a95bbf4485cab4c953d6a12 ts=2026-08-31T17:37:56.7170000Z; 15ms: wenyi083126-1.stratalog.logdata.json[5652] _id=6a95bbf7485cab4c953d6a24 ts=2026-08-31T17:37:59.8540000Z -> wenyi083126-1.stratalog.logdata.json[5651] _id=6a95bbf7485cab4c953d6a26 ts=2026-08-31T17:37:59.8690000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 5h 53m 
  - Evidence: 5h 53m: wenyi083126-1.stratalog.logdata.json[5589] _id=6a95bc3b485cab4c953d6ac2 ts=2026-08-31T17:39:08.1180000Z -> wenyi083126-1.stratalog.logdata.json[3761] _id=6a960f04485cab4c953db779 ts=2026-08-31T23:32:20.6130000Z; 52m 1s: wenyi083126-1.stratalog.logdata.json[3248] _id=6a96118b485cab4c953dbd27 ts=2026-08-31T23:43:07.7550000Z -> wenyi083126-1.stratalog.logdata.json[276] _id=6a961dbd485cab4c953dda23 ts=2026-09-01T00:35:09.7480000Z; 10m 45s: wenyi083126-1.stratalog.logdata.json[3760] _id=6a960f05485cab4c953db77b ts=2026-08-31T23:32:21.5640000Z -> wenyi083126-1.stratalog.logdata.json[3249] _id=6a96118a485cab4c953dbd23 ts=2026-08-31T23:43:06.5880000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 12m 1s 
  - Evidence: 12m 1s: wenyi083126-1.stratalog.logdata.json[842] _id=6a961a81485cab4c953dd5b7 ts=2026-09-01T00:21:21.5310000Z -> wenyi083126-1.stratalog.logdata.json[383] _id=6a961d53485cab4c953dd94d ts=2026-09-01T00:33:23.4160000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 37m 
  - Evidence: 5h 37m: wenyi083126-1.stratalog.logdata.json[5976] _id=6a95b9e3485cab4c953d6774 ts=2026-08-31T17:29:07.7690000Z -> wenyi083126-1.stratalog.logdata.json[5475] _id=6a9608f4485cab4c953da5bf ts=2026-08-31T23:06:28.7800000Z; 27m 1s: wenyi083126-1.stratalog.logdata.json[5475] _id=6a9608f4485cab4c953da5bf ts=2026-08-31T23:06:28.7800000Z -> wenyi083126-1.stratalog.logdata.json[3651] _id=6a960f49485cab4c953db857 ts=2026-08-31T23:33:30.0900000Z; 25m 33s: wenyi083126-1.stratalog.logdata.json[2429] _id=6a961482485cab4c953dc62b ts=2026-08-31T23:55:46.4720000Z -> wenyi083126-1.stratalog.logdata.json[843] _id=6a961a7f485cab4c953dd5b5 ts=2026-09-01T00:21:19.5960000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 40m 
  - Evidence: 5h 40m: wenyi083126-1.stratalog.logdata.json[5567] _id=6a95bcc0485cab4c953d6bc2 ts=2026-08-31T17:41:20.8290000Z -> wenyi083126-1.stratalog.logdata.json[4479] _id=6a960c9f485cab4c953db02b ts=2026-08-31T23:22:07.3990000Z; 16m 1s: wenyi083126-1.stratalog.logdata.json[3628] _id=6a960fc7485cab4c953db889 ts=2026-08-31T23:35:36.1190000Z -> wenyi083126-1.stratalog.logdata.json[2642] _id=6a961389485cab4c953dc3db ts=2026-08-31T23:51:37.6360000Z; 14m 29s: wenyi083126-1.stratalog.logdata.json[2098] _id=6a9615ec485cab4c953dca13 ts=2026-09-01T00:01:48.7620000Z -> wenyi083126-1.stratalog.logdata.json[976] _id=6a961951485cab4c953dd4a9 ts=2026-09-01T00:16:17.8380000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 5h 40m 
  - Evidence: 5h 40m: wenyi083126-1.stratalog.logdata.json[5580] _id=6a95bc43485cab4c953d6ad6 ts=2026-08-31T17:39:15.9710000Z -> wenyi083126-1.stratalog.logdata.json[4499] _id=6a960c12485cab4c953daf15 ts=2026-08-31T23:19:46.2540000Z; 17m 52s: wenyi083126-1.stratalog.logdata.json[3649] _id=6a960f50485cab4c953db85b ts=2026-08-31T23:33:36.7100000Z -> wenyi083126-1.stratalog.logdata.json[2649] _id=6a961380485cab4c953dc3cb ts=2026-08-31T23:51:28.9720000Z; 14m 17s: wenyi083126-1.stratalog.logdata.json[2099] _id=6a9615ea485cab4c953dca11 ts=2026-09-01T00:01:46.4700000Z -> wenyi083126-1.stratalog.logdata.json[978] _id=6a961944485cab4c953dd4a5 ts=2026-09-01T00:16:04.4110000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 5h 23m 
  - Evidence: 5h 23m: wenyi083126-1.stratalog.logdata.json[5499] _id=6a95bd5f485cab4c953d6cc8 ts=2026-08-31T17:43:59.3740000Z -> wenyi083126-1.stratalog.logdata.json[5455] _id=6a96093a485cab4c953da5e7 ts=2026-08-31T23:07:38.4070000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi083126-1.stratalog.logdata.json[191] _id=6a961e20485cab4c953ddacb ts=2026-09-01T00:36:48.2100000Z -> wenyi083126-1.stratalog.logdata.json[192] _id=6a961e20485cab4c953ddacd ts=2026-09-01T00:36:48.2100000Z; 0ms: wenyi083126-1.stratalog.logdata.json[5683] _id=6a95bbda485cab4c953d69d6 ts=2026-08-31T17:37:30.0920000Z -> wenyi083126-1.stratalog.logdata.json[5684] _id=6a95bbda485cab4c953d69d8 ts=2026-08-31T17:37:30.0920000Z; 1ms: wenyi083126-1.stratalog.logdata.json[1647] _id=6a9616fd485cab4c953dcd99 ts=2026-09-01T00:06:21.8730000Z -> wenyi083126-1.stratalog.logdata.json[1646] _id=6a9616fd485cab4c953dcd9b ts=2026-09-01T00:06:21.8740000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5587] _id=6a95bc3d485cab4c953d6ac6 ts=2026-08-31T17:39:09.4870000Z`; `wenyi083126-1.stratalog.logdata.json[240] _id=6a961de9485cab4c953dda6b ts=2026-09-01T00:35:53.7040000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5699] _id=6a95bbca485cab4c953d69ac ts=2026-08-31T17:37:14.7320000Z`; `wenyi083126-1.stratalog.logdata.json[5563] _id=6a95bcc3485cab4c953d6bd4 ts=2026-08-31T17:41:23.6700000Z`; `wenyi083126-1.stratalog.logdata.json[4655] _id=6a960b67485cab4c953dacdd ts=2026-08-31T23:16:55.9730000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `wenyi083126-1.stratalog.logdata.json[2992] _id=6a961276485cab4c953dc021 ts=2026-08-31T23:47:01.8000000Z`; `wenyi083126-1.stratalog.logdata.json[2987] _id=6a961276485cab4c953dc023 ts=2026-08-31T23:47:02.2340000Z`; `wenyi083126-1.stratalog.logdata.json[2982] _id=6a961277485cab4c953dc02f ts=2026-08-31T23:47:03.2340000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5401] _id=6a96098d485cab4c953da693 ts=2026-08-31T23:08:21.6100000Z`; `wenyi083126-1.stratalog.logdata.json[5392] _id=6a96098e485cab4c953da6a5 ts=2026-08-31T23:08:21.6290000Z`; `wenyi083126-1.stratalog.logdata.json[5180] _id=6a9609a1485cab4c953da815 ts=2026-08-31T23:09:20.2050000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `wenyi083126-1.stratalog.logdata.json[4676] _id=6a960b34485cab4c953dac81 ts=2026-08-31T23:16:04.8510000Z`; `wenyi083126-1.stratalog.logdata.json[4673] _id=6a960b34485cab4c953dac85 ts=2026-08-31T23:16:04.8650000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi083126-1.stratalog.logdata.json[3207] _id=6a9611a2485cab4c953dbd87 ts=2026-08-31T23:43:31.0500000Z`; `wenyi083126-1.stratalog.logdata.json[1141] _id=6a961898485cab4c953dd2e3 ts=2026-09-01T00:13:12.1730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5661] _id=6a95bbf4485cab4c953d6a12 ts=2026-08-31T17:37:56.7170000Z`; `wenyi083126-1.stratalog.logdata.json[5655] _id=6a95bbf6485cab4c953d6a1e ts=2026-08-31T17:37:58.5340000Z`; `wenyi083126-1.stratalog.logdata.json[5651] _id=6a95bbf7485cab4c953d6a26 ts=2026-08-31T17:37:59.8690000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `wenyi083126-1.stratalog.logdata.json[842] _id=6a961a81485cab4c953dd5b7 ts=2026-09-01T00:21:21.5310000Z`; `wenyi083126-1.stratalog.logdata.json[383] _id=6a961d53485cab4c953dd94d ts=2026-09-01T00:33:23.4160000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `wenyi083126-1.stratalog.logdata.json[4779] _id=6a960aac485cab4c953dab55 ts=2026-08-31T23:13:48.1840000Z`; `wenyi083126-1.stratalog.logdata.json[4774] _id=6a960aac485cab4c953dab5d ts=2026-08-31T23:13:48.1880000Z`; `wenyi083126-1.stratalog.logdata.json[4721] _id=6a960afb485cab4c953dabd7 ts=2026-08-31T23:15:07.4560000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 22 occurrence(s) 
  - Examples: `wenyi083126-1.stratalog.logdata.json[4428] _id=6a960ca8485cab4c953db099 ts=2026-08-31T23:22:15.5250000Z`; `wenyi083126-1.stratalog.logdata.json[4427] _id=6a960ca9485cab4c953db09b ts=2026-08-31T23:22:15.5250000Z`; `wenyi083126-1.stratalog.logdata.json[4418] _id=6a960caa485cab4c953db0ab ts=2026-08-31T23:22:16.8600000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 68 occurrence(s) 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5407] _id=6a96098d485cab4c953da68b ts=2026-08-31T23:08:21.5790000Z`; `wenyi083126-1.stratalog.logdata.json[5396] _id=6a96098e485cab4c953da69b ts=2026-08-31T23:08:21.6120000Z`; `wenyi083126-1.stratalog.logdata.json[5395] _id=6a96098e485cab4c953da6a1 ts=2026-08-31T23:08:21.6120000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `wenyi083126-1.stratalog.logdata.json[4778] _id=6a960aac485cab4c953dab53 ts=2026-08-31T23:13:48.1840000Z`; `wenyi083126-1.stratalog.logdata.json[4773] _id=6a960aac485cab4c953dab5f ts=2026-08-31T23:13:48.1880000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5609] _id=6a95bc22485cab4c953d6a80 ts=2026-08-31T17:38:42.9060000Z`; `wenyi083126-1.stratalog.logdata.json[5607] _id=6a95bc23485cab4c953d6a84 ts=2026-08-31T17:38:43.3560000Z`; `wenyi083126-1.stratalog.logdata.json[5590] _id=6a95bc3b485cab4c953d6aba ts=2026-08-31T17:39:07.3170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Open' (totals: 21 open, 21 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'DialogueStartEvent' (totals: 321 start, 318 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'BecameCameraCentered' (totals: 176 open, 182 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 22 unmatched 'BecameVisible' (totals: 337 open, 323 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 13 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 6 unmatched 'questActiveEvent' (totals: 37 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 161 of 5976 adjacent _id pairs reverse in client time; worst 40.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi083126-1.stratalog.logdata.json[5301] _id=6a96098e485cab4c953da69d ts=2026-08-31T23:09:02.3130000Z`; `wenyi083126-1.stratalog.logdata.json[5397] _id=6a96098e485cab4c953da69f ts=2026-08-31T23:08:21.6120000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.17s, min -41.48s, max +0.22s over 5977 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\gameplay-logs-test\config\coverage\08-31-26.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Single full playthrough by one tester (log shows EndOfUnit for units 1-5). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data

## 9. Event-Type Details

### `InputEvent` — 1883 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (400); Unit 4 Dev - Dungeon (387); Unit 3 Dev (263); Unit 5 Dev - Dungeon (261); Unit 3 Dungeon Dev (182); Unit 4 Dev (150); Unit 1 Dev (119); Unit 5 Dev (70); Unit 4 Dev - Anderson Base (51)
- **Intervals:** median 0.50s (p5 0.05s / p95 12.97s, n=1882)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1883/1883 records)
    "pressed"  x1883
data.actionType  (string, 1883/1883 records)
    "Move"  x1357
    "Sprint"  x235
    "Interact"  x212
    "Ascend"  x28
    "Jump"  x15
    "Descend"  x13
    "Hoverboard"  x13
    "Map"  x10
data.key  (string, 1883/1883 records, 1 empty-string)
    "w"  x512
    "a"  x303
    "s"  x286
    "d"  x256
    "leftShift"  x248
    "leftButton"  x204
    "space"  x34
    "e"  x17
    "h"  x12
    "m"  x10
    ""  x1
data.playerOrDrone  (string, 1883/1883 records)
    "Player"  x1593
    "Drone"  x290
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1775 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (493); Unit 3 Dev (273); Unit 4 Dev (232); Unit 5 Dev (209); Unit 1 Dev (193); Unit 3 Dungeon Dev (119); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (84); Unit 4 Dev - Anderson Base (73)
- **eventKey:** present on 1136 of 1775 records
- **Intervals:** median 0.68s (p5 0.00s / p95 16.31s, n=1774)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1136; [conversationId, dialogueEventType] x639
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1775/1775 records)
    numeric range 8 .. 118 (52 unique)
data.dialogueEventType  (string, 1775/1775 records)
    "DialogueNodeEvent"  x1136
    "DialogueStartEvent"  x321
    "DialogueFinishEvent"  x318
data.nodeId  (number, 1136/1775 records)
    numeric range 0 .. 290 (220 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PuzzlePieceVisibleEvent` — 1018 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (622); Unit 4 Dev (284); Unit 3 Dungeon Dev (112)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.18s, n=1017)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1018/1018 records)
    "BecameVisible"  x337
    "BecameInvisible"  x323
    "BecameCameraUncentered"  x182
    "BecameCameraCentered"  x176
data.pieceId  (string, 1018/1018 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1018/1018 records)
    764 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 655 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (156); Unit 4 Dev (97); Unit 3 Dev (96); Unit 1 Dev (93); Unit 5 Dev - Dungeon (72); Unit 5 Dev (49); Unit 4 Dev - Dungeon (37); Unit 3 Dungeon Dev (35); Unit 4 Dev - Anderson Base (20)
- **Intervals:** median 10.01s (p5 9.99s / p95 10.01s, n=643)
- **Fields under `data`:**

```text
data.position  (object, 655/655 records)
data.position.x  (number, 655/655 records)
    numeric range -689.691 .. 1558.42 (286 unique)
data.position.y  (number, 655/655 records)
    numeric range -114.205 .. 219.284 (242 unique)
data.position.z  (number, 655/655 records)
    numeric range -1027.14 .. 1804.61 (286 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 166 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (57); Unit 2 Prod (Refactor) (26); Unit 3 Dungeon Dev (23); Unit 4 Dev (15); Unit 1 Dev (13); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (6); Unit 5 Dev - Dungeon (6)
- **Intervals:** median 7.05s (p5 1.66s / p95 193.71s, n=165)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 166/166 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 166/166 records)
    101 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 155 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (42); Unit 2 Prod (Refactor) (33); Unit 3 Dev (31); Unit 5 Dev (26); Unit 4 Dev - Anderson Base (23)
- **Intervals:** median 0.25s (p5 0.02s / p95 8.62s, n=154)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 155/155 records)
    "argumentationNodeHoverEnd"  x68
    "argumentationNodeHoverStart"  x65
    "argumentationNodeAdd"  x20
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 155/155 records)
    "Unit 2 – Watershed"  x33
    "Unit 1 - Freshwater"  x31
    "Unit 3 - Pollution Upstream"  x31
    "Unit 5"  x26
    "Unit 4 - Flooding"  x23
    "Unit 1 - Argumentation Tutorial"  x11
data.nodeName  (string, 155/155 records)
    "A"  x35
    "II"  x27
    "I"  x21
    "D"  x14
    "1"  x13
    "B"  x12
    "C"  x12
    "2"  x9
    "3"  x5
    "4"  x4
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 68 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 68 of 68 records
- **Intervals:** median 64.48s (p5 0.00s / p95 295.20s, n=67)
- **`data` key-set variants:** [questEventType, questID, questName] x37; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 68/68 records)
    "questActiveEvent"  x37
    "questFinishEvent"  x31
data.questID  (string, 68/68 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 68/68 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/68 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 63 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (43); Unit 3 Dev (20)
- **Intervals:** median 2.48s (p5 0.04s / p95 283.28s, n=62)
- **`data` key-set variants:** [actionType, featureUsed] x34; [actionType, featureUsed, location] x29
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 63/63 records)
    "WaypointMoveEvent"  x23
    "MapCloseEvent"  x18
    "MapOpenEvent"  x16
    "WaypointSetEvent"  x4
    "WaypointResetEvent"  x2
data.featureUsed  (string, 63/63 records)
    "Map"  x34
    "Waypoint"  x29
data.location  (object, 29/63 records)
data.location.x  (number, 29/63 records)
    numeric range -272.258 .. 635.539 (21 unique)
data.location.y  (number, 29/63 records)
    numeric range -150.538 .. 135.021 (22 unique)
data.location.z  (number, 29/63 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DaniEvent` — 42 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (20); Unit 2 Prod (Refactor) (18); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 14.09s (p5 0.02s / p95 1115.59s, n=41)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "Close"  x21
    "Open"  x21
data.toolName  (string, 42/42 records)
    "Map"  x34
    "Argumentation"  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `Soil Key Puzzle` — 32 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (12); Unit 4 Dev (8)
- **Intervals:** median 0.62s (p5 0.42s / p95 653.45s, n=31)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x24; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/32 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/32 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 24/32 records)
    "RightDrag"  x15
    "LeftDrag"  x9
data.currentSoilType  (string, 24/32 records)
    "CLAY"  x5
    "CLAYROCK"  x4
    "CLAYSAND"  x4
    "SAND"  x4
    "SANDGRAVEL"  x4
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 24/32 records)
    "false"  x19
    "true"  x5
data.waterLevelStatus  (string, 24/32 records)
    "TooHigh"  x12
    "Proper"  x9
    "TooLow"  x3
data.waterRetentionChange  (string, 24/32 records)
    "Decrease"  x10
    "Increase"  x9
    "NoChange"  x5
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 18 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (18)
- **Intervals:** median 16.30s (p5 4.09s / p95 57.34s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "On"  x14
    "Off"  x4
data.floor  (string, 18/18 records)
    "4"  x7
    "3"  x6
    "2"  x3
    "1"  x2
data.machineNumber  (string, 18/18 records)
    "One"  x17
    "Two"  x1
data.machineType  (string, 18/18 records)
    "Condenser"  x9
    "Evaporator"  x6
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 18/18 records)
    "2"  x6
    "3"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 18 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 5 Dev (5); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 1.10s (p5 0.32s / p95 6736.09s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x5
data.argumentationTitle  (string, 18/18 records)
    "Unit 1 - Freshwater"  x7
    "Unit 5"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 18/18 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowFocusEvent` — 18 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 1 Dev (5); Unit 5 Dev - Dungeon (5); Unit 3 Dev (2); Unit 4 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 199.21s (p5 26.60s / p95 4858.53s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 18 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (5); Unit 5 Dev - Dungeon (5); Unit 3 Dev (2); Unit 4 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 216.72s (p5 31.10s / p95 4943.87s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    false  x18
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 36.30s (p5 0.01s / p95 9522.78s, n=13)
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

### `argumentationAnswerEvent` — 7 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 1006.20s (p5 28.98s / p95 16353.31s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "submitAnswerEvent"  x7
data.answerSubmitted  (string, 7/7 records)
    "A,1,I"  x2
    "A,1,II"  x2
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "C,D,3,II"  x1
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
    "Unit 4 - Flooding"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 4.72s (p5 1.41s / p95 19.77s, n=5)
- **`data` key-set variants:** [actionType, boxID, soilType] x3; [actionType, boxId, soilType] x3
- **Open findings:** 2 — see sections 5-8
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1432.51s (p5 1245.84s / p95 18015.45s, n=4)
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

### `gameStartEvent` — 5 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (5)
- **Intervals:** median 1577.22s (p5 1365.89s / p95 17448.06s, n=4)
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
- **Intervals:** median 37.41s (p5 11.53s / p95 65.13s, n=4)
- **Open findings:** 1 — see sections 5-8
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
- **Intervals:** median 2.33s (p5 2.14s / p95 2.73s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 721.88s (p5 721.88s / p95 721.88s, n=1)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot gameplay-logs-test\reports\08-25-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DEBUGMenu` : expected event type absent although its content was played — possible logging failure
- `DialogueEvent` : exact duplicate records (same timestamp, scene and data)
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : event type present in baseline 08-25-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : baseline field(s) absent this build
- `chatEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DaniEvent` actionType: tool open/close: close without preceding open
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (23x); "WaypointResetEvent" (2x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (29x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)


---
*Generated by gameplay-logs-test / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*