# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f736

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f736
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f736.jsonl
- **Records:** 1036 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f736
- **Time span:** 2026-04-15T17:48:15.528000+00:00 .. 2026-04-23T18:41:11.176000+00:00 (192h 52m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f736\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1036 records, 3 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 53 INFO, 5 NOT_TESTED, 34 PASS.
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
| DialogueEvent | 592 | 57.14 | 1 | 3 | 416 | 2026-04-15T17:48:33.514000+00:00 | 2026-04-23T18:41:11.176000+00:00 | 192h 52m |
| PlayerPositionEvent | 297 | 28.67 | 1 | 3 | 0 | 2026-04-15T17:48:15.528000+00:00 | 2026-04-23T18:40:45.203000+00:00 | 192h 52m |
| argumentationNodeEvent | 53 | 5.12 | 1 | 2 | 0 | 2026-04-15T18:18:52.292000+00:00 | 2026-04-23T18:40:28.988000+00:00 | 192h 21m |
| Topographic Map Event | 40 | 3.86 | 1 | 3 | 0 | 2026-04-15T18:21:50.571000+00:00 | 2026-04-23T18:23:01.716000+00:00 | 192h 1m |
| questEvent | 26 | 2.51 | 1 | 3 | 26 | 2026-04-15T17:48:33.486000+00:00 | 2026-04-23T18:40:39.017000+00:00 | 192h 52m |
| argumentationEvent | 12 | 1.16 | 1 | 2 | 0 | 2026-04-15T18:17:28.507000+00:00 | 2026-04-23T18:40:30.359000+00:00 | 192h 23m |
| TopographicMapEvent | 8 | 0.77 | 1 | 2 | 0 | 2026-04-21T18:37:13.927000+00:00 | 2026-04-23T18:22:54.270000+00:00 | 47h 45m |
| argumentationToolEvent | 4 | 0.39 | 1 | 1 | 0 | 2026-04-23T18:37:30.205000+00:00 | 2026-04-23T18:37:39.985000+00:00 | 9.8s |
| Soil Key Puzzle | 2 | 0.19 | 1 | 1 | 0 | 2026-04-21T18:18:30.182000+00:00 | 2026-04-21T18:18:33.162000+00:00 | 3.0s |
| EndOfUnit | 1 | 0.1 | 1 | 1 | 0 | 2026-04-21T17:02:14.998000+00:00 | 2026-04-21T17:02:14.998000+00:00 | 0.0s |
| crash | 1 | 0.1 | 1 | 1 | 0 |  |  | ? |

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
  - Observed: 30.005s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.98s median 
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
  - Observed: 4.301s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.07s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.794s median 
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
  - Observed: MainMenu; Transition; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DialogueEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 592 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 297 records 
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
  - Observed: 40 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
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
  - Observed: C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 24; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f736.jsonl[134] _id=69dfd6b67957a33870f43f23 ts=2026-04-15T18:19:34.1130000Z`; `69cdc907d385e3b94310f736.jsonl[166] _id=69dfd7887957a33870f44413 ts=2026-04-15T18:23:03.6320000Z`; `69cdc907d385e3b94310f736.jsonl[239] _id=69e7acad1724f0c9e2f91939 ts=2026-04-21T16:58:21.1960000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 8 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 591 | 0.002 | 3.055 | 1174.886 | 69.833 | 512711.762 | 0.05 | 155 | 4 |
| PlayerPositionEvent | 294 | 29.821 | 30.005 | 1774.37 | 36.042 | 512040.172 | 0.03 | 0 | 1 |
| argumentationNodeEvent | 52 | 1.509 | 8.07 | 13317.244 | 130.371 | 513082.086 | 0.0 | 0 | 2 |
| Topographic Map Event | 39 | 0.406 | 17.4 | 17724.901 | 19591.395 | 515350.704 | 0.0 | 0 | 4 |
| questEvent | 25 | 0.002 | 174.314 | 27773.021 | 137557.922 | 513327.587 | 0.0 | 4 | 7 |
| argumentationEvent | 11 | 0.087 | 38.153 | 62961.987 | 345903.893 | 513242.737 | 0.0 | 0 | 2 |
| TopographicMapEvent | 7 | 1.491 | 4.301 | 24562.906 | 119929.167 | 170971.97 | 0.0 | 0 | 2 |
| argumentationToolEvent | 3 | 0.153 | 3.794 | 3.26 | 5.629 | 5.833 | 18.4 | 0 | 0 |
| Soil Key Puzzle | 1 | 2.98 | 2.98 | 2.98 | 2.98 | 2.98 | 20.13 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.96s, p95 36.04s, n=294) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `87ms: 69cdc907d385e3b94310f736.jsonl[613] _id=69ea679f1724f0c9e2fb4d7b ts=2026-04-23T18:40:30.2720000Z ~ 69cdc907d385e3b94310f736.jsonl[614] _id=69ea679f1724f0c9e2fb4d83 ts=2026-04-23T18:40:30.3590000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 142h 25m 
  - Evidence: 142h 25m: 69cdc907d385e3b94310f736.jsonl[726] _id=69dfd96b7957a33870f45281 ts=2026-04-15T18:31:07.4850000Z -> 69cdc907d385e3b94310f736.jsonl[211] _id=69e7ac331724f0c9e2f91693 ts=2026-04-21T16:56:19.2470000Z; 47h 23m: 69cdc907d385e3b94310f736.jsonl[438] _id=69e7c4901724f0c9e2f9a73f ts=2026-04-21T18:40:16.3710000Z -> 69cdc907d385e3b94310f736.jsonl[886] _id=69ea5f021724f0c9e2fb08d5 ts=2026-04-23T18:03:46.0640000Z; 34m 45s: 69cdc907d385e3b94310f736.jsonl[268] _id=69e7ad8b1724f0c9e2f91e7d ts=2026-04-21T17:02:02.3900000Z -> 69cdc907d385e3b94310f736.jsonl[765] _id=69e7b5b01724f0c9e2f939a7 ts=2026-04-21T17:36:48.1670000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 155 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f736.jsonl[249] _id=69e7ad031724f0c9e2f91af1 ts=2026-04-21T16:59:47.1600000Z -> 69cdc907d385e3b94310f736.jsonl[250] _id=69e7ad031724f0c9e2f91af5 ts=2026-04-21T16:59:47.1620000Z; 2ms: 69cdc907d385e3b94310f736.jsonl[254] _id=69e7ad071724f0c9e2f91b0f ts=2026-04-21T16:59:50.9370000Z -> 69cdc907d385e3b94310f736.jsonl[251] _id=69e7ad071724f0c9e2f91b11 ts=2026-04-21T16:59:50.9390000Z; 2ms: 69cdc907d385e3b94310f736.jsonl[260] _id=69e7ad2c1724f0c9e2f91bfd ts=2026-04-21T17:00:27.5130000Z -> 69cdc907d385e3b94310f736.jsonl[752] _id=69e7ad2c1724f0c9e2f91bff ts=2026-04-21T17:00:27.5150000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 142h 14m 
  - Evidence: 142h 14m: 69cdc907d385e3b94310f736.jsonl[201] _id=69dfdbdf7957a33870f466f7 ts=2026-04-15T18:41:34.9990000Z -> 69cdc907d385e3b94310f736.jsonl[205] _id=69e7ac081724f0c9e2f91617 ts=2026-04-21T16:55:35.1710000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 9m 
  - Evidence: 143h 9m: 69cdc907d385e3b94310f736.jsonl[200] _id=69dfda2d7957a33870f45815 ts=2026-04-15T18:34:21.5050000Z -> 69cdc907d385e3b94310f736.jsonl[294] _id=69e7b7441724f0c9e2f9462d ts=2026-04-21T17:43:32.2090000Z; 47h 29m: 69cdc907d385e3b94310f736.jsonl[875] _id=69e7c3dc1724f0c9e2f9a29f ts=2026-04-21T18:37:16.3000000Z -> 69cdc907d385e3b94310f736.jsonl[899] _id=69ea5fbf1724f0c9e2fb0eb7 ts=2026-04-23T18:06:54.7910000Z; 46m 10s: 69cdc907d385e3b94310f736.jsonl[292] _id=69e7b7551724f0c9e2f9468b ts=2026-04-21T17:43:49.0890000Z -> 69cdc907d385e3b94310f736.jsonl[415] _id=69e7c2281724f0c9e2f99623 ts=2026-04-21T18:29:59.6950000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 29m 
  - Evidence: 47h 29m: 69cdc907d385e3b94310f736.jsonl[874] _id=69e7c3dc1724f0c9e2f9a29d ts=2026-04-21T18:37:16.2170000Z -> 69cdc907d385e3b94310f736.jsonl[897] _id=69ea5fb91724f0c9e2fb0e79 ts=2026-04-23T18:06:48.1870000Z; 13m 49s: 69cdc907d385e3b94310f736.jsonl[459] _id=69ea603e1724f0c9e2fb12ad ts=2026-04-23T18:09:00.6760000Z -> 69cdc907d385e3b94310f736.jsonl[499] _id=69ea637a1724f0c9e2fb2ef1 ts=2026-04-23T18:22:49.9690000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 142h 34m 
  - Evidence: 142h 34m: 69cdc907d385e3b94310f736.jsonl[164] _id=69dfd7877957a33870f44411 ts=2026-04-15T18:23:03.6100000Z -> 69cdc907d385e3b94310f736.jsonl[218] _id=69e7ac621724f0c9e2f9178d ts=2026-04-21T16:57:06.3470000Z; 49h 36m: 69cdc907d385e3b94310f736.jsonl[240] _id=69e7acad1724f0c9e2f91937 ts=2026-04-21T16:58:21.1690000Z -> 69cdc907d385e3b94310f736.jsonl[997] _id=69ea66321724f0c9e2fb43c5 ts=2026-04-23T18:34:26.2170000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 142h 31m 
  - Evidence: 142h 31m: 69cdc907d385e3b94310f736.jsonl[723] _id=69dfd85d7957a33870f44a24 ts=2026-04-15T18:26:37.0730000Z -> 69cdc907d385e3b94310f736.jsonl[737] _id=69e7ac971724f0c9e2f918c9 ts=2026-04-21T16:57:59.1590000Z; 49h 36m: 69cdc907d385e3b94310f736.jsonl[740] _id=69e7acab1724f0c9e2f9192d ts=2026-04-21T16:58:18.9320000Z -> 69cdc907d385e3b94310f736.jsonl[998] _id=69ea66431724f0c9e2fb446b ts=2026-04-23T18:34:43.0790000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 142h 35m 
  - Evidence: 142h 35m: 69cdc907d385e3b94310f736.jsonl[147] _id=69dfd6da7957a33870f44007 ts=2026-04-15T18:20:10.0500000Z -> 69cdc907d385e3b94310f736.jsonl[731] _id=69e7ac0b1724f0c9e2f91625 ts=2026-04-21T16:55:37.6370000Z; 47h 35m: 69cdc907d385e3b94310f736.jsonl[854] _id=69e7c21e1724f0c9e2f995e7 ts=2026-04-21T18:29:49.6100000Z -> 69cdc907d385e3b94310f736.jsonl[893] _id=69ea5f7d1724f0c9e2fb0c8e ts=2026-04-23T18:05:48.2730000Z; 39m 14s: 69cdc907d385e3b94310f736.jsonl[757] _id=69e7ad701724f0c9e2f91d95 ts=2026-04-21T17:01:35.7270000Z -> 69cdc907d385e3b94310f736.jsonl[773] _id=69e7b6a31724f0c9e2f941a3 ts=2026-04-21T17:40:50.6830000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.002s..0.012s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f736.jsonl[212] _id=69e7ac331724f0c9e2f91697 ts=2026-04-21T16:56:19.2700000Z -> 69cdc907d385e3b94310f736.jsonl[209] _id=69e7ac341724f0c9e2f91699 ts=2026-04-21T16:56:19.2720000Z; 6ms: 69cdc907d385e3b94310f736.jsonl[108] _id=69dfd6277957a33870f43b47 ts=2026-04-15T18:17:10.2670000Z -> 69cdc907d385e3b94310f736.jsonl[109] _id=69dfd6277957a33870f43b49 ts=2026-04-15T18:17:10.2730000Z; 12ms: 69cdc907d385e3b94310f736.jsonl[55] _id=69dfd2007957a33870f42195 ts=2026-04-15T17:59:27.6010000Z -> 69cdc907d385e3b94310f736.jsonl[56] _id=69dfd2007957a33870f42199 ts=2026-04-15T17:59:27.6130000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 1 record(s) match the trigger in 69cdc907d385e3b94310f736.jsonl:69cdc907d385e3b94310f736, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f736.jsonl[359] _id=69e7bf791724f0c9e2f9802f ts=2026-04-21T18:18:33.1620000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 8 record(s) match the trigger in 69cdc907d385e3b94310f736.jsonl:69cdc907d385e3b94310f736, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f736.jsonl[873] _id=69e7c3da1724f0c9e2f9a271 ts=2026-04-21T18:37:13.9270000Z`; `69cdc907d385e3b94310f736.jsonl[874] _id=69e7c3dc1724f0c9e2f9a29d ts=2026-04-21T18:37:16.2170000Z`; `69cdc907d385e3b94310f736.jsonl[897] _id=69ea5fb91724f0c9e2fb0e79 ts=2026-04-23T18:06:48.1870000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f736.jsonl[470] _id=69ea61661724f0c9e2fb1d0b ts=2026-04-23T18:13:57.7190000Z`; `69cdc907d385e3b94310f736.jsonl[948] _id=69ea62501724f0c9e2fb25c5 ts=2026-04-23T18:17:51.7830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f736.jsonl[164] _id=69dfd7877957a33870f44411 ts=2026-04-15T18:23:03.6100000Z`; `69cdc907d385e3b94310f736.jsonl[614] _id=69ea679f1724f0c9e2fb4d83 ts=2026-04-23T18:40:30.3590000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f736.jsonl[574] _id=69ea66f41724f0c9e2fb492f ts=2026-04-23T18:37:39.9850000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc907d385e3b94310f736.jsonl[271] _id=69e7ad981724f0c9e2f91edf ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 74 unmatched 'DialogueStartEvent' (totals: 124 start, 52 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 2 unmatched 'questActiveEvent' (totals: 14 start, 12 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.58s, min -1.87s, max -0.35s over 1035 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f736\coverage.yaml

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
  - Observed: 40 records 
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

### `DialogueEvent` — 592 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (235); Unit 3 Dev (211); Unit 2 Prod (Refactor) (146)
- **eventKey:** present on 416 of 592 records
- **Intervals:** median 3.06s (p5 0.01s / p95 69.83s, n=591)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x416; [conversationId, dialogueEventType] x176
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 592/592 records)
    numeric range 10 .. 101 (21 unique)
data.dialogueEventType  (string, 592/592 records)
    "DialogueNodeEvent"  x416
    "DialogueStartEvent"  x124
    "DialogueFinishEvent"  x52
data.nodeId  (number, 416/592 records)
    numeric range 0 .. 283 (129 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 297 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (118); Unit 1 Dev (105); Unit 3 Dev (74)
- **Intervals:** median 30.00s (p5 29.96s / p95 36.04s, n=294)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 297/297 records)
data.position.x  (number, 297/297 records)
    numeric range -34.3137 .. 1098.51 (154 unique)
data.position.y  (number, 297/297 records)
    numeric range -112.099 .. 162.108 (93 unique)
data.position.z  (number, 297/297 records)
    numeric range -388.818 .. 1530.77 (154 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 53 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (29); Unit 1 Dev (24)
- **Intervals:** median 8.07s (p5 1.74s / p95 130.37s, n=52)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "argumentationNodeAdd"  x31
    "argumentationNodeRemove"  x22
data.argumentationTitle  (string, 53/53 records)
    "Unit 3 - Pollution Upstream"  x29
    "Unit 1 - Freshwater"  x24
data.nodeName  (string, 53/53 records)
    "A"  x9
    "B"  x8
    "I"  x7
    "1"  x6
    "3"  x6
    "4"  x6
    "2"  x4
    "II"  x4
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (14); Unit 3 Dev (8)
- **Intervals:** median 17.40s (p5 1.28s / p95 19591.39s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 26 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (5); Unit 3 Dev (4)
- **eventKey:** present on 26 of 26 records
- **Intervals:** median 174.31s (p5 0.01s / p95 137557.92s, n=25)
- **`data` key-set variants:** [questEventType, questID, questName] x14; [questEventType, questID, questName, questSuccessOrFailure] x12
- **Fields under `data`:**

```text
data.questEventType  (string, 26/26 records)
    "questActiveEvent"  x14
    "questFinishEvent"  x12
data.questID  (string, 26/26 records)
    "32"  x4
    "33"  x4
    "34"  x3
    "16"  x2
    "17"  x2
    "21"  x2
    "23"  x2
    "28"  x2
    "29"  x2
    "31"  x2
    "22"  x1
data.questName  (string, 26/26 records)
    "Defend the Expedition"  x4
    "Info and Intros"  x4
    "What Was That?"  x3
    "Escape the Ruin"  x2
    "Foraged Forging"  x2
    "Gear Up"  x2
    "Getting Your Space Legs"  x2
    "Pollution Solution"  x2
    "Supply Run"  x2
    "TK, Reporting In!"  x2
    "Getting the Band Back Together"  x1
data.questSuccessOrFailure  (string, 12/26 records)
    "Succeeded"  x12
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (3)
- **Intervals:** median 38.15s (p5 2.80s / p95 345903.89s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "Unit 1 - Does the planet WAT-247 have freshwater"  x5
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TopographicMapEvent` — 8 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (6); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 4.30s (p5 1.73s / p95 119929.17s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "dragEnd"  x4
    "dragStart"  x4
data.featureUsed  (string, 8/8 records)
    "waypoint"  x8
data.location  (object, 8/8 records)
data.location.x  (number, 8/8 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 8/8 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 8/8 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 3.79s (p5 0.52s / p95 5.63s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x2
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 2 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.98s (p5 2.98s / p95 2.98s, n=1)
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
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit1"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (4x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (22x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*