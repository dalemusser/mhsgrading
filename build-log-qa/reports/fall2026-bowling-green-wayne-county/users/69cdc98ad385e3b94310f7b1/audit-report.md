# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b1

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b1
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7b1.jsonl
- **Records:** 1876 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7b1
- **Time span:** 2026-04-14T19:42:25.119000+00:00 .. 2026-04-22T19:39:41.219000+00:00 (191h 57m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b1\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 1876 records, 4 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 50 INFO, 5 NOT_TESTED, 34 PASS.
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
| DialogueEvent | 1264 | 67.38 | 1 | 4 | 906 | 2026-04-14T19:42:43.431000+00:00 | 2026-04-22T19:38:45.473000+00:00 | 191h 56m |
| PlayerPositionEvent | 396 | 21.11 | 1 | 4 | 0 | 2026-04-14T19:42:25.119000+00:00 | 2026-04-22T19:39:41.219000+00:00 | 191h 57m |
| Topographic Map Event | 52 | 2.77 | 1 | 2 | 0 | 2026-04-16T19:09:21.125000+00:00 | 2026-04-22T19:03:42.052000+00:00 | 143h 54m |
| argumentationNodeEvent | 51 | 2.72 | 1 | 3 | 0 | 2026-04-14T20:04:22.570000+00:00 | 2026-04-22T19:31:35.398000+00:00 | 191h 27m |
| questEvent | 46 | 2.45 | 1 | 4 | 46 | 2026-04-14T19:42:43.414000+00:00 | 2026-04-22T19:37:14.646000+00:00 | 191h 54m |
| TopographicMapEvent | 28 | 1.49 | 1 | 2 | 0 | 2026-04-16T20:05:59.064000+00:00 | 2026-04-22T19:02:30.041000+00:00 | 142h 56m |
| argumentationToolEvent | 14 | 0.75 | 1 | 2 | 0 | 2026-04-20T20:08:18.950000+00:00 | 2026-04-22T19:28:52.662000+00:00 | 47h 20m |
| argumentationEvent | 13 | 0.69 | 1 | 3 | 0 | 2026-04-14T20:04:17.390000+00:00 | 2026-04-22T19:31:37.321000+00:00 | 191h 27m |
| Soil Key Puzzle | 10 | 0.53 | 1 | 2 | 0 | 2026-04-16T20:02:05.961000+00:00 | 2026-04-22T19:36:21.518000+00:00 | 143h 34m |
| EndOfUnit | 2 | 0.11 | 1 | 2 | 0 | 2026-04-16T18:57:54.887000+00:00 | 2026-04-22T18:55:11.347000+00:00 | 143h 57m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 518236.46s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.191s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 82.932s median 
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
  - Observed: 6.429s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.325s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.507s median 
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
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 396 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 10 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 52 records this build 
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
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
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
  - Observed: D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7b1.jsonl[85] _id=69de9e607957a33870f3b557 ts=2026-04-14T20:06:55.9350000Z`; `69cdc98ad385e3b94310f7b1.jsonl[449] _id=69e66f7b1724f0c9e2f8b69f ts=2026-04-20T18:24:58.0770000Z`; `69cdc98ad385e3b94310f7b1.jsonl[1448] _id=69e677911724f0c9e2f8c091 ts=2026-04-20T18:59:28.9420000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 52 records, TopographicMapEvent: 28 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1263 | 0.0 | 2.654 | 547.08 | 36.488 | 332801.117 | 0.11 | 299 | 7 |
| PlayerPositionEvent | 392 | 29.801 | 30.191 | 1762.483 | 44.852 | 332803.237 | 0.03 | 0 | 7 |
| Topographic Map Event | 51 | 1.303 | 17.925 | 10158.057 | 2139.418 | 341460.49 | 0.01 | 0 | 4 |
| argumentationNodeEvent | 50 | 0.99 | 6.325 | 13784.657 | 92702.392 | 349991.963 | 0.0 | 0 | 3 |
| questEvent | 45 | 0.006 | 196.007 | 15352.694 | 135063.516 | 332948.409 | 0.0 | 4 | 12 |
| TopographicMapEvent | 27 | 0.531 | 6.429 | 19058.925 | 120407.402 | 341465.406 | 0.0 | 0 | 2 |
| argumentationToolEvent | 13 | 0.083 | 1.507 | 13110.286 | 68176.664 | 170334.483 | 0.0 | 0 | 1 |
| argumentationEvent | 12 | 0.108 | 54.3 | 57436.661 | 251116.894 | 349973.523 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 9 | 2.967 | 82.932 | 57428.395 | 273284.733 | 339715.791 | 0.0 | 0 | 4 |
| EndOfUnit | 1 | 518236.46 | 518236.46 | 518236.46 | 518236.46 | 518236.46 | 0.0 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.191s (p5 29.97s, p95 44.85s, n=392) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `108ms: 69cdc98ad385e3b94310f7b1.jsonl[1088] _id=69e922191724f0c9e2faa771 ts=2026-04-22T19:31:37.2130000Z ~ 69cdc98ad385e3b94310f7b1.jsonl[1091] _id=69e9221a1724f0c9e2faa779 ts=2026-04-22T19:31:37.3210000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `979ms: 69cdc98ad385e3b94310f7b1.jsonl[1676] _id=69e687c11724f0c9e2f90197 ts=2026-04-20T20:08:32.8780000Z ~ 69cdc98ad385e3b94310f7b1.jsonl[928] _id=69e687c21724f0c9e2f9019d ts=2026-04-20T20:08:33.8570000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 92h 26m 
  - Evidence: 92h 26m: 69cdc98ad385e3b94310f7b1.jsonl[1426] _id=69e141b41724f0c9e2f712b8 ts=2026-04-16T20:08:18.7580000Z -> 69cdc98ad385e3b94310f7b1.jsonl[354] _id=69e655b41724f0c9e2f8b5b1 ts=2026-04-20T16:34:59.8750000Z; 46h 43m: 69cdc98ad385e3b94310f7b1.jsonl[101] _id=69de9ef47957a33870f3b745 ts=2026-04-14T20:09:24.8060000Z -> 69cdc98ad385e3b94310f7b1.jsonl[122] _id=69e1300b1724f0c9e2f690fe ts=2026-04-16T18:52:58.3260000Z; 46h 38m: 69cdc98ad385e3b94310f7b1.jsonl[967] _id=69e6888a1724f0c9e2f904b9 ts=2026-04-20T20:11:53.3320000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1731] _id=69e9186c1724f0c9e2fa831d ts=2026-04-22T18:50:19.6820000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 299 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7b1.jsonl[1767] _id=69e919901724f0c9e2fa8781 ts=2026-04-22T18:55:11.3630000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1000] _id=69e919a21724f0c9e2fa87c3 ts=2026-04-22T18:55:11.363Z; 3ms: 69cdc98ad385e3b94310f7b1.jsonl[1389] _id=69e141091724f0c9e2f70eea ts=2026-04-16T20:05:26.2530000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1385] _id=69e141091724f0c9e2f70eee ts=2026-04-16T20:05:26.2560000Z; 3ms: 69cdc98ad385e3b94310f7b1.jsonl[99] _id=69de9eb17957a33870f3b699 ts=2026-04-14T20:08:17.3300000Z -> 69cdc98ad385e3b94310f7b1.jsonl[100] _id=69de9eb17957a33870f3b69b ts=2026-04-14T20:08:17.3330000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 69cdc98ad385e3b94310f7b1.jsonl[191] _id=69e131341724f0c9e2f69512 ts=2026-04-16T18:57:54.8870000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1766] _id=69e9198f1724f0c9e2fa877f ts=2026-04-22T18:55:11.3470000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 92h 26m 
  - Evidence: 92h 26m: 69cdc98ad385e3b94310f7b1.jsonl[1425] _id=69e141ae1724f0c9e2f712b4 ts=2026-04-16T20:08:12.5090000Z -> 69cdc98ad385e3b94310f7b1.jsonl[345] _id=69e655b11724f0c9e2f8b5ad ts=2026-04-20T16:34:55.7460000Z; 46h 43m: 69cdc98ad385e3b94310f7b1.jsonl[1277] _id=69de9ede7957a33870f3b721 ts=2026-04-14T20:09:02.1020000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1303] _id=69e12fd41724f0c9e2f69020 ts=2026-04-16T18:52:02.5520000Z; 46h 38m: 69cdc98ad385e3b94310f7b1.jsonl[960] _id=69e688701724f0c9e2f9045f ts=2026-04-20T20:11:27.9590000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1729] _id=69e9185b1724f0c9e2fa82cd ts=2026-04-22T18:50:02.3780000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 21m 
  - Evidence: 94h 21m: 69cdc98ad385e3b94310f7b1.jsonl[1374] _id=69e140421724f0c9e2f70c0e ts=2026-04-16T20:02:08.9650000Z -> 69cdc98ad385e3b94310f7b1.jsonl[340] _id=69e66f451724f0c9e2f8b68b ts=2026-04-20T18:24:04.7560000Z; 48h 13m: 69cdc98ad385e3b94310f7b1.jsonl[1502] _id=69e67cc31724f0c9e2f8d847 ts=2026-04-20T19:21:38.9430000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1857] _id=69e923091724f0c9e2faab1b ts=2026-04-22T19:35:37.0900000Z; 29m 32s: 69cdc98ad385e3b94310f7b1.jsonl[341] _id=69e66f481724f0c9e2f8b68d ts=2026-04-20T18:24:08.0250000Z -> 69cdc98ad385e3b94310f7b1.jsonl[521] _id=69e676351724f0c9e2f8ba79 ts=2026-04-20T18:53:40.7110000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc98ad385e3b94310f7b1.jsonl[1407] _id=69e1412c1724f0c9e2f7100a ts=2026-04-16T20:06:03.0970000Z -> 69cdc98ad385e3b94310f7b1.jsonl[593] _id=69e677001724f0c9e2f8bde9 ts=2026-04-20T18:57:03.5870000Z; 47h 5m: 69cdc98ad385e3b94310f7b1.jsonl[1638] _id=69e685171724f0c9e2f8fa89 ts=2026-04-20T19:57:10.5100000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1015] _id=69e91b381724f0c9e2fa8ea1 ts=2026-04-22T19:02:16.4150000Z; 56m 25s: 69cdc98ad385e3b94310f7b1.jsonl[1345] _id=69e133e91724f0c9e2f6a392 ts=2026-04-16T19:09:27.6690000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1400] _id=69e141231724f0c9e2f70fb4 ts=2026-04-16T20:05:53.3640000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc98ad385e3b94310f7b1.jsonl[1406] _id=69e1412c1724f0c9e2f71006 ts=2026-04-16T20:06:02.9400000Z -> 69cdc98ad385e3b94310f7b1.jsonl[594] _id=69e677051724f0c9e2f8bdf7 ts=2026-04-20T18:57:08.3460000Z; 47h 44m: 69cdc98ad385e3b94310f7b1.jsonl[690] _id=69e67b181724f0c9e2f8d031 ts=2026-04-20T19:14:31.9590000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1793] _id=69e91a7d1724f0c9e2fa8b97 ts=2026-04-22T18:59:09.2320000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 97h 12m 
  - Evidence: 97h 12m: 69cdc98ad385e3b94310f7b1.jsonl[144] _id=69e130681724f0c9e2f69260 ts=2026-04-16T18:54:31.2290000Z -> 69cdc98ad385e3b94310f7b1.jsonl[915] _id=69e6877d1724f0c9e2f90087 ts=2026-04-20T20:07:24.7520000Z; 47h 17m: 69cdc98ad385e3b94310f7b1.jsonl[1686] _id=69e687eb1724f0c9e2f90265 ts=2026-04-20T20:09:14.9790000Z -> 69cdc98ad385e3b94310f7b1.jsonl[885] _id=69e920e51724f0c9e2faa285 ts=2026-04-22T19:26:29.1760000Z; 46h 46m: 69cdc98ad385e3b94310f7b1.jsonl[1263] _id=69de9e5f7957a33870f3b553 ts=2026-04-14T20:06:55.9100000Z -> 69cdc98ad385e3b94310f7b1.jsonl[135] _id=69e130311724f0c9e2f6918e ts=2026-04-16T18:53:36.1180000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 97h 13m 
  - Evidence: 97h 13m: 69cdc98ad385e3b94310f7b1.jsonl[143] _id=69e130611724f0c9e2f69246 ts=2026-04-16T18:54:24.3290000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1670] _id=69e687881724f0c9e2f900c5 ts=2026-04-20T20:07:36.2920000Z; 47h 17m: 69cdc98ad385e3b94310f7b1.jsonl[1689] _id=69e687e91724f0c9e2f90255 ts=2026-04-20T20:09:12.8070000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1630] _id=69e920f51724f0c9e2faa2a9 ts=2026-04-22T19:26:44.9210000Z; 46h 47m: 69cdc98ad385e3b94310f7b1.jsonl[1265] _id=69de9e5a7957a33870f3b543 ts=2026-04-14T20:06:50.8850000Z -> 69cdc98ad385e3b94310f7b1.jsonl[141] _id=69e130591724f0c9e2f69220 ts=2026-04-16T18:54:16.1010000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 18m 
  - Evidence: 47h 18m: 69cdc98ad385e3b94310f7b1.jsonl[928] _id=69e687c21724f0c9e2f9019d ts=2026-04-20T20:08:33.8570000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1658] _id=69e921201724f0c9e2faa379 ts=2026-04-22T19:27:28.3400000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 92h 29m 
  - Evidence: 92h 29m: 69cdc98ad385e3b94310f7b1.jsonl[1398] _id=69e1411f1724f0c9e2f70f8c ts=2026-04-16T20:05:49.8770000Z -> 69cdc98ad385e3b94310f7b1.jsonl[353] _id=69e655b31724f0c9e2f8b5af ts=2026-04-20T16:34:58.2860000Z; 46h 44m: 69cdc98ad385e3b94310f7b1.jsonl[1268] _id=69de9e867957a33870f3b5f7 ts=2026-04-14T20:07:34.0130000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1305] _id=69e12fd61724f0c9e2f69026 ts=2026-04-16T18:52:04.8650000Z; 46h 39m: 69cdc98ad385e3b94310f7b1.jsonl[948] _id=69e6883b1724f0c9e2f9037f ts=2026-04-20T20:10:35.1690000Z -> 69cdc98ad385e3b94310f7b1.jsonl[1730] _id=69e9185d1724f0c9e2fa82d1 ts=2026-04-22T18:50:05.0840000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.006s..0.021s shown 
  - Evidence: 6ms: 69cdc98ad385e3b94310f7b1.jsonl[1306] _id=69e1300c1724f0c9e2f69102 ts=2026-04-16T18:52:58.3580000Z -> 69cdc98ad385e3b94310f7b1.jsonl[124] _id=69e1300c1724f0c9e2f69104 ts=2026-04-16T18:52:58.3640000Z; 8ms: 69cdc98ad385e3b94310f7b1.jsonl[61] _id=69de9d627957a33870f3b1d5 ts=2026-04-14T20:02:42.0180000Z -> 69cdc98ad385e3b94310f7b1.jsonl[57] _id=69de9d627957a33870f3b1d7 ts=2026-04-14T20:02:42.0260000Z; 21ms: 69cdc98ad385e3b94310f7b1.jsonl[28] _id=69de9ae27957a33870f3a667 ts=2026-04-14T19:52:02.7680000Z -> 69cdc98ad385e3b94310f7b1.jsonl[27] _id=69de9ae37957a33870f3a66b ts=2026-04-14T19:52:02.7890000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc98ad385e3b94310f7b1.jsonl:69cdc98ad385e3b94310f7b1, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7b1.jsonl[1374] _id=69e140421724f0c9e2f70c0e ts=2026-04-16T20:02:08.9650000Z`; `69cdc98ad385e3b94310f7b1.jsonl[341] _id=69e66f481724f0c9e2f8b68d ts=2026-04-20T18:24:08.0250000Z`; `69cdc98ad385e3b94310f7b1.jsonl[529] _id=69e676381724f0c9e2f8ba81 ts=2026-04-20T18:53:43.6780000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 28 record(s) match the trigger in 69cdc98ad385e3b94310f7b1.jsonl:69cdc98ad385e3b94310f7b1, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7b1.jsonl[1405] _id=69e141281724f0c9e2f70fd0 ts=2026-04-16T20:05:59.0640000Z`; `69cdc98ad385e3b94310f7b1.jsonl[1406] _id=69e1412c1724f0c9e2f71006 ts=2026-04-16T20:06:02.9400000Z`; `69cdc98ad385e3b94310f7b1.jsonl[594] _id=69e677051724f0c9e2f8bdf7 ts=2026-04-20T18:57:08.3460000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7b1.jsonl[1556] _id=69e681381724f0c9e2f8ed43 ts=2026-04-20T19:40:39.4060000Z`; `69cdc98ad385e3b94310f7b1.jsonl[1033] _id=69e91c5e1724f0c9e2fa93c5 ts=2026-04-22T19:07:10.3480000Z`; `69cdc98ad385e3b94310f7b1.jsonl[1049] _id=69e91d521724f0c9e2fa979b ts=2026-04-22T19:11:13.6460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7b1.jsonl[1091] _id=69e9221a1724f0c9e2faa779 ts=2026-04-22T19:31:37.3210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7b1.jsonl[1684] _id=69e9212d1724f0c9e2faa3b1 ts=2026-04-22T19:27:41.1280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 125 unmatched 'DialogueStartEvent' (totals: 240 start, 118 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 8 unmatched 'questActiveEvent' (totals: 27 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.78s, min -19.25s, max -0.03s over 1876 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b1\coverage.yaml

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
  - Observed: 52 records 
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

### `DialogueEvent` — 1264 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (778); Unit 3 Dev (246); Unit 1 Dev (232); Unit 3 Dungeon Dev (8)
- **eventKey:** present on 906 of 1264 records
- **Intervals:** median 2.65s (p5 0.01s / p95 36.49s, n=1263)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x906; [conversationId, dialogueEventType] x358
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1264/1264 records)
    numeric range 8 .. 103 (31 unique)
data.dialogueEventType  (string, 1264/1264 records)
    "DialogueNodeEvent"  x906
    "DialogueStartEvent"  x240
    "DialogueFinishEvent"  x118
data.nodeId  (number, 906/1264 records)
    numeric range 0 .. 290 (201 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 396 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (243); Unit 3 Dev (80); Unit 1 Dev (66); Unit 3 Dungeon Dev (7)
- **Intervals:** median 30.19s (p5 29.97s / p95 44.85s, n=392)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 396/396 records)
data.position.x  (number, 396/396 records)
    numeric range -615.275 .. 1589.82 (200 unique)
data.position.y  (number, 396/396 records)
    numeric range -114.326 .. 157.757 (150 unique)
data.position.z  (number, 396/396 records)
    numeric range -963.561 .. 2244.63 (200 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 52 records

- **Scenes:** Unit 2 Prod (Refactor) (48); Unit 3 Dev (4)
- **Intervals:** median 17.93s (p5 3.70s / p95 2139.42s, n=51)
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "MapCloseEvent"  x26
    "MapOpenEvent"  x26
data.featureUsed  (string, 52/52 records)
    "Map"  x52
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 51 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (29); Unit 1 Dev (11); Unit 2 Prod (Refactor) (11)
- **Intervals:** median 6.33s (p5 1.14s / p95 92702.39s, n=50)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 51/51 records)
    "argumentationNodeAdd"  x33
    "argumentationNodeRemove"  x18
data.argumentationTitle  (string, 51/51 records)
    "Unit 3 - Pollution Upstream"  x29
    "Unit 2 – Watershed"  x11
    "Unit 1 - Freshwater"  x6
    "Unit 1 - Argumentation Tutorial"  x5
data.nodeName  (string, 51/51 records)
    "1"  x10
    "I"  x8
    "3"  x6
    "B"  x6
    "A"  x5
    "2"  x4
    "4"  x4
    "C"  x4
    "II"  x3
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 46 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 1 Dev (17); Unit 3 Dev (5); Unit 3 Dungeon Dev (1)
- **eventKey:** present on 46 of 46 records
- **Intervals:** median 196.01s (p5 0.02s / p95 135063.52s, n=45)
- **`data` key-set variants:** [questEventType, questID, questName] x27; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Fields under `data`:**

```text
data.questEventType  (string, 46/46 records)
    "questActiveEvent"  x27
    "questFinishEvent"  x19
data.questID  (string, 46/46 records)
    15 unique values (see csv/event_unique_values.csv)
data.questName  (string, 46/46 records)
    15 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/46 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 28 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (4)
- **Intervals:** median 6.43s (p5 2.16s / p95 120407.40s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "dragEnd"  x14
    "dragStart"  x14
data.featureUsed  (string, 28/28 records)
    "waypoint"  x28
data.location  (object, 28/28 records)
data.location.x  (number, 28/28 records)
    numeric range -770.79 .. 185.933 (15 unique)
data.location.y  (number, 28/28 records)
    numeric range -311.652 .. 269.468 (15 unique)
data.location.z  (number, 28/28 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (6)
- **Intervals:** median 1.51s (p5 0.09s / p95 68176.66s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolClose"  x7
    "argumentationToolOpen"  x7
data.argumentationTitle  (string, 14/14 records)
    "Unit 2 – Watershed"  x8
    "Unit 3 - Pollution Upstream"  x6
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Waterfall Data"  x6
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 54.30s (p5 8.01s / p95 251116.89s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 13/13 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (2)
- **Intervals:** median 82.93s (p5 2.98s / p95 273284.73s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/10 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/10 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 518236.46s (p5 518236.46s / p95 518236.46s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "2"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TopographicMapEvent` data.actionType: "dragStart" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (18x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*