# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1fd

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1fd
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1fd.jsonl
- **Records:** 12964 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1fd
- **Time span:** 2026-09-23T13:04:05.860000+00:00 .. 2026-10-05T13:38:12.500000+00:00 (288h 34m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1fd\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 12964 records, 11 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 109 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `soilMachine`: median interval between records changed substantially
  - WARNING/Medium `DialogueEvent`: eventKey does not match its documented format
  - WARNING/Medium `questEvent`: eventKey does not match its documented format

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3522 | 27.17 | 1 | 4 | 0 | 2026-09-24T12:56:42.765000+00:00 | 2026-10-05T13:01:05.075000+00:00 | 264h 4m |
| InputEvent | 3303 | 25.48 | 1 | 9 | 0 | 2026-09-23T13:12:48.376000+00:00 | 2026-10-05T13:38:12.500000+00:00 | 288h 25m |
| DialogueEvent | 2262 | 17.45 | 1 | 9 | 1445 | 2026-09-23T13:06:28.565000+00:00 | 2026-10-05T13:38:08.068000+00:00 | 288h 31m |
| PlayerPositionEvent | 1883 | 14.52 | 1 | 9 | 0 | 2026-09-23T13:06:06.046000+00:00 | 2026-10-05T13:38:08.793000+00:00 | 288h 32m |
| argumentationNodeEvent | 1087 | 8.38 | 1 | 5 | 0 | 2026-09-23T13:32:22.909000+00:00 | 2026-10-05T13:21:11.001000+00:00 | 287h 48m |
| ObjectInterEvent | 288 | 2.22 | 1 | 9 | 0 | 2026-09-23T13:13:47.226000+00:00 | 2026-10-05T13:38:12.499000+00:00 | 288h 24m |
| TopographicMapEvent | 99 | 0.76 | 1 | 3 | 0 | 2026-09-24T12:57:09.891000+00:00 | 2026-09-29T13:37:47.498000+00:00 | 120h 40m |
| questEvent | 82 | 0.63 | 1 | 9 | 82 | 2026-09-23T13:06:28.544000+00:00 | 2026-10-05T13:34:29.387000+00:00 | 288h 28m |
| gameWindowFocusEvent | 65 | 0.5 | 1 | 9 | 0 | 2026-09-23T13:04:05.860000+00:00 | 2026-10-05T13:31:19.583000+00:00 | 288h 27m |
| Soil Key Puzzle | 64 | 0.49 | 1 | 3 | 0 | 2026-09-24T13:03:35.134000+00:00 | 2026-09-30T13:01:40.379000+00:00 | 143h 58m |
| argumentationAnswerEvent | 64 | 0.49 | 1 | 5 | 0 | 2026-09-23T13:33:21.272000+00:00 | 2026-10-05T13:21:11.759000+00:00 | 287h 47m |
| gameWindowUnfocusEvent | 48 | 0.37 | 1 | 8 | 0 | 2026-09-23T13:06:36.934000+00:00 | 2026-10-05T13:31:16.776000+00:00 | 288h 24m |
| WaterChamberEvent | 41 | 0.32 | 1 | 1 | 0 | 2026-10-01T13:32:12.845000+00:00 | 2026-10-05T13:04:31.491000+00:00 | 95h 32m |
| soilMachine | 32 | 0.25 | 1 | 1 | 0 | 2026-09-30T13:17:21.770000+00:00 | 2026-09-30T13:27:50.089000+00:00 | 10m 28s |
| DEBUGMenu | 24 | 0.19 | 1 | 8 | 0 | 2026-09-23T13:06:06.039000+00:00 | 2026-10-05T12:57:21.749000+00:00 | 287h 51m |
| DaniEvent | 18 | 0.14 | 1 | 4 | 0 | 2026-09-24T13:22:15.453000+00:00 | 2026-10-01T13:17:34.670000+00:00 | 167h 55m |
| SolarStillDesignEvent | 18 | 0.14 | 1 | 1 | 0 | 2026-10-05T13:31:26.230000+00:00 | 2026-10-05T13:32:01.992000+00:00 | 35.8s |
| gameStartEvent | 18 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:04:05.861000+00:00 | 2026-10-05T12:57:07.934000+00:00 | 287h 53m |
| argumentationEvent | 17 | 0.13 | 1 | 5 | 0 | 2026-09-23T13:32:38.463000+00:00 | 2026-10-05T13:21:11.785000+00:00 | 287h 48m |
| TerasGardenBox | 9 | 0.07 | 1 | 1 | 0 | 2026-10-01T13:13:16.892000+00:00 | 2026-10-01T13:14:32.998000+00:00 | 1m 16s |
| argumentationToolEvent | 8 | 0.06 | 1 | 2 | 0 | 2026-09-23T13:32:33.348000+00:00 | 2026-09-28T13:38:22.879000+00:00 | 120h 5m |
| chatEvent | 5 | 0.04 | 1 | 3 | 0 | 2026-09-29T13:06:07.726000+00:00 | 2026-10-05T13:06:28.703000+00:00 | 144h 0m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-23T13:37:28.169000+00:00 | 2026-10-05T13:38:12.490000+00:00 | 288h 0m |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 346274.921s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.218s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.456s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.064s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.568s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 87315.029s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.642s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 18 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; p; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.5x vs baseline. 
  - Observed: 18 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 210 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 12.8x vs baseline. 
  - Observed: 64 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 2,II; A,1,; A,2,II; A,3,I; B,1,I; B,1,II; B,2,II; B,3,I; B,3,II; B,4,II; C,2,II; C,A,2,II; D,1,II; D,2,II; D,C,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 7.8x vs baseline. 
  - Observed: 1087 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 6.4x vs baseline. 
  - Observed: 32 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 52 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[172] _id=6ab3d0f4485cab4c954badf6 ts=2026-09-23T13:15:32.2660000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[233] _id=6ab3d1d9485cab4c954bdbaa ts=2026-09-23T13:19:21.1120000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[299] _id=6ab3d28e485cab4c954bf370 ts=2026-09-23T13:22:22.0470000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[3784] _id=6ab670e9485cab4c95545b29 ts=2026-09-25T13:02:32.4150000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[12193] _id=6ac39fa6de269131f9a84302 ts=2026-10-05T13:01:26.3740000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[2] _id=6ab3ce45485cab4c954b8492 ts=2026-09-23T13:04:05.8610000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[758] _id=6ab3d68a485cab4c954ca805 ts=2026-09-23T13:39:22.2990000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[778] _id=6ab51d28485cab4c954fbd59 ts=2026-09-24T12:52:56.3900000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 65 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 65} 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[3] _id=6ab3ce45485cab4c954b8490 ts=2026-09-23T13:04:05.8600000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[15] _id=6ab3cedd485cab4c954b85d4 ts=2026-09-23T13:06:36.9470000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[6] _id=6ab3cee8485cab4c954b85f2 ts=2026-09-23T13:06:48.7220000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 48 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 48} 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[4] _id=6ab3cedc485cab4c954b85d2 ts=2026-09-23T13:06:36.9340000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[5] _id=6ab3cedd485cab4c954b85d6 ts=2026-09-23T13:06:37.6420000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[199] _id=6ab3d16b485cab4c954bc856 ts=2026-09-23T13:17:31.7720000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 99 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[910] _id=6ab51e25485cab4c954fd4f9 ts=2026-09-24T12:57:09.8910000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[925] _id=6ab51e4b485cab4c954fd9ef ts=2026-09-24T12:57:47.9410000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[922] _id=6ab51e4d485cab4c954fda2b ts=2026-09-24T12:57:49.6220000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3521 | 0.0 | 0.025 | 269.998 | 0.945 | 345713.173 | 0.22 | 2274 | 8 |
| InputEvent | 3302 | 0.001 | 0.798 | 314.453 | 17.375 | 343079.794 | 0.19 | 191 | 9 |
| DialogueEvent | 2261 | 0.0 | 3.627 | 459.398 | 34.026 | 342983.132 | 0.13 | 638 | 8 |
| PlayerPositionEvent | 1869 | 9.794 | 10.0 | 510.654 | 10.091 | 342971.816 | 0.12 | 0 | 7 |
| argumentationNodeEvent | 1086 | 0.001 | 0.359 | 954.077 | 7.751 | 346441.412 | 0.06 | 248 | 6 |
| ObjectInterEvent | 287 | 0.001 | 5.849 | 3617.649 | 362.309 | 343343.512 | 0.02 | 6 | 11 |
| TopographicMapEvent | 98 | 0.038 | 4.218 | 4433.037 | 589.391 | 259012.765 | 0.01 | 2 | 5 |
| questEvent | 81 | 0.001 | 213.152 | 12820.751 | 84152.491 | 343258.291 | 0.0 | 16 | 16 |
| gameWindowFocusEvent | 64 | 3.142 | 152.163 | 16225.527 | 84194.497 | 342954.502 | 0.0 | 0 | 21 |
| Soil Key Puzzle | 63 | 0.105 | 1.002 | 8226.75 | 1056.836 | 431036.779 | 0.01 | 0 | 4 |
| argumentationAnswerEvent | 63 | 0.131 | 15.064 | 16445.563 | 162875.341 | 346473.022 | 0.0 | 0 | 5 |
| gameWindowUnfocusEvent | 47 | 0.708 | 190.688 | 22091.06 | 85575.352 | 344065.255 | 0.0 | 0 | 17 |
| WaterChamberEvent | 40 | 0.177 | 4.456 | 8598.466 | 137.686 | 343109.096 | 0.01 | 0 | 1 |
| soilMachine | 31 | 0.355 | 2.642 | 20.268 | 137.117 | 232.741 | 2.96 | 0 | 0 |
| DEBUGMenu | 23 | 112.105 | 1140.936 | 45055.466 | 241788.11 | 343788.402 | 0.0 | 0 | 15 |
| DaniEvent | 17 | 0.823 | 7.734 | 35559.954 | 139052.234 | 345099.63 | 0.0 | 0 | 5 |
| SolarStillDesignEvent | 17 | 0.805 | 2.189 | 2.104 | 4.181 | 4.811 | 28.52 | 0 | 0 |
| gameStartEvent | 17 | 54.161 | 2116.438 | 60963.651 | 275950.552 | 343786.298 | 0.0 | 0 | 12 |
| argumentationEvent | 16 | 0.028 | 97.648 | 64757.083 | 280949.4 | 346434.575 | 0.0 | 3 | 5 |
| TerasGardenBox | 8 | 1.115 | 5.856 | 9.513 | 22.641 | 24.866 | 6.31 | 0 | 0 |
| argumentationToolEvent | 7 | 0.222 | 2.568 | 61764.219 | 302596.838 | 432236.976 | 0.0 | 0 | 1 |
| chatEvent | 4 | 2.469 | 87315.029 | 129605.244 | 318332.639 | 343788.451 | 0.0 | 0 | 2 |
| EndOfUnit | 3 | 172401.112 | 346274.921 | 345614.774 | 500978.951 | 518168.288 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 277 group(s), 454 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[954] _id=6ab51e6c485cab4c954fde5d ts=2026-09-24T12:58:20.5360000Z == 6aa413b141b41dbac0c7f1fd.jsonl[953] _id=6ab51e6c485cab4c954fde65 ts=2026-09-24T12:58:20.5360000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[947] _id=6ab51e6e485cab4c954fde89 ts=2026-09-24T12:58:20.7250000Z == 6aa413b141b41dbac0c7f1fd.jsonl[948] _id=6ab51e6e485cab4c954fde8d ts=2026-09-24T12:58:20.7250000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[957] _id=6ab51e6e485cab4c954fde9f ts=2026-09-24T12:58:20.8060000Z == 6aa413b141b41dbac0c7f1fd.jsonl[958] _id=6ab51e6e485cab4c954fdea5 ts=2026-09-24T12:58:20.8060000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 30 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa413b141b41dbac0c7f1fd.jsonl[127] _id=6ab3d08b485cab4c954b9a94 ts=2026-09-23T13:13:47.2260000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[131] _id=6ab3d08b485cab4c954b9a96 ts=2026-09-23T13:13:47.2300000Z`; `287ms: 6aa413b141b41dbac0c7f1fd.jsonl[315] _id=6ab3d2a4485cab4c954bf5cb ts=2026-09-23T13:22:44.6120000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[313] _id=6ab3d2a4485cab4c954bf5e4 ts=2026-09-23T13:22:44.8990000Z`; `189ms: 6aa413b141b41dbac0c7f1fd.jsonl[313] _id=6ab3d2a4485cab4c954bf5e4 ts=2026-09-23T13:22:44.8990000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[318] _id=6ab3d2a5485cab4c954bf5ea ts=2026-09-23T13:22:45.0880000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 708 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `25ms: 6aa413b141b41dbac0c7f1fd.jsonl[967] _id=6ab51e6e485cab4c954fdea7 ts=2026-09-24T12:58:20.8060000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[949] _id=6ab51e6e485cab4c954fdeab ts=2026-09-24T12:58:20.8310000Z`; `12ms: 6aa413b141b41dbac0c7f1fd.jsonl[949] _id=6ab51e6e485cab4c954fdeab ts=2026-09-24T12:58:20.8310000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[959] _id=6ab51e6f485cab4c954fdead ts=2026-09-24T12:58:20.8430000Z`; `117ms: 6aa413b141b41dbac0c7f1fd.jsonl[959] _id=6ab51e6f485cab4c954fdead ts=2026-09-24T12:58:20.8430000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[968] _id=6ab51e6f485cab4c954fdeb3 ts=2026-09-24T12:58:20.9600000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `180ms: 6aa413b141b41dbac0c7f1fd.jsonl[924] _id=6ab51e4e485cab4c954fda4b ts=2026-09-24T12:57:50.5800000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[928] _id=6ab51e4e485cab4c954fda53 ts=2026-09-24T12:57:50.7600000Z`; `110ms: 6aa413b141b41dbac0c7f1fd.jsonl[928] _id=6ab51e4e485cab4c954fda53 ts=2026-09-24T12:57:50.7600000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[929] _id=6ab51e4e485cab4c954fda57 ts=2026-09-24T12:57:50.8700000Z`; `42ms: 6aa413b141b41dbac0c7f1fd.jsonl[2467] _id=6ab52194485cab4c95502827 ts=2026-09-24T13:11:48.1700000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[2469] _id=6ab52194485cab4c95502839 ts=2026-09-24T13:11:48.2120000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `808ms: 6aa413b141b41dbac0c7f1fd.jsonl[12079] _id=6ac39f5bde269131f9a84048 ts=2026-10-05T13:00:11.0900000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[12081] _id=6ac39f5bde269131f9a84050 ts=2026-10-05T13:00:11.8980000Z`; `517ms: 6aa413b141b41dbac0c7f1fd.jsonl[12083] _id=6ac39f5ede269131f9a8406a ts=2026-10-05T13:00:14.3610000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[12099] _id=6ac39f5ede269131f9a8407a ts=2026-10-05T13:00:14.8780000Z`; `399ms: 6aa413b141b41dbac0c7f1fd.jsonl[12085] _id=6ac39f5ede269131f9a84074 ts=2026-10-05T13:00:14.6560000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[12100] _id=6ac39f5fde269131f9a84080 ts=2026-10-05T13:00:15.0550000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `489ms: 6aa413b141b41dbac0c7f1fd.jsonl[6195] _id=6aba6dd0485cab4c956811fd ts=2026-09-28T13:38:24.3340000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[6197] _id=6aba6dd0485cab4c95681205 ts=2026-09-28T13:38:24.8230000Z`; `146ms: 6aa413b141b41dbac0c7f1fd.jsonl[6197] _id=6aba6dd0485cab4c95681205 ts=2026-09-28T13:38:24.8230000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[6178] _id=6aba6dd0485cab4c95681207 ts=2026-09-28T13:38:24.9690000Z`; `186ms: 6aa413b141b41dbac0c7f1fd.jsonl[6225] _id=6aba6de2485cab4c95681333 ts=2026-09-28T13:38:42.5580000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[6226] _id=6aba6de2485cab4c95681337 ts=2026-09-28T13:38:42.7440000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa413b141b41dbac0c7f1fd.jsonl[6010] _id=6aba6cb1485cab4c956806e1 ts=2026-09-28T13:33:37.1900000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[5997] _id=6aba6cb1485cab4c956806e7 ts=2026-09-28T13:33:37.2180000Z`; `37ms: 6aa413b141b41dbac0c7f1fd.jsonl[6143] _id=6aba6dbd485cab4c95681125 ts=2026-09-28T13:38:05.6800000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[6170] _id=6aba6dbe485cab4c9568112b ts=2026-09-28T13:38:05.7170000Z`; `29ms: 6aa413b141b41dbac0c7f1fd.jsonl[10962] _id=6abe5ade485cab4c95a43813 ts=2026-10-01T13:06:38.7560000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[10966] _id=6abe5adf485cab4c95a4381f ts=2026-10-01T13:06:38.7850000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 185 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `18ms: 6aa413b141b41dbac0c7f1fd.jsonl[577] _id=6ab3d50a485cab4c954c6f31 ts=2026-09-23T13:32:58.9770000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[575] _id=6ab3d50b485cab4c954c6f37 ts=2026-09-23T13:32:58.9950000Z`; `977ms: 6aa413b141b41dbac0c7f1fd.jsonl[574] _id=6ab3d50a485cab4c954c6f21 ts=2026-09-23T13:32:58.5650000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[576] _id=6ab3d50b485cab4c954c6f55 ts=2026-09-23T13:32:59.5420000Z`; `940ms: 6aa413b141b41dbac0c7f1fd.jsonl[575] _id=6ab3d50b485cab4c954c6f37 ts=2026-09-23T13:32:58.9950000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[573] _id=6ab3d50b485cab4c954c6f71 ts=2026-09-23T13:32:59.9350000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `365ms: 6aa413b141b41dbac0c7f1fd.jsonl[619] _id=6ab3d55d485cab4c954c7fdd ts=2026-09-23T13:34:21.5890000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[615] _id=6ab3d55d485cab4c954c7fe3 ts=2026-09-23T13:34:21.9540000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `708ms: 6aa413b141b41dbac0c7f1fd.jsonl[4] _id=6ab3cedc485cab4c954b85d2 ts=2026-09-23T13:06:36.9340000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[5] _id=6ab3cedd485cab4c954b85d6 ts=2026-09-23T13:06:37.6420000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa413b141b41dbac0c7f1fd.jsonl[3784] _id=6ab670e9485cab4c95545b29 ts=2026-09-25T13:02:32.4150000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[3785] _id=6ab670e9485cab4c95545b2d ts=2026-09-25T13:02:32.4180000Z`; `25ms: 6aa413b141b41dbac0c7f1fd.jsonl[12193] _id=6ac39fa6de269131f9a84302 ts=2026-10-05T13:01:26.3740000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[12189] _id=6ac39fa6de269131f9a84304 ts=2026-10-05T13:01:26.3990000Z`; `1ms: 6aa413b141b41dbac0c7f1fd.jsonl[12620] _id=6ac3a48bde269131f9a8bf88 ts=2026-10-05T13:22:19.8860000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[12640] _id=6ac3a48cde269131f9a8bf8b ts=2026-10-05T13:22:19.8870000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `557ms: 6aa413b141b41dbac0c7f1fd.jsonl[9033] _id=6abd0d5f485cab4c958756e9 ts=2026-09-30T13:23:43.5170000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[9037] _id=6abd0d60485cab4c95875735 ts=2026-09-30T13:23:44.0740000Z`; `355ms: 6aa413b141b41dbac0c7f1fd.jsonl[9037] _id=6abd0d60485cab4c95875735 ts=2026-09-30T13:23:44.0740000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[9040] _id=6abd0d60485cab4c9587575f ts=2026-09-30T13:23:44.4290000Z`; `448ms: 6aa413b141b41dbac0c7f1fd.jsonl[9125] _id=6abd0dae485cab4c958780d3 ts=2026-09-30T13:25:02.1450000Z ~ 6aa413b141b41dbac0c7f1fd.jsonl[9129] _id=6abd0daf485cab4c95878153 ts=2026-09-30T13:25:02.5930000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa413b141b41dbac0c7f1fd.jsonl[11413] _id=6abe5fcb485cab4c95a59243 ts=2026-10-01T13:27:33.3470000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11990] _id=6ac39eb8de269131f9a83d3c ts=2026-10-05T12:57:21.7490000Z; 71h 56m: 6aa413b141b41dbac0c7f1fd.jsonl[3766] _id=6ab670e1485cab4c95545a3d ts=2026-09-25T13:02:25.9800000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5068] _id=6aba6491485cab4c95679607 ts=2026-09-28T12:58:57.1120000Z; 24h 9m: 6aa413b141b41dbac0c7f1fd.jsonl[777] _id=6ab51d31485cab4c954fbd75 ts=2026-09-24T12:53:05.0640000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[3766] _id=6ab670e1485cab4c95545a3d ts=2026-09-25T13:02:25.9800000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 51m 
  - Evidence: 95h 51m: 6aa413b141b41dbac0c7f1fd.jsonl[2731] _id=6ab52409485cab4c9550ae1a ts=2026-09-24T13:22:17.4240000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5220] _id=6aba6815485cab4c9567bbf5 ts=2026-09-28T13:13:57.0540000Z; 24h 19m: 6aa413b141b41dbac0c7f1fd.jsonl[6332] _id=6abbb7c3485cab4c957c2172 ts=2026-09-29T13:06:11.3250000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[9135] _id=6abd0db7485cab4c958785a5 ts=2026-09-30T13:25:11.7100000Z; 23h 48m: 6aa413b141b41dbac0c7f1fd.jsonl[9141] _id=6abd0e0f485cab4c9587b047 ts=2026-09-30T13:26:39.8050000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11158] _id=6abe5cc9485cab4c95a48d3d ts=2026-10-01T13:14:49.4650000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa413b141b41dbac0c7f1fd.jsonl[11981] _id=6abe62f7485cab4c95a68002 ts=2026-10-01T13:41:11.7300000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11999] _id=6ac39ebede269131f9a83d4a ts=2026-10-05T12:57:34.8620000Z; 71h 24m: 6aa413b141b41dbac0c7f1fd.jsonl[5052] _id=6ab67861485cab4c955526f8 ts=2026-09-25T13:34:26.0200000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5060] _id=6aba6497485cab4c9567960d ts=2026-09-28T12:59:03.1700000Z; 23h 31m: 6aa413b141b41dbac0c7f1fd.jsonl[3711] _id=6ab52633485cab4c95511efa ts=2026-09-24T13:31:31.2530000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[3776] _id=6ab670e9485cab4c95545b1f ts=2026-09-25T13:02:31.8490000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 638 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fd.jsonl[9821] _id=6abd3200485cab4c958d2b11 ts=2026-09-30T16:00:00.0540000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[9833] _id=6abd3206485cab4c958d2b23 ts=2026-09-30T16:00:00.0540000Z; 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[10015] _id=6abd32a0485cab4c958d379e ts=2026-09-30T16:02:40.1050000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10008] _id=6abd32a0485cab4c958d37a2 ts=2026-09-30T16:02:40.1060000Z; 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[10030] _id=6abd32b3485cab4c958d3908 ts=2026-09-30T16:02:59.4050000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10031] _id=6abd32b3485cab4c958d390e ts=2026-09-30T16:02:59.4060000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 56m 
  - Evidence: 143h 56m: 6aa413b141b41dbac0c7f1fd.jsonl[757] _id=6ab3d618485cab4c954c9688 ts=2026-09-23T13:37:28.1690000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[7387] _id=6abbbe30485cab4c957d52d2 ts=2026-09-29T13:33:36.4570000Z; 96h 11m: 6aa413b141b41dbac0c7f1fd.jsonl[11388] _id=6abe5fa1485cab4c95a58715 ts=2026-10-01T13:26:57.5690000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12963] _id=6ac3a844de269131f9a97ee7 ts=2026-10-05T13:38:12.4900000Z; 47h 53m: 6aa413b141b41dbac0c7f1fd.jsonl[7387] _id=6abbbe30485cab4c957d52d2 ts=2026-09-29T13:33:36.4570000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11388] _id=6abe5fa1485cab4c95a58715 ts=2026-10-01T13:26:57.5690000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa413b141b41dbac0c7f1fd.jsonl[11962] _id=6abe628e485cab4c95a664af ts=2026-10-01T13:39:26.6600000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12003] _id=6ac39eb8de269131f9a83d40 ts=2026-10-05T12:57:26.4540000Z; 71h 31m: 6aa413b141b41dbac0c7f1fd.jsonl[4911] _id=6ab67765485cab4c95550c2e ts=2026-09-25T13:30:13.9630000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5109] _id=6aba6537485cab4c95679aaf ts=2026-09-28T13:01:43.6330000Z; 23h 31m: 6aa413b141b41dbac0c7f1fd.jsonl[3696] _id=6ab52629485cab4c95511eaf ts=2026-09-24T13:31:20.9880000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[3792] _id=6ab670f1485cab4c95545b69 ts=2026-09-25T13:02:41.4460000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 191 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[8074] _id=6abd07bc485cab4c9586782f ts=2026-09-30T12:59:39.8900000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[8075] _id=6abd07bc485cab4c95867835 ts=2026-09-30T12:59:39.8910000Z; 2ms: 6aa413b141b41dbac0c7f1fd.jsonl[10612] _id=6abe5855485cab4c95a40001 ts=2026-10-01T12:55:48.9400000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10610] _id=6abe5855485cab4c95a40003 ts=2026-10-01T12:55:48.9420000Z; 2ms: 6aa413b141b41dbac0c7f1fd.jsonl[11776] _id=6abe60cb485cab4c95a5de2c ts=2026-10-01T13:31:54.4460000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11777] _id=6abe60cb485cab4c95a5de3c ts=2026-10-01T13:31:54.4480000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 6aa413b141b41dbac0c7f1fd.jsonl[11922] _id=6abe61cf485cab4c95a6284f ts=2026-10-01T13:36:15.4980000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12031] _id=6ac39effde269131f9a83e86 ts=2026-10-05T12:58:39.0100000Z; 71h 46m: 6aa413b141b41dbac0c7f1fd.jsonl[4876] _id=6ab6773d485cab4c9555078c ts=2026-09-25T13:29:34.1420000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5294] _id=6aba689a485cab4c9567c50f ts=2026-09-28T13:16:10.8300000Z; 23h 55m: 6aa413b141b41dbac0c7f1fd.jsonl[3488] _id=6ab5256f485cab4c95510445 ts=2026-09-24T13:28:13.5200000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[4671] _id=6ab675df485cab4c9554cdda ts=2026-09-25T13:23:43.5980000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[10647] _id=6abe58c7485cab4c95a40559 ts=2026-10-01T12:57:43.3660000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10648] _id=6abe58c7485cab4c95a4055b ts=2026-10-01T12:57:43.3670000Z; 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[9585] _id=6abd1141485cab4c9588ec97 ts=2026-09-30T13:40:17.0390000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[9582] _id=6abd1141485cab4c9588ec9b ts=2026-09-30T13:40:17.0400000Z; 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[9656] _id=6abd30f7485cab4c958d0f22 ts=2026-09-30T15:55:35.3400000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[9659] _id=6abd30f7485cab4c958d0f24 ts=2026-09-30T15:55:35.3410000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa413b141b41dbac0c7f1fd.jsonl[11980] _id=6abe62f5485cab4c95a67fa1 ts=2026-10-01T13:41:09.9370000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11991] _id=6ac39eb8de269131f9a83d3e ts=2026-10-05T12:57:21.7530000Z; 71h 24m: 6aa413b141b41dbac0c7f1fd.jsonl[5048] _id=6ab6785f485cab4c955526a8 ts=2026-09-25T13:34:23.2200000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5058] _id=6aba6497485cab4c95679609 ts=2026-09-28T12:58:57.1180000Z; 23h 30m: 6aa413b141b41dbac0c7f1fd.jsonl[3714] _id=6ab5263b485cab4c95511f47 ts=2026-09-24T13:31:39.6750000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[3775] _id=6ab670e8485cab4c95545b13 ts=2026-09-25T13:02:25.9920000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa413b141b41dbac0c7f1fd.jsonl[3743] _id=6ab67214485cab4c95546e0d ts=2026-09-25T13:07:28.2200000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[6419] _id=6abbb882485cab4c957c2dac ts=2026-09-29T13:09:21.3930000Z; 95h 29m: 6aa413b141b41dbac0c7f1fd.jsonl[11532] _id=6abe60d2485cab4c95a5dfc1 ts=2026-10-01T13:32:00.8700000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12089] _id=6ac39f90de269131f9a84206 ts=2026-10-05T13:01:03.7470000Z; 23h 54m: 6aa413b141b41dbac0c7f1fd.jsonl[9424] _id=6abd0fb7485cab4c95886ab2 ts=2026-09-30T13:33:38.2750000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11416] _id=6abe5fd1485cab4c95a593f5 ts=2026-10-01T13:27:42.9110000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2274 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fd.jsonl[1000] _id=6ab51e7a485cab4c954fe065 ts=2026-09-24T12:56:43.0400000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[1020] _id=6ab51e7a485cab4c954fe06b ts=2026-09-24T12:56:43.0400000Z; 0ms: 6aa413b141b41dbac0c7f1fd.jsonl[1001] _id=6ab51e7b485cab4c954fe076 ts=2026-09-24T12:56:43.0540000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[1002] _id=6ab51e7b485cab4c954fe07b ts=2026-09-24T12:56:43.0540000Z; 0ms: 6aa413b141b41dbac0c7f1fd.jsonl[1002] _id=6ab51e7b485cab4c954fe07b ts=2026-09-24T12:56:43.0540000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[1010] _id=6ab51e7b485cab4c954fe07f ts=2026-09-24T12:56:43.0540000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6aa413b141b41dbac0c7f1fd.jsonl[2810] _id=6ab52477485cab4c9550ce4e ts=2026-09-24T13:24:07.6330000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[6380] _id=6abbb834485cab4c957c2622 ts=2026-09-29T13:08:04.4120000Z; 23h 22m: 6aa413b141b41dbac0c7f1fd.jsonl[7510] _id=6abbbf7f485cab4c957d8ab8 ts=2026-09-29T13:39:11.6990000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[8112] _id=6abd0828485cab4c95867f33 ts=2026-09-30T13:01:28.3610000Z; 30m 16s: 6aa413b141b41dbac0c7f1fd.jsonl[6401] _id=6abbb85b485cab4c957c2928 ts=2026-09-29T13:08:43.0050000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[7492] _id=6abbbf73485cab4c957d88ae ts=2026-09-29T13:38:59.1390000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 71h 56m 
  - Evidence: 71h 56m: 6aa413b141b41dbac0c7f1fd.jsonl[4541] _id=6ab67451485cab4c95549c73 ts=2026-09-25T13:17:06.0460000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5219] _id=6aba6816485cab4c9567bc09 ts=2026-09-28T13:13:58.8110000Z; 23h 55m: 6aa413b141b41dbac0c7f1fd.jsonl[2719] _id=6ab523ea485cab4c9550a7cf ts=2026-09-24T13:21:46.1470000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[4518] _id=6ab67443485cab4c95549aa3 ts=2026-09-25T13:16:51.7290000Z; 23h 38m: 6aa413b141b41dbac0c7f1fd.jsonl[5794] _id=6aba6b40485cab4c9567f7e7 ts=2026-09-28T13:27:27.9950000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[6291] _id=6abbb7b1485cab4c957c20fa ts=2026-09-29T13:05:54.0250000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.038s..0.042s shown 
  - Evidence: 38ms: 6aa413b141b41dbac0c7f1fd.jsonl[2466] _id=6ab52194485cab4c9550281f ts=2026-09-24T13:11:48.1320000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[2467] _id=6ab52194485cab4c95502827 ts=2026-09-24T13:11:48.1700000Z; 42ms: 6aa413b141b41dbac0c7f1fd.jsonl[2467] _id=6ab52194485cab4c95502827 ts=2026-09-24T13:11:48.1700000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[2469] _id=6ab52194485cab4c95502839 ts=2026-09-24T13:11:48.2120000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1fd.jsonl[11957] _id=6abe6283485cab4c95a65fc9 ts=2026-10-01T13:39:15.5090000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12013] _id=6ac39ec8de269131f9a83dac ts=2026-10-05T12:57:44.6050000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 14m 
  - Evidence: 96h 14m: 6aa413b141b41dbac0c7f1fd.jsonl[10961] _id=6abe5ade485cab4c95a4380f ts=2026-10-01T13:06:38.7370000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12590] _id=6ac3a447de269131f9a8b33a ts=2026-10-05T13:21:11.7590000Z; 71h 59m: 6aa413b141b41dbac0c7f1fd.jsonl[5037] _id=6ab67824485cab4c95551eba ts=2026-09-25T13:33:24.2020000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5937] _id=6aba6c94485cab4c956805b1 ts=2026-09-28T13:33:08.5220000Z; 50h 21m: 6aa413b141b41dbac0c7f1fd.jsonl[6237] _id=6aba6de3485cab4c95681341 ts=2026-09-28T13:38:43.0720000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[9817] _id=6abd3200485cab4c958d2b09 ts=2026-09-30T16:00:00.0330000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 13m 
  - Evidence: 96h 13m: 6aa413b141b41dbac0c7f1fd.jsonl[10966] _id=6abe5adf485cab4c95a4381f ts=2026-10-01T13:06:38.7850000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12556] _id=6ac3a421de269131f9a8ac44 ts=2026-10-05T13:20:33.3600000Z; 71h 58m: 6aa413b141b41dbac0c7f1fd.jsonl[5038] _id=6ab67824485cab4c95551ec5 ts=2026-09-25T13:33:24.2340000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5912] _id=6aba6c55485cab4c95680353 ts=2026-09-28T13:32:05.2420000Z; 50h 21m: 6aa413b141b41dbac0c7f1fd.jsonl[6170] _id=6aba6dbe485cab4c9568112b ts=2026-09-28T13:38:05.7170000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[9766] _id=6abd31cc485cab4c958d2754 ts=2026-09-30T15:59:08.6680000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.028s..0.037s shown 
  - Evidence: 28ms: 6aa413b141b41dbac0c7f1fd.jsonl[6010] _id=6aba6cb1485cab4c956806e1 ts=2026-09-28T13:33:37.1900000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5997] _id=6aba6cb1485cab4c956806e7 ts=2026-09-28T13:33:37.2180000Z; 29ms: 6aa413b141b41dbac0c7f1fd.jsonl[10962] _id=6abe5ade485cab4c95a43813 ts=2026-10-01T13:06:38.7560000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10966] _id=6abe5adf485cab4c95a4381f ts=2026-10-01T13:06:38.7850000Z; 37ms: 6aa413b141b41dbac0c7f1fd.jsonl[6143] _id=6aba6dbd485cab4c95681125 ts=2026-09-28T13:38:05.6800000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[6170] _id=6aba6dbe485cab4c9568112b ts=2026-09-28T13:38:05.7170000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 14m 
  - Evidence: 96h 14m: 6aa413b141b41dbac0c7f1fd.jsonl[10956] _id=6abe5ad5485cab4c95a43727 ts=2026-10-01T13:06:29.7680000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12552] _id=6ac3a41fde269131f9a8abe8 ts=2026-10-05T13:20:31.1800000Z; 71h 58m: 6aa413b141b41dbac0c7f1fd.jsonl[5029] _id=6ab6781d485cab4c95551dde ts=2026-09-25T13:33:17.4980000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5905] _id=6aba6c4d485cab4c95680307 ts=2026-09-28T13:31:57.2480000Z; 47h 56m: 6aa413b141b41dbac0c7f1fd.jsonl[650] _id=6ab3d579485cab4c954c82cb ts=2026-09-23T13:34:49.6480000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[4937] _id=6ab677b7485cab4c95551194 ts=2026-09-25T13:31:35.7920000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 248 interval(s) ≤ 0.001s..0.016s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[10552] _id=6abd35bc485cab4c958d6c94 ts=2026-09-30T16:15:56.0180000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10553] _id=6abd35bc485cab4c958d6c96 ts=2026-09-30T16:15:56.0190000Z; 13ms: 6aa413b141b41dbac0c7f1fd.jsonl[10127] _id=6abd335a485cab4c958d41d2 ts=2026-09-30T16:05:46.5200000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10128] _id=6abd335a485cab4c958d41d6 ts=2026-09-30T16:05:46.5330000Z; 16ms: 6aa413b141b41dbac0c7f1fd.jsonl[10584] _id=6abd35d6485cab4c958d6e5a ts=2026-09-30T16:16:22.8780000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[10585] _id=6abd35d7485cab4c958d6e5e ts=2026-09-30T16:16:22.8940000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 120h 3m 
  - Evidence: 120h 3m: 6aa413b141b41dbac0c7f1fd.jsonl[622] _id=6ab3d561485cab4c954c803b ts=2026-09-23T13:34:25.9030000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[6194] _id=6aba6dce485cab4c956811ef ts=2026-09-28T13:38:22.8790000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa413b141b41dbac0c7f1fd.jsonl[11410] _id=6abe5fc5485cab4c95a59079 ts=2026-10-01T13:27:33.2300000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12002] _id=6ac39eb1de269131f9a83d28 ts=2026-10-05T12:57:21.6810000Z; 48h 21m: 6aa413b141b41dbac0c7f1fd.jsonl[6326] _id=6abbb7c2485cab4c957c216c ts=2026-09-29T13:06:10.1950000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11410] _id=6abe5fc5485cab4c95a59079 ts=2026-10-01T13:27:33.2300000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa413b141b41dbac0c7f1fd.jsonl[11409] _id=6abe5fb9485cab4c95a58d5c ts=2026-10-01T13:27:21.6360000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12001] _id=6ac39ea4de269131f9a83d18 ts=2026-10-05T12:57:07.9340000Z; 71h 56m: 6aa413b141b41dbac0c7f1fd.jsonl[3765] _id=6ab670da485cab4c95545929 ts=2026-09-25T13:02:18.8410000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5067] _id=6aba648a485cab4c95679601 ts=2026-09-28T12:58:50.4570000Z; 24h 9m: 6aa413b141b41dbac0c7f1fd.jsonl[778] _id=6ab51d28485cab4c954fbd59 ts=2026-09-24T12:52:56.3900000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[3765] _id=6ab670da485cab4c95545929 ts=2026-09-25T13:02:18.8410000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 95h 15m 
  - Evidence: 95h 15m: 6aa413b141b41dbac0c7f1fd.jsonl[11982] _id=6abe62f9485cab4c95a68075 ts=2026-10-01T13:41:13.4300000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11997] _id=6ac39ea3de269131f9a83d16 ts=2026-10-05T12:57:07.9320000Z; 71h 24m: 6aa413b141b41dbac0c7f1fd.jsonl[5054] _id=6ab67866485cab4c9555278a ts=2026-09-25T13:34:30.1830000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5057] _id=6aba648a485cab4c956795ff ts=2026-09-28T12:58:50.4560000Z; 23h 30m: 6aa413b141b41dbac0c7f1fd.jsonl[3713] _id=6ab52644485cab4c95511fa1 ts=2026-09-24T13:31:48.6030000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[3764] _id=6ab670da485cab4c95545923 ts=2026-09-25T13:02:18.8400000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 34m 
  - Evidence: 95h 34m: 6aa413b141b41dbac0c7f1fd.jsonl[11987] _id=6abe62f9485cab4c95a68071 ts=2026-10-01T13:41:13.4200000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12475] _id=6ac3a2fade269131f9a88122 ts=2026-10-05T13:15:38.6750000Z; 71h 25m: 6aa413b141b41dbac0c7f1fd.jsonl[5053] _id=6ab67866485cab4c95552777 ts=2026-09-25T13:34:30.1700000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5077] _id=6aba64e2485cab4c956797b3 ts=2026-09-28T13:00:18.8530000Z; 23h 46m: 6aa413b141b41dbac0c7f1fd.jsonl[6249] _id=6aba6e62485cab4c95681891 ts=2026-09-28T13:40:50.3930000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[7273] _id=6abbbcd6485cab4c957d0162 ts=2026-09-29T13:27:50.3420000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa413b141b41dbac0c7f1fd.jsonl[11910] _id=6abe61dd485cab4c95a62d3a ts=2026-10-01T13:36:29.5700000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12004] _id=6ac39eb8de269131f9a83d42 ts=2026-10-05T12:57:27.8610000Z; 71h 25m: 6aa413b141b41dbac0c7f1fd.jsonl[5041] _id=6ab67834485cab4c955520e2 ts=2026-09-25T13:33:40.5950000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[5059] _id=6aba6497485cab4c9567960b ts=2026-09-28T12:59:03.1640000Z; 23h 31m: 6aa413b141b41dbac0c7f1fd.jsonl[3705] _id=6ab5262e485cab4c95511ecb ts=2026-09-24T13:31:26.1890000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[3784] _id=6ab670e9485cab4c95545b29 ts=2026-09-25T13:02:32.4150000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[11848] _id=6abe6131485cab4c95a5fc33 ts=2026-10-01T13:33:37.2000000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[11851] _id=6abe6131485cab4c95a5fc37 ts=2026-10-01T13:33:37.2010000Z; 1ms: 6aa413b141b41dbac0c7f1fd.jsonl[12620] _id=6ac3a48bde269131f9a8bf88 ts=2026-10-05T13:22:19.8860000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12640] _id=6ac3a48cde269131f9a8bf8b ts=2026-10-05T13:22:19.8870000Z; 2ms: 6aa413b141b41dbac0c7f1fd.jsonl[12189] _id=6ac39fa6de269131f9a84304 ts=2026-10-05T13:01:26.3990000Z -> 6aa413b141b41dbac0c7f1fd.jsonl[12194] _id=6ac39fa6de269131f9a84306 ts=2026-10-05T13:01:26.4010000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[469] _id=6ab3d46d485cab4c954c4ff9 ts=2026-09-23T13:30:22.0340000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[668] _id=6ab3d58f485cab4c954c8659 ts=2026-09-23T13:35:11.6570000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[2586] _id=6ab522e8485cab4c95506b09 ts=2026-09-24T13:17:28.2610000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 155 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[1006] _id=6ab51e86485cab4c954fe239 ts=2026-09-24T12:58:45.6110000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[1100] _id=6ab51e88485cab4c954fe2a5 ts=2026-09-24T12:58:47.0870000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[1101] _id=6ab51e88485cab4c954fe2aa ts=2026-09-24T12:58:47.0930000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 517 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[1003] _id=6ab51e7a485cab4c954fe059 ts=2026-09-24T12:56:42.9440000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[1032] _id=6ab51e7c485cab4c954fe0b5 ts=2026-09-24T12:56:43.6000000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[958] _id=6ab51e6e485cab4c954fdea5 ts=2026-09-24T12:58:20.8060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[5997] _id=6aba6cb1485cab4c956806e7 ts=2026-09-28T13:33:37.2180000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[6143] _id=6aba6dbd485cab4c95681125 ts=2026-09-28T13:38:05.6800000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[6170] _id=6aba6dbe485cab4c9568112b ts=2026-09-28T13:38:05.7170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 32 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[575] _id=6ab3d50b485cab4c954c6f37 ts=2026-09-23T13:32:58.9950000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[588] _id=6ab3d50f485cab4c954c7084 ts=2026-09-23T13:33:03.8940000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[5028] _id=6ab6781d485cab4c95551dd0 ts=2026-09-25T13:33:17.4580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[11410] _id=6abe5fc5485cab4c95a59079 ts=2026-10-01T13:27:33.2300000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[12002] _id=6ac39eb1de269131f9a83d28 ts=2026-10-05T12:57:21.6810000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[12306] _id=6ac3a0d4de269131f9a85612 ts=2026-10-05T13:06:28.7030000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[4379] _id=6ab6723f485cab4c95547007 ts=2026-09-25T13:08:15.6460000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[6418] _id=6abbb87b485cab4c957c2cd8 ts=2026-09-29T13:09:15.5780000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[8526] _id=6abd0a12485cab4c95869d9d ts=2026-09-30T13:09:38.5410000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[769] _id=6ab3d6a7485cab4c954cab4d ts=?`; `6aa413b141b41dbac0c7f1fd.jsonl[9617] _id=6abd3075485cab4c958d089e ts=?`; `6aa413b141b41dbac0c7f1fd.jsonl[11998] _id=6ac39eb8de269131f9a83d3a ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 552 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[1159] _id=6ab51e94485cab4c954fe4a7 ts=2026-09-24T12:59:00.1470000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[1171] _id=6ab51e99485cab4c954fe513 ts=2026-09-24T12:59:03.6910000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[1172] _id=6ab51e99485cab4c954fe517 ts=2026-09-24T12:59:03.6980000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 522 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[1020] _id=6ab51e7a485cab4c954fe06b ts=2026-09-24T12:56:43.0400000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[946] _id=6ab51e7c485cab4c954fe0b3 ts=2026-09-24T12:56:43.5580000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[953] _id=6ab51e6c485cab4c954fde65 ts=2026-09-24T12:58:20.5360000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 30 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[2467] _id=6ab52194485cab4c95502827 ts=2026-09-24T13:11:48.1700000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[2469] _id=6ab52194485cab4c95502839 ts=2026-09-24T13:11:48.2120000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[2491] _id=6ab521b0485cab4c95502bcb ts=2026-09-24T13:12:16.7520000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[10755] _id=6abe59c5485cab4c95a41b9b ts=2026-10-01T13:01:57.4520000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 89 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[5939] _id=6aba6c75485cab4c956804bb ts=2026-09-28T13:32:37.4900000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[6177] _id=6aba6dd5485cab4c9568124b ts=2026-09-28T13:38:29.3730000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[9779] _id=6abd31d6485cab4c958d283a ts=2026-09-30T15:59:18.0670000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[615] _id=6ab3d55d485cab4c954c7fe3 ts=2026-09-23T13:34:21.9540000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[621] _id=6ab3d560485cab4c954c8017 ts=2026-09-23T13:34:24.7440000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 412 start, 405 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 204 unmatched 'BecameCameraCentered' (totals: 734 open, 685 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 88 unmatched 'BecameVisible' (totals: 837 open, 1266 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 32 open, 30 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationNodeHoverStart' (totals: 474 open, 498 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 5 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 47 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 365 of 12960 adjacent _id pairs reverse in client time; worst 110.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1fd.jsonl[1008] _id=6ab51e79485cab4c954fe03d ts=2026-09-24T12:58:33.4470000Z`; `6aa413b141b41dbac0c7f1fd.jsonl[1015] _id=6ab51e7a485cab4c954fe049 ts=2026-09-24T12:56:42.7650000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -112.57s, max +0.27s over 12961 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1fd\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3522 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2384); Unit 4 Dev (708); Unit 5 Dev - Dungeon (290); Unit 3 Dungeon Dev (140)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.94s, n=3521)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3522/3522 records)
    "BecameInvisible"  x1266
    "BecameVisible"  x837
    "BecameCameraCentered"  x734
    "BecameCameraUncentered"  x685
data.pieceId  (string, 3522/3522 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3522/3522 records)
    1825 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3303 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (677); Unit 2 Prod (Refactor) (673); Unit 4 Dev - Dungeon (536); Unit 4 Dev (362); Unit 5 Dev - Dungeon (297); Unit 3 Dungeon Dev (259); Unit 1 Dev (226); Unit 5 Dev (161); Unit 4 Dev - Anderson Base (112)
- **Intervals:** median 0.80s (p5 0.04s / p95 17.37s, n=3302)
- **Fields under `data`:**

```text
data.Value  (string, 3303/3303 records)
    "pressed"  x3303
data.actionType  (string, 3303/3303 records)
    "Move"  x1900
    "Sprint"  x714
    "Interact"  x360
    "Jump"  x109
    "Descend"  x53
    "Hoverboard"  x50
    "Ascend"  x49
    "Map"  x36
    "Pause"  x25
    "SkipCinematic"  x5
    "ToggleDebug"  x2
data.key  (string, 3303/3303 records, 13 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3303/3303 records)
    "Player"  x2798
    "Drone"  x505
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2262 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (568); Unit 3 Dev (354); Unit 4 Dev - Anderson Base (280); Unit 4 Dev (276); Unit 5 Dev (230); Unit 1 Dev (221); Unit 3 Dungeon Dev (130); Unit 4 Dev - Dungeon (108); Unit 5 Dev - Dungeon (95)
- **eventKey:** present on 1445 of 2262 records
- **Intervals:** median 3.63s (p5 0.00s / p95 34.03s, n=2261)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1445; [conversationId, dialogueEventType] x817
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2262/2262 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2262/2262 records)
    "DialogueNodeEvent"  x1445
    "DialogueStartEvent"  x412
    "DialogueFinishEvent"  x405
data.nodeId  (number, 1445/2262 records)
    numeric range 0 .. 290 (231 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1883 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (459); Unit 3 Dev (262); Unit 4 Dev - Anderson Base (223); Unit 4 Dev (221); Unit 1 Dev (188); Unit 5 Dev (186); Unit 4 Dev - Dungeon (147); Unit 5 Dev - Dungeon (129); Unit 3 Dungeon Dev (68)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.09s, n=1869)
- **Fields under `data`:**

```text
data.position  (object, 1883/1883 records)
data.position.x  (number, 1883/1883 records)
    numeric range -817.411 .. 1559.19 (528 unique)
data.position.y  (number, 1883/1883 records)
    numeric range -113.543 .. 222.061 (396 unique)
data.position.z  (number, 1883/1883 records)
    numeric range -1029.16 .. 1919.46 (528 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 1087 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (741); Unit 3 Dev (136); Unit 2 Prod (Refactor) (109); Unit 1 Dev (65); Unit 5 Dev (36)
- **Intervals:** median 0.36s (p5 0.02s / p95 7.75s, n=1086)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1087/1087 records)
    "argumentationNodeHoverEnd"  x498
    "argumentationNodeHoverStart"  x474
    "argumentationNodeAdd"  x66
    "argumentationNodeRemove"  x49
data.argumentationTitle  (string, 1087/1087 records)
    "Unit 4 - Flooding"  x741
    "Unit 3 - Pollution Upstream"  x136
    "Unit 2 – Watershed"  x109
    "Unit 5"  x36
    "Unit 1 - Freshwater"  x33
    "Unit 1 - Argumentation Tutorial"  x32
data.nodeName  (string, 1087/1087 records)
    "B"  x149
    "A"  x124
    "2"  x118
    "C"  x108
    "I"  x102
    "D"  x100
    "II"  x100
    "1"  x95
    "3"  x91
    "4"  x75
    "5"  x25
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 288 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (96); Unit 2 Prod (Refactor) (52); Unit 3 Dungeon Dev (33); Unit 4 Dev - Anderson Base (22); Unit 1 Dev (21); Unit 4 Dev (20); Unit 5 Dev (18); Unit 5 Dev - Dungeon (15); Unit 3 Dev (11)
- **Intervals:** median 5.85s (p5 0.20s / p95 362.31s, n=287)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 288/288 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 288/288 records)
    104 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 99 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (56); Unit 2 Prod (Refactor) (41); Unit 4 Dev (2)
- **Intervals:** median 4.22s (p5 0.50s / p95 589.39s, n=98)
- **`data` key-set variants:** [actionType, featureUsed] x62; [actionType, featureUsed, location] x35; [actionType, featureUsed, legendName] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 99/99 records)
    "MapOpenEvent"  x32
    "MapCloseEvent"  x30
    "WaypointMoveEvent"  x25
    "WaypointSetEvent"  x6
    "WaypointResetEvent"  x4
    "Selected"  x2
data.featureUsed  (string, 99/99 records)
    "Map"  x62
    "Waypoint"  x35
    "Legend"  x2
data.legendName  (string, 2/99 records)
    "120 ft"  x1
    "210 ft"  x1
data.location  (object, 35/99 records)
data.location.x  (number, 35/99 records)
    numeric range -252.284 .. 652.815 (27 unique)
data.location.y  (number, 35/99 records)
    numeric range -274.895 .. 301.627 (26 unique)
data.location.z  (number, 35/99 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 82 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (12); Unit 3 Dev (12); Unit 5 Dev - Dungeon (10); Unit 4 Dev (9); Unit 4 Dev - Dungeon (8); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 82 of 82 records
- **Intervals:** median 213.15s (p5 0.00s / p95 84152.49s, n=81)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 82/82 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x35
data.questID  (string, 82/82 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 82/82 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/82 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 65 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (17); Unit 3 Dev (7); Unit 4 Dev - Anderson Base (7); Unit 1 Dev (4); Unit 5 Dev - Dungeon (4); Transition (3); Unit 4 Dev - Dungeon (3); Unit 5 Dev (2)
- **Intervals:** median 152.16s (p5 4.80s / p95 84194.50s, n=64)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 65/65 records)
    true  x65
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 64 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (36); Unit 4 Dev (16); Unit 3 Dev (12)
- **Intervals:** median 1.00s (p5 0.17s / p95 1056.84s, n=63)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x54; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/64 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/64 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 54/64 records)
    "RightDrag"  x30
    "LeftDrag"  x24
data.currentSoilType  (string, 54/64 records)
    "CLAY"  x12
    "CLAYSAND"  x11
    "CLAYROCK"  x8
    "SAND"  x8
    "SANDGRAVEL"  x8
    "GRAVEL"  x4
    "BEDROCK"  x3
data.isCorrectSelection  (string, 54/64 records)
    "false"  x43
    "true"  x11
data.waterLevelStatus  (string, 54/64 records)
    "Proper"  x24
    "TooHigh"  x20
    "TooLow"  x10
data.waterRetentionChange  (string, 54/64 records)
    "Increase"  x26
    "Decrease"  x17
    "NoChange"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 64 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (44); Unit 3 Dev (13); Unit 2 Prod (Refactor) (4); Unit 1 Dev (2); Unit 5 Dev (1)
- **Intervals:** median 15.06s (p5 0.18s / p95 162875.34s, n=63)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 64/64 records)
    "submitAnswerEvent"  x64
data.answerSubmitted  (string, 64/64 records, 8 empty-string)
    21 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 64/64 records)
    "Unit 4 - Flooding"  x44
    "Unit 3 - Pollution Upstream"  x13
    "Unit 2 – Watershed"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 48 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 4 Dev - Anderson Base (8); Unit 3 Dev (7); Unit 1 Dev (4); Unit 5 Dev - Dungeon (4); Transition (3); Unit 4 Dev - Dungeon (3); Unit 5 Dev (2)
- **Intervals:** median 190.69s (p5 1.24s / p95 85575.35s, n=47)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 48/48 records)
    false  x48
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `WaterChamberEvent` — 41 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (41)
- **Intervals:** median 4.46s (p5 0.19s / p95 137.69s, n=40)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "On"  x26
    "Off"  x15
data.floor  (string, 41/41 records)
    "3"  x25
    "2"  x7
    "4"  x7
    "1"  x2
data.machineNumber  (string, 41/41 records)
    "One"  x40
    "Two"  x1
data.machineType  (string, 41/41 records)
    "Condenser"  x16
    "DualChamber_Condenser"  x9
    "DualChamber_Evaporator"  x7
    "Evaporator"  x6
    "VentSwitch"  x3
data.room  (string, 41/41 records)
    "2"  x24
    "1"  x9
    "3"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 32 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (32)
- **Intervals:** median 2.64s (p5 0.50s / p95 137.12s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "ChangeCanister"  x32
data.canisterType  (string, 32/32 records)
    "Bedrock"  x13
    "Clay"  x9
    "Gravel"  x5
    "Sand"  x5
data.floor  (string, 32/32 records)
    "5"  x25
    "4"  x6
    "3"  x1
data.machine  (string, 32/32 records)
    "1"  x28
    "2"  x4
data.row  (string, 32/32 records)
    "TopRow"  x23
    "BottomRow"  x9
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 24 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 1140.94s (p5 184.31s / p95 241788.11s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "DebugMenuStateChanged"  x24
data.isOpened  (bool, 24/24 records)
    false  x24
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 18 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (12); Unit 2 Prod (Refactor) (2); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 7.73s (p5 1.06s / p95 139052.23s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "Close"  x9
    "Open"  x9
data.toolName  (string, 18/18 records, 18 empty-string)
    ""  x18
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 18 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (18)
- **Intervals:** median 2.19s (p5 0.86s / p95 4.18s, n=17)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x17; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "optionSelected"  x17
    "DesignSubmitted"  x1
data.designSelections  (object, 1/18 records)
data.designSelections.glassRoofTemperature  (string, 1/18 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/18 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/18 records)
    "Tilted Out"  x1
data.featureUsed  (string, 18/18 records)
    "ExtraCovering"  x6
    "GlassRoofTemperature"  x6
    "RoofStyle"  x5
    "Submit"  x1
data.selectedOption  (string, 17/18 records, 3 empty-string)
    ""  x3
    "Cold"  x3
    "Covered"  x3
    "Hot"  x3
    "Tilted Out"  x3
    "Uncovered"  x2
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 2116.44s (p5 97.53s / p95 275950.55s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (5); Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 97.65s (p5 0.03s / p95 280949.40s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 17/17 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x5
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 3 - Pollution Upstream"  x5
    "Unit 4 - Flooding"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 5.86s (p5 1.35s / p95 22.64s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x4
data.boxId  (string, 9/9 records)
    "1"  x5
    "0"  x2
    "2"  x2
data.soilType  (string, 9/9 records)
    "Clay"  x5
    "Sand"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (1)
- **Intervals:** median 2.57s (p5 0.26s / p95 302596.84s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2); Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 87315.03s (p5 84.15s / p95 318332.64s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x4
    "Open"  x1
data.chatID  (string, 5/5 records)
    "NA"  x4
    "[]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 346274.92s (p5 189788.49s / p95 500978.95s, n=3)
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

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Pointer is already locked."  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 3 empty-string)
    ""  x3
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x1
    "unit4"  x1
    "unit5"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open
- `argumentationNodeEvent` actionType: node hover: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (36 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (25x); "WaypointResetEvent" (4x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (35x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (49x)
- `soilMachine` data.canisterType: "Bedrock" (13x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*