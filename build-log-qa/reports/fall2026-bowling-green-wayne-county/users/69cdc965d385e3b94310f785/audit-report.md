# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f785

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f785
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f785.jsonl
- **Records:** 3069 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f785
- **Time span:** 2026-04-14T13:43:19.243000+00:00 .. 2026-04-22T13:45:19.368000+00:00 (192h 2m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f785\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 3069 records, 9 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 68 INFO, 0 NOT_TESTED, 54 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2308 | 75.2 | 1 | 9 | 1634 | 2026-04-14T13:43:37.650000+00:00 | 2026-04-22T13:45:19.368000+00:00 | 192h 1m |
| PlayerPositionEvent | 462 | 15.05 | 1 | 9 | 0 | 2026-04-14T13:43:19.243000+00:00 | 2026-04-22T13:45:13.973000+00:00 | 192h 1m |
| questEvent | 108 | 3.52 | 1 | 9 | 108 | 2026-04-14T13:43:37.637000+00:00 | 2026-04-22T13:43:43.374000+00:00 | 192h 0m |
| WaterChamberEvent | 43 | 1.4 | 1 | 1 | 0 | 2026-04-22T13:22:52.797000+00:00 | 2026-04-22T13:28:21.440000+00:00 | 5m 28s |
| Topographic Map Event | 36 | 1.17 | 1 | 2 | 0 | 2026-04-14T14:04:45.678000+00:00 | 2026-04-20T13:56:39.507000+00:00 | 143h 51m |
| soilMachine | 26 | 0.85 | 1 | 1 | 0 | 2026-04-20T14:12:02.305000+00:00 | 2026-04-20T14:19:30.021000+00:00 | 7m 27s |
| Soil Key Puzzle | 23 | 0.75 | 1 | 3 | 0 | 2026-04-14T14:11:47.855000+00:00 | 2026-04-20T14:03:57.273000+00:00 | 143h 52m |
| argumentationEvent | 14 | 0.46 | 1 | 4 | 0 | 2026-04-14T13:56:51.941000+00:00 | 2026-04-22T13:34:36.008000+00:00 | 191h 37m |
| argumentationToolEvent | 12 | 0.39 | 1 | 1 | 0 | 2026-04-20T14:27:33.652000+00:00 | 2026-04-20T14:28:44.437000+00:00 | 1m 10s |
| TerasGardenBox | 11 | 0.36 | 1 | 1 | 0 | 2026-04-20T14:34:33.548000+00:00 | 2026-04-22T13:16:27.281000+00:00 | 46h 41m |
| argumentationNodeEvent | 11 | 0.36 | 1 | 2 | 0 | 2026-04-14T13:57:18.581000+00:00 | 2026-04-20T13:37:44.574000+00:00 | 143h 40m |
| TopographicMapEvent | 8 | 0.26 | 1 | 1 | 0 | 2026-04-20T13:54:23.586000+00:00 | 2026-04-20T13:56:37.891000+00:00 | 2m 14s |
| EndOfUnit | 7 | 0.23 | 1 | 4 | 0 | 2026-04-14T14:00:27.203000+00:00 | 2026-04-22T13:43:20.101000+00:00 | 191h 42m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.189s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 85872.711s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
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
  - Observed: 331.269s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 10.384s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 3.116s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 24.283s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.08s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.793s median 
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
  - Observed: 5.999s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 36 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
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
  - Observed: 2; 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 60 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f785.jsonl[832] _id=69de47d57957a33870f332e1 ts=2026-04-14T13:57:41.1610000Z`; `69cdc965d385e3b94310f785.jsonl[1040] _id=69de4c9c7957a33870f355eb ts=2026-04-14T14:18:04.5900000Z`; `69cdc965d385e3b94310f785.jsonl[1166] _id=69e0e5b27957a33870f4feb3 ts=2026-04-16T13:35:45.8270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:22' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc965d385e3b94310f785.jsonl[1225] _id=69e0e7657957a33870f509e9 ts=2026-04-16T13:42:59.6910000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 36 records, TopographicMapEvent: 8 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2307 | 0.0 | 1.189 | 299.654 | 24.471 | 309461.072 | 0.2 | 554 | 5 |
| PlayerPositionEvent | 448 | 25.49 | 30.008 | 1541.536 | 37.889 | 309045.427 | 0.04 | 0 | 4 |
| questEvent | 107 | 0.001 | 81.916 | 6459.867 | 713.384 | 309303.275 | 0.01 | 20 | 9 |
| WaterChamberEvent | 42 | 0.227 | 3.116 | 7.825 | 25.744 | 43.425 | 7.67 | 0 | 0 |
| Topographic Map Event | 35 | 0.581 | 17.085 | 14797.538 | 52791.704 | 341575.062 | 0.0 | 0 | 5 |
| soilMachine | 25 | 0.265 | 5.999 | 17.909 | 56.963 | 185.712 | 3.35 | 0 | 0 |
| Soil Key Puzzle | 22 | 2.996 | 331.269 | 23542.246 | 162749.08 | 310673.427 | 0.0 | 0 | 7 |
| argumentationEvent | 13 | 0.104 | 24.283 | 53066.467 | 241646.177 | 343240.533 | 0.0 | 0 | 4 |
| argumentationToolEvent | 11 | 0.002 | 0.793 | 6.435 | 32.712 | 63.675 | 9.32 | 2 | 0 |
| TerasGardenBox | 10 | 0.189 | 10.384 | 16811.373 | 92427.729 | 168027.976 | 0.0 | 0 | 1 |
| argumentationNodeEvent | 10 | 1.032 | 6.08 | 51722.599 | 267060.056 | 343252.846 | 0.0 | 0 | 2 |
| TopographicMapEvent | 7 | 1.54 | 2.919 | 19.186 | 55.222 | 64.321 | 3.13 | 0 | 0 |
| EndOfUnit | 6 | 0.0 | 85872.711 | 115028.816 | 301753.086 | 344363.09 | 0.0 | 1 | 4 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.97s, p95 37.89s, n=448) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc965d385e3b94310f785.jsonl[872] _id=69de487b7957a33870f33715 ts=2026-04-14T14:00:27.2030000Z ~ 69cdc965d385e3b94310f785.jsonl[873] _id=69de488d7957a33870f33775 ts=2026-04-14T14:00:27.203Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `189ms: 69cdc965d385e3b94310f785.jsonl[2629] _id=69e639911724f0c9e2f8b4e7 ts=2026-04-20T14:34:57.1740000Z ~ 69cdc965d385e3b94310f785.jsonl[536] _id=69e639911724f0c9e2f8b4e9 ts=2026-04-20T14:34:57.3630000Z`; `204ms: 69cdc965d385e3b94310f785.jsonl[536] _id=69e639911724f0c9e2f8b4e9 ts=2026-04-20T14:34:57.3630000Z ~ 69cdc965d385e3b94310f785.jsonl[537] _id=69e639911724f0c9e2f8b4eb ts=2026-04-20T14:34:57.5670000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `462ms: 69cdc965d385e3b94310f785.jsonl[2772] _id=69e8cc141724f0c9e2fa151d ts=2026-04-22T13:24:35.6370000Z ~ 69cdc965d385e3b94310f785.jsonl[2770] _id=69e8cc141724f0c9e2fa1523 ts=2026-04-22T13:24:36.0990000Z`; `736ms: 69cdc965d385e3b94310f785.jsonl[597] _id=69e8cc141724f0c9e2fa151f ts=2026-04-22T13:24:35.8640000Z ~ 69cdc965d385e3b94310f785.jsonl[598] _id=69e8cc151724f0c9e2fa1527 ts=2026-04-22T13:24:36.6000000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `104ms: 69cdc965d385e3b94310f785.jsonl[1985] _id=69e62c2c1724f0c9e2f86671 ts=2026-04-20T13:37:47.5210000Z ~ 69cdc965d385e3b94310f785.jsonl[368] _id=69e62c2c1724f0c9e2f86681 ts=2026-04-20T13:37:47.6250000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc965d385e3b94310f785.jsonl[2514] _id=69e637d61724f0c9e2f8ac31 ts=2026-04-20T14:27:33.6520000Z ~ 69cdc965d385e3b94310f785.jsonl[503] _id=69e637d61724f0c9e2f8ac33 ts=2026-04-20T14:27:33.6540000Z`; `891ms: 69cdc965d385e3b94310f785.jsonl[2502] _id=69e638171724f0c9e2f8ad81 ts=2026-04-20T14:28:39.0780000Z ~ 69cdc965d385e3b94310f785.jsonl[2531] _id=69e638181724f0c9e2f8ad85 ts=2026-04-20T14:28:39.9690000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 69cdc965d385e3b94310f785.jsonl[1225] _id=69e0e7657957a33870f509e9 ts=2026-04-16T13:42:59.6910000Z ~ 69cdc965d385e3b94310f785.jsonl[1224] _id=69e0e7657957a33870f509ed ts=2026-04-16T13:42:59.6920000Z`; `6ms: 69cdc965d385e3b94310f785.jsonl[2895] _id=69e8ce761724f0c9e2fa253f ts=2026-04-22T13:34:46.0810000Z ~ 69cdc965d385e3b94310f785.jsonl[2893] _id=69e8ce761724f0c9e2fa2543 ts=2026-04-22T13:34:46.0870000Z`; `6ms: 69cdc965d385e3b94310f785.jsonl[2950] _id=69e8cfa71724f0c9e2fa2e01 ts=2026-04-22T13:39:51.3560000Z ~ 69cdc965d385e3b94310f785.jsonl[2951] _id=69e8cfa81724f0c9e2fa2e05 ts=2026-04-22T13:39:51.3620000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `522ms: 69cdc965d385e3b94310f785.jsonl[476] _id=69e634731724f0c9e2f8950f ts=2026-04-20T14:13:06.6100000Z ~ 69cdc965d385e3b94310f785.jsonl[477] _id=69e634731724f0c9e2f89515 ts=2026-04-20T14:13:07.1320000Z`; `265ms: 69cdc965d385e3b94310f785.jsonl[477] _id=69e634731724f0c9e2f89515 ts=2026-04-20T14:13:07.1320000Z ~ 69cdc965d385e3b94310f785.jsonl[478] _id=69e634731724f0c9e2f89517 ts=2026-04-20T14:13:07.3970000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 85h 57m 
  - Evidence: 85h 57m: 69cdc965d385e3b94310f785.jsonl[346] _id=69e16f601724f0c9e2f71812 ts=2026-04-16T23:23:11.6950000Z -> 69cdc965d385e3b94310f785.jsonl[1811] _id=69e628351724f0c9e2f84df7 ts=2026-04-20T13:20:52.7670000Z; 47h 3m: 69cdc965d385e3b94310f785.jsonl[1145] _id=69de4f9f7957a33870f369b4 ts=2026-04-14T14:30:55.7070000Z -> 69cdc965d385e3b94310f785.jsonl[1151] _id=69e0e5507957a33870f4fa03 ts=2026-04-16T13:34:07.5550000Z; 46h 39m: 69cdc965d385e3b94310f785.jsonl[543] _id=69e639aa1724f0c9e2f8b59b ts=2026-04-20T14:35:22.1920000Z -> 69cdc965d385e3b94310f785.jsonl[2654] _id=69e8c9d91724f0c9e2fa09f1 ts=2026-04-22T13:15:05.2340000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 554 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f785.jsonl[590] _id=69e8cad51724f0c9e2fa0ee1 ts=2026-04-22T13:19:16.8260000Z -> 69cdc965d385e3b94310f785.jsonl[2732] _id=69e8caea1724f0c9e2fa0f29 ts=2026-04-22T13:19:16.826Z; 2ms: 69cdc965d385e3b94310f785.jsonl[2576] _id=69e639371724f0c9e2f8b10d ts=2026-04-20T14:33:26.9140000Z -> 69cdc965d385e3b94310f785.jsonl[2573] _id=69e639371724f0c9e2f8b10f ts=2026-04-20T14:33:26.9160000Z; 2ms: 69cdc965d385e3b94310f785.jsonl[843] _id=69de48157957a33870f33499 ts=2026-04-14T13:58:45.4320000Z -> 69cdc965d385e3b94310f785.jsonl[40] _id=69de48157957a33870f3349b ts=2026-04-14T13:58:45.4340000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 39m 
  - Evidence: 95h 39m: 69cdc965d385e3b94310f785.jsonl[255] _id=69e0efdf7957a33870f53ce7 ts=2026-04-16T14:19:10.2770000Z -> 69cdc965d385e3b94310f785.jsonl[428] _id=69e631091724f0c9e2f8816d ts=2026-04-20T13:58:33.3670000Z; 48h 18m: 69cdc965d385e3b94310f785.jsonl[873] _id=69de488d7957a33870f33775 ts=2026-04-14T14:00:27.203Z -> 69cdc965d385e3b94310f785.jsonl[255] _id=69e0efdf7957a33870f53ce7 ts=2026-04-16T14:19:10.2770000Z; 47h 20m: 69cdc965d385e3b94310f785.jsonl[428] _id=69e631091724f0c9e2f8816d ts=2026-04-20T13:58:33.3670000Z -> 69cdc965d385e3b94310f785.jsonl[589] _id=69e8cad51724f0c9e2fa0edf ts=2026-04-22T13:19:16.8140000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f785.jsonl[872] _id=69de487b7957a33870f33715 ts=2026-04-14T14:00:27.2030000Z -> 69cdc965d385e3b94310f785.jsonl[873] _id=69de488d7957a33870f33775 ts=2026-04-14T14:00:27.203Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 85h 50m 
  - Evidence: 85h 50m: 69cdc965d385e3b94310f785.jsonl[1803] _id=69e170531724f0c9e2f71816 ts=2026-04-16T23:27:14.8620000Z -> 69cdc965d385e3b94310f785.jsonl[1810] _id=69e627891724f0c9e2f84ab1 ts=2026-04-20T13:18:00.2890000Z; 47h 1m: 69cdc965d385e3b94310f785.jsonl[1147] _id=69de4fc57957a33870f36aa8 ts=2026-04-14T14:31:33.2890000Z -> 69cdc965d385e3b94310f785.jsonl[1148] _id=69e0e5277957a33870f4f9b9 ts=2026-04-16T13:33:25.7970000Z; 46h 39m: 69cdc965d385e3b94310f785.jsonl[544] _id=69e639c21724f0c9e2f8b5a9 ts=2026-04-20T14:35:46.0680000Z -> 69cdc965d385e3b94310f785.jsonl[2651] _id=69e8c9cc1724f0c9e2fa09d3 ts=2026-04-22T13:14:51.7490000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 86h 17m 
  - Evidence: 86h 17m: 69cdc965d385e3b94310f785.jsonl[344] _id=69e16f4c1724f0c9e2f71808 ts=2026-04-16T23:22:51.8630000Z -> 69cdc965d385e3b94310f785.jsonl[2058] _id=69e62cdd1724f0c9e2f86c11 ts=2026-04-20T13:40:45.2900000Z; 47h 8m: 69cdc965d385e3b94310f785.jsonl[1126] _id=69de4f577957a33870f3672a ts=2026-04-14T14:29:43.3090000Z -> 69cdc965d385e3b94310f785.jsonl[91] _id=69e0e6567957a33870f5024d ts=2026-04-16T13:38:29.9960000Z; 8h 22m: 69cdc965d385e3b94310f785.jsonl[1752] _id=69e0f3767957a33870f557e3 ts=2026-04-16T14:34:29.6110000Z -> 69cdc965d385e3b94310f785.jsonl[1789] _id=69e169541724f0c9e2f71750 ts=2026-04-16T22:57:24.1610000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 46h 40m 
  - Evidence: 46h 40m: 69cdc965d385e3b94310f785.jsonl[537] _id=69e639911724f0c9e2f8b4eb ts=2026-04-20T14:34:57.5670000Z -> 69cdc965d385e3b94310f785.jsonl[2661] _id=69e8c9ee1724f0c9e2fa0a97 ts=2026-04-22T13:15:25.5430000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 52m 
  - Evidence: 94h 52m: 69cdc965d385e3b94310f785.jsonl[285] _id=69e0f2dc7957a33870f551ef ts=2026-04-16T14:31:56.0750000Z -> 69cdc965d385e3b94310f785.jsonl[1853] _id=69e629231724f0c9e2f8524b ts=2026-04-20T13:24:51.1370000Z; 47h 29m: 69cdc965d385e3b94310f785.jsonl[1072] _id=69de4d6f7957a33870f35adb ts=2026-04-14T14:21:35.3280000Z -> 69cdc965d385e3b94310f785.jsonl[138] _id=69e0e93b7957a33870f51579 ts=2026-04-16T13:50:50.5100000Z; 35m 50s: 69cdc965d385e3b94310f785.jsonl[1343] _id=69e0e9da7957a33870f519fe ts=2026-04-16T13:53:28.9170000Z -> 69cdc965d385e3b94310f785.jsonl[1669] _id=69e0f2407957a33870f54c47 ts=2026-04-16T14:29:19.1310000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 69cdc965d385e3b94310f785.jsonl[222] _id=69e0ef4b7957a33870f53a23 ts=2026-04-16T14:16:42.7050000Z -> 69cdc965d385e3b94310f785.jsonl[1984] _id=69e62c131724f0c9e2f865b1 ts=2026-04-20T13:37:23.2380000Z; 48h 18m: 69cdc965d385e3b94310f785.jsonl[831] _id=69de47d57957a33870f332df ts=2026-04-14T13:57:41.1370000Z -> 69cdc965d385e3b94310f785.jsonl[233] _id=69e0ef327957a33870f53995 ts=2026-04-16T14:16:17.7430000Z; 47h 4m: 69cdc965d385e3b94310f785.jsonl[2515] _id=69e637db1724f0c9e2f8ac49 ts=2026-04-20T14:27:38.6250000Z -> 69cdc965d385e3b94310f785.jsonl[2848] _id=69e8cdc21724f0c9e2fa1fbe ts=2026-04-22T13:31:46.1850000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 69cdc965d385e3b94310f785.jsonl[221] _id=69e0ef487957a33870f53a1f ts=2026-04-16T14:16:39.5680000Z -> 69cdc965d385e3b94310f785.jsonl[2018] _id=69e62c1c1724f0c9e2f86603 ts=2026-04-20T13:37:32.4140000Z; 48h 18m: 69cdc965d385e3b94310f785.jsonl[35] _id=69de47d27957a33870f332d7 ts=2026-04-14T13:57:38.7730000Z -> 69cdc965d385e3b94310f785.jsonl[1521] _id=69e0ef437957a33870f539f9 ts=2026-04-16T14:16:34.3070000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.002s..0.049s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f785.jsonl[2514] _id=69e637d61724f0c9e2f8ac31 ts=2026-04-20T14:27:33.6520000Z -> 69cdc965d385e3b94310f785.jsonl[503] _id=69e637d61724f0c9e2f8ac33 ts=2026-04-20T14:27:33.6540000Z; 49ms: 69cdc965d385e3b94310f785.jsonl[509] _id=69e638191724f0c9e2f8ad95 ts=2026-04-20T14:28:41.4720000Z -> 69cdc965d385e3b94310f785.jsonl[510] _id=69e638191724f0c9e2f8ad97 ts=2026-04-20T14:28:41.5210000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 85h 55m 
  - Evidence: 85h 55m: 69cdc965d385e3b94310f785.jsonl[1809] _id=69e170551724f0c9e2f71818 ts=2026-04-16T23:27:17.0540000Z -> 69cdc965d385e3b94310f785.jsonl[348] _id=69e6288c1724f0c9e2f84f77 ts=2026-04-20T13:22:20.3290000Z; 47h 5m: 69cdc965d385e3b94310f785.jsonl[1116] _id=69de4f247957a33870f364ed ts=2026-04-14T14:28:52.3130000Z -> 69cdc965d385e3b94310f785.jsonl[70] _id=69e0e5607957a33870f4faab ts=2026-04-16T13:34:23.5110000Z; 46h 40m: 69cdc965d385e3b94310f785.jsonl[2599] _id=69e639561724f0c9e2f8b2b7 ts=2026-04-20T14:33:57.6810000Z -> 69cdc965d385e3b94310f785.jsonl[2648] _id=69e8c9ce1724f0c9e2fa09d5 ts=2026-04-22T13:14:53.7860000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 20 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 69cdc965d385e3b94310f785.jsonl[1225] _id=69e0e7657957a33870f509e9 ts=2026-04-16T13:42:59.6910000Z -> 69cdc965d385e3b94310f785.jsonl[1224] _id=69e0e7657957a33870f509ed ts=2026-04-16T13:42:59.6920000Z; 3ms: 69cdc965d385e3b94310f785.jsonl[1505] _id=69e0ef287957a33870f5395d ts=2026-04-16T14:16:07.3940000Z -> 69cdc965d385e3b94310f785.jsonl[227] _id=69e0ef287957a33870f5395f ts=2026-04-16T14:16:07.3970000Z; 3ms: 69cdc965d385e3b94310f785.jsonl[22] _id=69de47a07957a33870f331a1 ts=2026-04-14T13:56:47.8710000Z -> 69cdc965d385e3b94310f785.jsonl[23] _id=69de47a07957a33870f331a5 ts=2026-04-14T13:56:47.8740000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 9 record(s) match the trigger in 69cdc965d385e3b94310f785.jsonl:69cdc965d385e3b94310f785, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f785.jsonl[952] _id=69de4b267957a33870f349ff ts=2026-04-14T14:11:50.8780000Z`; `69cdc965d385e3b94310f785.jsonl[1126] _id=69de4f577957a33870f3672a ts=2026-04-14T14:29:43.3090000Z`; `69cdc965d385e3b94310f785.jsonl[92] _id=69e0e6597957a33870f50261 ts=2026-04-16T13:38:32.9920000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 8 record(s) match the trigger in 69cdc965d385e3b94310f785.jsonl:69cdc965d385e3b94310f785, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f785.jsonl[2183] _id=69e630101724f0c9e2f87c49 ts=2026-04-20T13:54:23.5860000Z`; `69cdc965d385e3b94310f785.jsonl[2184] _id=69e630111724f0c9e2f87c53 ts=2026-04-20T13:54:25.1830000Z`; `69cdc965d385e3b94310f785.jsonl[2188] _id=69e630331724f0c9e2f87d2f ts=2026-04-20T13:54:59.1740000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f785.jsonl[1872] _id=69e6297c1724f0c9e2f853d1 ts=2026-04-20T13:26:20.4010000Z`; `69cdc965d385e3b94310f785.jsonl[352] _id=69e629b61724f0c9e2f85585 ts=2026-04-20T13:27:16.9680000Z`; `69cdc965d385e3b94310f785.jsonl[2431] _id=69e636811724f0c9e2f8a2c5 ts=2026-04-20T14:21:53.1060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f785.jsonl[368] _id=69e62c2c1724f0c9e2f86681 ts=2026-04-20T13:37:47.6250000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f785.jsonl[2514] _id=69e637d61724f0c9e2f8ac31 ts=2026-04-20T14:27:33.6520000Z`; `69cdc965d385e3b94310f785.jsonl[503] _id=69e637d61724f0c9e2f8ac33 ts=2026-04-20T14:27:33.6540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f785.jsonl[1264] _id=69e0e8907957a33870f5114d ts=2026-04-16T13:47:59.8160000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f785.jsonl[1414] _id=69e0ec297957a33870f5266d ts=2026-04-16T14:03:20.4920000Z`; `69cdc965d385e3b94310f785.jsonl[1608] _id=69e0f1617957a33870f544c1 ts=2026-04-16T14:25:37.1790000Z`; `69cdc965d385e3b94310f785.jsonl[1742] _id=69e0f3617957a33870f55757 ts=2026-04-16T14:34:08.0960000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 221 unmatched 'DialogueStartEvent' (totals: 446 start, 228 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'Started' (totals: 14 open, 9 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 29 unmatched 'questActiveEvent' (totals: 68 start, 40 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.52s, min -22.08s, max +0.03s over 3069 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f785\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=complete 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 36 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2308 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (751); Unit 1 Dev (355); Unit 3 Dev (326); Unit 5 Dev (286); Unit 4 Dev (277); Unit 4 Dev - Anderson Base (104); Unit 4 Dev - Dungeon (95); Unit 3 Dungeon Dev (90); Unit 5 Dev - Dungeon (24)
- **eventKey:** present on 1634 of 2308 records
- **Intervals:** median 1.19s (p5 0.01s / p95 24.47s, n=2307)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1634; [conversationId, dialogueEventType] x674
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2308/2308 records)
    numeric range 10 .. 114 (45 unique)
data.dialogueEventType  (string, 2308/2308 records)
    "DialogueNodeEvent"  x1634
    "DialogueStartEvent"  x446
    "DialogueFinishEvent"  x228
data.nodeId  (number, 1634/2308 records)
    numeric range 0 .. 286 (200 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 462 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (202); Unit 1 Dev (56); Unit 3 Dev (51); Unit 4 Dev (39); Unit 5 Dev (32); Unit 4 Dev - Dungeon (29); Unit 3 Dungeon Dev (22); Unit 5 Dev - Dungeon (18); Unit 4 Dev - Anderson Base (13)
- **Intervals:** median 30.01s (p5 29.97s / p95 37.89s, n=448)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 462/462 records)
data.position.x  (number, 462/462 records)
    numeric range -562.1 .. 1556.15 (301 unique)
data.position.y  (number, 462/462 records)
    numeric range -113.937 .. 220.633 (243 unique)
data.position.z  (number, 462/462 records)
    numeric range -1107.7 .. 2326.1 (302 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 108 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 1 Dev (24); Unit 5 Dev (14); Unit 3 Dev (9); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 108 of 108 records
- **Intervals:** median 81.92s (p5 0.01s / p95 713.38s, n=107)
- **`data` key-set variants:** [questEventType, questID, questName] x68; [questEventType, questID, questName, questSuccessOrFailure] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 108/108 records)
    "questActiveEvent"  x68
    "questFinishEvent"  x40
data.questID  (string, 108/108 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 108/108 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 40/108 records)
    "Succeeded"  x40
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 43 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (43)
- **Intervals:** median 3.12s (p5 0.51s / p95 25.74s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "On"  x27
    "Off"  x16
data.floor  (string, 43/43 records)
    "4"  x20
    "3"  x16
    "1"  x4
    "2"  x3
data.machineNumber  (string, 43/43 records)
    "One"  x42
    "Two"  x1
data.machineType  (string, 43/43 records)
    "Condenser"  x24
    "Evaporator"  x12
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 43/43 records)
    "3"  x18
    "2"  x15
    "1"  x8
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Topographic Map Event` — 36 records

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (14)
- **Intervals:** median 17.09s (p5 1.82s / p95 52791.70s, n=35)
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
data.featureUsed  (string, 36/36 records)
    "Map"  x36
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 6.00s (p5 0.46s / p95 56.96s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Clay"  x11
    "Bedrock"  x5
    "Gravel"  x5
    "Sand"  x5
data.floor  (string, 26/26 records)
    "5"  x13
    "4"  x12
    "3"  x1
data.machine  (string, 26/26 records)
    "1"  x23
    "2"  x3
data.row  (string, 26/26 records)
    "TopRow"  x21
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 23 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 331.27s (p5 3.02s / p95 162749.08s, n=22)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 23/23 records)
    "Started"  x14
    "Finished"  x9
data.Unit  (string, 23/23 records)
    "Unit 2 Prod (Refactor)"  x19
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 24.28s (p5 0.57s / p95 241646.18s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 14/14 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (12)
- **Intervals:** median 0.79s (p5 0.03s / p95 32.71s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolClose"  x7
    "argumentationToolOpen"  x5
data.argumentationTitle  (string, 12/12 records)
    "Unit 4 - Flooding"  x12
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Soil Layers and Fountain Data"  x6
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 10.38s (p5 0.20s / p95 92427.73s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "cameraPlaced"  x11
data.boxId  (string, 11/11 records)
    "2"  x5
    "0"  x3
    "1"  x3
data.soilType  (string, 11/11 records)
    "None"  x11
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationNodeEvent` — 11 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3)
- **Intervals:** median 6.08s (p5 1.59s / p95 267060.06s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 1 - Freshwater"  x8
    "Unit 3 - Pollution Upstream"  x3
data.nodeName  (string, 11/11 records)
    "I"  x3
    "1"  x2
    "B"  x2
    "II"  x2
    "5"  x1
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 8 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (8)
- **Intervals:** median 2.92s (p5 1.56s / p95 55.22s, n=7)
- **Open findings:** 1 — see sections 5-8
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

### `EndOfUnit` — 7 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (3); Unit 5 Dev (2); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 85872.71s (p5 35.33s / p95 301753.09s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 7/7 records)
    "1"  x3
    "5"  x2
    "3"  x1
    "4"  x1
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
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (19 records)
- `TerasGardenBox` data.soilType: "None" (11x)
- `TopographicMapEvent` data.actionType: "dragStart" (4x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*