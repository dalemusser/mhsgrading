# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f731

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f731
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f731.jsonl
- **Records:** 1938 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f731
- **Time span:** 2026-04-13T17:53:42.952000+00:00 .. 2026-04-23T18:39:48.690000+00:00 (240h 46m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f731\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **12 event types**, 1938 records, 6 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 61 INFO, 2 NOT_TESTED, 41 PASS.
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
| DialogueEvent | 1230 | 63.47 | 1 | 6 | 869 | 2026-04-13T17:54:01.018000+00:00 | 2026-04-23T18:37:35.107000+00:00 | 240h 43m |
| PlayerPositionEvent | 462 | 23.84 | 1 | 6 | 0 | 2026-04-13T17:53:42.952000+00:00 | 2026-04-23T18:39:48.690000+00:00 | 240h 46m |
| Topographic Map Event | 92 | 4.75 | 1 | 2 | 0 | 2026-04-15T18:05:12.773000+00:00 | 2026-04-21T18:34:00.227000+00:00 | 144h 28m |
| questEvent | 57 | 2.94 | 1 | 6 | 57 | 2026-04-13T17:54:01+00:00 | 2026-04-23T18:37:33.803000+00:00 | 240h 43m |
| TopographicMapEvent | 30 | 1.55 | 1 | 2 | 0 | 2026-04-15T18:36:22.538000+00:00 | 2026-04-21T17:41:04.372000+00:00 | 143h 4m |
| soilMachine | 26 | 1.34 | 1 | 1 | 0 | 2026-04-23T18:22:24.584000+00:00 | 2026-04-23T18:31:52.049000+00:00 | 9m 27s |
| argumentationNodeEvent | 14 | 0.72 | 1 | 2 | 0 | 2026-04-15T17:59:06.362000+00:00 | 2026-04-21T18:06:07.174000+00:00 | 144h 7m |
| argumentationToolEvent | 10 | 0.52 | 1 | 1 | 0 | 2026-04-21T18:05:46.776000+00:00 | 2026-04-21T18:05:54.821000+00:00 | 8.0s |
| Soil Key Puzzle | 7 | 0.36 | 1 | 3 | 0 | 2026-04-15T18:13:18.934000+00:00 | 2026-04-23T18:07:23.242000+00:00 | 191h 54m |
| argumentationEvent | 7 | 0.36 | 1 | 2 | 0 | 2026-04-15T17:58:21.501000+00:00 | 2026-04-21T18:06:12.344000+00:00 | 144h 7m |
| EndOfUnit | 2 | 0.1 | 1 | 2 | 0 | 2026-04-15T18:01:58.878000+00:00 | 2026-04-21T18:39:33.676000+00:00 | 144h 37m |
| crash | 1 | 0.05 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 520654.798s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
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
  - Observed: 2132.044s median 
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
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 27.771s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.097s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.77s median 
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
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.831s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 7 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 92 records this build 
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
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; C; D; II 
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
  - Observed: 24; 25; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 32 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f731.jsonl[675] _id=69dfd1f87957a33870f4212d ts=2026-04-15T17:59:20.0430000Z`; `69cdc907d385e3b94310f731.jsonl[874] _id=69dfd7a07957a33870f44491 ts=2026-04-15T18:23:27.6800000Z`; `69cdc907d385e3b94310f731.jsonl[999] _id=69dfdb2b7957a33870f46235 ts=2026-04-15T18:38:34.2930000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 92 records, TopographicMapEvent: 30 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1229 | 0.0 | 2.091 | 705.138 | 48.413 | 334054.996 | 0.09 | 319 | 6 |
| PlayerPositionEvent | 454 | 29.897 | 30.002 | 1533.11 | 45.08 | 334037.572 | 0.04 | 0 | 4 |
| Topographic Map Event | 91 | 0.0 | 8.634 | 5715.686 | 802.547 | 334243.551 | 0.01 | 1 | 7 |
| questEvent | 56 | 0.001 | 140.055 | 15475.229 | 170114.483 | 335102.37 | 0.0 | 9 | 9 |
| TopographicMapEvent | 29 | 0.377 | 3.516 | 17761.443 | 106556.532 | 336662.117 | 0.0 | 0 | 2 |
| soilMachine | 25 | 0.164 | 5.831 | 22.699 | 61.072 | 205.553 | 2.64 | 0 | 0 |
| argumentationNodeEvent | 13 | 1.172 | 8.097 | 39909.293 | 207501.695 | 518702.259 | 0.0 | 0 | 1 |
| argumentationToolEvent | 9 | 0.006 | 0.77 | 0.894 | 2.554 | 3.183 | 67.12 | 1 | 0 |
| Soil Key Puzzle | 6 | 3.002 | 2132.044 | 115140.718 | 428642.986 | 514005.852 | 0.0 | 0 | 3 |
| argumentationEvent | 6 | 0.072 | 27.771 | 86478.474 | 389050.235 | 518694.348 | 0.0 | 0 | 1 |
| EndOfUnit | 1 | 520654.798 | 520654.798 | 520654.798 | 520654.798 | 520654.798 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.002s (p5 29.98s, p95 45.08s, n=454) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc907d385e3b94310f731.jsonl[235] _id=69e2930f1724f0c9e2f7d9f0 ts=2026-04-17T20:07:05.0860000Z ~ 69cdc907d385e3b94310f731.jsonl[246] _id=69e7abe81724f0c9e2f91559 ts=2026-04-17T20:07:05.086Z`; `502ms: 69cdc907d385e3b94310f731.jsonl[1655] _id=69e7c3041724f0c9e2f99ba7 ts=2026-04-21T18:33:40.0930000Z ~ 69cdc907d385e3b94310f731.jsonl[1653] _id=69e7c3041724f0c9e2f99bb1 ts=2026-04-21T18:33:40.5950000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `72ms: 69cdc907d385e3b94310f731.jsonl[1467] _id=69e7bc941724f0c9e2f96af9 ts=2026-04-21T18:06:12.2720000Z ~ 69cdc907d385e3b94310f731.jsonl[301] _id=69e7bc941724f0c9e2f96b03 ts=2026-04-21T18:06:12.3440000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `422ms: 69cdc907d385e3b94310f731.jsonl[292] _id=69e7bc801724f0c9e2f96a83 ts=2026-04-21T18:05:52.3900000Z ~ 69cdc907d385e3b94310f731.jsonl[293] _id=69e7bc801724f0c9e2f96a8b ts=2026-04-21T18:05:52.8120000Z`; `573ms: 69cdc907d385e3b94310f731.jsonl[1461] _id=69e7bc801724f0c9e2f96a89 ts=2026-04-21T18:05:52.4650000Z ~ 69cdc907d385e3b94310f731.jsonl[1462] _id=69e7bc811724f0c9e2f96a8f ts=2026-04-21T18:05:53.0380000Z`; `776ms: 69cdc907d385e3b94310f731.jsonl[294] _id=69e7bc821724f0c9e2f96a93 ts=2026-04-21T18:05:54.0450000Z ~ 69cdc907d385e3b94310f731.jsonl[296] _id=69e7bc821724f0c9e2f96a9d ts=2026-04-21T18:05:54.8210000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `732ms: 69cdc907d385e3b94310f731.jsonl[400] _id=69ea64dc1724f0c9e2fb38c6 ts=2026-04-23T18:28:43.4290000Z ~ 69cdc907d385e3b94310f731.jsonl[401] _id=69ea64dc1724f0c9e2fb38cf ts=2026-04-23T18:28:44.1610000Z`; `164ms: 69cdc907d385e3b94310f731.jsonl[401] _id=69ea64dc1724f0c9e2fb38cf ts=2026-04-23T18:28:44.1610000Z ~ 69cdc907d385e3b94310f731.jsonl[1878] _id=69ea64dd1724f0c9e2fb38d1 ts=2026-04-23T18:28:44.3250000Z`; `168ms: 69cdc907d385e3b94310f731.jsonl[1878] _id=69ea64dd1724f0c9e2fb38d1 ts=2026-04-23T18:28:44.3250000Z ~ 69cdc907d385e3b94310f731.jsonl[402] _id=69ea64dd1724f0c9e2fb38d5 ts=2026-04-23T18:28:44.4930000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 92h 47m 
  - Evidence: 92h 47m: 69cdc907d385e3b94310f731.jsonl[256] _id=69e7abe91724f0c9e2f91581 ts=2026-04-17T20:08:51.075Z -> 69cdc907d385e3b94310f731.jsonl[1185] _id=69e7ac3b1724f0c9e2f916bd ts=2026-04-21T16:56:26.0710000Z; 49h 1m: 69cdc907d385e3b94310f731.jsonl[1016] _id=69dfdbb87957a33870f46693 ts=2026-04-15T18:40:55.6430000Z -> 69cdc907d385e3b94310f731.jsonl[1021] _id=69e28d2d1724f0c9e2f7bc84 ts=2026-04-17T19:42:37.3690000Z; 47h 22m: 69cdc907d385e3b94310f731.jsonl[1718] _id=69e7c47e1724f0c9e2f9a705 ts=2026-04-21T18:39:33.681Z -> 69cdc907d385e3b94310f731.jsonl[1722] _id=69ea5eb21724f0c9e2fb06e7 ts=2026-04-23T18:02:25.6150000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 319 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f731.jsonl[105] _id=69dfd7ed7957a33870f446ef ts=2026-04-15T18:24:44.7710000Z -> 69cdc907d385e3b94310f731.jsonl[880] _id=69dfd8227957a33870f44855 ts=2026-04-15T18:24:44.771Z; 0ms: 69cdc907d385e3b94310f731.jsonl[106] _id=69dfd7ed7957a33870f446f1 ts=2026-04-15T18:24:44.7770000Z -> 69cdc907d385e3b94310f731.jsonl[881] _id=69dfd8227957a33870f44857 ts=2026-04-15T18:24:44.777Z; 0ms: 69cdc907d385e3b94310f731.jsonl[1713] _id=69e7c4651724f0c9e2f9a69d ts=2026-04-21T18:39:33.6810000Z -> 69cdc907d385e3b94310f731.jsonl[1718] _id=69e7c47e1724f0c9e2f9a705 ts=2026-04-21T18:39:33.681Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 37m 
  - Evidence: 144h 37m: 69cdc907d385e3b94310f731.jsonl[715] _id=69dfd2977957a33870f4265d ts=2026-04-15T18:01:58.8780000Z -> 69cdc907d385e3b94310f731.jsonl[368] _id=69e7c4651724f0c9e2f9a699 ts=2026-04-21T18:39:33.6760000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 92h 47m 
  - Evidence: 92h 47m: 69cdc907d385e3b94310f731.jsonl[254] _id=69e7abea1724f0c9e2f91585 ts=2026-04-17T20:09:05.896Z -> 69cdc907d385e3b94310f731.jsonl[1186] _id=69e7ac371724f0c9e2f916b1 ts=2026-04-21T16:56:23.4680000Z; 49h 2m: 69cdc907d385e3b94310f731.jsonl[1012] _id=69dfdb8f7957a33870f4655d ts=2026-04-15T18:40:15.3930000Z -> 69cdc907d385e3b94310f731.jsonl[1019] _id=69e28d2a1724f0c9e2f7bc6e ts=2026-04-17T19:42:33.4890000Z; 47h 6m: 69cdc907d385e3b94310f731.jsonl[565] _id=69dd38bf7957a33870f291a2 ts=2026-04-13T18:41:03.1570000Z -> 69cdc907d385e3b94310f731.jsonl[30] _id=69dfcf287957a33870f40cdf ts=2026-04-15T17:47:18.9940000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 142h 46m 
  - Evidence: 142h 46m: 69cdc907d385e3b94310f731.jsonl[787] _id=69dfd5427957a33870f436a7 ts=2026-04-15T18:13:21.9360000Z -> 69cdc907d385e3b94310f731.jsonl[261] _id=69e7ad181724f0c9e2f91b69 ts=2026-04-21T17:00:07.7880000Z; 47h 55m: 69cdc907d385e3b94310f731.jsonl[1510] _id=69e7bdbf1724f0c9e2f9731b ts=2026-04-21T18:11:11.8770000Z -> 69cdc907d385e3b94310f731.jsonl[1745] _id=69ea5fca1724f0c9e2fb0f55 ts=2026-04-23T18:07:06.2640000Z; 1h 10m: 69cdc907d385e3b94310f731.jsonl[261] _id=69e7ad181724f0c9e2f91b69 ts=2026-04-21T17:00:07.7880000Z -> 69cdc907d385e3b94310f731.jsonl[311] _id=69e7bd9f1724f0c9e2f97251 ts=2026-04-21T18:10:39.6670000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 92h 50m 
  - Evidence: 92h 50m: 69cdc907d385e3b94310f731.jsonl[253] _id=69e7abe91724f0c9e2f91583 ts=2026-04-17T20:08:54.051Z -> 69cdc907d385e3b94310f731.jsonl[1200] _id=69e7acf91724f0c9e2f91a9d ts=2026-04-21T16:59:37.6020000Z; 49h 10m: 69cdc907d385e3b94310f731.jsonl[1015] _id=69dfdba67957a33870f46607 ts=2026-04-15T18:40:38.1110000Z -> 69cdc907d385e3b94310f731.jsonl[185] _id=69e28f3e1724f0c9e2f7cbe8 ts=2026-04-17T19:51:25.9380000Z; 40m 29s: 69cdc907d385e3b94310f731.jsonl[1194] _id=69e7ad001724f0c9e2f91ae7 ts=2026-04-21T16:59:44.4080000Z -> 69cdc907d385e3b94310f731.jsonl[1278] _id=69e7b67e1724f0c9e2f940d5 ts=2026-04-21T17:40:14.2870000Z
- **INFO / Info** `Topographic Map Event` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f731.jsonl[235] _id=69e2930f1724f0c9e2f7d9f0 ts=2026-04-17T20:07:05.0860000Z -> 69cdc907d385e3b94310f731.jsonl[246] _id=69e7abe81724f0c9e2f91559 ts=2026-04-17T20:07:05.086Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 69cdc907d385e3b94310f731.jsonl[255] _id=69e7abe91724f0c9e2f9157d ts=2026-04-17T20:08:48.774Z -> 69cdc907d385e3b94310f731.jsonl[1267] _id=69e7b6671724f0c9e2f9402f ts=2026-04-21T17:39:50.8910000Z; 49h 15m: 69cdc907d385e3b94310f731.jsonl[153] _id=69dfdaa77957a33870f45eb1 ts=2026-04-15T18:36:23.0800000Z -> 69cdc907d385e3b94310f731.jsonl[1117] _id=69e28f531724f0c9e2f7cc66 ts=2026-04-17T19:51:47.6180000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 4m 
  - Evidence: 144h 4m: 69cdc907d385e3b94310f731.jsonl[674] _id=69dfd1f87957a33870f4212b ts=2026-04-15T17:59:20.0300000Z -> 69cdc907d385e3b94310f731.jsonl[288] _id=69e7bc1e1724f0c9e2f967e0 ts=2026-04-21T18:04:14.3780000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 5m 
  - Evidence: 144h 5m: 69cdc907d385e3b94310f731.jsonl[672] _id=69dfd1f67957a33870f42117 ts=2026-04-15T17:59:18.2370000Z -> 69cdc907d385e3b94310f731.jsonl[1440] _id=69e7bc241724f0c9e2f96817 ts=2026-04-21T18:04:20.4960000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 69cdc907d385e3b94310f731.jsonl[294] _id=69e7bc821724f0c9e2f96a93 ts=2026-04-21T18:05:54.0450000Z -> 69cdc907d385e3b94310f731.jsonl[295] _id=69e7bc821724f0c9e2f96a95 ts=2026-04-21T18:05:54.0510000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 93h 5m 
  - Evidence: 93h 5m: 69cdc907d385e3b94310f731.jsonl[1109] _id=69e28f3c1724f0c9e2f7cbd4 ts=2026-04-17T19:51:24.4320000Z -> 69cdc907d385e3b94310f731.jsonl[258] _id=69e7ac3c1724f0c9e2f916c3 ts=2026-04-21T16:56:26.8020000Z; 49h 6m: 69cdc907d385e3b94310f731.jsonl[148] _id=69dfda9a7957a33870f45e4b ts=2026-04-15T18:36:09.5360000Z -> 69cdc907d385e3b94310f731.jsonl[1020] _id=69e28d2c1724f0c9e2f7bc7e ts=2026-04-17T19:42:35.8400000Z; 47h 25m: 69cdc907d385e3b94310f731.jsonl[1716] _id=69e7c4621724f0c9e2f9a68d ts=2026-04-21T18:39:30.4420000Z -> 69cdc907d385e3b94310f731.jsonl[1733] _id=69ea5f631724f0c9e2fb0bb2 ts=2026-04-23T18:05:21.9300000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 69cdc907d385e3b94310f731.jsonl[649] _id=69dfd1497957a33870f41c1f ts=2026-04-15T17:56:24.7960000Z -> 69cdc907d385e3b94310f731.jsonl[652] _id=69dfd1497957a33870f41c21 ts=2026-04-15T17:56:24.7970000Z; 3ms: 69cdc907d385e3b94310f731.jsonl[1837] _id=69ea632b1724f0c9e2fb2caf ts=2026-04-23T18:21:30.9610000Z -> 69cdc907d385e3b94310f731.jsonl[391] _id=69ea632b1724f0c9e2fb2cb1 ts=2026-04-23T18:21:30.9640000Z; 4ms: 69cdc907d385e3b94310f731.jsonl[1807] _id=69ea61e51724f0c9e2fb2239 ts=2026-04-23T18:16:04.9710000Z -> 69cdc907d385e3b94310f731.jsonl[1808] _id=69ea61e51724f0c9e2fb223b ts=2026-04-23T18:16:04.9750000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc907d385e3b94310f731.jsonl:69cdc907d385e3b94310f731, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f731.jsonl[787] _id=69dfd5427957a33870f436a7 ts=2026-04-15T18:13:21.9360000Z`; `69cdc907d385e3b94310f731.jsonl[1510] _id=69e7bdbf1724f0c9e2f9731b ts=2026-04-21T18:11:11.8770000Z`; `69cdc907d385e3b94310f731.jsonl[1747] _id=69ea5fdb1724f0c9e2fb0fe9 ts=2026-04-23T18:07:23.2420000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 30 record(s) match the trigger in 69cdc907d385e3b94310f731.jsonl:69cdc907d385e3b94310f731, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f731.jsonl[975] _id=69dfdaa77957a33870f45eab ts=2026-04-15T18:36:22.5380000Z`; `69cdc907d385e3b94310f731.jsonl[153] _id=69dfdaa77957a33870f45eb1 ts=2026-04-15T18:36:23.0800000Z`; `69cdc907d385e3b94310f731.jsonl[1117] _id=69e28f531724f0c9e2f7cc66 ts=2026-04-17T19:51:47.6180000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f731.jsonl[1329] _id=69e7b7de1724f0c9e2f94a55 ts=2026-04-21T17:46:06.2430000Z`; `69cdc907d385e3b94310f731.jsonl[1346] _id=69e7b87b1724f0c9e2f94eed ts=2026-04-21T17:48:43.0070000Z`; `69cdc907d385e3b94310f731.jsonl[1932] _id=69ea66ef1724f0c9e2fb490b ts=2026-04-23T18:37:35.1070000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f731.jsonl[301] _id=69e7bc941724f0c9e2f96b03 ts=2026-04-21T18:06:12.3440000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f731.jsonl[292] _id=69e7bc801724f0c9e2f96a83 ts=2026-04-21T18:05:52.3900000Z`; `69cdc907d385e3b94310f731.jsonl[293] _id=69e7bc801724f0c9e2f96a8b ts=2026-04-21T18:05:52.8120000Z`; `69cdc907d385e3b94310f731.jsonl[294] _id=69e7bc821724f0c9e2f96a93 ts=2026-04-21T18:05:54.0450000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc907d385e3b94310f731.jsonl[1717] _id=69e7c4661724f0c9e2f9a69f ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f731.jsonl[1461] _id=69e7bc801724f0c9e2f96a89 ts=2026-04-21T18:05:52.4650000Z`; `69cdc907d385e3b94310f731.jsonl[1462] _id=69e7bc811724f0c9e2f96a8f ts=2026-04-21T18:05:53.0380000Z`; `69cdc907d385e3b94310f731.jsonl[295] _id=69e7bc821724f0c9e2f96a95 ts=2026-04-21T18:05:54.0510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 158 unmatched 'DialogueStartEvent' (totals: 258 start, 103 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 33 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 1 of 1936 adjacent _id pairs reverse in client time; worst 0.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `69cdc907d385e3b94310f731.jsonl[106] _id=69dfd7ed7957a33870f446f1 ts=2026-04-15T18:24:44.7770000Z`; `69cdc907d385e3b94310f731.jsonl[880] _id=69dfd8227957a33870f44855 ts=2026-04-15T18:24:44.771Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.53s, min -334079.06s, max -0.05s over 1937 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f731\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=partial 
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
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 92 records 
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

### `DialogueEvent` — 1230 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (464); Unit 3 Dev (270); Unit 1 Dev (258); Unit 4 Dev - Dungeon (92); Unit 3 Dungeon Dev (91); Unit 4 Dev (55)
- **eventKey:** present on 869 of 1230 records
- **Intervals:** median 2.09s (p5 0.01s / p95 48.41s, n=1229)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x869; [conversationId, dialogueEventType] x361
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1230/1230 records)
    numeric range 10 .. 107 (33 unique)
data.dialogueEventType  (string, 1230/1230 records)
    "DialogueNodeEvent"  x869
    "DialogueStartEvent"  x258
    "DialogueFinishEvent"  x103
data.nodeId  (number, 869/1230 records)
    numeric range 0 .. 289 (191 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 462 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (172); Unit 1 Dev (95); Unit 3 Dev (78); Unit 4 Dev - Dungeon (45); Unit 3 Dungeon Dev (40); Unit 4 Dev (32)
- **Intervals:** median 30.00s (p5 29.98s / p95 45.08s, n=454)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 462/462 records)
data.position.x  (number, 462/462 records)
    numeric range -679.878 .. 1512.99 (227 unique)
data.position.y  (number, 462/462 records)
    numeric range -112.489 .. 156.063 (183 unique)
data.position.z  (number, 462/462 records)
    numeric range -1104.29 .. 1745.67 (227 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 92 records

- **Scenes:** Unit 2 Prod (Refactor) (48); Unit 3 Dev (44)
- **Intervals:** median 8.63s (p5 0.76s / p95 802.55s, n=91)
- **Fields under `data`:**

```text
data.actionType  (string, 92/92 records)
    "MapCloseEvent"  x50
    "MapOpenEvent"  x42
data.featureUsed  (string, 92/92 records)
    "Map"  x92
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 57 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (16); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (4); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 57 of 57 records
- **Intervals:** median 140.06s (p5 0.01s / p95 170114.48s, n=56)
- **`data` key-set variants:** [questEventType, questID, questName] x33; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Fields under `data`:**

```text
data.questEventType  (string, 57/57 records)
    "questActiveEvent"  x33
    "questFinishEvent"  x24
data.questID  (string, 57/57 records)
    22 unique values (see csv/event_unique_values.csv)
data.questName  (string, 57/57 records)
    22 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/57 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 30 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (6)
- **Intervals:** median 3.52s (p5 0.55s / p95 106556.53s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "dragEnd"  x15
    "dragStart"  x15
data.featureUsed  (string, 30/30 records)
    "waypoint"  x30
data.location  (object, 30/30 records)
data.location.x  (number, 30/30 records)
    numeric range -792.954 .. 389.121 (17 unique)
data.location.y  (number, 30/30 records)
    numeric range -331.411 .. 161.736 (16 unique)
data.location.z  (number, 30/30 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 5.83s (p5 0.28s / p95 61.07s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Bedrock"  x14
    "Clay"  x9
    "Sand"  x2
    "Gravel"  x1
data.floor  (string, 26/26 records)
    "5"  x25
    "4"  x1
data.machine  (string, 26/26 records)
    "1"  x24
    "2"  x2
data.row  (string, 26/26 records)
    "BottomRow"  x14
    "TopRow"  x12
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationNodeEvent` — 14 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (11); Unit 1 Dev (3)
- **Intervals:** median 8.10s (p5 1.22s / p95 207501.70s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 14/14 records)
    "B"  x9
    "I"  x2
    "1"  x1
    "5"  x1
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (10)
- **Intervals:** median 0.77s (p5 0.03s / p95 2.55s, n=9)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolClose"  x5
    "argumentationToolOpen"  x5
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x10
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - "  x4
    "BackingInfoPanel - Watershed Image"  x4
    "BackingInfoPanel - Pollution Site Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 7 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 2132.04s (p5 6.50s / p95 428642.99s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 7/7 records)
    "Started"  x4
    "Finished"  x3
data.Unit  (string, 7/7 records)
    "Unit 2 Prod (Refactor)"  x3
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 27.77s (p5 0.80s / p95 389050.23s, n=6)
- **Open findings:** 2 — see sections 5-8
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

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 520654.80s (p5 520654.80s / p95 520654.80s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
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
    "Cannot close a closed AudioContext."  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (3 records)
- `TopographicMapEvent` data.actionType: "dragStart" (15x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (14x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*