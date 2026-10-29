# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9439a8420a1e6b56ba5

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9439a8420a1e6b56ba5
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56ba5.jsonl
- **Records:** 12978 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56ba5
- **Time span:** 2026-10-05T20:03:50.568000+00:00 .. 2026-10-19T09:43:12.554000+00:00 (325h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9439a8420a1e6b56ba5\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 12978 records, 11 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 99 INFO, 0 NOT_TESTED, 103 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4429 | 34.13 | 1 | 9 | 0 | 2026-10-05T20:04:11.337000+00:00 | 2026-10-19T09:43:12.554000+00:00 | 325h 39m |
| PuzzlePieceVisibleEvent | 2846 | 21.93 | 1 | 4 | 0 | 2026-10-06T19:51:38.339000+00:00 | 2026-10-19T09:05:15.953000+00:00 | 301h 13m |
| DialogueEvent | 2406 | 18.54 | 1 | 9 | 1472 | 2026-10-05T20:04:27.607000+00:00 | 2026-10-19T09:43:03.085000+00:00 | 325h 38m |
| PlayerPositionEvent | 1853 | 14.28 | 1 | 9 | 0 | 2026-10-05T20:04:07.755000+00:00 | 2026-10-19T09:43:12.535000+00:00 | 325h 39m |
| argumentationNodeEvent | 522 | 4.02 | 1 | 5 | 0 | 2026-10-06T19:41:33.962000+00:00 | 2026-10-19T09:30:02.423000+00:00 | 301h 48m |
| ObjectInterEvent | 318 | 2.45 | 1 | 9 | 0 | 2026-10-05T20:10:05.677000+00:00 | 2026-10-19T09:43:12.554000+00:00 | 325h 33m |
| TopographicMapEvent | 122 | 0.94 | 1 | 2 | 0 | 2026-10-06T19:52:46.455000+00:00 | 2026-10-14T20:00:23.571000+00:00 | 192h 7m |
| questEvent | 86 | 0.66 | 1 | 9 | 86 | 2026-10-05T20:04:27.577000+00:00 | 2026-10-19T09:39:04.648000+00:00 | 325h 34m |
| Soil Key Puzzle | 68 | 0.52 | 1 | 3 | 0 | 2026-10-06T20:00:09.685000+00:00 | 2026-10-15T19:34:06.421000+00:00 | 215h 33m |
| argumentationAnswerEvent | 56 | 0.43 | 1 | 5 | 0 | 2026-10-06T19:42:28.599000+00:00 | 2026-10-19T09:30:03.656000+00:00 | 301h 47m |
| DEBUGMenu | 43 | 0.33 | 1 | 9 | 0 | 2026-10-05T20:04:07.739000+00:00 | 2026-10-19T08:59:43.860000+00:00 | 324h 55m |
| gameWindowFocusEvent | 39 | 0.3 | 1 | 6 | 0 | 2026-10-05T20:03:50.568000+00:00 | 2026-10-19T08:59:35.314000+00:00 | 324h 55m |
| WaterChamberEvent | 37 | 0.29 | 1 | 1 | 0 | 2026-10-16T20:10:17.089000+00:00 | 2026-10-19T09:16:37.654000+00:00 | 61h 6m |
| argumentationToolEvent | 26 | 0.2 | 1 | 4 | 0 | 2026-10-06T19:42:16.123000+00:00 | 2026-10-19T09:29:24.186000+00:00 | 301h 47m |
| gameWindowUnfocusEvent | 25 | 0.19 | 1 | 6 | 0 | 2026-10-05T20:07:42.333000+00:00 | 2026-10-16T20:05:39.784000+00:00 | 263h 57m |
| gameStartEvent | 20 | 0.15 | 1 | 1 | 0 | 2026-10-05T20:03:50.570000+00:00 | 2026-10-19T08:59:35.314000+00:00 | 324h 55m |
| DaniEvent | 18 | 0.14 | 1 | 1 | 0 | 2026-10-08T19:41:53.622000+00:00 | 2026-10-08T19:42:11.438000+00:00 | 17.8s |
| argumentationEvent | 17 | 0.13 | 1 | 5 | 0 | 2026-10-06T19:42:18.460000+00:00 | 2026-10-19T09:30:03.722000+00:00 | 301h 47m |
| TerasGardenBox | 16 | 0.12 | 1 | 1 | 0 | 2026-10-16T07:52:19.869000+00:00 | 2026-10-16T07:53:17.737000+00:00 | 57.9s |
| soilMachine | 13 | 0.1 | 1 | 1 | 0 | 2026-10-15T19:47:58.638000+00:00 | 2026-10-15T19:54:31.940000+00:00 | 6m 33s |
| SolarStillDesignEvent | 7 | 0.05 | 1 | 1 | 0 | 2026-10-19T09:36:09.239000+00:00 | 2026-10-19T09:36:18.610000+00:00 | 9.4s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T19:46:26.928000+00:00 | 2026-10-19T09:43:12.542000+00:00 | 301h 56m |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-16T15:55:58.841000+00:00 | 2026-10-19T09:17:54.450000+00:00 | 65h 21m |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 219659.758s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.066s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.933s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.347s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 7.831s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.438s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 15069.126s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 14967.256s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 224.113s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 31.537s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 12.824s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 18 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
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
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 11.2x vs baseline. 
  - Observed: 56 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 1,; A,1,; A,B,C,1,II; A,B,C,2,II; A,B,C,3,II; A,C,2,II; A,C,B,2,II; B,A,2,1,I; B,C,2,II; B,C,D,2,II; C,A,2,II; C,A,4,II; C,B,A,2,II; C,B,A,4,II; C,D,4,2,II; C,D,4,3,II; C,D,4,II; D,3,4,II; D,3,II; D,C,3,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.7x vs baseline. 
  - Observed: 522 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[4] _id=6ac402a7de269131f9af8d81 ts=2026-10-05T20:03:50.5700000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[172] _id=6ac54b54de269131f9b79df8 ts=2026-10-06T19:26:11.2350000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[653] _id=6ac55067de269131f9b7b823 ts=2026-10-06T19:47:50.6990000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 39 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 39} 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[3] _id=6ac402a7de269131f9af8d7f ts=2026-10-05T20:03:50.5680000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[53] _id=6ac40391de269131f9af91ef ts=2026-10-05T20:07:44.3630000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[51] _id=6ac403a1de269131f9af922f ts=2026-10-05T20:08:00.0420000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[49] _id=6ac4038fde269131f9af91e5 ts=2026-10-05T20:07:42.3330000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[56] _id=6ac403a0de269131f9af9229 ts=2026-10-05T20:07:59.3850000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[715] _id=6ac55109de269131f9b7bdbc ts=2026-10-06T19:50:32.8210000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4428 | 0.0 | 0.843 | 264.756 | 13.108 | 429758.811 | 0.23 | 186 | 11 |
| PuzzlePieceVisibleEvent | 2845 | 0.0 | 0.066 | 381.166 | 1.86 | 517782.011 | 0.16 | 1229 | 8 |
| DialogueEvent | 2405 | 0.0 | 3.496 | 487.449 | 27.185 | 429721.33 | 0.12 | 696 | 10 |
| PlayerPositionEvent | 1839 | 0.0 | 10.001 | 320.291 | 10.299 | 218903.128 | 0.19 | 1 | 6 |
| argumentationNodeEvent | 521 | 0.0 | 0.446 | 2085.429 | 11.45 | 431935.203 | 0.03 | 88 | 5 |
| ObjectInterEvent | 317 | 0.0 | 8.351 | 3697.119 | 323.408 | 430569.795 | 0.02 | 6 | 12 |
| TopographicMapEvent | 121 | 0.027 | 2.639 | 5716.175 | 306.955 | 431081.954 | 0.01 | 2 | 5 |
| questEvent | 85 | 0.0 | 188.146 | 13789.142 | 84184.428 | 429843.919 | 0.0 | 14 | 17 |
| Soil Key Puzzle | 67 | 0.16 | 1.933 | 11582.638 | 58795.944 | 518557.921 | 0.01 | 0 | 4 |
| argumentationAnswerEvent | 55 | 0.005 | 7.831 | 19753.728 | 173311.873 | 431952.856 | 0.0 | 2 | 5 |
| DEBUGMenu | 42 | 6.2 | 459.188 | 27850.86 | 84614.857 | 429611.398 | 0.0 | 0 | 19 |
| gameWindowFocusEvent | 38 | 0.935 | 224.113 | 30782.756 | 104803.437 | 429611.556 | 0.0 | 0 | 17 |
| WaterChamberEvent | 36 | 0.132 | 12.408 | 6110.571 | 78.544 | 219221.747 | 0.01 | 0 | 1 |
| argumentationToolEvent | 25 | 0.544 | 1.438 | 43457.123 | 380350.951 | 480386.76 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 24 | 0.0 | 31.537 | 39594.894 | 159794.039 | 432685.75 | 0.0 | 2 | 9 |
| gameStartEvent | 19 | 26.983 | 14967.256 | 61565.513 | 240199.041 | 429611.557 | 0.0 | 0 | 17 |
| DaniEvent | 17 | 0.01 | 0.175 | 1.048 | 4.082 | 10.911 | 57.25 | 1 | 0 |
| argumentationEvent | 16 | 0.035 | 123.197 | 67904.079 | 306824.946 | 431918.063 | 0.0 | 2 | 5 |
| TerasGardenBox | 15 | 0.121 | 1.347 | 3.858 | 16.735 | 21.164 | 15.55 | 0 | 0 |
| soilMachine | 12 | 2.205 | 12.824 | 32.775 | 116.356 | 168.852 | 1.83 | 0 | 0 |
| SolarStillDesignEvent | 6 | 0.89 | 1.631 | 1.562 | 2.013 | 2.081 | 38.42 | 0 | 0 |
| EndOfUnit | 4 | 129325.225 | 219659.758 | 271751.404 | 480386.465 | 518360.874 | 0.0 | 0 | 4 |
| chatEvent | 3 | 1090.726 | 15069.126 | 78438.536 | 198747.094 | 219155.757 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 15 group(s), 34 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[2558] _id=6ac69f45de269131f9bf2214 ts=2026-10-07T19:36:35.9540000Z == 6ab9a9439a8420a1e6b56ba5.jsonl[2559] _id=6ac69f45de269131f9bf2215 ts=2026-10-07T19:36:35.9540000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[2565] _id=6ac69f45de269131f9bf221b ts=2026-10-07T19:36:35.9550000Z == 6ab9a9439a8420a1e6b56ba5.jsonl[2566] _id=6ac69f45de269131f9bf221c ts=2026-10-07T19:36:35.9550000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[3909] _id=6ac7f146de269131f9c6ac41 ts=2026-10-08T19:38:44.3380000Z == 6ab9a9439a8420a1e6b56ba5.jsonl[3910] _id=6ac7f146de269131f9c6ac42 ts=2026-10-08T19:38:44.3380000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 23 group(s), 35 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[777] _id=6ac5516bde269131f9b7c44f ts=2026-10-06T19:52:09.8840000Z == 6ab9a9439a8420a1e6b56ba5.jsonl[783] _id=6ac5516bde269131f9b7c457 ts=2026-10-06T19:52:09.8840000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[800] _id=6ac5516dde269131f9b7c496 ts=2026-10-06T19:52:10.5860000Z == 6ab9a9439a8420a1e6b56ba5.jsonl[802] _id=6ac5516dde269131f9b7c499 ts=2026-10-06T19:52:10.5860000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[778] _id=6ac5516dde269131f9b7c4a1 ts=2026-10-06T19:52:10.6080000Z == 6ab9a9439a8420a1e6b56ba5.jsonl[804] _id=6ac5516dde269131f9b7c4a5 ts=2026-10-06T19:52:10.6080000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[12724] _id=6ad5e367de269131f9e960a2 ts=2026-10-19T09:31:18.3270000Z == 6ab9a9439a8420a1e6b56ba5.jsonl[12725] _id=6ad5e367de269131f9e960a3 ts=2026-10-19T09:31:18.3270000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `356ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4046] _id=6ac7f202de269131f9c6bb90 ts=2026-10-08T19:41:53.6220000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4053] _id=6ac7f202de269131f9c6bbac ts=2026-10-08T19:41:53.9780000Z`; `274ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4048] _id=6ac7f202de269131f9c6bb96 ts=2026-10-08T19:41:53.7870000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4055] _id=6ac7f202de269131f9c6bbae ts=2026-10-08T19:41:54.0610000Z`; `611ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4062] _id=6ac7f205de269131f9c6bbf9 ts=2026-10-08T19:41:56.3160000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4066] _id=6ac7f205de269131f9c6bc22 ts=2026-10-08T19:41:56.9270000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 34 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba5.jsonl[140] _id=6ac4041ede269131f9af95c3 ts=2026-10-05T20:10:05.6770000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[132] _id=6ac4041ede269131f9af95c5 ts=2026-10-05T20:10:05.6820000Z`; `3ms: 6ab9a9439a8420a1e6b56ba5.jsonl[219] _id=6ac54b93de269131f9b79f07 ts=2026-10-06T19:27:14.4230000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[225] _id=6ac54b93de269131f9b79f09 ts=2026-10-06T19:27:14.4260000Z`; `638ms: 6ab9a9439a8420a1e6b56ba5.jsonl[1025] _id=6ac551d9de269131f9b7cb08 ts=2026-10-06T19:54:00.7770000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[1017] _id=6ac551dade269131f9b7cb14 ts=2026-10-06T19:54:01.4150000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `181ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10912] _id=6ad1d7bade269131f9e33dd6 ts=2026-10-16T07:52:26.5460000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[10928] _id=6ad1d7bbde269131f9e33dd8 ts=2026-10-16T07:52:26.7270000Z`; `152ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10928] _id=6ad1d7bbde269131f9e33dd8 ts=2026-10-16T07:52:26.7270000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[10929] _id=6ad1d7bbde269131f9e33dda ts=2026-10-16T07:52:26.8790000Z`; `121ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10929] _id=6ad1d7bbde269131f9e33dda ts=2026-10-16T07:52:26.8790000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[10930] _id=6ad1d7bbde269131f9e33ddc ts=2026-10-16T07:52:27.0000000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `205ms: 6ab9a9439a8420a1e6b56ba5.jsonl[2810] _id=6ac6a1c3de269131f9bf41c0 ts=2026-10-07T19:47:14.6050000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[2811] _id=6ac6a1c3de269131f9bf41c4 ts=2026-10-07T19:47:14.8100000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `816ms: 6ab9a9439a8420a1e6b56ba5.jsonl[12027] _id=6ad5ddecde269131f9e95b60 ts=2026-10-19T09:07:55.8520000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[12030] _id=6ad5ddedde269131f9e95b6a ts=2026-10-19T09:07:56.6680000Z`; `513ms: 6ab9a9439a8420a1e6b56ba5.jsonl[12028] _id=6ad5ddedde269131f9e95b64 ts=2026-10-19T09:07:56.3510000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[12032] _id=6ad5ddedde269131f9e95b6d ts=2026-10-19T09:07:56.8640000Z`; `385ms: 6ab9a9439a8420a1e6b56ba5.jsonl[12030] _id=6ad5ddedde269131f9e95b6a ts=2026-10-19T09:07:56.6680000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[12048] _id=6ad5ddeede269131f9e95b70 ts=2026-10-19T09:07:57.0530000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `632ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4696] _id=6ac7f72bde269131f9c72861 ts=2026-10-08T20:03:54.8170000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4695] _id=6ac7f72cde269131f9c7286f ts=2026-10-08T20:03:55.4490000Z`; `821ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4695] _id=6ac7f72cde269131f9c7286f ts=2026-10-08T20:03:55.4490000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4698] _id=6ac7f72dde269131f9c7287f ts=2026-10-08T20:03:56.2700000Z`; `201ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10594] _id=6ad1d559de269131f9e33b84 ts=2026-10-16T07:42:17.3340000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[10599] _id=6ad1d559de269131f9e33b86 ts=2026-10-16T07:42:17.5350000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6ab9a9439a8420a1e6b56ba5.jsonl[6526] _id=6ace8e83de269131f9d245af ts=2026-10-13T20:03:14.9090000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[6529] _id=6ace8e83de269131f9d245b2 ts=2026-10-13T20:03:14.9460000Z`; `52ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10263] _id=6ad132d4de269131f9e11aeb ts=2026-10-15T20:08:52.6000000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[10266] _id=6ad132d5de269131f9e11af1 ts=2026-10-15T20:08:52.6520000Z`; `35ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10789] _id=6ad1d66ede269131f9e33ce6 ts=2026-10-16T07:46:53.9660000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[10792] _id=6ad1d66ede269131f9e33ce9 ts=2026-10-16T07:46:54.0010000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 34 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `592ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4662] _id=6ac7f6edde269131f9c7224e ts=2026-10-08T20:02:52.9770000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4661] _id=6ac7f6eede269131f9c72264 ts=2026-10-08T20:02:53.5690000Z`; `243ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4566] _id=6ac7f70dde269131f9c7259b ts=2026-10-08T20:03:24.1780000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4572] _id=6ac7f70dde269131f9c725a9 ts=2026-10-08T20:03:24.4210000Z`; `492ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4569] _id=6ac7f70dde269131f9c7259d ts=2026-10-08T20:03:24.2120000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4568] _id=6ac7f70dde269131f9c725bf ts=2026-10-08T20:03:24.7040000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `832ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4622] _id=6ac7f6c4de269131f9c71e05 ts=2026-10-08T20:02:11.3610000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4623] _id=6ac7f6c5de269131f9c71e1d ts=2026-10-08T20:02:12.1930000Z`; `620ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4623] _id=6ac7f6c5de269131f9c71e1d ts=2026-10-08T20:02:12.1930000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4621] _id=6ac7f6c5de269131f9c71e35 ts=2026-10-08T20:02:12.8130000Z`; `784ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4621] _id=6ac7f6c5de269131f9c71e35 ts=2026-10-08T20:02:12.8130000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[4624] _id=6ac7f6c6de269131f9c71e4f ts=2026-10-08T20:02:13.5970000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[7646] _id=6acfdb0ede269131f9d9023d ts=2026-10-14T19:42:05.4190000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[7647] _id=6acfdb19de269131f9d902e4 ts=2026-10-14T19:42:05.419Z`; `0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[11248] _id=6ad28394de269131f9e7fa92 ts=2026-10-16T20:05:39.7840000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[11249] _id=6ad283e6de269131f9e7fb8f ts=2026-10-16T20:05:39.784Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba5.jsonl[12871] _id=6ad5e4e2de269131f9e961aa ts=2026-10-19T09:37:37.7440000Z ~ 6ab9a9439a8420a1e6b56ba5.jsonl[12878] _id=6ad5e4e2de269131f9e961ac ts=2026-10-19T09:37:37.7490000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9439a8420a1e6b56ba5.jsonl[4799] _id=6ac7f894de269131f9c74419 ts=2026-10-08T20:09:55.7580000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4800] _id=6ace86bfde269131f9d1f1bd ts=2026-10-13T19:30:07.1560000Z; 60h 52m: 6ab9a9439a8420a1e6b56ba5.jsonl[11256] _id=6ad283efde269131f9e7fbb6 ts=2026-10-16T20:07:08.1760000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11524] _id=6ad5dbf8de269131f9e957cd ts=2026-10-19T08:59:35.1560000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba5.jsonl[2410] _id=6ac554aade269131f9b830a6 ts=2026-10-06T20:06:01.8970000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2552] _id=6ac69f31de269131f9bf21e0 ts=2026-10-07T19:36:17.0640000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.010s..0.010s shown 
  - Evidence: 10ms: 6ab9a9439a8420a1e6b56ba5.jsonl[4073] _id=6ac7f206de269131f9c6bc49 ts=2026-10-08T19:41:57.5300000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4071] _id=6ac7f206de269131f9c6bc4e ts=2026-10-08T19:41:57.5400000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a9439a8420a1e6b56ba5.jsonl[4795] _id=6ac7f83dde269131f9c73f40 ts=2026-10-08T20:08:28.3120000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4817] _id=6ace86d6de269131f9d1f31f ts=2026-10-13T19:30:29.6420000Z; 60h 48m: 6ab9a9439a8420a1e6b56ba5.jsonl[11486] _id=6ad284e2de269131f9e8034d ts=2026-10-16T20:11:14.0830000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11542] _id=6ad5dc0ade269131f9e957eb ts=2026-10-19T08:59:53.2340000Z; 23h 29m: 6ab9a9439a8420a1e6b56ba5.jsonl[3823] _id=6ac6a6d7de269131f9bf8974 ts=2026-10-07T20:08:54.3660000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[3915] _id=6ac7f146de269131f9c6ac47 ts=2026-10-08T19:38:44.3590000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 696 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10203] _id=6ad1327dde269131f9e11399 ts=2026-10-15T20:07:25.5170000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10204] _id=6ad1327dde269131f9e1139a ts=2026-10-15T20:07:25.5170000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10221] _id=6ad13299de269131f9e11615 ts=2026-10-15T20:07:53.1330000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10222] _id=6ad13299de269131f9e11616 ts=2026-10-15T20:07:53.1330000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10236] _id=6ad132cade269131f9e11a1c ts=2026-10-15T20:08:41.6470000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10237] _id=6ad132cade269131f9e11a1d ts=2026-10-15T20:08:41.6470000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6ab9a9439a8420a1e6b56ba5.jsonl[4796] _id=6ac7f83dde269131f9c73f38 ts=2026-10-08T20:08:28.2930000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[8516] _id=6acfe116de269131f9d95b94 ts=2026-10-14T20:07:49.1670000Z; 73h 39m: 6ab9a9439a8420a1e6b56ba5.jsonl[11134] _id=6ad1da42de269131f9e33f92 ts=2026-10-16T08:03:14.3920000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12975] _id=6ad5e631de269131f9e96283 ts=2026-10-19T09:43:12.5420000Z; 48h 22m: 6ab9a9439a8420a1e6b56ba5.jsonl[650] _id=6ac55013de269131f9b7b612 ts=2026-10-06T19:46:26.9280000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4796] _id=6ac7f83dde269131f9c73f38 ts=2026-10-08T20:08:28.2930000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a9439a8420a1e6b56ba5.jsonl[4774] _id=6ac7f80fde269131f9c73b61 ts=2026-10-08T20:07:42.2360000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4805] _id=6ace86cede269131f9d1f297 ts=2026-10-13T19:30:21.0470000Z; 60h 48m: 6ab9a9439a8420a1e6b56ba5.jsonl[11494] _id=6ad284e5de269131f9e80381 ts=2026-10-16T20:11:16.7640000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11541] _id=6ad5dc08de269131f9e957e5 ts=2026-10-19T08:59:51.6160000Z; 23h 29m: 6ab9a9439a8420a1e6b56ba5.jsonl[3865] _id=6ac6a6e8de269131f9bf8a3d ts=2026-10-07T20:09:12.3470000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[3907] _id=6ac7f146de269131f9c6ac3f ts=2026-10-08T19:38:44.3360000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 186 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[11649] _id=6ad5dc99de269131f9e958be ts=2026-10-19T09:02:16.4390000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11664] _id=6ad5dc99de269131f9e958bf ts=2026-10-19T09:02:16.4390000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[2558] _id=6ac69f45de269131f9bf2214 ts=2026-10-07T19:36:35.9540000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2559] _id=6ac69f45de269131f9bf2215 ts=2026-10-07T19:36:35.9540000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[2559] _id=6ac69f45de269131f9bf2215 ts=2026-10-07T19:36:35.9540000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2560] _id=6ac69f45de269131f9bf2216 ts=2026-10-07T19:36:35.9540000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 36m 
  - Evidence: 119h 36m: 6ab9a9439a8420a1e6b56ba5.jsonl[4561] _id=6ac7f63ade269131f9c70b6c ts=2026-10-08T19:59:53.8010000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4905] _id=6ace8824de269131f9d2017c ts=2026-10-13T19:36:03.5960000Z; 72h 59m: 6ab9a9439a8420a1e6b56ba5.jsonl[11127] _id=6ad1da34de269131f9e33f83 ts=2026-10-16T08:03:00.1440000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11733] _id=6ad5dca8de269131f9e95944 ts=2026-10-19T09:02:31.2730000Z; 23h 58m: 6ab9a9439a8420a1e6b56ba5.jsonl[2291] _id=6ac5534ade269131f9b7fdbb ts=2026-10-06T20:00:09.6890000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[3171] _id=6ac6a469de269131f9bf5dc0 ts=2026-10-07T19:58:32.8910000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10061] _id=6ad1319dde269131f9e103f3 ts=2026-10-15T20:03:41.1340000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10062] _id=6ad1319dde269131f9e103f4 ts=2026-10-15T20:03:41.1340000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10117] _id=6ad131d7de269131f9e1074d ts=2026-10-15T20:04:38.7860000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10118] _id=6ad131d7de269131f9e1074e ts=2026-10-15T20:04:38.7860000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10395] _id=6ad1d3fede269131f9e33a13 ts=2026-10-16T07:36:29.7980000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10396] _id=6ad1d3fede269131f9e33a14 ts=2026-10-16T07:36:29.7980000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 60h 48m 
  - Evidence: 60h 48m: 6ab9a9439a8420a1e6b56ba5.jsonl[11500] _id=6ad284e9de269131f9e803ae ts=2026-10-16T20:11:20.7380000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11511] _id=6ad5dc03de269131f9e957d5 ts=2026-10-19T08:59:43.8660000Z; 23h 29m: 6ab9a9439a8420a1e6b56ba5.jsonl[3897] _id=6ac6a6f4de269131f9bf8a84 ts=2026-10-07T20:09:24.2760000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[3906] _id=6ac7f146de269131f9c6ac3e ts=2026-10-08T19:38:39.4930000Z; 23h 26m: 6ab9a9439a8420a1e6b56ba5.jsonl[2546] _id=6ac5558bde269131f9b84d1d ts=2026-10-06T20:09:46.9860000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2556] _id=6ac69f45de269131f9bf2212 ts=2026-10-07T19:36:30.5120000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[6812] _id=6ace9036de269131f9d253fa ts=2026-10-13T20:10:30.2360000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6814] _id=6acfd70fde269131f9d8a2e9 ts=2026-10-13T20:10:30.236Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 49m 
  - Evidence: 143h 49m: 6ab9a9439a8420a1e6b56ba5.jsonl[3979] _id=6ac7f168de269131f9c6aed8 ts=2026-10-08T19:39:17.2820000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6936] _id=6acfd7fdde269131f9d8b657 ts=2026-10-14T19:28:59.2930000Z; 60h 48m: 6ab9a9439a8420a1e6b56ba5.jsonl[11506] _id=6ad284eade269131f9e803c5 ts=2026-10-16T20:11:19.3350000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11513] _id=6ad5dc07de269131f9e957d8 ts=2026-10-19T08:59:50.1020000Z; 24h 1m: 6ab9a9439a8420a1e6b56ba5.jsonl[2265] _id=6ac5530dde269131f9b7f642 ts=2026-10-06T19:59:07.0470000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[3225] _id=6ac6a4efde269131f9bf66bd ts=2026-10-07T20:00:46.9400000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1229 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[1007] _id=6ac551d8de269131f9b7cae6 ts=2026-10-06T19:53:58.8950000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[1016] _id=6ac551d8de269131f9b7caf4 ts=2026-10-06T19:53:58.8950000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[1014] _id=6ac551d9de269131f9b7cb06 ts=2026-10-06T19:53:59.2870000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[992] _id=6ac551d9de269131f9b7cb0b ts=2026-10-06T19:53:59.2870000Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[1016] _id=6ac551d8de269131f9b7caf4 ts=2026-10-06T19:53:58.8950000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[1018] _id=6ac551d9de269131f9b7cafa ts=2026-10-06T19:53:58.8950000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 2m 
  - Evidence: 144h 2m: 6ab9a9439a8420a1e6b56ba5.jsonl[3725] _id=6ac6a65fde269131f9bf80bb ts=2026-10-07T20:06:55.3850000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6800] _id=6ace8ffdde269131f9d25318 ts=2026-10-13T20:09:33.3060000Z; 24h 4m: 6ab9a9439a8420a1e6b56ba5.jsonl[6903] _id=6acfd7d5de269131f9d8b322 ts=2026-10-14T19:28:20.8620000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[8650] _id=6ad12a6ade269131f9e07ba9 ts=2026-10-15T19:32:58.2140000Z; 23h 55m: 6ab9a9439a8420a1e6b56ba5.jsonl[2352] _id=6ac55406de269131f9b81820 ts=2026-10-06T20:03:17.7650000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[3173] _id=6ac6a469de269131f9bf5dbc ts=2026-10-07T19:58:32.8850000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a9439a8420a1e6b56ba5.jsonl[4203] _id=6ac7f369de269131f9c6d700 ts=2026-10-08T19:47:52.7150000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4848] _id=6ace8753de269131f9d1f8cd ts=2026-10-13T19:32:34.6690000Z; 23h 49m: 6ab9a9439a8420a1e6b56ba5.jsonl[6732] _id=6ace8f94de269131f9d250a2 ts=2026-10-13T20:07:47.7390000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[8297] _id=6acfdeb7de269131f9d93afd ts=2026-10-14T19:57:42.5400000Z; 23h 47m: 6ab9a9439a8420a1e6b56ba5.jsonl[859] _id=6ac5519dde269131f9b7c74e ts=2026-10-06T19:53:00.6890000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2635] _id=6ac6a01ede269131f9bf25bd ts=2026-10-07T19:40:14.0620000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.029s shown 
  - Evidence: 27ms: 6ab9a9439a8420a1e6b56ba5.jsonl[2643] _id=6ac6a024de269131f9bf25f6 ts=2026-10-07T19:40:20.1930000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2647] _id=6ac6a024de269131f9bf25fa ts=2026-10-07T19:40:20.2200000Z; 29ms: 6ab9a9439a8420a1e6b56ba5.jsonl[2642] _id=6ac6a024de269131f9bf25f0 ts=2026-10-07T19:40:20.1640000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2643] _id=6ac6a024de269131f9bf25f6 ts=2026-10-07T19:40:20.1930000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 60h 53m 
  - Evidence: 60h 53m: 6ab9a9439a8420a1e6b56ba5.jsonl[11443] _id=6ad284a9de269131f9e80134 ts=2026-10-16T20:10:17.0890000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11898] _id=6ad5dcffde269131f9e95a6c ts=2026-10-19T09:03:58.8360000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6ab9a9439a8420a1e6b56ba5.jsonl[4704] _id=6ac7f732de269131f9c72908 ts=2026-10-08T20:04:02.0360000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6525] _id=6ace8e83de269131f9d245ad ts=2026-10-13T20:03:14.8920000Z; 73h 39m: 6ab9a9439a8420a1e6b56ba5.jsonl[10788] _id=6ad1d66ede269131f9e33ce4 ts=2026-10-16T07:46:53.9460000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12470] _id=6ad5e252de269131f9e95ec8 ts=2026-10-19T09:26:41.0620000Z; 48h 18m: 6ab9a9439a8420a1e6b56ba5.jsonl[511] _id=6ac54f6ade269131f9b7b141 ts=2026-10-06T19:43:37.2580000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4630] _id=6ac7f6cbde269131f9c71eee ts=2026-10-08T20:02:18.7890000Z
- **INFO / Info** `argumentationAnswerEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10596] _id=6ad1d55ade269131f9e33b8e ts=2026-10-16T07:42:18.2780000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10602] _id=6ad1d55ade269131f9e33b90 ts=2026-10-16T07:42:18.2830000Z; 5ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10606] _id=6ad1d55bde269131f9e33b9a ts=2026-10-16T07:42:19.3240000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10607] _id=6ad1d55bde269131f9e33b9c ts=2026-10-16T07:42:19.3290000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6ab9a9439a8420a1e6b56ba5.jsonl[4708] _id=6ac7f732de269131f9c7290c ts=2026-10-08T20:04:02.0610000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6463] _id=6ace8e60de269131f9d24485 ts=2026-10-13T20:02:40.1240000Z; 73h 38m: 6ab9a9439a8420a1e6b56ba5.jsonl[10792] _id=6ad1d66ede269131f9e33ce9 ts=2026-10-16T07:46:54.0010000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12404] _id=6ad5e216de269131f9e95e4b ts=2026-10-19T09:25:41.2420000Z; 48h 18m: 6ab9a9439a8420a1e6b56ba5.jsonl[514] _id=6ac54f6ade269131f9b7b143 ts=2026-10-06T19:43:37.2880000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4616] _id=6ac7f6bede269131f9c71d41 ts=2026-10-08T20:02:05.5060000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.035s..0.037s shown 
  - Evidence: 35ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10789] _id=6ad1d66ede269131f9e33ce6 ts=2026-10-16T07:46:53.9660000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10792] _id=6ad1d66ede269131f9e33ce9 ts=2026-10-16T07:46:54.0010000Z; 37ms: 6ab9a9439a8420a1e6b56ba5.jsonl[6526] _id=6ace8e83de269131f9d245af ts=2026-10-13T20:03:14.9090000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6529] _id=6ace8e83de269131f9d245b2 ts=2026-10-13T20:03:14.9460000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6ab9a9439a8420a1e6b56ba5.jsonl[4706] _id=6ac7f730de269131f9c728ce ts=2026-10-08T20:03:59.3240000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6510] _id=6ace8e6fde269131f9d24508 ts=2026-10-13T20:02:54.5270000Z; 73h 38m: 6ab9a9439a8420a1e6b56ba5.jsonl[10771] _id=6ad1d66ade269131f9e33ce0 ts=2026-10-16T07:46:49.7770000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12401] _id=6ad5e212de269131f9e95e45 ts=2026-10-19T09:25:36.8410000Z; 48h 18m: 6ab9a9439a8420a1e6b56ba5.jsonl[513] _id=6ac54f67de269131f9b7b135 ts=2026-10-06T19:43:35.1570000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4631] _id=6ac7f6ccde269131f9c71f00 ts=2026-10-08T20:02:19.3830000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 88 interval(s) ≤ 0.000s..0.021s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[12656] _id=6ad5e30dde269131f9e96029 ts=2026-10-19T09:29:48.0960000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12657] _id=6ad5e30dde269131f9e9602a ts=2026-10-19T09:29:48.0960000Z; 19ms: 6ab9a9439a8420a1e6b56ba5.jsonl[12401] _id=6ad5e212de269131f9e95e45 ts=2026-10-19T09:25:36.8410000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12402] _id=6ad5e212de269131f9e95e46 ts=2026-10-19T09:25:36.8600000Z; 21ms: 6ab9a9439a8420a1e6b56ba5.jsonl[10665] _id=6ad1d5b3de269131f9e33c12 ts=2026-10-16T07:43:46.6940000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[10674] _id=6ad1d5b3de269131f9e33c14 ts=2026-10-16T07:43:46.7150000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 133h 26m 
  - Evidence: 133h 26m: 6ab9a9439a8420a1e6b56ba5.jsonl[6509] _id=6ace8e6dde269131f9d244fa ts=2026-10-13T20:02:52.3600000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12626] _id=6ad5e2f0de269131f9e95ff5 ts=2026-10-19T09:29:19.1200000Z; 119h 59m: 6ab9a9439a8420a1e6b56ba5.jsonl[4606] _id=6ac7f711de269131f9c7262d ts=2026-10-08T20:03:28.2790000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6501] _id=6ace8e64de269131f9d244b4 ts=2026-10-13T20:02:44.3200000Z; 48h 18m: 6ab9a9439a8420a1e6b56ba5.jsonl[161] _id=6ac54f57de269131f9b7b0be ts=2026-10-06T19:43:18.8100000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4620] _id=6ac7f6c2de269131f9c71dc1 ts=2026-10-08T20:02:09.4010000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 60h 52m 
  - Evidence: 60h 52m: 6ab9a9439a8420a1e6b56ba5.jsonl[11253] _id=6ad283ecde269131f9e7fba9 ts=2026-10-16T20:07:07.9670000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11515] _id=6ad5dc00de269131f9e957d2 ts=2026-10-19T08:59:43.7240000Z; 4h 11m: 6ab9a9439a8420a1e6b56ba5.jsonl[11138] _id=6ad2490fde269131f9e56a5c ts=2026-10-16T15:55:58.8410000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11253] _id=6ad283ecde269131f9e7fba9 ts=2026-10-16T20:07:07.9670000Z; 18m 10s: 6ab9a9439a8420a1e6b56ba5.jsonl[11515] _id=6ad5dc00de269131f9e957d2 ts=2026-10-19T08:59:43.7240000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12247] _id=6ad5e043de269131f9e95d1b ts=2026-10-19T09:17:54.4500000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9439a8420a1e6b56ba5.jsonl[4798] _id=6ac7f894de269131f9c74423 ts=2026-10-08T20:09:55.9310000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4802] _id=6ace86c0de269131f9d1f1c9 ts=2026-10-13T19:30:07.4880000Z; 60h 52m: 6ab9a9439a8420a1e6b56ba5.jsonl[11252] _id=6ad283e6de269131f9e7fb93 ts=2026-10-16T20:07:02.1080000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11509] _id=6ad5dbf8de269131f9e957d0 ts=2026-10-19T08:59:35.3140000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba5.jsonl[2422] _id=6ac554a2de269131f9b82fcf ts=2026-10-06T20:05:53.1590000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2555] _id=6ac69f31de269131f9bf21e3 ts=2026-10-07T19:36:17.2250000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9439a8420a1e6b56ba5.jsonl[4797] _id=6ac7f894de269131f9c74422 ts=2026-10-08T20:09:55.9310000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4801] _id=6ace86c0de269131f9d1f1c8 ts=2026-10-13T19:30:07.4870000Z; 60h 52m: 6ab9a9439a8420a1e6b56ba5.jsonl[11251] _id=6ad283e6de269131f9e7fb92 ts=2026-10-16T20:07:02.1080000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11508] _id=6ad5dbf8de269131f9e957cf ts=2026-10-19T08:59:35.3140000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba5.jsonl[2421] _id=6ac554a2de269131f9b82fce ts=2026-10-06T20:05:53.1590000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2554] _id=6ac69f31de269131f9bf21e2 ts=2026-10-07T19:36:17.2250000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 11m 
  - Evidence: 120h 11m: 6ab9a9439a8420a1e6b56ba5.jsonl[4082] _id=6ac7f20bde269131f9c6bcf9 ts=2026-10-08T19:42:02.1880000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[6081] _id=6ace8c38de269131f9d231fc ts=2026-10-13T19:53:27.9380000Z; 48h 1m: 6ab9a9439a8420a1e6b56ba5.jsonl[8471] _id=6acfe051de269131f9d951de ts=2026-10-14T20:04:30.3330000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11248] _id=6ad28394de269131f9e7fa92 ts=2026-10-16T20:05:39.7840000Z; 23h 48m: 6ab9a9439a8420a1e6b56ba5.jsonl[715] _id=6ac55109de269131f9b7bdbc ts=2026-10-06T19:50:32.8210000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2610] _id=6ac69fcdde269131f9bf23aa ts=2026-10-07T19:38:52.8600000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[11248] _id=6ad28394de269131f9e7fa92 ts=2026-10-16T20:05:39.7840000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11249] _id=6ad283e6de269131f9e7fb8f ts=2026-10-16T20:05:39.784Z; 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[7646] _id=6acfdb0ede269131f9d9023d ts=2026-10-14T19:42:05.4190000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[7647] _id=6acfdb19de269131f9d902e4 ts=2026-10-14T19:42:05.419Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 24m 
  - Evidence: 119h 24m: 6ab9a9439a8420a1e6b56ba5.jsonl[4788] _id=6ac7f836de269131f9c73e9f ts=2026-10-08T20:08:21.7230000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[4843] _id=6ace874ade269131f9d1f878 ts=2026-10-13T19:32:25.6420000Z; 60h 52m: 6ab9a9439a8420a1e6b56ba5.jsonl[11258] _id=6ad283efde269131f9e7fbb8 ts=2026-10-16T20:07:10.5530000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[11512] _id=6ad5dc03de269131f9e957d6 ts=2026-10-19T08:59:46.3720000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba5.jsonl[2427] _id=6ac554b0de269131f9b8311b ts=2026-10-06T20:06:06.8940000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[2568] _id=6ac69f45de269131f9bf221e ts=2026-10-07T19:36:35.9980000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba5.jsonl[12724] _id=6ad5e367de269131f9e960a2 ts=2026-10-19T09:31:18.3270000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[12725] _id=6ad5e367de269131f9e960a3 ts=2026-10-19T09:31:18.3270000Z; 1ms: 6ab9a9439a8420a1e6b56ba5.jsonl[493] _id=6ac54ecfde269131f9b7ac5c ts=2026-10-06T19:41:02.9070000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[494] _id=6ac54ecfde269131f9b7ac5d ts=2026-10-06T19:41:02.9080000Z; 1ms: 6ab9a9439a8420a1e6b56ba5.jsonl[9483] _id=6ad12e70de269131f9e0c97c ts=2026-10-15T19:50:07.4580000Z -> 6ab9a9439a8420a1e6b56ba5.jsonl[9484] _id=6ad12e70de269131f9e0c97d ts=2026-10-15T19:50:07.4590000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[559] _id=6ac54f7bde269131f9b7b19f ts=2026-10-06T19:43:54.3290000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[2773] _id=6ac6a17ede269131f9bf3bff ts=2026-10-07T19:46:06.0400000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[3732] _id=6ac6a670de269131f9bf822a ts=2026-10-07T20:07:12.4390000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[6529] _id=6ace8e83de269131f9d245b2 ts=2026-10-13T20:03:14.9460000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[10266] _id=6ad132d5de269131f9e11af1 ts=2026-10-15T20:08:52.6520000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[10792] _id=6ad1d66ede269131f9e33ce9 ts=2026-10-16T07:46:54.0010000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[11138] _id=6ad2490fde269131f9e56a5c ts=2026-10-16T15:55:58.8410000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[11253] _id=6ad283ecde269131f9e7fba9 ts=2026-10-16T20:07:07.9670000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[11515] _id=6ad5dc00de269131f9e957d2 ts=2026-10-19T08:59:43.7240000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[6921] _id=6acfd7f6de269131f9d8b5ba ts=2026-10-14T19:28:53.4610000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[2348] _id=6ac554b0de269131f9b83112 ts=?`; `6ab9a9439a8420a1e6b56ba5.jsonl[4061] _id=6ac7f207de269131f9c6bc77 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 80 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[3385] _id=6ac6a583de269131f9bf7147 ts=2026-10-07T20:03:12.2540000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[3430] _id=6ac6a595de269131f9bf7218 ts=2026-10-07T20:03:31.5300000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[3432] _id=6ac6a595de269131f9bf721e ts=2026-10-07T20:03:32.6790000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 72 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[777] _id=6ac5516bde269131f9b7c44f ts=2026-10-06T19:52:09.8840000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[783] _id=6ac5516bde269131f9b7c457 ts=2026-10-06T19:52:09.8840000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[788] _id=6ac5516bde269131f9b7c462 ts=2026-10-06T19:52:09.8840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 15 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[160] _id=6ac54f56de269131f9b7b0b5 ts=2026-10-06T19:43:17.3720000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[4622] _id=6ac7f6c4de269131f9c71e05 ts=2026-10-08T20:02:11.3610000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[4623] _id=6ac7f6c5de269131f9c71e1d ts=2026-10-08T20:02:12.1930000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 gameWindowFocusEvent record in 'Unit 3 Dungeon Dev' inside a 'Transition' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[7582] _id=6acfdb0ade269131f9d901cf ts=2026-10-14T19:42:00.8500000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 471 start, 463 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'BecameCameraCentered' (totals: 535 open, 529 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 897 open, 885 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 20 unmatched 'argumentationToolOpen' (totals: 23 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 51 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 292 of 12975 adjacent _id pairs reverse in client time; worst 130.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56ba5.jsonl[927] _id=6ac551cdde269131f9b7c9f1 ts=2026-10-06T19:53:48.9560000Z`; `6ab9a9439a8420a1e6b56ba5.jsonl[939] _id=6ac551cede269131f9b7c9fb ts=2026-10-06T19:51:38.3390000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.85s, min -83673.50s, max -0.25s over 12976 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9439a8420a1e6b56ba5\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4429 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1448); Unit 2 Prod (Refactor) (1029); Unit 3 Dungeon Dev (608); Unit 4 Dev - Dungeon (489); Unit 5 Dev - Dungeon (204); Unit 4 Dev (197); Unit 1 Dev (196); Unit 4 Dev - Anderson Base (161); Unit 5 Dev (97)
- **Intervals:** median 0.84s (p5 0.07s / p95 13.11s, n=4428)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4429/4429 records)
    "pressed"  x4429
data.actionType  (string, 4429/4429 records)
    "Move"  x2519
    "Jump"  x747
    "Interact"  x679
    "Ascend"  x193
    "Sprint"  x111
    "Hoverboard"  x89
    "Map"  x63
    "Pause"  x12
    "Descend"  x9
    "SkipCinematic"  x7
data.key  (string, 4429/4429 records, 28 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4429/4429 records)
    "Player"  x3063
    "Drone"  x1366
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2846 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1728); Unit 5 Dev - Dungeon (572); Unit 4 Dev (282); Unit 3 Dungeon Dev (264)
- **Intervals:** median 0.07s (p5 0.00s / p95 1.86s, n=2845)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2846/2846 records)
    "BecameVisible"  x897
    "BecameInvisible"  x885
    "BecameCameraCentered"  x535
    "BecameCameraUncentered"  x529
data.pieceId  (string, 2846/2846 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2846/2846 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2406 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (575); Unit 3 Dev (503); Unit 4 Dev (275); Unit 5 Dev (246); Unit 1 Dev (209); Unit 3 Dungeon Dev (202); Unit 4 Dev - Anderson Base (198); Unit 4 Dev - Dungeon (104); Unit 5 Dev - Dungeon (94)
- **eventKey:** present on 1472 of 2406 records
- **Intervals:** median 3.50s (p5 0.00s / p95 27.18s, n=2405)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1472; [conversationId, dialogueEventType] x934
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2406/2406 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2406/2406 records)
    "DialogueNodeEvent"  x1472
    "DialogueStartEvent"  x471
    "DialogueFinishEvent"  x463
data.nodeId  (number, 1472/2406 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1853 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (486); Unit 3 Dev (313); Unit 4 Dev (179); Unit 1 Dev (163); Unit 3 Dungeon Dev (158); Unit 5 Dev - Dungeon (157); Unit 5 Dev (151); Unit 4 Dev - Anderson Base (126); Unit 4 Dev - Dungeon (120)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.30s, n=1839)
- **Fields under `data`:**

```text
data.position  (object, 1853/1853 records)
data.position.x  (number, 1853/1853 records)
    numeric range -679.6 .. 1557.13 (672 unique)
data.position.y  (number, 1853/1853 records)
    numeric range -114.326 .. 222.004 (518 unique)
data.position.z  (number, 1853/1853 records)
    numeric range -1046.17 .. 1893.9 (671 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 522 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (224); Unit 5 Dev (192); Unit 2 Prod (Refactor) (63); Unit 1 Dev (30); Unit 3 Dev (13)
- **Intervals:** median 0.45s (p5 0.03s / p95 11.45s, n=521)
- **Fields under `data`:**

```text
data.actionType  (string, 522/522 records)
    "argumentationNodeHoverEnd"  x212
    "argumentationNodeHoverStart"  x212
    "argumentationNodeAdd"  x62
    "argumentationNodeRemove"  x36
data.argumentationTitle  (string, 522/522 records)
    "Unit 4 - Flooding"  x224
    "Unit 5"  x192
    "Unit 2 – Watershed"  x63
    "Unit 1 - Argumentation Tutorial"  x15
    "Unit 1 - Freshwater"  x15
    "Unit 3 - Pollution Upstream"  x13
data.nodeName  (string, 522/522 records)
    "C"  x65
    "A"  x64
    "4"  x58
    "B"  x58
    "II"  x58
    "I"  x51
    "D"  x49
    "2"  x46
    "1"  x37
    "3"  x33
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 318 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (85); Unit 2 Prod (Refactor) (73); Unit 3 Dungeon Dev (67); Unit 5 Dev - Dungeon (21); Unit 4 Dev - Anderson Base (18); Unit 4 Dev (17); Unit 1 Dev (13); Unit 3 Dev (13); Unit 5 Dev (11)
- **Intervals:** median 8.35s (p5 0.19s / p95 323.41s, n=317)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 318/318 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 318/318 records)
    112 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 122 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (72); Unit 3 Dev (50)
- **Intervals:** median 2.64s (p5 0.75s / p95 306.95s, n=121)
- **`data` key-set variants:** [actionType, featureUsed, location] x64; [actionType, featureUsed] x58
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 122/122 records)
    "WaypointMoveEvent"  x56
    "MapCloseEvent"  x29
    "MapOpenEvent"  x29
    "WaypointSetEvent"  x6
    "WaypointResetEvent"  x2
data.featureUsed  (string, 122/122 records)
    "Waypoint"  x64
    "Map"  x58
data.location  (object, 64/122 records)
data.location.x  (number, 64/122 records)
    numeric range -369.39 .. 439.927 (60 unique)
data.location.y  (number, 64/122 records)
    numeric range -292.859 .. 231.766 (57 unique)
data.location.z  (number, 64/122 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 86 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (15); Unit 3 Dev (15); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 86 of 86 records
- **Intervals:** median 188.15s (p5 0.01s / p95 84184.43s, n=85)
- **`data` key-set variants:** [questEventType, questID, questName] x51; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 86/86 records)
    "questActiveEvent"  x51
    "questFinishEvent"  x35
data.questID  (string, 86/86 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 86/86 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/86 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 68 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (22); Unit 4 Dev (12)
- **Intervals:** median 1.93s (p5 0.36s / p95 58795.94s, n=67)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x58; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/68 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/68 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x4
    "Unit 4 Dev"  x2
data.actionType  (string, 58/68 records)
    "RightDrag"  x34
    "LeftDrag"  x24
data.currentSoilType  (string, 58/68 records)
    "CLAY"  x13
    "CLAYSAND"  x12
    "SAND"  x11
    "CLAYROCK"  x10
    "SANDGRAVEL"  x6
    "BEDROCK"  x4
    "GRAVEL"  x2
data.isCorrectSelection  (string, 58/68 records)
    "false"  x43
    "true"  x15
data.waterLevelStatus  (string, 58/68 records)
    "TooHigh"  x29
    "Proper"  x18
    "TooLow"  x11
data.waterRetentionChange  (string, 58/68 records)
    "Increase"  x25
    "Decrease"  x18
    "NoChange"  x15
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 56 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (36); Unit 5 Dev (8); Unit 2 Prod (Refactor) (7); Unit 1 Dev (4); Unit 3 Dev (1)
- **Intervals:** median 7.83s (p5 0.12s / p95 173311.87s, n=55)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 56/56 records)
    "submitAnswerEvent"  x56
data.answerSubmitted  (string, 56/56 records, 2 empty-string)
    26 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 56/56 records)
    "Unit 4 - Flooding"  x36
    "Unit 5"  x8
    "Unit 2 – Watershed"  x7
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 43 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (19); Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 4 Dev (4); Unit 5 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 459.19s (p5 8.15s / p95 84614.86s, n=42)
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "DebugMenuStateChanged"  x43
data.isOpened  (bool, 43/43 records)
    false  x43
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 39 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (21); Transition (4); Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 3 Dungeon Dev (4); Unit 1 Dev (2)
- **Intervals:** median 224.11s (p5 4.90s / p95 104803.44s, n=38)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 39/39 records)
    true  x39
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `WaterChamberEvent` — 37 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (37)
- **Intervals:** median 12.41s (p5 0.19s / p95 78.54s, n=36)
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "On"  x24
    "Off"  x13
data.floor  (string, 37/37 records)
    "3"  x15
    "2"  x11
    "4"  x7
    "1"  x4
data.machineNumber  (string, 37/37 records)
    "One"  x36
    "Two"  x1
data.machineType  (string, 37/37 records)
    "Condenser"  x15
    "Evaporator"  x13
    "DualChamber_Condenser"  x4
    "DualChamber_Evaporator"  x3
    "VentSwitch"  x2
data.room  (string, 37/37 records)
    "2"  x17
    "3"  x13
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 26 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 5 Dev (6); Unit 1 Dev (5); Unit 3 Dev (4)
- **Intervals:** median 1.44s (p5 0.65s / p95 380350.95s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "argumentationToolOpen"  x23
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 26/26 records)
    "Unit 2 – Watershed"  x11
    "Unit 5"  x6
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 26/26 records)
    "BackingInfoPanel - Watershed Graph"  x8
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Evaporation Flow Diagram"  x3
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Waterfall Data"  x3
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 25 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Transition (8); Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 3 Dungeon Dev (4); Unit 1 Dev (2); MainMenu (1)
- **Intervals:** median 31.54s (p5 0.68s / p95 159794.04s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 14967.26s (p5 95.40s / p95 240199.04s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 18 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (18)
- **Intervals:** median 0.17s (p5 0.05s / p95 4.08s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "Close"  x9
    "Open"  x9
data.toolName  (string, 18/18 records, 18 empty-string)
    ""  x18
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 123.20s (p5 0.04s / p95 306824.95s, n=16)
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

### `TerasGardenBox` — 16 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (16)
- **Intervals:** median 1.35s (p5 0.14s / p95 16.74s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records, 12 empty-string)
    ""  x12
    "cameraPlaced"  x4
data.boxId  (string, 16/16 records)
    "0"  x11
    "1"  x3
    "2"  x2
data.soilType  (string, 16/16 records)
    "Sand"  x12
    "Gravel"  x3
    "Clay"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 13 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (13)
- **Intervals:** median 12.82s (p5 2.27s / p95 116.36s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "ChangeCanister"  x13
data.canisterType  (string, 13/13 records)
    "Clay"  x5
    "Bedrock"  x3
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 13/13 records)
    "5"  x9
    "4"  x4
data.machine  (string, 13/13 records)
    "1"  x12
    "2"  x1
data.row  (string, 13/13 records)
    "TopRow"  x9
    "BottomRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `SolarStillDesignEvent` — 7 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (7)
- **Intervals:** median 1.63s (p5 1.00s / p95 2.01s, n=6)
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
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/7 records)
    "Flat"  x1
data.featureUsed  (string, 7/7 records)
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x2
    "RoofStyle"  x2
    "Submit"  x1
data.selectedOption  (string, 6/7 records)
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 219659.76s (p5 136044.65s / p95 480386.47s, n=4)
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
- **Intervals:** median 15069.13s (p5 2488.57s / p95 198747.09s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time."  x1
    "Permissions check failed"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records)
    "NotAllowedError: Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time.
    at requestPointerLock (blob:https://mhs.adroit.games/f82b16b1-1187-48f2-8735-5217c0d2bf69:9:213829)
    at Object.runDeferredCalls (blob:https://mhs.adroit.games/f82b16b1-1187-48f2-8735-5217c0d2bf69:9:204819)
    at HTMLCanvasElement.jsEventHandler (blob:https://mhs.adroit.games/f82b16b1-1187-48f2-8735-5217c0d2bf69:9:205513)"  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x2
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (34 records)
- `TerasGardenBox` data.actionType: "" (12x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (56x); "WaypointResetEvent" (2x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (64x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (36x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*