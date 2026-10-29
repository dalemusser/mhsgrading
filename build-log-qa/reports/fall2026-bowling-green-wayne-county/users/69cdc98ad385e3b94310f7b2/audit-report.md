# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b2

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b2
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7b2.jsonl
- **Records:** 1924 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7b2
- **Time span:** 2026-04-14T19:37:30.677000+00:00 .. 2026-04-22T20:04:24.704000+00:00 (192h 26m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b2\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 1924 records, 4 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 45 INFO, 5 NOT_TESTED, 30 PASS.
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
| DialogueEvent | 1181 | 61.38 | 1 | 4 | 816 | 2026-04-14T19:37:48.960000+00:00 | 2026-04-22T20:04:24.704000+00:00 | 192h 26m |
| PlayerPositionEvent | 494 | 25.68 | 1 | 4 | 0 | 2026-04-14T19:37:30.677000+00:00 | 2026-04-22T20:04:13.168000+00:00 | 192h 26m |
| TopographicMapEvent | 84 | 4.37 | 1 | 2 | 0 | 2026-04-16T19:53:45.819000+00:00 | 2026-04-22T19:25:34.622000+00:00 | 143h 31m |
| argumentationNodeEvent | 63 | 3.27 | 1 | 2 | 0 | 2026-04-14T20:06:08.572000+00:00 | 2026-04-22T19:18:50.223000+00:00 | 191h 12m |
| questEvent | 43 | 2.23 | 1 | 4 | 43 | 2026-04-14T19:37:48.945000+00:00 | 2026-04-22T20:03:47.785000+00:00 | 192h 25m |
| Topographic Map Event | 40 | 2.08 | 1 | 2 | 0 | 2026-04-16T19:53:32.684000+00:00 | 2026-04-22T19:26:26.253000+00:00 | 143h 32m |
| argumentationEvent | 10 | 0.52 | 1 | 2 | 0 | 2026-04-14T20:05:47.496000+00:00 | 2026-04-22T19:18:51.996000+00:00 | 191h 13m |
| Soil Key Puzzle | 6 | 0.31 | 1 | 2 | 0 | 2026-04-16T19:22:27.268000+00:00 | 2026-04-22T19:29:54.971000+00:00 | 144h 7m |
| crash | 2 | 0.1 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 1 | 0.05 | 1 | 1 | 0 | 2026-04-16T19:00:29.698000+00:00 | 2026-04-16T19:00:29.698000+00:00 | 0.0s |

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
  - Observed: 30.007s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 71.806s median 
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
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.946s median 
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
  - Observed: MainMenu; Transition; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 40 records this build 
  - Expected: new logging or newly exercised content — review
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
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 24; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7b2.jsonl[1065] _id=69e130c91724f0c9e2f69380 ts=2026-04-16T18:56:08.1650000Z`; `69cdc98ad385e3b94310f7b2.jsonl[322] _id=69e13d171724f0c9e2f6ffcc ts=2026-04-16T19:48:38.2560000Z`; `69cdc98ad385e3b94310f7b2.jsonl[404] _id=69e13fb91724f0c9e2f709ca ts=2026-04-16T19:59:52.5470000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 84 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1180 | 0.003 | 3.159 | 587.115 | 51.857 | 341255.581 | 0.1 | 326 | 4 |
| PlayerPositionEvent | 489 | 17.541 | 30.007 | 1416.347 | 36.893 | 340898.712 | 0.04 | 0 | 3 |
| TopographicMapEvent | 83 | 0.282 | 3.11 | 6225.407 | 813.881 | 342047.479 | 0.01 | 0 | 5 |
| argumentationNodeEvent | 62 | 0.904 | 4.946 | 11102.607 | 70.522 | 519427.027 | 0.01 | 0 | 2 |
| questEvent | 42 | 0.003 | 189.593 | 16494.258 | 160087.102 | 341795.936 | 0.0 | 4 | 11 |
| Topographic Map Event | 39 | 4.344 | 38.903 | 13250.604 | 18862.099 | 342033.894 | 0.0 | 0 | 4 |
| argumentationEvent | 9 | 0.097 | 45.577 | 76487.167 | 379007.906 | 519410.416 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 5 | 2.959 | 71.806 | 103769.541 | 310233.126 | 344131.898 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.007s (p5 29.95s, p95 36.89s, n=489) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `97ms: 69cdc98ad385e3b94310f7b2.jsonl[271] _id=69e91f1b1724f0c9e2fa9e89 ts=2026-04-22T19:18:51.8990000Z ~ 69cdc98ad385e3b94310f7b2.jsonl[388] _id=69e91f1c1724f0c9e2fa9e92 ts=2026-04-22T19:18:51.9960000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 47m 
  - Evidence: 94h 47m: 69cdc98ad385e3b94310f7b2.jsonl[415] _id=69e1404e1724f0c9e2f70c38 ts=2026-04-16T20:02:21.6580000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1333] _id=69e675551724f0c9e2f8b781 ts=2026-04-20T18:49:57.2390000Z; 46h 44m: 69cdc98ad385e3b94310f7b2.jsonl[982] _id=69de9eb67957a33870f3b6a7 ts=2026-04-14T20:08:20.8740000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1028] _id=69e12fed1724f0c9e2f69060 ts=2026-04-16T18:52:28.3670000Z; 46h 43m: 69cdc98ad385e3b94310f7b2.jsonl[1644] _id=69e687fa1724f0c9e2f902b5 ts=2026-04-20T20:09:30.4800000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1675] _id=69e9191b1724f0c9e2fa85dd ts=2026-04-22T18:53:15.5970000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 326 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7b2.jsonl[1086] _id=69e131651724f0c9e2f695ba ts=2026-04-16T18:58:44.1960000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1083] _id=69e131651724f0c9e2f695be ts=2026-04-16T18:58:44.1990000Z; 3ms: 69cdc98ad385e3b94310f7b2.jsonl[169] _id=69e131141724f0c9e2f694a2 ts=2026-04-16T18:57:23.7650000Z -> 69cdc98ad385e3b94310f7b2.jsonl[154] _id=69e131141724f0c9e2f694a4 ts=2026-04-16T18:57:23.7680000Z; 3ms: 69cdc98ad385e3b94310f7b2.jsonl[1869] _id=69e928a21724f0c9e2fabf8d ts=2026-04-22T19:59:29.9630000Z -> 69cdc98ad385e3b94310f7b2.jsonl[791] _id=69e928a21724f0c9e2fabf8f ts=2026-04-22T19:59:29.9660000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 41m 
  - Evidence: 94h 41m: 69cdc98ad385e3b94310f7b2.jsonl[1309] _id=69e141af1724f0c9e2f712b6 ts=2026-04-16T20:08:14.0980000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1332] _id=69e675511724f0c9e2f8b773 ts=2026-04-20T18:49:52.8100000Z; 46h 42m: 69cdc98ad385e3b94310f7b2.jsonl[123] _id=69de9ec57957a33870f3b6d9 ts=2026-04-14T20:08:36.1720000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1029] _id=69e12fb91724f0c9e2f68fb0 ts=2026-04-16T18:51:36.1480000Z; 46h 38m: 69cdc98ad385e3b94310f7b2.jsonl[664] _id=69e6885b1724f0c9e2f903fd ts=2026-04-20T20:11:07.2780000Z -> 69cdc98ad385e3b94310f7b2.jsonl[666] _id=69e9182f1724f0c9e2fa828f ts=2026-04-22T18:49:18.7240000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 69cdc98ad385e3b94310f7b2.jsonl[1160] _id=69e136f71724f0c9e2f6b84e ts=2026-04-16T19:22:30.2710000Z -> 69cdc98ad385e3b94310f7b2.jsonl[465] _id=69e6773a1724f0c9e2f8bee9 ts=2026-04-20T18:58:02.1690000Z; 48h 30m: 69cdc98ad385e3b94310f7b2.jsonl[1361] _id=69e6773d1724f0c9e2f8bef9 ts=2026-04-20T18:58:05.1280000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1655] _id=69e9216b1724f0c9e2faa4c3 ts=2026-04-22T19:28:43.1650000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 0m 
  - Evidence: 95h 0m: 69cdc98ad385e3b94310f7b2.jsonl[425] _id=69e141021724f0c9e2f70eb0 ts=2026-04-16T20:05:21.4880000Z -> 69cdc98ad385e3b94310f7b2.jsonl[508] _id=69e679131724f0c9e2f8c76b ts=2026-04-20T19:05:55.3820000Z; 47h 8m: 69cdc98ad385e3b94310f7b2.jsonl[626] _id=69e6845a1724f0c9e2f8f805 ts=2026-04-20T19:54:01.8260000Z -> 69cdc98ad385e3b94310f7b2.jsonl[700] _id=69e91b321724f0c9e2fa8e99 ts=2026-04-22T19:02:10.7510000Z; 35m 3s: 69cdc98ad385e3b94310f7b2.jsonl[1451] _id=69e67bfb1724f0c9e2f8d469 ts=2026-04-20T19:18:19.0760000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1592] _id=69e684321724f0c9e2f8f759 ts=2026-04-20T19:53:22.6390000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 0m 
  - Evidence: 95h 0m: 69cdc98ad385e3b94310f7b2.jsonl[424] _id=69e141011724f0c9e2f70eaa ts=2026-04-16T20:05:20.4860000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1399] _id=69e679201724f0c9e2f8c7b1 ts=2026-04-20T19:06:07.9650000Z; 47h 10m: 69cdc98ad385e3b94310f7b2.jsonl[1599] _id=69e684581724f0c9e2f8f801 ts=2026-04-20T19:54:00.5440000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1732] _id=69e91bcc1724f0c9e2fa90f5 ts=2026-04-22T19:04:44.7570000Z; 20m 12s: 69cdc98ad385e3b94310f7b2.jsonl[1526] _id=69e67f7b1724f0c9e2f8e575 ts=2026-04-20T19:33:15.3950000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1594] _id=69e684381724f0c9e2f8f77d ts=2026-04-20T19:53:27.9940000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 16m 
  - Evidence: 144h 16m: 69cdc98ad385e3b94310f7b2.jsonl[161] _id=69e130c91724f0c9e2f6937e ts=2026-04-16T18:56:08.1430000Z -> 69cdc98ad385e3b94310f7b2.jsonl[850] _id=69e91dba1724f0c9e2fa9947 ts=2026-04-22T19:12:58.5590000Z; 46h 46m: 69cdc98ad385e3b94310f7b2.jsonl[971] _id=69de9e767957a33870f3b5a7 ts=2026-04-14T20:07:17.3500000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1045] _id=69e1304a1724f0c9e2f691de ts=2026-04-16T18:54:01.4910000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 17m 
  - Evidence: 144h 17m: 69cdc98ad385e3b94310f7b2.jsonl[1066] _id=69e130c31724f0c9e2f6936c ts=2026-04-16T18:56:02.3550000Z -> 69cdc98ad385e3b94310f7b2.jsonl[983] _id=69e91dc51724f0c9e2fa997d ts=2026-04-22T19:13:09.3820000Z; 46h 45m: 69cdc98ad385e3b94310f7b2.jsonl[986] _id=69de9ecb7957a33870f3b6ef ts=2026-04-14T20:08:42.4170000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1048] _id=69e130521724f0c9e2f691f4 ts=2026-04-16T18:54:09.3510000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 56m 
  - Evidence: 94h 56m: 69cdc98ad385e3b94310f7b2.jsonl[367] _id=69e13e301724f0c9e2f70412 ts=2026-04-16T19:53:19.4480000Z -> 69cdc98ad385e3b94310f7b2.jsonl[433] _id=69e675541724f0c9e2f8b777 ts=2026-04-20T18:49:55.3840000Z; 47h 8m: 69cdc98ad385e3b94310f7b2.jsonl[619] _id=69e6814e1724f0c9e2f8edc3 ts=2026-04-20T19:41:02.2010000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1666] _id=69e918321724f0c9e2fa8293 ts=2026-04-22T18:49:22.1120000Z; 46h 47m: 69cdc98ad385e3b94310f7b2.jsonl[957] _id=69de9dd67957a33870f3b35b ts=2026-04-14T20:04:36.7820000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1030] _id=69e12fbc1724f0c9e2f68fbc ts=2026-04-16T18:51:38.7680000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.003s..0.012s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7b2.jsonl[148] _id=69e12fed1724f0c9e2f69064 ts=2026-04-16T18:52:28.3910000Z -> 69cdc98ad385e3b94310f7b2.jsonl[1035] _id=69e12fed1724f0c9e2f69066 ts=2026-04-16T18:52:28.3940000Z; 3ms: 69cdc98ad385e3b94310f7b2.jsonl[79] _id=69de9dd67957a33870f3b359 ts=2026-04-14T20:04:36.7790000Z -> 69cdc98ad385e3b94310f7b2.jsonl[957] _id=69de9dd67957a33870f3b35b ts=2026-04-14T20:04:36.7820000Z; 12ms: 69cdc98ad385e3b94310f7b2.jsonl[908] _id=69de9a4c7957a33870f3a37b ts=2026-04-14T19:49:31.2800000Z -> 69cdc98ad385e3b94310f7b2.jsonl[907] _id=69de9a4c7957a33870f3a37d ts=2026-04-14T19:49:31.2920000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7b2.jsonl:69cdc98ad385e3b94310f7b2, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7b2.jsonl[1160] _id=69e136f71724f0c9e2f6b84e ts=2026-04-16T19:22:30.2710000Z`; `69cdc98ad385e3b94310f7b2.jsonl[1361] _id=69e6773d1724f0c9e2f8bef9 ts=2026-04-20T18:58:05.1280000Z`; `69cdc98ad385e3b94310f7b2.jsonl[1659] _id=69e921b31724f0c9e2faa5e1 ts=2026-04-22T19:29:54.9710000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 84 record(s) match the trigger in 69cdc98ad385e3b94310f7b2.jsonl:69cdc98ad385e3b94310f7b2, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7b2.jsonl[371] _id=69e13e4a1724f0c9e2f70478 ts=2026-04-16T19:53:45.8190000Z`; `69cdc98ad385e3b94310f7b2.jsonl[372] _id=69e13e4b1724f0c9e2f7047e ts=2026-04-16T19:53:46.4690000Z`; `69cdc98ad385e3b94310f7b2.jsonl[1260] _id=69e13ec61724f0c9e2f70606 ts=2026-04-16T19:55:49.2720000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7b2.jsonl[1550] _id=69e680b71724f0c9e2f8eafd ts=2026-04-20T19:38:31.4950000Z`; `69cdc98ad385e3b94310f7b2.jsonl[1565] _id=69e6814e1724f0c9e2f8edcb ts=2026-04-20T19:41:02.2750000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7b2.jsonl[388] _id=69e91f1c1724f0c9e2fa9e92 ts=2026-04-22T19:18:51.9960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc98ad385e3b94310f7b2.jsonl[1582] _id=69e682901724f0c9e2f8f28b ts=?`; `69cdc98ad385e3b94310f7b2.jsonl[1667] _id=69e918421724f0c9e2fa829f ts=?`
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7b2.jsonl[1056] _id=69e130a11724f0c9e2f69310 ts=2026-04-16T18:55:28.2010000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 193 unmatched 'DialogueStartEvent' (totals: 278 start, 87 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 26 start, 17 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.32s, min -42.08s, max -0.02s over 1922 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b2\coverage.yaml

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
  - Observed: 40 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
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

### `DialogueEvent` — 1181 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (436); Unit 3 Dev (422); Unit 1 Dev (227); Unit 3 Dungeon Dev (96)
- **eventKey:** present on 816 of 1181 records
- **Intervals:** median 3.16s (p5 0.01s / p95 51.86s, n=1180)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x816; [conversationId, dialogueEventType] x365
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1181/1181 records)
    numeric range 10 .. 104 (28 unique)
data.dialogueEventType  (string, 1181/1181 records)
    "DialogueNodeEvent"  x816
    "DialogueStartEvent"  x278
    "DialogueFinishEvent"  x87
data.nodeId  (number, 816/1181 records)
    numeric range 0 .. 283 (183 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 494 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (186); Unit 3 Dev (168); Unit 1 Dev (81); Unit 3 Dungeon Dev (59)
- **Intervals:** median 30.01s (p5 29.95s / p95 36.89s, n=489)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 494/494 records)
data.position.x  (number, 494/494 records)
    numeric range -676.846 .. 1097.33 (255 unique)
data.position.y  (number, 494/494 records)
    numeric range -114.326 .. 155.19 (175 unique)
data.position.z  (number, 494/494 records)
    numeric range -1109.48 .. 1982.78 (255 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `TopographicMapEvent` — 84 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (52); Unit 3 Dev (32)
- **Intervals:** median 3.11s (p5 0.41s / p95 813.88s, n=83)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 84/84 records)
    "dragEnd"  x42
    "dragStart"  x42
data.featureUsed  (string, 84/84 records)
    "waypoint"  x84
data.location  (object, 84/84 records)
data.location.x  (number, 84/84 records)
    numeric range -791.879 .. 297.699 (43 unique)
data.location.y  (number, 84/84 records)
    numeric range -342.548 .. 544.579 (42 unique)
data.location.z  (number, 84/84 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 63 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (35); Unit 1 Dev (28)
- **Intervals:** median 4.95s (p5 1.17s / p95 70.52s, n=62)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 63/63 records)
    "argumentationNodeAdd"  x38
    "argumentationNodeRemove"  x25
data.argumentationTitle  (string, 63/63 records)
    "Unit 3 - Pollution Upstream"  x35
    "Unit 1 - Freshwater"  x24
    "Unit 1 - Argumentation Tutorial"  x4
data.nodeName  (string, 63/63 records)
    "1"  x15
    "I"  x12
    "A"  x11
    "B"  x8
    "2"  x6
    "II"  x6
    "3"  x2
    "4"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 43 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (15); Unit 2 Prod (Refactor) (15); Unit 3 Dev (11); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 43 of 43 records
- **Intervals:** median 189.59s (p5 0.01s / p95 160087.10s, n=42)
- **`data` key-set variants:** [questEventType, questID, questName] x26; [questEventType, questID, questName, questSuccessOrFailure] x17
- **Fields under `data`:**

```text
data.questEventType  (string, 43/43 records)
    "questActiveEvent"  x26
    "questFinishEvent"  x17
data.questID  (string, 43/43 records)
    14 unique values (see csv/event_unique_values.csv)
data.questName  (string, 43/43 records)
    14 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 17/43 records)
    "Succeeded"  x17
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 3 Dev (14)
- **Intervals:** median 38.90s (p5 6.14s / p95 18862.10s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (3)
- **Intervals:** median 45.58s (p5 14.78s / p95 379007.91s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 10/10 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x3
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2)
- **Intervals:** median 71.81s (p5 2.97s / p95 310233.13s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/6 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/6 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x1
    "unhandled_rejection"  x1
data.unitId  (string, 2/2 records)
    "unit3"  x2
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

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
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TopographicMapEvent` data.actionType: "dragStart" (42x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (25x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*