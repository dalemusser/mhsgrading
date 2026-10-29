# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75f
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f75f.jsonl
- **Records:** 2707 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f75f
- **Time span:** 2026-04-13T19:15:58.457000+00:00 .. 2026-04-23T20:10:28.136000+00:00 (240h 54m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2707 records, 7 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 49 INFO, 2 NOT_TESTED, 38 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1810 | 66.86 | 1 | 7 | 1285 | 2026-04-13T19:16:16.771000+00:00 | 2026-04-23T20:10:28.136000+00:00 | 240h 54m |
| PlayerPositionEvent | 562 | 20.76 | 1 | 7 | 0 | 2026-04-13T19:15:58.457000+00:00 | 2026-04-23T20:10:26.668000+00:00 | 240h 54m |
| Topographic Map Event | 125 | 4.62 | 1 | 2 | 0 | 2026-04-15T19:24:56.643000+00:00 | 2026-04-21T19:56:41.891000+00:00 | 144h 31m |
| questEvent | 73 | 2.7 | 1 | 7 | 73 | 2026-04-13T19:16:16.755000+00:00 | 2026-04-23T20:07:27.461000+00:00 | 240h 51m |
| TopographicMapEvent | 47 | 1.74 | 1 | 2 | 0 | 2026-04-15T19:25:11.749000+00:00 | 2026-04-21T19:56:40.030000+00:00 | 144h 31m |
| argumentationNodeEvent | 36 | 1.33 | 1 | 3 | 0 | 2026-04-13T19:39:30.642000+00:00 | 2026-04-21T19:25:42.970000+00:00 | 191h 46m |
| soilMachine | 33 | 1.22 | 1 | 1 | 0 | 2026-04-23T19:50:08.551000+00:00 | 2026-04-23T19:59:59.055000+00:00 | 9m 50s |
| argumentationEvent | 9 | 0.33 | 1 | 3 | 0 | 2026-04-13T19:39:23.664000+00:00 | 2026-04-21T19:25:47.747000+00:00 | 191h 46m |
| Soil Key Puzzle | 8 | 0.3 | 1 | 3 | 0 | 2026-04-13T20:04:31.604000+00:00 | 2026-04-23T19:39:21.817000+00:00 | 239h 34m |
| EndOfUnit | 3 | 0.11 | 1 | 3 | 0 | 2026-04-13T19:49:06.626000+00:00 | 2026-04-21T20:00:59.918000+00:00 | 192h 11m |
| crash | 1 | 0.04 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 345956.646s median 
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
  - Observed: 68.182s median 
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
  - Observed: 10.189s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.988s median 
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
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.89s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 125 records this build 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 36 records 
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
  - Observed: 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 6.6x vs baseline. 
  - Observed: 33 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 11 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f75f.jsonl[433] _id=69dd47537957a33870f2a571 ts=2026-04-13T19:43:15.2580000Z`; `69cdc937d385e3b94310f75f.jsonl[765] _id=69dfe3dd7957a33870f46b9f ts=2026-04-15T19:15:40.4910000Z`; `69cdc937d385e3b94310f75f.jsonl[1090] _id=69dfee337957a33870f494d7 ts=2026-04-15T19:59:46.8660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 125 records, TopographicMapEvent: 47 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1809 | 0.0 | 2.061 | 479.409 | 51.318 | 341196.395 | 0.13 | 444 | 4 |
| PlayerPositionEvent | 553 | 29.798 | 30.013 | 1567.894 | 43.808 | 341078.296 | 0.04 | 0 | 4 |
| Topographic Map Event | 124 | 0.221 | 13.809 | 4196.01 | 497.223 | 341965.992 | 0.01 | 0 | 6 |
| questEvent | 72 | 0.004 | 163.906 | 12042.649 | 76527.866 | 341561.678 | 0.0 | 8 | 11 |
| TopographicMapEvent | 46 | 1.082 | 10.189 | 11310.615 | 3019.705 | 342177.14 | 0.01 | 0 | 6 |
| argumentationNodeEvent | 35 | 1.085 | 6.988 | 19724.924 | 103382.289 | 345686.816 | 0.0 | 0 | 2 |
| soilMachine | 32 | 0.158 | 1.89 | 18.453 | 129.179 | 190.403 | 3.25 | 0 | 0 |
| argumentationEvent | 8 | 0.177 | 100.556 | 86298.01 | 345198.503 | 345674.553 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 7 | 3.019 | 68.182 | 123212.888 | 345462.683 | 346872.543 | 0.0 | 0 | 3 |
| EndOfUnit | 2 | 345543.411 | 345956.646 | 345956.646 | 346328.557 | 346369.881 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.013s (p5 29.96s, p95 43.81s, n=553) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `668ms: 69cdc937d385e3b94310f75f.jsonl[954] _id=69dfea417957a33870f48511 ts=2026-04-15T19:42:56.9580000Z ~ 69cdc937d385e3b94310f75f.jsonl[953] _id=69dfea427957a33870f48517 ts=2026-04-15T19:42:57.6260000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `177ms: 69cdc937d385e3b94310f75f.jsonl[2068] _id=69e7cf3b1724f0c9e2f9d521 ts=2026-04-21T19:25:47.5700000Z ~ 69cdc937d385e3b94310f75f.jsonl[2133] _id=69e7cf3c1724f0c9e2f9d529 ts=2026-04-21T19:25:47.7470000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `714ms: 69cdc937d385e3b94310f75f.jsonl[281] _id=69ea79861724f0c9e2fb62d7 ts=2026-04-23T19:56:53.8160000Z ~ 69cdc937d385e3b94310f75f.jsonl[2584] _id=69ea79871724f0c9e2fb62db ts=2026-04-23T19:56:54.5300000Z`; `579ms: 69cdc937d385e3b94310f75f.jsonl[2595] _id=69ea79b91724f0c9e2fb6375 ts=2026-04-23T19:57:44.9480000Z ~ 69cdc937d385e3b94310f75f.jsonl[2593] _id=69ea79ba1724f0c9e2fb6377 ts=2026-04-23T19:57:45.5270000Z`; `368ms: 69cdc937d385e3b94310f75f.jsonl[2593] _id=69ea79ba1724f0c9e2fb6377 ts=2026-04-23T19:57:45.5270000Z ~ 69cdc937d385e3b94310f75f.jsonl[2594] _id=69ea79ba1724f0c9e2fb6379 ts=2026-04-23T19:57:45.8950000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc937d385e3b94310f75f.jsonl[1903] _id=69e2937c1724f0c9e2f7dc3c ts=2026-04-17T20:09:32.0740000Z -> 69cdc937d385e3b94310f75f.jsonl[1915] _id=69e7c8481724f0c9e2f9af85 ts=2026-04-21T18:56:08.4690000Z; 47h 31m: 69cdc937d385e3b94310f75f.jsonl[2427] _id=69e7d8741724f0c9e2f9fdc9 ts=2026-04-21T20:05:08.0400000Z -> 69cdc937d385e3b94310f75f.jsonl[2433] _id=69ea74cf1724f0c9e2fb55cd ts=2026-04-23T19:36:47.1810000Z; 47h 4m: 69cdc937d385e3b94310f75f.jsonl[726] _id=69dd4d487957a33870f2bbb3 ts=2026-04-13T20:08:40.5410000Z -> 69cdc937d385e3b94310f75f.jsonl[752] _id=69dfe3547957a33870f469e3 ts=2026-04-15T19:13:24.1080000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 444 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f75f.jsonl[1799] _id=69e28e7a1724f0c9e2f7c796 ts=2026-04-17T19:48:10.0590000Z -> 69cdc937d385e3b94310f75f.jsonl[1802] _id=69e28e8b1724f0c9e2f7c823 ts=2026-04-17T19:48:10.059Z; 0ms: 69cdc937d385e3b94310f75f.jsonl[266] _id=69e7d77c1724f0c9e2f9fa0f ts=2026-04-21T20:00:59.9390000Z -> 69cdc937d385e3b94310f75f.jsonl[2414] _id=69e7d7971724f0c9e2f9fa79 ts=2026-04-21T20:00:59.939Z; 3ms: 69cdc937d385e3b94310f75f.jsonl[146] _id=69e2825e1724f0c9e2f792fe ts=2026-04-17T18:56:30.2580000Z -> 69cdc937d385e3b94310f75f.jsonl[147] _id=69e2825f1724f0c9e2f79300 ts=2026-04-17T18:56:30.2610000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 69cdc937d385e3b94310f75f.jsonl[1797] _id=69e28e7a1724f0c9e2f7c792 ts=2026-04-17T19:48:10.0370000Z -> 69cdc937d385e3b94310f75f.jsonl[2409] _id=69e7d77c1724f0c9e2f9fa09 ts=2026-04-21T20:00:59.9180000Z; 95h 59m: 69cdc937d385e3b94310f75f.jsonl[480] _id=69dd48b27957a33870f2ab8b ts=2026-04-13T19:49:06.6260000Z -> 69cdc937d385e3b94310f75f.jsonl[1797] _id=69e28e7a1724f0c9e2f7c792 ts=2026-04-17T19:48:10.0370000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f75f.jsonl[1905] _id=69e293801724f0c9e2f7dc54 ts=2026-04-17T20:09:36.8760000Z -> 69cdc937d385e3b94310f75f.jsonl[1909] _id=69e7c7d71724f0c9e2f9adb5 ts=2026-04-21T18:54:15.1720000Z; 47h 30m: 69cdc937d385e3b94310f75f.jsonl[2425] _id=69e7d87b1724f0c9e2f9fddb ts=2026-04-21T20:05:15.5130000Z -> 69cdc937d385e3b94310f75f.jsonl[2429] _id=69ea74a01724f0c9e2fb5595 ts=2026-04-23T19:35:59.4290000Z; 47h 2m: 69cdc937d385e3b94310f75f.jsonl[729] _id=69dd4dab7957a33870f2bcbb ts=2026-04-13T20:10:19.5480000Z -> 69cdc937d385e3b94310f75f.jsonl[750] _id=69dfe34b7957a33870f469c7 ts=2026-04-15T19:13:14.0670000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 21m 
  - Evidence: 96h 21m: 69cdc937d385e3b94310f75f.jsonl[1414] _id=69e285331724f0c9e2f79e2e ts=2026-04-17T19:08:35.8140000Z -> 69cdc937d385e3b94310f75f.jsonl[2172] _id=69e7d02c1724f0c9e2f9d989 ts=2026-04-21T19:29:48.3570000Z; 95h 2m: 69cdc937d385e3b94310f75f.jsonl[688] _id=69dd4c527957a33870f2b8b1 ts=2026-04-13T20:04:34.6230000Z -> 69cdc937d385e3b94310f75f.jsonl[1404] _id=69e284ef1724f0c9e2f79cfa ts=2026-04-17T19:07:27.6320000Z; 48h 8m: 69cdc937d385e3b94310f75f.jsonl[2178] _id=69e7d0531724f0c9e2f9da1f ts=2026-04-21T19:30:27.1530000Z -> 69cdc937d385e3b94310f75f.jsonl[2445] _id=69ea75561724f0c9e2fb5741 ts=2026-04-23T19:39:02.1200000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 59m 
  - Evidence: 94h 59m: 69cdc937d385e3b94310f75f.jsonl[1853] _id=69e291741724f0c9e2f7d28e ts=2026-04-17T20:00:52.3990000Z -> 69cdc937d385e3b94310f75f.jsonl[1949] _id=69e7c9421724f0c9e2f9b4f7 ts=2026-04-21T19:00:18.3910000Z; 46h 45m: 69cdc937d385e3b94310f75f.jsonl[129] _id=69dff0d37957a33870f49fb1 ts=2026-04-15T20:10:59.0810000Z -> 69cdc937d385e3b94310f75f.jsonl[151] _id=69e282771724f0c9e2f79382 ts=2026-04-17T18:56:55.2010000Z; 25m 50s: 69cdc937d385e3b94310f75f.jsonl[2160] _id=69e7cfac1724f0c9e2f9d6ed ts=2026-04-21T19:27:40.3430000Z -> 69cdc937d385e3b94310f75f.jsonl[2329] _id=69e7d5ba1724f0c9e2f9f259 ts=2026-04-21T19:53:30.7440000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 2m 
  - Evidence: 95h 2m: 69cdc937d385e3b94310f75f.jsonl[1841] _id=69e290c41724f0c9e2f7d090 ts=2026-04-17T19:57:36.1000000Z -> 69cdc937d385e3b94310f75f.jsonl[1948] _id=69e7c9511724f0c9e2f9b52d ts=2026-04-21T19:00:33.2400000Z; 46h 47m: 69cdc937d385e3b94310f75f.jsonl[1161] _id=69dff05f7957a33870f49f45 ts=2026-04-15T20:09:02.6860000Z -> 69cdc937d385e3b94310f75f.jsonl[1308] _id=69e2827e1724f0c9e2f793a4 ts=2026-04-17T18:57:02.0120000Z; 56m 51s: 69cdc937d385e3b94310f75f.jsonl[1201] _id=69e2835a1724f0c9e2f7970c ts=2026-04-17T19:00:42.1110000Z -> 69cdc937d385e3b94310f75f.jsonl[1840] _id=69e290ad1724f0c9e2f7d066 ts=2026-04-17T19:57:33.7030000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 69cdc937d385e3b94310f75f.jsonl[432] _id=69dd47537957a33870f2a56f ts=2026-04-13T19:43:15.2130000Z -> 69cdc937d385e3b94310f75f.jsonl[1726] _id=69e28d9d1724f0c9e2f7bfac ts=2026-04-17T19:44:29.7660000Z; 95h 38m: 69cdc937d385e3b94310f75f.jsonl[1735] _id=69e28dd51724f0c9e2f7c10e ts=2026-04-17T19:45:25.7900000Z -> 69cdc937d385e3b94310f75f.jsonl[2106] _id=69e7ced01724f0c9e2f9d32f ts=2026-04-21T19:24:00.2000000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 69cdc937d385e3b94310f75f.jsonl[434] _id=69dd474b7957a33870f2a54b ts=2026-04-13T19:43:07.6360000Z -> 69cdc937d385e3b94310f75f.jsonl[1728] _id=69e28da21724f0c9e2f7bfda ts=2026-04-17T19:44:34.4520000Z; 95h 38m: 69cdc937d385e3b94310f75f.jsonl[1733] _id=69e28dd21724f0c9e2f7c0ee ts=2026-04-17T19:45:22.5700000Z -> 69cdc937d385e3b94310f75f.jsonl[2108] _id=69e7ced91724f0c9e2f9d34b ts=2026-04-21T19:24:09.3480000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 52m 
  - Evidence: 94h 52m: 69cdc937d385e3b94310f75f.jsonl[1857] _id=69e291a11724f0c9e2f7d32c ts=2026-04-17T20:01:36.7180000Z -> 69cdc937d385e3b94310f75f.jsonl[1910] _id=69e7c7db1724f0c9e2f9adc1 ts=2026-04-21T18:54:18.3960000Z; 47h 31m: 69cdc937d385e3b94310f75f.jsonl[2426] _id=69e7d86a1724f0c9e2f9fd99 ts=2026-04-21T20:04:58.8450000Z -> 69cdc937d385e3b94310f75f.jsonl[2430] _id=69ea74a21724f0c9e2fb5599 ts=2026-04-23T19:36:01.6710000Z; 47h 4m: 69cdc937d385e3b94310f75f.jsonl[727] _id=69dd4d477957a33870f2bbac ts=2026-04-13T20:08:39.4090000Z -> 69cdc937d385e3b94310f75f.jsonl[751] _id=69dfe3547957a33870f469e1 ts=2026-04-15T19:13:21.9950000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.004s..0.011s shown 
  - Evidence: 4ms: 69cdc937d385e3b94310f75f.jsonl[14] _id=69dd46357957a33870f2a1b7 ts=2026-04-13T19:38:28.8580000Z -> 69cdc937d385e3b94310f75f.jsonl[371] _id=69dd46367957a33870f2a1bb ts=2026-04-13T19:38:28.8620000Z; 10ms: 69cdc937d385e3b94310f75f.jsonl[2487] _id=69ea767f1724f0c9e2fb5a89 ts=2026-04-23T19:43:59.2360000Z -> 69cdc937d385e3b94310f75f.jsonl[2484] _id=69ea76801724f0c9e2fb5a8b ts=2026-04-23T19:43:59.2460000Z; 11ms: 69cdc937d385e3b94310f75f.jsonl[599] _id=69dd42c07957a33870f29556 ts=2026-04-13T19:23:44.1460000Z -> 69cdc937d385e3b94310f75f.jsonl[600] _id=69dd42c07957a33870f29558 ts=2026-04-13T19:23:44.1570000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc937d385e3b94310f75f.jsonl:69cdc937d385e3b94310f75f, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f75f.jsonl[688] _id=69dd4c527957a33870f2b8b1 ts=2026-04-13T20:04:34.6230000Z`; `69cdc937d385e3b94310f75f.jsonl[1414] _id=69e285331724f0c9e2f79e2e ts=2026-04-17T19:08:35.8140000Z`; `69cdc937d385e3b94310f75f.jsonl[2178] _id=69e7d0531724f0c9e2f9da1f ts=2026-04-21T19:30:27.1530000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 47 record(s) match the trigger in 69cdc937d385e3b94310f75f.jsonl:69cdc937d385e3b94310f75f, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f75f.jsonl[859] _id=69dfe6187957a33870f474f5 ts=2026-04-15T19:25:11.7490000Z`; `69cdc937d385e3b94310f75f.jsonl[1065] _id=69dfed4c7957a33870f490f9 ts=2026-04-15T19:55:55.7930000Z`; `69cdc937d385e3b94310f75f.jsonl[1066] _id=69dfed507957a33870f4910a ts=2026-04-15T19:55:59.9570000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f75f.jsonl[1515] _id=69e2884b1724f0c9e2f7aa68 ts=2026-04-17T19:21:47.0420000Z`; `69cdc937d385e3b94310f75f.jsonl[1903] _id=69e2937c1724f0c9e2f7dc3c ts=2026-04-17T20:09:32.0740000Z`; `69cdc937d385e3b94310f75f.jsonl[1936] _id=69e7c8a21724f0c9e2f9b1ef ts=2026-04-21T18:57:37.9900000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f75f.jsonl[2133] _id=69e7cf3c1724f0c9e2f9d529 ts=2026-04-21T19:25:47.7470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc937d385e3b94310f75f.jsonl[2002] _id=69e7cbf81724f0c9e2f9c47d ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 203 unmatched 'DialogueStartEvent' (totals: 362 start, 163 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 43 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.29s, min -27.57s, max -0.00s over 2706 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75f\coverage.yaml

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
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
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
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 125 records 
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

### `DialogueEvent` — 1810 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (986); Unit 3 Dev (290); Unit 1 Dev (236); Unit 4 Dev - Dungeon (95); Unit 3 Dungeon Dev (93); Unit 4 Dev (90); Unit 4 Dev - Anderson Base (20)
- **eventKey:** present on 1285 of 1810 records
- **Intervals:** median 2.06s (p5 0.01s / p95 51.32s, n=1809)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1285; [conversationId, dialogueEventType] x525
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1810/1810 records)
    numeric range 8 .. 107 (39 unique)
data.dialogueEventType  (string, 1810/1810 records)
    "DialogueNodeEvent"  x1285
    "DialogueStartEvent"  x362
    "DialogueFinishEvent"  x163
data.nodeId  (number, 1285/1810 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 562 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (262); Unit 3 Dev (115); Unit 1 Dev (64); Unit 3 Dungeon Dev (43); Unit 4 Dev - Dungeon (39); Unit 4 Dev (32); Unit 4 Dev - Anderson Base (7)
- **Intervals:** median 30.01s (p5 29.96s / p95 43.81s, n=553)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 562/562 records)
data.position.x  (number, 562/562 records)
    numeric range -687.2 .. 1618.73 (358 unique)
data.position.y  (number, 562/562 records)
    numeric range -115.102 .. 158.243 (275 unique)
data.position.z  (number, 562/562 records)
    numeric range -1120.48 .. 1853.59 (358 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 125 records

- **Scenes:** Unit 2 Prod (Refactor) (67); Unit 3 Dev (58)
- **Intervals:** median 13.81s (p5 0.98s / p95 497.22s, n=124)
- **Fields under `data`:**

```text
data.actionType  (string, 125/125 records)
    "MapOpenEvent"  x63
    "MapCloseEvent"  x62
data.featureUsed  (string, 125/125 records)
    "Map"  x125
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 73 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (30); Unit 1 Dev (15); Unit 3 Dev (11); Unit 4 Dev - Dungeon (9); Unit 4 Dev (5); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 73 of 73 records
- **Intervals:** median 163.91s (p5 0.01s / p95 76527.87s, n=72)
- **`data` key-set variants:** [questEventType, questID, questName] x43; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Fields under `data`:**

```text
data.questEventType  (string, 73/73 records)
    "questActiveEvent"  x43
    "questFinishEvent"  x30
data.questID  (string, 73/73 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 73/73 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/73 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 47 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (36); Unit 2 Prod (Refactor) (11)
- **Intervals:** median 10.19s (p5 2.09s / p95 3019.70s, n=46)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "dragStart"  x24
    "dragEnd"  x23
data.featureUsed  (string, 47/47 records)
    "waypoint"  x47
data.location  (object, 47/47 records)
data.location.x  (number, 47/47 records)
    numeric range -770.79 .. 428.302 (24 unique)
data.location.y  (number, 47/47 records)
    numeric range -318.739 .. 219.029 (24 unique)
data.location.z  (number, 47/47 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 36 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (20); Unit 3 Dev (11); Unit 2 Prod (Refactor) (5)
- **Intervals:** median 6.99s (p5 1.27s / p95 103382.29s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "argumentationNodeAdd"  x24
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 36/36 records)
    "Unit 1 - Freshwater"  x17
    "Unit 3 - Pollution Upstream"  x11
    "Unit 2 – Watershed"  x5
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 36/36 records)
    "A"  x9
    "I"  x9
    "1"  x5
    "B"  x5
    "II"  x5
    "2"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 33 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (33)
- **Intervals:** median 1.89s (p5 0.18s / p95 129.18s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "ChangeCanister"  x33
data.canisterType  (string, 33/33 records)
    "Clay"  x23
    "Bedrock"  x5
    "Gravel"  x4
    "Sand"  x1
data.floor  (string, 33/33 records)
    "5"  x29
    "4"  x3
    "3"  x1
data.machine  (string, 33/33 records)
    "1"  x32
    "2"  x1
data.row  (string, 33/33 records)
    "BottomRow"  x26
    "TopRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 100.56s (p5 10.77s / p95 345198.50s, n=8)
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

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 68.18s (p5 8.02s / p95 345462.68s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 345956.65s (p5 345584.73s / p95 346328.56s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
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
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TopographicMapEvent` data.actionType: "dragStart" (24x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*