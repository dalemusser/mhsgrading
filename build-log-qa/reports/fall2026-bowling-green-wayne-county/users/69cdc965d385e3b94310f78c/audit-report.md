# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f78c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f78c
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f78c.jsonl
- **Records:** 2042 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f78c
- **Time span:** 2026-04-14T13:50:43.235000+00:00 .. 2026-04-22T14:29:45.808000+00:00 (192h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f78c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **9 event types**, 2042 records, 6 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 45 INFO, 2 NOT_TESTED, 30 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1347 | 65.96 | 1 | 6 | 935 | 2026-04-14T13:51:01.354000+00:00 | 2026-04-22T14:28:32.564000+00:00 | 192h 37m |
| PlayerPositionEvent | 482 | 23.6 | 1 | 6 | 0 | 2026-04-14T13:50:43.235000+00:00 | 2026-04-22T14:29:45.808000+00:00 | 192h 39m |
| Topographic Map Event | 76 | 3.72 | 1 | 2 | 0 | 2026-04-14T14:23:44.728000+00:00 | 2026-04-22T14:10:03.339000+00:00 | 191h 46m |
| argumentationNodeEvent | 45 | 2.2 | 1 | 3 | 0 | 2026-04-14T14:10:12.877000+00:00 | 2026-04-20T14:20:56.609000+00:00 | 144h 10m |
| questEvent | 43 | 2.11 | 1 | 6 | 43 | 2026-04-14T13:51:01.327000+00:00 | 2026-04-22T14:26:04.213000+00:00 | 192h 35m |
| argumentationToolEvent | 28 | 1.37 | 1 | 2 | 0 | 2026-04-20T13:34:37.142000+00:00 | 2026-04-20T14:20:22.538000+00:00 | 45m 45s |
| argumentationEvent | 9 | 0.44 | 1 | 3 | 0 | 2026-04-14T14:09:03.471000+00:00 | 2026-04-20T14:20:58.386000+00:00 | 144h 11m |
| Soil Key Puzzle | 8 | 0.39 | 1 | 3 | 0 | 2026-04-16T13:50:58.223000+00:00 | 2026-04-22T14:19:25.139000+00:00 | 144h 28m |
| EndOfUnit | 4 | 0.2 | 1 | 3 | 0 | 2026-04-14T14:16:41.297000+00:00 | 2026-04-22T14:13:21.695000+00:00 | 191h 56m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 174845.442s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.006s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 149.353s median 
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
  - Observed: 7.967s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.934s median 
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
  - Observed: 76 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 45 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 28 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 48; 49; 50; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f78c.jsonl[1397] _id=69de4b137957a33870f349a7 ts=2026-04-14T14:11:30.6450000Z`; `69cdc965d385e3b94310f78c.jsonl[1536] _id=69e0ecd57957a33870f52a3d ts=2026-04-16T14:06:12.7820000Z`; `69cdc965d385e3b94310f78c.jsonl[633] _id=69e62ad01724f0c9e2f85c1d ts=2026-04-20T13:32:00.1320000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1346 | 0.002 | 2.155 | 515.194 | 43.877 | 341063.775 | 0.12 | 352 | 5 |
| PlayerPositionEvent | 475 | 29.776 | 30.006 | 1459.618 | 38.826 | 341010.052 | 0.04 | 0 | 3 |
| Topographic Map Event | 75 | 2.009 | 12.438 | 9205.048 | 948.781 | 342647.702 | 0.01 | 0 | 5 |
| argumentationNodeEvent | 44 | 0.949 | 7.967 | 11796.448 | 44.043 | 516112.533 | 0.01 | 0 | 2 |
| questEvent | 42 | 0.003 | 215.107 | 16507.212 | 160187.399 | 341422.058 | 0.0 | 4 | 9 |
| argumentationToolEvent | 27 | 0.01 | 0.934 | 101.681 | 52.224 | 2632.044 | 0.59 | 6 | 1 |
| argumentationEvent | 8 | 0.149 | 108.77 | 64889.364 | 336331.122 | 516096.317 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 7 | 2.965 | 149.353 | 74300.988 | 293939.528 | 346027.629 | 0.0 | 0 | 3 |
| EndOfUnit | 3 | 0.0 | 174845.442 | 230333.466 | 482024.005 | 516154.956 | 0.0 | 1 | 2 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.006s (p5 29.96s, p95 38.83s, n=475) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc965d385e3b94310f78c.jsonl[1253] _id=69e8d7821724f0c9e2fa61a1 ts=2026-04-22T14:13:21.6950000Z ~ 69cdc965d385e3b94310f78c.jsonl[1244] _id=69e8d7931724f0c9e2fa61ef ts=2026-04-22T14:13:21.695Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `149ms: 69cdc965d385e3b94310f78c.jsonl[876] _id=69e6364a1724f0c9e2f8a16d ts=2026-04-20T14:20:58.2370000Z ~ 69cdc965d385e3b94310f78c.jsonl[879] _id=69e6364a1724f0c9e2f8a173 ts=2026-04-20T14:20:58.3860000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `956ms: 69cdc965d385e3b94310f78c.jsonl[846] _id=69e6361e1724f0c9e2f8a047 ts=2026-04-20T14:20:14.1550000Z ~ 69cdc965d385e3b94310f78c.jsonl[857] _id=69e6361f1724f0c9e2f8a04b ts=2026-04-20T14:20:15.1110000Z`; `956ms: 69cdc965d385e3b94310f78c.jsonl[1885] _id=69e6361e1724f0c9e2f8a049 ts=2026-04-20T14:20:14.1660000Z ~ 69cdc965d385e3b94310f78c.jsonl[858] _id=69e6361f1724f0c9e2f8a04d ts=2026-04-20T14:20:15.1220000Z`; `683ms: 69cdc965d385e3b94310f78c.jsonl[854] _id=69e636231724f0c9e2f8a05b ts=2026-04-20T14:20:18.8540000Z ~ 69cdc965d385e3b94310f78c.jsonl[860] _id=69e636241724f0c9e2f8a061 ts=2026-04-20T14:20:19.5370000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc965d385e3b94310f78c.jsonl[1638] _id=69e0f3867957a33870f55841 ts=2026-04-16T14:34:46.4500000Z -> 69cdc965d385e3b94310f78c.jsonl[1642] _id=69e627ce1724f0c9e2f84bf1 ts=2026-04-20T13:19:10.2250000Z; 47h 6m: 69cdc965d385e3b94310f78c.jsonl[1446] _id=69de4f517957a33870f366d0 ts=2026-04-14T14:29:35.5740000Z -> 69cdc965d385e3b94310f78c.jsonl[232] _id=69e0e5aa7957a33870f4fe5d ts=2026-04-16T13:35:38.1230000Z; 46h 40m: 69cdc965d385e3b94310f78c.jsonl[1910] _id=69e6396d1724f0c9e2f8b410 ts=2026-04-20T14:34:21.3810000Z -> 69cdc965d385e3b94310f78c.jsonl[1911] _id=69e8c9d41724f0c9e2fa09e1 ts=2026-04-22T13:14:59.8220000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 352 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f78c.jsonl[156] _id=69de4b567957a33870f34b24 ts=2026-04-14T14:12:37.7940000Z -> 69cdc965d385e3b94310f78c.jsonl[155] _id=69de4b567957a33870f34b27 ts=2026-04-14T14:12:37.7960000Z; 2ms: 69cdc965d385e3b94310f78c.jsonl[474] _id=69e0f1b47957a33870f54787 ts=2026-04-16T14:26:59.9410000Z -> 69cdc965d385e3b94310f78c.jsonl[476] _id=69e0f1b47957a33870f54789 ts=2026-04-16T14:26:59.9430000Z; 3ms: 69cdc965d385e3b94310f78c.jsonl[1147] _id=69e8d4cc1724f0c9e2fa4c89 ts=2026-04-22T14:01:47.5560000Z -> 69cdc965d385e3b94310f78c.jsonl[1145] _id=69e8d4cc1724f0c9e2fa4c8b ts=2026-04-22T14:01:47.5590000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 22m 
  - Evidence: 143h 22m: 69cdc965d385e3b94310f78c.jsonl[1423] _id=69de4c4a7957a33870f353b5 ts=2026-04-14T14:16:41.2970000Z -> 69cdc965d385e3b94310f78c.jsonl[707] _id=69e62c841724f0c9e2f869bf ts=2026-04-20T13:39:16.2530000Z; 48h 34m: 69cdc965d385e3b94310f78c.jsonl[707] _id=69e62c841724f0c9e2f869bf ts=2026-04-20T13:39:16.2530000Z -> 69cdc965d385e3b94310f78c.jsonl[1253] _id=69e8d7821724f0c9e2fa61a1 ts=2026-04-22T14:13:21.6950000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f78c.jsonl[1253] _id=69e8d7821724f0c9e2fa61a1 ts=2026-04-22T14:13:21.6950000Z -> 69cdc965d385e3b94310f78c.jsonl[1244] _id=69e8d7931724f0c9e2fa61ef ts=2026-04-22T14:13:21.695Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f78c.jsonl[1639] _id=69e0f3ae7957a33870f558ed ts=2026-04-16T14:35:26.2450000Z -> 69cdc965d385e3b94310f78c.jsonl[1640] _id=69e627c11724f0c9e2f84ba9 ts=2026-04-20T13:18:56.2970000Z; 47h 2m: 69cdc965d385e3b94310f78c.jsonl[229] _id=69de4fc47957a33870f36aa6 ts=2026-04-14T14:31:31.2840000Z -> 69cdc965d385e3b94310f78c.jsonl[230] _id=69e0e5637957a33870f4fad7 ts=2026-04-16T13:34:26.5100000Z; 46h 39m: 69cdc965d385e3b94310f78c.jsonl[975] _id=69e639971724f0c9e2f8b526 ts=2026-04-20T14:35:03.3540000Z -> 69cdc965d385e3b94310f78c.jsonl[978] _id=69e8c9d21724f0c9e2fa09d9 ts=2026-04-22T13:14:58.2300000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 7m 
  - Evidence: 96h 7m: 69cdc965d385e3b94310f78c.jsonl[1575] _id=69e0ef897957a33870f53b51 ts=2026-04-16T14:17:44.7630000Z -> 69cdc965d385e3b94310f78c.jsonl[1903] _id=69e637341724f0c9e2f8a879 ts=2026-04-20T14:24:52.3920000Z; 47h 53m: 69cdc965d385e3b94310f78c.jsonl[938] _id=69e6375f1724f0c9e2f8a96d ts=2026-04-20T14:25:35.1180000Z -> 69cdc965d385e3b94310f78c.jsonl[2018] _id=69e8d8d01724f0c9e2fa67d1 ts=2026-04-22T14:18:55.7440000Z; 24m 14s: 69cdc965d385e3b94310f78c.jsonl[1486] _id=69e0e9457957a33870f515a7 ts=2026-04-16T13:51:01.1880000Z -> 69cdc965d385e3b94310f78c.jsonl[408] _id=69e0eef47957a33870f5383d ts=2026-04-16T14:15:15.4100000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 10m 
  - Evidence: 95h 10m: 69cdc965d385e3b94310f78c.jsonl[542] _id=69e0f37f7957a33870f55815 ts=2026-04-16T14:34:39.3660000Z -> 69cdc965d385e3b94310f78c.jsonl[1757] _id=69e62df71724f0c9e2f870c3 ts=2026-04-20T13:45:27.0680000Z; 47h 51m: 69cdc965d385e3b94310f78c.jsonl[806] _id=69e634ee1724f0c9e2f89823 ts=2026-04-20T14:15:10.0730000Z -> 69cdc965d385e3b94310f78c.jsonl[1993] _id=69e8d5d61724f0c9e2fa54c3 ts=2026-04-22T14:06:13.9950000Z; 47h 24m: 69cdc965d385e3b94310f78c.jsonl[1439] _id=69de4df97957a33870f35e00 ts=2026-04-14T14:23:52.4860000Z -> 69cdc965d385e3b94310f78c.jsonl[278] _id=69e0e8917957a33870f51157 ts=2026-04-16T13:48:01.5650000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 21m 
  - Evidence: 143h 21m: 69cdc965d385e3b94310f78c.jsonl[137] _id=69de4b137957a33870f349a5 ts=2026-04-14T14:11:30.6080000Z -> 69cdc965d385e3b94310f78c.jsonl[640] _id=69e62b131724f0c9e2f85df5 ts=2026-04-20T13:33:06.9250000Z; 41m 21s: 69cdc965d385e3b94310f78c.jsonl[662] _id=69e62c151724f0c9e2f865b7 ts=2026-04-20T13:37:24.6790000Z -> 69cdc965d385e3b94310f78c.jsonl[1864] _id=69e635c61724f0c9e2f89df7 ts=2026-04-20T14:18:46.1540000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 21m 
  - Evidence: 143h 21m: 69cdc965d385e3b94310f78c.jsonl[141] _id=69de4b0e7957a33870f3498f ts=2026-04-14T14:11:25.1050000Z -> 69cdc965d385e3b94310f78c.jsonl[634] _id=69e62b1e1724f0c9e2f85e65 ts=2026-04-20T13:33:17.6380000Z; 41m 33s: 69cdc965d385e3b94310f78c.jsonl[676] _id=69e62c131724f0c9e2f865ab ts=2026-04-20T13:37:22.8240000Z -> 69cdc965d385e3b94310f78c.jsonl[1863] _id=69e635d01724f0c9e2f89e45 ts=2026-04-20T14:18:56.1450000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 43m 52s 
  - Evidence: 43m 52s: 69cdc965d385e3b94310f78c.jsonl[657] _id=69e62bc91724f0c9e2f863bd ts=2026-04-20T13:36:08.9420000Z -> 69cdc965d385e3b94310f78c.jsonl[1883] _id=69e636111724f0c9e2f89ffe ts=2026-04-20T14:20:00.9860000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.010s..0.011s shown 
  - Evidence: 10ms: 69cdc965d385e3b94310f78c.jsonl[851] _id=69e636251724f0c9e2f8a077 ts=2026-04-20T14:20:21.5410000Z -> 69cdc965d385e3b94310f78c.jsonl[862] _id=69e636261724f0c9e2f8a079 ts=2026-04-20T14:20:21.5510000Z; 11ms: 69cdc965d385e3b94310f78c.jsonl[846] _id=69e6361e1724f0c9e2f8a047 ts=2026-04-20T14:20:14.1550000Z -> 69cdc965d385e3b94310f78c.jsonl[1885] _id=69e6361e1724f0c9e2f8a049 ts=2026-04-20T14:20:14.1660000Z; 11ms: 69cdc965d385e3b94310f78c.jsonl[854] _id=69e636231724f0c9e2f8a05b ts=2026-04-20T14:20:18.8540000Z -> 69cdc965d385e3b94310f78c.jsonl[859] _id=69e636231724f0c9e2f8a05d ts=2026-04-20T14:20:18.8650000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 50m 
  - Evidence: 94h 50m: 69cdc965d385e3b94310f78c.jsonl[1613] _id=69e0f2157957a33870f54aab ts=2026-04-16T14:28:36.8250000Z -> 69cdc965d385e3b94310f78c.jsonl[545] _id=69e627c31724f0c9e2f84bb9 ts=2026-04-20T13:18:58.8830000Z; 47h 17m: 69cdc965d385e3b94310f78c.jsonl[175] _id=69de4cbe7957a33870f35667 ts=2026-04-14T14:18:37.9310000Z -> 69cdc965d385e3b94310f78c.jsonl[1451] _id=69e0e5bc7957a33870f4ff0f ts=2026-04-16T13:35:56.5830000Z; 46h 48m: 69cdc965d385e3b94310f78c.jsonl[945] _id=69e6378c1724f0c9e2f8aa89 ts=2026-04-20T14:26:19.8350000Z -> 69cdc965d385e3b94310f78c.jsonl[1914] _id=69e8c9d41724f0c9e2fa09de ts=2026-04-22T13:14:59.5160000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.003s..0.011s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f78c.jsonl[107] _id=69de4a6e7957a33870f34517 ts=2026-04-14T14:08:45.0350000Z -> 69cdc965d385e3b94310f78c.jsonl[108] _id=69de4a6e7957a33870f3451b ts=2026-04-14T14:08:45.0380000Z; 10ms: 69cdc965d385e3b94310f78c.jsonl[1306] _id=69e8da7c1724f0c9e2fa701f ts=2026-04-22T14:26:04.2030000Z -> 69cdc965d385e3b94310f78c.jsonl[1302] _id=69e8da7c1724f0c9e2fa7021 ts=2026-04-22T14:26:04.2130000Z; 11ms: 69cdc965d385e3b94310f78c.jsonl[61] _id=69de48ac7957a33870f337fd ts=2026-04-14T14:01:15.7430000Z -> 69cdc965d385e3b94310f78c.jsonl[57] _id=69de48ad7957a33870f337ff ts=2026-04-14T14:01:15.7540000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc965d385e3b94310f78c.jsonl:69cdc965d385e3b94310f78c, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f78c.jsonl[1486] _id=69e0e9457957a33870f515a7 ts=2026-04-16T13:51:01.1880000Z`; `69cdc965d385e3b94310f78c.jsonl[1575] _id=69e0ef897957a33870f53b51 ts=2026-04-16T14:17:44.7630000Z`; `69cdc965d385e3b94310f78c.jsonl[938] _id=69e6375f1724f0c9e2f8a96d ts=2026-04-20T14:25:35.1180000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f78c.jsonl[498] _id=69e0f22f7957a33870f54bad ts=2026-04-16T14:29:03.3780000Z`; `69cdc965d385e3b94310f78c.jsonl[722] _id=69e62e9b1724f0c9e2f8746f ts=2026-04-20T13:48:11.4290000Z`; `69cdc965d385e3b94310f78c.jsonl[1773] _id=69e62efc1724f0c9e2f876c9 ts=2026-04-20T13:49:47.6430000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f78c.jsonl[879] _id=69e6364a1724f0c9e2f8a173 ts=2026-04-20T14:20:58.3860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f78c.jsonl[1884] _id=69e636151724f0c9e2f8a017 ts=2026-04-20T14:20:04.6230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 163 unmatched 'DialogueStartEvent' (totals: 286 start, 126 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 14 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 25 start, 18 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.48s, min -17.49s, max -0.30s over 2042 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f78c\coverage.yaml

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
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=complete, Unit3=complete 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
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
  - Observed: 76 records 
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

### `DialogueEvent` — 1347 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (584); Unit 3 Dev (326); Unit 1 Dev (197); Unit 3 Dungeon Dev (174); Unit 4 Dev - Dungeon (41); Unit 4 Dev (25)
- **eventKey:** present on 935 of 1347 records
- **Intervals:** median 2.16s (p5 0.01s / p95 43.88s, n=1346)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x935; [conversationId, dialogueEventType] x412
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1347/1347 records)
    numeric range 8 .. 104 (38 unique)
data.dialogueEventType  (string, 1347/1347 records)
    "DialogueNodeEvent"  x935
    "DialogueStartEvent"  x286
    "DialogueFinishEvent"  x126
data.nodeId  (number, 935/1347 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 482 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (185); Unit 3 Dev (108); Unit 3 Dungeon Dev (104); Unit 1 Dev (52); Unit 4 Dev (18); Unit 4 Dev - Dungeon (15)
- **Intervals:** median 30.01s (p5 29.96s / p95 38.83s, n=475)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 482/482 records)
data.position.x  (number, 482/482 records)
    numeric range -741.427 .. 1450.88 (276 unique)
data.position.y  (number, 482/482 records)
    numeric range -115.127 .. 157.759 (196 unique)
data.position.z  (number, 482/482 records)
    numeric range -1115.78 .. 1599.28 (277 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 76 records

- **Scenes:** Unit 3 Dev (56); Unit 2 Prod (Refactor) (20)
- **Intervals:** median 12.44s (p5 2.71s / p95 948.78s, n=75)
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapCloseEvent"  x38
    "MapOpenEvent"  x38
data.featureUsed  (string, 76/76 records)
    "Map"  x76
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 45 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 3 Dev (15); Unit 1 Dev (7)
- **Intervals:** median 7.97s (p5 1.47s / p95 44.04s, n=44)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "argumentationNodeAdd"  x27
    "argumentationNodeRemove"  x18
data.argumentationTitle  (string, 45/45 records)
    "Unit 2 – Watershed"  x23
    "Unit 3 - Pollution Upstream"  x15
    "Unit 1 - Freshwater"  x7
data.nodeName  (string, 45/45 records)
    "I"  x10
    "1"  x8
    "A"  x8
    "B"  x5
    "II"  x5
    "2"  x2
    "3"  x2
    "C"  x2
    "D"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 43 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 1 Dev (12); Unit 3 Dev (9); Unit 3 Dungeon Dev (4); Unit 4 Dev - Dungeon (3); Unit 4 Dev (1)
- **eventKey:** present on 43 of 43 records
- **Intervals:** median 215.11s (p5 0.01s / p95 160187.40s, n=42)
- **`data` key-set variants:** [questEventType, questID, questName] x25; [questEventType, questID, questName, questSuccessOrFailure] x18
- **Fields under `data`:**

```text
data.questEventType  (string, 43/43 records)
    "questActiveEvent"  x25
    "questFinishEvent"  x18
data.questID  (string, 43/43 records)
    20 unique values (see csv/event_unique_values.csv)
data.questName  (string, 43/43 records)
    20 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 18/43 records)
    "Succeeded"  x18
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationToolEvent` — 28 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (20); Unit 2 Prod (Refactor) (8)
- **Intervals:** median 0.93s (p5 0.01s / p95 52.22s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "argumentationToolClose"  x14
    "argumentationToolOpen"  x14
data.argumentationTitle  (string, 28/28 records)
    "Unit 3 - Pollution Upstream"  x20
    "Unit 2 – Watershed"  x8
data.toolName  (string, 28/28 records)
    "BackingInfoPanel - Pollution Site Data"  x18
    "BackingInfoPanel - Waterfall Data"  x4
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 108.77s (p5 4.92s / p95 336331.12s, n=8)
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
- **Intervals:** median 149.35s (p5 10.89s / p95 293939.53s, n=7)
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

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 3 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 174845.44s (p5 17484.54s / p95 482024.00s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "3"  x2
    "1"  x1
    "2"  x1
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
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (18x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*