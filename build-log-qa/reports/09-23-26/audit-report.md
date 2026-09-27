# MHS Gameplay Log Audit Report — build 09-23-26

## 1. Build Information

- **Build ID:** 09-23-26
- **Game version string(s) in log:** 20260914-
- **Audit date:** 2026-09-26
- **Log file(s):** wenyi09232026.stratalog.logdata.json
- **Records:** 11648 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab42757bf592cbac358b8c1
- **Time span:** 2026-09-25T20:06:09.050000+00:00 .. 2026-09-25T23:55:02.153000+00:00 (3h 48m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-23-26.yaml
- **Baseline:** snapshot build-log-qa\reports\09-14-26-3\snapshot.json

## 2. Executive Summary

- **22 event types**, 11648 records, 11 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 82 INFO, 0 NOT_TESTED, 97 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `argumentationNodeEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DaniEvent`: event type present in baseline 09-14-26-3 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5172 | 44.4 | 1 | 4 | 0 | 2026-09-25T20:40:47.260000+00:00 | 2026-09-25T23:28:44.899000+00:00 | 2h 47m |
| InputEvent | 2411 | 20.7 | 1 | 9 | 0 | 2026-09-25T20:09:28.592000+00:00 | 2026-09-25T23:55:02.153000+00:00 | 3h 45m |
| DialogueEvent | 1943 | 16.68 | 1 | 9 | 1220 | 2026-09-25T20:06:31.144000+00:00 | 2026-09-25T23:54:59.700000+00:00 | 3h 48m |
| PlayerPositionEvent | 1304 | 11.2 | 1 | 9 | 0 | 2026-09-25T20:06:14.610000+00:00 | 2026-09-25T23:55:00.316000+00:00 | 3h 48m |
| ObjectInterEvent | 235 | 2.02 | 1 | 9 | 0 | 2026-09-25T20:10:17.733000+00:00 | 2026-09-25T23:55:02.152000+00:00 | 3h 44m |
| argumentationNodeEvent | 140 | 1.2 | 1 | 5 | 0 | 2026-09-25T20:25:04.353000+00:00 | 2026-09-25T23:42:38.205000+00:00 | 3h 17m |
| TopographicMapEvent | 83 | 0.71 | 1 | 2 | 0 | 2026-09-25T20:41:05.752000+00:00 | 2026-09-25T22:26:01.828000+00:00 | 1h 44m |
| gameWindowFocusEvent | 82 | 0.7 | 1 | 11 | 0 | 2026-09-25T20:06:09.050000+00:00 | 2026-09-25T23:41:55.584000+00:00 | 3h 35m |
| gameWindowUnfocusEvent | 76 | 0.65 | 1 | 10 | 0 | 2026-09-25T20:06:18.525000+00:00 | 2026-09-25T23:41:48.321000+00:00 | 3h 35m |
| questEvent | 71 | 0.61 | 1 | 9 | 71 | 2026-09-25T20:06:31.140000+00:00 | 2026-09-25T23:51:03.135000+00:00 | 3h 44m |
| Soil Key Puzzle | 38 | 0.33 | 1 | 3 | 0 | 2026-09-25T20:48:08.306000+00:00 | 2026-09-25T22:34:02.978000+00:00 | 1h 45m |
| WaterChamberEvent | 20 | 0.17 | 1 | 1 | 0 | 2026-09-25T23:28:01.417000+00:00 | 2026-09-25T23:35:36.300000+00:00 | 7m 34s |
| argumentationEvent | 14 | 0.12 | 1 | 5 | 0 | 2026-09-25T20:25:54.141000+00:00 | 2026-09-25T23:42:39.278000+00:00 | 3h 16m |
| DEBUGMenu | 12 | 0.1 | 1 | 8 | 0 | 2026-09-25T20:06:14.608000+00:00 | 2026-09-25T23:20:57.367000+00:00 | 3h 14m |
| TerasGardenBox | 11 | 0.09 | 1 | 1 | 0 | 2026-09-25T23:10:50.762000+00:00 | 2026-09-25T23:12:15.669000+00:00 | 1m 24s |
| argumentationToolEvent | 9 | 0.08 | 1 | 4 | 0 | 2026-09-25T20:27:46.819000+00:00 | 2026-09-25T23:41:30.722000+00:00 | 3h 13m |
| gameStartEvent | 6 | 0.05 | 1 | 1 | 0 | 2026-09-25T20:06:09.051000+00:00 | 2026-09-25T23:20:54.330000+00:00 | 3h 14m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-09-25T20:30:50.816000+00:00 | 2026-09-25T23:55:02.150000+00:00 | 3h 24m |
| argumentationAnswerEvent | 5 | 0.04 | 1 | 5 | 0 | 2026-09-25T20:28:09.047000+00:00 | 2026-09-25T23:42:39.272000+00:00 | 3h 14m |
| soilMachine | 5 | 0.04 | 1 | 1 | 0 | 2026-09-25T22:44:22.710000+00:00 | 2026-09-25T22:50:10.178000+00:00 | 5m 47s |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-09-25T23:48:41.448000+00:00 | 2026-09-25T23:48:47.023000+00:00 | 5.6s |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-09-25T23:20:57.337000+00:00 | 2026-09-25T23:36:21.714000+00:00 | 15m 24s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DaniEvent` — event type present in baseline 09-14-26-3 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 4.06s median 
  - Expected: 1.434s in 09-14-26-3 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 19.608s median 
  - Expected: 6.144s in 09-14-26-3 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 3024.27s median 
  - Expected: 20.302s in 09-14-26-3 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 66.927s median 
  - Expected: 158.479s in 09-14-26-3 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 0.467s median 
  - Expected: 0.218s in 09-14-26-3 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 62.313s median 
  - Expected: 1.434s in 09-14-26-3 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: PodsEscapingCopernicus Cutscene 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to pick up 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Hot 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Cold 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Covered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Uncovered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted In 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted Out 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Covered; Hot; Tilted In 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Cold; Tilted Out; Uncovered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: WaypointResetEvent 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: Water 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
  - Expected: 37 in 09-14-26-3 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: ; 2,I; A,2,I; A,2,II; A,3,I; A,B,1,I; A,B,2,I; A,B,3,I; A,B,4,I; A,D,C,2,II; B,1,I; B,1,II; B,4,II; B,C,1,I; C,1,I; C,1,II; C,3,II; C,4,II; C,D,3,II; D,1,I; D,1,II; D,2,II; D,3,I; D,4,I; D,4,II; D,A,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 140 records 
  - Expected: 504 in 09-14-26-3 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeRemove 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationToolClose 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 2 – Watershed 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
  - Expected: 43 in 09-14-26-3 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Bedrock 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 17 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi09232026.stratalog.logdata.json[11492] _id=6ab6d58d485cab4c95635c8d ts=2026-09-25T20:11:57.3120000Z`; `wenyi09232026.stratalog.logdata.json[11433] _id=6ab6d669485cab4c9563bd30 ts=2026-09-25T20:15:37.5390000Z`; `wenyi09232026.stratalog.logdata.json[11401] _id=6ab6d6bf485cab4c9563de36 ts=2026-09-25T20:17:04.1220000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 6 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 6} 
  - Examples: `wenyi09232026.stratalog.logdata.json[11646] _id=6ab6d431485cab4c9562d53c ts=2026-09-25T20:06:09.0510000Z`; `wenyi09232026.stratalog.logdata.json[11114] _id=6ab6dbaa485cab4c956591d8 ts=2026-09-25T20:38:02.3820000Z`; `wenyi09232026.stratalog.logdata.json[8620] _id=6ab6e037485cab4c95669ede ts=2026-09-25T20:57:27.3850000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 82 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 82} 
  - Examples: `wenyi09232026.stratalog.logdata.json[11647] _id=6ab6d430485cab4c9562d531 ts=2026-09-25T20:06:09.0500000Z`; `wenyi09232026.stratalog.logdata.json[11642] _id=6ab6d43e485cab4c9562da5a ts=2026-09-25T20:06:23.2160000Z`; `wenyi09232026.stratalog.logdata.json[11618] _id=6ab6d4ab485cab4c95630054 ts=2026-09-25T20:08:12.0710000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 76 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 76} 
  - Examples: `wenyi09232026.stratalog.logdata.json[11643] _id=6ab6d43a485cab4c9562d8b4 ts=2026-09-25T20:06:18.5250000Z`; `wenyi09232026.stratalog.logdata.json[11619] _id=6ab6d4a6485cab4c9562fe70 ts=2026-09-25T20:08:06.6510000Z`; `wenyi09232026.stratalog.logdata.json[11541] _id=6ab6d532485cab4c956330b5 ts=2026-09-25T20:10:26.2850000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 5 of 83 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `wenyi09232026.stratalog.logdata.json[10998] _id=6ab6dc61485cab4c9565c1fb ts=2026-09-25T20:41:05.7520000Z`; `wenyi09232026.stratalog.logdata.json[10988] _id=6ab6dc76485cab4c9565c791 ts=2026-09-25T20:41:26.2290000Z`; `wenyi09232026.stratalog.logdata.json[8647] _id=6ab6dfaa485cab4c9566820f ts=2026-09-25T20:55:06.6940000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5171 | 0.0 | 0.018 | 1.949 | 0.691 | 2594.945 | 30.79 | 3541 | 5 |
| InputEvent | 2410 | 0.0 | 0.583 | 5.616 | 20.674 | 498.983 | 10.68 | 71 | 0 |
| DialogueEvent | 1942 | 0.0 | 3.7 | 7.059 | 21.911 | 441.229 | 8.5 | 574 | 0 |
| PlayerPositionEvent | 1292 | 9.984 | 10.005 | 10.16 | 10.006 | 121.211 | 5.91 | 0 | 0 |
| ObjectInterEvent | 234 | 0.0 | 5.979 | 57.626 | 369.204 | 1346.313 | 1.04 | 3 | 4 |
| argumentationNodeEvent | 139 | 0.0 | 0.467 | 85.28 | 19.599 | 4392.918 | 0.7 | 30 | 4 |
| TopographicMapEvent | 82 | 0.003 | 1.827 | 76.781 | 384.036 | 1358.368 | 0.78 | 2 | 4 |
| gameWindowFocusEvent | 81 | 1.69 | 95.83 | 159.834 | 450.583 | 1015.768 | 0.38 | 0 | 1 |
| gameWindowUnfocusEvent | 75 | 1.802 | 108.82 | 172.397 | 460.612 | 1010.461 | 0.35 | 0 | 2 |
| questEvent | 70 | 0.0 | 147.974 | 192.457 | 549.228 | 914.298 | 0.31 | 13 | 3 |
| Soil Key Puzzle | 37 | 0.166 | 0.8 | 171.748 | 1424.207 | 3219.303 | 0.35 | 0 | 3 |
| WaterChamberEvent | 19 | 1.535 | 19.608 | 23.941 | 69.193 | 96.581 | 2.51 | 0 | 0 |
| argumentationEvent | 13 | 0.014 | 66.927 | 908.087 | 4000.897 | 4377.158 | 0.07 | 2 | 4 |
| DEBUGMenu | 11 | 434.287 | 795.292 | 1062.069 | 2402.3 | 2891.543 | 0.06 | 0 | 9 |
| TerasGardenBox | 10 | 1.033 | 4.06 | 8.491 | 22.456 | 23.529 | 7.07 | 0 | 0 |
| argumentationToolEvent | 8 | 0.9 | 17.074 | 1452.988 | 5429.7 | 5980.927 | 0.04 | 0 | 3 |
| gameStartEvent | 5 | 1165.003 | 2479.84 | 2337.056 | 3166.848 | 3235.712 | 0.03 | 0 | 5 |
| EndOfUnit | 4 | 2084.846 | 2855.05 | 3062.834 | 4272.263 | 4456.389 | 0.02 | 0 | 4 |
| argumentationAnswerEvent | 4 | 1220.413 | 3024.27 | 2917.556 | 4325.605 | 4401.272 | 0.02 | 0 | 4 |
| soilMachine | 4 | 11.839 | 62.313 | 86.867 | 194.877 | 211.002 | 0.69 | 0 | 0 |
| SolarStillDesignEvent | 3 | 1.501 | 1.823 | 1.858 | 2.208 | 2.251 | 32.29 | 0 | 0 |
| chatEvent | 1 | 924.377 | 924.377 | 924.377 | 924.377 | 924.377 | 0.06 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi09232026.stratalog.logdata.json[2318] _id=6ab6f94f485cab4c9566f80b ts=2026-09-25T22:44:31.2150000Z == wenyi09232026.stratalog.logdata.json[2319] _id=6ab6f94f485cab4c9566f80d ts=2026-09-25T22:44:31.2150000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi09232026.stratalog.logdata.json[1776] _id=6ab6fd36485cab4c9566ffa3 ts=2026-09-25T23:01:11.0180000Z == wenyi09232026.stratalog.logdata.json[1775] _id=6ab6fd36485cab4c9566ffa5 ts=2026-09-25T23:01:11.0180000Z`; `wenyi09232026.stratalog.logdata.json[1740] _id=6ab6fd79485cab4c95670021 ts=2026-09-25T23:02:17.7660000Z == wenyi09232026.stratalog.logdata.json[1741] _id=6ab6fd79485cab4c95670023 ts=2026-09-25T23:02:17.7660000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 102 group(s), 144 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi09232026.stratalog.logdata.json[10939] _id=6ab6dc9f485cab4c9565d2d2 ts=2026-09-25T20:42:05.1600000Z == wenyi09232026.stratalog.logdata.json[10940] _id=6ab6dc9f485cab4c9565d2e0 ts=2026-09-25T20:42:05.1600000Z`; `wenyi09232026.stratalog.logdata.json[10717] _id=6ab6dcbc485cab4c9565db6a ts=2026-09-25T20:42:33.6760000Z == wenyi09232026.stratalog.logdata.json[10719] _id=6ab6dcbc485cab4c9565db6c ts=2026-09-25T20:42:33.6760000Z`; `wenyi09232026.stratalog.logdata.json[10713] _id=6ab6dcbc485cab4c9565db93 ts=2026-09-25T20:42:33.7420000Z == wenyi09232026.stratalog.logdata.json[10712] _id=6ab6dcbc485cab4c9565db9a ts=2026-09-25T20:42:33.7420000Z`
- **WARNING / Medium** `argumentationNodeEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi09232026.stratalog.logdata.json[1637] _id=6ab6fe86485cab4c956701d3 ts=2026-09-25T23:06:46.6930000Z == wenyi09232026.stratalog.logdata.json[1636] _id=6ab6fe86485cab4c956701d5 ts=2026-09-25T23:06:46.6930000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi09232026.stratalog.logdata.json[219] _id=6ab70743485cab4c956713ed ts=2026-09-25T23:44:04.2490000Z == wenyi09232026.stratalog.logdata.json[218] _id=6ab70744485cab4c956713ef ts=2026-09-25T23:44:04.2490000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi09232026.stratalog.logdata.json[11546] _id=6ab6d529485cab4c95632d87 ts=2026-09-25T20:10:17.7330000Z ~ wenyi09232026.stratalog.logdata.json[11545] _id=6ab6d529485cab4c95632d89 ts=2026-09-25T20:10:17.7340000Z`; `184ms: wenyi09232026.stratalog.logdata.json[10151] _id=6ab6dd07485cab4c9565ee70 ts=2026-09-25T20:43:51.9060000Z ~ wenyi09232026.stratalog.logdata.json[10149] _id=6ab6dd07485cab4c9565ee85 ts=2026-09-25T20:43:52.0900000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 156 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `400ms: wenyi09232026.stratalog.logdata.json[10914] _id=6ab6dca9485cab4c9565d5a9 ts=2026-09-25T20:42:16.8160000Z ~ wenyi09232026.stratalog.logdata.json[10913] _id=6ab6dca9485cab4c9565d5ab ts=2026-09-25T20:42:17.2160000Z`; `15ms: wenyi09232026.stratalog.logdata.json[10848] _id=6ab6dcb2485cab4c9565d825 ts=2026-09-25T20:42:24.6540000Z ~ wenyi09232026.stratalog.logdata.json[10847] _id=6ab6dcb2485cab4c9565d828 ts=2026-09-25T20:42:24.6690000Z`; `16ms: wenyi09232026.stratalog.logdata.json[10844] _id=6ab6dcb2485cab4c9565d82e ts=2026-09-25T20:42:24.9540000Z ~ wenyi09232026.stratalog.logdata.json[10843] _id=6ab6dcb2485cab4c9565d834 ts=2026-09-25T20:42:24.9700000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: wenyi09232026.stratalog.logdata.json[8516] _id=6ab6e0fb485cab4c9566ac9b ts=2026-09-25T21:00:44.1130000Z ~ wenyi09232026.stratalog.logdata.json[8512] _id=6ab6e0fc485cab4c9566aca3 ts=2026-09-25T21:00:44.1160000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: wenyi09232026.stratalog.logdata.json[5131] _id=6ab6ef4e485cab4c9566d8c7 ts=2026-09-25T22:01:50.7350000Z ~ wenyi09232026.stratalog.logdata.json[5128] _id=6ab6ef4e485cab4c9566d8cd ts=2026-09-25T22:01:50.7490000Z`; `14ms: wenyi09232026.stratalog.logdata.json[1633] _id=6ab6fe87485cab4c956701db ts=2026-09-25T23:06:47.5630000Z ~ wenyi09232026.stratalog.logdata.json[1630] _id=6ab6fe87485cab4c956701e1 ts=2026-09-25T23:06:47.5770000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `100ms: wenyi09232026.stratalog.logdata.json[5800] _id=6ab6ea7c485cab4c9566cea1 ts=2026-09-25T21:41:16.7120000Z ~ wenyi09232026.stratalog.logdata.json[5798] _id=6ab6ea7c485cab4c9566cea5 ts=2026-09-25T21:41:16.8120000Z`; `100ms: wenyi09232026.stratalog.logdata.json[5799] _id=6ab6ea7c485cab4c9566cea3 ts=2026-09-25T21:41:16.7290000Z ~ wenyi09232026.stratalog.logdata.json[5797] _id=6ab6ea7c485cab4c9566cea7 ts=2026-09-25T21:41:16.8290000Z`; `551ms: wenyi09232026.stratalog.logdata.json[5150] _id=6ab6ef38485cab4c9566d88b ts=2026-09-25T22:01:28.4210000Z ~ wenyi09232026.stratalog.logdata.json[5147] _id=6ab6ef38485cab4c9566d891 ts=2026-09-25T22:01:28.9720000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi09232026.stratalog.logdata.json[100] _id=6ab7089d485cab4c956715e7 ts=2026-09-25T23:49:49.8650000Z ~ wenyi09232026.stratalog.logdata.json[99] _id=6ab7089d485cab4c956715e9 ts=2026-09-25T23:49:49.8660000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 48m 11s 
  - Evidence: 48m 11s: wenyi09232026.stratalog.logdata.json[8618] _id=6ab6e039485cab4c95669f4d ts=2026-09-25T20:57:29.5630000Z -> wenyi09232026.stratalog.logdata.json[5702] _id=6ab6eb84485cab4c9566d079 ts=2026-09-25T21:45:41.1060000Z; 31m 53s: wenyi09232026.stratalog.logdata.json[11645] _id=6ab6d436485cab4c9562d739 ts=2026-09-25T20:06:14.6080000Z -> wenyi09232026.stratalog.logdata.json[11113] _id=6ab6dbaf485cab4c95659318 ts=2026-09-25T20:38:07.6640000Z; 19m 48s: wenyi09232026.stratalog.logdata.json[5702] _id=6ab6eb84485cab4c9566d079 ts=2026-09-25T21:45:41.1060000Z -> wenyi09232026.stratalog.logdata.json[5017] _id=6ab6f028485cab4c9566da81 ts=2026-09-25T22:05:29.1300000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 574 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi09232026.stratalog.logdata.json[11068] _id=6ab6dc17485cab4c9565aefd ts=2026-09-25T20:39:51.3870000Z -> wenyi09232026.stratalog.logdata.json[11067] _id=6ab6dc17485cab4c9565af03 ts=2026-09-25T20:39:51.3870000Z; 0ms: wenyi09232026.stratalog.logdata.json[11126] _id=6ab6d9e6485cab4c95651e8e ts=2026-09-25T20:30:30.8280000Z -> wenyi09232026.stratalog.logdata.json[11127] _id=6ab6d9e6485cab4c95651e95 ts=2026-09-25T20:30:30.8280000Z; 0ms: wenyi09232026.stratalog.logdata.json[11158] _id=6ab6d9ba485cab4c956513d2 ts=2026-09-25T20:29:46.7400000Z -> wenyi09232026.stratalog.logdata.json[11159] _id=6ab6d9ba485cab4c956513d9 ts=2026-09-25T20:29:46.7400000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 1h 14m 
  - Evidence: 1h 14m: wenyi09232026.stratalog.logdata.json[11118] _id=6ab6d9fa485cab4c956523d7 ts=2026-09-25T20:30:50.8160000Z -> wenyi09232026.stratalog.logdata.json[5706] _id=6ab6eb63485cab4c9566d04f ts=2026-09-25T21:45:07.2050000Z; 53m 48s: wenyi09232026.stratalog.logdata.json[3953] _id=6ab6f514485cab4c9566e779 ts=2026-09-25T22:26:28.4240000Z -> wenyi09232026.stratalog.logdata.json[1216] _id=6ab701b1485cab4c956707b9 ts=2026-09-25T23:20:17.3040000Z; 41m 21s: wenyi09232026.stratalog.logdata.json[5706] _id=6ab6eb63485cab4c9566d04f ts=2026-09-25T21:45:07.2050000Z -> wenyi09232026.stratalog.logdata.json[3953] _id=6ab6f514485cab4c9566e779 ts=2026-09-25T22:26:28.4240000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 71 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: wenyi09232026.stratalog.logdata.json[2318] _id=6ab6f94f485cab4c9566f80b ts=2026-09-25T22:44:31.2150000Z -> wenyi09232026.stratalog.logdata.json[2319] _id=6ab6f94f485cab4c9566f80d ts=2026-09-25T22:44:31.2150000Z; 1ms: wenyi09232026.stratalog.logdata.json[2458] _id=6ab6f8c6485cab4c9566f67d ts=2026-09-25T22:42:14.8150000Z -> wenyi09232026.stratalog.logdata.json[2457] _id=6ab6f8c6485cab4c9566f67f ts=2026-09-25T22:42:14.8160000Z; 2ms: wenyi09232026.stratalog.logdata.json[2490] _id=6ab6f89c485cab4c9566f617 ts=2026-09-25T22:41:32.7610000Z -> wenyi09232026.stratalog.logdata.json[2488] _id=6ab6f89c485cab4c9566f61b ts=2026-09-25T22:41:32.7630000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 22m 26s 
  - Evidence: 22m 26s: wenyi09232026.stratalog.logdata.json[8780] _id=6ab6de08485cab4c95662bce ts=2026-09-25T20:48:08.3070000Z -> wenyi09232026.stratalog.logdata.json[8328] _id=6ab6e34a485cab4c9566b2d5 ts=2026-09-25T21:10:34.6200000Z; 19m 39s: wenyi09232026.stratalog.logdata.json[7223] _id=6ab6e494485cab4c9566bc7b ts=2026-09-25T21:16:04.8370000Z -> wenyi09232026.stratalog.logdata.json[5983] _id=6ab6e930485cab4c9566cbcf ts=2026-09-25T21:35:44.2200000Z; 10m 12s: wenyi09232026.stratalog.logdata.json[5848] _id=6ab6ea02485cab4c9566cdbf ts=2026-09-25T21:39:14.3870000Z -> wenyi09232026.stratalog.logdata.json[5627] _id=6ab6ec66485cab4c9566d1f9 ts=2026-09-25T21:49:26.7950000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi09232026.stratalog.logdata.json[1740] _id=6ab6fd79485cab4c95670021 ts=2026-09-25T23:02:17.7660000Z -> wenyi09232026.stratalog.logdata.json[1741] _id=6ab6fd79485cab4c95670023 ts=2026-09-25T23:02:17.7660000Z; 0ms: wenyi09232026.stratalog.logdata.json[1776] _id=6ab6fd36485cab4c9566ffa3 ts=2026-09-25T23:01:11.0180000Z -> wenyi09232026.stratalog.logdata.json[1775] _id=6ab6fd36485cab4c9566ffa5 ts=2026-09-25T23:01:11.0180000Z; 1ms: wenyi09232026.stratalog.logdata.json[11546] _id=6ab6d529485cab4c95632d87 ts=2026-09-25T20:10:17.7330000Z -> wenyi09232026.stratalog.logdata.json[11545] _id=6ab6d529485cab4c95632d89 ts=2026-09-25T20:10:17.7340000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 43m 14s 
  - Evidence: 43m 14s: wenyi09232026.stratalog.logdata.json[6235] _id=6ab6e608485cab4c9566c661 ts=2026-09-25T21:22:14.3410000Z -> wenyi09232026.stratalog.logdata.json[5015] _id=6ab6f02a485cab4c9566da87 ts=2026-09-25T22:05:29.2860000Z; 27m 40s: wenyi09232026.stratalog.logdata.json[1902] _id=6ab6fb63485cab4c9566fd19 ts=2026-09-25T22:53:21.3690000Z -> wenyi09232026.stratalog.logdata.json[1202] _id=6ab701de485cab4c956707f3 ts=2026-09-25T23:21:02.3260000Z; 24m 17s: wenyi09232026.stratalog.logdata.json[8810] _id=6ab6ddcb485cab4c9566204a ts=2026-09-25T20:47:05.7110000Z -> wenyi09232026.stratalog.logdata.json[8297] _id=6ab6e37b485cab4c9566b34d ts=2026-09-25T21:11:23.2740000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3541 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi09232026.stratalog.logdata.json[10002] _id=6ab6dd19485cab4c9565f34e ts=2026-09-25T20:44:07.8800000Z -> wenyi09232026.stratalog.logdata.json[10006] _id=6ab6dd19485cab4c9565f350 ts=2026-09-25T20:44:07.8800000Z; 0ms: wenyi09232026.stratalog.logdata.json[10003] _id=6ab6dd19485cab4c9565f34b ts=2026-09-25T20:44:07.8800000Z -> wenyi09232026.stratalog.logdata.json[10002] _id=6ab6dd19485cab4c9565f34e ts=2026-09-25T20:44:07.8800000Z; 0ms: wenyi09232026.stratalog.logdata.json[10004] _id=6ab6dd19485cab4c9565f352 ts=2026-09-25T20:44:07.8800000Z -> wenyi09232026.stratalog.logdata.json[10005] _id=6ab6dd19485cab4c9565f356 ts=2026-09-25T20:44:07.8800000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 53m 39s 
  - Evidence: 53m 39s: wenyi09232026.stratalog.logdata.json[8317] _id=6ab6e358485cab4c9566b2fb ts=2026-09-25T21:10:48.6900000Z -> wenyi09232026.stratalog.logdata.json[5047] _id=6ab6efeb485cab4c9566da09 ts=2026-09-25T22:04:27.9930000Z; 29m 7s: wenyi09232026.stratalog.logdata.json[5033] _id=6ab6eff8485cab4c9566da31 ts=2026-09-25T22:04:40.2980000Z -> wenyi09232026.stratalog.logdata.json[3868] _id=6ab6f6cb485cab4c9566e9b5 ts=2026-09-25T22:33:48.0210000Z; 22m 23s: wenyi09232026.stratalog.logdata.json[8778] _id=6ab6de0b485cab4c95662c79 ts=2026-09-25T20:48:11.2910000Z -> wenyi09232026.stratalog.logdata.json[8329] _id=6ab6e34a485cab4c9566b2d3 ts=2026-09-25T21:10:34.6190000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 22m 38s 
  - Evidence: 22m 38s: wenyi09232026.stratalog.logdata.json[5461] _id=6ab6edc0485cab4c9566d4a5 ts=2026-09-25T21:55:13.0420000Z -> wenyi09232026.stratalog.logdata.json[4137] _id=6ab6f30f485cab4c9566e427 ts=2026-09-25T22:17:51.4100000Z; 20m 3s: wenyi09232026.stratalog.logdata.json[8343] _id=6ab6e32e485cab4c9566b295 ts=2026-09-25T21:10:07.1710000Z -> wenyi09232026.stratalog.logdata.json[6081] _id=6ab6e7e2485cab4c9566c9a1 ts=2026-09-25T21:30:10.1980000Z; 18m 47s: wenyi09232026.stratalog.logdata.json[6077] _id=6ab6e7ef485cab4c9566c9b7 ts=2026-09-25T21:30:23.9720000Z -> wenyi09232026.stratalog.logdata.json[5634] _id=6ab6ec57485cab4c9566d1db ts=2026-09-25T21:49:11.8540000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.003s..0.016s shown 
  - Evidence: 3ms: wenyi09232026.stratalog.logdata.json[8516] _id=6ab6e0fb485cab4c9566ac9b ts=2026-09-25T21:00:44.1130000Z -> wenyi09232026.stratalog.logdata.json[8512] _id=6ab6e0fc485cab4c9566aca3 ts=2026-09-25T21:00:44.1160000Z; 16ms: wenyi09232026.stratalog.logdata.json[8517] _id=6ab6e0fb485cab4c9566ac99 ts=2026-09-25T21:00:44.0970000Z -> wenyi09232026.stratalog.logdata.json[8516] _id=6ab6e0fb485cab4c9566ac9b ts=2026-09-25T21:00:44.1130000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 1h 13m 
  - Evidence: 1h 13m: wenyi09232026.stratalog.logdata.json[11212] _id=6ab6d958485cab4c9564ede4 ts=2026-09-25T20:28:09.0470000Z -> wenyi09232026.stratalog.logdata.json[5784] _id=6ab6ea8a485cab4c9566cecf ts=2026-09-25T21:41:30.3190000Z; 1h 4m: wenyi09232026.stratalog.logdata.json[5132] _id=6ab6ef4e485cab4c9566d8c5 ts=2026-09-25T22:01:50.7320000Z -> wenyi09232026.stratalog.logdata.json[1634] _id=6ab6fe87485cab4c956701d9 ts=2026-09-25T23:06:47.5600000Z; 35m 51s: wenyi09232026.stratalog.logdata.json[1634] _id=6ab6fe87485cab4c956701d9 ts=2026-09-25T23:06:47.5600000Z -> wenyi09232026.stratalog.logdata.json[270] _id=6ab706ee485cab4c95671345 ts=2026-09-25T23:42:39.2720000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 1h 12m 
  - Evidence: 1h 12m: wenyi09232026.stratalog.logdata.json[11211] _id=6ab6d958485cab4c9564edf4 ts=2026-09-25T20:28:09.0500000Z -> wenyi09232026.stratalog.logdata.json[5808] _id=6ab6ea72485cab4c9566ce85 ts=2026-09-25T21:41:06.2080000Z; 1h 2m: wenyi09232026.stratalog.logdata.json[5128] _id=6ab6ef4e485cab4c9566d8cd ts=2026-09-25T22:01:50.7490000Z -> wenyi09232026.stratalog.logdata.json[1695] _id=6ab6fdf4485cab4c956700e3 ts=2026-09-25T23:04:20.8060000Z; 34m 40s: wenyi09232026.stratalog.logdata.json[1630] _id=6ab6fe87485cab4c956701e1 ts=2026-09-25T23:06:47.5770000Z -> wenyi09232026.stratalog.logdata.json[326] _id=6ab706a7485cab4c9567129d ts=2026-09-25T23:41:27.8040000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.014s..0.014s shown 
  - Evidence: 14ms: wenyi09232026.stratalog.logdata.json[1633] _id=6ab6fe87485cab4c956701db ts=2026-09-25T23:06:47.5630000Z -> wenyi09232026.stratalog.logdata.json[1630] _id=6ab6fe87485cab4c956701e1 ts=2026-09-25T23:06:47.5770000Z; 14ms: wenyi09232026.stratalog.logdata.json[5131] _id=6ab6ef4e485cab4c9566d8c7 ts=2026-09-25T22:01:50.7350000Z -> wenyi09232026.stratalog.logdata.json[5128] _id=6ab6ef4e485cab4c9566d8cd ts=2026-09-25T22:01:50.7490000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 1h 13m 
  - Evidence: 1h 13m: wenyi09232026.stratalog.logdata.json[11216] _id=6ab6d953485cab4c9564ebd6 ts=2026-09-25T20:28:03.7940000Z -> wenyi09232026.stratalog.logdata.json[5800] _id=6ab6ea7c485cab4c9566cea1 ts=2026-09-25T21:41:16.7120000Z; 1h 2m: wenyi09232026.stratalog.logdata.json[5136] _id=6ab6ef45485cab4c9566d8b3 ts=2026-09-25T22:01:41.2780000Z -> wenyi09232026.stratalog.logdata.json[1691] _id=6ab6fdf9485cab4c956700f1 ts=2026-09-25T23:04:26.0420000Z; 34m 45s: wenyi09232026.stratalog.logdata.json[1635] _id=6ab6fe86485cab4c956701d7 ts=2026-09-25T23:06:46.7100000Z -> wenyi09232026.stratalog.logdata.json[320] _id=6ab706ac485cab4c956712ad ts=2026-09-25T23:41:32.5560000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 30 interval(s) ≤ 0.000s..0.016s shown 
  - Evidence: 0ms: wenyi09232026.stratalog.logdata.json[1637] _id=6ab6fe86485cab4c956701d3 ts=2026-09-25T23:06:46.6930000Z -> wenyi09232026.stratalog.logdata.json[1636] _id=6ab6fe86485cab4c956701d5 ts=2026-09-25T23:06:46.6930000Z; 16ms: wenyi09232026.stratalog.logdata.json[11225] _id=6ab6d94b485cab4c9564e87f ts=2026-09-25T20:27:55.4400000Z -> wenyi09232026.stratalog.logdata.json[11224] _id=6ab6d94b485cab4c9564e88b ts=2026-09-25T20:27:55.4560000Z; 16ms: wenyi09232026.stratalog.logdata.json[1687] _id=6ab6fe06485cab4c95670103 ts=2026-09-25T23:04:38.9650000Z -> wenyi09232026.stratalog.logdata.json[1686] _id=6ab6fe06485cab4c95670105 ts=2026-09-25T23:04:38.9810000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 1h 39m 
  - Evidence: 1h 39m: wenyi09232026.stratalog.logdata.json[5134] _id=6ab6ef4c485cab4c9566d8bf ts=2026-09-25T22:01:48.3800000Z -> wenyi09232026.stratalog.logdata.json[323] _id=6ab706a8485cab4c956712a5 ts=2026-09-25T23:41:29.3070000Z; 1h 13m: wenyi09232026.stratalog.logdata.json[11228] _id=6ab6d942485cab4c9564e455 ts=2026-09-25T20:27:46.8190000Z -> wenyi09232026.stratalog.logdata.json[5803] _id=6ab6ea78485cab4c9566ce97 ts=2026-09-25T21:41:12.8110000Z; 19m 59s: wenyi09232026.stratalog.logdata.json[5802] _id=6ab6ea7a485cab4c9566ce9b ts=2026-09-25T21:41:14.2610000Z -> wenyi09232026.stratalog.logdata.json[5165] _id=6ab6ef29485cab4c9566d85d ts=2026-09-25T22:01:13.3980000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 15m 24s 
  - Evidence: 15m 24s: wenyi09232026.stratalog.logdata.json[1210] _id=6ab701d9485cab4c956707e7 ts=2026-09-25T23:20:57.3370000Z -> wenyi09232026.stratalog.logdata.json[443] _id=6ab70575485cab4c956710c1 ts=2026-09-25T23:36:21.7140000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 53m 55s 
  - Evidence: 53m 55s: wenyi09232026.stratalog.logdata.json[3951] _id=6ab6f532485cab4c9566e79b ts=2026-09-25T22:26:58.6180000Z -> wenyi09232026.stratalog.logdata.json[1212] _id=6ab701d6485cab4c956707e3 ts=2026-09-25T23:20:54.3300000Z; 48m 11s: wenyi09232026.stratalog.logdata.json[8620] _id=6ab6e037485cab4c95669ede ts=2026-09-25T20:57:27.3850000Z -> wenyi09232026.stratalog.logdata.json[5703] _id=6ab6eb82485cab4c9566d073 ts=2026-09-25T21:45:38.7780000Z; 41m 19s: wenyi09232026.stratalog.logdata.json[5703] _id=6ab6eb82485cab4c9566d073 ts=2026-09-25T21:45:38.7780000Z -> wenyi09232026.stratalog.logdata.json[3951] _id=6ab6f532485cab4c9566e79b ts=2026-09-25T22:26:58.6180000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 16m 55s 
  - Evidence: 16m 55s: wenyi09232026.stratalog.logdata.json[852] _id=6ab702cb485cab4c95670b71 ts=2026-09-25T23:24:59.8160000Z -> wenyi09232026.stratalog.logdata.json[308] _id=6ab706c3485cab4c956712d7 ts=2026-09-25T23:41:55.5840000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 16m 50s 
  - Evidence: 16m 50s: wenyi09232026.stratalog.logdata.json[854] _id=6ab702c9485cab4c95670b67 ts=2026-09-25T23:24:57.8600000Z -> wenyi09232026.stratalog.logdata.json[310] _id=6ab706bc485cab4c956712cd ts=2026-09-25T23:41:48.3210000Z; 15m 48s: wenyi09232026.stratalog.logdata.json[11117] _id=6ab6da1f485cab4c95652de2 ts=2026-09-25T20:31:28.1820000Z -> wenyi09232026.stratalog.logdata.json[8805] _id=6ab6ddd4485cab4c95662216 ts=2026-09-25T20:47:16.6030000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 15m 14s 
  - Evidence: 15m 14s: wenyi09232026.stratalog.logdata.json[6159] _id=6ab6e6fc485cab4c9566c807 ts=2026-09-25T21:26:21.1570000Z -> wenyi09232026.stratalog.logdata.json[5778] _id=6ab6ea8f485cab4c9566cee1 ts=2026-09-25T21:41:35.4550000Z; 10m 4s: wenyi09232026.stratalog.logdata.json[8527] _id=6ab6e0e8485cab4c9566ac51 ts=2026-09-25T21:00:24.5540000Z -> wenyi09232026.stratalog.logdata.json[8334] _id=6ab6e344485cab4c9566b2c3 ts=2026-09-25T21:10:28.9320000Z; 10m 4s: wenyi09232026.stratalog.logdata.json[4958] _id=6ab6f02e485cab4c9566daf1 ts=2026-09-25T22:05:35.0560000Z -> wenyi09232026.stratalog.logdata.json[4202] _id=6ab6f28b485cab4c9566e329 ts=2026-09-25T22:15:39.1980000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi09232026.stratalog.logdata.json[11284] _id=6ab6d875485cab4c95649e95 ts=2026-09-25T20:24:21.6570000Z -> wenyi09232026.stratalog.logdata.json[11283] _id=6ab6d875485cab4c95649e97 ts=2026-09-25T20:24:21.6570000Z; 0ms: wenyi09232026.stratalog.logdata.json[219] _id=6ab70743485cab4c956713ed ts=2026-09-25T23:44:04.2490000Z -> wenyi09232026.stratalog.logdata.json[218] _id=6ab70744485cab4c956713ef ts=2026-09-25T23:44:04.2490000Z; 0ms: wenyi09232026.stratalog.logdata.json[544] _id=6ab704b6485cab4c95670f61 ts=2026-09-25T23:33:10.6490000Z -> wenyi09232026.stratalog.logdata.json[543] _id=6ab704b6485cab4c95670f63 ts=2026-09-25T23:33:10.6490000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi09232026.stratalog.logdata.json[11293] _id=6ab6d864485cab4c95649678 ts=2026-09-25T20:24:04.3790000Z`; `wenyi09232026.stratalog.logdata.json[11201] _id=6ab6d973485cab4c9564f944 ts=2026-09-25T20:28:35.7480000Z`; `wenyi09232026.stratalog.logdata.json[8403] _id=6ab6e23d485cab4c9566b0f5 ts=2026-09-25T21:06:06.0930000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 72 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `wenyi09232026.stratalog.logdata.json[10751] _id=6ab6dcb9485cab4c9565da96 ts=2026-09-25T20:42:30.9070000Z`; `wenyi09232026.stratalog.logdata.json[10747] _id=6ab6dcb9485cab4c9565da9f ts=2026-09-25T20:42:30.9730000Z`; `wenyi09232026.stratalog.logdata.json[10396] _id=6ab6dce3485cab4c9565e5e7 ts=2026-09-25T20:43:13.8920000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 55 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi09232026.stratalog.logdata.json[10914] _id=6ab6dca9485cab4c9565d5a9 ts=2026-09-25T20:42:16.8160000Z`; `wenyi09232026.stratalog.logdata.json[10913] _id=6ab6dca9485cab4c9565d5ab ts=2026-09-25T20:42:17.2160000Z`; `wenyi09232026.stratalog.logdata.json[10847] _id=6ab6dcb2485cab4c9565d828 ts=2026-09-25T20:42:24.6690000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi09232026.stratalog.logdata.json[5128] _id=6ab6ef4e485cab4c9566d8cd ts=2026-09-25T22:01:50.7490000Z`; `wenyi09232026.stratalog.logdata.json[1630] _id=6ab6fe87485cab4c956701e1 ts=2026-09-25T23:06:47.5770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `wenyi09232026.stratalog.logdata.json[1637] _id=6ab6fe86485cab4c956701d3 ts=2026-09-25T23:06:46.6930000Z`; `wenyi09232026.stratalog.logdata.json[1636] _id=6ab6fe86485cab4c956701d5 ts=2026-09-25T23:06:46.6930000Z`; `wenyi09232026.stratalog.logdata.json[1635] _id=6ab6fe86485cab4c956701d7 ts=2026-09-25T23:06:46.7100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `wenyi09232026.stratalog.logdata.json[1210] _id=6ab701d9485cab4c956707e7 ts=2026-09-25T23:20:57.3370000Z`; `wenyi09232026.stratalog.logdata.json[443] _id=6ab70575485cab4c956710c1 ts=2026-09-25T23:36:21.7140000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 513 occurrence(s) 
  - Examples: `wenyi09232026.stratalog.logdata.json[10843] _id=6ab6dcb2485cab4c9565d834 ts=2026-09-25T20:42:24.9700000Z`; `wenyi09232026.stratalog.logdata.json[10837] _id=6ab6dcb3485cab4c9565d896 ts=2026-09-25T20:42:25.1540000Z`; `wenyi09232026.stratalog.logdata.json[10813] _id=6ab6dcb5485cab4c9565d90c ts=2026-09-25T20:42:26.5710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 792 occurrence(s) 
  - Examples: `wenyi09232026.stratalog.logdata.json[10977] _id=6ab6dc9c485cab4c9565d1db ts=2026-09-25T20:42:03.9960000Z`; `wenyi09232026.stratalog.logdata.json[10976] _id=6ab6dc9c485cab4c9565d1de ts=2026-09-25T20:42:04.0120000Z`; `wenyi09232026.stratalog.logdata.json[10974] _id=6ab6dc9d485cab4c9565d221 ts=2026-09-25T20:42:04.6120000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 15 occurrence(s) 
  - Examples: `wenyi09232026.stratalog.logdata.json[8516] _id=6ab6e0fb485cab4c9566ac9b ts=2026-09-25T21:00:44.1130000Z`; `wenyi09232026.stratalog.logdata.json[8512] _id=6ab6e0fc485cab4c9566aca3 ts=2026-09-25T21:00:44.1160000Z`; `wenyi09232026.stratalog.logdata.json[8448] _id=6ab6e1a7485cab4c9566afc7 ts=2026-09-25T21:03:35.7760000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `wenyi09232026.stratalog.logdata.json[285] _id=6ab706e6485cab4c95671321 ts=2026-09-25T23:42:30.4180000Z`; `wenyi09232026.stratalog.logdata.json[279] _id=6ab706ea485cab4c9567132f ts=2026-09-25T23:42:34.4530000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `wenyi09232026.stratalog.logdata.json[5135] _id=6ab6ef4b485cab4c9566d8bb ts=2026-09-25T22:01:47.4800000Z`; `wenyi09232026.stratalog.logdata.json[5134] _id=6ab6ef4c485cab4c9566d8bf ts=2026-09-25T22:01:48.3800000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'DialogueStartEvent' (totals: 363 start, 360 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 47 unmatched 'BecameCameraCentered' (totals: 1155 open, 1180 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 72 unmatched 'BecameVisible' (totals: 1427 open, 1410 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 20 open, 18 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 60 open, 62 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 9 unmatched 'argumentationToolOpen' (totals: 9 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 39 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 675 of 11647 adjacent _id pairs reverse in client time; worst 83.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi09232026.stratalog.logdata.json[10922] _id=6ab6dca2485cab4c9565d39b ts=2026-09-25T20:42:10.2990000Z`; `wenyi09232026.stratalog.logdata.json[11030] _id=6ab6dca3485cab4c9565d3d3 ts=2026-09-25T20:40:47.2600000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.17s, min -85.06s, max +0.35s over 11648 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-23-26.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Full playthrough by one tester in a single sitting, logged 2026-09-25 20:06Z to 23:55Z (~3h49m, 11,648 records; EndOfUnit fired for units 1-5). No gap longer than 20 minutes. Log file is named wenyi09232026 but every record is dated 2026-09-25.; SAME BUILD as the 09-14-26-3 run: the version string is again literally '20260914-' on every record, with the build number after the dash still missing. This run is therefore a second playthrough of the 2026-09-14 build, not a new build; build-vs-baseline differences are playthrough variation unless stated otherwise.; Six gameStartEvent records = six launches from MainMenu: initial launch, one relaunch mid-Unit 2 (20:57Z, see next note), and one relaunch before each of Units 3, 4 and 5 (Unit 1 -> Unit 2 also went through Transition + MainMenu).; Unit 2 was played in two scene loads: 20:38Z-20:55Z, then MainMenu, then 20:57Z-21:45Z. The relaunch resumed from a checkpoint that predates the 'Foraged Forging' (quest 23) completion: questActiveEvent:23 / questFinishEvent:23 / questActiveEvent:22 each appear twice (20:52-20:54Z and again 20:57-21:00Z), so Unit 2 quest 23 was played twice and its duplicated quest records are player-driven, not a logging defect. EndOfUnit 2 fires once, at 21:45Z.; Debug menu was NOT used. The 12 DEBUGMenu records (DebugMenuStateChanged, all isOpened=false) each sit at the exact first instant of a gameplay scene load (12 of the 13 gameplay scene loads; only the final 'Unit 5 Dev' load at 23:36:21Z lacks one) — the same scene-load emission pattern first seen in 09-14-26-3.; chatEvent: the two records (actionType Close, chatID NA) coincide exactly with the two Unit 5 scene loads (23:20:57Z dungeon, 23:36:21Z surface), the same pattern as 08-31-26, 09-03-26-3 and 09-14-26-3; the tester never opened the chat log.; argumentationToolEvent: 9 records, all argumentationToolOpen, in Units 1, 2, 3 and 5 only — NO Unit 4 backing-info panel event at all, although the Unit 4 argumentation was completed (answer submitted 23:06:47Z). Consistent with the Unit 4 panel-logging gap reported to the team.; No 'crash' eventType records this run. |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 5172 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3456); Unit 4 Dev (1064); Unit 3 Dungeon Dev (342); Unit 5 Dev - Dungeon (310)
- **Intervals:** median 0.02s (p5 0.00s / p95 0.69s, n=5171)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5172/5172 records)
    "BecameVisible"  x1427
    "BecameInvisible"  x1410
    "BecameCameraUncentered"  x1180
    "BecameCameraCentered"  x1155
data.pieceId  (string, 5172/5172 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5172/5172 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2411 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (756); Unit 3 Dev (350); Unit 4 Dev - Dungeon (322); Unit 4 Dev (306); Unit 3 Dungeon Dev (257); Unit 5 Dev - Dungeon (220); Unit 1 Dev (117); Unit 5 Dev (50); Unit 4 Dev - Anderson Base (33)
- **Intervals:** median 0.58s (p5 0.07s / p95 20.67s, n=2410)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2411/2411 records)
    "pressed"  x2411
data.actionType  (string, 2411/2411 records)
    "Move"  x1737
    "Interact"  x479
    "Sprint"  x105
    "Ascend"  x37
    "Jump"  x20
    "Descend"  x14
    "Hoverboard"  x14
    "Map"  x5
data.key  (string, 2411/2411 records, 5 empty-string)
    "w"  x711
    "leftButton"  x452
    "d"  x351
    "a"  x341
    "s"  x333
    "leftShift"  x119
    "e"  x43
    "space"  x41
    "h"  x10
    ""  x5
    "m"  x5
data.playerOrDrone  (string, 2411/2411 records)
    "Player"  x2072
    "Drone"  x339
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1943 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (566); Unit 4 Dev (287); Unit 3 Dev (278); Unit 5 Dev (214); Unit 1 Dev (189); Unit 3 Dungeon Dev (132); Unit 5 Dev - Dungeon (106); Unit 4 Dev - Dungeon (102); Unit 4 Dev - Anderson Base (69)
- **eventKey:** present on 1220 of 1943 records
- **Intervals:** median 3.70s (p5 0.00s / p95 21.91s, n=1942)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1220; [conversationId, dialogueEventType] x723
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1943/1943 records)
    numeric range 8 .. 118 (54 unique)
data.dialogueEventType  (string, 1943/1943 records)
    "DialogueNodeEvent"  x1220
    "DialogueStartEvent"  x363
    "DialogueFinishEvent"  x360
data.nodeId  (number, 1220/1943 records)
    numeric range 0 .. 290 (216 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1304 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (386); Unit 4 Dev (184); Unit 3 Dev (176); Unit 1 Dev (148); Unit 5 Dev (112); Unit 5 Dev - Dungeon (93); Unit 4 Dev - Dungeon (80); Unit 3 Dungeon Dev (67); Unit 4 Dev - Anderson Base (58)
- **Intervals:** median 10.01s (p5 9.99s / p95 10.01s, n=1292)
- **Fields under `data`:**

```text
data.position  (object, 1304/1304 records)
data.position.x  (number, 1304/1304 records)
    numeric range -693.336 .. 1558.92 (402 unique)
data.position.y  (number, 1304/1304 records)
    numeric range -112.453 .. 217.936 (310 unique)
data.position.z  (number, 1304/1304 records)
    numeric range -1031.71 .. 1802.88 (402 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 235 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (87); Unit 4 Dev - Dungeon (51); Unit 3 Dungeon Dev (33); Unit 4 Dev (22); Unit 1 Dev (11); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (6); Unit 5 Dev - Dungeon (5)
- **Intervals:** median 5.98s (p5 1.43s / p95 369.20s, n=234)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 235/235 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 235/235 records)
    97 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 140 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (43); Unit 5 Dev (42); Unit 3 Dev (25); Unit 1 Dev (15); Unit 2 Prod (Refactor) (15)
- **Intervals:** median 0.47s (p5 0.02s / p95 19.60s, n=139)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 140/140 records)
    "argumentationNodeHoverEnd"  x62
    "argumentationNodeHoverStart"  x60
    "argumentationNodeAdd"  x18
data.argumentationTitle  (string, 140/140 records)
    "Unit 4 - Flooding"  x43
    "Unit 5"  x42
    "Unit 3 - Pollution Upstream"  x25
    "Unit 2 – Watershed"  x15
    "Unit 1 - Freshwater"  x11
    "Unit 1 - Argumentation Tutorial"  x4
data.nodeName  (string, 140/140 records)
    "1"  x20
    "A"  x20
    "2"  x17
    "I"  x14
    "3"  x13
    "C"  x13
    "II"  x13
    "4"  x10
    "D"  x9
    "B"  x8
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 83 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (54); Unit 3 Dev (29)
- **Intervals:** median 1.83s (p5 0.50s / p95 384.04s, n=82)
- **`data` key-set variants:** [actionType, featureUsed, location] x40; [actionType, featureUsed] x38; [actionType, featureUsed, legendName] x5
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 83/83 records)
    "WaypointMoveEvent"  x36
    "MapOpenEvent"  x20
    "MapCloseEvent"  x18
    "Selected"  x3
    "WaypointSetEvent"  x3
    "Unselected"  x2
    "WaypointResetEvent"  x1
data.featureUsed  (string, 83/83 records)
    "Waypoint"  x40
    "Map"  x38
    "Legend"  x5
data.legendName  (string, 5/83 records)
    "0 ft"  x4
    "90 ft"  x1
data.location  (object, 40/83 records)
data.location.x  (number, 40/83 records)
    numeric range -269.428 .. 638.759 (31 unique)
data.location.y  (number, 40/83 records)
    numeric range -153.544 .. 361.6 (33 unique)
data.location.z  (number, 40/83 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 82 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev (15); Unit 1 Dev (14); Unit 4 Dev - Dungeon (7); MainMenu (6); Unit 3 Dev (6); Transition (2); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 95.83s (p5 3.19s / p95 450.58s, n=81)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 82/82 records)
    true  x82
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 76 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev (15); Unit 1 Dev (14); Unit 4 Dev - Dungeon (7); Unit 3 Dev (6); Transition (2); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 108.82s (p5 5.32s / p95 460.61s, n=75)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 76/76 records)
    false  x76
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `questEvent` — 71 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 71 of 71 records
- **Intervals:** median 147.97s (p5 0.00s / p95 549.23s, n=70)
- **`data` key-set variants:** [questEventType, questID, questName] x39; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 71/71 records)
    "questActiveEvent"  x39
    "questFinishEvent"  x32
data.questID  (string, 71/71 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 71/71 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/71 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 38 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (14); Unit 2 Prod (Refactor) (12); Unit 3 Dev (12)
- **Intervals:** median 0.80s (p5 0.17s / p95 1424.21s, n=37)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x30; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/38 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/38 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 30/38 records)
    "RightDrag"  x18
    "LeftDrag"  x12
data.currentSoilType  (string, 30/38 records)
    "SAND"  x6
    "SANDGRAVEL"  x6
    "CLAY"  x5
    "CLAYSAND"  x5
    "CLAYROCK"  x4
    "GRAVEL"  x3
    "BEDROCK"  x1
data.isCorrectSelection  (string, 30/38 records)
    "false"  x24
    "true"  x6
data.waterLevelStatus  (string, 30/38 records)
    "TooHigh"  x12
    "Proper"  x9
    "TooLow"  x9
data.waterRetentionChange  (string, 30/38 records)
    "Decrease"  x15
    "Increase"  x9
    "NoChange"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 20 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (20)
- **Intervals:** median 19.61s (p5 1.96s / p95 69.19s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "On"  x16
    "Off"  x4
data.floor  (string, 20/20 records)
    "3"  x10
    "4"  x5
    "2"  x3
    "1"  x2
data.machineNumber  (string, 20/20 records)
    "One"  x19
    "Two"  x1
data.machineType  (string, 20/20 records)
    "Condenser"  x9
    "Evaporator"  x4
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 20/20 records)
    "2"  x10
    "1"  x4
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 66.93s (p5 0.01s / p95 4000.90s, n=13)
- **Open findings:** 2 — see sections 5-8
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

### `DEBUGMenu` — 12 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (3); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 795.29s (p5 504.04s / p95 2402.30s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "DebugMenuStateChanged"  x12
data.isOpened  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 4.06s (p5 1.15s / p95 22.46s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 5 empty-string)
    "cameraPlaced"  x6
    ""  x5
data.boxId  (string, 11/11 records)
    "0"  x4
    "2"  x4
    "1"  x3
data.soilType  (string, 11/11 records)
    "Sand"  x7
    "Clay"  x2
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 1 Dev (1)
- **Intervals:** median 17.07s (p5 1.07s / p95 5429.70s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x9
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x4
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 6 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (6)
- **Intervals:** median 2479.84s (p5 1314.67s / p95 3166.85s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 6/6 records)
    true  x6
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 2855.05s (p5 2144.30s / p95 4272.26s, n=4)
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

### `argumentationAnswerEvent` — 5 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 3024.27s (p5 1360.11s / p95 4325.61s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "submitAnswerEvent"  x5
data.answerSubmitted  (string, 5/5 records)
    "A,1,I"  x1
    "A,1,II"  x1
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "D,C,3,II"  x1
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
    "Unit 4 - Flooding"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 5 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (5)
- **Intervals:** median 62.31s (p5 13.23s / p95 194.88s, n=4)
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
- **Intervals:** median 1.82s (p5 1.53s / p95 2.21s, n=3)
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
- **Intervals:** median 924.38s (p5 924.38s / p95 924.38s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-14-26-3\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `argumentationNodeEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DaniEvent` : event type present in baseline 09-14-26-3 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationNodeEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "Selected" (3x); "Unselected" (2x); "WaypointMoveEvent" (36x); "WaypointResetEvent" (1x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (5x); "Waypoint" (40x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*