# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f730

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f730
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f730.jsonl
- **Records:** 3077 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f730
- **Time span:** 2026-04-13T17:56:21.995000+00:00 .. 2026-04-23T18:40:21.712000+00:00 (240h 43m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f730\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 3077 records, 6 scenes.
- Findings: **0 FAIL**, **45 WARNING**, 52 INFO, 2 NOT_TESTED, 34 PASS.
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
| DialogueEvent | 2004 | 65.13 | 1 | 6 | 1375 | 2026-04-13T17:56:40.270000+00:00 | 2026-04-23T18:40:13.030000+00:00 | 240h 43m |
| PlayerPositionEvent | 805 | 26.16 | 1 | 6 | 0 | 2026-04-13T17:56:21.995000+00:00 | 2026-04-23T18:40:21.712000+00:00 | 240h 43m |
| argumentationNodeEvent | 75 | 2.44 | 1 | 3 | 0 | 2026-04-13T18:21:00.141000+00:00 | 2026-04-21T17:37:57.720000+00:00 | 191h 16m |
| questEvent | 65 | 2.11 | 1 | 6 | 65 | 2026-04-13T17:56:40.254000+00:00 | 2026-04-23T18:39:01.092000+00:00 | 240h 42m |
| TopographicMapEvent | 44 | 1.43 | 1 | 2 | 0 | 2026-04-15T18:28:08.177000+00:00 | 2026-04-23T18:23:28.334000+00:00 | 191h 55m |
| Topographic Map Event | 40 | 1.3 | 1 | 3 | 0 | 2026-04-15T17:50:05.649000+00:00 | 2026-04-23T18:23:31.454000+00:00 | 192h 33m |
| argumentationToolEvent | 24 | 0.78 | 1 | 2 | 0 | 2026-04-17T22:59:33.950000+00:00 | 2026-04-21T17:36:54.464000+00:00 | 90h 37m |
| argumentationEvent | 9 | 0.29 | 1 | 3 | 0 | 2026-04-13T18:20:49.393000+00:00 | 2026-04-21T17:38:03.775000+00:00 | 191h 17m |
| Soil Key Puzzle | 8 | 0.26 | 1 | 3 | 0 | 2026-04-15T18:20:38.257000+00:00 | 2026-04-23T18:36:12.014000+00:00 | 192h 15m |
| EndOfUnit | 2 | 0.06 | 1 | 2 | 0 | 2026-04-17T23:06:05.385000+00:00 | 2026-04-23T18:29:30.491000+00:00 | 139h 23m |
| crash | 1 | 0.03 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 501805.106s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.004s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 103.46s median 
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
  - Observed: 8.282s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 179.89s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.032s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.911s median 
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
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 40 records this build 
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
  - Observed: 2 
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 47; 48; 49; 50; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f730.jsonl[1343] _id=69dd34da7957a33870f276fe ts=2026-04-13T18:24:25.5140000Z`; `69cdc907d385e3b94310f730.jsonl[1710] _id=69e266221724f0c9e2f72200 ts=2026-04-17T16:56:01.2470000Z`; `69cdc907d385e3b94310f730.jsonl[233] _id=69e270ff1724f0c9e2f7433a ts=2026-04-17T17:42:22.3320000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 44 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2003 | 0.002 | 2.623 | 432.657 | 40.737 | 170902.309 | 0.14 | 555 | 10 |
| PlayerPositionEvent | 798 | 15.066 | 30.004 | 1085.579 | 34.494 | 170441.19 | 0.06 | 0 | 7 |
| argumentationNodeEvent | 74 | 0.849 | 4.032 | 9305.643 | 89.291 | 362082.741 | 0.01 | 0 | 3 |
| questEvent | 64 | 0.002 | 225.831 | 13539.701 | 149190.236 | 170981.203 | 0.0 | 3 | 15 |
| TopographicMapEvent | 43 | 0.275 | 8.282 | 16067.911 | 149771.404 | 335395.148 | 0.0 | 0 | 7 |
| Topographic Map Event | 39 | 1.155 | 24.04 | 17774.508 | 168615.273 | 335386.995 | 0.0 | 0 | 7 |
| argumentationToolEvent | 23 | 0.041 | 0.911 | 14184.37 | 127.331 | 326072.763 | 0.0 | 5 | 1 |
| argumentationEvent | 8 | 0.099 | 179.89 | 86079.298 | 348798.605 | 362066.557 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 7 | 2.976 | 103.46 | 98876.251 | 294241.066 | 345051.786 | 0.0 | 0 | 3 |
| EndOfUnit | 1 | 501805.106 | 501805.106 | 501805.106 | 501805.106 | 501805.106 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.004s (p5 29.97s, p95 34.49s, n=798) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `99ms: 69cdc907d385e3b94310f730.jsonl[978] _id=69e7b5fb1724f0c9e2f93d2d ts=2026-04-21T17:38:03.6760000Z ~ 69cdc907d385e3b94310f730.jsonl[972] _id=69e7b5fc1724f0c9e2f93d37 ts=2026-04-21T17:38:03.7750000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `849ms: 69cdc907d385e3b94310f730.jsonl[583] _id=69e2bbe51724f0c9e2f7ec02 ts=2026-04-17T23:01:56.8240000Z ~ 69cdc907d385e3b94310f730.jsonl[585] _id=69e2bbe61724f0c9e2f7ec0a ts=2026-04-17T23:01:57.6730000Z`; `970ms: 69cdc907d385e3b94310f730.jsonl[584] _id=69e2bbe61724f0c9e2f7ec06 ts=2026-04-17T23:01:57.6320000Z ~ 69cdc907d385e3b94310f730.jsonl[586] _id=69e2bbe71724f0c9e2f7ec12 ts=2026-04-17T23:01:58.6020000Z`; `980ms: 69cdc907d385e3b94310f730.jsonl[593] _id=69e2bbec1724f0c9e2f7ec2e ts=2026-04-17T23:02:03.2390000Z ~ 69cdc907d385e3b94310f730.jsonl[597] _id=69e2bbed1724f0c9e2f7ec36 ts=2026-04-17T23:02:04.2190000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 47h 28m 
  - Evidence: 47h 28m: 69cdc907d385e3b94310f730.jsonl[1381] _id=69dd36117957a33870f27f7a ts=2026-04-13T18:29:36.9220000Z -> 69cdc907d385e3b94310f730.jsonl[1426] _id=69dfd1a77957a33870f41eb5 ts=2026-04-15T17:57:59.2310000Z; 47h 21m: 69cdc907d385e3b94310f730.jsonl[2779] _id=69e7c46c1724f0c9e2f9a6af ts=2026-04-21T18:39:40.1680000Z -> 69cdc907d385e3b94310f730.jsonl[1082] _id=69ea5e4b1724f0c9e2fb04f9 ts=2026-04-23T18:00:41.2650000Z; 46h 13m: 69cdc907d385e3b94310f730.jsonl[1681] _id=69dfdbaa7957a33870f46621 ts=2026-04-15T18:40:41.9890000Z -> 69cdc907d385e3b94310f730.jsonl[1686] _id=69e265bc1724f0c9e2f71f62 ts=2026-04-17T16:54:19.9540000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 555 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f730.jsonl[1361] _id=69dd352a7957a33870f2792a ts=2026-04-13T18:25:46.0320000Z -> 69cdc907d385e3b94310f730.jsonl[1365] _id=69dd352a7957a33870f2792c ts=2026-04-13T18:25:46.0340000Z; 2ms: 69cdc907d385e3b94310f730.jsonl[1580] _id=69dfd8607957a33870f44a45 ts=2026-04-15T18:26:39.7140000Z -> 69cdc907d385e3b94310f730.jsonl[1581] _id=69dfd8607957a33870f44a47 ts=2026-04-15T18:26:39.7160000Z; 2ms: 69cdc907d385e3b94310f730.jsonl[190] _id=69e267cb1724f0c9e2f72e88 ts=2026-04-17T17:03:06.6650000Z -> 69cdc907d385e3b94310f730.jsonl[195] _id=69e267cb1724f0c9e2f72e90 ts=2026-04-17T17:03:06.6670000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 139h 23m 
  - Evidence: 139h 23m: 69cdc907d385e3b94310f730.jsonl[647] _id=69e2bcde1724f0c9e2f7eea4 ts=2026-04-17T23:06:05.3850000Z -> 69cdc907d385e3b94310f730.jsonl[3020] _id=69ea650b1724f0c9e2fb3a71 ts=2026-04-23T18:29:30.4910000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 47h 20m 
  - Evidence: 47h 20m: 69cdc907d385e3b94310f730.jsonl[2780] _id=69e7c47d1724f0c9e2f9a701 ts=2026-04-21T18:39:57.8750000Z -> 69cdc907d385e3b94310f730.jsonl[2784] _id=69ea5e481724f0c9e2fb04e3 ts=2026-04-23T18:00:39.0650000Z; 47h 3m: 69cdc907d385e3b94310f730.jsonl[1404] _id=69dd38bb7957a33870f29194 ts=2026-04-13T18:40:58.9990000Z -> 69cdc907d385e3b94310f730.jsonl[1407] _id=69dfce907957a33870f40b5f ts=2026-04-15T17:44:48.3150000Z; 46h 13m: 69cdc907d385e3b94310f730.jsonl[1682] _id=69dfdbb17957a33870f46675 ts=2026-04-15T18:40:49.7810000Z -> 69cdc907d385e3b94310f730.jsonl[1685] _id=69e265b91724f0c9e2f71f58 ts=2026-04-17T16:54:15.8750000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 69cdc907d385e3b94310f730.jsonl[253] _id=69e2742b1724f0c9e2f758ea ts=2026-04-17T17:55:54.6660000Z -> 69cdc907d385e3b94310f730.jsonl[2482] _id=69e7b8061724f0c9e2f94b8c ts=2026-04-21T17:46:46.4520000Z; 48h 48m: 69cdc907d385e3b94310f730.jsonl[2478] _id=69e7b8301724f0c9e2f94cd1 ts=2026-04-21T17:47:28.8110000Z -> 69cdc907d385e3b94310f730.jsonl[3039] _id=69ea66741724f0c9e2fb4555 ts=2026-04-23T18:35:31.5290000Z; 47h 33m: 69cdc907d385e3b94310f730.jsonl[1534] _id=69dfd6f97957a33870f440a1 ts=2026-04-15T18:20:41.2330000Z -> 69cdc907d385e3b94310f730.jsonl[250] _id=69e273c41724f0c9e2f75616 ts=2026-04-17T17:54:11.2060000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 93h 9m 
  - Evidence: 93h 9m: 69cdc907d385e3b94310f730.jsonl[916] _id=69e542e01724f0c9e2f84a25 ts=2026-04-19T21:02:24.3230000Z -> 69cdc907d385e3b94310f730.jsonl[2884] _id=69ea60fc1724f0c9e2fb19b1 ts=2026-04-23T18:12:11.3180000Z; 50h 46m: 69cdc907d385e3b94310f730.jsonl[2100] _id=69e278eb1724f0c9e2f77302 ts=2026-04-17T18:16:10.8440000Z -> 69cdc907d385e3b94310f730.jsonl[870] _id=69e542d51724f0c9e2f84a1f ts=2026-04-19T21:02:12.7990000Z; 46h 24m: 69cdc907d385e3b94310f730.jsonl[1667] _id=69dfdb687957a33870f4643b ts=2026-04-15T18:39:36.4980000Z -> 69cdc907d385e3b94310f730.jsonl[1754] _id=69e267ec1724f0c9e2f72fdc ts=2026-04-17T17:03:39.9170000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 93h 9m 
  - Evidence: 93h 9m: 69cdc907d385e3b94310f730.jsonl[923] _id=69e542da1724f0c9e2f84a23 ts=2026-04-19T21:02:18.4350000Z -> 69cdc907d385e3b94310f730.jsonl[2842] _id=69ea60fe1724f0c9e2fb19c9 ts=2026-04-23T18:12:13.5830000Z; 46h 24m: 69cdc907d385e3b94310f730.jsonl[1673] _id=69dfdb687957a33870f46431 ts=2026-04-15T18:39:36.4460000Z -> 69cdc907d385e3b94310f730.jsonl[201] _id=69e267f21724f0c9e2f73012 ts=2026-04-17T17:03:45.7700000Z; 45h 40m: 69cdc907d385e3b94310f730.jsonl[710] _id=69e2be681724f0c9e2f7f29c ts=2026-04-17T23:12:39.8050000Z -> 69cdc907d385e3b94310f730.jsonl[848] _id=69e540bc1724f0c9e2f849a5 ts=2026-04-19T20:53:15.8100000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 100h 34m 
  - Evidence: 100h 34m: 69cdc907d385e3b94310f730.jsonl[1345] _id=69dd34d97957a33870f276fc ts=2026-04-13T18:24:25.4950000Z -> 69cdc907d385e3b94310f730.jsonl[481] _id=69e2bb2d1724f0c9e2f7e908 ts=2026-04-17T22:58:52.0520000Z; 90h 2m: 69cdc907d385e3b94310f730.jsonl[599] _id=69e2bc0a1724f0c9e2f7ecd8 ts=2026-04-17T23:02:34.0050000Z -> 69cdc907d385e3b94310f730.jsonl[2333] _id=69e7ae481724f0c9e2f92465 ts=2026-04-21T17:05:12.1280000Z; 32m 51s: 69cdc907d385e3b94310f730.jsonl[2333] _id=69e7ae481724f0c9e2f92465 ts=2026-04-21T17:05:12.1280000Z -> 69cdc907d385e3b94310f730.jsonl[978] _id=69e7b5fb1724f0c9e2f93d2d ts=2026-04-21T17:38:03.6760000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 100h 34m 
  - Evidence: 100h 34m: 69cdc907d385e3b94310f730.jsonl[49] _id=69dd34d17957a33870f276b0 ts=2026-04-13T18:24:17.2350000Z -> 69cdc907d385e3b94310f730.jsonl[472] _id=69e2bb341724f0c9e2f7e910 ts=2026-04-17T22:58:59.9760000Z; 90h 2m: 69cdc907d385e3b94310f730.jsonl[609] _id=69e2bc091724f0c9e2f7ecba ts=2026-04-17T23:02:32.1120000Z -> 69cdc907d385e3b94310f730.jsonl[2334] _id=69e7ae551724f0c9e2f924c7 ts=2026-04-21T17:05:25.0300000Z; 29m 46s: 69cdc907d385e3b94310f730.jsonl[2336] _id=69e7ae661724f0c9e2f9252d ts=2026-04-21T17:05:42.3510000Z -> 69cdc907d385e3b94310f730.jsonl[2398] _id=69e7b5601724f0c9e2f9360d ts=2026-04-21T17:35:28.5200000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 90h 34m 
  - Evidence: 90h 34m: 69cdc907d385e3b94310f730.jsonl[598] _id=69e2bbee1724f0c9e2f7ec3e ts=2026-04-17T23:02:05.3720000Z -> 69cdc907d385e3b94310f730.jsonl[2419] _id=69e7b5a61724f0c9e2f93943 ts=2026-04-21T17:36:38.1350000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.041s..0.044s shown 
  - Evidence: 41ms: 69cdc907d385e3b94310f730.jsonl[584] _id=69e2bbe61724f0c9e2f7ec06 ts=2026-04-17T23:01:57.6320000Z -> 69cdc907d385e3b94310f730.jsonl[585] _id=69e2bbe61724f0c9e2f7ec0a ts=2026-04-17T23:01:57.6730000Z; 41ms: 69cdc907d385e3b94310f730.jsonl[594] _id=69e2bbea1724f0c9e2f7ec1a ts=2026-04-17T23:02:01.3790000Z -> 69cdc907d385e3b94310f730.jsonl[595] _id=69e2bbea1724f0c9e2f7ec1c ts=2026-04-17T23:02:01.4200000Z; 44ms: 69cdc907d385e3b94310f730.jsonl[586] _id=69e2bbe71724f0c9e2f7ec12 ts=2026-04-17T23:01:58.6020000Z -> 69cdc907d385e3b94310f730.jsonl[587] _id=69e2bbe71724f0c9e2f7ec14 ts=2026-04-17T23:01:58.6460000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 47h 29m 
  - Evidence: 47h 29m: 69cdc907d385e3b94310f730.jsonl[1379] _id=69dd360a7957a33870f27f3c ts=2026-04-13T18:29:29.7150000Z -> 69cdc907d385e3b94310f730.jsonl[1434] _id=69dfd1ee7957a33870f420d5 ts=2026-04-15T17:59:10.9180000Z; 47h 21m: 69cdc907d385e3b94310f730.jsonl[2778] _id=69e7c4601724f0c9e2f9a66b ts=2026-04-21T18:39:27.6250000Z -> 69cdc907d385e3b94310f730.jsonl[2782] _id=69ea5e4b1724f0c9e2fb04f3 ts=2026-04-23T18:00:40.7930000Z; 46h 15m: 69cdc907d385e3b94310f730.jsonl[1668] _id=69dfdb567957a33870f4639f ts=2026-04-15T18:39:18.4490000Z -> 69cdc907d385e3b94310f730.jsonl[1684] _id=69e265bb1724f0c9e2f71f60 ts=2026-04-17T16:54:18.4940000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.010s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f730.jsonl[1292] _id=69dd33c07957a33870f27040 ts=2026-04-13T18:19:44.2840000Z -> 69cdc907d385e3b94310f730.jsonl[40] _id=69dd33c17957a33870f2704c ts=2026-04-13T18:19:44.2860000Z; 10ms: 69cdc907d385e3b94310f730.jsonl[1225] _id=69dd30fc7957a33870f25c70 ts=2026-04-13T18:07:55.5860000Z -> 69cdc907d385e3b94310f730.jsonl[1222] _id=69dd30fc7957a33870f25c72 ts=2026-04-13T18:07:55.5960000Z; 10ms: 69cdc907d385e3b94310f730.jsonl[16] _id=69dd30087957a33870f2566c ts=2026-04-13T18:03:51.8840000Z -> 69cdc907d385e3b94310f730.jsonl[17] _id=69dd30087957a33870f2566f ts=2026-04-13T18:03:51.8940000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f730.jsonl:69cdc907d385e3b94310f730, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f730.jsonl[1534] _id=69dfd6f97957a33870f440a1 ts=2026-04-15T18:20:41.2330000Z`; `69cdc907d385e3b94310f730.jsonl[253] _id=69e2742b1724f0c9e2f758ea ts=2026-04-17T17:55:54.6660000Z`; `69cdc907d385e3b94310f730.jsonl[2478] _id=69e7b8301724f0c9e2f94cd1 ts=2026-04-21T17:47:28.8110000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 44 record(s) match the trigger in 69cdc907d385e3b94310f730.jsonl:69cdc907d385e3b94310f730, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f730.jsonl[100] _id=69dfd8b87957a33870f44d73 ts=2026-04-15T18:28:08.1770000Z`; `69cdc907d385e3b94310f730.jsonl[1598] _id=69dfd8bc7957a33870f44da9 ts=2026-04-15T18:28:12.1920000Z`; `69cdc907d385e3b94310f730.jsonl[1672] _id=69dfdb607957a33870f463f9 ts=2026-04-15T18:39:28.1640000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f730.jsonl[2018] _id=69e277511724f0c9e2f76b2a ts=2026-04-17T18:09:21.0110000Z`; `69cdc907d385e3b94310f730.jsonl[739] _id=69e2bf4c1724f0c9e2f7f79a ts=2026-04-17T23:16:28.0250000Z`; `69cdc907d385e3b94310f730.jsonl[743] _id=69e2c0431724f0c9e2f7f80c ts=2026-04-17T23:20:33.3440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f730.jsonl[972] _id=69e7b5fc1724f0c9e2f93d37 ts=2026-04-21T17:38:03.7750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f730.jsonl[2429] _id=69e7b5b31724f0c9e2f939cb ts=2026-04-21T17:36:51.8170000Z`; `69cdc907d385e3b94310f730.jsonl[2433] _id=69e7b5b51724f0c9e2f939ed ts=2026-04-21T17:36:53.3350000Z`; `69cdc907d385e3b94310f730.jsonl[2434] _id=69e7b5b61724f0c9e2f939fb ts=2026-04-21T17:36:54.4640000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc907d385e3b94310f730.jsonl[2896] _id=69ea618b1724f0c9e2fb1e75 ts=2026-04-23T18:14:34.5470000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc907d385e3b94310f730.jsonl[2498] _id=69e7b8d41724f0c9e2f9510d ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f730.jsonl[2432] _id=69e7b5b41724f0c9e2f939cd ts=2026-04-21T17:36:51.8720000Z`; `69cdc907d385e3b94310f730.jsonl[2430] _id=69e7b5b51724f0c9e2f939f2 ts=2026-04-21T17:36:53.4000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 226 unmatched 'DialogueStartEvent' (totals: 426 start, 203 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 12 open, 12 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 40 start, 25 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.58s, min -6.58s, max +0.04s over 3076 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f730\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
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
  - Evidence: coverage: Unit1=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
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
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `DialogueEvent` — 2004 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (987); Unit 3 Dev (429); Unit 3 Dungeon Dev (340); Unit 1 Dev (202); Unit 4 Dev (25); Unit 4 Dev - Dungeon (21)
- **eventKey:** present on 1375 of 2004 records
- **Intervals:** median 2.62s (p5 0.01s / p95 40.74s, n=2003)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1375; [conversationId, dialogueEventType] x629
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2004/2004 records)
    numeric range 8 .. 104 (38 unique)
data.dialogueEventType  (string, 2004/2004 records)
    "DialogueNodeEvent"  x1375
    "DialogueStartEvent"  x426
    "DialogueFinishEvent"  x203
data.nodeId  (number, 1375/2004 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 805 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (328); Unit 3 Dev (229); Unit 3 Dungeon Dev (120); Unit 1 Dev (106); Unit 4 Dev (17); Unit 4 Dev - Dungeon (5)
- **Intervals:** median 30.00s (p5 29.97s / p95 34.49s, n=798)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 805/805 records)
data.position.x  (number, 805/805 records)
    numeric range -692.71 .. 1428.98 (352 unique)
data.position.y  (number, 805/805 records)
    numeric range -115.127 .. 177.436 (252 unique)
data.position.z  (number, 805/805 records)
    numeric range -1188.32 .. 2188.76 (351 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 75 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (43); Unit 3 Dev (23); Unit 1 Dev (9)
- **Intervals:** median 4.03s (p5 1.03s / p95 89.29s, n=74)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 75/75 records)
    "argumentationNodeAdd"  x43
    "argumentationNodeRemove"  x32
data.argumentationTitle  (string, 75/75 records)
    "Unit 2 – Watershed"  x43
    "Unit 3 - Pollution Upstream"  x23
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x4
data.nodeName  (string, 75/75 records)
    "I"  x14
    "B"  x13
    "A"  x11
    "II"  x9
    "C"  x8
    "1"  x7
    "D"  x6
    "5"  x3
    "3"  x2
    "4"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 65 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (19); Unit 1 Dev (12); Unit 3 Dungeon Dev (8); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **eventKey:** present on 65 of 65 records
- **Intervals:** median 225.83s (p5 3.99s / p95 149190.24s, n=64)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x25
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 65/65 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x25
data.questID  (string, 65/65 records)
    19 unique values (see csv/event_unique_values.csv)
data.questName  (string, 65/65 records)
    19 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 25/65 records)
    "Succeeded"  x25
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 44 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (30); Unit 2 Prod (Refactor) (14)
- **Intervals:** median 8.28s (p5 0.70s / p95 149771.40s, n=43)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "dragEnd"  x22
    "dragStart"  x22
data.featureUsed  (string, 44/44 records)
    "waypoint"  x44
data.location  (object, 44/44 records)
data.location.x  (number, 44/44 records)
    numeric range -798.039 .. 137.514 (23 unique)
data.location.y  (number, 44/44 records)
    numeric range -323.749 .. 193.984 (23 unique)
data.location.z  (number, 44/44 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (12); Unit 1 Dev (4)
- **Intervals:** median 24.04s (p5 4.98s / p95 168615.27s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationToolEvent` — 24 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 3 Dev (8)
- **Intervals:** median 0.91s (p5 0.04s / p95 127.33s, n=23)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "argumentationToolClose"  x12
    "argumentationToolOpen"  x12
data.argumentationTitle  (string, 24/24 records)
    "Unit 2 – Watershed"  x16
    "Unit 3 - Pollution Upstream"  x8
data.toolName  (string, 24/24 records)
    "BackingInfoPanel - Waterfall Data"  x8
    "BackingInfoPanel - Watershed Graph"  x8
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Pollution Site Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 179.89s (p5 7.54s / p95 348798.61s, n=8)
- **Open findings:** 2 — see sections 5-8
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
- **Intervals:** median 103.46s (p5 14.23s / p95 294241.07s, n=7)
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

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 501805.11s (p5 501805.11s / p95 501805.11s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
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
    "A user gesture is required to request Pointer Lock."  x1
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
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TopographicMapEvent` data.actionType: "dragStart" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (32x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*