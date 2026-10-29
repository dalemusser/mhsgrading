# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f724

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f724
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f724.jsonl
- **Records:** 1588 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f724
- **Time span:** 2026-04-13T18:00:56.418000+00:00 .. 2026-04-23T18:41:52.886000+00:00 (240h 40m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f724\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **9 event types**, 1588 records, 3 scenes.
- Findings: **0 FAIL**, **40 WARNING**, 42 INFO, 5 NOT_TESTED, 28 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 958 | 60.33 | 1 | 3 | 704 | 2026-04-13T18:01:19.915000+00:00 | 2026-04-23T18:40:33.523000+00:00 | 240h 39m |
| PlayerPositionEvent | 464 | 29.22 | 1 | 3 | 0 | 2026-04-13T18:00:56.418000+00:00 | 2026-04-23T18:41:45.244000+00:00 | 240h 40m |
| argumentationNodeEvent | 62 | 3.9 | 1 | 2 | 0 | 2026-04-13T18:34:46.835000+00:00 | 2026-04-23T18:36:45.523000+00:00 | 240h 1m |
| questEvent | 47 | 2.96 | 1 | 3 | 47 | 2026-04-13T18:01:19.868000+00:00 | 2026-04-23T18:38:16.879000+00:00 | 240h 36m |
| Topographic Map Event | 22 | 1.39 | 1 | 2 | 0 | 2026-04-15T18:40:44.566000+00:00 | 2026-04-23T18:14:11.972000+00:00 | 191h 33m |
| argumentationEvent | 15 | 0.94 | 1 | 2 | 0 | 2026-04-13T18:34:32.740000+00:00 | 2026-04-23T18:36:47.232000+00:00 | 240h 2m |
| argumentationToolEvent | 12 | 0.76 | 1 | 1 | 0 | 2026-04-23T18:30:27.822000+00:00 | 2026-04-23T18:35:17.590000+00:00 | 4m 49s |
| Soil Key Puzzle | 6 | 0.38 | 1 | 2 | 0 | 2026-04-15T18:12:53.427000+00:00 | 2026-04-23T18:41:52.886000+00:00 | 192h 28m |
| EndOfUnit | 2 | 0.13 | 1 | 1 | 0 | 2026-04-15T17:58:15.690000+00:00 | 2026-04-17T18:21:37.361000+00:00 | 48h 23m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 174201.671s median 
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
  - Observed: 239.545s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 83 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.649s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.576s median 
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
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 22 records this build 
  - Expected: new logging or newly exercised content — review
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
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 22; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Getting the Band Back Together; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 13 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f724.jsonl[553] _id=69dd382a7957a33870f28dca ts=2026-04-13T18:38:33.9500000Z`; `69cdc907d385e3b94310f724.jsonl[58] _id=69dfd0ca7957a33870f4181d ts=2026-04-15T17:54:17.6120000Z`; `69cdc907d385e3b94310f724.jsonl[1063] _id=69e274951724f0c9e2f75b64 ts=2026-04-17T17:57:40.8130000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:23' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc907d385e3b94310f724.jsonl[3] _id=69e777fa1724f0c9e2f913e9 ts=2026-04-21T13:13:28.7640000Z`; `69cdc907d385e3b94310f724.jsonl[194] _id=69e77f9b1724f0c9e2f913f7 ts=2026-04-21T13:46:01.1830000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 957 | 0.003 | 3.116 | 905.281 | 56.518 | 326356.14 | 0.07 | 215 | 9 |
| PlayerPositionEvent | 459 | 24.664 | 30.004 | 1494.571 | 48.531 | 326011.096 | 0.04 | 0 | 10 |
| argumentationNodeEvent | 61 | 0.742 | 4.649 | 14165.88 | 141.396 | 519091.692 | 0.0 | 0 | 3 |
| questEvent | 46 | 0.002 | 158.415 | 18830.805 | 169194.692 | 327005.426 | 0.0 | 9 | 12 |
| Topographic Map Event | 21 | 2.196 | 35.425 | 32838.448 | 166702.767 | 521994.96 | 0.0 | 0 | 2 |
| argumentationEvent | 14 | 0.104 | 52.534 | 61723.892 | 294908.001 | 519072.963 | 0.0 | 0 | 3 |
| argumentationToolEvent | 11 | 0.007 | 2.576 | 26.343 | 135.252 | 252.82 | 2.28 | 1 | 0 |
| Soil Key Puzzle | 5 | 2.993 | 239.545 | 138587.892 | 451589.547 | 521768.024 | 0.0 | 0 | 2 |
| EndOfUnit | 1 | 174201.671 | 174201.671 | 174201.671 | 174201.671 | 174201.671 | 0.0 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.004s (p5 29.96s, p95 48.53s, n=459) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `104ms: 69cdc907d385e3b94310f724.jsonl[1549] _id=69ea66bf1724f0c9e2fb4797 ts=2026-04-23T18:36:47.1280000Z ~ 69cdc907d385e3b94310f724.jsonl[299] _id=69ea66bf1724f0c9e2fb479d ts=2026-04-23T18:36:47.2320000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 69cdc907d385e3b94310f724.jsonl[3] _id=69e777fa1724f0c9e2f913e9 ts=2026-04-21T13:13:28.7640000Z ~ 69cdc907d385e3b94310f724.jsonl[165] _id=69e777fa1724f0c9e2f913eb ts=2026-04-21T13:13:28.7680000Z`; `6ms: 69cdc907d385e3b94310f724.jsonl[194] _id=69e77f9b1724f0c9e2f913f7 ts=2026-04-21T13:46:01.1830000Z ~ 69cdc907d385e3b94310f724.jsonl[195] _id=69e77f9c1724f0c9e2f913f9 ts=2026-04-21T13:46:01.1890000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 90h 39m 
  - Evidence: 90h 39m: 69cdc907d385e3b94310f724.jsonl[1265] _id=69e27d261724f0c9e2f7848e ts=2026-04-17T18:34:13.9430000Z -> 69cdc907d385e3b94310f724.jsonl[166] _id=69e777fb1724f0c9e2f913ed ts=2026-04-21T13:13:30.0830000Z; 50h 2m: 69cdc907d385e3b94310f724.jsonl[1284] _id=69e79e9e1724f0c9e2f91465 ts=2026-04-21T15:58:20.8480000Z -> 69cdc907d385e3b94310f724.jsonl[1288] _id=69ea5e491724f0c9e2fb04e5 ts=2026-04-23T18:00:41.4720000Z; 47h 10m: 69cdc907d385e3b94310f724.jsonl[52] _id=69dd38cd7957a33870f291f0 ts=2026-04-13T18:41:17.2620000Z -> 69cdc907d385e3b94310f724.jsonl[598] _id=69dfd02b7957a33870f4135d ts=2026-04-15T17:51:39.4060000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 215 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f724.jsonl[571] _id=69dd38967957a33870f290f0 ts=2026-04-13T18:40:22.1740000Z -> 69cdc907d385e3b94310f724.jsonl[576] _id=69dd38967957a33870f290f2 ts=2026-04-13T18:40:22.1770000Z; 3ms: 69cdc907d385e3b94310f724.jsonl[657] _id=69dfd1107957a33870f41a4b ts=2026-04-15T17:55:27.7440000Z -> 69cdc907d385e3b94310f724.jsonl[661] _id=69dfd1107957a33870f41a4f ts=2026-04-15T17:55:27.7470000Z; 3ms: 69cdc907d385e3b94310f724.jsonl[668] _id=69dfd1307957a33870f41b69 ts=2026-04-15T17:56:00.2570000Z -> 69cdc907d385e3b94310f724.jsonl[669] _id=69dfd1307957a33870f41b6d ts=2026-04-15T17:56:00.2600000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 23m 
  - Evidence: 48h 23m: 69cdc907d385e3b94310f724.jsonl[688] _id=69dfd1b87957a33870f41f25 ts=2026-04-15T17:58:15.6900000Z -> 69cdc907d385e3b94310f724.jsonl[1219] _id=69e27a311724f0c9e2f77a04 ts=2026-04-17T18:21:37.3610000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 90h 33m 
  - Evidence: 90h 33m: 69cdc907d385e3b94310f724.jsonl[1279] _id=69e27e7c1724f0c9e2f78cd4 ts=2026-04-17T18:39:55.2990000Z -> 69cdc907d385e3b94310f724.jsonl[164] _id=69e777f81724f0c9e2f913e7 ts=2026-04-21T13:13:26.3950000Z; 47h 6m: 69cdc907d385e3b94310f724.jsonl[579] _id=69dd38c97957a33870f291c8 ts=2026-04-13T18:41:12.4770000Z -> 69cdc907d385e3b94310f724.jsonl[583] _id=69dfcf537957a33870f40ddd ts=2026-04-15T17:48:01.5600000Z; 46h 15m: 69cdc907d385e3b94310f724.jsonl[894] _id=69dfdbb27957a33870f4667b ts=2026-04-15T18:40:50.5330000Z -> 69cdc907d385e3b94310f724.jsonl[70] _id=69e266291724f0c9e2f72252 ts=2026-04-17T16:56:08.8080000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 56m 
  - Evidence: 144h 56m: 69cdc907d385e3b94310f724.jsonl[1005] _id=69e271941724f0c9e2f7478c ts=2026-04-17T17:44:51.6060000Z -> 69cdc907d385e3b94310f724.jsonl[1585] _id=69ea67bb1724f0c9e2fb4e0e ts=2026-04-23T18:40:59.6300000Z; 47h 27m: 69cdc907d385e3b94310f724.jsonl[781] _id=69dfd5287957a33870f43629 ts=2026-04-15T18:12:56.4200000Z -> 69cdc907d385e3b94310f724.jsonl[984] _id=69e270a41724f0c9e2f74088 ts=2026-04-17T17:40:52.0610000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 59m 
  - Evidence: 144h 59m: 69cdc907d385e3b94310f724.jsonl[909] _id=69e267f81724f0c9e2f73066 ts=2026-04-17T17:03:51.7910000Z -> 69cdc907d385e3b94310f724.jsonl[1309] _id=69ea5f031724f0c9e2fb08db ts=2026-04-23T18:03:46.7510000Z; 46h 18m: 69cdc907d385e3b94310f724.jsonl[892] _id=69dfdbb07957a33870f4666b ts=2026-04-15T18:40:48.3260000Z -> 69cdc907d385e3b94310f724.jsonl[900] _id=69e266df1724f0c9e2f727ae ts=2026-04-17T16:59:11.0930000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 11m 
  - Evidence: 144h 11m: 69cdc907d385e3b94310f724.jsonl[138] _id=69e279701724f0c9e2f775fc ts=2026-04-17T18:18:23.4920000Z -> 69cdc907d385e3b94310f724.jsonl[245] _id=69ea65101724f0c9e2fb3a9f ts=2026-04-23T18:29:36.4550000Z; 48h 23m: 69cdc907d385e3b94310f724.jsonl[638] _id=69dfd0ca7957a33870f41817 ts=2026-04-15T17:54:17.5890000Z -> 69cdc907d385e3b94310f724.jsonl[127] _id=69e279461724f0c9e2f774da ts=2026-04-17T18:17:41.3790000Z; 47h 13m: 69cdc907d385e3b94310f724.jsonl[552] _id=69dd382a7957a33870f28dc8 ts=2026-04-13T18:38:33.9060000Z -> 69cdc907d385e3b94310f724.jsonl[606] _id=69dfd0597957a33870f414a5 ts=2026-04-15T17:52:24.4260000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 11m 
  - Evidence: 144h 11m: 69cdc907d385e3b94310f724.jsonl[118] _id=69e279681724f0c9e2f775d6 ts=2026-04-17T18:18:15.9300000Z -> 69cdc907d385e3b94310f724.jsonl[1504] _id=69ea651b1724f0c9e2fb3add ts=2026-04-23T18:29:47.6220000Z; 48h 23m: 69cdc907d385e3b94310f724.jsonl[635] _id=69dfd0c87957a33870f41811 ts=2026-04-15T17:54:15.9810000Z -> 69cdc907d385e3b94310f724.jsonl[136] _id=69e279621724f0c9e2f775a8 ts=2026-04-17T18:18:10.1870000Z; 47h 15m: 69cdc907d385e3b94310f724.jsonl[41] _id=69dd38287957a33870f28db2 ts=2026-04-13T18:38:32.2300000Z -> 69cdc907d385e3b94310f724.jsonl[625] _id=69dfd0a67957a33870f416bb ts=2026-04-15T17:53:42.4850000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.007s..0.007s shown 
  - Evidence: 7ms: 69cdc907d385e3b94310f724.jsonl[1510] _id=69ea65491724f0c9e2fb3bd7 ts=2026-04-23T18:30:33.0690000Z -> 69cdc907d385e3b94310f724.jsonl[255] _id=69ea65491724f0c9e2fb3bd9 ts=2026-04-23T18:30:33.0760000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 90h 50m 
  - Evidence: 90h 50m: 69cdc907d385e3b94310f724.jsonl[1236] _id=69e27a9b1724f0c9e2f77bce ts=2026-04-17T18:23:23.3380000Z -> 69cdc907d385e3b94310f724.jsonl[3] _id=69e777fa1724f0c9e2f913e9 ts=2026-04-21T13:13:28.7640000Z; 52h 17m: 69cdc907d385e3b94310f724.jsonl[195] _id=69e77f9c1724f0c9e2f913f9 ts=2026-04-21T13:46:01.1890000Z -> 69cdc907d385e3b94310f724.jsonl[1305] _id=69ea5eee1724f0c9e2fb0841 ts=2026-04-23T18:03:25.7520000Z; 47h 11m: 69cdc907d385e3b94310f724.jsonl[471] _id=69dd384b7957a33870f28ede ts=2026-04-13T18:39:07.6600000Z -> 69cdc907d385e3b94310f724.jsonl[589] _id=69dfcff27957a33870f411ed ts=2026-04-15T17:50:41.3940000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f724.jsonl[600] _id=69dfd02c7957a33870f41361 ts=2026-04-15T17:51:39.4430000Z -> 69cdc907d385e3b94310f724.jsonl[601] _id=69dfd02c7957a33870f41365 ts=2026-04-15T17:51:39.4450000Z; 3ms: 69cdc907d385e3b94310f724.jsonl[114] _id=69e2788c1724f0c9e2f77156 ts=2026-04-17T18:14:35.7650000Z -> 69cdc907d385e3b94310f724.jsonl[115] _id=69e2788c1724f0c9e2f77158 ts=2026-04-17T18:14:35.7680000Z; 4ms: 69cdc907d385e3b94310f724.jsonl[3] _id=69e777fa1724f0c9e2f913e9 ts=2026-04-21T13:13:28.7640000Z -> 69cdc907d385e3b94310f724.jsonl[165] _id=69e777fa1724f0c9e2f913eb ts=2026-04-21T13:13:28.7680000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 2 record(s) match the trigger in 69cdc907d385e3b94310f724.jsonl:69cdc907d385e3b94310f724, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f724.jsonl[781] _id=69dfd5287957a33870f43629 ts=2026-04-15T18:12:56.4200000Z`; `69cdc907d385e3b94310f724.jsonl[1586] _id=69ea67f11724f0c9e2fb4e83 ts=2026-04-23T18:41:52.8860000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f724.jsonl[1379] _id=69ea61bf1724f0c9e2fb20b1 ts=2026-04-23T18:15:26.6630000Z`; `69cdc907d385e3b94310f724.jsonl[1412] _id=69ea62801724f0c9e2fb276d ts=2026-04-23T18:18:40.0330000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f724.jsonl[299] _id=69ea66bf1724f0c9e2fb479d ts=2026-04-23T18:36:47.2320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f724.jsonl[1510] _id=69ea65491724f0c9e2fb3bd7 ts=2026-04-23T18:30:33.0690000Z`; `69cdc907d385e3b94310f724.jsonl[256] _id=69ea654b1724f0c9e2fb3bf0 ts=2026-04-23T18:30:35.6520000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f724.jsonl[1005] _id=69e271941724f0c9e2f7478c ts=2026-04-17T17:44:51.6060000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f724.jsonl[255] _id=69ea65491724f0c9e2fb3bd9 ts=2026-04-23T18:30:33.0760000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 100 unmatched 'DialogueStartEvent' (totals: 176 start, 78 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 4 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 30 start, 17 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.41s, min -3.35s, max -0.19s over 1588 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f724\coverage.yaml

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
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=complete, Unit3=partial 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
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
  - Observed: 22 records 
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

### `DialogueEvent` — 958 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (485); Unit 3 Dev (253); Unit 2 Prod (Refactor) (220)
- **eventKey:** present on 704 of 958 records
- **Intervals:** median 3.12s (p5 0.01s / p95 56.52s, n=957)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x704; [conversationId, dialogueEventType] x254
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 958/958 records)
    numeric range 10 .. 84 (19 unique)
data.dialogueEventType  (string, 958/958 records)
    "DialogueNodeEvent"  x704
    "DialogueStartEvent"  x176
    "DialogueFinishEvent"  x78
data.nodeId  (number, 704/958 records)
    numeric range 0 .. 286 (144 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 464 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (226); Unit 1 Dev (159); Unit 3 Dev (79)
- **Intervals:** median 30.00s (p5 29.96s / p95 48.53s, n=459)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 464/464 records)
data.position.x  (number, 464/464 records)
    numeric range -694.73 .. 1351.64 (198 unique)
data.position.y  (number, 464/464 records)
    numeric range -112.488 .. 165.8 (164 unique)
data.position.z  (number, 464/464 records)
    numeric range -952.421 .. 2361.61 (195 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 62 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (31); Unit 3 Dev (31)
- **Intervals:** median 4.65s (p5 1.03s / p95 141.40s, n=61)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "argumentationNodeAdd"  x38
    "argumentationNodeRemove"  x24
data.argumentationTitle  (string, 62/62 records)
    "Unit 3 - Pollution Upstream"  x31
    "Unit 1 - Freshwater"  x27
    "Unit 1 - Argumentation Tutorial"  x4
data.nodeName  (string, 62/62 records)
    "1"  x12
    "B"  x11
    "A"  x10
    "I"  x8
    "II"  x8
    "4"  x6
    "2"  x4
    "3"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 47 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (29); Unit 2 Prod (Refactor) (13); Unit 3 Dev (5)
- **eventKey:** present on 47 of 47 records
- **Intervals:** median 158.41s (p5 0.00s / p95 169194.69s, n=46)
- **`data` key-set variants:** [questEventType, questID, questName] x30; [questEventType, questID, questName, questSuccessOrFailure] x17
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 47/47 records)
    "questActiveEvent"  x30
    "questFinishEvent"  x17
data.questID  (string, 47/47 records)
    "23"  x8
    "32"  x6
    "33"  x6
    "34"  x5
    "28"  x4
    "29"  x4
    "31"  x4
    "21"  x3
    "16"  x2
    "17"  x2
    "24"  x2
    "18"  x1
data.questName  (string, 47/47 records)
    "Foraged Forging"  x8
    "Defend the Expedition"  x6
    "Info and Intros"  x6
    "What Was That?"  x5
    "Gear Up"  x4
    "Getting Your Space Legs"  x4
    "TK, Reporting In!"  x4
    "Escape the Ruin"  x3
    "Investigate the Temple"  x2
    "Pollution Solution"  x2
    "Supply Run"  x2
    "Forsaken Facility"  x1
data.questSuccessOrFailure  (string, 17/47 records)
    "Succeeded"  x17
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 22 records

- **Scenes:** Unit 3 Dev (16); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 35.42s (p5 2.37s / p95 166702.77s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "MapCloseEvent"  x11
    "MapOpenEvent"  x11
data.featureUsed  (string, 22/22 records)
    "Map"  x22
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (12); Unit 3 Dev (3)
- **Intervals:** median 52.53s (p5 0.74s / p95 294908.00s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x6
    "Unit 1 - Does the planet WAT-247 have freshwater"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
data.argumentationTitle  (string, 15/15 records)
    "Unit 1 - Argumentation Tutorial"  x6
    "Unit 1 - Freshwater"  x6
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (12)
- **Intervals:** median 2.58s (p5 0.42s / p95 135.25s, n=11)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x6
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x12
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - Pollution Site Data"  x8
    "BackingInfoPanel - "  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2)
- **Intervals:** median 239.54s (p5 13.05s / p95 451589.55s, n=5)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/6 records)
    "Started"  x4
    "Finished"  x2
data.Unit  (string, 6/6 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 174201.67s (p5 174201.67s / p95 174201.67s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x2
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
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now
- `EndOfUnit` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (24x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*