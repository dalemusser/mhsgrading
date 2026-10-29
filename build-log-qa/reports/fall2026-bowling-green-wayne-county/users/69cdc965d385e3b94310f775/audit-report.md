# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f775

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f775
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f775.jsonl
- **Records:** 1770 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f775
- **Time span:** 2026-04-14T13:54:21.192000+00:00 .. 2026-04-28T14:33:52.992000+00:00 (336h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f775\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1770 records, 4 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 51 INFO, 5 NOT_TESTED, 36 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowUnfocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1149 | 64.92 | 1 | 4 | 767 | 2026-04-14T13:54:39.920000+00:00 | 2026-04-28T14:23:33.317000+00:00 | 336h 28m |
| PlayerPositionEvent | 434 | 24.52 | 1 | 4 | 0 | 2026-04-14T13:54:21.192000+00:00 | 2026-04-28T14:33:52.992000+00:00 | 336h 39m |
| Topographic Map Event | 81 | 4.58 | 1 | 3 | 0 | 2026-04-14T14:27:25.727000+00:00 | 2026-04-22T14:18:01.528000+00:00 | 191h 50m |
| argumentationNodeEvent | 48 | 2.71 | 1 | 2 | 0 | 2026-04-14T14:14:00.267000+00:00 | 2026-04-20T14:24:01.462000+00:00 | 144h 10m |
| questEvent | 33 | 1.86 | 1 | 4 | 33 | 2026-04-14T13:54:39.903000+00:00 | 2026-04-28T14:16:16.490000+00:00 | 336h 21m |
| TopographicMapEvent | 12 | 0.68 | 1 | 1 | 0 | 2026-04-16T17:47:51.940000+00:00 | 2026-04-20T13:37:29.925000+00:00 | 91h 49m |
| argumentationEvent | 7 | 0.4 | 1 | 2 | 0 | 2026-04-14T14:13:25.284000+00:00 | 2026-04-20T14:24:02.699000+00:00 | 144h 10m |
| Soil Key Puzzle | 2 | 0.11 | 1 | 1 | 0 | 2026-04-22T13:21:55.043000+00:00 | 2026-04-22T13:22:48.862000+00:00 | 53.8s |
| argumentationToolEvent | 2 | 0.11 | 1 | 1 | 0 | 2026-04-20T14:22:41.783000+00:00 | 2026-04-20T14:22:42.496000+00:00 | 0.7s |
| EndOfUnit | 1 | 0.06 | 1 | 1 | 0 | 2026-04-14T14:22:02.412000+00:00 | 2026-04-14T14:22:02.412000+00:00 | 0.0s |
| crash | 1 | 0.06 | 1 | 1 | 0 |  |  | ? |

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
  - Observed: 30.008s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 53.819s median 
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
  - Observed: 2.507s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.713s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
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
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 434 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 Prod (Refactor); Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 81 records this build 
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
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 24; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 10 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f775.jsonl[726] _id=69de4c407957a33870f3532c ts=2026-04-14T14:16:32.0370000Z`; `69cdc965d385e3b94310f775.jsonl[836] _id=69e11d9f7957a33870f56eb4 ts=2026-04-16T17:34:23.6580000Z`; `69cdc965d385e3b94310f775.jsonl[924] _id=69e628091724f0c9e2f84d5d ts=2026-04-20T13:20:08.7360000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 81 records, TopographicMapEvent: 12 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1148 | 0.002 | 1.935 | 1055.168 | 45.754 | 520110.253 | 0.06 | 328 | 5 |
| PlayerPositionEvent | 430 | 29.895 | 30.008 | 2818.237 | 37.604 | 517580.337 | 0.02 | 0 | 5 |
| Topographic Map Event | 80 | 0.423 | 6.982 | 8632.948 | 7170.373 | 205852.158 | 0.01 | 0 | 6 |
| argumentationNodeEvent | 47 | 0.69 | 2.507 | 11042.579 | 12.968 | 518760.655 | 0.01 | 0 | 1 |
| questEvent | 32 | 0.003 | 165.4 | 37840.518 | 193897.34 | 521553.575 | 0.0 | 3 | 8 |
| TopographicMapEvent | 11 | 0.3 | 2.031 | 30052.544 | 165204.982 | 330068.656 | 0.0 | 0 | 1 |
| argumentationEvent | 6 | 0.096 | 62.84 | 86506.236 | 389100.06 | 518747.485 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 1 | 53.819 | 53.819 | 53.819 | 53.819 | 53.819 | 1.11 | 0 | 0 |
| argumentationToolEvent | 1 | 0.713 | 0.713 | 0.713 | 0.713 | 0.713 | 84.15 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.95s, p95 37.60s, n=430) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `876ms: 69cdc965d385e3b94310f775.jsonl[1096] _id=69e62d0f1724f0c9e2f86ce9 ts=2026-04-20T13:41:34.5220000Z ~ 69cdc965d385e3b94310f775.jsonl[1103] _id=69e62d101724f0c9e2f86cf5 ts=2026-04-20T13:41:35.3980000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `96ms: 69cdc965d385e3b94310f775.jsonl[371] _id=69e637031724f0c9e2f8a6fb ts=2026-04-20T14:24:02.6030000Z ~ 69cdc965d385e3b94310f775.jsonl[1461] _id=69e637041724f0c9e2f8a705 ts=2026-04-20T14:24:02.6990000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 28m 
  - Evidence: 144h 28m: 69cdc965d385e3b94310f775.jsonl[1667] _id=69e8d1821724f0c9e2fa3bf9 ts=2026-04-22T13:47:46.5360000Z -> 69cdc965d385e3b94310f775.jsonl[449] _id=69f0c1311724f0c9e2fcab2f ts=2026-04-28T14:16:16.7890000Z; 57h 10m: 69cdc965d385e3b94310f775.jsonl[142] _id=69e120cb7957a33870f56fb0 ts=2026-04-16T17:47:54.7210000Z -> 69cdc965d385e3b94310f775.jsonl[879] _id=69e444eb1724f0c9e2f84939 ts=2026-04-19T02:58:50.7880000Z; 51h 1m: 69cdc965d385e3b94310f775.jsonl[835] _id=69de4fb47957a33870f36a42 ts=2026-04-14T14:31:15.6880000Z -> 69cdc965d385e3b94310f775.jsonl[848] _id=69e11d267957a33870f56e7a ts=2026-04-16T17:32:22.0590000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 328 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f775.jsonl[359] _id=69e636ad1724f0c9e2f8a401 ts=2026-04-20T14:22:36.9060000Z -> 69cdc965d385e3b94310f775.jsonl[360] _id=69e636ad1724f0c9e2f8a409 ts=2026-04-20T14:22:36.9080000Z; 3ms: 69cdc965d385e3b94310f775.jsonl[234] _id=69e629f81724f0c9e2f856ef ts=2026-04-20T13:28:22.7810000Z -> 69cdc965d385e3b94310f775.jsonl[235] _id=69e629f81724f0c9e2f856f1 ts=2026-04-20T13:28:22.7840000Z; 3ms: 69cdc965d385e3b94310f775.jsonl[43] _id=69de4d2f7957a33870f358c1 ts=2026-04-14T14:20:30.7970000Z -> 69cdc965d385e3b94310f775.jsonl[775] _id=69de4d2f7957a33870f358c5 ts=2026-04-14T14:20:30.8000000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 46m 
  - Evidence: 143h 46m: 69cdc965d385e3b94310f775.jsonl[1750] _id=69e8db621724f0c9e2fa74e3 ts=2026-04-22T14:29:54.5960000Z -> 69cdc965d385e3b94310f775.jsonl[447] _id=69f0c12f1724f0c9e2fcab25 ts=2026-04-28T14:16:14.9330000Z; 57h 10m: 69cdc965d385e3b94310f775.jsonl[141] _id=69e120ca7957a33870f56fae ts=2026-04-16T17:47:54.5670000Z -> 69cdc965d385e3b94310f775.jsonl[878] _id=69e444e11724f0c9e2f84931 ts=2026-04-19T02:58:41.1360000Z; 51h 1m: 69cdc965d385e3b94310f775.jsonl[664] _id=69de4fa97957a33870f369f2 ts=2026-04-14T14:31:04.8410000Z -> 69cdc965d385e3b94310f775.jsonl[847] _id=69e11d227957a33870f56e76 ts=2026-04-16T17:32:18.0370000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 57h 10m 
  - Evidence: 57h 10m: 69cdc965d385e3b94310f775.jsonl[140] _id=69e120c87957a33870f56fac ts=2026-04-16T17:47:52.6100000Z -> 69cdc965d385e3b94310f775.jsonl[867] _id=69e444e71724f0c9e2f84933 ts=2026-04-19T02:58:44.7680000Z; 51h 20m: 69cdc965d385e3b94310f775.jsonl[822] _id=69de4ecf7957a33870f362c2 ts=2026-04-14T14:27:27.6570000Z -> 69cdc965d385e3b94310f775.jsonl[865] _id=69e120c17957a33870f56fa6 ts=2026-04-16T17:47:44.6800000Z; 47h 30m: 69cdc965d385e3b94310f775.jsonl[400] _id=69e639011724f0c9e2f8af0d ts=2026-04-20T14:32:33.2150000Z -> 69cdc965d385e3b94310f775.jsonl[1701] _id=69e8d52e1724f0c9e2fa4fa7 ts=2026-04-22T14:03:26.0560000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 91h 41m 
  - Evidence: 91h 41m: 69cdc965d385e3b94310f775.jsonl[866] _id=69e120c87957a33870f56faa ts=2026-04-16T17:47:52.4940000Z -> 69cdc965d385e3b94310f775.jsonl[992] _id=69e62a1d1724f0c9e2f857f9 ts=2026-04-20T13:29:01.1500000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 5m 
  - Evidence: 144h 5m: 69cdc965d385e3b94310f775.jsonl[744] _id=69de4c407957a33870f35327 ts=2026-04-14T14:16:32.0090000Z -> 69cdc965d385e3b94310f775.jsonl[358] _id=69e6369c1724f0c9e2f8a393 ts=2026-04-20T14:22:19.4940000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 6m 
  - Evidence: 144h 6m: 69cdc965d385e3b94310f775.jsonl[740] _id=69de4c3e7957a33870f35313 ts=2026-04-14T14:16:30.1190000Z -> 69cdc965d385e3b94310f775.jsonl[1429] _id=69e636a71724f0c9e2f8a3cd ts=2026-04-20T14:22:30.7740000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 144h 52m 
  - Evidence: 144h 52m: 69cdc965d385e3b94310f775.jsonl[1576] _id=69e8cbdf1724f0c9e2fa1431 ts=2026-04-22T13:23:42.9150000Z -> 69cdc965d385e3b94310f775.jsonl[446] _id=69f0c1311724f0c9e2fcab29 ts=2026-04-28T14:16:16.4900000Z; 57h 11m: 69cdc965d385e3b94310f775.jsonl[858] _id=69e120be7957a33870f56f9c ts=2026-04-16T17:47:42.2620000Z -> 69cdc965d385e3b94310f775.jsonl[197] _id=69e444e71724f0c9e2f84935 ts=2026-04-19T02:58:44.8270000Z; 51h 8m: 69cdc965d385e3b94310f775.jsonl[52] _id=69de4df97957a33870f35dfe ts=2026-04-14T14:23:52.9630000Z -> 69cdc965d385e3b94310f775.jsonl[849] _id=69e11d257957a33870f56e78 ts=2026-04-16T17:32:20.5740000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.003s..0.016s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f775.jsonl[667] _id=69de4b6f7957a33870f34bff ts=2026-04-14T14:13:02.1770000Z -> 69cdc965d385e3b94310f775.jsonl[668] _id=69de4b6f7957a33870f34c03 ts=2026-04-14T14:13:02.1800000Z; 9ms: 69cdc965d385e3b94310f775.jsonl[570] _id=69de48e57957a33870f33995 ts=2026-04-14T14:02:13.0280000Z -> 69cdc965d385e3b94310f775.jsonl[556] _id=69de48e57957a33870f33997 ts=2026-04-14T14:02:13.0370000Z; 16ms: 69cdc965d385e3b94310f775.jsonl[596] _id=69de49877957a33870f33e95 ts=2026-04-14T14:04:55.5640000Z -> 69cdc965d385e3b94310f775.jsonl[594] _id=69de49887957a33870f33e99 ts=2026-04-14T14:04:55.5800000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 1 record(s) match the trigger in 69cdc965d385e3b94310f775.jsonl:69cdc965d385e3b94310f775, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f775.jsonl[1571] _id=69e8cba81724f0c9e2fa12f7 ts=2026-04-22T13:22:48.8620000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 12 record(s) match the trigger in 69cdc965d385e3b94310f775.jsonl:69cdc965d385e3b94310f775, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f775.jsonl[139] _id=69e120c87957a33870f56fa8 ts=2026-04-16T17:47:51.9400000Z`; `69cdc965d385e3b94310f775.jsonl[866] _id=69e120c87957a33870f56faa ts=2026-04-16T17:47:52.4940000Z`; `69cdc965d385e3b94310f775.jsonl[992] _id=69e62a1d1724f0c9e2f857f9 ts=2026-04-20T13:29:01.1500000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f775.jsonl[291] _id=69e630201724f0c9e2f87cc1 ts=2026-04-20T13:54:40.2200000Z`; `69cdc965d385e3b94310f775.jsonl[294] _id=69e6308a1724f0c9e2f87eed ts=2026-04-20T13:56:25.2260000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f775.jsonl[1461] _id=69e637041724f0c9e2f8a705 ts=2026-04-20T14:24:02.6990000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f775.jsonl[1544] _id=69e8ca181724f0c9e2fa0b53 ts=2026-04-22T13:16:08.5160000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc965d385e3b94310f775.jsonl[1743] _id=69e8da781724f0c9e2fa7005 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 208 unmatched 'DialogueStartEvent' (totals: 294 start, 88 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 8 unmatched 'questActiveEvent' (totals: 20 start, 13 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.66s, min -10.30s, max -0.02s over 1769 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f775\coverage.yaml

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
  - Observed: 81 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
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

### `DialogueEvent` — 1149 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (432); Unit 2 Prod (Refactor) (368); Unit 1 Dev (222); Unit 3 Dungeon Dev (127)
- **eventKey:** present on 767 of 1149 records
- **Intervals:** median 1.94s (p5 0.01s / p95 45.75s, n=1148)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x767; [conversationId, dialogueEventType] x382
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1149/1149 records)
    numeric range 10 .. 101 (26 unique)
data.dialogueEventType  (string, 1149/1149 records)
    "DialogueNodeEvent"  x767
    "DialogueStartEvent"  x294
    "DialogueFinishEvent"  x88
data.nodeId  (number, 767/1149 records)
    numeric range 0 .. 283 (155 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 434 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dungeon Dev (166); Unit 3 Dev (108); Unit 2 Prod (Refactor) (104); Unit 1 Dev (56)
- **Intervals:** median 30.01s (p5 29.95s / p95 37.60s, n=430)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 434/434 records)
data.position.x  (number, 434/434 records)
    numeric range -812.145 .. 1971.51 (305 unique)
data.position.y  (number, 434/434 records)
    numeric range -114.326 .. 177.731 (214 unique)
data.position.z  (number, 434/434 records)
    numeric range -1120.8 .. 2004.06 (305 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 81 records

- **Scenes:** Unit 2 Prod (Refactor) (45); Unit 3 Dev (32); Unit 3 Dungeon Dev (4)
- **Intervals:** median 6.98s (p5 1.62s / p95 7170.37s, n=80)
- **Fields under `data`:**

```text
data.actionType  (string, 81/81 records)
    "MapOpenEvent"  x41
    "MapCloseEvent"  x40
data.featureUsed  (string, 81/81 records)
    "Map"  x81
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 48 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (25); Unit 3 Dev (23)
- **Intervals:** median 2.51s (p5 1.02s / p95 12.97s, n=47)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "argumentationNodeAdd"  x27
    "argumentationNodeRemove"  x21
data.argumentationTitle  (string, 48/48 records)
    "Unit 1 - Freshwater"  x25
    "Unit 3 - Pollution Upstream"  x23
data.nodeName  (string, 48/48 records)
    "B"  x15
    "I"  x12
    "1"  x7
    "A"  x7
    "2"  x2
    "3"  x2
    "II"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 33 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (12); Unit 3 Dev (7); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 33 of 33 records
- **Intervals:** median 165.40s (p5 0.01s / p95 193897.34s, n=32)
- **`data` key-set variants:** [questEventType, questID, questName] x20; [questEventType, questID, questName, questSuccessOrFailure] x13
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 33/33 records)
    "questActiveEvent"  x20
    "questFinishEvent"  x13
data.questID  (string, 33/33 records)
    "21"  x6
    "18"  x4
    "23"  x4
    "16"  x3
    "17"  x2
    "22"  x2
    "28"  x2
    "29"  x2
    "31"  x2
    "32"  x2
    "33"  x2
    "34"  x2
data.questName  (string, 33/33 records)
    "Escape the Ruin"  x6
    "Foraged Forging"  x4
    "Forsaken Facility"  x4
    "Supply Run"  x3
    "Defend the Expedition"  x2
    "Gear Up"  x2
    "Getting Your Space Legs"  x2
    "Getting the Band Back Together"  x2
    "Info and Intros"  x2
    "Pollution Solution"  x2
    "TK, Reporting In!"  x2
    "What Was That?"  x2
data.questSuccessOrFailure  (string, 13/33 records)
    "Succeeded"  x13
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 12 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (12)
- **Intervals:** median 2.03s (p5 0.33s / p95 165204.98s, n=11)
- **Open findings:** 1 — see sections 5-8
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

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 62.84s (p5 1.66s / p95 389100.06s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 7/7 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 2 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 53.82s (p5 53.82s / p95 53.82s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 2/2 records)
    "Finished"  x1
    "Started"  x1
data.Unit  (string, 2/2 records)
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 0.71s (p5 0.71s / p95 0.71s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x1
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 2/2 records)
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Pollution Site Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
    false  x1
data.message  (string, 1/1 records)
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit3"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

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
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now
- `InputEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `TopographicMapEvent` data.actionType: "dragStart" (6x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (21x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*