# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f786

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f786
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f786.jsonl
- **Records:** 1922 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f786
- **Time span:** 2026-04-14T13:59:51.093000+00:00 .. 2026-04-22T14:29:29.240000+00:00 (192h 29m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f786\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1922 records, 5 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 52 INFO, 2 NOT_TESTED, 36 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1292 | 67.22 | 1 | 5 | 892 | 2026-04-14T14:00:09.804000+00:00 | 2026-04-22T14:28:54.411000+00:00 | 192h 28m |
| PlayerPositionEvent | 452 | 23.52 | 1 | 5 | 0 | 2026-04-14T13:59:51.093000+00:00 | 2026-04-22T14:29:29.240000+00:00 | 192h 29m |
| Topographic Map Event | 52 | 2.71 | 1 | 2 | 0 | 2026-04-14T14:23:28.369000+00:00 | 2026-04-22T13:59:55.773000+00:00 | 191h 36m |
| questEvent | 47 | 2.45 | 1 | 5 | 47 | 2026-04-14T14:00:09.777000+00:00 | 2026-04-22T14:28:44.422000+00:00 | 192h 28m |
| argumentationNodeEvent | 32 | 1.66 | 1 | 2 | 0 | 2026-04-14T14:11:27.638000+00:00 | 2026-04-16T20:48:35.062000+00:00 | 54h 37m |
| TopographicMapEvent | 28 | 1.46 | 1 | 1 | 0 | 2026-04-20T13:38:01.030000+00:00 | 2026-04-22T13:59:08.049000+00:00 | 48h 21m |
| Soil Key Puzzle | 6 | 0.31 | 1 | 2 | 0 | 2026-04-16T13:46:56.068000+00:00 | 2026-04-22T14:10:27.873000+00:00 | 144h 23m |
| argumentationEvent | 6 | 0.31 | 1 | 2 | 0 | 2026-04-14T14:11:20.654000+00:00 | 2026-04-16T20:48:36.412000+00:00 | 54h 37m |
| argumentationToolEvent | 4 | 0.21 | 1 | 1 | 0 | 2026-04-16T20:47:10.213000+00:00 | 2026-04-16T20:47:11.897000+00:00 | 1.7s |
| EndOfUnit | 2 | 0.1 | 1 | 2 | 0 | 2026-04-14T14:15:55.998000+00:00 | 2026-04-16T20:50:42.542000+00:00 | 54h 34m |
| crash | 1 | 0.05 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.773s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 196486.544s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.013s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 58.375s median 
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
  - Observed: 5.25s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 3.59s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.62s median 
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
  - Observed: MainMenu; Transition; Unit 3 Dungeon Dev; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
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
  - Observed: U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 32 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; C 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 36; 40; 41; 43; 44; 45; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f786.jsonl[1041] _id=69de4b777957a33870f34c3f ts=2026-04-14T14:13:10.7440000Z`; `69cdc965d385e3b94310f786.jsonl[185] _id=69e0ea617957a33870f51da3 ts=2026-04-16T13:55:45.2510000Z`; `69cdc965d385e3b94310f786.jsonl[559] _id=69e14b241724f0c9e2f71598 ts=2026-04-16T20:48:36.4520000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 52 records, TopographicMapEvent: 28 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1291 | 0.002 | 1.773 | 536.735 | 45.039 | 318433.208 | 0.11 | 351 | 7 |
| PlayerPositionEvent | 447 | 23.762 | 30.013 | 837.721 | 42.474 | 169657.641 | 0.07 | 0 | 4 |
| Topographic Map Event | 51 | 0.182 | 26.06 | 13525.243 | 86056.159 | 342666.45 | 0.0 | 0 | 6 |
| questEvent | 46 | 0.008 | 147.991 | 15063.362 | 132679.344 | 319352.782 | 0.0 | 6 | 9 |
| argumentationNodeEvent | 31 | 0.75 | 3.59 | 6342.82 | 29.305 | 196436.471 | 0.01 | 0 | 1 |
| TopographicMapEvent | 27 | 0.382 | 5.25 | 6446.927 | 1163.871 | 170617.231 | 0.01 | 0 | 3 |
| Soil Key Puzzle | 5 | 2.987 | 58.375 | 103962.361 | 415028.418 | 518479.594 | 0.0 | 0 | 2 |
| argumentationEvent | 5 | 13.716 | 64.199 | 39327.152 | 157150.861 | 196409.538 | 0.0 | 0 | 1 |
| argumentationToolEvent | 3 | 0.055 | 0.62 | 0.561 | 0.97 | 1.009 | 106.89 | 0 | 0 |
| EndOfUnit | 1 | 196486.544 | 196486.544 | 196486.544 | 196486.544 | 196486.544 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.013s (p5 29.96s, p95 42.47s, n=447) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `642ms: 69cdc965d385e3b94310f786.jsonl[104] _id=69de4e067957a33870f35e42 ts=2026-04-14T14:24:06.4290000Z ~ 69cdc965d385e3b94310f786.jsonl[106] _id=69de4e077957a33870f35e48 ts=2026-04-14T14:24:07.0710000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `675ms: 69cdc965d385e3b94310f786.jsonl[541] _id=69e14ace1724f0c9e2f7154e ts=2026-04-16T20:47:10.2130000Z ~ 69cdc965d385e3b94310f786.jsonl[543] _id=69e14acf1724f0c9e2f71552 ts=2026-04-16T20:47:10.8880000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 88h 27m 
  - Evidence: 88h 27m: 69cdc965d385e3b94310f786.jsonl[626] _id=69e14ba31724f0c9e2f71616 ts=2026-04-16T20:50:42.5620000Z -> 69cdc965d385e3b94310f786.jsonl[632] _id=69e627841724f0c9e2f84aa9 ts=2026-04-20T13:17:55.7700000Z; 47h 11m: 69cdc965d385e3b94310f786.jsonl[1128] _id=69de4ec07957a33870f36264 ts=2026-04-14T14:27:11.9180000Z -> 69cdc965d385e3b94310f786.jsonl[108] _id=69e0e67f7957a33870f5035b ts=2026-04-16T13:39:10.9520000Z; 46h 46m: 69cdc965d385e3b94310f786.jsonl[729] _id=69e639731724f0c9e2f8b45d ts=2026-04-20T14:34:25.4490000Z -> 69cdc965d385e3b94310f786.jsonl[1683] _id=69e8cb3b1724f0c9e2fa10db ts=2026-04-22T13:20:59.1850000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 351 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f786.jsonl[1056] _id=69de4bd17957a33870f34ee1 ts=2026-04-14T14:14:41.2080000Z -> 69cdc965d385e3b94310f786.jsonl[89] _id=69de4bd17957a33870f34ee3 ts=2026-04-14T14:14:41.2100000Z; 3ms: 69cdc965d385e3b94310f786.jsonl[1048] _id=69de4bb97957a33870f34e33 ts=2026-04-14T14:14:16.7890000Z -> 69cdc965d385e3b94310f786.jsonl[1051] _id=69de4bb97957a33870f34e35 ts=2026-04-14T14:14:16.7920000Z; 3ms: 69cdc965d385e3b94310f786.jsonl[1049] _id=69de4bb17957a33870f34e05 ts=2026-04-14T14:14:09.1410000Z -> 69cdc965d385e3b94310f786.jsonl[1050] _id=69de4bb17957a33870f34e07 ts=2026-04-14T14:14:09.1440000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 54h 34m 
  - Evidence: 54h 34m: 69cdc965d385e3b94310f786.jsonl[1071] _id=69de4c1c7957a33870f351b3 ts=2026-04-14T14:15:55.9980000Z -> 69cdc965d385e3b94310f786.jsonl[625] _id=69e14ba21724f0c9e2f71614 ts=2026-04-16T20:50:42.5420000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 7m 
  - Evidence: 47h 7m: 69cdc965d385e3b94310f786.jsonl[1142] _id=69de4fbd7957a33870f36a78 ts=2026-04-14T14:31:24.8580000Z -> 69cdc965d385e3b94310f786.jsonl[1143] _id=69e0e6777957a33870f50305 ts=2026-04-16T13:39:02.4990000Z; 46h 45m: 69cdc965d385e3b94310f786.jsonl[1676] _id=69e639951724f0c9e2f8b50c ts=2026-04-20T14:34:59.9440000Z -> 69cdc965d385e3b94310f786.jsonl[732] _id=69e8cb0c1724f0c9e2fa0fed ts=2026-04-22T13:20:11.7960000Z; 5h 57m: 69cdc965d385e3b94310f786.jsonl[1439] _id=69e0f3ba7957a33870f55909 ts=2026-04-16T14:35:36.6720000Z -> 69cdc965d385e3b94310f786.jsonl[1440] _id=69e1479c1724f0c9e2f7143c ts=2026-04-16T20:33:31.9090000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 1m 
  - Evidence: 144h 1m: 69cdc965d385e3b94310f786.jsonl[240] _id=69e0ed557957a33870f52d27 ts=2026-04-16T14:08:21.1450000Z -> 69cdc965d385e3b94310f786.jsonl[1848] _id=69e8d6a41724f0c9e2fa5a9b ts=2026-04-22T14:09:40.7390000Z; 20m 23s: 69cdc965d385e3b94310f786.jsonl[129] _id=69e0e8537957a33870f50f4b ts=2026-04-16T13:46:59.0550000Z -> 69cdc965d385e3b94310f786.jsonl[234] _id=69e0ed1b7957a33870f52bbd ts=2026-04-16T14:07:22.7700000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 11m 
  - Evidence: 95h 11m: 69cdc965d385e3b94310f786.jsonl[370] _id=69e0f19a7957a33870f546b7 ts=2026-04-16T14:26:34.5940000Z -> 69cdc965d385e3b94310f786.jsonl[1471] _id=69e62c261724f0c9e2f8664f ts=2026-04-20T13:37:41.0440000Z; 47h 28m: 69cdc965d385e3b94310f786.jsonl[1122] _id=69de4e097957a33870f35e5b ts=2026-04-14T14:24:09.4760000Z -> 69cdc965d385e3b94310f786.jsonl[1221] _id=69e0e98c7957a33870f517b5 ts=2026-04-16T13:52:11.5730000Z; 47h 24m: 69cdc965d385e3b94310f786.jsonl[692] _id=69e6318b1724f0c9e2f88467 ts=2026-04-20T14:00:42.0160000Z -> 69cdc965d385e3b94310f786.jsonl[753] _id=69e8cc281724f0c9e2fa1599 ts=2026-04-22T13:24:56.4030000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 23m 
  - Evidence: 47h 23m: 69cdc965d385e3b94310f786.jsonl[1579] _id=69e631881724f0c9e2f88457 ts=2026-04-20T14:00:38.9020000Z -> 69cdc965d385e3b94310f786.jsonl[751] _id=69e8cc001724f0c9e2fa14bf ts=2026-04-22T13:24:16.1330000Z; 20m 17s: 69cdc965d385e3b94310f786.jsonl[1480] _id=69e62c5e1724f0c9e2f8685f ts=2026-04-20T13:38:37.2030000Z -> 69cdc965d385e3b94310f786.jsonl[1570] _id=69e631201724f0c9e2f881d5 ts=2026-04-20T13:58:54.6510000Z; 17m 18s: 69cdc965d385e3b94310f786.jsonl[786] _id=69e8d0181724f0c9e2fa31fd ts=2026-04-22T13:41:44.5910000Z -> 69cdc965d385e3b94310f786.jsonl[1816] _id=69e8d4271724f0c9e2fa4873 ts=2026-04-22T13:59:03.4490000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 54h 33m 
  - Evidence: 54h 33m: 69cdc965d385e3b94310f786.jsonl[1033] _id=69de4b767957a33870f34c3b ts=2026-04-14T14:13:10.7220000Z -> 69cdc965d385e3b94310f786.jsonl[537] _id=69e14ab01724f0c9e2f71544 ts=2026-04-16T20:46:40.2600000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 54h 33m 
  - Evidence: 54h 33m: 69cdc965d385e3b94310f786.jsonl[1039] _id=69de4b6f7957a33870f34c01 ts=2026-04-14T14:13:03.0610000Z -> 69cdc965d385e3b94310f786.jsonl[540] _id=69e14ac31724f0c9e2f7154a ts=2026-04-16T20:46:59.5320000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 88h 42m 
  - Evidence: 88h 42m: 69cdc965d385e3b94310f786.jsonl[617] _id=69e14b9f1724f0c9e2f7160c ts=2026-04-16T20:50:39.5170000Z -> 69cdc965d385e3b94310f786.jsonl[1455] _id=69e62b191724f0c9e2f85e29 ts=2026-04-20T13:33:12.2990000Z; 47h 21m: 69cdc965d385e3b94310f786.jsonl[1081] _id=69de4c957957a33870f355a7 ts=2026-04-14T14:17:56.8490000Z -> 69cdc965d385e3b94310f786.jsonl[1144] _id=69e0e67f7957a33870f50355 ts=2026-04-16T13:39:09.1160000Z; 47h 4m: 69cdc965d385e3b94310f786.jsonl[704] _id=69e635001724f0c9e2f89895 ts=2026-04-20T14:15:26.7880000Z -> 69cdc965d385e3b94310f786.jsonl[1679] _id=69e8cb0e1724f0c9e2fa0ff9 ts=2026-04-22T13:20:14.4990000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.008s..0.011s shown 
  - Evidence: 8ms: 69cdc965d385e3b94310f786.jsonl[63] _id=69de4af07957a33870f348c9 ts=2026-04-14T14:10:56.1500000Z -> 69cdc965d385e3b94310f786.jsonl[64] _id=69de4af07957a33870f348cb ts=2026-04-14T14:10:56.1580000Z; 9ms: 69cdc965d385e3b94310f786.jsonl[25] _id=69de49227957a33870f33ba5 ts=2026-04-14T14:03:13.9660000Z -> 69cdc965d385e3b94310f786.jsonl[24] _id=69de49227957a33870f33ba7 ts=2026-04-14T14:03:13.9750000Z; 11ms: 69cdc965d385e3b94310f786.jsonl[36] _id=69de49b67957a33870f33fe9 ts=2026-04-14T14:05:41.9540000Z -> 69cdc965d385e3b94310f786.jsonl[957] _id=69de49b67957a33870f33feb ts=2026-04-14T14:05:41.9650000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc965d385e3b94310f786.jsonl:69cdc965d385e3b94310f786, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f786.jsonl[129] _id=69e0e8537957a33870f50f4b ts=2026-04-16T13:46:59.0550000Z`; `69cdc965d385e3b94310f786.jsonl[240] _id=69e0ed557957a33870f52d27 ts=2026-04-16T14:08:21.1450000Z`; `69cdc965d385e3b94310f786.jsonl[857] _id=69e8d6d31724f0c9e2fa5c27 ts=2026-04-22T14:10:27.8730000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 28 record(s) match the trigger in 69cdc965d385e3b94310f786.jsonl:69cdc965d385e3b94310f786, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f786.jsonl[1473] _id=69e62c3a1724f0c9e2f866e1 ts=2026-04-20T13:38:01.0300000Z`; `69cdc965d385e3b94310f786.jsonl[1474] _id=69e62c3f1724f0c9e2f86713 ts=2026-04-20T13:38:06.3760000Z`; `69cdc965d385e3b94310f786.jsonl[1479] _id=69e62c5d1724f0c9e2f8684f ts=2026-04-20T13:38:36.1250000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f786.jsonl[318] _id=69e0f0ca7957a33870f54123 ts=2026-04-16T14:23:05.6340000Z`; `69cdc965d385e3b94310f786.jsonl[660] _id=69e62fa01724f0c9e2f87a2b ts=2026-04-20T13:52:31.3290000Z`; `69cdc965d385e3b94310f786.jsonl[672] _id=69e62fed1724f0c9e2f87bb1 ts=2026-04-20T13:53:47.2330000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc965d385e3b94310f786.jsonl[1811] _id=69e8d3571724f0c9e2fa4401 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 179 unmatched 'DialogueStartEvent' (totals: 288 start, 112 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 28 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.29s, min -5.20s, max +0.08s over 1921 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f786\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=partial, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 52 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `DialogueEvent` — 1292 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (677); Unit 3 Dev (333); Unit 1 Dev (179); Unit 4 Dev - Dungeon (78); Unit 4 Dev (25)
- **eventKey:** present on 892 of 1292 records
- **Intervals:** median 1.77s (p5 0.01s / p95 45.04s, n=1291)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x892; [conversationId, dialogueEventType] x400
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1292/1292 records)
    numeric range 8 .. 103 (28 unique)
data.dialogueEventType  (string, 1292/1292 records)
    "DialogueNodeEvent"  x892
    "DialogueStartEvent"  x288
    "DialogueFinishEvent"  x112
data.nodeId  (number, 892/1292 records)
    numeric range 0 .. 290 (200 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 452 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (194); Unit 2 Prod (Refactor) (172); Unit 1 Dev (33); Unit 4 Dev - Dungeon (32); Unit 4 Dev (21)
- **Intervals:** median 30.01s (p5 29.96s / p95 42.47s, n=447)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 452/452 records)
data.position.x  (number, 452/452 records)
    numeric range -106.24 .. 1424.93 (206 unique)
data.position.y  (number, 452/452 records)
    numeric range -115.127 .. 159.686 (169 unique)
data.position.z  (number, 452/452 records)
    numeric range -639.68 .. 1827.26 (207 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 52 records

- **Scenes:** Unit 3 Dev (36); Unit 2 Prod (Refactor) (16)
- **Intervals:** median 26.06s (p5 1.92s / p95 86056.16s, n=51)
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "MapCloseEvent"  x26
    "MapOpenEvent"  x26
data.featureUsed  (string, 52/52 records)
    "Map"  x52
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 47 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev - Dungeon (7); Unit 4 Dev (1)
- **eventKey:** present on 47 of 47 records
- **Intervals:** median 147.99s (p5 0.01s / p95 132679.34s, n=46)
- **`data` key-set variants:** [questEventType, questID, questName] x28; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Fields under `data`:**

```text
data.questEventType  (string, 47/47 records)
    "questActiveEvent"  x28
    "questFinishEvent"  x19
data.questID  (string, 47/47 records)
    19 unique values (see csv/event_unique_values.csv)
data.questName  (string, 47/47 records)
    19 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/47 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 32 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (15)
- **Intervals:** median 3.59s (p5 1.19s / p95 29.30s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "argumentationNodeAdd"  x20
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 32/32 records)
    "Unit 1 - Freshwater"  x15
    "Unit 2 – Watershed"  x15
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 32/32 records)
    "1"  x7
    "I"  x6
    "A"  x5
    "B"  x5
    "II"  x5
    "D"  x4
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 28 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (28)
- **Intervals:** median 5.25s (p5 0.84s / p95 1163.87s, n=27)
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
    numeric range -816.588 .. 397.519 (15 unique)
data.location.y  (number, 28/28 records)
    numeric range -471.825 .. 270.886 (15 unique)
data.location.z  (number, 28/28 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 4 Dev (2)
- **Intervals:** median 58.38s (p5 11.82s / p95 415028.42s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/6 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/6 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 6 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 64.20s (p5 17.40s / p95 157150.86s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationSessionClose"  x3
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 6/6 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (4)
- **Intervals:** median 0.62s (p5 0.11s / p95 0.97s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x2
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 2 – Watershed"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Watershed Graph"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 196486.54s (p5 196486.54s / p95 196486.54s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "2"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 1/1 records)
    "runtime_error"  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TopographicMapEvent` data.actionType: "dragStart" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*