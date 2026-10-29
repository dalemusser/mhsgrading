# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7aa

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7aa
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7aa.jsonl
- **Records:** 1937 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7aa
- **Time span:** 2026-04-14T19:18:37.642000+00:00 .. 2026-04-22T19:56:11.431000+00:00 (192h 37m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7aa\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1937 records, 4 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 53 INFO, 5 NOT_TESTED, 34 PASS.
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
| DialogueEvent | 1222 | 63.09 | 1 | 4 | 856 | 2026-04-14T19:18:55.754000+00:00 | 2026-04-22T19:43:39.900000+00:00 | 192h 24m |
| PlayerPositionEvent | 504 | 26.02 | 1 | 4 | 0 | 2026-04-14T19:18:37.642000+00:00 | 2026-04-22T19:56:11.431000+00:00 | 192h 37m |
| Topographic Map Event | 66 | 3.41 | 1 | 2 | 0 | 2026-04-14T20:00:51.749000+00:00 | 2026-04-20T19:37:42.696000+00:00 | 143h 36m |
| questEvent | 35 | 1.81 | 1 | 4 | 35 | 2026-04-14T19:18:55.739000+00:00 | 2026-04-22T19:04:15.423000+00:00 | 191h 45m |
| TopographicMapEvent | 34 | 1.76 | 1 | 2 | 0 | 2026-04-16T19:02:29.101000+00:00 | 2026-04-20T19:31:25.639000+00:00 | 96h 28m |
| argumentationNodeEvent | 29 | 1.5 | 1 | 3 | 0 | 2026-04-14T19:40:05.158000+00:00 | 2026-04-20T19:43:47.562000+00:00 | 144h 3m |
| argumentationToolEvent | 26 | 1.34 | 1 | 1 | 0 | 2026-04-16T19:59:26.038000+00:00 | 2026-04-16T20:00:41.337000+00:00 | 1m 15s |
| argumentationEvent | 9 | 0.46 | 1 | 3 | 0 | 2026-04-14T19:39:52.481000+00:00 | 2026-04-20T19:43:50.364000+00:00 | 144h 3m |
| Soil Key Puzzle | 8 | 0.41 | 1 | 2 | 0 | 2026-04-14T19:55:36.185000+00:00 | 2026-04-20T19:49:15.846000+00:00 | 143h 53m |
| EndOfUnit | 2 | 0.1 | 1 | 2 | 0 | 2026-04-14T19:44:55.093000+00:00 | 2026-04-16T20:07:16.143000+00:00 | 48h 22m |
| crash | 2 | 0.1 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 174141.05s median 
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
  - Observed: 117.551s median 
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
  - Observed: 5.166s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.273s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.605s median 
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
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 66 records this build 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 29 records 
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
  - Observed: 2; 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
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
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[456] _id=69de98717957a33870f39b31 ts=2026-04-14T19:41:37.2810000Z`; `69cdc98ad385e3b94310f7aa.jsonl[135] _id=69e132d51724f0c9e2f69de6 ts=2026-04-16T19:04:52.1010000Z`; `69cdc98ad385e3b94310f7aa.jsonl[234] _id=69e140001724f0c9e2f70afa ts=2026-04-16T20:01:03.1780000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 66 records, TopographicMapEvent: 34 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1221 | 0.0 | 2.554 | 567.309 | 44.572 | 341154.505 | 0.11 | 317 | 5 |
| PlayerPositionEvent | 500 | 29.878 | 30.008 | 1386.701 | 41.589 | 341128.411 | 0.04 | 0 | 3 |
| Topographic Map Event | 65 | 0.446 | 18.665 | 7954.015 | 676.708 | 342723.375 | 0.01 | 0 | 4 |
| questEvent | 34 | 0.003 | 190.738 | 20303.52 | 168960.326 | 341393.821 | 0.0 | 3 | 9 |
| TopographicMapEvent | 33 | 1.317 | 5.166 | 10525.35 | 566.42 | 344918.297 | 0.01 | 0 | 2 |
| argumentationNodeEvent | 28 | 1.176 | 8.273 | 18522.229 | 112960.679 | 344550.378 | 0.0 | 0 | 2 |
| argumentationToolEvent | 25 | 0.01 | 0.605 | 3.012 | 12.355 | 27.322 | 19.92 | 1 | 0 |
| argumentationEvent | 8 | 0.154 | 39.23 | 64829.735 | 284760.632 | 344537.66 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 7 | 2.972 | 117.551 | 74002.809 | 293704.508 | 347017.19 | 0.0 | 0 | 3 |
| EndOfUnit | 1 | 174141.05 | 174141.05 | 174141.05 | 174141.05 | 174141.05 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[1815] _id=69e91b941724f0c9e2fa8fe3 ts=? == 69cdc98ad385e3b94310f7aa.jsonl[1852] _id=69e91ca91724f0c9e2fa94f1 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.95s, p95 41.59s, n=500) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `154ms: 69cdc98ad385e3b94310f7aa.jsonl[276] _id=69e681f61724f0c9e2f8f053 ts=2026-04-20T19:43:50.2100000Z ~ 69cdc98ad385e3b94310f7aa.jsonl[277] _id=69e681f71724f0c9e2f8f05b ts=2026-04-20T19:43:50.3640000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `618ms: 69cdc98ad385e3b94310f7aa.jsonl[213] _id=69e13f9f1724f0c9e2f7093f ts=2026-04-16T19:59:26.0380000Z ~ 69cdc98ad385e3b94310f7aa.jsonl[911] _id=69e13f9f1724f0c9e2f7094c ts=2026-04-16T19:59:26.6560000Z`; `675ms: 69cdc98ad385e3b94310f7aa.jsonl[1177] _id=69e13f9f1724f0c9e2f70948 ts=2026-04-16T19:59:26.5750000Z ~ 69cdc98ad385e3b94310f7aa.jsonl[1179] _id=69e13fa01724f0c9e2f70950 ts=2026-04-16T19:59:27.2500000Z`; `604ms: 69cdc98ad385e3b94310f7aa.jsonl[911] _id=69e13f9f1724f0c9e2f7094c ts=2026-04-16T19:59:26.6560000Z ~ 69cdc98ad385e3b94310f7aa.jsonl[217] _id=69e13fa01724f0c9e2f70952 ts=2026-04-16T19:59:27.2600000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc98ad385e3b94310f7aa.jsonl[1261] _id=69e141a71724f0c9e2f712a0 ts=2026-04-16T20:08:06.0520000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1282] _id=69e676481724f0c9e2f8baad ts=2026-04-20T18:54:00.5570000Z; 46h 51m: 69cdc98ad385e3b94310f7aa.jsonl[598] _id=69de9cb07957a33870f3af05 ts=2026-04-14T19:59:44.3370000Z -> 69cdc98ad385e3b94310f7aa.jsonl[642] _id=69e12fbe1724f0c9e2f68fc6 ts=2026-04-16T18:51:41.4280000Z; 46h 47m: 69cdc98ad385e3b94310f7aa.jsonl[1744] _id=69e6872d1724f0c9e2f8ff0f ts=2026-04-20T20:06:05.4700000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1766] _id=69e919251724f0c9e2fa8615 ts=2026-04-22T18:53:23.1700000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 317 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7aa.jsonl[1262] _id=69e141751724f0c9e2f711e6 ts=2026-04-16T20:07:16.1670000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1266] _id=69e141871724f0c9e2f7124c ts=2026-04-16T20:07:16.167Z; 3ms: 69cdc98ad385e3b94310f7aa.jsonl[476] _id=69de98bc7957a33870f39c8b ts=2026-04-14T19:42:51.6980000Z -> 69cdc98ad385e3b94310f7aa.jsonl[79] _id=69de98bc7957a33870f39c8d ts=2026-04-14T19:42:51.7010000Z; 3ms: 69cdc98ad385e3b94310f7aa.jsonl[934] _id=69e139971724f0c9e2f6e004 ts=2026-04-16T19:33:41.8760000Z -> 69cdc98ad385e3b94310f7aa.jsonl[936] _id=69e139971724f0c9e2f6e006 ts=2026-04-16T19:33:41.8790000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 22m 
  - Evidence: 48h 22m: 69cdc98ad385e3b94310f7aa.jsonl[495] _id=69de99377957a33870f39e8b ts=2026-04-14T19:44:55.0930000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1260] _id=69e141751724f0c9e2f711e1 ts=2026-04-16T20:07:16.1430000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc98ad385e3b94310f7aa.jsonl[1269] _id=69e141b61724f0c9e2f712ca ts=2026-04-16T20:08:21.7100000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1285] _id=69e6763e1724f0c9e2f8ba99 ts=2026-04-20T18:53:50.1210000Z; 46h 43m: 69cdc98ad385e3b94310f7aa.jsonl[1754] _id=69e687fb1724f0c9e2f902b7 ts=2026-04-20T20:09:30.7370000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1764] _id=69e919231724f0c9e2fa8607 ts=2026-04-22T18:53:21.7210000Z; 46h 42m: 69cdc98ad385e3b94310f7aa.jsonl[628] _id=69de9ed57957a33870f3b70d ts=2026-04-14T20:08:52.9550000Z -> 69cdc98ad385e3b94310f7aa.jsonl[640] _id=69e12fba1724f0c9e2f68fb2 ts=2026-04-16T18:51:36.8370000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 69cdc98ad385e3b94310f7aa.jsonl[868] _id=69e137911724f0c9e2f6be0e ts=2026-04-16T19:25:04.7660000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1651] _id=69e6831a1724f0c9e2f8f49f ts=2026-04-20T19:48:41.9560000Z; 47h 1m: 69cdc98ad385e3b94310f7aa.jsonl[563] _id=69de9bbb7957a33870f3aa0d ts=2026-04-14T19:55:39.2110000Z -> 69cdc98ad385e3b94310f7aa.jsonl[693] _id=69e131181724f0c9e2f694ae ts=2026-04-16T18:57:27.4610000Z; 25m 36s: 69cdc98ad385e3b94310f7aa.jsonl[694] _id=69e1311b1724f0c9e2f694b0 ts=2026-04-16T18:57:30.4330000Z -> 69cdc98ad385e3b94310f7aa.jsonl[148] _id=69e1371c1724f0c9e2f6b97c ts=2026-04-16T19:23:07.2150000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 12m 
  - Evidence: 95h 12m: 69cdc98ad385e3b94310f7aa.jsonl[1078] _id=69e13c6a1724f0c9e2f6fc08 ts=2026-04-16T19:45:45.7800000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1311] _id=69e6772d1724f0c9e2f8beaf ts=2026-04-20T18:57:49.1550000Z; 46h 54m: 69cdc98ad385e3b94310f7aa.jsonl[629] _id=69de9e947957a33870f3b62b ts=2026-04-14T20:07:48.6940000Z -> 69cdc98ad385e3b94310f7aa.jsonl[128] _id=69e132391724f0c9e2f69990 ts=2026-04-16T19:02:16.7630000Z; 27m 30s: 69cdc98ad385e3b94310f7aa.jsonl[790] _id=69e1345f1724f0c9e2f6a66c ts=2026-04-16T19:11:26.5760000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1022] _id=69e13ad21724f0c9e2f6f514 ts=2026-04-16T19:38:57.1460000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 48m 
  - Evidence: 95h 48m: 69cdc98ad385e3b94310f7aa.jsonl[828] _id=69e134581724f0c9e2f6a640 ts=2026-04-16T19:11:19.6740000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1315] _id=69e677ae1724f0c9e2f8c105 ts=2026-04-20T18:59:57.9710000Z; 15m 48s: 69cdc98ad385e3b94310f7aa.jsonl[1329] _id=69e6783f1724f0c9e2f8c361 ts=2026-04-20T19:02:22.9300000Z -> 69cdc98ad385e3b94310f7aa.jsonl[260] _id=69e67bf31724f0c9e2f8d43f ts=2026-04-20T19:18:10.9310000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 42m 
  - Evidence: 95h 42m: 69cdc98ad385e3b94310f7aa.jsonl[226] _id=69e140001724f0c9e2f70af8 ts=2026-04-16T20:01:03.1420000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1595] _id=69e681d91724f0c9e2f8efed ts=2026-04-20T19:43:20.8020000Z; 48h 15m: 69cdc98ad385e3b94310f7aa.jsonl[455] _id=69de98717957a33870f39b2d ts=2026-04-14T19:41:37.2560000Z -> 69cdc98ad385e3b94310f7aa.jsonl[195] _id=69e13f241724f0c9e2f7073e ts=2026-04-16T19:57:23.4080000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 42m 
  - Evidence: 95h 42m: 69cdc98ad385e3b94310f7aa.jsonl[233] _id=69e13ffe1724f0c9e2f70af2 ts=2026-04-16T20:01:01.3750000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1611] _id=69e681e41724f0c9e2f8f013 ts=2026-04-20T19:43:31.7530000Z; 48h 15m: 69cdc98ad385e3b94310f7aa.jsonl[453] _id=69de986f7957a33870f39b1d ts=2026-04-14T19:41:34.7570000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1150] _id=69e13f271724f0c9e2f70752 ts=2026-04-16T19:57:26.6030000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.010s..0.010s shown 
  - Evidence: 10ms: 69cdc98ad385e3b94310f7aa.jsonl[1179] _id=69e13fa01724f0c9e2f70950 ts=2026-04-16T19:59:27.2500000Z -> 69cdc98ad385e3b94310f7aa.jsonl[217] _id=69e13fa01724f0c9e2f70952 ts=2026-04-16T19:59:27.2600000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 49m 
  - Evidence: 94h 49m: 69cdc98ad385e3b94310f7aa.jsonl[1257] _id=69e1416e1724f0c9e2f71194 ts=2026-04-16T20:07:09.4560000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1303] _id=69e676ff1724f0c9e2f8bddb ts=2026-04-20T18:57:03.2770000Z; 47h 3m: 69cdc98ad385e3b94310f7aa.jsonl[1659] _id=69e683651724f0c9e2f8f549 ts=2026-04-20T19:49:57.5520000Z -> 69cdc98ad385e3b94310f7aa.jsonl[1765] _id=69e919241724f0c9e2fa8611 ts=2026-04-22T18:53:23.0140000Z; 46h 52m: 69cdc98ad385e3b94310f7aa.jsonl[605] _id=69de9cab7957a33870f3aef5 ts=2026-04-14T19:59:39.1320000Z -> 69cdc98ad385e3b94310f7aa.jsonl[641] _id=69e12fbd1724f0c9e2f68fc2 ts=2026-04-16T18:51:39.7690000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.003s..0.016s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7aa.jsonl[424] _id=69de97c57957a33870f397a7 ts=2026-04-14T19:38:45.1190000Z -> 69cdc98ad385e3b94310f7aa.jsonl[425] _id=69de97c57957a33870f397a9 ts=2026-04-14T19:38:45.1220000Z; 14ms: 69cdc98ad385e3b94310f7aa.jsonl[346] _id=69de94fe7957a33870f38ac1 ts=2026-04-14T19:26:54.1290000Z -> 69cdc98ad385e3b94310f7aa.jsonl[340] _id=69de94fe7957a33870f38ac3 ts=2026-04-14T19:26:54.1430000Z; 16ms: 69cdc98ad385e3b94310f7aa.jsonl[332] _id=69de943b7957a33870f3892e ts=2026-04-14T19:23:38.9500000Z -> 69cdc98ad385e3b94310f7aa.jsonl[326] _id=69de943b7957a33870f38930 ts=2026-04-14T19:23:38.9660000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc98ad385e3b94310f7aa.jsonl:69cdc98ad385e3b94310f7aa, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[563] _id=69de9bbb7957a33870f3aa0d ts=2026-04-14T19:55:39.2110000Z`; `69cdc98ad385e3b94310f7aa.jsonl[694] _id=69e1311b1724f0c9e2f694b0 ts=2026-04-16T18:57:30.4330000Z`; `69cdc98ad385e3b94310f7aa.jsonl[868] _id=69e137911724f0c9e2f6be0e ts=2026-04-16T19:25:04.7660000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 34 record(s) match the trigger in 69cdc98ad385e3b94310f7aa.jsonl:69cdc98ad385e3b94310f7aa, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[746] _id=69e132461724f0c9e2f699ee ts=2026-04-16T19:02:29.1010000Z`; `69cdc98ad385e3b94310f7aa.jsonl[747] _id=69e132491724f0c9e2f69a0e ts=2026-04-16T19:02:32.6010000Z`; `69cdc98ad385e3b94310f7aa.jsonl[771] _id=69e132e31724f0c9e2f69e3c ts=2026-04-16T19:05:06.0950000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[982] _id=69e13a491724f0c9e2f6f26a ts=2026-04-16T19:36:40.2280000Z`; `69cdc98ad385e3b94310f7aa.jsonl[1378] _id=69e679781724f0c9e2f8c97d ts=2026-04-20T19:07:36.0460000Z`; `69cdc98ad385e3b94310f7aa.jsonl[1406] _id=69e67a261724f0c9e2f8cc9d ts=2026-04-20T19:10:29.5790000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[277] _id=69e681f71724f0c9e2f8f05b ts=2026-04-20T19:43:50.3640000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[1815] _id=69e91b941724f0c9e2fa8fe3 ts=?`; `69cdc98ad385e3b94310f7aa.jsonl[1852] _id=69e91ca91724f0c9e2fa94f1 ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7aa.jsonl[1184] _id=69e13fc21724f0c9e2f709fe ts=2026-04-16T20:00:00.6210000Z`; `69cdc98ad385e3b94310f7aa.jsonl[1191] _id=69e13fe51724f0c9e2f70a90 ts=2026-04-16T20:00:36.3200000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 161 unmatched 'DialogueStartEvent' (totals: 262 start, 104 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 14 open, 12 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 5 unmatched 'questActiveEvent' (totals: 20 start, 15 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.95s, min -19.04s, max -0.24s over 1935 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7aa\coverage.yaml

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
  - Observed: 66 records 
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

### `DialogueEvent` — 1222 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (617); Unit 3 Dev (246); Unit 1 Dev (188); Unit 3 Dungeon Dev (171)
- **eventKey:** present on 856 of 1222 records
- **Intervals:** median 2.55s (p5 0.01s / p95 44.57s, n=1221)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x856; [conversationId, dialogueEventType] x366
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1222/1222 records)
    numeric range 8 .. 103 (32 unique)
data.dialogueEventType  (string, 1222/1222 records)
    "DialogueNodeEvent"  x856
    "DialogueStartEvent"  x262
    "DialogueFinishEvent"  x104
data.nodeId  (number, 856/1222 records)
    numeric range 0 .. 290 (215 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 504 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (193); Unit 3 Dungeon Dev (158); Unit 3 Dev (100); Unit 1 Dev (53)
- **Intervals:** median 30.01s (p5 29.95s / p95 41.59s, n=500)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 504/504 records)
data.position.x  (number, 504/504 records)
    numeric range -708.323 .. 1426.77 (255 unique)
data.position.y  (number, 504/504 records)
    numeric range -115.127 .. 157.095 (177 unique)
data.position.z  (number, 504/504 records)
    numeric range -1107.67 .. 2015.61 (256 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 66 records

- **Scenes:** Unit 3 Dev (42); Unit 2 Prod (Refactor) (24)
- **Intervals:** median 18.66s (p5 0.97s / p95 676.71s, n=65)
- **Fields under `data`:**

```text
data.actionType  (string, 66/66 records)
    "MapCloseEvent"  x33
    "MapOpenEvent"  x33
data.featureUsed  (string, 66/66 records)
    "Map"  x66
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 35 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (12); Unit 3 Dev (5); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 35 of 35 records
- **Intervals:** median 190.74s (p5 0.02s / p95 168960.33s, n=34)
- **`data` key-set variants:** [questEventType, questID, questName] x20; [questEventType, questID, questName, questSuccessOrFailure] x15
- **Fields under `data`:**

```text
data.questEventType  (string, 35/35 records)
    "questActiveEvent"  x20
    "questFinishEvent"  x15
data.questID  (string, 35/35 records)
    15 unique values (see csv/event_unique_values.csv)
data.questName  (string, 35/35 records)
    15 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 15/35 records)
    "Succeeded"  x15
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 34 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 5.17s (p5 2.30s / p95 566.42s, n=33)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "dragEnd"  x17
    "dragStart"  x17
data.featureUsed  (string, 34/34 records)
    "waypoint"  x34
data.location  (object, 34/34 records)
data.location.x  (number, 34/34 records)
    numeric range -779.225 .. 431.26 (18 unique)
data.location.y  (number, 34/34 records)
    numeric range -324.271 .. 374.465 (17 unique)
data.location.z  (number, 34/34 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 29 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 1 Dev (5); Unit 3 Dev (3)
- **Intervals:** median 8.27s (p5 1.35s / p95 112960.68s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "argumentationNodeAdd"  x20
    "argumentationNodeRemove"  x9
data.argumentationTitle  (string, 29/29 records)
    "Unit 2 – Watershed"  x21
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 29/29 records)
    "A"  x7
    "1"  x5
    "C"  x4
    "D"  x4
    "I"  x4
    "B"  x3
    "5"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 26 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (26)
- **Intervals:** median 0.60s (p5 0.08s / p95 12.36s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "argumentationToolOpen"  x14
    "argumentationToolClose"  x12
data.argumentationTitle  (string, 26/26 records)
    "Unit 2 – Watershed"  x26
data.toolName  (string, 26/26 records)
    "BackingInfoPanel - Waterfall Data"  x15
    "BackingInfoPanel - Watershed Graph"  x11
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 39.23s (p5 9.31s / p95 284760.63s, n=8)
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

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2)
- **Intervals:** median 117.55s (p5 2.99s / p95 293704.51s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 174141.05s (p5 174141.05s / p95 174141.05s, n=1)
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
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Uncaught ReferenceError: onResize is not defined"  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x2
data.type  (string, 2/2 records)
    "runtime_error"  x2
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
- `crash` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (9x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*