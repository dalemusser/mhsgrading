# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b23

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b23
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b23.jsonl
- **Records:** 15851 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b23
- **Time span:** 2026-10-05T16:31:44.582000+00:00 .. 2026-10-16T16:47:39.415000+00:00 (264h 15m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b23\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 15851 records, 10 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 91 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8188 | 51.66 | 1 | 9 | 0 | 2026-10-05T16:31:56.396000+00:00 | 2026-10-16T16:47:39.415000+00:00 | 264h 15m |
| PuzzlePieceVisibleEvent | 2509 | 15.83 | 1 | 4 | 0 | 2026-10-05T17:02:31.629000+00:00 | 2026-10-16T16:18:09.113000+00:00 | 263h 15m |
| DialogueEvent | 2221 | 14.01 | 1 | 9 | 1374 | 2026-10-05T16:32:16.280000+00:00 | 2026-10-16T16:47:28.925000+00:00 | 264h 15m |
| PlayerPositionEvent | 1770 | 11.17 | 1 | 9 | 0 | 2026-10-05T16:31:52.863000+00:00 | 2026-10-16T16:47:32.467000+00:00 | 264h 15m |
| ObjectInterEvent | 380 | 2.4 | 1 | 9 | 0 | 2026-10-05T16:36:52.725000+00:00 | 2026-10-16T16:47:39.415000+00:00 | 264h 10m |
| argumentationNodeEvent | 309 | 1.95 | 1 | 5 | 0 | 2026-10-05T16:52:39.832000+00:00 | 2026-10-16T16:34:51.149000+00:00 | 263h 42m |
| questEvent | 90 | 0.57 | 1 | 9 | 90 | 2026-10-05T16:32:16.252000+00:00 | 2026-10-16T16:43:54.375000+00:00 | 264h 11m |
| Soil Key Puzzle | 81 | 0.51 | 1 | 3 | 0 | 2026-10-07T16:45:14.798000+00:00 | 2026-10-14T16:49:15.315000+00:00 | 168h 4m |
| soilMachine | 54 | 0.34 | 1 | 1 | 0 | 2026-10-14T16:59:23.034000+00:00 | 2026-10-15T16:27:35.252000+00:00 | 23h 28m |
| TopographicMapEvent | 51 | 0.32 | 1 | 2 | 0 | 2026-10-05T16:59:18.469000+00:00 | 2026-10-14T16:33:45.804000+00:00 | 215h 34m |
| DEBUGMenu | 32 | 0.2 | 1 | 9 | 0 | 2026-10-05T16:31:52.843000+00:00 | 2026-10-16T16:17:16.336000+00:00 | 263h 45m |
| WaterChamberEvent | 31 | 0.2 | 1 | 1 | 0 | 2026-10-16T15:29:31.721000+00:00 | 2026-10-16T16:24:11.281000+00:00 | 54m 39s |
| gameWindowFocusEvent | 27 | 0.17 | 1 | 5 | 0 | 2026-10-05T16:31:44.582000+00:00 | 2026-10-16T16:17:56.019000+00:00 | 263h 46m |
| argumentationAnswerEvent | 26 | 0.16 | 1 | 5 | 0 | 2026-10-05T16:52:55.978000+00:00 | 2026-10-16T16:37:20.162000+00:00 | 263h 44m |
| gameWindowUnfocusEvent | 19 | 0.12 | 1 | 7 | 0 | 2026-10-05T16:32:20.360000+00:00 | 2026-10-16T16:17:55.236000+00:00 | 263h 45m |
| argumentationEvent | 15 | 0.09 | 1 | 5 | 0 | 2026-10-05T16:52:36.264000+00:00 | 2026-10-16T16:37:04.210000+00:00 | 263h 44m |
| gameStartEvent | 14 | 0.09 | 1 | 1 | 0 | 2026-10-05T16:31:44.583000+00:00 | 2026-10-16T16:17:07.538000+00:00 | 263h 45m |
| argumentationToolEvent | 9 | 0.06 | 1 | 3 | 0 | 2026-10-05T16:52:33.338000+00:00 | 2026-10-16T16:37:23.278000+00:00 | 263h 44m |
| SolarStillDesignEvent | 7 | 0.04 | 1 | 1 | 0 | 2026-10-16T16:41:06.697000+00:00 | 2026-10-16T16:41:20.759000+00:00 | 14.1s |
| TerasGardenBox | 7 | 0.04 | 1 | 1 | 0 | 2026-10-15T16:49:38.236000+00:00 | 2026-10-15T16:50:43.184000+00:00 | 1m 4s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-05T16:57:18.980000+00:00 | 2026-10-16T16:47:39.379000+00:00 | 263h 50m |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-15T17:00:48.208000+00:00 | 2026-10-16T16:25:02.414000+00:00 | 23h 24m |
| DaniEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-16T16:37:36.571000+00:00 | 2026-10-16T16:37:38.528000+00:00 | 2.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173433.605s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.058s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.566s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.479s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 25.852s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.819s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3281.565s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 76437.814s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 789.645s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 791.099s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.262s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` — record volume changed 3.4x vs baseline. 
  - Observed: 8188 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,II; A,C,3,4,II; A,C,D,4,3,II; B,1,I; C,1,II; C,2,II; C,3,II; C,4,II; C,D,3,II; C,D,A,2,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 27 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 10.8x vs baseline. 
  - Observed: 54 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[167] _id=6ac3d28fde269131f9ade449 ts=2026-10-05T16:38:38.9450000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[231] _id=6ac3d364de269131f9adf377 ts=2026-10-05T16:42:11.0560000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[288] _id=6ac3d40dde269131f9ae008e ts=2026-10-05T16:44:59.8670000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[0] _id=6ac3d0f1de269131f9adbfcd ts=2026-10-05T16:31:44.5830000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[726] _id=6ac3d747de269131f9ae527c ts=2026-10-05T16:58:46.8180000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[986] _id=6ac524cade269131f9b52809 ts=2026-10-06T16:41:45.9080000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[9] _id=6ac3d0f1de269131f9adbfc6 ts=2026-10-05T16:31:44.5820000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[23] _id=6ac3d117de269131f9adc54f ts=2026-10-05T16:32:22.3790000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[717] _id=6ac3d747de269131f9ae5277 ts=2026-10-05T16:58:46.8170000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[16] _id=6ac3d115de269131f9adc501 ts=2026-10-05T16:32:20.3600000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[987] _id=6ac524cade269131f9b52801 ts=2026-10-05T17:04:16.342Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[2746] _id=6ac6748ede269131f9bc95e6 ts=2026-10-06T17:04:15.339Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8187 | 0.0 | 0.369 | 116.202 | 2.795 | 429287.088 | 0.52 | 517 | 9 |
| PuzzlePieceVisibleEvent | 2508 | 0.0 | 0.058 | 377.886 | 1.827 | 433179.889 | 0.16 | 1203 | 10 |
| DialogueEvent | 2220 | 0.0 | 3.694 | 428.519 | 30.418 | 429336.901 | 0.14 | 634 | 9 |
| PlayerPositionEvent | 1756 | 0.0 | 10.001 | 498.501 | 10.231 | 429288.724 | 0.12 | 2 | 8 |
| ObjectInterEvent | 379 | 0.0 | 7.682 | 2509.358 | 340.186 | 429407.426 | 0.02 | 3 | 12 |
| argumentationNodeEvent | 308 | 0.025 | 0.798 | 3082.245 | 11.373 | 431236.346 | 0.02 | 29 | 4 |
| questEvent | 89 | 0.0 | 165.33 | 10686.496 | 82957.075 | 429515.29 | 0.01 | 18 | 13 |
| Soil Key Puzzle | 80 | 0.001 | 1.582 | 7563.006 | 28.723 | 432866.721 | 0.01 | 2 | 3 |
| soilMachine | 53 | 0.222 | 5.262 | 1594.193 | 157.079 | 75859.126 | 0.04 | 0 | 2 |
| TopographicMapEvent | 50 | 0.029 | 7.566 | 15521.347 | 85781.105 | 429398.713 | 0.0 | 2 | 7 |
| DEBUGMenu | 31 | 8.011 | 645.483 | 30629.79 | 85980.833 | 429619.119 | 0.0 | 0 | 18 |
| WaterChamberEvent | 30 | 0.438 | 6.479 | 109.319 | 76.714 | 2731.901 | 0.55 | 0 | 1 |
| gameWindowFocusEvent | 26 | 20.106 | 789.645 | 36521.978 | 86011.032 | 429634.349 | 0.0 | 0 | 13 |
| argumentationAnswerEvent | 25 | 1.116 | 25.852 | 37978.567 | 241812.233 | 431291.493 | 0.0 | 0 | 4 |
| gameWindowUnfocusEvent | 18 | 2.224 | 791.099 | 52751.938 | 163790.793 | 602344.306 | 0.0 | 0 | 9 |
| argumentationEvent | 14 | 0.037 | 111.773 | 67819.139 | 319287.483 | 431236.435 | 0.0 | 1 | 4 |
| gameStartEvent | 13 | 1230.616 | 76437.814 | 73040.227 | 223704.784 | 429634.349 | 0.0 | 0 | 13 |
| argumentationToolEvent | 8 | 0.548 | 2.819 | 118686.242 | 539388.531 | 690326.718 | 0.0 | 0 | 2 |
| SolarStillDesignEvent | 6 | 1.421 | 1.995 | 2.344 | 4.069 | 4.604 | 25.6 | 0 | 0 |
| TerasGardenBox | 6 | 1.232 | 3.455 | 10.825 | 27.793 | 28.135 | 5.54 | 0 | 0 |
| EndOfUnit | 4 | 85667.832 | 173433.605 | 237455.1 | 478581.886 | 517285.357 | 0.0 | 0 | 4 |
| chatEvent | 3 | 466.263 | 3281.565 | 28084.735 | 72783.897 | 80506.378 | 0.0 | 0 | 2 |
| DaniEvent | 1 | 1.957 | 1.957 | 1.957 | 1.957 | 1.957 | 30.66 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 15 group(s), 31 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[2915] _id=6ac6758ade269131f9bcc91a ts=2026-10-07T16:38:33.7460000Z == 6ab9a8e69a8420a1e6b56b23.jsonl[2916] _id=6ac6758ade269131f9bcc91b ts=2026-10-07T16:38:33.7460000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[2946] _id=6ac67591de269131f9bccada ts=2026-10-07T16:38:40.7710000Z == 6ab9a8e69a8420a1e6b56b23.jsonl[2947] _id=6ac67591de269131f9bccadb ts=2026-10-07T16:38:40.7710000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[3196] _id=6ac676bfde269131f9bd0139 ts=2026-10-07T16:43:42.2930000Z == 6ab9a8e69a8420a1e6b56b23.jsonl[3197] _id=6ac676bfde269131f9bd013a ts=2026-10-07T16:43:42.2930000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 96 group(s), 163 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[802] _id=6ac3d834de269131f9ae6aa3 ts=2026-10-05T17:02:42.5890000Z == 6ab9a8e69a8420a1e6b56b23.jsonl[777] _id=6ac3d834de269131f9ae6ab5 ts=2026-10-05T17:02:42.5890000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[940] _id=6ac3d836de269131f9ae6af1 ts=2026-10-05T17:02:45.0580000Z == 6ab9a8e69a8420a1e6b56b23.jsonl[881] _id=6ac3d836de269131f9ae6b05 ts=2026-10-05T17:02:45.0580000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[803] _id=6ac3d836de269131f9ae6afd ts=2026-10-05T17:02:45.0580000Z == 6ab9a8e69a8420a1e6b56b23.jsonl[804] _id=6ac3d836de269131f9ae6aff ts=2026-10-05T17:02:45.0580000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[15574] _id=6ad25272de269131f9e5f3b3 ts=2026-10-16T16:36:01.6150000Z == 6ab9a8e69a8420a1e6b56b23.jsonl[15575] _id=6ad25272de269131f9e5f3b4 ts=2026-10-16T16:36:01.6150000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 6ab9a8e69a8420a1e6b56b23.jsonl[90] _id=6ac3d225de269131f9adda79 ts=2026-10-05T16:36:52.7250000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[55] _id=6ac3d225de269131f9adda7d ts=2026-10-05T16:36:52.7370000Z`; `704ms: 6ab9a8e69a8420a1e6b56b23.jsonl[8619] _id=6acfad74de269131f9d5730e ts=2026-10-14T16:27:32.4960000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[8611] _id=6acfad75de269131f9d5731c ts=2026-10-14T16:27:33.2000000Z`; `536ms: 6ab9a8e69a8420a1e6b56b23.jsonl[11559] _id=6acfd45ade269131f9d851dd ts=2026-10-14T19:13:29.3010000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[11552] _id=6acfd45ade269131f9d851f4 ts=2026-10-14T19:13:29.8370000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 192 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `166ms: 6ab9a8e69a8420a1e6b56b23.jsonl[840] _id=6ac3d836de269131f9ae6aeb ts=2026-10-05T17:02:44.8920000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[940] _id=6ac3d836de269131f9ae6af1 ts=2026-10-05T17:02:45.0580000Z`; `26ms: 6ab9a8e69a8420a1e6b56b23.jsonl[799] _id=6ac3d843de269131f9ae6bf9 ts=2026-10-05T17:02:57.1560000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[829] _id=6ac3d843de269131f9ae6bfd ts=2026-10-05T17:02:57.1820000Z`; `23ms: 6ab9a8e69a8420a1e6b56b23.jsonl[801] _id=6ac3d844de269131f9ae6c09 ts=2026-10-05T17:02:57.6740000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[787] _id=6ac3d844de269131f9ae6c0d ts=2026-10-05T17:02:57.6970000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6ab9a8e69a8420a1e6b56b23.jsonl[2612] _id=6ac528a5de269131f9b5c38a ts=2026-10-06T16:58:12.4210000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[2614] _id=6ac528a5de269131f9b5c3a8 ts=2026-10-06T16:58:12.4510000Z`; `528ms: 6ab9a8e69a8420a1e6b56b23.jsonl[5746] _id=6ace5a17de269131f9cf5a01 ts=2026-10-13T16:19:34.1130000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[5749] _id=6ace5a17de269131f9cf5a0a ts=2026-10-13T16:19:34.6410000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6ab9a8e69a8420a1e6b56b23.jsonl[6495] _id=6ace5f73de269131f9cfa859 ts=2026-10-13T16:42:26.2250000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[6498] _id=6ace5f73de269131f9cfa85c ts=2026-10-13T16:42:26.2620000Z`; `51ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13688] _id=6ad10327de269131f9ddd2a5 ts=2026-10-15T16:45:26.8310000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[13691] _id=6ad10327de269131f9ddd2a9 ts=2026-10-15T16:45:26.8820000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `54ms: 6ab9a8e69a8420a1e6b56b23.jsonl[536] _id=6ac3d5e1de269131f9ae2cd9 ts=2026-10-05T16:52:48.6250000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[537] _id=6ac3d5e1de269131f9ae2cdd ts=2026-10-05T16:52:48.6790000Z`; `588ms: 6ab9a8e69a8420a1e6b56b23.jsonl[545] _id=6ac3d5e4de269131f9ae2d2d ts=2026-10-05T16:52:51.8670000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[540] _id=6ac3d5e5de269131f9ae2d35 ts=2026-10-05T16:52:52.4550000Z`; `771ms: 6ab9a8e69a8420a1e6b56b23.jsonl[546] _id=6ac3d5e4de269131f9ae2d33 ts=2026-10-05T16:52:52.0650000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[547] _id=6ac3d5e5de269131f9ae2d3b ts=2026-10-05T16:52:52.8360000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `771ms: 6ab9a8e69a8420a1e6b56b23.jsonl[5288] _id=6ac7ca2ade269131f9c4b0a9 ts=2026-10-08T16:51:53.9700000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[5289] _id=6ac7ca2bde269131f9c4b0af ts=2026-10-08T16:51:54.7410000Z`; `548ms: 6ab9a8e69a8420a1e6b56b23.jsonl[5289] _id=6ac7ca2bde269131f9c4b0af ts=2026-10-08T16:51:54.7410000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[5281] _id=6ac7ca2bde269131f9c4b0b1 ts=2026-10-08T16:51:55.2890000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6ab9a8e69a8420a1e6b56b23.jsonl[15741] _id=6ad25407de269131f9e6099b ts=2026-10-16T16:42:46.3810000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[15742] _id=6ad25407de269131f9e6099e ts=2026-10-16T16:42:46.3900000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `536ms: 6ab9a8e69a8420a1e6b56b23.jsonl[11705] _id=6acfd45ade269131f9d851d4 ts=2026-10-14T19:13:29.2960000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[11551] _id=6acfd45ade269131f9d851ec ts=2026-10-14T19:13:29.8320000Z`; `783ms: 6ab9a8e69a8420a1e6b56b23.jsonl[12706] _id=6ad0fec6de269131f9dd7e4f ts=2026-10-15T16:26:45.9870000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[12725] _id=6ad0fec7de269131f9dd7e5c ts=2026-10-15T16:26:46.7700000Z`; `222ms: 6ab9a8e69a8420a1e6b56b23.jsonl[12723] _id=6ad0fec8de269131f9dd7e6e ts=2026-10-15T16:26:47.7170000Z ~ 6ab9a8e69a8420a1e6b56b23.jsonl[12715] _id=6ad0fec8de269131f9dd7e7b ts=2026-10-15T16:26:47.9390000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b23.jsonl[5459] _id=6ac7cbcbde269131f9c4ca71 ts=2026-10-08T16:58:50.9320000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5718] _id=6ace59fede269131f9cf5984 ts=2026-10-13T16:19:10.0510000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b23.jsonl[2750] _id=6ac6749ade269131f9bc96e2 ts=2026-10-07T16:34:33.6150000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[4501] _id=6ac7c49bde269131f9c4259a ts=2026-10-08T16:28:10.8510000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b23.jsonl[989] _id=6ac524d5de269131f9b52863 ts=2026-10-06T16:41:56.9410000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2747] _id=6ac6748ede269131f9bc95e8 ts=2026-10-07T16:34:21.3700000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a8e69a8420a1e6b56b23.jsonl[5683] _id=6ac7cd12de269131f9c4df6d ts=2026-10-08T17:04:18.3990000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5788] _id=6ace5a2cde269131f9cf5abe ts=2026-10-13T16:19:55.3000000Z; 23h 38m: 6ab9a8e69a8420a1e6b56b23.jsonl[970] _id=6ac3d88bde269131f9ae71b2 ts=2026-10-05T17:04:10.1670000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[1007] _id=6ac524f0de269131f9b52a09 ts=2026-10-06T16:42:24.1550000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b23.jsonl[2737] _id=6ac52a02de269131f9b6067b ts=2026-10-06T17:04:01.5460000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2776] _id=6ac674c2de269131f9bc9d69 ts=2026-10-07T16:35:13.9700000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 634 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13519] _id=6ad10249de269131f9ddbdf2 ts=2026-10-15T16:41:44.9750000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13520] _id=6ad10249de269131f9ddbdf3 ts=2026-10-15T16:41:44.9750000Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13576] _id=6ad1029ede269131f9ddc62f ts=2026-10-15T16:43:09.6820000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13577] _id=6ad1029ede269131f9ddc630 ts=2026-10-15T16:43:09.6820000Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13593] _id=6ad102b8de269131f9ddc8af ts=2026-10-15T16:43:35.5290000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13594] _id=6ad102b8de269131f9ddc8b0 ts=2026-10-15T16:43:35.5290000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 41m 
  - Evidence: 143h 41m: 6ab9a8e69a8420a1e6b56b23.jsonl[5447] _id=6ac7cbadde269131f9c4c84a ts=2026-10-08T16:58:21.1990000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[9136] _id=6acfb052de269131f9d5aadb ts=2026-10-14T16:39:46.5560000Z; 72h 1m: 6ab9a8e69a8420a1e6b56b23.jsonl[724] _id=6ac3d6efde269131f9ae4a61 ts=2026-10-05T16:57:18.9800000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5447] _id=6ac7cbadde269131f9c4c84a ts=2026-10-08T16:58:21.1990000Z; 24h 20m: 6ab9a8e69a8420a1e6b56b23.jsonl[9136] _id=6acfb052de269131f9d5aadb ts=2026-10-14T16:39:46.5560000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14186] _id=6ad10688de269131f9de2d50 ts=2026-10-15T16:59:51.5470000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 14m 
  - Evidence: 119h 14m: 6ab9a8e69a8420a1e6b56b23.jsonl[5712] _id=6ac7cd29de269131f9c4e039 ts=2026-10-08T17:04:41.0300000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5720] _id=6ace5a12de269131f9cf59d9 ts=2026-10-13T16:19:28.1180000Z; 23h 37m: 6ab9a8e69a8420a1e6b56b23.jsonl[973] _id=6ac3d88ade269131f9ae71a9 ts=2026-10-05T17:04:09.7730000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[995] _id=6ac524e2de269131f9b528f5 ts=2026-10-06T16:42:09.6810000Z; 23h 33m: 6ab9a8e69a8420a1e6b56b23.jsonl[4367] _id=6ac67963de269131f9bd550f ts=2026-10-07T16:54:57.7320000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[4509] _id=6ac7c4acde269131f9c42608 ts=2026-10-08T16:28:27.4910000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 517 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[10440] _id=6acfb4d4de269131f9d61e65 ts=2026-10-14T16:59:00.1100000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[10441] _id=6acfb4d4de269131f9d61e66 ts=2026-10-14T16:59:00.1100000Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[10442] _id=6acfb4d4de269131f9d61e6e ts=2026-10-14T16:59:00.2330000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[10443] _id=6acfb4d4de269131f9d61e6f ts=2026-10-14T16:59:00.2330000Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[10983] _id=6acfd2b0de269131f9d80ab7 ts=2026-10-14T19:06:23.5720000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[10984] _id=6acfd2b0de269131f9d80ab8 ts=2026-10-14T19:06:23.5720000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b23.jsonl[5703] _id=6ac7cd1fde269131f9c4dff1 ts=2026-10-08T17:04:30.9130000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5830] _id=6ace5a7fde269131f9cf5d0b ts=2026-10-13T16:21:18.3390000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b23.jsonl[2279] _id=6ac52672de269131f9b55ce3 ts=2026-10-06T16:48:49.4280000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[3428] _id=6ac6771bde269131f9bd11c4 ts=2026-10-07T16:45:14.8040000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b23.jsonl[4215] _id=6ac678abde269131f9bd463b ts=2026-10-07T16:51:55.0240000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2741] _id=6ac7c815de269131f9c4874e ts=2026-10-08T16:43:01.5720000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.012s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13352] _id=6ad1014ade269131f9ddac26 ts=2026-10-15T16:37:29.6930000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13353] _id=6ad1014ade269131f9ddac27 ts=2026-10-15T16:37:29.6930000Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13442] _id=6ad1018dde269131f9ddb0a6 ts=2026-10-15T16:38:36.6000000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13443] _id=6ad1018dde269131f9ddb0a7 ts=2026-10-15T16:38:36.6000000Z; 12ms: 6ab9a8e69a8420a1e6b56b23.jsonl[90] _id=6ac3d225de269131f9adda79 ts=2026-10-05T16:36:52.7250000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[55] _id=6ac3d225de269131f9adda7d ts=2026-10-05T16:36:52.7370000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 14m 
  - Evidence: 119h 14m: 6ab9a8e69a8420a1e6b56b23.jsonl[5714] _id=6ac7cd23de269131f9c4e01d ts=2026-10-08T17:04:35.0670000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5719] _id=6ace5a12de269131f9cf59d8 ts=2026-10-13T16:19:23.7910000Z; 23h 37m: 6ab9a8e69a8420a1e6b56b23.jsonl[960] _id=6ac3d88cde269131f9ae71d3 ts=2026-10-05T17:04:11.4860000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[991] _id=6ac524d8de269131f9b5288b ts=2026-10-06T16:41:56.9540000Z; 23h 30m: 6ab9a8e69a8420a1e6b56b23.jsonl[2745] _id=6ac6748ede269131f9bc95e5 ts=2026-10-06T17:04:14.701Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2751] _id=6ac6749fde269131f9bc9764 ts=2026-10-07T16:34:33.6280000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[14255] _id=6ad1078dde269131f9de45b8 ts=2026-10-15T17:04:12.2710000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14260] _id=6ad24133de269131f9e524f9 ts=2026-10-15T17:04:12.271Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[2739] _id=6ac52a0fde269131f9b6094f ts=2026-10-06T17:04:14.7010000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2745] _id=6ac6748ede269131f9bc95e5 ts=2026-10-06T17:04:14.701Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 120h 19m 
  - Evidence: 120h 19m: 6ab9a8e69a8420a1e6b56b23.jsonl[4567] _id=6ac7c4bede269131f9c42712 ts=2026-10-08T16:28:45.1810000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[6819] _id=6ace60dade269131f9cfc02a ts=2026-10-13T16:48:25.0700000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b23.jsonl[2232] _id=6ac52651de269131f9b55769 ts=2026-10-06T16:48:13.3260000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2917] _id=6ac6758ade269131f9bcc91c ts=2026-10-07T16:38:33.1560000Z; 23h 39m: 6ab9a8e69a8420a1e6b56b23.jsonl[982] _id=6ac3d88dde269131f9ae71f7 ts=2026-10-05T17:04:09.7880000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[1130] _id=6ac5257bde269131f9b536c3 ts=2026-10-06T16:43:32.7940000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1203 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[1042] _id=6ac52545de269131f9b530f5 ts=2026-10-06T16:43:47.2470000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[1065] _id=6ac52545de269131f9b530fb ts=2026-10-06T16:43:47.2470000Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[1043] _id=6ac52545de269131f9b53105 ts=2026-10-06T16:43:47.2470000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[1082] _id=6ac52545de269131f9b53107 ts=2026-10-06T16:43:47.2470000Z; 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[1044] _id=6ac52545de269131f9b5310d ts=2026-10-06T16:43:47.6610000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[1083] _id=6ac52546de269131f9b5311d ts=2026-10-06T16:43:47.6610000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 14m 
  - Evidence: 120h 14m: 6ab9a8e69a8420a1e6b56b23.jsonl[4683] _id=6ac7c58ade269131f9c43766 ts=2026-10-08T16:32:10.5960000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[6766] _id=6ace606ede269131f9cfb903 ts=2026-10-13T16:46:37.3170000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b23.jsonl[6806] _id=6ace60acde269131f9cfbdb1 ts=2026-10-13T16:47:39.7730000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[9308] _id=6acfb220de269131f9d5d4d7 ts=2026-10-14T16:47:27.8790000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b23.jsonl[3479] _id=6ac6778cde269131f9bd25da ts=2026-10-07T16:47:07.4620000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[4682] _id=6ac7c589de269131f9c4374a ts=2026-10-08T16:32:09.7060000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.001s..0.005s shown 
  - Evidence: 1ms: 6ab9a8e69a8420a1e6b56b23.jsonl[6787] _id=6ace6082de269131f9cfbab6 ts=2026-10-13T16:46:58.0310000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[6788] _id=6ace6082de269131f9cfbab7 ts=2026-10-13T16:46:58.0320000Z; 5ms: 6ab9a8e69a8420a1e6b56b23.jsonl[9321] _id=6acfb23ade269131f9d5d792 ts=2026-10-14T16:47:54.4200000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[9320] _id=6acfb23bde269131f9d5d7a4 ts=2026-10-14T16:47:54.4250000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b23.jsonl[5566] _id=6ac7ccb9de269131f9c4db26 ts=2026-10-08T17:02:49.4130000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5734] _id=6ace5a12de269131f9cf59e6 ts=2026-10-13T16:19:28.1260000Z; 24h 9m: 6ab9a8e69a8420a1e6b56b23.jsonl[5873] _id=6ace5a9ede269131f9cf5e7f ts=2026-10-13T16:21:49.6680000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[8812] _id=6acfae62de269131f9d58234 ts=2026-10-14T16:31:29.8100000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b23.jsonl[3067] _id=6ac675d3de269131f9bcda83 ts=2026-10-07T16:39:46.7330000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[4778] _id=6ac7c6abde269131f9c45ed8 ts=2026-10-08T16:36:59.2210000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.029s..0.030s shown 
  - Evidence: 29ms: 6ab9a8e69a8420a1e6b56b23.jsonl[2608] _id=6ac528a5de269131f9b5c380 ts=2026-10-06T16:58:12.3920000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2612] _id=6ac528a5de269131f9b5c38a ts=2026-10-06T16:58:12.4210000Z; 30ms: 6ab9a8e69a8420a1e6b56b23.jsonl[2612] _id=6ac528a5de269131f9b5c38a ts=2026-10-06T16:58:12.4210000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2614] _id=6ac528a5de269131f9b5c3a8 ts=2026-10-06T16:58:12.4510000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 45m 31s 
  - Evidence: 45m 31s: 6ab9a8e69a8420a1e6b56b23.jsonl[14642] _id=6ad24368de269131f9e54401 ts=2026-10-16T15:31:51.6580000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14722] _id=6ad24e14de269131f9e5ab94 ts=2026-10-16T16:17:23.5590000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a8e69a8420a1e6b56b23.jsonl[5361] _id=6ac7cab7de269131f9c4b7ef ts=2026-10-08T16:54:14.7110000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[6494] _id=6ace5f72de269131f9cfa854 ts=2026-10-13T16:42:26.2040000Z; 71h 57m: 6ab9a8e69a8420a1e6b56b23.jsonl[586] _id=6ac3d64ade269131f9ae38ef ts=2026-10-05T16:54:33.3470000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5298] _id=6ac7ca4dde269131f9c4b1f2 ts=2026-10-08T16:52:28.9540000Z; 47h 59m: 6ab9a8e69a8420a1e6b56b23.jsonl[6494] _id=6ace5f72de269131f9cfa854 ts=2026-10-13T16:42:26.2040000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13515] _id=6ad10249de269131f9ddbdec ts=2026-10-15T16:41:44.9400000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a8e69a8420a1e6b56b23.jsonl[5362] _id=6ac7cab7de269131f9c4b7f2 ts=2026-10-08T16:54:14.7310000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[6453] _id=6ace5f3bde269131f9cfa3ce ts=2026-10-13T16:41:31.1660000Z; 71h 56m: 6ab9a8e69a8420a1e6b56b23.jsonl[588] _id=6ac3d64ade269131f9ae38f6 ts=2026-10-05T16:54:33.3750000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5273] _id=6ac7ca08de269131f9c4af38 ts=2026-10-08T16:51:20.6530000Z; 47h 58m: 6ab9a8e69a8420a1e6b56b23.jsonl[6498] _id=6ace5f73de269131f9cfa85c ts=2026-10-13T16:42:26.2620000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13481] _id=6ad10201de269131f9ddb7da ts=2026-10-15T16:40:33.3280000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.037s..0.037s shown 
  - Evidence: 37ms: 6ab9a8e69a8420a1e6b56b23.jsonl[6495] _id=6ace5f73de269131f9cfa859 ts=2026-10-13T16:42:26.2250000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[6498] _id=6ace5f73de269131f9cfa85c ts=2026-10-13T16:42:26.2620000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a8e69a8420a1e6b56b23.jsonl[5360] _id=6ac7cab5de269131f9c4b7bd ts=2026-10-08T16:54:12.6940000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[6450] _id=6ace5f39de269131f9cfa3a2 ts=2026-10-13T16:41:29.0400000Z; 71h 57m: 6ab9a8e69a8420a1e6b56b23.jsonl[581] _id=6ac3d637de269131f9ae35b5 ts=2026-10-05T16:54:14.6100000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5286] _id=6ac7ca31de269131f9c4b0e8 ts=2026-10-08T16:52:00.8710000Z; 47h 58m: 6ab9a8e69a8420a1e6b56b23.jsonl[6493] _id=6ace5f70de269131f9cfa832 ts=2026-10-13T16:42:24.0950000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13484] _id=6ad10208de269131f9ddb858 ts=2026-10-15T16:40:40.1230000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 29 interval(s) ≤ 0.025s..0.027s shown 
  - Evidence: 25ms: 6ab9a8e69a8420a1e6b56b23.jsonl[15505] _id=6ad25215de269131f9e5ee7a ts=2026-10-16T16:34:28.4950000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[15501] _id=6ad25215de269131f9e5ee7e ts=2026-10-16T16:34:28.5200000Z; 26ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13581] _id=6ad102b3de269131f9ddc7d4 ts=2026-10-15T16:43:30.4730000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13586] _id=6ad102b3de269131f9ddc7db ts=2026-10-15T16:43:30.4990000Z; 27ms: 6ab9a8e69a8420a1e6b56b23.jsonl[13589] _id=6ad102b4de269131f9ddc815 ts=2026-10-15T16:43:31.5870000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[13588] _id=6ad102b4de269131f9ddc821 ts=2026-10-15T16:43:31.6140000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 45m 
  - Evidence: 191h 45m: 6ab9a8e69a8420a1e6b56b23.jsonl[5281] _id=6ac7ca2bde269131f9c4b0b1 ts=2026-10-08T16:51:55.2890000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[15614] _id=6ad252c3de269131f9e5f8c7 ts=2026-10-16T16:37:22.0070000Z; 71h 57m: 6ab9a8e69a8420a1e6b56b23.jsonl[566] _id=6ac3d625de269131f9ae333b ts=2026-10-05T16:53:56.4260000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5285] _id=6ac7ca27de269131f9c4b087 ts=2026-10-08T16:51:51.1810000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 22h 21m 
  - Evidence: 22h 21m: 6ab9a8e69a8420a1e6b56b23.jsonl[14203] _id=6ad106c0de269131f9de326d ts=2026-10-15T17:00:48.2080000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14264] _id=6ad2413bde269131f9e5259b ts=2026-10-16T15:22:34.5860000Z; 54m 41s: 6ab9a8e69a8420a1e6b56b23.jsonl[14264] _id=6ad2413bde269131f9e5259b ts=2026-10-16T15:22:34.5860000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14708] _id=6ad24e0dde269131f9e5ab4c ts=2026-10-16T16:17:16.1510000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b23.jsonl[5451] _id=6ac7cbbcde269131f9c4c936 ts=2026-10-08T16:58:36.0480000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5717] _id=6ace59ffde269131f9cf5987 ts=2026-10-13T16:19:10.3970000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b23.jsonl[5717] _id=6ace59ffde269131f9cf5987 ts=2026-10-13T16:19:10.3970000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[8015] _id=6acfab91de269131f9d54ea4 ts=2026-10-14T16:19:28.8040000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b23.jsonl[2749] _id=6ac6748ede269131f9bc95ea ts=2026-10-07T16:34:21.5070000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[4503] _id=6ac7c49bde269131f9c4259d ts=2026-10-08T16:28:11.0160000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b23.jsonl[5450] _id=6ac7cbbcde269131f9c4c935 ts=2026-10-08T16:58:36.0480000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5716] _id=6ace59ffde269131f9cf5986 ts=2026-10-13T16:19:10.3970000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b23.jsonl[2748] _id=6ac6748ede269131f9bc95e9 ts=2026-10-07T16:34:21.5070000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[4502] _id=6ac7c49bde269131f9c4259c ts=2026-10-08T16:28:11.0160000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b23.jsonl[988] _id=6ac524cade269131f9b52807 ts=2026-10-06T16:41:45.9060000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2748] _id=6ac6748ede269131f9bc95e9 ts=2026-10-07T16:34:21.5070000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 167h 19m 
  - Evidence: 167h 19m: 6ab9a8e69a8420a1e6b56b23.jsonl[2746] _id=6ac6748ede269131f9bc95e6 ts=2026-10-06T17:04:15.339Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5893] _id=6ace5af8de269131f9cf61c5 ts=2026-10-13T16:23:19.6450000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b23.jsonl[987] _id=6ac524cade269131f9b52801 ts=2026-10-05T17:04:16.342Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2746] _id=6ac6748ede269131f9bc95e6 ts=2026-10-06T17:04:15.339Z; 23h 59m: 6ab9a8e69a8420a1e6b56b23.jsonl[10988] _id=6acfd233de269131f9d7faa4 ts=2026-10-14T17:04:40.19Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14253] _id=6ad1078ade269131f9de4593 ts=2026-10-15T17:04:09.5430000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b23.jsonl[5485] _id=6ac7cc45de269131f9c4d421 ts=2026-10-08T17:00:52.8880000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[5735] _id=6ace5a12de269131f9cf59e7 ts=2026-10-13T16:19:28.1780000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b23.jsonl[852] _id=6ac3d7b4de269131f9ae5e47 ts=2026-10-05T17:00:35.4480000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[990] _id=6ac524d9de269131f9b5288e ts=2026-10-06T16:41:58.8830000Z; 23h 36m: 6ab9a8e69a8420a1e6b56b23.jsonl[2605] _id=6ac5288fde269131f9b5bf49 ts=2026-10-06T16:57:50.9590000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[2752] _id=6ac6749fde269131f9bc9765 ts=2026-10-07T16:34:36.5650000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b23.jsonl[15574] _id=6ad25272de269131f9e5f3b3 ts=2026-10-16T16:36:01.6150000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[15575] _id=6ad25272de269131f9e5f3b4 ts=2026-10-16T16:36:01.6150000Z; 1ms: 6ab9a8e69a8420a1e6b56b23.jsonl[14825] _id=6ad24e62de269131f9e5b21b ts=2026-10-16T16:18:41.4840000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14826] _id=6ad24e62de269131f9e5b21c ts=2026-10-16T16:18:41.4850000Z; 2ms: 6ab9a8e69a8420a1e6b56b23.jsonl[14651] _id=6ad24339de269131f9e541b2 ts=2026-10-16T15:31:04.4990000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[14652] _id=6ad24339de269131f9e541b3 ts=2026-10-16T15:31:04.5010000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 21h 4m 
  - Evidence: 21h 4m: 6ab9a8e69a8420a1e6b56b23.jsonl[11968] _id=6acfd4f6de269131f9d87003 ts=2026-10-14T19:16:05.3260000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[12154] _id=6ad0fd49de269131f9dd5d76 ts=2026-10-15T16:20:24.4520000Z; 2h 2m: 6ab9a8e69a8420a1e6b56b23.jsonl[10938] _id=6acfb617de269131f9d6437b ts=2026-10-14T17:04:22.7150000Z -> 6ab9a8e69a8420a1e6b56b23.jsonl[11106] _id=6acfd2d2de269131f9d8108b ts=2026-10-14T19:06:57.6930000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[458] _id=6ac3d55cde269131f9ae217e ts=2026-10-05T16:50:35.8230000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[595] _id=6ac3d65dde269131f9ae3bc5 ts=2026-10-05T16:54:52.5620000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[4253] _id=6ac67945de269131f9bd51d2 ts=2026-10-07T16:54:28.9910000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 22 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[1233] _id=6ac5258fde269131f9b5393e ts=2026-10-06T16:45:01.2650000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[1183] _id=6ac5258fde269131f9b53945 ts=2026-10-06T16:45:01.2980000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[1238] _id=6ac5258fde269131f9b5394b ts=2026-10-06T16:45:01.3030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 109 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[939] _id=6ac3d836de269131f9ae6aed ts=2026-10-05T17:02:45.0580000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[841] _id=6ac3d836de269131f9ae6af7 ts=2026-10-05T17:02:45.0580000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[803] _id=6ac3d836de269131f9ae6afd ts=2026-10-05T17:02:45.0580000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[6498] _id=6ace5f73de269131f9cfa85c ts=2026-10-13T16:42:26.2620000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[13691] _id=6ad10327de269131f9ddd2a9 ts=2026-10-15T16:45:26.8820000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[15610] _id=6ad252b1de269131f9e5f7ec ts=2026-10-16T16:37:04.2100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[537] _id=6ac3d5e1de269131f9ae2cdd ts=2026-10-05T16:52:48.6790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[14203] _id=6ad106c0de269131f9de326d ts=2026-10-15T17:00:48.2080000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[14264] _id=6ad2413bde269131f9e5259b ts=2026-10-16T15:22:34.5860000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[14708] _id=6ad24e0dde269131f9e5ab4c ts=2026-10-16T16:17:16.1510000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[11000] _id=6acfd274de269131f9d80237 ts=2026-10-14T19:05:23.6930000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[12039] _id=6ad0fce9de269131f9dd57c9 ts=2026-10-15T16:18:48.5100000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 122 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[1176] _id=6ac52585de269131f9b53825 ts=2026-10-06T16:44:51.4130000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[1276] _id=6ac52597de269131f9b53a75 ts=2026-10-06T16:45:10.4460000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[1248] _id=6ac52598de269131f9b53a84 ts=2026-10-06T16:45:10.6550000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 339 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[777] _id=6ac3d834de269131f9ae6ab5 ts=2026-10-05T17:02:42.5890000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[778] _id=6ac3d835de269131f9ae6ab9 ts=2026-10-05T17:02:42.5890000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[838] _id=6ac3d835de269131f9ae6ac3 ts=2026-10-05T17:02:42.5890000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 15 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[2612] _id=6ac528a5de269131f9b5c38a ts=2026-10-06T16:58:12.4210000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[2614] _id=6ac528a5de269131f9b5c3a8 ts=2026-10-06T16:58:12.4510000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[2693] _id=6ac529a0de269131f9b5f578 ts=2026-10-06T17:02:23.5350000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[5288] _id=6ac7ca2ade269131f9c4b0a9 ts=2026-10-08T16:51:53.9700000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[5289] _id=6ac7ca2bde269131f9c4b0af ts=2026-10-08T16:51:54.7410000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[5281] _id=6ac7ca2bde269131f9c4b0b1 ts=2026-10-08T16:51:55.2890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 427 start, 420 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 32 unmatched 'BecameCameraCentered' (totals: 540 open, 530 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 58 unmatched 'BecameVisible' (totals: 694 open, 745 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 19 open, 17 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 8 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 51 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 529 of 15850 adjacent _id pairs reverse in client time; worst 98.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b23.jsonl[970] _id=6ac3d88bde269131f9ae71b2 ts=2026-10-05T17:04:10.1670000Z`; `6ab9a8e69a8420a1e6b56b23.jsonl[975] _id=6ac3d88cde269131f9ae71c3 ts=2026-10-05T17:02:31.6290000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.85s, min -85050.30s, max -0.26s over 15851 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b23\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

No coverage-related findings.

## 9. Event-Type Details

### `InputEvent` — 8188 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (2297); Unit 2 Prod (Refactor) (1853); Unit 3 Dungeon Dev (1109); Unit 3 Dev (1079); Unit 4 Dev (680); Unit 5 Dev - Dungeon (511); Unit 1 Dev (296); Unit 5 Dev (222); Unit 4 Dev - Anderson Base (141)
- **Intervals:** median 0.37s (p5 0.03s / p95 2.79s, n=8187)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 8188/8188 records)
    "pressed"  x8188
data.actionType  (string, 8188/8188 records)
    "Move"  x6872
    "Interact"  x572
    "Sprint"  x289
    "Jump"  x270
    "Hoverboard"  x111
    "Ascend"  x43
    "Map"  x20
    "Descend"  x7
    "Pause"  x3
    "ToggleDebug"  x1
data.key  (string, 8188/8188 records, 4 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 8188/8188 records)
    "Player"  x7586
    "Drone"  x602
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2509 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1525); Unit 4 Dev (422); Unit 3 Dungeon Dev (368); Unit 5 Dev - Dungeon (194)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.83s, n=2508)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2509/2509 records)
    "BecameInvisible"  x745
    "BecameVisible"  x694
    "BecameCameraCentered"  x540
    "BecameCameraUncentered"  x530
data.pieceId  (string, 2509/2509 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2509/2509 records)
    1465 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2221 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (628); Unit 3 Dev (320); Unit 4 Dev (269); Unit 5 Dev (218); Unit 3 Dungeon Dev (210); Unit 1 Dev (197); Unit 4 Dev - Dungeon (196); Unit 4 Dev - Anderson Base (99); Unit 5 Dev - Dungeon (84)
- **eventKey:** present on 1374 of 2221 records
- **Intervals:** median 3.69s (p5 0.00s / p95 30.42s, n=2220)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1374; [conversationId, dialogueEventType] x847
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2221/2221 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2221/2221 records)
    "DialogueNodeEvent"  x1374
    "DialogueStartEvent"  x427
    "DialogueFinishEvent"  x420
data.nodeId  (number, 1374/2221 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1770 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (518); Unit 3 Dev (237); Unit 4 Dev - Dungeon (220); Unit 4 Dev (173); Unit 3 Dungeon Dev (160); Unit 1 Dev (152); Unit 5 Dev (132); Unit 5 Dev - Dungeon (113); Unit 4 Dev - Anderson Base (65)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.23s, n=1756)
- **Fields under `data`:**

```text
data.position  (object, 1770/1770 records)
data.position.x  (number, 1770/1770 records)
    numeric range -696.478 .. 1556.53 (642 unique)
data.position.y  (number, 1770/1770 records)
    numeric range -112.489 .. 221.563 (457 unique)
data.position.z  (number, 1770/1770 records)
    numeric range -1038.59 .. 2244.74 (643 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 380 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (184); Unit 3 Dungeon Dev (74); Unit 2 Prod (Refactor) (46); Unit 4 Dev (20); Unit 3 Dev (15); Unit 5 Dev - Dungeon (15); Unit 1 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (6)
- **Intervals:** median 7.68s (p5 1.10s / p95 340.19s, n=379)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 380/380 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 380/380 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 309 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (131); Unit 5 Dev (58); Unit 2 Prod (Refactor) (53); Unit 1 Dev (36); Unit 3 Dev (31)
- **Intervals:** median 0.80s (p5 0.03s / p95 11.37s, n=308)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 309/309 records)
    "argumentationNodeHoverEnd"  x131
    "argumentationNodeHoverStart"  x130
    "argumentationNodeAdd"  x34
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 309/309 records)
    "Unit 4 - Flooding"  x131
    "Unit 5"  x58
    "Unit 2 – Watershed"  x53
    "Unit 3 - Pollution Upstream"  x31
    "Unit 1 - Argumentation Tutorial"  x23
    "Unit 1 - Freshwater"  x13
data.nodeName  (string, 309/309 records)
    "A"  x41
    "1"  x37
    "C"  x32
    "D"  x32
    "I"  x31
    "3"  x29
    "4"  x26
    "B"  x26
    "2"  x25
    "II"  x25
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 90 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (21); Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 3 Dev (10); Unit 5 Dev - Dungeon (10); Unit 4 Dev (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 90 of 90 records
- **Intervals:** median 165.33s (p5 0.01s / p95 82957.08s, n=89)
- **`data` key-set variants:** [questEventType, questID, questName] x51; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 90/90 records)
    "questActiveEvent"  x51
    "questFinishEvent"  x39
data.questID  (string, 90/90 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 90/90 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/90 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 81 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (36); Unit 3 Dev (24); Unit 4 Dev (21)
- **Intervals:** median 1.58s (p5 0.16s / p95 28.72s, n=80)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x75; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/81 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/81 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 75/81 records)
    "RightDrag"  x40
    "LeftDrag"  x35
data.currentSoilType  (string, 75/81 records)
    "CLAY"  x17
    "CLAYSAND"  x15
    "CLAYROCK"  x14
    "SAND"  x13
    "SANDGRAVEL"  x8
    "BEDROCK"  x5
    "GRAVEL"  x3
data.isCorrectSelection  (string, 75/81 records)
    "false"  x56
    "true"  x19
data.waterLevelStatus  (string, 75/81 records)
    "TooHigh"  x34
    "Proper"  x27
    "TooLow"  x14
data.waterRetentionChange  (string, 75/81 records)
    "Increase"  x35
    "Decrease"  x21
    "NoChange"  x19
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `soilMachine` — 54 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (54)
- **Intervals:** median 5.26s (p5 0.88s / p95 157.08s, n=53)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "ChangeCanister"  x54
data.canisterType  (string, 54/54 records)
    "Clay"  x27
    "Bedrock"  x16
    "Gravel"  x7
    "Sand"  x4
data.floor  (string, 54/54 records)
    "5"  x43
    "4"  x6
    "3"  x5
data.machine  (string, 54/54 records)
    "1"  x52
    "2"  x2
data.row  (string, 54/54 records)
    "TopRow"  x30
    "BottomRow"  x24
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 51 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (23)
- **Intervals:** median 7.57s (p5 0.26s / p95 85781.11s, n=50)
- **`data` key-set variants:** [actionType, featureUsed] x36; [actionType, featureUsed, location] x15
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 51/51 records)
    "MapOpenEvent"  x19
    "MapCloseEvent"  x17
    "WaypointMoveEvent"  x10
    "WaypointSetEvent"  x5
data.featureUsed  (string, 51/51 records)
    "Map"  x36
    "Waypoint"  x15
data.location  (object, 15/51 records)
data.location.x  (number, 15/51 records)
    numeric range -329.253 .. 138.914 (14 unique)
data.location.y  (number, 15/51 records)
    numeric range -166.327 .. 270.91 (14 unique)
data.location.z  (number, 15/51 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 32 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (4); Unit 4 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Dungeon (3); Unit 5 Dev - Dungeon (3); Unit 3 Dungeon Dev (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 645.48s (p5 8.60s / p95 85980.83s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "DebugMenuStateChanged"  x32
data.isOpened  (bool, 32/32 records)
    false  x32
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 31 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (31)
- **Intervals:** median 6.48s (p5 1.24s / p95 76.71s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "On"  x22
    "Off"  x9
data.floor  (string, 31/31 records)
    "3"  x14
    "4"  x11
    "2"  x4
    "1"  x2
data.machineNumber  (string, 31/31 records)
    "One"  x28
    "Two"  x3
data.machineType  (string, 31/31 records)
    "Condenser"  x16
    "Evaporator"  x8
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 31/31 records)
    "2"  x10
    "3"  x10
    "4"  x6
    "1"  x5
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 27 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 5 Dev - Dungeon (9); Unit 3 Dev (2); Unit 1 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 789.64s (p5 30.67s / p95 86011.03s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    true  x27
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 26 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (12); Unit 4 Dev - Anderson Base (7); Unit 2 Prod (Refactor) (4); Unit 1 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 25.85s (p5 1.62s / p95 241812.23s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "submitAnswerEvent"  x26
data.answerSubmitted  (string, 26/26 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 26/26 records)
    "Unit 5"  x12
    "Unit 4 - Flooding"  x7
    "Unit 2 – Watershed"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 5 Dev - Dungeon (11); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 791.10s (p5 3.19s / p95 163790.79s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 111.77s (p5 0.05s / p95 319287.48s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 15/15 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 76437.81s (p5 1465.59s / p95 223704.78s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 1 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 2.82s (p5 0.63s / p95 539388.53s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x8
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 9/9 records)
    "Unit 2 – Watershed"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `SolarStillDesignEvent` — 7 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (7)
- **Intervals:** median 2.00s (p5 1.46s / p95 4.07s, n=6)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x6; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "optionSelected"  x6
    "DesignSubmitted"  x1
data.designSelections  (object, 1/7 records)
data.designSelections.glassRoofTemperature  (string, 1/7 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/7 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/7 records)
    "Tilted Out"  x1
data.featureUsed  (string, 7/7 records)
    "RoofStyle"  x3
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 6/7 records)
    "Tilted Out"  x2
    "Cold"  x1
    "Covered"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 3.46s (p5 1.40s / p95 27.79s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x3
data.boxId  (string, 7/7 records)
    "1"  x3
    "0"  x2
    "2"  x2
data.soilType  (string, 7/7 records)
    "Clay"  x4
    "Gravel"  x2
    "Sand"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 173433.60s (p5 85958.41s / p95 478581.89s, n=4)
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

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (3); Unit 5 Dev (1)
- **Intervals:** median 3281.57s (p5 747.79s / p95 72783.90s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 5 Dev (2)
- **Intervals:** median 1.96s (p5 1.96s / p95 1.96s, n=1)
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
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (36 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (10x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (15x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (16x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*