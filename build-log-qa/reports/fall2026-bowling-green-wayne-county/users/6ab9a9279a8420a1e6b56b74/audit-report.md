# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b74

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b74
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b74.jsonl
- **Records:** 8646 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b74
- **Time span:** 2026-10-06T19:02:06.292000+00:00 .. 2026-10-16T18:59:21.428000+00:00 (239h 57m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b74\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 8646 records, 5 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 89 INFO, 5 NOT_TESTED, 75 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3469 | 40.12 | 1 | 2 | 0 | 2026-10-08T19:10:03.795000+00:00 | 2026-10-16T18:34:32.167000+00:00 | 191h 24m |
| InputEvent | 1918 | 22.18 | 1 | 4 | 0 | 2026-10-06T19:03:02.991000+00:00 | 2026-10-16T18:57:54.228000+00:00 | 239h 54m |
| PlayerPositionEvent | 1657 | 19.16 | 1 | 4 | 0 | 2026-10-06T19:02:59.505000+00:00 | 2026-10-16T18:59:21.428000+00:00 | 239h 56m |
| DialogueEvent | 1089 | 12.6 | 1 | 4 | 684 | 2026-10-06T19:03:19.480000+00:00 | 2026-10-16T18:59:19.937000+00:00 | 239h 56m |
| argumentationNodeEvent | 138 | 1.6 | 1 | 2 | 0 | 2026-10-07T19:15:11.256000+00:00 | 2026-10-15T23:18:18.738000+00:00 | 196h 3m |
| ObjectInterEvent | 103 | 1.19 | 1 | 4 | 0 | 2026-10-06T19:10:02.022000+00:00 | 2026-10-16T18:57:28.114000+00:00 | 239h 47m |
| TopographicMapEvent | 88 | 1.02 | 1 | 2 | 0 | 2026-10-08T19:11:17.312000+00:00 | 2026-10-16T18:57:08.036000+00:00 | 191h 45m |
| questEvent | 46 | 0.53 | 1 | 4 | 46 | 2026-10-06T19:03:19.458000+00:00 | 2026-10-16T18:57:59.025000+00:00 | 239h 54m |
| DEBUGMenu | 31 | 0.36 | 1 | 5 | 0 | 2026-10-06T19:02:59.491000+00:00 | 2026-10-16T18:49:17.230000+00:00 | 239h 46m |
| Soil Key Puzzle | 26 | 0.3 | 1 | 1 | 0 | 2026-10-15T23:24:46.126000+00:00 | 2026-10-15T23:42:57.973000+00:00 | 18m 11s |
| gameWindowFocusEvent | 16 | 0.19 | 1 | 2 | 0 | 2026-10-06T19:02:06.292000+00:00 | 2026-10-16T18:32:45.424000+00:00 | 239h 30m |
| gameStartEvent | 15 | 0.17 | 1 | 1 | 0 | 2026-10-06T19:02:06.293000+00:00 | 2026-10-16T18:32:45.424000+00:00 | 239h 30m |
| argumentationToolEvent | 13 | 0.15 | 1 | 2 | 0 | 2026-10-07T19:14:58.666000+00:00 | 2026-10-15T23:12:29.022000+00:00 | 195h 57m |
| chatEvent | 10 | 0.12 | 1 | 1 | 0 | 2026-10-14T19:10:31.091000+00:00 | 2026-10-14T19:10:51.932000+00:00 | 20.8s |
| argumentationEvent | 9 | 0.1 | 1 | 2 | 0 | 2026-10-07T19:15:01.661000+00:00 | 2026-10-15T23:18:20.889000+00:00 | 196h 3m |
| argumentationAnswerEvent | 8 | 0.09 | 1 | 2 | 0 | 2026-10-07T19:15:26.897000+00:00 | 2026-10-15T23:18:20.827000+00:00 | 196h 2m |
| gameWindowUnfocusEvent | 6 | 0.07 | 1 | 3 | 0 | 2026-10-06T19:17:42.337000+00:00 | 2026-10-15T23:27:00.272000+00:00 | 220h 9m |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-14T19:10:27.534000+00:00 | 2026-10-14T19:10:30.702000+00:00 | 3.2s |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-10-08T19:02:53.261000+00:00 | 2026-10-08T19:02:53.261000+00:00 | 0.0s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 86.25s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.328s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 15.155s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.064s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.246s median 
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
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.88s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 141.269s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 147.607s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 7.21s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 2.024s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8050.892s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 3483.323s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86465.589s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 Prod (Refactor); Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C; D 
  - Expected: may simply not have been exercised — review
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 10 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [19-0, 19-1, 19-49, 19-2, 19-59, 19-50, 19-51]; [22-5, 22-50, 22-11, 22-12, 22-13]; [23-73, 23-22, 23-24, 23-25, 23-27] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[172] _id=6ac54829de269131f9b77331 ts=2026-10-06T19:12:40.7760000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[1] _id=6ac545afde269131f9b72e83 ts=2026-10-06T19:02:06.2930000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[219] _id=6ac69300de269131f9bdf631 ts=2026-10-07T18:44:14.8300000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[652] _id=6ac7e63ade269131f9c59dd6 ts=2026-10-08T18:51:37.9180000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[0] _id=6ac545aede269131f9b72e7d ts=2026-10-06T19:02:06.2920000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[218] _id=6ac69300de269131f9bdf630 ts=2026-10-07T18:44:14.8300000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[651] _id=6ac7e63ade269131f9c59dd5 ts=2026-10-08T18:51:37.9180000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 6 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 6} 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[216] _id=6ac692ffde269131f9bdf62b ts=2026-10-06T19:17:42.337Z`; `6ab9a9279a8420a1e6b56b74.jsonl[648] _id=6ac7e63ade269131f9c59dd1 ts=2026-10-07T19:17:15.695Z`; `6ab9a9279a8420a1e6b56b74.jsonl[2189] _id=6ace7a85de269131f9d0ff85 ts=2026-10-08T19:18:21.284Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3468 | 0.0 | 0.064 | 198.693 | 1.717 | 429709.527 | 0.3 | 1565 | 6 |
| InputEvent | 1917 | 0.0 | 1.328 | 450.543 | 19.971 | 429601.724 | 0.13 | 46 | 11 |
| PlayerPositionEvent | 1652 | 9.685 | 10.001 | 522.711 | 10.113 | 429589.133 | 0.11 | 0 | 8 |
| DialogueEvent | 1088 | 0.0 | 4.783 | 793.897 | 55.102 | 429618.05 | 0.08 | 290 | 11 |
| argumentationNodeEvent | 137 | 0.02 | 0.742 | 5151.733 | 24.341 | 619947.668 | 0.01 | 16 | 2 |
| ObjectInterEvent | 102 | 0.004 | 15.155 | 8463.197 | 63672.87 | 429668.876 | 0.01 | 2 | 9 |
| TopographicMapEvent | 87 | 0.021 | 5.88 | 7935.066 | 827.798 | 430145.365 | 0.01 | 2 | 5 |
| questEvent | 45 | 0.001 | 289.246 | 19192.879 | 84940.8 | 430333.177 | 0.0 | 5 | 14 |
| DEBUGMenu | 30 | 8.089 | 86.25 | 28772.591 | 86745.572 | 430411.165 | 0.0 | 0 | 11 |
| Soil Key Puzzle | 25 | 0.154 | 2.246 | 43.674 | 17.995 | 987.886 | 1.37 | 0 | 1 |
| gameWindowFocusEvent | 15 | 88.045 | 3483.323 | 57482.609 | 189916.509 | 430421.159 | 0.0 | 0 | 10 |
| gameStartEvent | 14 | 88.045 | 8050.892 | 61588.509 | 207095.413 | 430421.159 | 0.0 | 0 | 9 |
| argumentationToolEvent | 12 | 0.144 | 7.21 | 58787.53 | 325830.95 | 619989.177 | 0.0 | 0 | 2 |
| chatEvent | 9 | 0.432 | 2.024 | 2.316 | 5.195 | 6.76 | 25.91 | 0 | 0 |
| argumentationEvent | 8 | 0.035 | 147.607 | 88224.904 | 432718.898 | 619916.96 | 0.0 | 1 | 2 |
| argumentationAnswerEvent | 7 | 7.342 | 141.269 | 100824.847 | 459588.704 | 620061.385 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 5 | 16510.667 | 86465.589 | 158511.587 | 379070.473 | 430714.681 | 0.0 | 0 | 5 |
| DaniEvent | 1 | 3.168 | 3.168 | 3.168 | 3.168 | 3.168 | 18.94 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 8 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[6495] _id=6ad15755de269131f9e1dcc2 ts=2026-10-15T22:44:36.4300000Z == 6ab9a9279a8420a1e6b56b74.jsonl[6496] _id=6ad15755de269131f9e1dcc3 ts=2026-10-15T22:44:36.4300000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[7433] _id=6ad16534de269131f9e20fc3 ts=2026-10-15T23:43:47.1750000Z == 6ab9a9279a8420a1e6b56b74.jsonl[7434] _id=6ad16534de269131f9e20fc4 ts=2026-10-15T23:43:47.1750000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[7439] _id=6ad16534de269131f9e20fc9 ts=2026-10-15T23:43:47.3140000Z == 6ab9a9279a8420a1e6b56b74.jsonl[7440] _id=6ad16534de269131f9e20fca ts=2026-10-15T23:43:47.3140000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 137 group(s), 235 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[1028] _id=6ac7eaa0de269131f9c65637 ts=2026-10-08T19:10:19.7820000Z == 6ab9a9279a8420a1e6b56b74.jsonl[1029] _id=6ac7eaa0de269131f9c6563b ts=2026-10-08T19:10:19.7820000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[1030] _id=6ac7eaa0de269131f9c65650 ts=2026-10-08T19:10:19.9070000Z == 6ab9a9279a8420a1e6b56b74.jsonl[1035] _id=6ac7eaa0de269131f9c65655 ts=2026-10-08T19:10:19.9070000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[1038] _id=6ac7eaa7de269131f9c656eb ts=2026-10-08T19:10:30.0510000Z == 6ab9a9279a8420a1e6b56b74.jsonl[1048] _id=6ac7eaa7de269131f9c656ed ts=2026-10-08T19:10:30.0510000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9279a8420a1e6b56b74.jsonl[126] _id=6ac5478ade269131f9b767eb ts=2026-10-06T19:10:02.0220000Z ~ 6ab9a9279a8420a1e6b56b74.jsonl[87] _id=6ac5478ade269131f9b767f6 ts=2026-10-06T19:10:02.0260000Z`; `7ms: 6ab9a9279a8420a1e6b56b74.jsonl[238] _id=6ac69381de269131f9be06b4 ts=2026-10-07T18:46:24.1180000Z ~ 6ab9a9279a8420a1e6b56b74.jsonl[239] _id=6ac69381de269131f9be06b8 ts=2026-10-07T18:46:24.1250000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6ab9a9279a8420a1e6b56b74.jsonl[7160] _id=6ad15f3dde269131f9e1f998 ts=2026-10-15T23:18:20.8540000Z ~ 6ab9a9279a8420a1e6b56b74.jsonl[7163] _id=6ad15f3dde269131f9e1f99b ts=2026-10-15T23:18:20.8890000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `386ms: 6ab9a9279a8420a1e6b56b74.jsonl[603] _id=6ac69a40de269131f9bf1583 ts=2026-10-07T19:15:11.2560000Z ~ 6ab9a9279a8420a1e6b56b74.jsonl[617] _id=6ac69a40de269131f9bf1590 ts=2026-10-07T19:15:11.6420000Z`; `714ms: 6ab9a9279a8420a1e6b56b74.jsonl[621] _id=6ac69a40de269131f9bf1584 ts=2026-10-07T19:15:11.2860000Z ~ 6ab9a9279a8420a1e6b56b74.jsonl[623] _id=6ac69a41de269131f9bf159b ts=2026-10-07T19:15:12.0000000Z`; `393ms: 6ab9a9279a8420a1e6b56b74.jsonl[755] _id=6ac7e7e0de269131f9c5dacb ts=2026-10-08T18:58:39.9470000Z ~ 6ab9a9279a8420a1e6b56b74.jsonl[757] _id=6ac7e7e0de269131f9c5dae9 ts=2026-10-08T18:58:40.3400000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `652ms: 6ab9a9279a8420a1e6b56b74.jsonl[748] _id=6ac7e7d2de269131f9c5d86f ts=2026-10-08T18:58:25.9120000Z ~ 6ab9a9279a8420a1e6b56b74.jsonl[747] _id=6ac7e7d2de269131f9c5d885 ts=2026-10-08T18:58:26.5640000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 33m 
  - Evidence: 119h 33m: 6ab9a9279a8420a1e6b56b74.jsonl[908] _id=6ac7e939de269131f9c6116a ts=2026-10-08T19:04:25.6700000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2186] _id=6ace7a85de269131f9d0ff8b ts=2026-10-13T18:37:56.8350000Z; 24h 6m: 6ab9a9279a8420a1e6b56b74.jsonl[224] _id=6ac69352de269131f9be00c1 ts=2026-10-07T18:45:36.9380000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[650] _id=6ac7e63ade269131f9c59dd4 ts=2026-10-08T18:51:37.7820000Z; 24h 5m: 6ab9a9279a8420a1e6b56b74.jsonl[2978] _id=6acfcb39de269131f9d71e38 ts=2026-10-14T18:34:32.3660000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[4993] _id=6ad11dffde269131f9df0d83 ts=2026-10-15T18:39:59.2730000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9279a8420a1e6b56b74.jsonl[2183] _id=6ac7ec7bde269131f9c6897a ts=2026-10-08T19:18:19.2060000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2210] _id=6ace7aadde269131f9d1030b ts=2026-10-13T18:38:37.2560000Z; 23h 35m: 6ab9a9279a8420a1e6b56b74.jsonl[4433] _id=6acfd30bde269131f9d81a8a ts=2026-10-14T19:07:54.5620000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[5241] _id=6ad11ee5de269131f9df2c7b ts=2026-10-15T18:43:49.1080000Z; 23h 35m: 6ab9a9279a8420a1e6b56b74.jsonl[644] _id=6ac69aacde269131f9bf1fce ts=2026-10-07T19:16:59.2500000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[668] _id=6ac7e678de269131f9c5a53f ts=2026-10-08T18:52:39.2940000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 290 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[7093] _id=6ad15ebede269131f9e1f741 ts=2026-10-15T23:16:13.8100000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7094] _id=6ad15ebede269131f9e1f742 ts=2026-10-15T23:16:13.8100000Z; 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[7149] _id=6ad15f2cde269131f9e1f957 ts=2026-10-15T23:18:03.1720000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7150] _id=6ad15f2cde269131f9e1f958 ts=2026-10-15T23:18:03.1720000Z; 1ms: 6ab9a9279a8420a1e6b56b74.jsonl[3010] _id=6acfcba1de269131f9d72ba7 ts=2026-10-14T18:36:17.0240000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[3011] _id=6acfcba1de269131f9d72ba8 ts=2026-10-14T18:36:17.0250000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9279a8420a1e6b56b74.jsonl[2154] _id=6ac7ec73de269131f9c68916 ts=2026-10-08T19:18:11.4200000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2192] _id=6ace7a96de269131f9d10143 ts=2026-10-13T18:38:13.1440000Z; 23h 41m: 6ab9a9279a8420a1e6b56b74.jsonl[566] _id=6ac69939de269131f9beff90 ts=2026-10-07T19:10:47.9050000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[656] _id=6ac7e65cde269131f9c5a1ef ts=2026-10-08T18:52:11.9580000Z; 23h 33m: 6ab9a9279a8420a1e6b56b74.jsonl[167] _id=6ac54821de269131f9b77237 ts=2026-10-06T19:12:33.6030000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[223] _id=6ac6935bde269131f9be022c ts=2026-10-07T18:45:46.6530000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 46 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[6459] _id=6ad126a5de269131f9e04198 ts=2026-10-15T19:16:52.9470000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[6460] _id=6ad126a5de269131f9e04199 ts=2026-10-15T19:16:52.9470000Z; 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[6495] _id=6ad15755de269131f9e1dcc2 ts=2026-10-15T22:44:36.4300000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[6496] _id=6ad15755de269131f9e1dcc3 ts=2026-10-15T22:44:36.4300000Z; 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[6496] _id=6ad15755de269131f9e1dcc3 ts=2026-10-15T22:44:36.4300000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[6497] _id=6ad15755de269131f9e1dcc4 ts=2026-10-15T22:44:36.4300000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a9279a8420a1e6b56b74.jsonl[2159] _id=6ac7ec76de269131f9c68936 ts=2026-10-08T19:18:13.7790000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2231] _id=6ace7adade269131f9d10686 ts=2026-10-13T18:39:22.6550000Z; 24h 17m: 6ab9a9279a8420a1e6b56b74.jsonl[2788] _id=6ace7c24de269131f9d11a4c ts=2026-10-13T18:44:52.3760000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[4054] _id=6acfd1b4de269131f9d7ea17 ts=2026-10-14T19:02:11.5790000Z; 23h 57m: 6ab9a9279a8420a1e6b56b74.jsonl[4369] _id=6acfd21cde269131f9d7f83f ts=2026-10-14T19:03:55.4200000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[5825] _id=6ad12302de269131f9dfb414 ts=2026-10-15T19:01:21.9060000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 6ab9a9279a8420a1e6b56b74.jsonl[126] _id=6ac5478ade269131f9b767eb ts=2026-10-06T19:10:02.0220000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[87] _id=6ac5478ade269131f9b767f6 ts=2026-10-06T19:10:02.0260000Z; 7ms: 6ab9a9279a8420a1e6b56b74.jsonl[238] _id=6ac69381de269131f9be06b4 ts=2026-10-07T18:46:24.1180000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[239] _id=6ac69381de269131f9be06b8 ts=2026-10-07T18:46:24.1250000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b74.jsonl[2173] _id=6ac7ec7bde269131f9c6896d ts=2026-10-08T19:18:18.9680000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2191] _id=6ace7a96de269131f9d10142 ts=2026-10-13T18:38:08.1010000Z; 23h 34m: 6ab9a9279a8420a1e6b56b74.jsonl[646] _id=6ac69ab8de269131f9bf206d ts=2026-10-07T19:17:11.2370000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[654] _id=6ac7e654de269131f9c5a102 ts=2026-10-08T18:52:01.6110000Z; 23h 28m: 6ab9a9279a8420a1e6b56b74.jsonl[213] _id=6ac5494ede269131f9b79c33 ts=2026-10-06T19:17:34.3960000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[221] _id=6ac69354de269131f9be0111 ts=2026-10-07T18:45:36.9570000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a9279a8420a1e6b56b74.jsonl[2180] _id=6ac7ec7bde269131f9c68981 ts=2026-10-08T19:18:19.2460000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2255] _id=6ace7b09de269131f9d10955 ts=2026-10-13T18:40:08.7730000Z; 24h 13m: 6ab9a9279a8420a1e6b56b74.jsonl[2771] _id=6ace7bf4de269131f9d117fb ts=2026-10-13T18:44:04.0990000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[3430] _id=6acfd09bde269131f9d7c805 ts=2026-10-14T18:57:29.6640000Z; 23h 25m: 6ab9a9279a8420a1e6b56b74.jsonl[4965] _id=6acfd4a5de269131f9d86031 ts=2026-10-14T19:14:39.3310000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[5008] _id=6ad11e17de269131f9df1027 ts=2026-10-15T18:40:22.2470000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1565 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[1003] _id=6ac7ea99de269131f9c6555a ts=2026-10-08T19:10:17.3290000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[1000] _id=6ac7ea9ade269131f9c65561 ts=2026-10-08T19:10:17.3290000Z; 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[1004] _id=6ac7eaabde269131f9c65778 ts=2026-10-08T19:10:33.0440000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[1060] _id=6ac7eaabde269131f9c65780 ts=2026-10-08T19:10:33.0440000Z; 0ms: 6ab9a9279a8420a1e6b56b74.jsonl[1005] _id=6ac7eaadde269131f9c657cd ts=2026-10-08T19:10:35.8660000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[1064] _id=6ac7eaadde269131f9c657db ts=2026-10-08T19:10:35.8660000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 16m 27s 
  - Evidence: 16m 27s: 6ab9a9279a8420a1e6b56b74.jsonl[7294] _id=6ad16108de269131f9e20222 ts=2026-10-15T23:25:59.3490000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7405] _id=6ad164e4de269131f9e20ec6 ts=2026-10-15T23:42:27.2350000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a9279a8420a1e6b56b74.jsonl[1095] _id=6ac7eaf8de269131f9c65f42 ts=2026-10-08T19:11:52.5510000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2258] _id=6ace7b3ade269131f9d10bf7 ts=2026-10-13T18:40:57.9160000Z; 23h 56m: 6ab9a9279a8420a1e6b56b74.jsonl[2331] _id=6ace7b4cde269131f9d10cd1 ts=2026-10-13T18:41:16.4670000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[3042] _id=6acfcc11de269131f9d73993 ts=2026-10-14T18:38:08.7010000Z; 23h 49m: 6ab9a9279a8420a1e6b56b74.jsonl[3324] _id=6acfcfeede269131f9d7b493 ts=2026-10-14T18:54:37.4540000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[5240] _id=6ad11edcde269131f9df2a5b ts=2026-10-15T18:43:40.0080000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.039s shown 
  - Evidence: 21ms: 6ab9a9279a8420a1e6b56b74.jsonl[3045] _id=6acfcc22de269131f9d73c60 ts=2026-10-14T18:38:26.1500000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[3049] _id=6acfcc22de269131f9d73c64 ts=2026-10-14T18:38:26.1710000Z; 39ms: 6ab9a9279a8420a1e6b56b74.jsonl[3050] _id=6acfcc22de269131f9d73c57 ts=2026-10-14T18:38:26.1110000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[3045] _id=6acfcc22de269131f9d73c60 ts=2026-10-14T18:38:26.1500000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 172h 14m 
  - Evidence: 172h 14m: 6ab9a9279a8420a1e6b56b74.jsonl[789] _id=6ac7e813de269131f9c5e11c ts=2026-10-08T18:59:31.1380000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7076] _id=6ad15e31de269131f9e1f4b8 ts=2026-10-15T23:13:52.5230000Z; 23h 39m: 6ab9a9279a8420a1e6b56b74.jsonl[628] _id=6ac69a4fde269131f9bf16e6 ts=2026-10-07T19:15:26.8970000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[708] _id=6ac7e6efde269131f9c5b312 ts=2026-10-08T18:54:39.3460000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 172h 11m 
  - Evidence: 172h 11m: 6ab9a9279a8420a1e6b56b74.jsonl[790] _id=6ac7e813de269131f9c5e120 ts=2026-10-08T18:59:31.1680000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7014] _id=6ad15da1de269131f9e1f29a ts=2026-10-15T23:11:28.1280000Z; 23h 37m: 6ab9a9279a8420a1e6b56b74.jsonl[641] _id=6ac69a95de269131f9bf1e3d ts=2026-10-07T19:16:36.3180000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[696] _id=6ac7e6dede269131f9c5b0fb ts=2026-10-08T18:54:21.6710000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.035s..0.035s shown 
  - Evidence: 35ms: 6ab9a9279a8420a1e6b56b74.jsonl[7160] _id=6ad15f3dde269131f9e1f998 ts=2026-10-15T23:18:20.8540000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7163] _id=6ad15f3dde269131f9e1f99b ts=2026-10-15T23:18:20.8890000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 172h 12m 
  - Evidence: 172h 12m: 6ab9a9279a8420a1e6b56b74.jsonl[788] _id=6ac7e80ede269131f9c5e092 ts=2026-10-08T18:59:25.4310000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7022] _id=6ad15dbade269131f9e1f2d0 ts=2026-10-15T23:11:53.0990000Z; 23h 37m: 6ab9a9279a8420a1e6b56b74.jsonl[631] _id=6ac69a4cde269131f9bf1695 ts=2026-10-07T19:15:22.8610000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[683] _id=6ac7e699de269131f9c5a900 ts=2026-10-08T18:53:13.7820000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.020s..0.031s shown 
  - Evidence: 20ms: 6ab9a9279a8420a1e6b56b74.jsonl[701] _id=6ac7e6e3de269131f9c5b164 ts=2026-10-08T18:54:26.7490000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[702] _id=6ac7e6e3de269131f9c5b165 ts=2026-10-08T18:54:26.7690000Z; 30ms: 6ab9a9279a8420a1e6b56b74.jsonl[603] _id=6ac69a40de269131f9bf1583 ts=2026-10-07T19:15:11.2560000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[621] _id=6ac69a40de269131f9bf1584 ts=2026-10-07T19:15:11.2860000Z; 31ms: 6ab9a9279a8420a1e6b56b74.jsonl[619] _id=6ac69a48de269131f9bf1647 ts=2026-10-07T19:15:19.5070000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[620] _id=6ac69a48de269131f9bf1648 ts=2026-10-07T19:15:19.5380000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 172h 13m 
  - Evidence: 172h 13m: 6ab9a9279a8420a1e6b56b74.jsonl[752] _id=6ac7e7d5de269131f9c5d90e ts=2026-10-08T18:58:29.4030000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[7017] _id=6ad15dabde269131f9e1f2ae ts=2026-10-15T23:11:38.5800000Z; 23h 39m: 6ab9a9279a8420a1e6b56b74.jsonl[600] _id=6ac69a36de269131f9bf1484 ts=2026-10-07T19:15:01.6090000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[693] _id=6ac7e6d9de269131f9c5b076 ts=2026-10-08T18:54:17.6460000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 33m 
  - Evidence: 119h 33m: 6ab9a9279a8420a1e6b56b74.jsonl[907] _id=6ac7e930de269131f9c60f20 ts=2026-10-08T19:04:15.9940000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2188] _id=6ace7a85de269131f9d0ff8d ts=2026-10-13T18:37:57.1530000Z; 24h 7m: 6ab9a9279a8420a1e6b56b74.jsonl[219] _id=6ac69300de269131f9bdf631 ts=2026-10-07T18:44:14.8300000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[652] _id=6ac7e63ade269131f9c59dd6 ts=2026-10-08T18:51:37.9180000Z; 24h 5m: 6ab9a9279a8420a1e6b56b74.jsonl[2976] _id=6acfcb2cde269131f9d71cd2 ts=2026-10-14T18:34:20.2310000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[4992] _id=6ad11dffde269131f9df0d88 ts=2026-10-15T18:39:59.4430000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 33m 
  - Evidence: 119h 33m: 6ab9a9279a8420a1e6b56b74.jsonl[906] _id=6ac7e930de269131f9c60f1f ts=2026-10-08T19:04:15.9940000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2187] _id=6ace7a85de269131f9d0ff8c ts=2026-10-13T18:37:57.1530000Z; 24h 7m: 6ab9a9279a8420a1e6b56b74.jsonl[218] _id=6ac69300de269131f9bdf630 ts=2026-10-07T18:44:14.8300000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[651] _id=6ac7e63ade269131f9c59dd5 ts=2026-10-08T18:51:37.9180000Z; 24h 5m: 6ab9a9279a8420a1e6b56b74.jsonl[2975] _id=6acfcb2cde269131f9d71cd1 ts=2026-10-14T18:34:20.2310000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[4991] _id=6ad11dffde269131f9df0d87 ts=2026-10-15T18:39:59.4420000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6ab9a9279a8420a1e6b56b74.jsonl[2189] _id=6ace7a85de269131f9d0ff85 ts=2026-10-08T19:18:21.284Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2929] _id=6ace7ef8de269131f9d133e7 ts=2026-10-13T18:56:55.9650000Z; 47h 54m: 6ab9a9279a8420a1e6b56b74.jsonl[2929] _id=6ace7ef8de269131f9d133e7 ts=2026-10-13T18:56:55.9650000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[5689] _id=6ad120c6de269131f9df686e ts=2026-10-15T18:51:49.6050000Z; 24h 1m: 6ab9a9279a8420a1e6b56b74.jsonl[648] _id=6ac7e63ade269131f9c59dd1 ts=2026-10-07T19:17:15.695Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2189] _id=6ace7a85de269131f9d0ff85 ts=2026-10-08T19:18:21.284Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a9279a8420a1e6b56b74.jsonl[929] _id=6ac7e998de269131f9c6267f ts=2026-10-08T19:06:00.0080000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[2194] _id=6ace7a96de269131f9d10145 ts=2026-10-13T18:38:13.1850000Z; 23h 41m: 6ab9a9279a8420a1e6b56b74.jsonl[576] _id=6ac6993fde269131f9beffeb ts=2026-10-07T19:10:54.0060000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[655] _id=6ac7e654de269131f9c5a103 ts=2026-10-08T18:52:03.3360000Z; 23h 36m: 6ab9a9279a8420a1e6b56b74.jsonl[4387] _id=6acfd22ede269131f9d7f9f7 ts=2026-10-14T19:04:13.7660000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[5000] _id=6ad11e16de269131f9df1019 ts=2026-10-15T18:40:21.7410000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.008s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b74.jsonl[575] _id=6ac6993fde269131f9beffea ts=2026-10-07T19:10:54.0050000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[576] _id=6ac6993fde269131f9beffeb ts=2026-10-07T19:10:54.0060000Z; 1ms: 6ab9a9279a8420a1e6b56b74.jsonl[670] _id=6ac7e678de269131f9c5a541 ts=2026-10-08T18:52:39.3120000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[671] _id=6ac7e678de269131f9c5a542 ts=2026-10-08T18:52:39.3130000Z; 8ms: 6ab9a9279a8420a1e6b56b74.jsonl[322] _id=6ac69541de269131f9be5bfe ts=2026-10-07T18:53:52.7880000Z -> 6ab9a9279a8420a1e6b56b74.jsonl[324] _id=6ac69541de269131f9be5c0f ts=2026-10-07T18:53:52.7960000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[559] _id=6ac69913de269131f9befcb6 ts=2026-10-07T19:10:10.6120000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[3200] _id=6acfce58de269131f9d78e4d ts=2026-10-14T18:47:51.2720000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[4433] _id=6acfd30bde269131f9d81a8a ts=2026-10-14T19:07:54.5620000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[7163] _id=6ad15f3dde269131f9e1f99b ts=2026-10-15T23:18:20.8890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[2945] _id=6ace8376de269131f9d1b513 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 162 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[3665] _id=6acfd154de269131f9d7dcc6 ts=2026-10-14T19:00:33.8150000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[3667] _id=6acfd155de269131f9d7dce8 ts=2026-10-14T19:00:33.9660000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[3693] _id=6acfd159de269131f9d7dd5f ts=2026-10-14T19:00:36.0610000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 508 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[999] _id=6ac7ea9cde269131f9c655b1 ts=2026-10-08T19:10:18.0160000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[1007] _id=6ac7ea9cde269131f9c655b2 ts=2026-10-08T19:10:18.1910000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[1008] _id=6ac7ea9cde269131f9c655b3 ts=2026-10-08T19:10:18.2850000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 12 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[5807] _id=6ad122e3de269131f9dfafbc ts=2026-10-15T19:00:50.3960000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[5830] _id=6ad12390de269131f9dfc957 ts=2026-10-15T19:03:43.0490000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[6176] _id=6ad125dfde269131f9e0277a ts=2026-10-15T19:13:34.9740000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[747] _id=6ac7e7d2de269131f9c5d885 ts=2026-10-08T18:58:26.5640000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[751] _id=6ac7e7d4de269131f9c5d8df ts=2026-10-08T18:58:28.0730000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[7034] _id=6ad15dc3de269131f9e1f2ef ts=2026-10-15T23:12:03.0260000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'DialogueStartEvent' (totals: 206 start, 199 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 15 unmatched 'BecameCameraCentered' (totals: 588 open, 573 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 46 unmatched 'BecameVisible' (totals: 1177 open, 1131 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 25 open, 24 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationToolOpen' (totals: 9 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 30 start, 16 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 273 of 8644 adjacent _id pairs reverse in client time; worst 161.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b74.jsonl[1121] _id=6ac7eb2dde269131f9c664e3 ts=2026-10-08T19:12:45.1090000Z`; `6ab9a9279a8420a1e6b56b74.jsonl[1122] _id=6ac7eb2ede269131f9c664fa ts=2026-10-08T19:10:03.7950000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.96s, min -429575.87s, max -0.20s over 8645 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b74\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `TerasGardenBox` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **NOT_TESTED / NotTested** `soilMachine` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3469 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3147); Unit 3 Dungeon Dev (322)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.72s, n=3468)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3469/3469 records)
    "BecameVisible"  x1177
    "BecameInvisible"  x1131
    "BecameCameraCentered"  x588
    "BecameCameraUncentered"  x573
data.pieceId  (string, 3469/3469 records)
    24 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3469/3469 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 1918 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (837); Unit 2 Prod (Refactor) (657); Unit 3 Dungeon Dev (242); Unit 1 Dev (182)
- **Intervals:** median 1.33s (p5 0.12s / p95 19.97s, n=1917)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1918/1918 records)
    "pressed"  x1918
data.actionType  (string, 1918/1918 records)
    "Move"  x1517
    "Interact"  x218
    "Jump"  x100
    "Hoverboard"  x21
    "Sprint"  x21
    "Ascend"  x18
    "Descend"  x11
    "Map"  x8
    "SkipCinematic"  x4
data.key  (string, 1918/1918 records, 11 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1918/1918 records)
    "Player"  x1225
    "Drone"  x693
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1657 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (545); Unit 2 Prod (Refactor) (510); Unit 1 Dev (343); Unit 3 Dungeon Dev (259)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.11s, n=1652)
- **Fields under `data`:**

```text
data.position  (object, 1657/1657 records)
data.position.x  (number, 1657/1657 records)
    numeric range -692.93 .. 2054.32 (469 unique)
data.position.y  (number, 1657/1657 records)
    numeric range -115.127 .. 175.274 (317 unique)
data.position.z  (number, 1657/1657 records)
    numeric range -1080.45 .. 2171.6 (468 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1089 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (367); Unit 2 Prod (Refactor) (319); Unit 1 Dev (257); Unit 3 Dungeon Dev (146)
- **eventKey:** present on 684 of 1089 records
- **Intervals:** median 4.78s (p5 0.00s / p95 55.10s, n=1088)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x684; [conversationId, dialogueEventType] x405
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1089/1089 records)
    numeric range 10 .. 84 (30 unique)
data.dialogueEventType  (string, 1089/1089 records)
    "DialogueNodeEvent"  x684
    "DialogueStartEvent"  x206
    "DialogueFinishEvent"  x199
data.nodeId  (number, 684/1089 records)
    numeric range 0 .. 289 (203 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 138 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (81); Unit 1 Dev (57)
- **Intervals:** median 0.74s (p5 0.04s / p95 24.34s, n=137)
- **Fields under `data`:**

```text
data.actionType  (string, 138/138 records)
    "argumentationNodeHoverEnd"  x59
    "argumentationNodeHoverStart"  x59
    "argumentationNodeAdd"  x16
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 138/138 records)
    "Unit 3 - Pollution Upstream"  x81
    "Unit 1 - Freshwater"  x33
    "Unit 1 - Argumentation Tutorial"  x24
data.nodeName  (string, 138/138 records)
    "A"  x32
    "1"  x27
    "I"  x26
    "3"  x18
    "4"  x12
    "2"  x8
    "II"  x8
    "5"  x5
    "B"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 103 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (44); Unit 3 Dungeon Dev (34); Unit 1 Dev (14); Unit 3 Dev (11)
- **Intervals:** median 15.15s (p5 4.72s / p95 63672.87s, n=102)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 103/103 records)
    18 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 103/103 records)
    43 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 88 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (45); Unit 2 Prod (Refactor) (43)
- **Intervals:** median 5.88s (p5 0.78s / p95 827.80s, n=87)
- **`data` key-set variants:** [actionType, featureUsed] x49; [actionType, featureUsed, location] x39
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 88/88 records)
    "WaypointMoveEvent"  x33
    "MapOpenEvent"  x25
    "MapCloseEvent"  x24
    "WaypointSetEvent"  x6
data.featureUsed  (string, 88/88 records)
    "Map"  x49
    "Waypoint"  x39
data.location  (object, 39/88 records)
data.location.x  (number, 39/88 records)
    numeric range -274.422 .. 543.815 (31 unique)
data.location.y  (number, 39/88 records)
    numeric range -360.342 .. 277.94 (37 unique)
data.location.z  (number, 39/88 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 46 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (18); Unit 2 Prod (Refactor) (15); Unit 3 Dev (10); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 46 of 46 records
- **Intervals:** median 289.25s (p5 0.01s / p95 84940.80s, n=45)
- **`data` key-set variants:** [questEventType, questID, questName] x30; [questEventType, questID, questName, questSuccessOrFailure] x16
- **Fields under `data`:**

```text
data.questEventType  (string, 46/46 records)
    "questActiveEvent"  x30
    "questFinishEvent"  x16
data.questID  (string, 46/46 records)
    14 unique values (see csv/event_unique_values.csv)
data.questName  (string, 46/46 records)
    14 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 16/46 records)
    "Succeeded"  x16
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 31 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (14); Unit 2 Prod (Refactor) (9); Unit 1 Dev (3); Unit 3 Dev (3); Unit 3 Dungeon Dev (2)
- **Intervals:** median 86.25s (p5 8.70s / p95 86745.57s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "DebugMenuStateChanged"  x31
data.isOpened  (bool, 31/31 records)
    false  x31
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `Soil Key Puzzle` — 26 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (26)
- **Intervals:** median 2.25s (p5 0.78s / p95 18.00s, n=25)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x24; [Soil Key Puzzle Status, Unit] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 2/26 records)
    "Finished"  x1
    "Started"  x1
data.Unit  (string, 2/26 records)
    "Unit 3 Dev"  x2
data.actionType  (string, 24/26 records)
    "RightDrag"  x13
    "LeftDrag"  x11
data.currentSoilType  (string, 24/26 records)
    "CLAY"  x5
    "CLAYSAND"  x5
    "SAND"  x4
    "SANDGRAVEL"  x4
    "CLAYROCK"  x3
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 24/26 records)
    "false"  x19
    "true"  x5
data.waterLevelStatus  (string, 24/26 records)
    "TooLow"  x16
    "TooHigh"  x7
    "Proper"  x1
data.waterRetentionChange  (string, 24/26 records)
    "Decrease"  x15
    "NoChange"  x5
    "Increase"  x4
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 16 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 3 Dev (1)
- **Intervals:** median 3483.32s (p5 99.06s / p95 189916.51s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 8050.89s (p5 98.27s / p95 207095.41s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 13 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (4)
- **Intervals:** median 7.21s (p5 0.42s / p95 325830.95s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 13/13 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 10 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (10)
- **Intervals:** median 2.02s (p5 0.50s / p95 5.20s, n=9)
- **`data` key-set variants:** [actionType, chatID] x6; [actionKey, chatID] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 4/10 records)
    "ScrollStop"  x4
data.actionType  (string, 6/10 records)
    "ScrollStart"  x4
    "Close"  x1
    "Open"  x1
data.chatID  (string, 10/10 records)
    "NA"  x5
    "[19-0, 19-1, 19-49, 19-2, 19-59, 19-50, 19-51]"  x2
    "[23-73, 23-22, 23-24, 23-25, 23-27]"  x2
    "[22-5, 22-50, 22-11, 22-12, 22-13]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (6); Unit 3 Dev (3)
- **Intervals:** median 147.61s (p5 10.31s / p95 432718.90s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationAnswerEvent` — 8 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (5); Unit 1 Dev (3)
- **Intervals:** median 141.27s (p5 10.44s / p95 459588.70s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "submitAnswerEvent"  x8
data.answerSubmitted  (string, 8/8 records)
    "A,1,I"  x6
    "A,3,I"  x1
    "A,5,I"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 6 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 1 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 86465.59s (p5 30483.21s / p95 379070.47s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 6/6 records)
    false  x6
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 3.17s (p5 3.17s / p95 3.17s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "1"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit2"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (33x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (39x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*