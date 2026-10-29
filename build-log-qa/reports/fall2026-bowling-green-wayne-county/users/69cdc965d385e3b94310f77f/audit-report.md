# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77f
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f77f.jsonl
- **Records:** 970 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f77f
- **Time span:** 2026-04-20T13:42:39.846000+00:00 .. 2026-04-28T14:24:30.698000+00:00 (192h 41m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **9 event types**, 970 records, 3 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 47 INFO, 5 NOT_TESTED, 30 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 568 | 58.56 | 1 | 3 | 425 | 2026-04-20T13:42:58.529000+00:00 | 2026-04-28T14:22:07.212000+00:00 | 192h 39m |
| PlayerPositionEvent | 327 | 33.71 | 1 | 3 | 0 | 2026-04-20T13:42:39.846000+00:00 | 2026-04-28T14:24:30.698000+00:00 | 192h 41m |
| questEvent | 29 | 2.99 | 1 | 3 | 29 | 2026-04-20T13:42:58.505000+00:00 | 2026-04-28T14:21:03.687000+00:00 | 192h 38m |
| Topographic Map Event | 16 | 1.65 | 1 | 2 | 0 | 2026-04-22T13:45:34.951000+00:00 | 2026-04-28T14:24:11.612000+00:00 | 144h 38m |
| TopographicMapEvent | 12 | 1.24 | 1 | 1 | 0 | 2026-04-22T13:45:49.991000+00:00 | 2026-04-22T14:26:56.128000+00:00 | 41m 6s |
| argumentationNodeEvent | 11 | 1.13 | 1 | 1 | 0 | 2026-04-20T14:02:05.910000+00:00 | 2026-04-20T14:03:02.955000+00:00 | 57.0s |
| argumentationEvent | 4 | 0.41 | 1 | 1 | 0 | 2026-04-20T14:01:30.280000+00:00 | 2026-04-20T14:03:04.473000+00:00 | 1m 34s |
| Soil Key Puzzle | 2 | 0.21 | 1 | 1 | 0 | 2026-04-24T14:15:57.711000+00:00 | 2026-04-24T14:22:51.646000+00:00 | 6m 53s |
| EndOfUnit | 1 | 0.1 | 1 | 1 | 0 | 2026-04-20T14:21:52.465000+00:00 | 2026-04-20T14:21:52.465000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.002s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 413.935s median 
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
  - Observed: 12.9s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 28.896s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 3.718s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 6 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowFocusEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 82 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowUnfocusEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 76 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DialogueEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 568 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 327 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Soil Key Puzzle Status` — baseline categorical value(s) not seen this build. 
  - Observed: Finished 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 16 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 12 records 
  - Expected: 83 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: MapCloseEvent; MapOpenEvent; Selected; Unselected; WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: dragEnd; dragStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend; Map; Waypoint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — categorical value(s) not seen in baseline. 
  - Observed: waypoint 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 4 records 
  - Expected: 14 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f77f.jsonl[40] _id=69e632191724f0c9e2f88819 ts=2026-04-20T14:03:04.4980000Z`; `69cdc965d385e3b94310f77f.jsonl[650] _id=69e8d2111724f0c9e2fa3f5b ts=2026-04-22T13:50:08.4190000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 16 records, TopographicMapEvent: 12 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 567 | 0.003 | 2.047 | 1223.19 | 69.831 | 344041.601 | 0.05 | 129 | 5 |
| PlayerPositionEvent | 324 | 0.0 | 30.002 | 2140.826 | 35.014 | 343997.194 | 0.03 | 1 | 3 |
| questEvent | 28 | 0.003 | 193.488 | 24767.328 | 172173.504 | 344332.118 | 0.0 | 3 | 6 |
| Topographic Map Event | 15 | 5.422 | 33.349 | 34714.444 | 156542.85 | 518148.257 | 0.0 | 0 | 2 |
| TopographicMapEvent | 11 | 0.43 | 12.9 | 224.194 | 997.794 | 1689.77 | 0.27 | 0 | 1 |
| argumentationNodeEvent | 10 | 1.784 | 3.718 | 5.705 | 15.15 | 16.209 | 10.52 | 0 | 0 |
| argumentationEvent | 3 | 1.498 | 28.896 | 31.398 | 60.309 | 63.799 | 1.91 | 0 | 0 |
| Soil Key Puzzle | 1 | 413.935 | 413.935 | 413.935 | 413.935 | 413.935 | 0.14 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.002s (p5 29.96s, p95 35.01s, n=324) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 34m 
  - Evidence: 95h 34m: 69cdc965d385e3b94310f77f.jsonl[914] _id=69eb7f821724f0c9e2fba319 ts=2026-04-24T14:34:42.8320000Z -> 69cdc965d385e3b94310f77f.jsonl[917] _id=69f0bf6c1724f0c9e2fca9b3 ts=2026-04-28T14:08:44.4330000Z; 47h 40m: 69cdc965d385e3b94310f77f.jsonl[763] _id=69e8da081724f0c9e2fa6d6f ts=2026-04-22T14:24:06.8640000Z -> 69cdc965d385e3b94310f77f.jsonl[779] _id=69eb78901724f0c9e2fb8071 ts=2026-04-24T14:05:03.5580000Z; 46h 44m: 69cdc965d385e3b94310f77f.jsonl[451] _id=69e639031724f0c9e2f8af15 ts=2026-04-20T14:32:34.8410000Z -> 69cdc965d385e3b94310f77f.jsonl[461] _id=69e8ca6e1724f0c9e2fa0cb5 ts=2026-04-22T13:17:32.9690000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 129 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f77f.jsonl[350] _id=69e6326a1724f0c9e2f889dd ts=2026-04-20T14:04:25.7780000Z -> 69cdc965d385e3b94310f77f.jsonl[352] _id=69e6326a1724f0c9e2f889df ts=2026-04-20T14:04:25.7810000Z; 3ms: 69cdc965d385e3b94310f77f.jsonl[386] _id=69e6362b1724f0c9e2f8a09b ts=2026-04-20T14:20:27.1090000Z -> 69cdc965d385e3b94310f77f.jsonl[387] _id=69e6362b1724f0c9e2f8a09d ts=2026-04-20T14:20:27.1120000Z; 3ms: 69cdc965d385e3b94310f77f.jsonl[536] _id=69e8cede1724f0c9e2fa27b6 ts=2026-04-22T13:36:28.9240000Z -> 69cdc965d385e3b94310f77f.jsonl[537] _id=69e8cede1724f0c9e2fa27bb ts=2026-04-22T13:36:28.9270000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc965d385e3b94310f77f.jsonl[911] _id=69eb7f7c1724f0c9e2fba2e9 ts=2026-04-24T14:34:36.3610000Z -> 69cdc965d385e3b94310f77f.jsonl[110] _id=69f0bf391724f0c9e2fca997 ts=2026-04-28T14:07:53.5550000Z; 47h 37m: 69cdc965d385e3b94310f77f.jsonl[775] _id=69e8dae51724f0c9e2fa7295 ts=2026-04-22T14:27:48.5880000Z -> 69cdc965d385e3b94310f77f.jsonl[778] _id=69eb788f1724f0c9e2fb8065 ts=2026-04-24T14:05:03.1230000Z; 46h 42m: 69cdc965d385e3b94310f77f.jsonl[57] _id=69e8ca511724f0c9e2fa0c3d ts=2026-04-20T14:34:58.365Z -> 69cdc965d385e3b94310f77f.jsonl[459] _id=69e8ca6a1724f0c9e2fa0ca5 ts=2026-04-22T13:17:28.9470000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77f.jsonl[453] _id=69e639381724f0c9e2f8b125 ts=2026-04-20T14:33:28.3970000Z -> 69cdc965d385e3b94310f77f.jsonl[458] _id=69e8ca511724f0c9e2fa0c37 ts=2026-04-20T14:33:28.397Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 55m 
  - Evidence: 143h 55m: 69cdc965d385e3b94310f77f.jsonl[773] _id=69e8dab21724f0c9e2fa715f ts=2026-04-22T14:26:57.4860000Z -> 69cdc965d385e3b94310f77f.jsonl[969] _id=69f0c2b51724f0c9e2fcae31 ts=2026-04-28T14:22:45.7430000Z; 26m 9s: 69cdc965d385e3b94310f77f.jsonl[679] _id=69e8d3651724f0c9e2fa444f ts=2026-04-22T13:55:48.0180000Z -> 69cdc965d385e3b94310f77f.jsonl[751] _id=69e8d9861724f0c9e2fa6b21 ts=2026-04-22T14:21:57.1220000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 28m 9s 
  - Evidence: 28m 9s: 69cdc965d385e3b94310f77f.jsonl[678] _id=69e8d3651724f0c9e2fa444b ts=2026-04-22T13:55:47.9370000Z -> 69cdc965d385e3b94310f77f.jsonl[760] _id=69e8d9ff1724f0c9e2fa6d49 ts=2026-04-22T14:23:57.7070000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 69cdc965d385e3b94310f77f.jsonl[102] _id=69eb7e301724f0c9e2fb9ba3 ts=2026-04-24T14:29:04.1150000Z -> 69cdc965d385e3b94310f77f.jsonl[111] _id=69f0bf3d1724f0c9e2fca999 ts=2026-04-28T14:07:56.2330000Z; 48h 19m: 69cdc965d385e3b94310f77f.jsonl[604] _id=69e8d0fe1724f0c9e2fa3839 ts=2026-04-22T13:45:32.7920000Z -> 69cdc965d385e3b94310f77f.jsonl[781] _id=69eb78911724f0c9e2fb8075 ts=2026-04-24T14:05:03.7280000Z; 46h 53m: 69cdc965d385e3b94310f77f.jsonl[421] _id=69e636e91724f0c9e2f8a62f ts=2026-04-20T14:23:36.1020000Z -> 69cdc965d385e3b94310f77f.jsonl[460] _id=69e8ca6d1724f0c9e2fa0cad ts=2026-04-22T13:17:31.5170000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.003s..0.019s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f77f.jsonl[296] _id=69e631a21724f0c9e2f884fb ts=2026-04-20T14:01:06.0760000Z -> 69cdc965d385e3b94310f77f.jsonl[297] _id=69e631a21724f0c9e2f88503 ts=2026-04-20T14:01:06.0790000Z; 15ms: 69cdc965d385e3b94310f77f.jsonl[15] _id=69e62f091724f0c9e2f87711 ts=2026-04-20T13:50:01.0560000Z -> 69cdc965d385e3b94310f77f.jsonl[198] _id=69e62f091724f0c9e2f87715 ts=2026-04-20T13:50:01.0710000Z; 19ms: 69cdc965d385e3b94310f77f.jsonl[238] _id=69e62fd21724f0c9e2f87b31 ts=2026-04-20T13:53:22.1990000Z -> 69cdc965d385e3b94310f77f.jsonl[239] _id=69e62fd31724f0c9e2f87b33 ts=2026-04-20T13:53:22.2180000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 12 record(s) match the trigger in 69cdc965d385e3b94310f77f.jsonl:69cdc965d385e3b94310f77f, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f77f.jsonl[615] _id=69e8d10f1724f0c9e2fa38b9 ts=2026-04-22T13:45:49.9910000Z`; `69cdc965d385e3b94310f77f.jsonl[612] _id=69e8d1101724f0c9e2fa38bb ts=2026-04-22T13:45:50.7730000Z`; `69cdc965d385e3b94310f77f.jsonl[652] _id=69e8d22f1724f0c9e2fa3fbf ts=2026-04-22T13:50:38.0980000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f77f.jsonl[121] _id=69f0bf941724f0c9e2fcaa1d ts=2026-04-28T14:09:23.7370000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f77f.jsonl[844] _id=69eb7cbc1724f0c9e2fb94db ts=2026-04-24T14:22:51.6460000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 52 unmatched 'DialogueStartEvent' (totals: 97 start, 46 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 2 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 19 start, 10 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.62s, min -168217.01s, max -0.05s over 970 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77f\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=partial, Unit4=skipped 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 16 records 
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

### `DialogueEvent` — 568 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (239); Unit 1 Dev (196); Unit 3 Dev (133)
- **eventKey:** present on 425 of 568 records
- **Intervals:** median 2.05s (p5 0.01s / p95 69.83s, n=567)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x425; [conversationId, dialogueEventType] x143
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 568/568 records)
    numeric range 10 .. 101 (20 unique)
data.dialogueEventType  (string, 568/568 records)
    "DialogueNodeEvent"  x425
    "DialogueStartEvent"  x97
    "DialogueFinishEvent"  x46
data.nodeId  (number, 425/568 records)
    numeric range 0 .. 289 (128 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 327 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (201); Unit 1 Dev (79); Unit 3 Dev (47)
- **Intervals:** median 30.00s (p5 29.96s / p95 35.01s, n=324)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 327/327 records)
data.position.x  (number, 327/327 records)
    numeric range -24.9555 .. 1885.36 (190 unique)
data.position.y  (number, 327/327 records)
    numeric range -114.388 .. 156.453 (147 unique)
data.position.z  (number, 327/327 records)
    numeric range -388.238 .. 2299.77 (190 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 29 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (10); Unit 3 Dev (7)
- **eventKey:** present on 29 of 29 records
- **Intervals:** median 193.49s (p5 0.02s / p95 172173.50s, n=28)
- **`data` key-set variants:** [questEventType, questID, questName] x19; [questEventType, questID, questName, questSuccessOrFailure] x10
- **Fields under `data`:**

```text
data.questEventType  (string, 29/29 records)
    "questActiveEvent"  x19
    "questFinishEvent"  x10
data.questID  (string, 29/29 records)
    "16"  x5
    "21"  x3
    "22"  x3
    "17"  x2
    "23"  x2
    "24"  x2
    "28"  x2
    "29"  x2
    "31"  x2
    "32"  x2
    "33"  x2
    "34"  x2
data.questName  (string, 29/29 records)
    "Supply Run"  x5
    "Escape the Ruin"  x3
    "Getting the Band Back Together"  x3
    "Defend the Expedition"  x2
    "Foraged Forging"  x2
    "Gear Up"  x2
    "Getting Your Space Legs"  x2
    "Info and Intros"  x2
    "Investigate the Temple"  x2
    "Pollution Solution"  x2
    "TK, Reporting In!"  x2
    "What Was That?"  x2
data.questSuccessOrFailure  (string, 10/29 records)
    "Succeeded"  x10
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 16 records

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (2)
- **Intervals:** median 33.35s (p5 6.89s / p95 156542.85s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "MapCloseEvent"  x8
    "MapOpenEvent"  x8
data.featureUsed  (string, 16/16 records)
    "Map"  x16
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 12 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (12)
- **Intervals:** median 12.90s (p5 0.61s / p95 997.79s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "dragEnd"  x6
    "dragStart"  x6
data.featureUsed  (string, 12/12 records)
    "waypoint"  x12
data.location  (object, 12/12 records)
data.location.x  (number, 12/12 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 12/12 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 12/12 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 11 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (11)
- **Intervals:** median 3.72s (p5 2.05s / p95 15.15s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationNodeAdd"  x7
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 11/11 records)
    "Unit 1 - Freshwater"  x11
data.nodeName  (string, 11/11 records)
    "1"  x3
    "B"  x3
    "I"  x3
    "A"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 4 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 28.90s (p5 4.24s / p95 60.31s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationSessionClose"  x2
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 4/4 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 2 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 413.94s (p5 413.94s / p95 413.94s, n=1)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 2/2 records)
    "Started"  x2
data.Unit  (string, 2/2 records)
    "Unit 2 Prod (Refactor)"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "1"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DEBUGMenu` : expected event type absent although its content was played — possible logging failure
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : expected event type absent although its content was played — possible logging failure
- `ObjectInterEvent` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now
- `InputEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (6x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*