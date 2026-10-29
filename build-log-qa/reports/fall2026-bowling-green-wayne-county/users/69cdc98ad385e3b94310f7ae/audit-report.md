# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ae

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ae
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7ae.jsonl
- **Records:** 1671 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7ae
- **Time span:** 2026-04-14T19:38:39.780000+00:00 .. 2026-04-22T20:04:28.588000+00:00 (192h 25m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ae\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1671 records, 4 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 56 INFO, 5 NOT_TESTED, 34 PASS.
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
| DialogueEvent | 1166 | 69.78 | 1 | 4 | 812 | 2026-04-14T19:38:58.191000+00:00 | 2026-04-22T20:04:28.588000+00:00 | 192h 25m |
| PlayerPositionEvent | 326 | 19.51 | 1 | 4 | 0 | 2026-04-14T19:38:39.780000+00:00 | 2026-04-22T20:04:27.176000+00:00 | 192h 25m |
| argumentationNodeEvent | 43 | 2.57 | 1 | 3 | 0 | 2026-04-14T20:00:53.104000+00:00 | 2026-04-22T19:42:37.506000+00:00 | 191h 41m |
| Topographic Map Event | 42 | 2.51 | 1 | 2 | 0 | 2026-04-20T19:10:38.556000+00:00 | 2026-04-22T19:26:10.580000+00:00 | 48h 15m |
| questEvent | 35 | 2.09 | 1 | 4 | 35 | 2026-04-14T19:38:58.173000+00:00 | 2026-04-22T20:04:28.547000+00:00 | 192h 25m |
| TopographicMapEvent | 26 | 1.56 | 1 | 2 | 0 | 2026-04-20T19:10:47.642000+00:00 | 2026-04-22T19:05:32.258000+00:00 | 47h 54m |
| argumentationToolEvent | 14 | 0.84 | 1 | 2 | 0 | 2026-04-20T20:07:41.800000+00:00 | 2026-04-22T19:42:31.320000+00:00 | 47h 34m |
| argumentationEvent | 9 | 0.54 | 1 | 3 | 0 | 2026-04-14T20:00:40.482000+00:00 | 2026-04-22T19:42:39.761000+00:00 | 191h 41m |
| Soil Key Puzzle | 6 | 0.36 | 1 | 2 | 0 | 2026-04-20T19:02:40.514000+00:00 | 2026-04-22T19:48:52.557000+00:00 | 48h 46m |
| EndOfUnit | 2 | 0.12 | 1 | 2 | 0 | 2026-04-14T20:07:13.838000+00:00 | 2026-04-22T18:53:34.152000+00:00 | 190h 46m |
| crash | 2 | 0.12 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 686780.314s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.01s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 51.057s median 
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
  - Observed: 3.85s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.978s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.029s median 
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
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 326 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 42 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 26 records 
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
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 43 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[485] _id=69de9d6f7957a33870f3b1fb ts=2026-04-14T20:02:54.9370000Z`; `69cdc98ad385e3b94310f7ae.jsonl[763] _id=69e67b2d1724f0c9e2f8d0af ts=2026-04-20T19:14:52.6460000Z`; `69cdc98ad385e3b94310f7ae.jsonl[1152] _id=69e6881a1724f0c9e2f90325 ts=2026-04-20T20:10:01.5030000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 42 records, TopographicMapEvent: 26 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1165 | 0.003 | 2.979 | 594.618 | 33.582 | 513930.396 | 0.1 | 314 | 3 |
| PlayerPositionEvent | 322 | 29.856 | 30.01 | 2150.826 | 38.999 | 513866.664 | 0.03 | 0 | 2 |
| argumentationNodeEvent | 42 | 0.97 | 4.978 | 16431.057 | 80.89 | 518801.166 | 0.0 | 0 | 2 |
| Topographic Map Event | 41 | 2.783 | 21.887 | 4237.366 | 488.551 | 169209.155 | 0.01 | 0 | 2 |
| questEvent | 34 | 0.003 | 191.671 | 20374.423 | 60029.084 | 514135.369 | 0.0 | 3 | 8 |
| TopographicMapEvent | 25 | 0.601 | 3.85 | 6899.385 | 2024.311 | 169122.257 | 0.01 | 0 | 2 |
| argumentationToolEvent | 13 | 0.013 | 1.029 | 13176.117 | 68510.909 | 171269.842 | 0.0 | 4 | 1 |
| argumentationEvent | 8 | 0.096 | 49.901 | 86264.91 | 397041.016 | 518792.975 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 5 | 2.973 | 51.057 | 35114.409 | 139589.675 | 174152.052 | 0.0 | 0 | 2 |
| EndOfUnit | 1 | 686780.314 | 686780.314 | 686780.314 | 686780.314 | 686780.314 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.010s (p5 29.95s, p95 39.00s, n=322) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `96ms: 69cdc98ad385e3b94310f7ae.jsonl[1493] _id=69e924af1724f0c9e2fab1e3 ts=2026-04-22T19:42:39.6650000Z ~ 69cdc98ad385e3b94310f7ae.jsonl[1495] _id=69e924b01724f0c9e2fab1eb ts=2026-04-22T19:42:39.7610000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `975ms: 69cdc98ad385e3b94310f7ae.jsonl[210] _id=69e924991724f0c9e2fab175 ts=2026-04-22T19:42:17.4470000Z ~ 69cdc98ad385e3b94310f7ae.jsonl[1485] _id=69e9249b1724f0c9e2fab17f ts=2026-04-22T19:42:18.4220000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 142h 45m 
  - Evidence: 142h 45m: 69cdc98ad385e3b94310f7ae.jsonl[524] _id=69de9eb07957a33870f3b693 ts=2026-04-14T20:08:14.4320000Z -> 69cdc98ad385e3b94310f7ae.jsonl[584] _id=69e676391724f0c9e2f8ba8d ts=2026-04-20T18:53:44.8280000Z; 46h 37m: 69cdc98ad385e3b94310f7ae.jsonl[160] _id=69e688901724f0c9e2f904c3 ts=2026-04-20T20:11:59.7280000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1178] _id=69e9184e1724f0c9e2fa82ad ts=2026-04-22T18:49:49.8300000Z; 10m 20s: 69cdc98ad385e3b94310f7ae.jsonl[1112] _id=69e685411724f0c9e2f8fb39 ts=2026-04-20T19:57:52.9380000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1133] _id=69e687ae1724f0c9e2f9015d ts=2026-04-20T20:08:13.6580000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 314 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7ae.jsonl[28] _id=69de9db47957a33870f3b2e3 ts=2026-04-14T20:04:03.1530000Z -> 69cdc98ad385e3b94310f7ae.jsonl[29] _id=69de9db47957a33870f3b2e5 ts=2026-04-14T20:04:03.1560000Z; 3ms: 69cdc98ad385e3b94310f7ae.jsonl[491] _id=69de9d897957a33870f3b24d ts=2026-04-14T20:03:20.9110000Z -> 69cdc98ad385e3b94310f7ae.jsonl[492] _id=69de9d897957a33870f3b253 ts=2026-04-14T20:03:20.9140000Z; 3ms: 69cdc98ad385e3b94310f7ae.jsonl[506] _id=69de9e257957a33870f3b471 ts=2026-04-14T20:05:56.9330000Z -> 69cdc98ad385e3b94310f7ae.jsonl[512] _id=69de9e257957a33870f3b473 ts=2026-04-14T20:05:56.9360000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 190h 46m 
  - Evidence: 190h 46m: 69cdc98ad385e3b94310f7ae.jsonl[521] _id=69de9e727957a33870f3b59d ts=2026-04-14T20:07:13.8380000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1215] _id=69e9192e1724f0c9e2fa8639 ts=2026-04-22T18:53:34.1520000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 142h 44m 
  - Evidence: 142h 44m: 69cdc98ad385e3b94310f7ae.jsonl[526] _id=69de9eea7957a33870f3b730 ts=2026-04-14T20:09:13.8200000Z -> 69cdc98ad385e3b94310f7ae.jsonl[581] _id=69e676351724f0c9e2f8ba7b ts=2026-04-20T18:53:40.4840000Z; 46h 38m: 69cdc98ad385e3b94310f7ae.jsonl[1168] _id=69e688781724f0c9e2f90481 ts=2026-04-20T20:11:35.6580000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1176] _id=69e9184b1724f0c9e2fa82a9 ts=2026-04-22T18:49:47.1340000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 48h 22m 
  - Evidence: 48h 22m: 69cdc98ad385e3b94310f7ae.jsonl[832] _id=69e67dc31724f0c9e2f8dd37 ts=2026-04-20T19:25:54.7100000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1565] _id=69e9260a1724f0c9e2fab6a7 ts=2026-04-22T19:48:26.7620000Z; 22m 20s: 69cdc98ad385e3b94310f7ae.jsonl[640] _id=69e678541724f0c9e2f8c3bf ts=2026-04-20T19:02:43.4870000Z -> 69cdc98ad385e3b94310f7ae.jsonl[823] _id=69e67d901724f0c9e2f8dc6d ts=2026-04-20T19:25:03.6530000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 0m 
  - Evidence: 47h 0m: 69cdc98ad385e3b94310f7ae.jsonl[1116] _id=69e685671724f0c9e2f8fbd1 ts=2026-04-20T19:58:30.3550000Z -> 69cdc98ad385e3b94310f7ae.jsonl[177] _id=69e91a5f1724f0c9e2fa8b25 ts=2026-04-22T18:58:39.5100000Z; 19m 1s: 69cdc98ad385e3b94310f7ae.jsonl[815] _id=69e67cf61724f0c9e2f8d965 ts=2026-04-20T19:22:29.2500000Z -> 69cdc98ad385e3b94310f7ae.jsonl[981] _id=69e6816b1724f0c9e2f8ee23 ts=2026-04-20T19:41:30.5990000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 46h 58m 
  - Evidence: 46h 58m: 69cdc98ad385e3b94310f7ae.jsonl[149] _id=69e6855b1724f0c9e2f8fba3 ts=2026-04-20T19:58:19.0340000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1236] _id=69e919fd1724f0c9e2fa8943 ts=2026-04-22T18:57:01.2910000Z; 40m 33s: 69cdc98ad385e3b94310f7ae.jsonl[785] _id=69e67bd81724f0c9e2f8d3dd ts=2026-04-20T19:17:43.6800000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1115] _id=69e685591724f0c9e2f8fb95 ts=2026-04-20T19:58:16.9430000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 6m 
  - Evidence: 144h 6m: 69cdc98ad385e3b94310f7ae.jsonl[481] _id=69de9d6f7957a33870f3b1f5 ts=2026-04-14T20:02:54.9110000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1125] _id=69e687f81724f0c9e2f902a9 ts=2026-04-20T20:09:27.8860000Z; 47h 28m: 69cdc98ad385e3b94310f7ae.jsonl[154] _id=69e6881a1724f0c9e2f90323 ts=2026-04-20T20:10:01.4790000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1440] _id=69e923cb1724f0c9e2faae63 ts=2026-04-22T19:38:51.7130000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 6m 
  - Evidence: 144h 6m: 69cdc98ad385e3b94310f7ae.jsonl[484] _id=69de9d6e7957a33870f3b1f1 ts=2026-04-14T20:02:53.3410000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1146] _id=69e687ff1724f0c9e2f902d1 ts=2026-04-20T20:09:34.5070000Z; 47h 29m: 69cdc98ad385e3b94310f7ae.jsonl[1149] _id=69e688181724f0c9e2f90319 ts=2026-04-20T20:09:59.6350000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1443] _id=69e923df1724f0c9e2faaead ts=2026-04-22T19:39:11.5830000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 34m 
  - Evidence: 47h 34m: 69cdc98ad385e3b94310f7ae.jsonl[1131] _id=69e6878f1724f0c9e2f900e1 ts=2026-04-20T20:07:43.0350000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1481] _id=69e924951724f0c9e2fab151 ts=2026-04-22T19:42:12.8770000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.013s..0.014s shown 
  - Evidence: 13ms: 69cdc98ad385e3b94310f7ae.jsonl[1484] _id=69e9249a1724f0c9e2fab177 ts=2026-04-22T19:42:18.4090000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1485] _id=69e9249b1724f0c9e2fab17f ts=2026-04-22T19:42:18.4220000Z; 13ms: 69cdc98ad385e3b94310f7ae.jsonl[214] _id=69e924991724f0c9e2fab173 ts=2026-04-22T19:42:17.4340000Z -> 69cdc98ad385e3b94310f7ae.jsonl[210] _id=69e924991724f0c9e2fab175 ts=2026-04-22T19:42:17.4470000Z; 14ms: 69cdc98ad385e3b94310f7ae.jsonl[1490] _id=69e9249f1724f0c9e2fab19f ts=2026-04-22T19:42:23.3750000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1491] _id=69e9249f1724f0c9e2fab1a3 ts=2026-04-22T19:42:23.3890000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 142h 48m 
  - Evidence: 142h 48m: 69cdc98ad385e3b94310f7ae.jsonl[513] _id=69de9e4a7957a33870f3b501 ts=2026-04-14T20:06:33.3450000Z -> 69cdc98ad385e3b94310f7ae.jsonl[597] _id=69e676a11724f0c9e2f8bc1b ts=2026-04-20T18:55:28.7140000Z; 46h 38m: 69cdc98ad385e3b94310f7ae.jsonl[159] _id=69e688681724f0c9e2f90433 ts=2026-04-20T20:11:20.1050000Z -> 69cdc98ad385e3b94310f7ae.jsonl[1177] _id=69e918501724f0c9e2fa82b5 ts=2026-04-22T18:49:50.2400000Z; 32m 19s: 69cdc98ad385e3b94310f7ae.jsonl[937] _id=69e680891724f0c9e2f8ea37 ts=2026-04-20T19:37:44.5280000Z -> 69cdc98ad385e3b94310f7ae.jsonl[155] _id=69e6881c1724f0c9e2f90330 ts=2026-04-20T20:10:03.8160000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.003s..0.010s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7ae.jsonl[448] _id=69de9cb87957a33870f3af2b ts=2026-04-14T19:59:51.3360000Z -> 69cdc98ad385e3b94310f7ae.jsonl[449] _id=69de9cb87957a33870f3af2d ts=2026-04-14T19:59:51.3390000Z; 7ms: 69cdc98ad385e3b94310f7ae.jsonl[327] _id=69de994d7957a33870f39ed9 ts=2026-04-14T19:45:16.4720000Z -> 69cdc98ad385e3b94310f7ae.jsonl[328] _id=69de994d7957a33870f39edb ts=2026-04-14T19:45:16.4790000Z; 10ms: 69cdc98ad385e3b94310f7ae.jsonl[358] _id=69de9a3e7957a33870f3a32b ts=2026-04-14T19:49:17.3220000Z -> 69cdc98ad385e3b94310f7ae.jsonl[355] _id=69de9a3e7957a33870f3a32d ts=2026-04-14T19:49:17.3320000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7ae.jsonl:69cdc98ad385e3b94310f7ae, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[640] _id=69e678541724f0c9e2f8c3bf ts=2026-04-20T19:02:43.4870000Z`; `69cdc98ad385e3b94310f7ae.jsonl[832] _id=69e67dc31724f0c9e2f8dd37 ts=2026-04-20T19:25:54.7100000Z`; `69cdc98ad385e3b94310f7ae.jsonl[1566] _id=69e926241724f0c9e2fab6d5 ts=2026-04-22T19:48:52.5570000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 26 record(s) match the trigger in 69cdc98ad385e3b94310f7ae.jsonl:69cdc98ad385e3b94310f7ae, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[721] _id=69e67a381724f0c9e2f8cce1 ts=2026-04-20T19:10:47.6420000Z`; `69cdc98ad385e3b94310f7ae.jsonl[61] _id=69e67a391724f0c9e2f8cce7 ts=2026-04-20T19:10:49.1110000Z`; `69cdc98ad385e3b94310f7ae.jsonl[724] _id=69e67a451724f0c9e2f8cd29 ts=2026-04-20T19:11:00.5620000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[948] _id=69e680c71724f0c9e2f8eb37 ts=2026-04-20T19:38:46.5980000Z`; `69cdc98ad385e3b94310f7ae.jsonl[1288] _id=69e91b541724f0c9e2fa8eed ts=2026-04-22T19:02:44.2290000Z`; `69cdc98ad385e3b94310f7ae.jsonl[1308] _id=69e91bdb1724f0c9e2fa9139 ts=2026-04-22T19:04:58.8080000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[1495] _id=69e924b01724f0c9e2fab1eb ts=2026-04-22T19:42:39.7610000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[209] _id=69e924981724f0c9e2fab167 ts=2026-04-22T19:42:16.4280000Z`; `69cdc98ad385e3b94310f7ae.jsonl[214] _id=69e924991724f0c9e2fab173 ts=2026-04-22T19:42:17.4340000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[39] _id=69e91dd21724f0c9e2fa99ad ts=?`; `69cdc98ad385e3b94310f7ae.jsonl[1538] _id=69e9256a1724f0c9e2fab49d ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7ae.jsonl[1477] _id=69e924981724f0c9e2fab16b ts=2026-04-22T19:42:16.4460000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 153 unmatched 'DialogueStartEvent' (totals: 252 start, 102 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 3 unmatched 'questActiveEvent' (totals: 19 start, 16 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.74s, min -5.64s, max -0.12s over 1669 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ae\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=partial, Unit4=skipped 
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
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 42 records 
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

### `DialogueEvent` — 1166 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (544); Unit 3 Dev (340); Unit 1 Dev (201); Unit 3 Dungeon Dev (81)
- **eventKey:** present on 812 of 1166 records
- **Intervals:** median 2.98s (p5 0.01s / p95 33.58s, n=1165)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x812; [conversationId, dialogueEventType] x354
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1166/1166 records)
    numeric range 8 .. 103 (31 unique)
data.dialogueEventType  (string, 1166/1166 records)
    "DialogueNodeEvent"  x812
    "DialogueStartEvent"  x252
    "DialogueFinishEvent"  x102
data.nodeId  (number, 812/1166 records)
    numeric range 0 .. 290 (210 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 326 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (145); Unit 3 Dev (93); Unit 1 Dev (57); Unit 3 Dungeon Dev (31)
- **Intervals:** median 30.01s (p5 29.95s / p95 39.00s, n=322)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 326/326 records)
data.position.x  (number, 326/326 records)
    numeric range -654.661 .. 1644.43 (150 unique)
data.position.y  (number, 326/326 records)
    numeric range -114.326 .. 158.035 (128 unique)
data.position.z  (number, 326/326 records)
    numeric range -1114.86 .. 1828.19 (150 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 43 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (31); Unit 1 Dev (9); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 4.98s (p5 1.59s / p95 80.89s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "argumentationNodeAdd"  x27
    "argumentationNodeRemove"  x16
data.argumentationTitle  (string, 43/43 records)
    "Unit 3 - Pollution Upstream"  x31
    "Unit 1 - Freshwater"  x7
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 43/43 records)
    "A"  x13
    "I"  x8
    "1"  x5
    "5"  x5
    "B"  x3
    "II"  x3
    "2"  x2
    "3"  x2
    "4"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 42 records

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (20)
- **Intervals:** median 21.89s (p5 3.90s / p95 488.55s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "MapCloseEvent"  x21
    "MapOpenEvent"  x21
data.featureUsed  (string, 42/42 records)
    "Map"  x42
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 35 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (12); Unit 3 Dev (8); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 35 of 35 records
- **Intervals:** median 191.67s (p5 0.01s / p95 60029.08s, n=34)
- **`data` key-set variants:** [questEventType, questID, questName] x19; [questEventType, questID, questName, questSuccessOrFailure] x16
- **Fields under `data`:**

```text
data.questEventType  (string, 35/35 records)
    "questActiveEvent"  x19
    "questFinishEvent"  x16
data.questID  (string, 35/35 records)
    15 unique values (see csv/event_unique_values.csv)
data.questName  (string, 35/35 records)
    15 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 16/35 records)
    "Succeeded"  x16
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 26 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (12)
- **Intervals:** median 3.85s (p5 0.72s / p95 2024.31s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "dragEnd"  x13
    "dragStart"  x13
data.featureUsed  (string, 26/26 records)
    "waypoint"  x26
data.location  (object, 26/26 records)
data.location.x  (number, 26/26 records)
    numeric range -770.79 .. 170.342 (14 unique)
data.location.y  (number, 26/26 records)
    numeric range -327.243 .. 157.496 (14 unique)
data.location.z  (number, 26/26 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (12); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1.03s (p5 0.01s / p95 68510.91s, n=13)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolClose"  x7
    "argumentationToolOpen"  x7
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x12
    "Unit 2 – Watershed"  x2
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Pollution Site Data"  x8
    "BackingInfoPanel - "  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 49.90s (p5 11.82s / p95 397041.02s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2)
- **Intervals:** median 51.06s (p5 7.54s / p95 139589.67s, n=5)
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

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 686780.31s (p5 686780.31s / p95 686780.31s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "2"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

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
- `EndOfUnit` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TopographicMapEvent` data.actionType: "dragStart" (13x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (16x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*