# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f782

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f782
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f782.jsonl
- **Records:** 2275 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f782
- **Time span:** 2026-04-14T13:45:49.461000+00:00 .. 2026-04-24T14:35:15.822000+00:00 (240h 49m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f782\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2275 records, 7 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 53 INFO, 2 NOT_TESTED, 41 PASS.
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
| DialogueEvent | 1441 | 63.34 | 1 | 7 | 1003 | 2026-04-14T13:46:07.375000+00:00 | 2026-04-24T14:34:53.621000+00:00 | 240h 48m |
| PlayerPositionEvent | 505 | 22.2 | 1 | 7 | 0 | 2026-04-14T13:45:49.461000+00:00 | 2026-04-24T14:35:15.822000+00:00 | 240h 49m |
| Topographic Map Event | 108 | 4.75 | 1 | 2 | 0 | 2026-04-16T13:56:06.022000+00:00 | 2026-04-24T13:59:02.956000+00:00 | 192h 2m |
| questEvent | 60 | 2.64 | 1 | 7 | 60 | 2026-04-14T13:46:07.363000+00:00 | 2026-04-24T14:34:46.771000+00:00 | 240h 48m |
| argumentationNodeEvent | 50 | 2.2 | 1 | 2 | 0 | 2026-04-14T14:09:48.398000+00:00 | 2026-04-22T13:33:38.465000+00:00 | 191h 23m |
| soilMachine | 42 | 1.85 | 1 | 1 | 0 | 2026-04-24T14:17:57.314000+00:00 | 2026-04-24T14:27:57.880000+00:00 | 10m 0s |
| TopographicMapEvent | 41 | 1.8 | 1 | 2 | 0 | 2026-04-16T13:56:14.385000+00:00 | 2026-04-24T13:59:01.516000+00:00 | 192h 2m |
| Soil Key Puzzle | 12 | 0.53 | 1 | 3 | 0 | 2026-04-16T13:50:28.139000+00:00 | 2026-04-24T14:07:28.188000+00:00 | 192h 17m |
| argumentationEvent | 10 | 0.44 | 1 | 2 | 0 | 2026-04-14T14:09:44.502000+00:00 | 2026-04-22T13:33:40.265000+00:00 | 191h 23m |
| argumentationToolEvent | 4 | 0.18 | 1 | 1 | 0 | 2026-04-22T13:32:49.505000+00:00 | 2026-04-22T13:32:52.553000+00:00 | 3.0s |
| EndOfUnit | 2 | 0.09 | 1 | 2 | 0 | 2026-04-14T14:15:26.391000+00:00 | 2026-04-24T14:01:53.042000+00:00 | 239h 46m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.738s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 863186.651s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.025s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 430.538s median 
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
  - Observed: 5.268s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.749s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.021s median 
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
  - Observed: 2.522s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 12 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 108 records this build 
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
  - Observed: C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 8.4x vs baseline. 
  - Observed: 42 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 277 mismatch(es); e.g. 'DialogueNodeEvent:30:38' vs expected 'DialogueNodeEvent:36:60' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f782.jsonl[30] _id=69de48b47957a33870f3382d ts=2026-04-14T13:52:17.8370000Z`; `69cdc965d385e3b94310f782.jsonl[31] _id=69de48c77957a33870f338b7 ts=2026-04-14T13:52:31.9040000Z`; `69cdc965d385e3b94310f782.jsonl[32] _id=69de48c97957a33870f338c7 ts=2026-04-14T13:52:38.7350000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'questFinishEvent:29' vs expected 'questFinishEvent:31' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc965d385e3b94310f782.jsonl[944] _id=69de490b7957a33870f33acb ts=2026-04-14T13:53:28.8020000Z`; `69cdc965d385e3b94310f782.jsonl[38] _id=69de490b7957a33870f33acf ts=2026-04-14T13:53:28.8120000Z`; `69cdc965d385e3b94310f782.jsonl[114] _id=69de4d3e7957a33870f35969 ts=2026-04-14T14:12:08.39Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 108 records, TopographicMapEvent: 41 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1440 | 0.0 | 1.738 | 602.032 | 41.388 | 341179.636 | 0.1 | 318 | 5 |
| PlayerPositionEvent | 493 | 29.858 | 30.025 | 723.94 | 39.934 | 170866.269 | 0.08 | 0 | 2 |
| Topographic Map Event | 107 | 0.005 | 11.949 | 6461.467 | 498.215 | 341885.124 | 0.01 | 5 | 5 |
| questEvent | 59 | 0.004 | 165.54 | 14693.549 | 169858.153 | 341193.014 | 0.0 | 7 | 10 |
| argumentationNodeEvent | 49 | 1.236 | 6.749 | 14061.838 | 53.036 | 517740.305 | 0.0 | 0 | 2 |
| soilMachine | 41 | 0.064 | 2.522 | 14.648 | 56.926 | 166.852 | 4.1 | 0 | 0 |
| TopographicMapEvent | 40 | 0.449 | 5.268 | 17284.178 | 171956.429 | 344019.152 | 0.0 | 0 | 5 |
| Soil Key Puzzle | 11 | 3.0 | 430.538 | 62929.095 | 259350.157 | 344171.689 | 0.0 | 0 | 5 |
| argumentationEvent | 9 | 0.094 | 46.414 | 76559.529 | 378982.826 | 517731.964 | 0.0 | 0 | 2 |
| argumentationToolEvent | 3 | 0.075 | 1.021 | 1.016 | 1.859 | 1.952 | 59.06 | 0 | 0 |
| EndOfUnit | 1 | 863186.651 | 863186.651 | 863186.651 | 863186.651 | 863186.651 | 0.0 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.025s (p5 29.96s, p95 39.93s, n=493) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 69cdc965d385e3b94310f782.jsonl[1265] _id=69e0eb297957a33870f521a1 ts=2026-04-16T13:59:04.6310000Z ~ 69cdc965d385e3b94310f782.jsonl[185] _id=69e0eb297957a33870f521a3 ts=2026-04-16T13:59:04.6530000Z`; `6ms: 69cdc965d385e3b94310f782.jsonl[185] _id=69e0eb297957a33870f521a3 ts=2026-04-16T13:59:04.6530000Z ~ 69cdc965d385e3b94310f782.jsonl[1266] _id=69e0eb2a7957a33870f521a5 ts=2026-04-16T13:59:04.6590000Z`; `5ms: 69cdc965d385e3b94310f782.jsonl[1266] _id=69e0eb2a7957a33870f521a5 ts=2026-04-16T13:59:04.6590000Z ~ 69cdc965d385e3b94310f782.jsonl[186] _id=69e0eb2a7957a33870f521a9 ts=2026-04-16T13:59:04.6640000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `295ms: 69cdc965d385e3b94310f782.jsonl[535] _id=69e6394f1724f0c9e2f8b249 ts=2026-04-20T14:03:07.1030000Z ~ 69cdc965d385e3b94310f782.jsonl[1531] _id=69e639501724f0c9e2f8b251 ts=2026-04-20T14:03:07.3980000Z`; `94ms: 69cdc965d385e3b94310f782.jsonl[734] _id=69e8ce341724f0c9e2fa2343 ts=2026-04-22T13:33:40.1710000Z ~ 69cdc965d385e3b94310f782.jsonl[732] _id=69e8ce351724f0c9e2fa234f ts=2026-04-22T13:33:40.2650000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `882ms: 69cdc965d385e3b94310f782.jsonl[2173] _id=69eb7cc21724f0c9e2fb94fd ts=2026-04-24T14:22:58.3000000Z ~ 69cdc965d385e3b94310f782.jsonl[2170] _id=69eb7cc31724f0c9e2fb94ff ts=2026-04-24T14:22:59.1820000Z`; `811ms: 69cdc965d385e3b94310f782.jsonl[2171] _id=69eb7cc51724f0c9e2fb9505 ts=2026-04-24T14:23:01.4680000Z ~ 69cdc965d385e3b94310f782.jsonl[2166] _id=69eb7cc61724f0c9e2fb950b ts=2026-04-24T14:23:02.2790000Z`; `351ms: 69cdc965d385e3b94310f782.jsonl[2166] _id=69eb7cc61724f0c9e2fb950b ts=2026-04-24T14:23:02.2790000Z ~ 69cdc965d385e3b94310f782.jsonl[2172] _id=69eb7cc61724f0c9e2fb950f ts=2026-04-24T14:23:02.6300000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc965d385e3b94310f782.jsonl[1451] _id=69e0f33d7957a33870f554f9 ts=2026-04-16T14:33:32.9360000Z -> 69cdc965d385e3b94310f782.jsonl[293] _id=69e627f91724f0c9e2f84ce9 ts=2026-04-20T13:19:52.5720000Z; 48h 3m: 69cdc965d385e3b94310f782.jsonl[1853] _id=69e8d3291724f0c9e2fa432f ts=2026-04-22T13:54:48.2990000Z -> 69cdc965d385e3b94310f782.jsonl[1950] _id=69eb76fa1724f0c9e2fb7731 ts=2026-04-24T13:58:17.9170000Z; 47h 2m: 69cdc965d385e3b94310f782.jsonl[1121] _id=69de4fb47957a33870f36a46 ts=2026-04-14T14:31:16.3350000Z -> 69cdc965d385e3b94310f782.jsonl[1124] _id=69e0e5497957a33870f4f9e1 ts=2026-04-16T13:34:00.6960000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 318 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f782.jsonl[1994] _id=69eb77d11724f0c9e2fb7b8b ts=2026-04-24T14:01:53.0580000Z -> 69cdc965d385e3b94310f782.jsonl[2013] _id=69eb77dd1724f0c9e2fb7bcb ts=2026-04-24T14:01:53.058Z; 0ms: 69cdc965d385e3b94310f782.jsonl[932] _id=69de46857957a33870f32cf7 ts=2026-04-14T13:51:58.8180000Z -> 69cdc965d385e3b94310f782.jsonl[29] _id=69de48b47957a33870f3382b ts=2026-04-14T13:51:58.8180000Z; 3ms: 69cdc965d385e3b94310f782.jsonl[1398] _id=69e0f23d7957a33870f54c1b ts=2026-04-16T14:29:16.7900000Z -> 69cdc965d385e3b94310f782.jsonl[1399] _id=69e0f23d7957a33870f54c1d ts=2026-04-16T14:29:16.7930000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 239h 46m 
  - Evidence: 239h 46m: 69cdc965d385e3b94310f782.jsonl[131] _id=69de4d427957a33870f359d3 ts=2026-04-14T14:15:26.391Z -> 69cdc965d385e3b94310f782.jsonl[845] _id=69eb77d11724f0c9e2fb7b89 ts=2026-04-24T14:01:53.0420000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 27m 
  - Evidence: 47h 27m: 69cdc965d385e3b94310f782.jsonl[1938] _id=69e8db431724f0c9e2fa74b3 ts=2026-04-22T14:29:23.1120000Z -> 69cdc965d385e3b94310f782.jsonl[1941] _id=69eb76b51724f0c9e2fb7691 ts=2026-04-24T13:57:09.3810000Z; 47h 1m: 69cdc965d385e3b94310f782.jsonl[1122] _id=69de4fc37957a33870f36a9c ts=2026-04-14T14:31:31.1180000Z -> 69cdc965d385e3b94310f782.jsonl[1123] _id=69e0e5277957a33870f4f9b7 ts=2026-04-16T13:33:23.9930000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 36m 
  - Evidence: 95h 36m: 69cdc965d385e3b94310f782.jsonl[286] _id=69e0f3377957a33870f554d3 ts=2026-04-16T14:33:26.8660000Z -> 69cdc965d385e3b94310f782.jsonl[569] _id=69e6395b1724f0c9e2f8b2ff ts=2026-04-20T14:09:38.5550000Z; 48h 28m: 69cdc965d385e3b94310f782.jsonl[1728] _id=69e8cf451724f0c9e2fa2a6d ts=2026-04-22T13:38:12.3660000Z -> 69cdc965d385e3b94310f782.jsonl[2037] _id=69eb79051724f0c9e2fb81fb ts=2026-04-24T14:07:00.9900000Z; 47h 27m: 69cdc965d385e3b94310f782.jsonl[333] _id=69e6395c1724f0c9e2f8b30d ts=2026-04-20T14:09:59.6980000Z -> 69cdc965d385e3b94310f782.jsonl[1726] _id=69e8cf311724f0c9e2fa29dd ts=2026-04-22T13:37:52.7880000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 58m 
  - Evidence: 94h 58m: 69cdc965d385e3b94310f782.jsonl[281] _id=69e0f3027957a33870f55319 ts=2026-04-16T14:32:34.1070000Z -> 69cdc965d385e3b94310f782.jsonl[319] _id=69e6382e1724f0c9e2f8add9 ts=2026-04-20T13:30:39.2310000Z; 47h 49m: 69cdc965d385e3b94310f782.jsonl[826] _id=69e8d6841724f0c9e2fa5981 ts=2026-04-22T14:09:07.0540000Z -> 69cdc965d385e3b94310f782.jsonl[1940] _id=69eb76ff1724f0c9e2fb7745 ts=2026-04-24T13:58:23.3240000Z; 47h 45m: 69cdc965d385e3b94310f782.jsonl[588] _id=69e639571724f0c9e2f8b2d1 ts=2026-04-20T14:08:31.4930000Z -> 69cdc965d385e3b94310f782.jsonl[812] _id=69e8d2f31724f0c9e2fa42b3 ts=2026-04-22T13:53:54.6700000Z
- **INFO / Info** `Topographic Map Event` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.005s..0.006s shown 
  - Evidence: 5ms: 69cdc965d385e3b94310f782.jsonl[1266] _id=69e0eb2a7957a33870f521a5 ts=2026-04-16T13:59:04.6590000Z -> 69cdc965d385e3b94310f782.jsonl[186] _id=69e0eb2a7957a33870f521a9 ts=2026-04-16T13:59:04.6640000Z; 5ms: 69cdc965d385e3b94310f782.jsonl[186] _id=69e0eb2a7957a33870f521a9 ts=2026-04-16T13:59:04.6640000Z -> 69cdc965d385e3b94310f782.jsonl[1267] _id=69e0eb2a7957a33870f521ad ts=2026-04-16T13:59:04.6690000Z; 6ms: 69cdc965d385e3b94310f782.jsonl[185] _id=69e0eb297957a33870f521a3 ts=2026-04-16T13:59:04.6530000Z -> 69cdc965d385e3b94310f782.jsonl[1266] _id=69e0eb2a7957a33870f521a5 ts=2026-04-16T13:59:04.6590000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc965d385e3b94310f782.jsonl[179] _id=69e0ea7e7957a33870f51e6b ts=2026-04-16T13:56:14.3850000Z -> 69cdc965d385e3b94310f782.jsonl[317] _id=69e6382b1724f0c9e2f8adc7 ts=2026-04-20T13:29:53.5370000Z; 47h 54m: 69cdc965d385e3b94310f782.jsonl[1892] _id=69e8d52b1724f0c9e2fa4f85 ts=2026-04-22T14:03:22.5270000Z -> 69cdc965d385e3b94310f782.jsonl[1944] _id=69eb76d11724f0c9e2fb76bd ts=2026-04-24T13:57:37.4850000Z; 47h 45m: 69cdc965d385e3b94310f782.jsonl[587] _id=69e639571724f0c9e2f8b2cf ts=2026-04-20T14:08:29.2040000Z -> 69cdc965d385e3b94310f782.jsonl[1847] _id=69e8d2f81724f0c9e2fa42bd ts=2026-04-22T13:53:59.3950000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 48m 
  - Evidence: 143h 48m: 69cdc965d385e3b94310f782.jsonl[81] _id=69de4d3d7957a33870f3594d ts=2026-04-14T14:11:40.054Z -> 69cdc965d385e3b94310f782.jsonl[489] _id=69e639451724f0c9e2f8b1d8 ts=2026-04-20T14:00:32.0180000Z; 47h 27m: 69cdc965d385e3b94310f782.jsonl[1531] _id=69e639501724f0c9e2f8b251 ts=2026-04-20T14:03:07.3980000Z -> 69cdc965d385e3b94310f782.jsonl[1647] _id=69e8cd871724f0c9e2fa1e07 ts=2026-04-22T13:30:46.5170000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 49m 
  - Evidence: 143h 49m: 69cdc965d385e3b94310f782.jsonl[72] _id=69de4d3d7957a33870f35949 ts=2026-04-14T14:11:33.494Z -> 69cdc965d385e3b94310f782.jsonl[490] _id=69e639461724f0c9e2f8b1df ts=2026-04-20T14:00:33.7990000Z; 47h 28m: 69cdc965d385e3b94310f782.jsonl[532] _id=69e6394e1724f0c9e2f8b23f ts=2026-04-20T14:02:59.8310000Z -> 69cdc965d385e3b94310f782.jsonl[705] _id=69e8cd991724f0c9e2fa1e85 ts=2026-04-22T13:31:04.6280000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc965d385e3b94310f782.jsonl[1447] _id=69e0f3307957a33870f5549b ts=2026-04-16T14:33:19.5440000Z -> 69cdc965d385e3b94310f782.jsonl[1460] _id=69e627f81724f0c9e2f84ce7 ts=2026-04-20T13:19:52.5580000Z; 48h 3m: 69cdc965d385e3b94310f782.jsonl[1843] _id=69e8d2e31724f0c9e2fa428b ts=2026-04-22T13:53:38.5420000Z -> 69cdc965d385e3b94310f782.jsonl[1939] _id=69eb76b91724f0c9e2fb7697 ts=2026-04-24T13:57:12.7500000Z; 47h 11m: 69cdc965d385e3b94310f782.jsonl[1072] _id=69de4dbe7957a33870f35c8f ts=2026-04-14T14:22:54.8590000Z -> 69cdc965d385e3b94310f782.jsonl[146] _id=69e0e5567957a33870f4fa1d ts=2026-04-16T13:34:13.0300000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.004s..0.009s shown 
  - Evidence: 4ms: 69cdc965d385e3b94310f782.jsonl[1031] _id=69de4a5b7957a33870f3449b ts=2026-04-14T14:08:20.3990000Z -> 69cdc965d385e3b94310f782.jsonl[1032] _id=69de4a607957a33870f344ab ts=2026-04-14T14:08:20.4030000Z; 7ms: 69cdc965d385e3b94310f782.jsonl[2084] _id=69eb7a4b1724f0c9e2fb88d9 ts=2026-04-24T14:12:26.8400000Z -> 69cdc965d385e3b94310f782.jsonl[2085] _id=69eb7a4b1724f0c9e2fb88dd ts=2026-04-24T14:12:26.8470000Z; 9ms: 69cdc965d385e3b94310f782.jsonl[2111] _id=69eb7b001724f0c9e2fb8c01 ts=2026-04-24T14:15:27.7700000Z -> 69cdc965d385e3b94310f782.jsonl[2112] _id=69eb7b001724f0c9e2fb8c03 ts=2026-04-24T14:15:27.7790000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc965d385e3b94310f782.jsonl:69cdc965d385e3b94310f782, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f782.jsonl[159] _id=69e0e9277957a33870f514fa ts=2026-04-16T13:50:31.1390000Z`; `69cdc965d385e3b94310f782.jsonl[1340] _id=69e0edc67957a33870f53085 ts=2026-04-16T14:10:13.4740000Z`; `69cdc965d385e3b94310f782.jsonl[569] _id=69e6395b1724f0c9e2f8b2ff ts=2026-04-20T14:09:38.5550000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 41 record(s) match the trigger in 69cdc965d385e3b94310f782.jsonl:69cdc965d385e3b94310f782, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f782.jsonl[179] _id=69e0ea7e7957a33870f51e6b ts=2026-04-16T13:56:14.3850000Z`; `69cdc965d385e3b94310f782.jsonl[317] _id=69e6382b1724f0c9e2f8adc7 ts=2026-04-20T13:29:53.5370000Z`; `69cdc965d385e3b94310f782.jsonl[323] _id=69e6382c1724f0c9e2f8adcb ts=2026-04-20T13:29:57.9500000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f782.jsonl[941] _id=69de49137957a33870f33b15 ts=2026-04-14T13:53:45.6930000Z`; `69cdc965d385e3b94310f782.jsonl[974] _id=69de49517957a33870f33d0d ts=2026-04-14T13:57:59.9900000Z`; `69cdc965d385e3b94310f782.jsonl[989] _id=69de497e7957a33870f33e39 ts=2026-04-14T14:00:29.7440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Finished' preceded by 'Started' per Unit 
  - Examples: `69cdc965d385e3b94310f782.jsonl[569] _id=69e6395b1724f0c9e2f8b2ff ts=2026-04-20T14:09:38.5550000Z`; `69cdc965d385e3b94310f782.jsonl[333] _id=69e6395c1724f0c9e2f8b30d ts=2026-04-20T14:09:59.6980000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f782.jsonl[75] _id=69de4d3c7957a33870f35933 ts=2026-04-14T14:10:25.117Z`; `69cdc965d385e3b94310f782.jsonl[1055] _id=69de4d3d7957a33870f3593f ts=2026-04-14T14:11:11.531Z`; `69cdc965d385e3b94310f782.jsonl[81] _id=69de4d3d7957a33870f3594d ts=2026-04-14T14:11:40.054Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f782.jsonl[944] _id=69de490b7957a33870f33acb ts=2026-04-14T13:53:28.8020000Z`; `69cdc965d385e3b94310f782.jsonl[973] _id=69de49507957a33870f33d07 ts=2026-04-14T13:57:56.9460000Z`; `69cdc965d385e3b94310f782.jsonl[114] _id=69de4d3e7957a33870f35969 ts=2026-04-14T14:12:08.39Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f782.jsonl[286] _id=69e0f3377957a33870f554d3 ts=2026-04-16T14:33:26.8660000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 174 unmatched 'DialogueStartEvent' (totals: 302 start, 136 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 2 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'questActiveEvent' (totals: 39 start, 21 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.79s, min -3593.73s, max -0.01s over 2275 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f782\coverage.yaml

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
  - Observed: 108 records 
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

### `DialogueEvent` — 1441 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (504); Unit 2 Prod (Refactor) (376); Unit 1 Dev (203); Unit 3 Dungeon Dev (172); Unit 4 Dev - Dungeon (95); Unit 4 Dev (87); Unit 4 Dev - Anderson Base (4)
- **eventKey:** present on 1003 of 1441 records
- **Intervals:** median 1.74s (p5 0.01s / p95 41.39s, n=1440)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1003; [conversationId, dialogueEventType] x438
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1441/1441 records)
    numeric range 8 .. 107 (33 unique)
data.dialogueEventType  (string, 1441/1441 records)
    "DialogueNodeEvent"  x1003
    "DialogueStartEvent"  x302
    "DialogueFinishEvent"  x136
data.nodeId  (number, 1003/1441 records)
    numeric range 0 .. 290 (200 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 505 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (186); Unit 2 Prod (Refactor) (117); Unit 3 Dungeon Dev (70); Unit 1 Dev (64); Unit 4 Dev - Dungeon (39); Unit 4 Dev (27); Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 30.02s (p5 29.96s / p95 39.93s, n=493)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 505/505 records)
data.position.x  (number, 505/505 records)
    numeric range -692.282 .. 1477.09 (281 unique)
data.position.y  (number, 505/505 records)
    numeric range -114.326 .. 166.732 (220 unique)
data.position.z  (number, 505/505 records)
    numeric range -1109.71 .. 1741.41 (280 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 108 records

- **Scenes:** Unit 3 Dev (66); Unit 2 Prod (Refactor) (42)
- **Intervals:** median 11.95s (p5 1.17s / p95 498.22s, n=107)
- **Fields under `data`:**

```text
data.actionType  (string, 108/108 records)
    "MapCloseEvent"  x66
    "MapOpenEvent"  x42
data.featureUsed  (string, 108/108 records)
    "Map"  x108
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 60 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 3 Dev (15); Unit 1 Dev (13); Unit 4 Dev - Dungeon (9); Unit 4 Dev (4); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 60 of 60 records
- **Intervals:** median 165.54s (p5 0.01s / p95 169858.15s, n=59)
- **`data` key-set variants:** [questEventType, questID, questName] x39; [questEventType, questID, questName, questSuccessOrFailure] x21
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 60/60 records)
    "questActiveEvent"  x39
    "questFinishEvent"  x21
data.questID  (string, 60/60 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 60/60 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 21/60 records)
    "Succeeded"  x21
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 50 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (44); Unit 1 Dev (6)
- **Intervals:** median 6.75s (p5 1.57s / p95 53.04s, n=49)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "argumentationNodeAdd"  x40
    "argumentationNodeRemove"  x10
data.argumentationTitle  (string, 50/50 records)
    "Unit 3 - Pollution Upstream"  x44
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 50/50 records)
    "A"  x25
    "3"  x6
    "B"  x5
    "4"  x4
    "1"  x3
    "5"  x3
    "2"  x2
    "I"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 42 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (42)
- **Intervals:** median 2.52s (p5 0.12s / p95 56.93s, n=41)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "ChangeCanister"  x42
data.canisterType  (string, 42/42 records)
    "Bedrock"  x21
    "Clay"  x15
    "Gravel"  x4
    "Sand"  x2
data.floor  (string, 42/42 records)
    "5"  x40
    "3"  x1
    "4"  x1
data.machine  (string, 42/42 records)
    "1"  x38
    "2"  x4
data.row  (string, 42/42 records)
    "TopRow"  x25
    "BottomRow"  x17
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 41 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (40); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 5.27s (p5 1.14s / p95 171956.43s, n=40)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "dragStart"  x21
    "dragEnd"  x20
data.featureUsed  (string, 41/41 records)
    "waypoint"  x41
data.location  (object, 41/41 records)
data.location.x  (number, 41/41 records)
    numeric range -773.625 .. 262.47 (21 unique)
data.location.y  (number, 41/41 records)
    numeric range -314.487 .. 79.5411 (21 unique)
data.location.z  (number, 41/41 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 12 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (4); Unit 4 Dev (2)
- **Intervals:** median 430.54s (p5 11.29s / p95 259350.16s, n=11)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/12 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/12 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x4
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (6); Unit 1 Dev (4)
- **Intervals:** median 46.41s (p5 0.17s / p95 378982.83s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 10/10 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x6
    "Unit 1 - Does the planet WAT-247 have freshwater"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x1
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 1.02s (p5 0.17s / p95 1.86s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x2
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Pollution Site Data"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 863186.65s (p5 863186.65s / p95 863186.65s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
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
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (21x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (10x)
- `soilMachine` data.canisterType: "Bedrock" (21x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*