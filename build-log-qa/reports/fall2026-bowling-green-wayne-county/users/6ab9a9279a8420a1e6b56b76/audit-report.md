# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b76

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b76
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b76.jsonl
- **Records:** 13042 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b76
- **Time span:** 2026-10-05T18:46:17.507000+00:00 .. 2026-10-16T01:34:37.212000+00:00 (246h 48m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b76\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 13042 records, 11 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 97 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3549 | 27.21 | 1 | 9 | 0 | 2026-10-05T19:12:49.785000+00:00 | 2026-10-16T01:34:37.212000+00:00 | 246h 21m |
| PuzzlePieceVisibleEvent | 3246 | 24.89 | 1 | 4 | 0 | 2026-10-07T18:50:28.862000+00:00 | 2026-10-16T00:49:43.955000+00:00 | 197h 59m |
| DialogueEvent | 2395 | 18.36 | 1 | 9 | 1496 | 2026-10-05T19:13:06.266000+00:00 | 2026-10-16T01:34:31.408000+00:00 | 246h 21m |
| PlayerPositionEvent | 2368 | 18.16 | 1 | 9 | 0 | 2026-10-05T19:12:46.368000+00:00 | 2026-10-16T01:34:28.880000+00:00 | 246h 21m |
| ObjectInterEvent | 480 | 3.68 | 1 | 9 | 0 | 2026-10-06T18:37:05.537000+00:00 | 2026-10-16T01:34:37.212000+00:00 | 222h 57m |
| argumentationNodeEvent | 375 | 2.88 | 1 | 5 | 0 | 2026-10-06T19:07:34.846000+00:00 | 2026-10-16T01:22:45.723000+00:00 | 222h 15m |
| Soil Key Puzzle | 147 | 1.13 | 1 | 3 | 0 | 2026-10-07T19:01:25.692000+00:00 | 2026-10-15T16:00:16.691000+00:00 | 188h 58m |
| questEvent | 92 | 0.71 | 1 | 9 | 92 | 2026-10-05T19:13:06.238000+00:00 | 2026-10-16T01:29:47.331000+00:00 | 246h 16m |
| WaterChamberEvent | 91 | 0.7 | 1 | 1 | 0 | 2026-10-16T00:48:51.705000+00:00 | 2026-10-16T01:12:27.879000+00:00 | 23m 36s |
| TopographicMapEvent | 62 | 0.48 | 1 | 3 | 0 | 2026-10-06T18:58:45.351000+00:00 | 2026-10-14T19:25:25.129000+00:00 | 192h 26m |
| argumentationAnswerEvent | 54 | 0.41 | 1 | 5 | 0 | 2026-10-06T19:08:25.176000+00:00 | 2026-10-16T01:22:52.642000+00:00 | 222h 14m |
| DEBUGMenu | 39 | 0.3 | 1 | 9 | 0 | 2026-10-05T19:12:46.354000+00:00 | 2026-10-16T00:44:39.755000+00:00 | 245h 31m |
| soilMachine | 30 | 0.23 | 1 | 1 | 0 | 2026-10-15T18:54:03.721000+00:00 | 2026-10-15T19:06:29.422000+00:00 | 12m 25s |
| gameWindowFocusEvent | 25 | 0.19 | 1 | 3 | 0 | 2026-10-05T18:46:17.507000+00:00 | 2026-10-16T00:44:32.338000+00:00 | 245h 58m |
| gameStartEvent | 19 | 0.15 | 1 | 1 | 0 | 2026-10-05T18:46:17.509000+00:00 | 2026-10-16T00:44:32.338000+00:00 | 245h 58m |
| argumentationEvent | 14 | 0.11 | 1 | 5 | 0 | 2026-10-06T19:07:56.857000+00:00 | 2026-10-16T01:22:52.676000+00:00 | 222h 14m |
| gameWindowUnfocusEvent | 13 | 0.1 | 1 | 4 | 0 | 2026-10-05T18:47:16.923000+00:00 | 2026-10-14T19:24:39.461000+00:00 | 216h 37m |
| SolarStillDesignEvent | 11 | 0.08 | 1 | 1 | 0 | 2026-10-16T01:25:59.369000+00:00 | 2026-10-16T01:26:39.886000+00:00 | 40.5s |
| TerasGardenBox | 11 | 0.08 | 1 | 1 | 0 | 2026-10-16T00:26:52.464000+00:00 | 2026-10-16T00:35:46.458000+00:00 | 8m 53s |
| argumentationToolEvent | 8 | 0.06 | 1 | 2 | 0 | 2026-10-06T19:09:22.155000+00:00 | 2026-10-13T19:06:26.669000+00:00 | 167h 57m |
| DaniEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-10-14T16:46:56.710000+00:00 | 2026-10-14T19:08:47.874000+00:00 | 2h 21m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T19:13:08.283000+00:00 | 2026-10-16T01:34:37.194000+00:00 | 222h 21m |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-10-16T00:44:39.622000+00:00 | 2026-10-16T01:13:17.827000+00:00 | 28m 38s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 96275.665s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.542s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.064s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 9.554s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.978s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.995s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 7.028s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.102s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 7954.814s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2161.774s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 5816.479s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.554s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** `DEBUGMenu` — record volume changed 3.2x vs baseline. 
  - Observed: 39 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.9x vs baseline. 
  - Observed: 147 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Commons; Jasper's Room; PodBay; Teleporter Room; Toppo's Room 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 4.5x vs baseline. 
  - Observed: 91 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.8x vs baseline. 
  - Observed: 54 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,I; A,3,I; A,4,I; B,1,I; C,1,I; C,1,II; C,4,II; D,1,I; D,1,II; D,2,II; D,3,II; D,4,II 
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
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 6.0x vs baseline. 
  - Observed: 30 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[548] _id=6ac542bade269131f9b6f4b1 ts=2026-10-06T18:49:29.6230000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[63] _id=6ac543d1de269131f9b70c75 ts=2026-10-06T18:54:08.2770000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[623] _id=6ac5447ade269131f9b71795 ts=2026-10-06T18:56:57.2410000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[1] _id=6ac3f079de269131f9af5e61 ts=2026-10-05T18:46:17.5090000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[15] _id=6ac3f690de269131f9af6af1 ts=2026-10-05T19:12:16.3620000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[70] _id=6ac53e88de269131f9b6768b ts=2026-10-06T18:31:35.4650000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[2] _id=6ac3f079de269131f9af5e5b ts=2026-10-05T18:46:17.5070000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[4] _id=6ac3f614de269131f9af6a29 ts=2026-10-05T19:10:12.6700000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[7] _id=6ac3f621de269131f9af6a35 ts=2026-10-05T19:10:24.8340000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[3] _id=6ac3f0b5de269131f9af6067 ts=2026-10-05T18:47:16.9230000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[5] _id=6ac3f619de269131f9af6a2d ts=2026-10-05T19:10:17.6890000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[8] _id=6ac3f625de269131f9af6a37 ts=2026-10-05T19:10:29.0580000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 6 of 62 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[651] _id=6ac544e8de269131f9b71eed ts=2026-10-06T18:58:45.3510000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[653] _id=6ac544fbde269131f9b71ff3 ts=2026-10-06T18:59:06.4680000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[656] _id=6ac54501de269131f9b7203f ts=2026-10-06T18:59:12.4460000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3548 | 0.0 | 1.542 | 249.974 | 25.332 | 411795.824 | 0.24 | 41 | 13 |
| PuzzlePieceVisibleEvent | 3245 | 0.0 | 0.064 | 219.647 | 2.037 | 411989.377 | 0.27 | 1466 | 8 |
| DialogueEvent | 2394 | 0.0 | 4.386 | 370.462 | 30.534 | 411593.048 | 0.16 | 695 | 14 |
| PlayerPositionEvent | 2356 | 9.803 | 10.001 | 345.29 | 10.108 | 411502.367 | 0.17 | 0 | 11 |
| ObjectInterEvent | 479 | 0.0 | 7.59 | 1675.682 | 259.21 | 413372.733 | 0.04 | 3 | 13 |
| argumentationNodeEvent | 374 | 0.005 | 0.438 | 2139.334 | 13.539 | 604524.7 | 0.03 | 42 | 4 |
| Soil Key Puzzle | 146 | 0.107 | 0.457 | 4659.801 | 7.999 | 511238.043 | 0.01 | 0 | 4 |
| questEvent | 91 | 0.001 | 205.354 | 9742.869 | 73983.854 | 411762.795 | 0.01 | 16 | 20 |
| WaterChamberEvent | 90 | 0.101 | 4.995 | 15.735 | 76.813 | 119.997 | 3.81 | 0 | 0 |
| TopographicMapEvent | 61 | 0.021 | 5.978 | 11357.373 | 84763.691 | 413822.546 | 0.01 | 2 | 7 |
| argumentationAnswerEvent | 53 | 0.154 | 7.028 | 15095.613 | 44206.007 | 604533.542 | 0.0 | 0 | 4 |
| DEBUGMenu | 38 | 7.01 | 566.407 | 23260.879 | 84987.234 | 413259.63 | 0.0 | 0 | 19 |
| soilMachine | 29 | 0.245 | 2.554 | 25.714 | 147.138 | 345.326 | 2.33 | 0 | 0 |
| gameWindowFocusEvent | 24 | 12.164 | 2161.774 | 36895.618 | 86225.461 | 413270.2 | 0.0 | 0 | 20 |
| gameStartEvent | 18 | 519.315 | 7954.814 | 49194.157 | 135504.692 | 413270.2 | 0.0 | 0 | 17 |
| argumentationEvent | 13 | 0.068 | 131.401 | 61545.832 | 298859.555 | 604520.857 | 0.0 | 0 | 4 |
| gameWindowUnfocusEvent | 12 | 0.0 | 5816.479 | 64986.878 | 280824.155 | 412836.488 | 0.0 | 1 | 9 |
| SolarStillDesignEvent | 10 | 0.0 | 2.357 | 4.052 | 10.535 | 11.717 | 14.81 | 2 | 0 |
| TerasGardenBox | 10 | 1.365 | 9.554 | 53.399 | 244.941 | 418.815 | 1.12 | 0 | 0 |
| argumentationToolEvent | 7 | 0.064 | 4.102 | 86374.931 | 423222.55 | 604598.202 | 0.0 | 0 | 1 |
| DaniEvent | 5 | 0.846 | 9.361 | 1702.233 | 6778.312 | 8464.894 | 0.04 | 0 | 1 |
| EndOfUnit | 4 | 3038.51 | 96275.665 | 200122.228 | 529890.517 | 604899.071 | 0.0 | 0 | 4 |
| chatEvent | 1 | 1718.205 | 1718.205 | 1718.205 | 1718.205 | 1718.205 | 0.03 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[4056] _id=6ace33dbde269131f9ceb933 ts=2026-10-13T13:36:23.7940000Z == 6ab9a9279a8420a1e6b56b76.jsonl[4057] _id=6ace33dbde269131f9ceb934 ts=2026-10-13T13:36:23.7940000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[10590] _id=6ad12479de269131f9dff11e ts=2026-10-15T19:07:35.8970000Z == 6ab9a9279a8420a1e6b56b76.jsonl[10591] _id=6ad12479de269131f9dff11f ts=2026-10-15T19:07:35.8970000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 48 group(s), 75 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[1184] _id=6ac694bade269131f9be3d0e ts=2026-10-07T18:51:38.1780000Z == 6ab9a9279a8420a1e6b56b76.jsonl[1185] _id=6ac694bade269131f9be3d0f ts=2026-10-07T18:51:38.1780000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[1186] _id=6ac694bdde269131f9be3dbc ts=2026-10-07T18:51:39.4940000Z == 6ab9a9279a8420a1e6b56b76.jsonl[1200] _id=6ac694bede269131f9be3dd5 ts=2026-10-07T18:51:39.4940000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[3187] _id=6ac7e8ffde269131f9c6057c ts=2026-10-08T19:03:25.1760000Z == 6ab9a9279a8420a1e6b56b76.jsonl[3180] _id=6ac7e8ffde269131f9c6058c ts=2026-10-08T19:03:25.1760000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 77 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `309ms: 6ab9a9279a8420a1e6b56b76.jsonl[173] _id=6ac53fd3de269131f9b699a0 ts=2026-10-06T18:37:06.8500000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[168] _id=6ac53fd4de269131f9b699ad ts=2026-10-06T18:37:07.1590000Z`; `232ms: 6ab9a9279a8420a1e6b56b76.jsonl[168] _id=6ac53fd4de269131f9b699ad ts=2026-10-06T18:37:07.1590000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[169] _id=6ac53fd4de269131f9b699b5 ts=2026-10-06T18:37:07.3910000Z`; `254ms: 6ab9a9279a8420a1e6b56b76.jsonl[169] _id=6ac53fd4de269131f9b699b5 ts=2026-10-06T18:37:07.3910000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[170] _id=6ac53fd5de269131f9b699c9 ts=2026-10-06T18:37:07.6450000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `857ms: 6ab9a9279a8420a1e6b56b76.jsonl[12296] _id=6ad178bcde269131f9e26402 ts=2026-10-16T01:07:08.0210000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[12287] _id=6ad178bdde269131f9e26412 ts=2026-10-16T01:07:08.8780000Z`; `637ms: 6ab9a9279a8420a1e6b56b76.jsonl[12287] _id=6ad178bdde269131f9e26412 ts=2026-10-16T01:07:08.8780000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[12301] _id=6ad178bede269131f9e2641a ts=2026-10-16T01:07:09.5150000Z`; `537ms: 6ab9a9279a8420a1e6b56b76.jsonl[12280] _id=6ad178bdde269131f9e26416 ts=2026-10-16T01:07:09.3040000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[12289] _id=6ad178bede269131f9e2641d ts=2026-10-16T01:07:09.8410000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `324ms: 6ab9a9279a8420a1e6b56b76.jsonl[922] _id=6ac54785de269131f9b7676f ts=2026-10-06T19:09:56.2320000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[923] _id=6ac54785de269131f9b76775 ts=2026-10-06T19:09:56.5560000Z`; `419ms: 6ab9a9279a8420a1e6b56b76.jsonl[5135] _id=6ace811ade269131f9d15601 ts=2026-10-13T19:06:01.9000000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[5136] _id=6ace811bde269131f9d15609 ts=2026-10-13T19:06:02.3190000Z`; `454ms: 6ab9a9279a8420a1e6b56b76.jsonl[5149] _id=6ace812cde269131f9d15861 ts=2026-10-13T19:06:19.3160000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[5150] _id=6ace812cde269131f9d1586f ts=2026-10-13T19:06:19.7700000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `68ms: 6ab9a9279a8420a1e6b56b76.jsonl[6354] _id=6acfb4adde269131f9d61a02 ts=2026-10-14T16:58:21.6390000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[6357] _id=6acfb4aede269131f9d61a07 ts=2026-10-14T16:58:21.7070000Z`; `122ms: 6ab9a9279a8420a1e6b56b76.jsonl[11058] _id=6ad12828de269131f9e05110 ts=2026-10-15T19:23:19.5410000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[11050] _id=6ad12828de269131f9e05114 ts=2026-10-15T19:23:19.6630000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 31 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `328ms: 6ab9a9279a8420a1e6b56b76.jsonl[842] _id=6ac546fade269131f9b75b50 ts=2026-10-06T19:07:37.8780000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[840] _id=6ac546fbde269131f9b75b61 ts=2026-10-06T19:07:38.2060000Z`; `718ms: 6ab9a9279a8420a1e6b56b76.jsonl[839] _id=6ac546fade269131f9b75b53 ts=2026-10-06T19:07:37.9450000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[841] _id=6ac546fbde269131f9b75b75 ts=2026-10-06T19:07:38.6630000Z`; `414ms: 6ab9a9279a8420a1e6b56b76.jsonl[864] _id=6ac5471ade269131f9b76033 ts=2026-10-06T19:08:09.7090000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[869] _id=6ac5471bde269131f9b76045 ts=2026-10-06T19:08:10.1230000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a9279a8420a1e6b56b76.jsonl[6531] _id=6acfb5dcde269131f9d63f2e ts=2026-10-14T17:03:24.2660000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[6536] _id=6acfca15de269131f9d7116e ts=2026-10-14T17:03:24.266Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6ab9a9279a8420a1e6b56b76.jsonl[12813] _id=6ad17cb6de269131f9e2796b ts=2026-10-16T01:24:05.4290000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[12814] _id=6ad17cb6de269131f9e2796c ts=2026-10-16T01:24:05.4300000Z`; `6ms: 6ab9a9279a8420a1e6b56b76.jsonl[12942] _id=6ad17dbcde269131f9e27f49 ts=2026-10-16T01:28:28.2800000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[12943] _id=6ad17dbcde269131f9e27f4b ts=2026-10-16T01:28:28.2860000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `913ms: 6ab9a9279a8420a1e6b56b76.jsonl[10113] _id=6ad1214fde269131f9df7863 ts=2026-10-15T18:54:06.9300000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[10076] _id=6ad12150de269131f9df789d ts=2026-10-15T18:54:07.8430000Z`; `653ms: 6ab9a9279a8420a1e6b56b76.jsonl[10122] _id=6ad1215ade269131f9df7a49 ts=2026-10-15T18:54:17.3670000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[10127] _id=6ad1215bde269131f9df7a66 ts=2026-10-15T18:54:18.0200000Z`; `936ms: 6ab9a9279a8420a1e6b56b76.jsonl[10408] _id=6ad12385de269131f9dfc76f ts=2026-10-15T19:03:32.0970000Z ~ 6ab9a9279a8420a1e6b56b76.jsonl[10413] _id=6ad12386de269131f9dfc785 ts=2026-10-15T19:03:33.0330000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 114h 47m 
  - Evidence: 114h 47m: 6ab9a9279a8420a1e6b56b76.jsonl[2929] _id=6ac7e580de269131f9c58914 ts=2026-10-08T18:48:31.6010000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4039] _id=6ace33ccde269131f9ceb84e ts=2026-10-13T13:36:11.2310000Z; 24h 1m: 6ab9a9279a8420a1e6b56b76.jsonl[1092] _id=6ac693aede269131f9be0cf2 ts=2026-10-07T18:47:10.7320000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2928] _id=6ac7e575de269131f9c58899 ts=2026-10-08T18:48:21.0210000Z; 23h 32m: 6ab9a9279a8420a1e6b56b76.jsonl[1026] _id=6ac548a9de269131f9b78346 ts=2026-10-06T19:14:48.2670000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1088] _id=6ac6939ede269131f9be0a89 ts=2026-10-07T18:46:53.7860000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 2h 21m 
  - Evidence: 2h 21m: 6ab9a9279a8420a1e6b56b76.jsonl[5907] _id=6acfb20ade269131f9d5d215 ts=2026-10-14T16:47:06.0710000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[7873] _id=6acfd31bde269131f9d81d97 ts=2026-10-14T19:08:10.9650000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 114h 19m 
  - Evidence: 114h 19m: 6ab9a9279a8420a1e6b56b76.jsonl[4030] _id=6ac7ec67de269131f9c6887e ts=2026-10-08T19:17:59.0230000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4216] _id=6ace3431de269131f9cebe69 ts=2026-10-13T13:37:52.0710000Z; 23h 31m: 6ab9a9279a8420a1e6b56b76.jsonl[2922] _id=6ac69ac8de269131f9bf20be ts=2026-10-07T19:17:28.1030000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2942] _id=6ac7e5a2de269131f9c58b51 ts=2026-10-08T18:49:05.9250000Z; 23h 30m: 6ab9a9279a8420a1e6b56b76.jsonl[1080] _id=6ac54939de269131f9b7995b ts=2026-10-06T19:17:12.7010000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1110] _id=6ac693e6de269131f9be160d ts=2026-10-07T18:48:06.1010000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 695 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[12650] _id=6ad17bddde269131f9e274cf ts=2026-10-16T01:20:28.9090000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12651] _id=6ad17bddde269131f9e274d0 ts=2026-10-16T01:20:28.9090000Z; 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[12689] _id=6ad17bfade269131f9e275f3 ts=2026-10-16T01:20:57.8730000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12690] _id=6ad17bfade269131f9e275f4 ts=2026-10-16T01:20:57.8730000Z; 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[12702] _id=6ad17c0ede269131f9e2764f ts=2026-10-16T01:21:17.9290000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12703] _id=6ad17c0ede269131f9e27650 ts=2026-10-16T01:21:17.9290000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 1m 
  - Evidence: 168h 1m: 6ab9a9279a8420a1e6b56b76.jsonl[1025] _id=6ac54845de269131f9b776d7 ts=2026-10-06T19:13:08.2830000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[5417] _id=6ace8328de269131f9d1aa59 ts=2026-10-13T19:14:47.3540000Z; 29h 7m: 6ab9a9279a8420a1e6b56b76.jsonl[8461] _id=6acfd9c5de269131f9d8e668 ts=2026-10-14T19:36:36.6420000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[11574] _id=6ad1734fde269131f9e2475a ts=2026-10-16T00:43:58.6840000Z; 24h 21m: 6ab9a9279a8420a1e6b56b76.jsonl[5417] _id=6ace8328de269131f9d1aa59 ts=2026-10-13T19:14:47.3540000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[8461] _id=6acfd9c5de269131f9d8e668 ts=2026-10-14T19:36:36.6420000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 114h 23m 
  - Evidence: 114h 23m: 6ab9a9279a8420a1e6b56b76.jsonl[3952] _id=6ac7eb44de269131f9c667c4 ts=2026-10-08T19:13:07.9670000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4055] _id=6ace33dbde269131f9ceb932 ts=2026-10-13T13:36:23.7910000Z; 23h 33m: 6ab9a9279a8420a1e6b56b76.jsonl[2898] _id=6ac69a2cde269131f9bf1393 ts=2026-10-07T19:14:52.6330000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2934] _id=6ac7e584de269131f9c5896f ts=2026-10-08T18:48:35.8270000Z; 23h 30m: 6ab9a9279a8420a1e6b56b76.jsonl[1084] _id=6ac54944de269131f9b79b2b ts=2026-10-06T19:17:23.3600000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1099] _id=6ac693d9de269131f9be1457 ts=2026-10-07T18:47:53.4200000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 41 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[10590] _id=6ad12479de269131f9dff11e ts=2026-10-15T19:07:35.8970000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[10591] _id=6ad12479de269131f9dff11f ts=2026-10-15T19:07:35.8970000Z; 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[4056] _id=6ace33dbde269131f9ceb933 ts=2026-10-13T13:36:23.7940000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4057] _id=6ace33dbde269131f9ceb934 ts=2026-10-13T13:36:23.7940000Z; 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[5731] _id=6acfa957de269131f9d542a6 ts=2026-10-14T16:09:58.2310000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[5732] _id=6acfa957de269131f9d542a7 ts=2026-10-14T16:09:58.2310000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 114h 49m 
  - Evidence: 114h 49m: 6ab9a9279a8420a1e6b56b76.jsonl[3715] _id=6ac7e9cbde269131f9c62f5d ts=2026-10-08T19:06:50.5590000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4528] _id=6ace3888de269131f9cef779 ts=2026-10-13T13:56:23.2920000Z; 23h 57m: 6ab9a9279a8420a1e6b56b76.jsonl[2685] _id=6ac69705de269131f9bebec9 ts=2026-10-07T19:01:25.6970000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[3086] _id=6ac7e80ade269131f9c5e033 ts=2026-10-08T18:59:21.9300000Z; 23h 37m: 6ab9a9279a8420a1e6b56b76.jsonl[998] _id=6ac5481ade269131f9b7718b ts=2026-10-06T19:12:24.9890000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1129] _id=6ac69439de269131f9be24ee ts=2026-10-07T18:49:29.5770000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[10904] _id=6ad126bede269131f9e04526 ts=2026-10-15T19:17:17.4960000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[10905] _id=6ad126bede269131f9e04527 ts=2026-10-15T19:17:17.4960000Z; 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[10966] _id=6ad12792de269131f9e04be1 ts=2026-10-15T19:20:49.5580000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[10967] _id=6ad12792de269131f9e04be2 ts=2026-10-15T19:20:49.5580000Z; 4ms: 6ab9a9279a8420a1e6b56b76.jsonl[501] _id=6ac54242de269131f9b6e537 ts=2026-10-06T18:47:29.7150000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[502] _id=6ac54242de269131f9b6e542 ts=2026-10-06T18:47:29.7190000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 114h 18m 
  - Evidence: 114h 18m: 6ab9a9279a8420a1e6b56b76.jsonl[4038] _id=6ac7ec67de269131f9c68887 ts=2026-10-08T19:17:59.2450000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4054] _id=6ace33dbde269131f9ceb931 ts=2026-10-13T13:36:21.6120000Z; 23h 31m: 6ab9a9279a8420a1e6b56b76.jsonl[2921] _id=6ac69ac1de269131f9bf20aa ts=2026-10-07T19:17:21.1110000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2930] _id=6ac7e583de269131f9c5894b ts=2026-10-08T18:48:31.6130000Z; 23h 29m: 6ab9a9279a8420a1e6b56b76.jsonl[1086] _id=6ac54956de269131f9b79c8f ts=2026-10-06T19:17:41.0180000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1093] _id=6ac693b2de269131f9be0d81 ts=2026-10-07T18:47:10.7450000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 114h 26m 
  - Evidence: 114h 26m: 6ab9a9279a8420a1e6b56b76.jsonl[3893] _id=6ac7ea86de269131f9c6530c ts=2026-10-08T19:09:56.3240000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4065] _id=6ace33dbde269131f9ceb944 ts=2026-10-13T13:36:25.7010000Z; 24h 2m: 6ab9a9279a8420a1e6b56b76.jsonl[2652] _id=6ac696b4de269131f9beb2d5 ts=2026-10-07T19:00:02.1940000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[3120] _id=6ac7e8bfde269131f9c5fa2c ts=2026-10-08T19:02:21.7400000Z; 23h 48m: 6ab9a9279a8420a1e6b56b76.jsonl[4865] _id=6ace7ca3de269131f9d12320 ts=2026-10-13T18:46:57.6970000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[6641] _id=6acfcb83de269131f9d72888 ts=2026-10-14T18:35:45.7970000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1466 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[10518] _id=6ad12488de269131f9dff3aa ts=2026-10-15T19:07:50.2850000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[10617] _id=6ad12488de269131f9dff3b0 ts=2026-10-15T19:07:50.2850000Z; 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[10592] _id=6ad1247bde269131f9dff174 ts=2026-10-15T19:07:37.1930000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[10593] _id=6ad1247bde269131f9dff18d ts=2026-10-15T19:07:37.1930000Z; 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[10593] _id=6ad1247bde269131f9dff18d ts=2026-10-15T19:07:37.1930000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[10597] _id=6ad1247bde269131f9dff198 ts=2026-10-15T19:07:37.1930000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 142h 0m 
  - Evidence: 142h 0m: 6ab9a9279a8420a1e6b56b76.jsonl[3139] _id=6ac7e873de269131f9c5eee4 ts=2026-10-08T19:01:06.6150000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[6462] _id=6acfb578de269131f9d63599 ts=2026-10-14T17:01:44.6580000Z; 23h 57m: 6ab9a9279a8420a1e6b56b76.jsonl[2686] _id=6ac69708de269131f9bebf1d ts=2026-10-07T19:01:28.5960000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[3090] _id=6ac7e80ade269131f9c5e02c ts=2026-10-08T18:59:21.9250000Z; 21h 24m: 6ab9a9279a8420a1e6b56b76.jsonl[6621] _id=6acfcb5cde269131f9d721e6 ts=2026-10-14T18:35:07.3180000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[8536] _id=6ad0f86ede269131f9dd045d ts=2026-10-15T15:59:42.4110000Z
- **INFO / Info** `SolarStillDesignEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.006s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[12881] _id=6ad17d36de269131f9e27c8b ts=2026-10-16T01:26:13.9250000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12882] _id=6ad17d36de269131f9e27c8c ts=2026-10-16T01:26:13.9250000Z; 6ms: 6ab9a9279a8420a1e6b56b76.jsonl[12880] _id=6ad17d36de269131f9e27c89 ts=2026-10-16T01:26:13.9190000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12881] _id=6ad17d36de269131f9e27c8b ts=2026-10-16T01:26:13.9250000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 114h 57m 
  - Evidence: 114h 57m: 6ab9a9279a8420a1e6b56b76.jsonl[2980] _id=6ac7e624de269131f9c59a3e ts=2026-10-08T18:51:16.0600000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4399] _id=6ace36a3de269131f9cedc6a ts=2026-10-13T13:48:18.6060000Z; 26h 13m: 6ab9a9279a8420a1e6b56b76.jsonl[4401] _id=6ace36b2de269131f9cedd4e ts=2026-10-13T13:48:33.7010000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[5527] _id=6acfa799de269131f9d51d95 ts=2026-10-14T16:02:32.8700000Z; 23h 45m: 6ab9a9279a8420a1e6b56b76.jsonl[741] _id=6ac54658de269131f9b74071 ts=2026-10-06T19:04:55.1590000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1162] _id=6ac6948dde269131f9be34d5 ts=2026-10-07T18:50:53.0890000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.036s shown 
  - Evidence: 21ms: 6ab9a9279a8420a1e6b56b76.jsonl[2819] _id=6ac69926de269131f9befe25 ts=2026-10-07T19:10:30.5260000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2823] _id=6ac69926de269131f9befe29 ts=2026-10-07T19:10:30.5470000Z; 36ms: 6ab9a9279a8420a1e6b56b76.jsonl[2824] _id=6ac69926de269131f9befe23 ts=2026-10-07T19:10:30.4900000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2819] _id=6ac69926de269131f9befe25 ts=2026-10-07T19:10:30.5260000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 55m 
  - Evidence: 167h 55m: 6ab9a9279a8420a1e6b56b76.jsonl[883] _id=6ac54788de269131f9b767b9 ts=2026-10-06T19:09:59.5320000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[5119] _id=6ace80fdde269131f9d153d7 ts=2026-10-13T19:05:33.0740000Z; 26h 24m: 6ab9a9279a8420a1e6b56b76.jsonl[6353] _id=6acfb4adde269131f9d619fd ts=2026-10-14T16:58:21.6090000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[11057] _id=6ad12828de269131f9e0510c ts=2026-10-15T19:23:19.5230000Z; 21h 46m: 6ab9a9279a8420a1e6b56b76.jsonl[5332] _id=6ace822bde269131f9d17e0e ts=2026-10-13T19:10:34.1750000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[6277] _id=6acfb44dde269131f9d611b7 ts=2026-10-14T16:56:45.1660000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 55m 
  - Evidence: 167h 55m: 6ab9a9279a8420a1e6b56b76.jsonl[928] _id=6ac54788de269131f9b767c1 ts=2026-10-06T19:09:59.5530000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[5110] _id=6ace80f1de269131f9d15311 ts=2026-10-13T19:05:20.4100000Z; 26h 24m: 6ab9a9279a8420a1e6b56b76.jsonl[6357] _id=6acfb4aede269131f9d61a07 ts=2026-10-14T16:58:21.7070000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[11032] _id=6ad1281cde269131f9e05036 ts=2026-10-15T19:23:07.0600000Z; 21h 45m: 6ab9a9279a8420a1e6b56b76.jsonl[5330] _id=6ace822bde269131f9d17e11 ts=2026-10-13T19:10:34.2010000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[6240] _id=6acfb42ade269131f9d60ea7 ts=2026-10-14T16:56:10.2380000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 55m 
  - Evidence: 167h 55m: 6ab9a9279a8420a1e6b56b76.jsonl[917] _id=6ac5477fde269131f9b7670d ts=2026-10-06T19:09:50.5460000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[5101] _id=6ace80ecde269131f9d152b7 ts=2026-10-13T19:05:15.2460000Z; 26h 24m: 6ab9a9279a8420a1e6b56b76.jsonl[6352] _id=6acfb4acde269131f9d619ce ts=2026-10-14T16:58:20.4290000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[11018] _id=6ad12811de269131f9e04fd5 ts=2026-10-15T19:22:56.4830000Z; 21h 45m: 6ab9a9279a8420a1e6b56b76.jsonl[5329] _id=6ace8229de269131f9d17dc8 ts=2026-10-13T19:10:32.4850000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[6245] _id=6acfb42fde269131f9d60f1b ts=2026-10-14T16:56:15.3030000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 42 interval(s) ≤ 0.005s..0.024s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b76.jsonl[12646] _id=6ad17bdade269131f9e274ba ts=2026-10-16T01:20:26.3840000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12642] _id=6ad17bdade269131f9e274bc ts=2026-10-16T01:20:26.3890000Z; 20ms: 6ab9a9279a8420a1e6b56b76.jsonl[12745] _id=6ad17c52de269131f9e27740 ts=2026-10-16T01:22:25.8650000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12753] _id=6ad17c52de269131f9e27742 ts=2026-10-16T01:22:25.8850000Z; 24ms: 6ab9a9279a8420a1e6b56b76.jsonl[12747] _id=6ad17c53de269131f9e2774a ts=2026-10-16T01:22:27.2110000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12748] _id=6ad17c53de269131f9e2774c ts=2026-10-16T01:22:27.2350000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 167h 56m 
  - Evidence: 167h 56m: 6ab9a9279a8420a1e6b56b76.jsonl[918] _id=6ac5477dde269131f9b766e9 ts=2026-10-06T19:09:48.4670000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[5160] _id=6ace8133de269131f9d15965 ts=2026-10-13T19:06:26.6690000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 28m 38s 
  - Evidence: 28m 38s: 6ab9a9279a8420a1e6b56b76.jsonl[11586] _id=6ad17378de269131f9e247ce ts=2026-10-16T00:44:39.6220000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12477] _id=6ad17a2ede269131f9e26c5e ts=2026-10-16T01:13:17.8270000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 114h 47m 
  - Evidence: 114h 47m: 6ab9a9279a8420a1e6b56b76.jsonl[2927] _id=6ac7e576de269131f9c5889e ts=2026-10-08T18:48:21.1750000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4041] _id=6ace33ccde269131f9ceb850 ts=2026-10-13T13:36:11.3750000Z; 24h 1m: 6ab9a9279a8420a1e6b56b76.jsonl[1090] _id=6ac6939ede269131f9be0a8b ts=2026-10-07T18:46:53.9260000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2927] _id=6ac7e576de269131f9c5889e ts=2026-10-08T18:48:21.1750000Z; 23h 32m: 6ab9a9279a8420a1e6b56b76.jsonl[1028] _id=6ac54899de269131f9b780c9 ts=2026-10-06T19:14:31.9330000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1090] _id=6ac6939ede269131f9be0a8b ts=2026-10-07T18:46:53.9260000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 114h 47m 
  - Evidence: 114h 47m: 6ab9a9279a8420a1e6b56b76.jsonl[2926] _id=6ac7e576de269131f9c5889d ts=2026-10-08T18:48:21.1750000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4040] _id=6ace33ccde269131f9ceb84f ts=2026-10-13T13:36:11.3750000Z; 24h 1m: 6ab9a9279a8420a1e6b56b76.jsonl[1089] _id=6ac6939ede269131f9be0a8a ts=2026-10-07T18:46:53.9260000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2926] _id=6ac7e576de269131f9c5889d ts=2026-10-08T18:48:21.1750000Z; 23h 32m: 6ab9a9279a8420a1e6b56b76.jsonl[1029] _id=6ac54899de269131f9b780bd ts=2026-10-06T19:14:31.9320000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1089] _id=6ac6939ede269131f9be0a8a ts=2026-10-07T18:46:53.9260000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 114h 40m 
  - Evidence: 114h 40m: 6ab9a9279a8420a1e6b56b76.jsonl[4042] _id=6ace33ccde269131f9ceb84c ts=2026-10-08T19:18:04.256Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4575] _id=6ace7a47de269131f9d0fbc7 ts=2026-10-13T13:58:40.744Z; 48h 0m: 6ab9a9279a8420a1e6b56b76.jsonl[1091] _id=6ac6939ede269131f9be0a73 ts=2026-10-06T19:17:50.191Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4042] _id=6ace33ccde269131f9ceb84c ts=2026-10-08T19:18:04.256Z; 24h 6m: 6ab9a9279a8420a1e6b56b76.jsonl[14] _id=6ac3f656de269131f9af6a95 ts=2026-10-05T19:11:18.1930000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1091] _id=6ac6939ede269131f9be0a73 ts=2026-10-06T19:17:50.191Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b76.jsonl[6531] _id=6acfb5dcde269131f9d63f2e ts=2026-10-14T17:03:24.2660000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[6536] _id=6acfca15de269131f9d7116e ts=2026-10-14T17:03:24.266Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 114h 22m 
  - Evidence: 114h 22m: 6ab9a9279a8420a1e6b56b76.jsonl[3963] _id=6ac7eb65de269131f9c66b1f ts=2026-10-08T19:13:41.0590000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[4064] _id=6ace33dbde269131f9ceb936 ts=2026-10-13T13:36:23.8540000Z; 23h 38m: 6ab9a9279a8420a1e6b56b76.jsonl[2810] _id=6ac69911de269131f9befc97 ts=2026-10-07T19:10:09.3590000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[2933] _id=6ac7e583de269131f9c5894c ts=2026-10-08T18:48:33.8110000Z; 23h 31m: 6ab9a9279a8420a1e6b56b76.jsonl[1057] _id=6ac548f8de269131f9b79007 ts=2026-10-06T19:16:06.7520000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[1094] _id=6ac693b2de269131f9be0d82 ts=2026-10-07T18:47:13.2570000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.001s..0.005s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b76.jsonl[12813] _id=6ad17cb6de269131f9e2796b ts=2026-10-16T01:24:05.4290000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[12814] _id=6ad17cb6de269131f9e2796c ts=2026-10-16T01:24:05.4300000Z; 2ms: 6ab9a9279a8420a1e6b56b76.jsonl[814] _id=6ac5469fde269131f9b74bdf ts=2026-10-06T19:06:05.8090000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[815] _id=6ac5469fde269131f9b74be1 ts=2026-10-06T19:06:05.8110000Z; 5ms: 6ab9a9279a8420a1e6b56b76.jsonl[11946] _id=6ad17575de269131f9e24fe9 ts=2026-10-16T00:53:09.1430000Z -> 6ab9a9279a8420a1e6b56b76.jsonl[11941] _id=6ad17575de269131f9e24feb ts=2026-10-16T00:53:09.1480000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[927] _id=6ac5479cde269131f9b768fd ts=2026-10-06T19:10:19.2160000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[2963] _id=6ac7e5eede269131f9c5922f ts=2026-10-08T18:50:21.4920000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[3805] _id=6ac7ea76de269131f9c6504a ts=2026-10-08T19:09:42.1270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[6357] _id=6acfb4aede269131f9d61a07 ts=2026-10-14T16:58:21.7070000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[11050] _id=6ad12828de269131f9e05114 ts=2026-10-15T19:23:19.6630000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[875] _id=6ac5471fde269131f9b760ab ts=2026-10-06T19:08:14.1620000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[11586] _id=6ad17378de269131f9e247ce ts=2026-10-16T00:44:39.6220000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[12477] _id=6ad17a2ede269131f9e26c5e ts=2026-10-16T01:13:17.8270000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[6631] _id=6acfcb7dde269131f9d727f6 ts=2026-10-14T18:35:40.7020000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 54 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[3272] _id=6ac7e963de269131f9c61a50 ts=2026-10-08T19:05:03.7540000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[3275] _id=6ac7e963de269131f9c61a53 ts=2026-10-08T19:05:03.7540000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[3283] _id=6ac7e963de269131f9c61a81 ts=2026-10-08T19:05:05.2370000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 80 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[1184] _id=6ac694bade269131f9be3d0e ts=2026-10-07T18:51:38.1780000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[1185] _id=6ac694bade269131f9be3d0f ts=2026-10-07T18:51:38.1780000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[1180] _id=6ac694bbde269131f9be3d2c ts=2026-10-07T18:51:38.1780000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[6572] _id=6acfcb36de269131f9d71dd4 ts=2026-10-14T18:34:29.3790000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 11 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[2959] _id=6ac7e5e4de269131f9c59151 ts=2026-10-08T18:50:11.7790000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[2978] _id=6ac7e621de269131f9c599c8 ts=2026-10-08T18:51:13.2280000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[4399] _id=6ace36a3de269131f9cedc6a ts=2026-10-13T13:48:18.6060000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[897] _id=6ac5476ade269131f9b76573 ts=2026-10-06T19:09:29.2630000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[901] _id=6ac5476bde269131f9b765a3 ts=2026-10-06T19:09:30.3030000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[914] _id=6ac5477cde269131f9b766c9 ts=2026-10-06T19:09:47.1000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 453 start, 446 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 963 open, 951 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 18 open, 17 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 5 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 54 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 302 of 13041 adjacent _id pairs reverse in client time; worst 138.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b76.jsonl[1246] _id=6ac694ffde269131f9be49f5 ts=2026-10-07T18:52:47.0990000Z`; `6ab9a9279a8420a1e6b56b76.jsonl[1255] _id=6ac69500de269131f9be4a37 ts=2026-10-07T18:50:28.8620000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.86s, min -411487.92s, max -0.13s over 13042 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b76\coverage.yaml

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

### `InputEvent` — 3549 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (712); Unit 2 Prod (Refactor) (648); Unit 3 Dungeon Dev (561); Unit 3 Dev (557); Unit 1 Dev (377); Unit 5 Dev - Dungeon (338); Unit 4 Dev (201); Unit 4 Dev - Anderson Base (87); Unit 5 Dev (68)
- **Intervals:** median 1.54s (p5 0.17s / p95 25.33s, n=3548)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3549/3549 records)
    "pressed"  x3549
data.actionType  (string, 3549/3549 records)
    "Move"  x2324
    "Interact"  x787
    "Jump"  x203
    "Hoverboard"  x87
    "Sprint"  x64
    "Ascend"  x34
    "Descend"  x27
    "Map"  x8
    "Pause"  x5
    "SkipCinematic"  x5
    "ToggleDebug"  x5
data.key  (string, 3549/3549 records, 13 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3549/3549 records)
    "Player"  x2837
    "Drone"  x712
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3246 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1998); Unit 4 Dev (620); Unit 3 Dungeon Dev (430); Unit 5 Dev - Dungeon (198)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.04s, n=3245)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3246/3246 records)
    "BecameVisible"  x963
    "BecameInvisible"  x951
    "BecameCameraCentered"  x666
    "BecameCameraUncentered"  x666
data.pieceId  (string, 3246/3246 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3246/3246 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2395 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (746); Unit 3 Dev (350); Unit 4 Dev (317); Unit 5 Dev (239); Unit 1 Dev (209); Unit 3 Dungeon Dev (204); Unit 4 Dev - Dungeon (188); Unit 5 Dev - Dungeon (72); Unit 4 Dev - Anderson Base (70)
- **eventKey:** present on 1496 of 2395 records
- **Intervals:** median 4.39s (p5 0.00s / p95 30.53s, n=2394)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1496; [conversationId, dialogueEventType] x899
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2395/2395 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2395/2395 records)
    "DialogueNodeEvent"  x1496
    "DialogueStartEvent"  x453
    "DialogueFinishEvent"  x446
data.nodeId  (number, 1496/2395 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2368 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (665); Unit 3 Dev (316); Unit 1 Dev (269); Unit 3 Dungeon Dev (268); Unit 4 Dev (252); Unit 4 Dev - Dungeon (250); Unit 5 Dev - Dungeon (171); Unit 5 Dev (124); Unit 4 Dev - Anderson Base (53)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.11s, n=2356)
- **Fields under `data`:**

```text
data.position  (object, 2368/2368 records)
data.position.x  (number, 2368/2368 records)
    numeric range -833.409 .. 1840.38 (895 unique)
data.position.y  (number, 2368/2368 records)
    numeric range -115.127 .. 221.597 (572 unique)
data.position.z  (number, 2368/2368 records)
    numeric range -1163.81 .. 2328.29 (896 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 480 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (168); Unit 3 Dungeon Dev (91); Unit 1 Dev (74); Unit 2 Prod (Refactor) (68); Unit 4 Dev (36); Unit 3 Dev (13); Unit 5 Dev (11); Unit 5 Dev - Dungeon (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 7.59s (p5 0.26s / p95 259.21s, n=479)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 480/480 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 480/480 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 375 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (139); Unit 5 Dev (98); Unit 3 Dev (71); Unit 1 Dev (40); Unit 4 Dev - Anderson Base (27)
- **Intervals:** median 0.44s (p5 0.03s / p95 13.54s, n=374)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 375/375 records)
    "argumentationNodeHoverEnd"  x157
    "argumentationNodeHoverStart"  x156
    "argumentationNodeAdd"  x41
    "argumentationNodeRemove"  x21
data.argumentationTitle  (string, 375/375 records)
    "Unit 2 – Watershed"  x139
    "Unit 5"  x98
    "Unit 3 - Pollution Upstream"  x71
    "Unit 4 - Flooding"  x27
    "Unit 1 - Argumentation Tutorial"  x25
    "Unit 1 - Freshwater"  x15
data.nodeName  (string, 375/375 records)
    "1"  x63
    "I"  x51
    "C"  x46
    "A"  x43
    "II"  x37
    "B"  x36
    "4"  x28
    "2"  x25
    "D"  x22
    "3"  x21
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 147 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (93); Unit 2 Prod (Refactor) (32); Unit 4 Dev (22)
- **Intervals:** median 0.46s (p5 0.15s / p95 8.00s, n=146)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x138; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/147 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/147 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x3
    "Unit 4 Dev"  x2
data.actionType  (string, 138/147 records)
    "RightDrag"  x72
    "LeftDrag"  x66
data.currentSoilType  (string, 138/147 records)
    "CLAY"  x27
    "CLAYSAND"  x27
    "CLAYROCK"  x26
    "SAND"  x23
    "SANDGRAVEL"  x16
    "BEDROCK"  x12
    "GRAVEL"  x7
data.isCorrectSelection  (string, 138/147 records)
    "false"  x111
    "true"  x27
data.waterLevelStatus  (string, 138/147 records)
    "Proper"  x57
    "TooLow"  x45
    "TooHigh"  x36
data.waterRetentionChange  (string, 138/147 records)
    "Decrease"  x59
    "Increase"  x52
    "NoChange"  x27
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 92 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 4 Dev - Dungeon (18); Unit 3 Dev (14); Unit 1 Dev (13); Unit 4 Dev (10); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 92 of 92 records
- **Intervals:** median 205.35s (p5 0.01s / p95 73983.85s, n=91)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 92/92 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x38
data.questID  (string, 92/92 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 92/92 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/92 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 91 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (91)
- **Intervals:** median 5.00s (p5 0.31s / p95 76.81s, n=90)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 91/91 records)
    "On"  x50
    "Off"  x41
data.floor  (string, 91/91 records)
    "4"  x72
    "3"  x12
    "2"  x4
    "1"  x3
data.machineNumber  (string, 91/91 records)
    "One"  x90
    "Two"  x1
data.machineType  (string, 91/91 records)
    "Condenser"  x48
    "Evaporator"  x36
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 91/91 records)
    "3"  x62
    "2"  x21
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TopographicMapEvent` — 62 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (28); Unit 2 Prod (Refactor) (23); Unit 1 Dev (11)
- **Intervals:** median 5.98s (p5 0.68s / p95 84763.69s, n=61)
- **`data` key-set variants:** [actionType, featureUsed] x35; [actionType, featureUsed, location] x21; [actionType, featureUsed, legendName] x6
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "MapOpenEvent"  x18
    "MapCloseEvent"  x17
    "WaypointMoveEvent"  x15
    "Selected"  x6
    "WaypointSetEvent"  x6
data.featureUsed  (string, 62/62 records)
    "Map"  x35
    "Waypoint"  x21
    "Legend"  x6
data.legendName  (string, 6/62 records)
    "Commons"  x2
    "Jasper's Room"  x1
    "PodBay"  x1
    "Teleporter Room"  x1
    "Toppo's Room"  x1
data.location  (object, 21/62 records)
data.location.x  (number, 21/62 records)
    numeric range -251.928 .. 576.151 (20 unique)
data.location.y  (number, 21/62 records)
    numeric range -290.047 .. 238.853 (20 unique)
data.location.z  (number, 21/62 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 54 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 5 Dev (13); Unit 3 Dev (7); Unit 1 Dev (6); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 7.03s (p5 0.21s / p95 44206.01s, n=53)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "submitAnswerEvent"  x54
data.answerSubmitted  (string, 54/54 records)
    18 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 54/54 records)
    "Unit 2 – Watershed"  x27
    "Unit 5"  x13
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 39 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 4 Dev (5); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 566.41s (p5 8.16s / p95 84987.23s, n=38)
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "DebugMenuStateChanged"  x39
data.isOpened  (bool, 39/39 records)
    false  x39
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 30 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (30)
- **Intervals:** median 2.55s (p5 0.34s / p95 147.14s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "ChangeCanister"  x30
data.canisterType  (string, 30/30 records)
    "Sand"  x14
    "Clay"  x10
    "Bedrock"  x4
    "Gravel"  x2
data.floor  (string, 30/30 records)
    "5"  x29
    "4"  x1
data.machine  (string, 30/30 records)
    "1"  x15
    "2"  x15
data.row  (string, 30/30 records)
    "TopRow"  x19
    "BottomRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (22); Unit 3 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 2161.77s (p5 36.22s / p95 86225.46s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 7954.81s (p5 672.62s / p95 135504.69s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 131.40s (p5 0.10s / p95 298859.55s, n=13)
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

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (5); Unit 2 Prod (Refactor) (4); MainMenu (3); Transition (1)
- **Intervals:** median 5816.48s (p5 6.25s / p95 280824.16s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `SolarStillDesignEvent` — 11 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (11)
- **Intervals:** median 2.36s (p5 0.00s / p95 10.54s, n=10)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x10; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "optionSelected"  x10
    "DesignSubmitted"  x1
data.designSelections  (object, 1/11 records)
data.designSelections.glassRoofTemperature  (string, 1/11 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/11 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/11 records)
    "Tilted In"  x1
data.featureUsed  (string, 11/11 records)
    "ExtraCovering"  x4
    "GlassRoofTemperature"  x3
    "RoofStyle"  x3
    "Submit"  x1
data.selectedOption  (string, 10/11 records, 3 empty-string)
    ""  x3
    "Covered"  x2
    "Cold"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 9.55s (p5 1.41s / p95 244.94s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 5 empty-string)
    "cameraPlaced"  x6
    ""  x5
data.boxId  (string, 11/11 records)
    "1"  x4
    "2"  x4
    "0"  x3
data.soilType  (string, 11/11 records)
    "Clay"  x4
    "Sand"  x3
    "Gravel"  x2
    "None"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 4.10s (p5 0.34s / p95 423222.55s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Freshwater"  x7
    "Unit 2 – Watershed"  x1
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dungeon Dev (4); Unit 3 Dev (2)
- **Intervals:** median 9.36s (p5 1.49s / p95 6778.31s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 96275.67s (p5 15739.13s / p95 529890.52s, n=4)
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1718.20s (p5 1718.20s / p95 1718.20s, n=1)
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

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (32 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "Selected" (6x); "WaypointMoveEvent" (15x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (6x); "Waypoint" (21x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (21x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*