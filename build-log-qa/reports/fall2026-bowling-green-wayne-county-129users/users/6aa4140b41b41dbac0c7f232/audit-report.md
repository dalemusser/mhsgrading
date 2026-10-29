# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f232

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f232
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f232.jsonl
- **Records:** 11074 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f232
- **Time span:** 2026-09-23T13:56:45.085000+00:00 .. 2026-10-06T14:06:22.598000+00:00 (312h 9m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f232\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 11074 records, 10 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 103 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3042 | 27.47 | 1 | 9 | 0 | 2026-09-23T13:57:01.800000+00:00 | 2026-10-06T14:04:09.529000+00:00 | 312h 7m |
| PuzzlePieceVisibleEvent | 2911 | 26.29 | 1 | 4 | 0 | 2026-09-23T14:28:01.259000+00:00 | 2026-10-05T13:53:55.711000+00:00 | 287h 25m |
| DialogueEvent | 2155 | 19.46 | 1 | 9 | 1343 | 2026-09-23T13:57:18.398000+00:00 | 2026-10-06T14:04:07.026000+00:00 | 312h 6m |
| PlayerPositionEvent | 1854 | 16.74 | 1 | 9 | 0 | 2026-09-23T13:56:56.748000+00:00 | 2026-10-06T14:04:05.520000+00:00 | 312h 7m |
| argumentationNodeEvent | 340 | 3.07 | 1 | 5 | 0 | 2026-09-23T14:17:50.280000+00:00 | 2026-10-05T14:10:07.460000+00:00 | 287h 52m |
| ObjectInterEvent | 301 | 2.72 | 1 | 9 | 0 | 2026-09-23T14:00:40.522000+00:00 | 2026-10-06T14:04:09.528000+00:00 | 312h 3m |
| TopographicMapEvent | 97 | 0.88 | 1 | 3 | 0 | 2026-09-23T14:28:38.492000+00:00 | 2026-10-01T13:55:25.458000+00:00 | 191h 26m |
| questEvent | 87 | 0.79 | 1 | 9 | 87 | 2026-09-23T13:57:18.375000+00:00 | 2026-10-06T14:00:13.640000+00:00 | 312h 2m |
| Soil Key Puzzle | 58 | 0.52 | 1 | 3 | 0 | 2026-09-24T13:47:28.190000+00:00 | 2026-09-30T13:55:25.847000+00:00 | 144h 7m |
| gameWindowFocusEvent | 34 | 0.31 | 1 | 7 | 0 | 2026-09-23T13:56:45.085000+00:00 | 2026-10-06T14:06:22.596000+00:00 | 312h 9m |
| argumentationAnswerEvent | 32 | 0.29 | 1 | 5 | 0 | 2026-09-23T14:18:58.167000+00:00 | 2026-10-05T14:10:16.398000+00:00 | 287h 51m |
| soilMachine | 26 | 0.23 | 1 | 1 | 0 | 2026-09-30T14:04:12.690000+00:00 | 2026-09-30T14:16:17.034000+00:00 | 12m 4s |
| WaterChamberEvent | 24 | 0.22 | 1 | 1 | 0 | 2026-10-05T13:53:10.252000+00:00 | 2026-10-05T14:01:52.014000+00:00 | 8m 41s |
| gameWindowUnfocusEvent | 22 | 0.2 | 1 | 6 | 0 | 2026-09-23T14:31:08.142000+00:00 | 2026-10-05T14:23:54.811000+00:00 | 287h 52m |
| DEBUGMenu | 20 | 0.18 | 1 | 8 | 0 | 2026-09-23T13:56:56.741000+00:00 | 2026-10-05T13:49:50.089000+00:00 | 287h 52m |
| gameStartEvent | 18 | 0.16 | 1 | 1 | 0 | 2026-09-23T13:56:45.085000+00:00 | 2026-10-06T14:06:22.598000+00:00 | 312h 9m |
| argumentationEvent | 17 | 0.15 | 1 | 5 | 0 | 2026-09-23T14:18:39.076000+00:00 | 2026-10-05T14:10:16.426000+00:00 | 287h 51m |
| SolarStillDesignEvent | 9 | 0.08 | 1 | 1 | 0 | 2026-10-05T14:16:01.829000+00:00 | 2026-10-06T13:58:00.460000+00:00 | 23h 41m |
| TerasGardenBox | 7 | 0.06 | 1 | 1 | 0 | 2026-10-01T13:56:33.594000+00:00 | 2026-10-01T13:57:14.441000+00:00 | 40.8s |
| chatEvent | 7 | 0.06 | 1 | 3 | 0 | 2026-09-25T14:29:52.917000+00:00 | 2026-10-06T13:49:37.895000+00:00 | 263h 19m |
| EndOfUnit | 4 | 0.04 | 1 | 4 | 0 | 2026-09-23T14:23:28.510000+00:00 | 2026-10-06T14:04:09.521000+00:00 | 311h 40m |
| crash | 4 | 0.04 | 1 | 1 | 0 |  |  | ? |
| argumentationToolEvent | 3 | 0.03 | 1 | 1 | 0 | 2026-09-23T14:20:39.978000+00:00 | 2026-09-23T14:20:44.290000+00:00 | 4.3s |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-25T14:29:50.079000+00:00 | 2026-09-25T14:29:52.548000+00:00 | 2.5s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1690.505s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 431006.404s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 9.399s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 9.548s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.156s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 43193.935s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1005.641s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1009.311s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.487s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; p; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 300 ft; 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.4x vs baseline. 
  - Observed: 32 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I; B,C,2,II; B,C,4,II; C,2,II; C,3,II; C,4,II; C,A,2,II; C,A,4,II; C,B,4,II; C,D,2,II; C,D,3,II; C,D,A,2,II; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 7 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [20-70, 20-71, 20-73, 20-74, 20-76] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: 30 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[163] _id=6ab3dbec485cab4c954ceef7 ts=2026-09-23T14:02:20.7450000Z`; `6aa4140b41b41dbac0c7f232.jsonl[220] _id=6ab3dcdd485cab4c954cf6ff ts=2026-09-23T14:06:21.0900000Z`; `6aa4140b41b41dbac0c7f232.jsonl[244] _id=6ab3dd65485cab4c954cfbfb ts=2026-09-23T14:08:37.8560000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[3214] _id=6ab67bd8485cab4c95559270 ts=2026-09-25T13:49:09.4650000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[42] _id=6ab3da9c485cab4c954ce47d ts=2026-09-23T13:56:45.0850000Z`; `6aa4140b41b41dbac0c7f232.jsonl[641] _id=6ab3e130485cab4c954d228d ts=2026-09-23T14:24:48.2060000Z`; `6aa4140b41b41dbac0c7f232.jsonl[1342] _id=6ab52857485cab4c95514706 ts=2026-09-24T13:40:38.8680000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 34 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 34} 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[41] _id=6ab3da9c485cab4c954ce47b ts=2026-09-23T13:56:45.0850000Z`; `6aa4140b41b41dbac0c7f232.jsonl[642] _id=6ab3e130485cab4c954d228b ts=2026-09-23T14:24:48.2050000Z`; `6aa4140b41b41dbac0c7f232.jsonl[1316] _id=6ab3e2ac485cab4c954d3476 ts=2026-09-23T14:31:08.1520000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[1315] _id=6ab3e2ac485cab4c954d3474 ts=2026-09-23T14:31:08.1420000Z`; `6aa4140b41b41dbac0c7f232.jsonl[3182] _id=6ab52f92485cab4c9551dfcb ts=2026-09-24T14:11:30.3360000Z`; `6aa4140b41b41dbac0c7f232.jsonl[3227] _id=6ab67bd8485cab4c95559276 ts=2026-09-25T13:49:09.7810000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 3 of 97 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[788] _id=6ab3e216485cab4c954d2c2d ts=2026-09-23T14:28:38.4920000Z`; `6aa4140b41b41dbac0c7f232.jsonl[787] _id=6ab3e219485cab4c954d2c45 ts=2026-09-23T14:28:41.1110000Z`; `6aa4140b41b41dbac0c7f232.jsonl[802] _id=6ab3e238485cab4c954d2d6e ts=2026-09-23T14:29:12.6390000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3041 | 0.001 | 0.847 | 369.493 | 20.086 | 343401.606 | 0.16 | 195 | 10 |
| PuzzlePieceVisibleEvent | 2910 | 0.0 | 0.021 | 355.586 | 1.095 | 343527.421 | 0.17 | 1959 | 9 |
| DialogueEvent | 2154 | 0.001 | 3.324 | 521.638 | 34.607 | 343401.148 | 0.12 | 628 | 8 |
| PlayerPositionEvent | 1842 | 9.527 | 9.999 | 609.62 | 10.033 | 343394.929 | 0.1 | 0 | 8 |
| argumentationNodeEvent | 339 | 0.016 | 0.351 | 3057.042 | 5.744 | 346580.495 | 0.02 | 83 | 5 |
| ObjectInterEvent | 300 | 0.001 | 6.331 | 3744.697 | 410.52 | 343542.204 | 0.02 | 5 | 12 |
| TopographicMapEvent | 96 | 0.022 | 2.869 | 7179.239 | 21711.255 | 257192.97 | 0.01 | 2 | 7 |
| questEvent | 86 | 0.001 | 160.731 | 13062.503 | 84458.887 | 343725.69 | 0.0 | 18 | 14 |
| Soil Key Puzzle | 57 | 0.156 | 1.008 | 9103.117 | 216.457 | 346526.653 | 0.01 | 0 | 3 |
| gameWindowFocusEvent | 33 | 0.855 | 1005.641 | 34053.864 | 155011.396 | 343183.851 | 0.0 | 0 | 18 |
| argumentationAnswerEvent | 31 | 0.172 | 9.548 | 33428.33 | 216108.682 | 346590.562 | 0.0 | 0 | 5 |
| soilMachine | 25 | 0.735 | 4.487 | 28.974 | 139.551 | 178.345 | 2.07 | 0 | 0 |
| WaterChamberEvent | 23 | 1.099 | 9.399 | 22.685 | 58.146 | 75.438 | 2.64 | 0 | 0 |
| gameWindowUnfocusEvent | 21 | 0.95 | 1009.311 | 49350.794 | 260039.033 | 345421.794 | 0.0 | 0 | 12 |
| DEBUGMenu | 19 | 190.507 | 1690.505 | 54545.966 | 267601.522 | 343720.71 | 0.0 | 0 | 13 |
| gameStartEvent | 17 | 190.162 | 2502.395 | 66104.56 | 275951.322 | 343183.851 | 0.0 | 0 | 14 |
| argumentationEvent | 16 | 0.022 | 53.671 | 64768.584 | 280460.317 | 346572.208 | 0.0 | 3 | 5 |
| SolarStillDesignEvent | 8 | 1.04 | 1.823 | 10664.829 | 55448.59 | 85302.885 | 0.01 | 0 | 1 |
| TerasGardenBox | 6 | 1.029 | 2.784 | 6.808 | 16.625 | 16.647 | 8.81 | 0 | 0 |
| chatEvent | 6 | 4.289 | 43193.935 | 157997.496 | 474197.907 | 517872.086 | 0.0 | 0 | 4 |
| EndOfUnit | 3 | 172136.175 | 431006.404 | 374013.67 | 510109.229 | 518898.432 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationToolEvent | 2 | 1.181 | 2.156 | 2.156 | 3.033 | 3.131 | 27.83 | 0 | 0 |
| DaniEvent | 1 | 2.469 | 2.469 | 2.469 | 2.469 | 2.469 | 24.3 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 164 group(s), 240 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[772] _id=6ab3e210485cab4c954d2ba3 ts=2026-09-23T14:28:32.1800000Z == 6aa4140b41b41dbac0c7f232.jsonl[757] _id=6ab3e210485cab4c954d2ba5 ts=2026-09-23T14:28:32.1800000Z`; `6aa4140b41b41dbac0c7f232.jsonl[765] _id=6ab3e212485cab4c954d2bdf ts=2026-09-23T14:28:32.6470000Z == 6aa4140b41b41dbac0c7f232.jsonl[778] _id=6ab3e212485cab4c954d2be1 ts=2026-09-23T14:28:32.6470000Z`; `6aa4140b41b41dbac0c7f232.jsonl[779] _id=6ab3e212485cab4c954d2be5 ts=2026-09-23T14:28:32.6750000Z == 6aa4140b41b41dbac0c7f232.jsonl[780] _id=6ab3e212485cab4c954d2be7 ts=2026-09-23T14:28:32.6750000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[9518] _id=6ac3ab03de269131f9a9e1bc ts=? == 6aa4140b41b41dbac0c7f232.jsonl[10777] _id=6ac4fc7cde269131f9b19359 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 25 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4140b41b41dbac0c7f232.jsonl[130] _id=6ab3db87485cab4c954cebcf ts=2026-09-23T14:00:40.5220000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[127] _id=6ab3db87485cab4c954cebd1 ts=2026-09-23T14:00:40.5250000Z`; `322ms: 6aa4140b41b41dbac0c7f232.jsonl[734] _id=6ab3e1d6485cab4c954d299f ts=2026-09-23T14:27:34.3720000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[724] _id=6ab3e1d6485cab4c954d29a7 ts=2026-09-23T14:27:34.6940000Z`; `929ms: 6aa4140b41b41dbac0c7f232.jsonl[724] _id=6ab3e1d6485cab4c954d29a7 ts=2026-09-23T14:27:34.6940000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[727] _id=6ab3e1d7485cab4c954d29b5 ts=2026-09-23T14:27:35.6230000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 588 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 6aa4140b41b41dbac0c7f232.jsonl[777] _id=6ab3e211485cab4c954d2bbf ts=2026-09-23T14:28:32.4730000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[783] _id=6ab3e211485cab4c954d2bc1 ts=2026-09-23T14:28:32.4850000Z`; `43ms: 6aa4140b41b41dbac0c7f232.jsonl[783] _id=6ab3e211485cab4c954d2bc1 ts=2026-09-23T14:28:32.4850000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[769] _id=6ab3e211485cab4c954d2bc3 ts=2026-09-23T14:28:32.5280000Z`; `91ms: 6aa4140b41b41dbac0c7f232.jsonl[769] _id=6ab3e211485cab4c954d2bc3 ts=2026-09-23T14:28:32.5280000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[763] _id=6ab3e211485cab4c954d2bc7 ts=2026-09-23T14:28:32.6190000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `262ms: 6aa4140b41b41dbac0c7f232.jsonl[1437] _id=6ab528de485cab4c95515a89 ts=2026-09-24T13:42:53.9960000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[1438] _id=6ab528de485cab4c95515a8d ts=2026-09-24T13:42:54.2580000Z`; `200ms: 6aa4140b41b41dbac0c7f232.jsonl[1438] _id=6ab528de485cab4c95515a8d ts=2026-09-24T13:42:54.2580000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[1439] _id=6ab528de485cab4c95515a91 ts=2026-09-24T13:42:54.4580000Z`; `157ms: 6aa4140b41b41dbac0c7f232.jsonl[1439] _id=6ab528de485cab4c95515a91 ts=2026-09-24T13:42:54.4580000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[1440] _id=6ab528de485cab4c95515a9b ts=2026-09-24T13:42:54.6150000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `206ms: 6aa4140b41b41dbac0c7f232.jsonl[536] _id=6ab3e03d485cab4c954d17e1 ts=2026-09-23T14:20:45.2510000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[537] _id=6ab3e03d485cab4c954d17e3 ts=2026-09-23T14:20:45.4570000Z`; `414ms: 6aa4140b41b41dbac0c7f232.jsonl[537] _id=6ab3e03d485cab4c954d17e3 ts=2026-09-23T14:20:45.4570000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[543] _id=6ab3e03d485cab4c954d17e9 ts=2026-09-23T14:20:45.8710000Z`; `214ms: 6aa4140b41b41dbac0c7f232.jsonl[543] _id=6ab3e03d485cab4c954d17e9 ts=2026-09-23T14:20:45.8710000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[538] _id=6ab3e03e485cab4c954d17eb ts=2026-09-23T14:20:46.0850000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6aa4140b41b41dbac0c7f232.jsonl[4952] _id=6aba7671485cab4c9568aa92 ts=2026-09-28T14:15:12.8840000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[4955] _id=6aba7671485cab4c9568aa9f ts=2026-09-28T14:15:12.9110000Z`; `26ms: 6aa4140b41b41dbac0c7f232.jsonl[8541] _id=6abd1d93485cab4c958b4a71 ts=2026-09-30T14:32:51.8620000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[8548] _id=6abd1d94485cab4c958b4a7b ts=2026-09-30T14:32:51.8880000Z`; `22ms: 6aa4140b41b41dbac0c7f232.jsonl[8801] _id=6abe65a1485cab4c95a728a3 ts=2026-10-01T13:52:33.7400000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[8804] _id=6abe65a1485cab4c95a728b9 ts=2026-10-01T13:52:33.7620000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 44 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `428ms: 6aa4140b41b41dbac0c7f232.jsonl[422] _id=6ab3dfa9485cab4c954d1025 ts=2026-09-23T14:18:17.3060000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[425] _id=6ab3dfa9485cab4c954d1035 ts=2026-09-23T14:18:17.7340000Z`; `301ms: 6aa4140b41b41dbac0c7f232.jsonl[27] _id=6ab3dfb7485cab4c954d10af ts=2026-09-23T14:18:31.3430000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[34] _id=6ab3dfb7485cab4c954d10b7 ts=2026-09-23T14:18:31.6440000Z`; `16ms: 6aa4140b41b41dbac0c7f232.jsonl[443] _id=6ab3dfc6485cab4c954d1193 ts=2026-09-23T14:18:46.6970000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[431] _id=6ab3dfc6485cab4c954d1195 ts=2026-09-23T14:18:46.7130000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `855ms: 6aa4140b41b41dbac0c7f232.jsonl[5976] _id=6abbc572485cab4c957e4699 ts=2026-09-29T14:04:34.6830000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[5972] _id=6abbc573485cab4c957e46ab ts=2026-09-29T14:04:35.5380000Z`; `913ms: 6aa4140b41b41dbac0c7f232.jsonl[5980] _id=6abbc575485cab4c957e4701 ts=2026-09-29T14:04:37.8320000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[5978] _id=6abbc576485cab4c957e4715 ts=2026-09-29T14:04:38.7450000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `950ms: 6aa4140b41b41dbac0c7f232.jsonl[5975] _id=6abbc572485cab4c957e468b ts=2026-09-29T14:04:34.0880000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[5971] _id=6abbc573485cab4c957e469f ts=2026-09-29T14:04:35.0380000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4140b41b41dbac0c7f232.jsonl[3214] _id=6ab67bd8485cab4c95559270 ts=2026-09-25T13:49:09.4650000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[3226] _id=6ab67bd8485cab4c95559274 ts=2026-09-25T13:49:09.4680000Z`; `2ms: 6aa4140b41b41dbac0c7f232.jsonl[10421] _id=6ac3b010de269131f9aadc37 ts=2026-10-05T14:11:28.0200000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[10419] _id=6ac3b010de269131f9aadc39 ts=2026-10-05T14:11:28.0220000Z`; `3ms: 6aa4140b41b41dbac0c7f232.jsonl[10578] _id=6ac3b187de269131f9ab3681 ts=2026-10-05T14:17:43.6160000Z ~ 6aa4140b41b41dbac0c7f232.jsonl[10579] _id=6ac3b187de269131f9ab3685 ts=2026-10-05T14:17:43.6190000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 6aa4140b41b41dbac0c7f232.jsonl[9310] _id=6abe6c5a485cab4c95a8247f ts=2026-10-01T14:21:09.3790000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9525] _id=6ac3ab03de269131f9a9e1c4 ts=2026-10-05T13:49:50.0890000Z; 71h 59m: 6aa4140b41b41dbac0c7f232.jsonl[3196] _id=6ab67bcf485cab4c955591ce ts=2026-09-25T13:49:03.2350000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4308] _id=6aba7017485cab4c95681bcf ts=2026-09-28T13:48:07.0690000Z; 24h 8m: 6aa4140b41b41dbac0c7f232.jsonl[1344] _id=6ab52864485cab4c955147ef ts=2026-09-24T13:40:52.4840000Z -> 6aa4140b41b41dbac0c7f232.jsonl[3196] _id=6ab67bcf485cab4c955591ce ts=2026-09-25T13:49:03.2350000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4140b41b41dbac0c7f232.jsonl[9501] _id=6abe6da1485cab4c95a86f32 ts=2026-10-01T14:26:41.2080000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9550] _id=6ac3ab0ade269131f9a9e357 ts=2026-10-05T13:50:02.3560000Z; 71h 18m: 6aa4140b41b41dbac0c7f232.jsonl[4298] _id=6ab6855c485cab4c955649ea ts=2026-09-25T14:29:48.4400000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4306] _id=6aba701d485cab4c95681c27 ts=2026-09-28T13:48:12.8190000Z; 23h 37m: 6aa4140b41b41dbac0c7f232.jsonl[3181] _id=6ab52f92485cab4c9551dfc7 ts=2026-09-24T14:11:30.0970000Z -> 6aa4140b41b41dbac0c7f232.jsonl[3243] _id=6ab67bdd485cab4c955592dc ts=2026-09-25T13:49:16.7700000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 628 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f232.jsonl[10116] _id=6ac3adeede269131f9aa7442 ts=2026-10-05T14:02:22.2830000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10120] _id=6ac3adeede269131f9aa7444 ts=2026-10-05T14:02:22.2840000Z; 1ms: 6aa4140b41b41dbac0c7f232.jsonl[10294] _id=6ac3af80de269131f9aabd79 ts=2026-10-05T14:09:04.2990000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10263] _id=6ac3af80de269131f9aabd7d ts=2026-10-05T14:09:04.3000000Z; 1ms: 6aa4140b41b41dbac0c7f232.jsonl[10330] _id=6ac3af9dde269131f9aac59b ts=2026-10-05T14:09:33.3400000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10331] _id=6ac3af9dde269131f9aac59d ts=2026-10-05T14:09:33.3410000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 8m 
  - Evidence: 144h 8m: 6aa4140b41b41dbac0c7f232.jsonl[640] _id=6ab3e0e0485cab4c954d2027 ts=2026-09-23T14:23:28.5100000Z -> 6aa4140b41b41dbac0c7f232.jsonl[6451] _id=6abbcbd2485cab4c957ee5eb ts=2026-09-29T14:31:46.9420000Z; 119h 43m: 6aa4140b41b41dbac0c7f232.jsonl[9303] _id=6abe6c3b485cab4c95a81747 ts=2026-10-01T14:20:43.1170000Z -> 6aa4140b41b41dbac0c7f232.jsonl[11071] _id=6ac4ffd9de269131f9b249dc ts=2026-10-06T14:04:09.5210000Z; 47h 48m: 6aa4140b41b41dbac0c7f232.jsonl[6451] _id=6abbcbd2485cab4c957ee5eb ts=2026-09-29T14:31:46.9420000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9303] _id=6abe6c3b485cab4c95a81747 ts=2026-10-01T14:20:43.1170000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4140b41b41dbac0c7f232.jsonl[9475] _id=6abe6d99485cab4c95a86d4c ts=2026-10-01T14:26:33.3980000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9528] _id=6ac3ab03de269131f9a9e1cf ts=2026-10-05T13:49:55.0040000Z; 71h 27m: 6aa4140b41b41dbac0c7f232.jsonl[4288] _id=6ab6851d485cab4c955646ec ts=2026-09-25T14:28:45.8570000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4386] _id=6aba71fa485cab4c956853d9 ts=2026-09-28T13:56:10.2850000Z; 23h 39m: 6aa4140b41b41dbac0c7f232.jsonl[3143] _id=6ab52f26485cab4c9551da85 ts=2026-09-24T14:09:42.1630000Z -> 6aa4140b41b41dbac0c7f232.jsonl[3198] _id=6ab67bd7485cab4c95559246 ts=2026-09-25T13:49:09.4040000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 195 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f232.jsonl[1346] _id=6ab5286c485cab4c955148bb ts=2026-09-24T13:40:59.2650000Z -> 6aa4140b41b41dbac0c7f232.jsonl[1352] _id=6ab5286c485cab4c955148c1 ts=2026-09-24T13:40:59.2660000Z; 1ms: 6aa4140b41b41dbac0c7f232.jsonl[1350] _id=6ab5286c485cab4c955148b1 ts=2026-09-24T13:40:59.2630000Z -> 6aa4140b41b41dbac0c7f232.jsonl[1351] _id=6ab5286c485cab4c955148b8 ts=2026-09-24T13:40:59.2640000Z; 1ms: 6aa4140b41b41dbac0c7f232.jsonl[1351] _id=6ab5286c485cab4c955148b8 ts=2026-09-24T13:40:59.2640000Z -> 6aa4140b41b41dbac0c7f232.jsonl[1346] _id=6ab5286c485cab4c955148bb ts=2026-09-24T13:40:59.2650000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4140b41b41dbac0c7f232.jsonl[9481] _id=6abe6d98485cab4c95a86d03 ts=2026-10-01T14:26:32.3960000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9643] _id=6ac3ab8ede269131f9aa00b0 ts=2026-10-05T13:52:14.6000000Z; 71h 36m: 6aa4140b41b41dbac0c7f232.jsonl[4167] _id=6ab683b4485cab4c9556330a ts=2026-09-25T14:22:44.8310000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4434] _id=6aba72b3485cab4c95686103 ts=2026-09-28T13:59:15.2290000Z; 24h 8m: 6aa4140b41b41dbac0c7f232.jsonl[2940] _id=6ab52f18485cab4c9551d915 ts=2026-09-24T14:09:27.5450000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4014] _id=6ab682a4485cab4c95561e74 ts=2026-09-25T14:18:12.6740000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f232.jsonl[8351] _id=6abd1c77485cab4c958b3c6f ts=2026-09-30T14:28:07.3750000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8352] _id=6abd1c77485cab4c958b3c73 ts=2026-09-30T14:28:07.3760000Z; 1ms: 6aa4140b41b41dbac0c7f232.jsonl[8379] _id=6abd1cad485cab4c958b3f79 ts=2026-09-30T14:29:00.8730000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8380] _id=6abd1cad485cab4c958b3f7b ts=2026-09-30T14:29:00.8740000Z; 1ms: 6aa4140b41b41dbac0c7f232.jsonl[8629] _id=6abe64af485cab4c95a6dc9a ts=2026-10-01T13:48:31.4410000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8632] _id=6abe64af485cab4c95a6dca5 ts=2026-10-01T13:48:31.4420000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4140b41b41dbac0c7f232.jsonl[9463] _id=6abe6d9b485cab4c95a86dbf ts=2026-10-01T14:26:35.1640000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9521] _id=6ac3ab03de269131f9a9e1c8 ts=2026-10-05T13:49:50.0930000Z; 71h 19m: 6aa4140b41b41dbac0c7f232.jsonl[4285] _id=6ab68518485cab4c955646b8 ts=2026-09-25T14:28:40.9390000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4309] _id=6aba701d485cab4c95681c1d ts=2026-09-28T13:48:07.0750000Z; 23h 37m: 6aa4140b41b41dbac0c7f232.jsonl[3180] _id=6ab52f91485cab4c9551dfc1 ts=2026-09-24T14:11:29.8040000Z -> 6aa4140b41b41dbac0c7f232.jsonl[3197] _id=6ab67bd7485cab4c95559244 ts=2026-09-25T13:49:03.2400000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4140b41b41dbac0c7f232.jsonl[9494] _id=6abe6d9a485cab4c95a86daf ts=2026-10-01T14:26:32.6390000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9568] _id=6ac3ab80de269131f9a9fd24 ts=2026-10-05T13:52:00.0600000Z; 72h 27m: 6aa4140b41b41dbac0c7f232.jsonl[3691] _id=6ab67d04485cab4c9555a0c4 ts=2026-09-25T13:54:11.0860000Z -> 6aa4140b41b41dbac0c7f232.jsonl[5128] _id=6aba780c485cab4c9568cc9d ts=2026-09-28T14:22:03.9270000Z; 24h 0m: 6aa4140b41b41dbac0c7f232.jsonl[8153] _id=6abd1aba485cab4c958af6c5 ts=2026-09-30T14:20:35.7310000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9313] _id=6abe6c60485cab4c95a82735 ts=2026-10-01T14:21:18.2390000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1959 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f232.jsonl[1000] _id=6ab3e275485cab4c954d3094 ts=2026-09-23T14:30:12.3920000Z -> 6aa4140b41b41dbac0c7f232.jsonl[1019] _id=6ab3e275485cab4c954d3096 ts=2026-09-23T14:30:12.3920000Z; 0ms: 6aa4140b41b41dbac0c7f232.jsonl[1012] _id=6ab3e272485cab4c954d306e ts=2026-09-23T14:30:09.4720000Z -> 6aa4140b41b41dbac0c7f232.jsonl[1013] _id=6ab3e272485cab4c954d3070 ts=2026-09-23T14:30:09.4720000Z; 0ms: 6aa4140b41b41dbac0c7f232.jsonl[1020] _id=6ab3e275485cab4c954d30a2 ts=2026-09-23T14:30:12.8940000Z -> 6aa4140b41b41dbac0c7f232.jsonl[1030] _id=6ab3e275485cab4c954d30a4 ts=2026-09-23T14:30:12.8940000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 15m 
  - Evidence: 96h 15m: 6aa4140b41b41dbac0c7f232.jsonl[2660] _id=6ab52e2f485cab4c9551cee9 ts=2026-09-24T14:05:35.7440000Z -> 6aa4140b41b41dbac0c7f232.jsonl[5194] _id=6aba77ce485cab4c9568c961 ts=2026-09-28T14:21:02.3970000Z; 47h 33m: 6aa4140b41b41dbac0c7f232.jsonl[5212] _id=6aba77e7485cab4c9568ca75 ts=2026-09-28T14:21:27.5550000Z -> 6aa4140b41b41dbac0c7f232.jsonl[6648] _id=6abd14c0485cab4c95895eaf ts=2026-09-30T13:55:12.9520000Z; 16m 42s: 6aa4140b41b41dbac0c7f232.jsonl[2318] _id=6ab529f3485cab4c955185e7 ts=2026-09-24T13:47:31.1510000Z -> 6aa4140b41b41dbac0c7f232.jsonl[2626] _id=6ab52ddd485cab4c9551cbe5 ts=2026-09-24T14:04:13.3510000Z
- **INFO / Info** `SolarStillDesignEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 41m 
  - Evidence: 23h 41m: 6aa4140b41b41dbac0c7f232.jsonl[10508] _id=6ac3b12dde269131f9ab1c15 ts=2026-10-05T14:16:13.8230000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10921] _id=6ac4fe64de269131f9b21c1a ts=2026-10-06T13:57:56.7080000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 26m 
  - Evidence: 71h 26m: 6aa4140b41b41dbac0c7f232.jsonl[4294] _id=6ab6855d485cab4c955649ee ts=2026-09-25T14:29:50.0680000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4392] _id=6aba7207485cab4c956855f5 ts=2026-09-28T13:56:23.0380000Z; 47h 39m: 6aa4140b41b41dbac0c7f232.jsonl[6263] _id=6abbc7cf485cab4c957e732a ts=2026-09-29T14:14:39.4460000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8894] _id=6abe6611485cab4c95a73ff1 ts=2026-10-01T13:54:25.0170000Z; 24h 3m: 6aa4140b41b41dbac0c7f232.jsonl[2771] _id=6ab52e9a485cab4c9551d39f ts=2026-09-24T14:07:22.4640000Z -> 6aa4140b41b41dbac0c7f232.jsonl[3910] _id=6ab680da485cab4c9555d63c ts=2026-09-25T14:10:34.3390000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.026s shown 
  - Evidence: 22ms: 6aa4140b41b41dbac0c7f232.jsonl[2458] _id=6ab52b9e485cab4c9551a579 ts=2026-09-24T13:54:38.8930000Z -> 6aa4140b41b41dbac0c7f232.jsonl[2453] _id=6ab52b9f485cab4c9551a581 ts=2026-09-24T13:54:38.9150000Z; 26ms: 6aa4140b41b41dbac0c7f232.jsonl[2453] _id=6ab52b9f485cab4c9551a581 ts=2026-09-24T13:54:38.9150000Z -> 6aa4140b41b41dbac0c7f232.jsonl[2456] _id=6ab52b9f485cab4c9551a593 ts=2026-09-24T13:54:38.9410000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6aa4140b41b41dbac0c7f232.jsonl[8800] _id=6abe65a1485cab4c95a7289e ts=2026-10-01T13:52:33.7210000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10250] _id=6ac3af80de269131f9aabd73 ts=2026-10-05T14:09:04.2830000Z; 71h 47m: 6aa4140b41b41dbac0c7f232.jsonl[4214] _id=6ab684cb485cab4c95564138 ts=2026-09-25T14:27:23.7210000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4936] _id=6aba7661485cab4c9568a92f ts=2026-09-28T14:14:57.2660000Z; 48h 16m: 6aa4140b41b41dbac0c7f232.jsonl[4945] _id=6aba7670485cab4c9568aa8f ts=2026-09-28T14:15:12.8700000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8463] _id=6abd1d34485cab4c958b472b ts=2026-09-30T14:31:16.6900000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6aa4140b41b41dbac0c7f232.jsonl[8804] _id=6abe65a1485cab4c95a728b9 ts=2026-10-01T13:52:33.7620000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10270] _id=6ac3af6dde269131f9aab92d ts=2026-10-05T14:08:45.9700000Z; 71h 47m: 6aa4140b41b41dbac0c7f232.jsonl[4215] _id=6ab684cb485cab4c9556413a ts=2026-09-25T14:27:23.7470000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4904] _id=6aba7642485cab4c9568a69d ts=2026-09-28T14:14:26.7670000Z; 48h 15m: 6aa4140b41b41dbac0c7f232.jsonl[4955] _id=6aba7671485cab4c9568aa9f ts=2026-09-28T14:15:12.9110000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8426] _id=6abd1d1b485cab4c958b45c5 ts=2026-09-30T14:30:51.6650000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.022s..0.027s shown 
  - Evidence: 22ms: 6aa4140b41b41dbac0c7f232.jsonl[8801] _id=6abe65a1485cab4c95a728a3 ts=2026-10-01T13:52:33.7400000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8804] _id=6abe65a1485cab4c95a728b9 ts=2026-10-01T13:52:33.7620000Z; 26ms: 6aa4140b41b41dbac0c7f232.jsonl[8541] _id=6abd1d93485cab4c958b4a71 ts=2026-09-30T14:32:51.8620000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8548] _id=6abd1d94485cab4c958b4a7b ts=2026-09-30T14:32:51.8880000Z; 27ms: 6aa4140b41b41dbac0c7f232.jsonl[4952] _id=6aba7671485cab4c9568aa92 ts=2026-09-28T14:15:12.8840000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4955] _id=6aba7671485cab4c9568aa9f ts=2026-09-28T14:15:12.9110000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6aa4140b41b41dbac0c7f232.jsonl[8798] _id=6abe659e485cab4c95a7275f ts=2026-10-01T13:52:29.9890000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10272] _id=6ac3af72de269131f9aaba60 ts=2026-10-05T14:08:50.4840000Z; 71h 47m: 6aa4140b41b41dbac0c7f232.jsonl[4244] _id=6ab684c8485cab4c955640d0 ts=2026-09-25T14:27:20.3360000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4906] _id=6aba7647485cab4c9568a6ed ts=2026-09-28T14:14:31.8130000Z; 48h 15m: 6aa4140b41b41dbac0c7f232.jsonl[4940] _id=6aba766e485cab4c9568aa13 ts=2026-09-28T14:15:10.4140000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8417] _id=6abd1d1c485cab4c958b45df ts=2026-09-30T14:30:52.7590000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 83 interval(s) ≤ 0.016s..0.018s shown 
  - Evidence: 16ms: 6aa4140b41b41dbac0c7f232.jsonl[443] _id=6ab3dfc6485cab4c954d1193 ts=2026-09-23T14:18:46.6970000Z -> 6aa4140b41b41dbac0c7f232.jsonl[431] _id=6ab3dfc6485cab4c954d1195 ts=2026-09-23T14:18:46.7130000Z; 16ms: 6aa4140b41b41dbac0c7f232.jsonl[8792] _id=6abe659d485cab4c95a7270b ts=2026-10-01T13:52:29.1990000Z -> 6aa4140b41b41dbac0c7f232.jsonl[8784] _id=6abe659d485cab4c95a72719 ts=2026-10-01T13:52:29.2150000Z; 18ms: 6aa4140b41b41dbac0c7f232.jsonl[10298] _id=6ac3af8bde269131f9aac07b ts=2026-10-05T14:09:15.3300000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10299] _id=6ac3af8bde269131f9aac07f ts=2026-10-05T14:09:15.3480000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 51m 
  - Evidence: 143h 51m: 6aa4140b41b41dbac0c7f232.jsonl[4295] _id=6ab68565485cab4c95564a1e ts=2026-09-25T14:29:57.2060000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9285] _id=6abe6c55485cab4c95a82227 ts=2026-10-01T14:21:09.2920000Z; 95h 19m: 6aa4140b41b41dbac0c7f232.jsonl[9507] _id=6abe6e77485cab4c95a8a025 ts=2026-10-01T14:30:14.6560000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9515] _id=6ac3aafede269131f9a9e0e8 ts=2026-10-05T13:49:50.0260000Z; 23h 46m: 6aa4140b41b41dbac0c7f232.jsonl[10130] _id=6ac3adffde269131f9aa7636 ts=2026-10-05T14:02:39.4580000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10773] _id=6ac4fc71de269131f9b19035 ts=2026-10-06T13:49:37.8950000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 6aa4140b41b41dbac0c7f232.jsonl[9505] _id=6abe6e6a485cab4c95a89da9 ts=2026-10-01T14:30:01.4490000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9514] _id=6ac3aaf9de269131f9a9dfda ts=2026-10-05T13:49:45.3000000Z; 71h 59m: 6aa4140b41b41dbac0c7f232.jsonl[3200] _id=6ab67bc9485cab4c95559124 ts=2026-09-25T13:48:57.5430000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4304] _id=6aba7010485cab4c95681bbf ts=2026-09-28T13:48:00.7330000Z; 24h 6m: 6aa4140b41b41dbac0c7f232.jsonl[4331] _id=6aba70cf485cab4c95682913 ts=2026-09-28T13:51:10.8950000Z -> 6aa4140b41b41dbac0c7f232.jsonl[5659] _id=6abbc3d4485cab4c957e19fb ts=2026-09-29T13:57:39.9490000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 6aa4140b41b41dbac0c7f232.jsonl[9506] _id=6abe6e69485cab4c95a89d9a ts=2026-10-01T14:30:01.4490000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9513] _id=6ac3aaf9de269131f9a9dfce ts=2026-10-05T13:49:45.3000000Z; 71h 29m: 6aa4140b41b41dbac0c7f232.jsonl[4042] _id=6ab682cf485cab4c955622de ts=2026-09-25T14:18:55.8220000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4303] _id=6aba7010485cab4c95681bbd ts=2026-09-28T13:48:00.7320000Z; 24h 6m: 6aa4140b41b41dbac0c7f232.jsonl[4330] _id=6aba70ce485cab4c9568290d ts=2026-09-28T13:51:10.8940000Z -> 6aa4140b41b41dbac0c7f232.jsonl[5658] _id=6abbc3d4485cab4c957e19f9 ts=2026-09-29T13:57:39.9480000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4140b41b41dbac0c7f232.jsonl[9504] _id=6abe6da4485cab4c95a87007 ts=2026-10-01T14:26:44.8520000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10703] _id=6ac3b2f2de269131f9ab94f2 ts=2026-10-05T14:23:46.6460000Z; 72h 13m: 6aa4140b41b41dbac0c7f232.jsonl[4040] _id=6ab682c8485cab4c955621f2 ts=2026-09-25T14:18:48.1070000Z -> 6aa4140b41b41dbac0c7f232.jsonl[5651] _id=6aba7a8f485cab4c9568f435 ts=2026-09-28T14:32:47.1400000Z; 23h 40m: 6aa4140b41b41dbac0c7f232.jsonl[1315] _id=6ab3e2ac485cab4c954d3474 ts=2026-09-23T14:31:08.1420000Z -> 6aa4140b41b41dbac0c7f232.jsonl[3182] _id=6ab52f92485cab4c9551dfcb ts=2026-09-24T14:11:30.3360000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 6aa4140b41b41dbac0c7f232.jsonl[9308] _id=6abe6c5a485cab4c95a82457 ts=2026-10-01T14:21:09.3710000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9542] _id=6ac3ab05de269131f9a9e274 ts=2026-10-05T13:49:55.0610000Z; 71h 18m: 6aa4140b41b41dbac0c7f232.jsonl[4296] _id=6ab6855b485cab4c955649de ts=2026-09-25T14:29:47.6200000Z -> 6aa4140b41b41dbac0c7f232.jsonl[4305] _id=6aba701d485cab4c95681c23 ts=2026-09-28T13:48:12.8120000Z; 23h 39m: 6aa4140b41b41dbac0c7f232.jsonl[3156] _id=6ab52f36485cab4c9551db25 ts=2026-09-24T14:09:58.7180000Z -> 6aa4140b41b41dbac0c7f232.jsonl[3214] _id=6ab67bd8485cab4c95559270 ts=2026-09-25T13:49:09.4650000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f232.jsonl[10774] _id=6ac4fc7dde269131f9b19363 ts=2026-10-06T13:49:47.0540000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10775] _id=6ac4fc7dde269131f9b19368 ts=2026-10-06T13:49:47.0550000Z; 1ms: 6aa4140b41b41dbac0c7f232.jsonl[9834] _id=6ac3ac15de269131f9aa1f5a ts=2026-10-05T13:54:29.1880000Z -> 6aa4140b41b41dbac0c7f232.jsonl[9835] _id=6ac3ac15de269131f9aa1f62 ts=2026-10-05T13:54:29.1890000Z; 2ms: 6aa4140b41b41dbac0c7f232.jsonl[10421] _id=6ac3b010de269131f9aadc37 ts=2026-10-05T14:11:28.0200000Z -> 6aa4140b41b41dbac0c7f232.jsonl[10419] _id=6ac3b010de269131f9aadc39 ts=2026-10-05T14:11:28.0220000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[396] _id=6ab3df57485cab4c954d0c55 ts=2026-09-23T14:16:55.6450000Z`; `6aa4140b41b41dbac0c7f232.jsonl[556] _id=6ab3e055485cab4c954d18e9 ts=2026-09-23T14:21:09.8900000Z`; `6aa4140b41b41dbac0c7f232.jsonl[2556] _id=6ab52cfb485cab4c9551c01f ts=2026-09-24T14:00:27.4980000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 152 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[898] _id=6ab3e268485cab4c954d2fe4 ts=2026-09-23T14:29:59.5660000Z`; `6aa4140b41b41dbac0c7f232.jsonl[976] _id=6ab3e268485cab4c954d2fe8 ts=2026-09-23T14:29:59.6040000Z`; `6aa4140b41b41dbac0c7f232.jsonl[974] _id=6ab3e268485cab4c954d2fea ts=2026-09-23T14:30:00.2450000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 308 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[851] _id=6ab3e25b485cab4c954d2e50 ts=2026-09-23T14:28:01.6450000Z`; `6aa4140b41b41dbac0c7f232.jsonl[805] _id=6ab3e25b485cab4c954d2e56 ts=2026-09-23T14:28:09.9100000Z`; `6aa4140b41b41dbac0c7f232.jsonl[856] _id=6ab3e25c485cab4c954d2e80 ts=2026-09-23T14:28:11.5960000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[4955] _id=6aba7671485cab4c9568aa9f ts=2026-09-28T14:15:12.9110000Z`; `6aa4140b41b41dbac0c7f232.jsonl[8548] _id=6abd1d94485cab4c958b4a7b ts=2026-09-30T14:32:51.8880000Z`; `6aa4140b41b41dbac0c7f232.jsonl[8804] _id=6abe65a1485cab4c95a728b9 ts=2026-10-01T13:52:33.7620000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[431] _id=6ab3dfc6485cab4c954d1195 ts=2026-09-23T14:18:46.7130000Z`; `6aa4140b41b41dbac0c7f232.jsonl[440] _id=6ab3dfcc485cab4c954d11fb ts=2026-09-23T14:18:52.8780000Z`; `6aa4140b41b41dbac0c7f232.jsonl[449] _id=6ab3dfce485cab4c954d1211 ts=2026-09-23T14:18:53.9750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[9285] _id=6abe6c55485cab4c95a82227 ts=2026-10-01T14:21:09.2920000Z`; `6aa4140b41b41dbac0c7f232.jsonl[9507] _id=6abe6e77485cab4c95a8a025 ts=2026-10-01T14:30:14.6560000Z`; `6aa4140b41b41dbac0c7f232.jsonl[9515] _id=6ac3aafede269131f9a9e0e8 ts=2026-10-05T13:49:50.0260000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[4305] _id=6aba701d485cab4c95681c23 ts=2026-09-28T13:48:12.8120000Z`; `6aa4140b41b41dbac0c7f232.jsonl[7190] _id=6abd15e9485cab4c95897a9b ts=2026-09-30T14:00:09.2140000Z`; `6aa4140b41b41dbac0c7f232.jsonl[7687] _id=6abd1852485cab4c958a7df4 ts=2026-09-30T14:10:26.7960000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[6459] _id=6abbcda7485cab4c957f07f5 ts=?`; `6aa4140b41b41dbac0c7f232.jsonl[6549] _id=6abd12ca485cab4c958937ff ts=?`; `6aa4140b41b41dbac0c7f232.jsonl[9518] _id=6ac3ab03de269131f9a9e1bc ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 401 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[1001] _id=6ab3e275485cab4c954d3099 ts=2026-09-23T14:30:12.4160000Z`; `6aa4140b41b41dbac0c7f232.jsonl[1030] _id=6ab3e275485cab4c954d30a4 ts=2026-09-23T14:30:12.8940000Z`; `6aa4140b41b41dbac0c7f232.jsonl[1021] _id=6ab3e275485cab4c954d30a6 ts=2026-09-23T14:30:12.8970000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 567 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[809] _id=6ab3e25c485cab4c954d2e6a ts=2026-09-23T14:28:11.4820000Z`; `6aa4140b41b41dbac0c7f232.jsonl[843] _id=6ab3e25c485cab4c954d2e6c ts=2026-09-23T14:28:11.5070000Z`; `6aa4140b41b41dbac0c7f232.jsonl[828] _id=6ab3e25c485cab4c954d2e72 ts=2026-09-23T14:28:11.5400000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 25 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[2453] _id=6ab52b9f485cab4c9551a581 ts=2026-09-24T13:54:38.9150000Z`; `6aa4140b41b41dbac0c7f232.jsonl[2456] _id=6ab52b9f485cab4c9551a593 ts=2026-09-24T13:54:38.9410000Z`; `6aa4140b41b41dbac0c7f232.jsonl[2517] _id=6ab52c7b485cab4c9551b961 ts=2026-09-24T13:58:19.3300000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 11 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[8432] _id=6abd1d26485cab4c958b4674 ts=2026-09-30T14:31:02.6910000Z`; `6aa4140b41b41dbac0c7f232.jsonl[8700] _id=6abe657b485cab4c95a71c07 ts=2026-10-01T13:51:55.5550000Z`; `6aa4140b41b41dbac0c7f232.jsonl[8713] _id=6abe657c485cab4c95a71c51 ts=2026-10-01T13:51:56.0500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[532] _id=6ab3e03b485cab4c954d17cb ts=2026-09-23T14:20:43.1090000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 chatEvent record in 'Unit 5 Dev - Dungeon' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[9507] _id=6abe6e77485cab4c95a8a025 ts=2026-10-01T14:30:14.6560000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 409 start, 403 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 170 unmatched 'BecameCameraCentered' (totals: 592 open, 574 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 189 unmatched 'BecameVisible' (totals: 813 open, 932 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 28 open, 26 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 144 open, 156 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 49 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 276 of 11069 adjacent _id pairs reverse in client time; worst 105.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f232.jsonl[827] _id=6ab3e25a485cab4c954d2e3a ts=2026-09-23T14:29:46.3400000Z`; `6aa4140b41b41dbac0c7f232.jsonl[849] _id=6ab3e25b485cab4c954d2e44 ts=2026-09-23T14:28:01.2590000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -106.08s, max +2.64s over 11070 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f232\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3042 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (519); Unit 4 Dev - Dungeon (509); Unit 4 Dev (435); Unit 3 Dev (431); Unit 3 Dungeon Dev (317); Unit 5 Dev (302); Unit 5 Dev - Dungeon (281); Unit 1 Dev (151); Unit 4 Dev - Anderson Base (97)
- **Intervals:** median 0.85s (p5 0.02s / p95 20.09s, n=3041)
- **Fields under `data`:**

```text
data.Value  (string, 3042/3042 records)
    "pressed"  x3042
data.actionType  (string, 3042/3042 records)
    "Move"  x2035
    "Interact"  x476
    "Jump"  x375
    "Hoverboard"  x55
    "Ascend"  x52
    "Descend"  x28
    "Map"  x15
    "Sprint"  x4
    "Pause"  x2
data.key  (string, 3042/3042 records, 11 empty-string)
    14 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3042/3042 records)
    "Player"  x2677
    "Drone"  x365
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2911 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1943); Unit 4 Dev (432); Unit 5 Dev - Dungeon (288); Unit 3 Dungeon Dev (248)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.09s, n=2910)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2911/2911 records)
    "BecameInvisible"  x932
    "BecameVisible"  x813
    "BecameCameraCentered"  x592
    "BecameCameraUncentered"  x574
data.pieceId  (string, 2911/2911 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2911/2911 records)
    1678 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2155 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (569); Unit 3 Dev (319); Unit 5 Dev (303); Unit 4 Dev (219); Unit 1 Dev (197); Unit 3 Dungeon Dev (175); Unit 4 Dev - Anderson Base (160); Unit 4 Dev - Dungeon (136); Unit 5 Dev - Dungeon (77)
- **eventKey:** present on 1343 of 2155 records
- **Intervals:** median 3.32s (p5 0.00s / p95 34.61s, n=2154)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1343; [conversationId, dialogueEventType] x812
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2155/2155 records)
    numeric range 8 .. 118 (53 unique)
data.dialogueEventType  (string, 2155/2155 records)
    "DialogueNodeEvent"  x1343
    "DialogueStartEvent"  x409
    "DialogueFinishEvent"  x403
data.nodeId  (number, 1343/2155 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1854 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (470); Unit 3 Dev (310); Unit 4 Dev (242); Unit 5 Dev (212); Unit 1 Dev (159); Unit 3 Dungeon Dev (137); Unit 4 Dev - Dungeon (118); Unit 5 Dev - Dungeon (109); Unit 4 Dev - Anderson Base (97)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.03s, n=1842)
- **Fields under `data`:**

```text
data.position  (object, 1854/1854 records)
data.position.x  (number, 1854/1854 records)
    numeric range -684.593 .. 1557.57 (516 unique)
data.position.y  (number, 1854/1854 records)
    numeric range -113.807 .. 222.002 (390 unique)
data.position.z  (number, 1854/1854 records)
    numeric range -1134.53 .. 1801.6 (513 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 340 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (134); Unit 1 Dev (84); Unit 5 Dev (72); Unit 3 Dev (33); Unit 2 Prod (Refactor) (17)
- **Intervals:** median 0.35s (p5 0.02s / p95 5.74s, n=339)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 340/340 records)
    "argumentationNodeHoverEnd"  x156
    "argumentationNodeHoverStart"  x144
    "argumentationNodeAdd"  x32
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 340/340 records)
    "Unit 4 - Flooding"  x134
    "Unit 5"  x72
    "Unit 1 - Freshwater"  x51
    "Unit 1 - Argumentation Tutorial"  x33
    "Unit 3 - Pollution Upstream"  x33
    "Unit 2 – Watershed"  x17
data.nodeName  (string, 340/340 records)
    "1"  x49
    "A"  x48
    "I"  x43
    "B"  x40
    "4"  x34
    "II"  x32
    "C"  x30
    "3"  x23
    "2"  x21
    "D"  x17
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 301 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (110); Unit 2 Prod (Refactor) (50); Unit 3 Dungeon Dev (45); Unit 5 Dev (25); Unit 4 Dev - Anderson Base (18); Unit 4 Dev (17); Unit 3 Dev (13); Unit 5 Dev - Dungeon (13); Unit 1 Dev (10)
- **Intervals:** median 6.33s (p5 0.38s / p95 410.52s, n=300)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 301/301 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 301/301 records)
    101 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 97 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (49); Unit 3 Dev (40); Unit 4 Dev (8)
- **Intervals:** median 2.87s (p5 0.21s / p95 21711.25s, n=96)
- **`data` key-set variants:** [actionType, featureUsed] x54; [actionType, featureUsed, location] x40; [actionType, featureUsed, legendName] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 97/97 records)
    "WaypointMoveEvent"  x33
    "MapOpenEvent"  x28
    "MapCloseEvent"  x26
    "WaypointSetEvent"  x5
    "Selected"  x2
    "WaypointResetEvent"  x2
    "Unselected"  x1
data.featureUsed  (string, 97/97 records)
    "Map"  x54
    "Waypoint"  x40
    "Legend"  x3
data.legendName  (string, 3/97 records)
    "300 ft"  x2
    "360 ft"  x1
data.location  (object, 40/97 records)
data.location.x  (number, 40/97 records)
    numeric range -346.09 .. 277.91 (28 unique)
data.location.y  (number, 40/97 records)
    numeric range -285.5 .. 335.5 (29 unique)
data.location.z  (number, 40/97 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 87 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 4 Dev - Dungeon (14); Unit 1 Dev (12); Unit 5 Dev (11); Unit 3 Dev (9); Unit 4 Dev (9); Unit 5 Dev - Dungeon (8); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 87 of 87 records
- **Intervals:** median 160.73s (p5 0.00s / p95 84458.89s, n=86)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 87/87 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x38
data.questID  (string, 87/87 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 87/87 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/87 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (20); Unit 4 Dev (10)
- **Intervals:** median 1.01s (p5 0.17s / p95 216.46s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x50; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/58 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/58 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 50/58 records)
    "RightDrag"  x28
    "LeftDrag"  x22
data.currentSoilType  (string, 50/58 records)
    "SAND"  x12
    "CLAYSAND"  x10
    "CLAY"  x8
    "CLAYROCK"  x8
    "SANDGRAVEL"  x7
    "BEDROCK"  x3
    "GRAVEL"  x2
data.isCorrectSelection  (string, 50/58 records)
    "false"  x39
    "true"  x11
data.waterLevelStatus  (string, 50/58 records)
    "Proper"  x23
    "TooHigh"  x21
    "TooLow"  x6
data.waterRetentionChange  (string, 50/58 records)
    "Increase"  x20
    "Decrease"  x19
    "NoChange"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 34 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (5); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (3); Unit 5 Dev - Dungeon (2); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1005.64s (p5 1.74s / p95 155011.40s, n=33)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 34/34 records)
    true  x34
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 32 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (12); Unit 4 Dev - Anderson Base (11); Unit 5 Dev (6); Unit 3 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 9.55s (p5 0.19s / p95 216108.68s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "submitAnswerEvent"  x32
data.answerSubmitted  (string, 32/32 records)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 32/32 records)
    "Unit 1 - Freshwater"  x11
    "Unit 4 - Flooding"  x11
    "Unit 5"  x6
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 4.49s (p5 0.93s / p95 139.55s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Clay"  x11
    "Bedrock"  x6
    "Gravel"  x6
    "Sand"  x3
data.floor  (string, 26/26 records)
    "5"  x12
    "4"  x10
    "3"  x4
data.machine  (string, 26/26 records)
    "1"  x25
    "2"  x1
data.row  (string, 26/26 records)
    "TopRow"  x18
    "BottomRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 24 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (24)
- **Intervals:** median 9.40s (p5 1.43s / p95 58.15s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "On"  x18
    "Off"  x6
data.floor  (string, 24/24 records)
    "3"  x12
    "4"  x7
    "2"  x3
    "1"  x2
data.machineNumber  (string, 24/24 records)
    "One"  x23
    "Two"  x1
data.machineType  (string, 24/24 records)
    "Condenser"  x12
    "DualChamber_Condenser"  x4
    "Evaporator"  x4
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 24/24 records)
    "2"  x13
    "1"  x5
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowUnfocusEvent` — 22 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dungeon Dev (5); Unit 4 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev - Dungeon (3); Unit 5 Dev (2)
- **Intervals:** median 1009.31s (p5 1.51s / p95 260039.03s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 20 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (5); Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1)
- **Intervals:** median 1690.51s (p5 208.34s / p95 267601.52s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "DebugMenuStateChanged"  x20
data.isOpened  (bool, 20/20 records)
    false  x20
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 2502.39s (p5 388.26s / p95 275951.32s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 53.67s (p5 0.02s / p95 280460.32s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 17/17 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 4 - Flooding"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 9 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (9)
- **Intervals:** median 1.82s (p5 1.13s / p95 55448.59s, n=8)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x7; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "optionSelected"  x7
    "DesignSubmitted"  x2
data.designSelections  (object, 2/9 records)
data.designSelections.glassRoofTemperature  (string, 2/9 records)
    "Cold"  x1
    "Hot"  x1
data.designSelections.roofCovering  (string, 2/9 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/9 records)
    "Tilted Out"  x2
data.featureUsed  (string, 9/9 records)
    "RoofStyle"  x3
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x2
    "Submit"  x2
data.selectedOption  (string, 7/9 records)
    "Tilted Out"  x2
    "Cold"  x1
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 2.78s (p5 1.03s / p95 16.63s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x3
data.boxId  (string, 7/7 records)
    "1"  x4
    "2"  x2
    "0"  x1
data.soilType  (string, 7/7 records)
    "Sand"  x4
    "Gravel"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 7 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 43193.93s (p5 139.56s / p95 474197.91s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "Close"  x6
    "Open"  x1
data.chatID  (string, 7/7 records)
    "NA"  x6
    "[20-70, 20-71, 20-73, 20-74, 20-76]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 431006.40s (p5 198023.20s / p95 510109.23s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x1
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit4"  x2
    "unit5"  x2
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationToolEvent` — 3 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3)
- **Intervals:** median 2.16s (p5 1.28s / p95 3.03s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "argumentationToolOpen"  x2
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 3/3 records)
    "Unit 1 - Freshwater"  x3
data.toolName  (string, 3/3 records)
    "BackingInfoPanel - "  x3
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.47s (p5 2.47s / p95 2.47s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (28 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "Unselected" (1x); "WaypointMoveEvent" (33x); "WaypointResetEvent" (2x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (3x); "Waypoint" (40x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*