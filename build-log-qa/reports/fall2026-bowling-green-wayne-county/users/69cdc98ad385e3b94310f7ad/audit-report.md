# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ad

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ad
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7ad.jsonl
- **Records:** 2147 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7ad
- **Time span:** 2026-04-14T19:31:28.735000+00:00 .. 2026-04-22T20:04:18.959000+00:00 (192h 32m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ad\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 2147 records, 6 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 50 INFO, 2 NOT_TESTED, 34 PASS.
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
| DialogueEvent | 1425 | 66.37 | 1 | 6 | 982 | 2026-04-14T19:31:47.203000+00:00 | 2026-04-22T20:04:16.780000+00:00 | 192h 32m |
| PlayerPositionEvent | 480 | 22.36 | 1 | 6 | 0 | 2026-04-14T19:31:28.735000+00:00 | 2026-04-22T20:04:18.959000+00:00 | 192h 32m |
| Topographic Map Event | 85 | 3.96 | 1 | 2 | 0 | 2026-04-16T19:11:19.375000+00:00 | 2026-04-22T19:32:40.223000+00:00 | 144h 21m |
| questEvent | 54 | 2.52 | 1 | 6 | 54 | 2026-04-14T19:31:47.163000+00:00 | 2026-04-22T20:04:11.699000+00:00 | 192h 32m |
| TopographicMapEvent | 53 | 2.47 | 1 | 2 | 0 | 2026-04-16T19:11:28.729000+00:00 | 2026-04-22T19:32:38.569000+00:00 | 144h 21m |
| argumentationToolEvent | 16 | 0.75 | 1 | 2 | 0 | 2026-04-20T19:02:06.500000+00:00 | 2026-04-20T20:05:30.302000+00:00 | 1h 3m |
| argumentationNodeEvent | 14 | 0.65 | 1 | 3 | 0 | 2026-04-14T19:52:29.490000+00:00 | 2026-04-20T20:05:12.994000+00:00 | 144h 12m |
| argumentationEvent | 9 | 0.42 | 1 | 3 | 0 | 2026-04-14T19:52:24.009000+00:00 | 2026-04-20T20:05:31.767000+00:00 | 144h 13m |
| Soil Key Puzzle | 8 | 0.37 | 1 | 3 | 0 | 2026-04-16T19:40:57.591000+00:00 | 2026-04-22T19:43:30.038000+00:00 | 144h 2m |
| EndOfUnit | 3 | 0.14 | 1 | 3 | 0 | 2026-04-14T19:58:46.591000+00:00 | 2026-04-22T19:36:46.150000+00:00 | 191h 37m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 344939.78s median 
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
  - Observed: 108.217s median 
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
  - Observed: 5.153s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 15.254s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.673s median 
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
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 85 records this build 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 14 records 
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
  - Observed: 2; 3; 4; C 
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
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[17] _id=69de9b617957a33870f3a8a7 ts=2026-04-14T19:54:09.5320000Z`; `69cdc98ad385e3b94310f7ad.jsonl[894] _id=69e1386b1724f0c9e2f6d842 ts=2026-04-16T19:28:42.4650000Z`; `69cdc98ad385e3b94310f7ad.jsonl[1362] _id=69e678451724f0c9e2f8c373 ts=2026-04-20T19:02:29.2580000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 85 records, TopographicMapEvent: 53 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1424 | 0.002 | 2.497 | 486.762 | 51.867 | 340914.99 | 0.12 | 378 | 3 |
| PlayerPositionEvent | 471 | 29.697 | 30.01 | 1114.054 | 45.162 | 340892.903 | 0.05 | 0 | 2 |
| Topographic Map Event | 84 | 0.883 | 26.307 | 6186.677 | 615.565 | 342364.511 | 0.01 | 0 | 6 |
| questEvent | 53 | 0.003 | 188.143 | 13078.199 | 69132.961 | 341373.755 | 0.0 | 7 | 8 |
| TopographicMapEvent | 52 | 0.424 | 5.153 | 9993.651 | 1189.782 | 342283.147 | 0.01 | 0 | 7 |
| argumentationToolEvent | 15 | 0.007 | 0.673 | 253.587 | 1140.794 | 3793.553 | 0.24 | 1 | 1 |
| argumentationNodeEvent | 13 | 4.482 | 15.254 | 39935.654 | 208328.308 | 515234.11 | 0.0 | 0 | 2 |
| argumentationEvent | 8 | 0.094 | 57.01 | 64898.47 | 336179.887 | 515204.262 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 7 | 30.154 | 108.217 | 74078.921 | 293580.534 | 347225.626 | 0.0 | 0 | 3 |
| EndOfUnit | 2 | 174648.14 | 344939.78 | 344939.78 | 498202.255 | 515231.419 | 0.0 | 0 | 2 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.010s (p5 29.95s, p95 45.16s, n=471) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `94ms: 69cdc98ad385e3b94310f7ad.jsonl[1756] _id=69e6870b1724f0c9e2f8fe79 ts=2026-04-20T20:05:31.6730000Z ~ 69cdc98ad385e3b94310f7ad.jsonl[228] _id=69e6870c1724f0c9e2f8fe83 ts=2026-04-20T20:05:31.7670000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 69cdc98ad385e3b94310f7ad.jsonl[1749] _id=69e687071724f0c9e2f8fe49 ts=2026-04-20T20:05:27.2310000Z ~ 69cdc98ad385e3b94310f7ad.jsonl[1752] _id=69e687071724f0c9e2f8fe51 ts=2026-04-20T20:05:27.2380000Z`; `111ms: 69cdc98ad385e3b94310f7ad.jsonl[1754] _id=69e687081724f0c9e2f8fe57 ts=2026-04-20T20:05:27.9850000Z ~ 69cdc98ad385e3b94310f7ad.jsonl[1753] _id=69e687081724f0c9e2f8fe5b ts=2026-04-20T20:05:28.0960000Z`; `824ms: 69cdc98ad385e3b94310f7ad.jsonl[1753] _id=69e687081724f0c9e2f8fe5b ts=2026-04-20T20:05:28.0960000Z ~ 69cdc98ad385e3b94310f7ad.jsonl[219] _id=69e687081724f0c9e2f8fe61 ts=2026-04-20T20:05:28.9200000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 41m 
  - Evidence: 94h 41m: 69cdc98ad385e3b94310f7ad.jsonl[144] _id=69e141bb1724f0c9e2f712e6 ts=2026-04-16T20:08:26.8240000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1230] _id=69e6756d1724f0c9e2f8b7df ts=2026-04-20T18:50:21.8140000Z; 46h 45m: 69cdc98ad385e3b94310f7ad.jsonl[1820] _id=69e6886d1724f0c9e2f90453 ts=2026-04-20T20:11:25.2450000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1848] _id=69e91a041724f0c9e2fa8953 ts=2026-04-22T18:57:08.0180000Z; 46h 45m: 69cdc98ad385e3b94310f7ad.jsonl[591] _id=69de9e337957a33870f3b49d ts=2026-04-14T20:06:11.0610000Z -> 69cdc98ad385e3b94310f7ad.jsonl[39] _id=69e12fc81724f0c9e2f68ff2 ts=2026-04-16T18:51:52.1110000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 378 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc98ad385e3b94310f7ad.jsonl[750] _id=69e134131724f0c9e2f6a49a ts=2026-04-16T19:10:10.7770000Z -> 69cdc98ad385e3b94310f7ad.jsonl[57] _id=69e134131724f0c9e2f6a49c ts=2026-04-16T19:10:10.7790000Z; 3ms: 69cdc98ad385e3b94310f7ad.jsonl[1080] _id=69e13f291724f0c9e2f7075b ts=2026-04-16T19:57:28.8990000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1055] _id=69e13f291724f0c9e2f70762 ts=2026-04-16T19:57:28.9020000Z; 3ms: 69cdc98ad385e3b94310f7ad.jsonl[1502] _id=69e920aa1724f0c9e2faa1a1 ts=2026-04-22T19:25:29.8070000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1497] _id=69e920aa1724f0c9e2faa1a3 ts=2026-04-22T19:25:29.8100000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 7m 
  - Evidence: 143h 7m: 69cdc98ad385e3b94310f7ad.jsonl[533] _id=69de9c767957a33870f3ae0d ts=2026-04-14T19:58:46.5910000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1407] _id=69e679161724f0c9e2f8c77f ts=2026-04-20T19:05:58.0100000Z; 48h 30m: 69cdc98ad385e3b94310f7ad.jsonl[1407] _id=69e679161724f0c9e2f8c77f ts=2026-04-20T19:05:58.0100000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1984] _id=69e9234e1724f0c9e2faac67 ts=2026-04-22T19:36:46.1500000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 41m 
  - Evidence: 94h 41m: 69cdc98ad385e3b94310f7ad.jsonl[1202] _id=69e141b91724f0c9e2f712d8 ts=2026-04-16T20:08:24.8720000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1227] _id=69e675561724f0c9e2f8b787 ts=2026-04-20T18:49:57.7750000Z; 46h 42m: 69cdc98ad385e3b94310f7ad.jsonl[597] _id=69de9edd7957a33870f3b717 ts=2026-04-14T20:09:01.0390000Z -> 69cdc98ad385e3b94310f7ad.jsonl[630] _id=69e12fc61724f0c9e2f68fe8 ts=2026-04-16T18:51:48.2850000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 27m 
  - Evidence: 96h 27m: 69cdc98ad385e3b94310f7ad.jsonl[990] _id=69e13bb61724f0c9e2f6f8b6 ts=2026-04-16T19:42:45.8080000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1810] _id=69e6880f1724f0c9e2f902fd ts=2026-04-20T20:09:51.4340000Z; 46h 46m: 69cdc98ad385e3b94310f7ad.jsonl[1814] _id=69e688501724f0c9e2f903e1 ts=2026-04-20T20:10:56.6360000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1857] _id=69e91a291724f0c9e2fa8a2f ts=2026-04-22T18:57:45.2870000Z; 44m 42s: 69cdc98ad385e3b94310f7ad.jsonl[1861] _id=69e91a471724f0c9e2fa8ac5 ts=2026-04-22T18:58:15.4410000Z -> 69cdc98ad385e3b94310f7ad.jsonl[2011] _id=69e924c21724f0c9e2fab22b ts=2026-04-22T19:42:58.1450000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 6m 
  - Evidence: 95h 6m: 69cdc98ad385e3b94310f7ad.jsonl[1185] _id=69e141471724f0c9e2f710c8 ts=2026-04-16T20:06:31.4290000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1462] _id=69e67aa41724f0c9e2f8ce93 ts=2026-04-20T19:12:35.9400000Z; 47h 32m: 69cdc98ad385e3b94310f7ad.jsonl[1706] _id=69e684b51724f0c9e2f8f919 ts=2026-04-20T19:55:33.1440000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1824] _id=69e921421724f0c9e2faa415 ts=2026-04-22T19:28:02.3300000Z; 14m 31s: 69cdc98ad385e3b94310f7ad.jsonl[1526] _id=69e67c6e1724f0c9e2f8d66d ts=2026-04-20T19:20:14.3490000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1622] _id=69e67fd61724f0c9e2f8e745 ts=2026-04-20T19:34:46.0670000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 4m 
  - Evidence: 95h 4m: 69cdc98ad385e3b94310f7ad.jsonl[141] _id=69e141411724f0c9e2f71090 ts=2026-04-16T20:06:25.2530000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1447] _id=69e67a4c1724f0c9e2f8cd4b ts=2026-04-20T19:11:08.4000000Z; 47h 32m: 69cdc98ad385e3b94310f7ad.jsonl[1705] _id=69e684b31724f0c9e2f8f915 ts=2026-04-20T19:55:31.5380000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1823] _id=69e921441724f0c9e2faa41d ts=2026-04-22T19:28:04.7490000Z; 22m 10s: 69cdc98ad385e3b94310f7ad.jsonl[1460] _id=69e67aaa1724f0c9e2f8cea7 ts=2026-04-20T19:12:42.4860000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1620] _id=69e67fdc1724f0c9e2f8e761 ts=2026-04-20T19:34:52.6840000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 6m 
  - Evidence: 143h 6m: 69cdc98ad385e3b94310f7ad.jsonl[16] _id=69de9b617957a33870f3a8a5 ts=2026-04-14T19:54:09.5050000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1343] _id=69e677e51724f0c9e2f8c1fd ts=2026-04-20T19:00:53.7670000Z; 1h 1m: 69cdc98ad385e3b94310f7ad.jsonl[162] _id=69e678451724f0c9e2f8c371 ts=2026-04-20T19:02:29.2310000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1735] _id=69e686bf1724f0c9e2f8fd0f ts=2026-04-20T20:04:15.2780000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 7m 
  - Evidence: 143h 7m: 69cdc98ad385e3b94310f7ad.jsonl[483] _id=69de9b5a7957a33870f3a875 ts=2026-04-14T19:54:02.3820000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1347] _id=69e677fc1724f0c9e2f8c25b ts=2026-04-20T19:01:16.4920000Z; 1h 2m: 69cdc98ad385e3b94310f7ad.jsonl[1361] _id=69e678431724f0c9e2f8c36d ts=2026-04-20T19:02:27.4070000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1737] _id=69e686cf1724f0c9e2f8fd4f ts=2026-04-20T20:04:31.8470000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 3m 
  - Evidence: 1h 3m: 69cdc98ad385e3b94310f7ad.jsonl[1357] _id=69e678301724f0c9e2f8c333 ts=2026-04-20T19:02:08.6440000Z -> 69cdc98ad385e3b94310f7ad.jsonl[216] _id=69e687021724f0c9e2f8fe35 ts=2026-04-20T20:05:22.1970000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.007s..0.007s shown 
  - Evidence: 7ms: 69cdc98ad385e3b94310f7ad.jsonl[1749] _id=69e687071724f0c9e2f8fe49 ts=2026-04-20T20:05:27.2310000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1752] _id=69e687071724f0c9e2f8fe51 ts=2026-04-20T20:05:27.2380000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 49m 
  - Evidence: 94h 49m: 69cdc98ad385e3b94310f7ad.jsonl[1110] _id=69e13fdb1724f0c9e2f70a6e ts=2026-04-16T20:00:27.1920000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1229] _id=69e675591724f0c9e2f8b78d ts=2026-04-20T18:50:00.9470000Z; 46h 50m: 69cdc98ad385e3b94310f7ad.jsonl[548] _id=69de9d1a7957a33870f3b079 ts=2026-04-14T20:01:30.0040000Z -> 69cdc98ad385e3b94310f7ad.jsonl[631] _id=69e12fc71724f0c9e2f68fee ts=2026-04-16T18:51:50.4960000Z; 46h 48m: 69cdc98ad385e3b94310f7ad.jsonl[1774] _id=69e687541724f0c9e2f8ffb7 ts=2026-04-20T20:06:44.4720000Z -> 69cdc98ad385e3b94310f7ad.jsonl[1845] _id=69e919af1724f0c9e2fa87fb ts=2026-04-22T18:55:42.3960000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.003s..0.008s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7ad.jsonl[456] _id=69de9ab87957a33870f3a59d ts=2026-04-14T19:51:20.0070000Z -> 69cdc98ad385e3b94310f7ad.jsonl[14] _id=69de9ab87957a33870f3a5a1 ts=2026-04-14T19:51:20.0100000Z; 8ms: 69cdc98ad385e3b94310f7ad.jsonl[2064] _id=69e926551724f0c9e2fab741 ts=2026-04-22T19:49:41.3440000Z -> 69cdc98ad385e3b94310f7ad.jsonl[294] _id=69e926551724f0c9e2fab743 ts=2026-04-22T19:49:41.3520000Z; 8ms: 69cdc98ad385e3b94310f7ad.jsonl[2089] _id=69e927091724f0c9e2fab9af ts=2026-04-22T19:52:41.5970000Z -> 69cdc98ad385e3b94310f7ad.jsonl[2087] _id=69e927091724f0c9e2fab9b1 ts=2026-04-22T19:52:41.6050000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc98ad385e3b94310f7ad.jsonl:69cdc98ad385e3b94310f7ad, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[990] _id=69e13bb61724f0c9e2f6f8b6 ts=2026-04-16T19:42:45.8080000Z`; `69cdc98ad385e3b94310f7ad.jsonl[1814] _id=69e688501724f0c9e2f903e1 ts=2026-04-20T20:10:56.6360000Z`; `69cdc98ad385e3b94310f7ad.jsonl[1861] _id=69e91a471724f0c9e2fa8ac5 ts=2026-04-22T18:58:15.4410000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 53 record(s) match the trigger in 69cdc98ad385e3b94310f7ad.jsonl:69cdc98ad385e3b94310f7ad, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[757] _id=69e134611724f0c9e2f6a67a ts=2026-04-16T19:11:28.7290000Z`; `69cdc98ad385e3b94310f7ad.jsonl[867] _id=69e137c21724f0c9e2f6c521 ts=2026-04-16T19:25:53.9750000Z`; `69cdc98ad385e3b94310f7ad.jsonl[868] _id=69e137c71724f0c9e2f6c656 ts=2026-04-16T19:25:59.3200000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[1113] _id=69e140451724f0c9e2f70c20 ts=2026-04-16T20:02:12.7580000Z`; `69cdc98ad385e3b94310f7ad.jsonl[183] _id=69e67b461724f0c9e2f8d13f ts=2026-04-20T19:15:18.6630000Z`; `69cdc98ad385e3b94310f7ad.jsonl[1510] _id=69e67be01724f0c9e2f8d3ff ts=2026-04-20T19:17:51.8500000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[228] _id=69e6870c1724f0c9e2f8fe83 ts=2026-04-20T20:05:31.7670000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[217] _id=69e687061724f0c9e2f8fe43 ts=2026-04-20T20:05:26.0940000Z`; `69cdc98ad385e3b94310f7ad.jsonl[1752] _id=69e687071724f0c9e2f8fe51 ts=2026-04-20T20:05:27.2380000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[1862] _id=69e91a5b1724f0c9e2fa8b0d ts=2026-04-22T18:58:34.9840000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7ad.jsonl[1753] _id=69e687081724f0c9e2f8fe5b ts=2026-04-20T20:05:28.0960000Z`; `69cdc98ad385e3b94310f7ad.jsonl[219] _id=69e687081724f0c9e2f8fe61 ts=2026-04-20T20:05:28.9200000Z`; `69cdc98ad385e3b94310f7ad.jsonl[221] _id=69e687091724f0c9e2f8fe65 ts=2026-04-20T20:05:29.6790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 180 unmatched 'DialogueStartEvent' (totals: 310 start, 133 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 8 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 30 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.18s, min -3.31s, max +0.05s over 2147 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ad\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 85 records 
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

### `DialogueEvent` — 1425 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (679); Unit 3 Dev (380); Unit 1 Dev (176); Unit 4 Dev - Dungeon (86); Unit 3 Dungeon Dev (79); Unit 4 Dev (25)
- **eventKey:** present on 982 of 1425 records
- **Intervals:** median 2.50s (p5 0.01s / p95 51.87s, n=1424)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x982; [conversationId, dialogueEventType] x443
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1425/1425 records)
    numeric range 8 .. 104 (37 unique)
data.dialogueEventType  (string, 1425/1425 records)
    "DialogueNodeEvent"  x982
    "DialogueStartEvent"  x310
    "DialogueFinishEvent"  x133
data.nodeId  (number, 982/1425 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 480 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (188); Unit 3 Dev (126); Unit 3 Dungeon Dev (56); Unit 1 Dev (55); Unit 4 Dev - Dungeon (38); Unit 4 Dev (17)
- **Intervals:** median 30.01s (p5 29.95s / p95 45.16s, n=471)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 480/480 records)
data.position.x  (number, 480/480 records)
    numeric range -705.33 .. 1441.38 (260 unique)
data.position.y  (number, 480/480 records)
    numeric range -115.127 .. 164.256 (205 unique)
data.position.z  (number, 480/480 records)
    numeric range -1106.16 .. 1890.9 (259 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 85 records

- **Scenes:** Unit 3 Dev (50); Unit 2 Prod (Refactor) (35)
- **Intervals:** median 26.31s (p5 2.52s / p95 615.56s, n=84)
- **Fields under `data`:**

```text
data.actionType  (string, 85/85 records)
    "MapOpenEvent"  x43
    "MapCloseEvent"  x42
data.featureUsed  (string, 85/85 records)
    "Map"  x85
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 54 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (2); Unit 4 Dev (1)
- **eventKey:** present on 54 of 54 records
- **Intervals:** median 188.14s (p5 0.01s / p95 69132.96s, n=53)
- **`data` key-set variants:** [questEventType, questID, questName] x30; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 54/54 records)
    "questActiveEvent"  x30
    "questFinishEvent"  x24
data.questID  (string, 54/54 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 54/54 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/54 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 53 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (32); Unit 2 Prod (Refactor) (21)
- **Intervals:** median 5.15s (p5 0.65s / p95 1189.78s, n=52)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "dragStart"  x27
    "dragEnd"  x26
data.featureUsed  (string, 53/53 records)
    "waypoint"  x53
data.location  (object, 53/53 records)
data.location.x  (number, 53/53 records)
    numeric range -776.465 .. 279.423 (27 unique)
data.location.y  (number, 53/53 records)
    numeric range -334.112 .. 342.129 (27 unique)
data.location.z  (number, 53/53 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (12); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 0.67s (p5 0.06s / p95 1140.79s, n=15)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolClose"  x8
    "argumentationToolOpen"  x8
data.argumentationTitle  (string, 16/16 records)
    "Unit 3 - Pollution Upstream"  x12
    "Unit 2 – Watershed"  x4
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - Pollution Site Data"  x10
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationNodeEvent` — 14 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (6); Unit 2 Prod (Refactor) (5); Unit 3 Dev (3)
- **Intervals:** median 15.25s (p5 4.59s / p95 208328.31s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationNodeAdd"  x13
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 2 – Watershed"  x5
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
data.nodeName  (string, 14/14 records)
    "1"  x3
    "A"  x3
    "I"  x3
    "D"  x2
    "5"  x1
    "B"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 57.01s (p5 11.88s / p95 336179.89s, n=8)
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

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (2); Unit 4 Dev (2)
- **Intervals:** median 108.22s (p5 30.68s / p95 293580.53s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 3 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 344939.78s (p5 191677.30s / p95 498202.26s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (27x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*