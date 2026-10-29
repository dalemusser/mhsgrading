# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f759

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f759
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f759.jsonl
- **Records:** 1006 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f759
- **Time span:** 2026-04-13T19:32:06.645000+00:00 .. 2026-04-23T20:10:41.315000+00:00 (240h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f759\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **9 event types**, 1006 records, 2 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 42 INFO, 6 NOT_TESTED, 31 PASS.
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
| DialogueEvent | 710 | 70.58 | 1 | 2 | 536 | 2026-04-13T19:32:24.589000+00:00 | 2026-04-23T20:10:38.639000+00:00 | 240h 38m |
| PlayerPositionEvent | 236 | 23.46 | 1 | 2 | 0 | 2026-04-13T19:32:06.645000+00:00 | 2026-04-23T20:10:41.315000+00:00 | 240h 38m |
| questEvent | 23 | 2.29 | 1 | 2 | 23 | 2026-04-13T19:32:24.574000+00:00 | 2026-04-23T19:57:10.444000+00:00 | 240h 24m |
| Topographic Map Event | 14 | 1.39 | 1 | 1 | 0 | 2026-04-17T19:16:00.293000+00:00 | 2026-04-17T19:53:08.094000+00:00 | 37m 7s |
| argumentationNodeEvent | 10 | 0.99 | 1 | 1 | 0 | 2026-04-13T19:56:43.833000+00:00 | 2026-04-13T19:59:53.997000+00:00 | 3m 10s |
| TopographicMapEvent | 5 | 0.5 | 1 | 1 | 0 | 2026-04-17T19:21:02.595000+00:00 | 2026-04-17T19:25:26.786000+00:00 | 4m 24s |
| argumentationEvent | 4 | 0.4 | 1 | 1 | 0 | 2026-04-13T19:56:35.504000+00:00 | 2026-04-13T19:59:55.566000+00:00 | 3m 20s |
| EndOfUnit | 2 | 0.2 | 1 | 1 | 0 | 2026-04-13T20:03:57.933000+00:00 | 2026-04-13T20:03:57.933000+00:00 | 0.0s |
| Soil Key Puzzle | 2 | 0.2 | 1 | 1 | 0 | 2026-04-17T19:31:14.746000+00:00 | 2026-04-17T19:35:55.462000+00:00 | 4m 40s |

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
  - Observed: 280.716s median 
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
  - Observed: 64.802s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.564s median 
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
  - Observed: MainMenu; Transition; Unit 3 Dev; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 236 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 14 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
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
  - Observed: 10 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 71 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f759.jsonl[70] _id=69dd4b3c7957a33870f2b41f ts=2026-04-13T19:59:55.5920000Z`; `69cdc937d385e3b94310f759.jsonl[607] _id=69e2880b1724f0c9e2f7a97e ts=2026-04-17T19:20:42.9530000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 14 records, TopographicMapEvent: 5 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 709 | 0.003 | 3.787 | 1221.853 | 39.236 | 517682.142 | 0.05 | 152 | 2 |
| PlayerPositionEvent | 234 | 29.909 | 30.008 | 3702.032 | 32.803 | 517651.313 | 0.02 | 0 | 2 |
| questEvent | 22 | 0.002 | 210.277 | 39340.267 | 324231.594 | 518945.265 | 0.0 | 3 | 6 |
| Topographic Map Event | 13 | 2.724 | 27.082 | 171.369 | 776.139 | 1616.223 | 0.35 | 0 | 1 |
| argumentationNodeEvent | 9 | 1.605 | 6.564 | 21.129 | 79.565 | 116.83 | 2.84 | 0 | 0 |
| TopographicMapEvent | 4 | 2.511 | 64.802 | 66.048 | 130.852 | 132.077 | 0.91 | 0 | 0 |
| argumentationEvent | 3 | 44.833 | 73.655 | 66.687 | 80.782 | 81.574 | 0.9 | 0 | 0 |
| EndOfUnit | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1 | 0 |
| Soil Key Puzzle | 1 | 280.716 | 280.716 | 280.716 | 280.716 | 280.716 | 0.21 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.96s, p95 32.80s, n=234) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc937d385e3b94310f759.jsonl[405] _id=69dd4c2e7957a33870f2b801 ts=2026-04-13T20:03:57.9330000Z ~ 69cdc937d385e3b94310f759.jsonl[415] _id=69dd4c407957a33870f2b863 ts=2026-04-13T20:03:57.933Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 48m 
  - Evidence: 143h 48m: 69cdc937d385e3b94310f759.jsonl[881] _id=69e2937d1724f0c9e2f7dc40 ts=2026-04-17T20:09:32.8270000Z -> 69cdc937d385e3b94310f759.jsonl[889] _id=69ea79af1724f0c9e2fb634b ts=2026-04-23T19:57:34.9690000Z; 94h 43m: 69cdc937d385e3b94310f759.jsonl[434] _id=69dd4dab7957a33870f2bcb9 ts=2026-04-13T20:10:18.3170000Z -> 69cdc937d385e3b94310f759.jsonl[440] _id=69e281a41724f0c9e2f79060 ts=2026-04-17T18:53:23.6940000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 152 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f759.jsonl[133] _id=69e284c11724f0c9e2f79c20 ts=2026-04-17T19:06:40.3880000Z -> 69cdc937d385e3b94310f759.jsonl[516] _id=69e284c11724f0c9e2f79c22 ts=2026-04-17T19:06:40.3910000Z; 3ms: 69cdc937d385e3b94310f759.jsonl[407] _id=69dd4bc27957a33870f2b63b ts=2026-04-13T20:02:09.8190000Z -> 69cdc937d385e3b94310f759.jsonl[93] _id=69dd4bc27957a33870f2b63d ts=2026-04-13T20:02:09.8220000Z; 3ms: 69cdc937d385e3b94310f759.jsonl[738] _id=69e28db11724f0c9e2f7c038 ts=2026-04-17T19:44:48.5350000Z -> 69cdc937d385e3b94310f759.jsonl[740] _id=69e28db11724f0c9e2f7c03a ts=2026-04-17T19:44:48.5380000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f759.jsonl[405] _id=69dd4c2e7957a33870f2b801 ts=2026-04-13T20:03:57.9330000Z -> 69cdc937d385e3b94310f759.jsonl[415] _id=69dd4c407957a33870f2b863 ts=2026-04-13T20:03:57.933Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 47m 
  - Evidence: 143h 47m: 69cdc937d385e3b94310f759.jsonl[883] _id=69e293801724f0c9e2f7dc52 ts=2026-04-17T20:09:36.3500000Z -> 69cdc937d385e3b94310f759.jsonl[884] _id=69ea79941724f0c9e2fb6319 ts=2026-04-23T19:57:07.6630000Z; 94h 43m: 69cdc937d385e3b94310f759.jsonl[435] _id=69dd4d977957a33870f2bc83 ts=2026-04-13T20:09:58.6210000Z -> 69cdc937d385e3b94310f759.jsonl[438] _id=69e281a11724f0c9e2f7905c ts=2026-04-17T18:53:20.0220000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 26m 56s 
  - Evidence: 26m 56s: 69cdc937d385e3b94310f759.jsonl[641] _id=69e289461724f0c9e2f7ae70 ts=2026-04-17T19:25:57.6140000Z -> 69cdc937d385e3b94310f759.jsonl[825] _id=69e28f961724f0c9e2f7cdba ts=2026-04-17T19:52:53.8370000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 144h 9m 
  - Evidence: 144h 9m: 69cdc937d385e3b94310f759.jsonl[779] _id=69e28e751724f0c9e2f7c764 ts=2026-04-17T19:48:05.1790000Z -> 69cdc937d385e3b94310f759.jsonl[886] _id=69ea79961724f0c9e2fb6321 ts=2026-04-23T19:57:10.4440000Z; 94h 47m: 69cdc937d385e3b94310f759.jsonl[424] _id=69dd4ca17957a33870f2b9ff ts=2026-04-13T20:05:52.9800000Z -> 69cdc937d385e3b94310f759.jsonl[439] _id=69e281a31724f0c9e2f7905e ts=2026-04-17T18:53:22.2820000Z; 14m 55s: 69cdc937d385e3b94310f759.jsonl[579] _id=69e286e31724f0c9e2f7a480 ts=2026-04-17T19:15:47.2070000Z -> 69cdc937d385e3b94310f759.jsonl[660] _id=69e28a621724f0c9e2f7b258 ts=2026-04-17T19:30:42.3470000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.018s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f759.jsonl[52] _id=69dd4a0b7957a33870f2afc9 ts=2026-04-13T19:54:50.4150000Z -> 69cdc937d385e3b94310f759.jsonl[363] _id=69dd4a0b7957a33870f2afcb ts=2026-04-13T19:54:50.4170000Z; 10ms: 69cdc937d385e3b94310f759.jsonl[290] _id=69dd474d7957a33870f2a555 ts=2026-04-13T19:43:08.7730000Z -> 69cdc937d385e3b94310f759.jsonl[291] _id=69dd474d7957a33870f2a557 ts=2026-04-13T19:43:08.7830000Z; 18ms: 69cdc937d385e3b94310f759.jsonl[18] _id=69dd46837957a33870f2a2b3 ts=2026-04-13T19:39:46.3200000Z -> 69cdc937d385e3b94310f759.jsonl[19] _id=69dd46837957a33870f2a2b5 ts=2026-04-13T19:39:46.3380000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 1 record(s) match the trigger in 69cdc937d385e3b94310f759.jsonl:69cdc937d385e3b94310f759, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f759.jsonl[683] _id=69e28b9b1724f0c9e2f7b68a ts=2026-04-17T19:35:55.4620000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc937d385e3b94310f759.jsonl:69cdc937d385e3b94310f759, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f759.jsonl[611] _id=69e2881f1724f0c9e2f7a9ae ts=2026-04-17T19:21:02.5950000Z`; `69cdc937d385e3b94310f759.jsonl[615] _id=69e288241724f0c9e2f7a9c4 ts=2026-04-17T19:21:08.2850000Z`; `69cdc937d385e3b94310f759.jsonl[566] _id=69e288a01724f0c9e2f7ac52 ts=2026-04-17T19:23:12.1980000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f759.jsonl[796] _id=69e28edb1724f0c9e2f7c9fa ts=2026-04-17T19:49:46.7020000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 47 unmatched 'DialogueStartEvent' (totals: 110 start, 64 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 3 unmatched 'questActiveEvent' (totals: 13 start, 10 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.60s, min -18.22s, max -0.08s over 1006 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f759\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | skipped |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=skipped, Unit4=skipped 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 14 records 
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

### `DialogueEvent` — 710 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (509); Unit 1 Dev (201)
- **eventKey:** present on 536 of 710 records
- **Intervals:** median 3.79s (p5 0.01s / p95 39.24s, n=709)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x536; [conversationId, dialogueEventType] x174
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 710/710 records)
    numeric range 8 .. 74 (20 unique)
data.dialogueEventType  (string, 710/710 records)
    "DialogueNodeEvent"  x536
    "DialogueStartEvent"  x110
    "DialogueFinishEvent"  x64
data.nodeId  (number, 536/710 records)
    numeric range 0 .. 290 (175 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 236 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (172); Unit 1 Dev (64)
- **Intervals:** median 30.01s (p5 29.96s / p95 32.80s, n=234)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 236/236 records)
data.position.x  (number, 236/236 records)
    numeric range -22.2672 .. 1596.13 (107 unique)
data.position.y  (number, 236/236 records)
    numeric range -3.02397 .. 155.19 (85 unique)
data.position.z  (number, 236/236 records)
    numeric range -101.843 .. 1964.74 (107 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 23 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (11)
- **eventKey:** present on 23 of 23 records
- **Intervals:** median 210.28s (p5 0.01s / p95 324231.59s, n=22)
- **`data` key-set variants:** [questEventType, questID, questName] x13; [questEventType, questID, questName, questSuccessOrFailure] x10
- **Fields under `data`:**

```text
data.questEventType  (string, 23/23 records)
    "questActiveEvent"  x13
    "questFinishEvent"  x10
data.questID  (string, 23/23 records)
    "21"  x3
    "22"  x2
    "23"  x2
    "24"  x2
    "25"  x2
    "28"  x2
    "29"  x2
    "31"  x2
    "32"  x2
    "33"  x2
    "34"  x2
data.questName  (string, 23/23 records)
    "Escape the Ruin"  x3
    "Defend the Expedition"  x2
    "Foraged Forging"  x2
    "Gear Up"  x2
    "Getting Your Space Legs"  x2
    "Getting the Band Back Together"  x2
    "Info and Intros"  x2
    "Investigate the Temple"  x2
    "TK, Reporting In!"  x2
    "What Was That?"  x2
    "Which Watershed?"  x2
data.questSuccessOrFailure  (string, 10/23 records)
    "Succeeded"  x10
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 14 records

- **Scenes:** Unit 2 Prod (Refactor) (14)
- **Intervals:** median 27.08s (p5 3.04s / p95 776.14s, n=13)
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "MapCloseEvent"  x7
    "MapOpenEvent"  x7
data.featureUsed  (string, 14/14 records)
    "Map"  x14
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 10 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (10)
- **Intervals:** median 6.56s (p5 2.09s / p95 79.56s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationNodeAdd"  x8
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 10/10 records)
    "B"  x3
    "1"  x2
    "I"  x2
    "II"  x2
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 5 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (5)
- **Intervals:** median 64.80s (p5 2.99s / p95 130.85s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "dragStart"  x3
    "dragEnd"  x2
data.featureUsed  (string, 5/5 records)
    "waypoint"  x5
data.location  (object, 5/5 records)
data.location.x  (number, 5/5 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/5 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/5 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationEvent` — 4 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 73.66s (p5 47.72s / p95 80.78s, n=3)
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

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 0.00s (p5 0.00s / p95 0.00s, n=1)
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x2
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `Soil Key Puzzle` — 2 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 280.72s (p5 280.72s / p95 280.72s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 2/2 records)
    "Finished"  x1
    "Started"  x1
data.Unit  (string, 2/2 records)
    "Unit 2 Prod (Refactor)"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 3 Dev' has no records of this event
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*