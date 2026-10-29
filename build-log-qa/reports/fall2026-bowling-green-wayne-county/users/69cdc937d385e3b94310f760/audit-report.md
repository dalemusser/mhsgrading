# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f760

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f760
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f760.jsonl
- **Records:** 2516 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f760
- **Time span:** 2026-04-13T19:40:47.495000+00:00 .. 2026-04-23T20:10:25.141000+00:00 (240h 29m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f760\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 2516 records, 4 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 49 INFO, 5 NOT_TESTED, 29 PASS.
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
| DialogueEvent | 1758 | 69.87 | 1 | 4 | 1238 | 2026-04-13T19:41:05.761000+00:00 | 2026-04-23T20:10:09.660000+00:00 | 240h 29m |
| PlayerPositionEvent | 506 | 20.11 | 1 | 4 | 0 | 2026-04-13T19:40:47.495000+00:00 | 2026-04-23T20:10:25.141000+00:00 | 240h 29m |
| Topographic Map Event | 76 | 3.02 | 1 | 2 | 0 | 2026-04-15T19:15:47.844000+00:00 | 2026-04-21T19:52:06.526000+00:00 | 144h 36m |
| argumentationNodeEvent | 71 | 2.82 | 1 | 3 | 0 | 2026-04-13T19:56:59.229000+00:00 | 2026-04-23T19:56:33.506000+00:00 | 239h 59m |
| questEvent | 53 | 2.11 | 1 | 4 | 53 | 2026-04-13T19:41:05.746000+00:00 | 2026-04-23T20:03:14.996000+00:00 | 240h 22m |
| argumentationToolEvent | 30 | 1.19 | 1 | 2 | 0 | 2026-04-17T20:04:21.195000+00:00 | 2026-04-21T20:04:49.587000+00:00 | 96h 0m |
| argumentationEvent | 10 | 0.4 | 1 | 3 | 0 | 2026-04-13T19:56:18.671000+00:00 | 2026-04-23T19:56:35.872000+00:00 | 240h 0m |
| crash | 5 | 0.2 | 1 | 1 | 0 |  |  | ? |
| Soil Key Puzzle | 4 | 0.16 | 1 | 2 | 0 | 2026-04-17T19:22:48.840000+00:00 | 2026-04-23T20:02:34.722000+00:00 | 144h 39m |
| EndOfUnit | 3 | 0.12 | 1 | 2 | 0 | 2026-04-13T20:01:36.194000+00:00 | 2026-04-21T18:58:14.375000+00:00 | 190h 56m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.073s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 343699.09s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.03s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 49.235s median 
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
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 144.209s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.736s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.917s median 
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
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.1x vs baseline. 
  - Observed: 4 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 76 records this build 
  - Expected: new logging or newly exercised content — review
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
  - Observed: Unit 1 - Argumentation Tutorial; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 30 records 
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
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
  - Observed: 122 mismatch(es); e.g. 'DialogueNodeEvent:31:51' vs expected 'DialogueNodeEvent:31:67' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f760.jsonl[590] _id=69dd4a637957a33870f2b10b ts=2026-04-13T19:56:18.5790000Z`; `69cdc937d385e3b94310f760.jsonl[591] _id=69dd4a647957a33870f2b10f ts=2026-04-13T19:56:18.7560000Z`; `69cdc937d385e3b94310f760.jsonl[592] _id=69dd4a647957a33870f2b111 ts=2026-04-13T19:56:19.1890000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:54' vs expected 'questActiveEvent:21' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc937d385e3b94310f760.jsonl[1724] _id=69e7c79e1724f0c9e2f9ace9 ts=2026-04-21T18:53:17.7940000Z`; `69cdc937d385e3b94310f760.jsonl[1732] _id=69e7c8061724f0c9e2f9ae71 ts=2026-04-21T18:55:01.5510000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1757 | 0.003 | 1.073 | 492.74 | 38.527 | 341143.57 | 0.12 | 443 | 6 |
| PlayerPositionEvent | 502 | 29.744 | 30.03 | 1724.49 | 44.547 | 341028.478 | 0.03 | 0 | 4 |
| Topographic Map Event | 75 | 0.346 | 14.251 | 6941.049 | 1022.622 | 343475.546 | 0.01 | 0 | 7 |
| argumentationNodeEvent | 70 | 0.824 | 6.736 | 12342.49 | 52.683 | 345898.654 | 0.0 | 0 | 3 |
| questEvent | 52 | 0.008 | 149.452 | 16640.947 | 169287.22 | 341097.607 | 0.0 | 3 | 12 |
| argumentationToolEvent | 29 | 0.008 | 0.917 | 11918.22 | 5.13 | 345600.314 | 0.01 | 5 | 1 |
| argumentationEvent | 9 | 0.164 | 144.209 | 96001.911 | 345630.597 | 345888.191 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| Soil Key Puzzle | 3 | 35.716 | 49.235 | 173595.294 | 468635.761 | 520700.931 | 0.0 | 0 | 1 |
| EndOfUnit | 2 | 0.0 | 343699.09 | 343699.09 | 653028.272 | 687398.181 | 0.0 | 1 | 1 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc937d385e3b94310f760.jsonl[1925] _id=69e7cd0c1724f0c9e2f9cc49 ts=? == 69cdc937d385e3b94310f760.jsonl[2116] _id=69e7d5be1724f0c9e2f9f265 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.030s (p5 29.96s, p95 44.55s, n=502) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc937d385e3b94310f760.jsonl[312] _id=69e7c8c61724f0c9e2f9b313 ts=2026-04-21T18:58:14.3750000Z ~ 69cdc937d385e3b94310f760.jsonl[1776] _id=69e7c8d91724f0c9e2f9b3a5 ts=2026-04-21T18:58:14.375Z`
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `346ms: 69cdc937d385e3b94310f760.jsonl[1488] _id=69e28d491724f0c9e2f7bd2e ts=2026-04-17T19:43:04.4410000Z ~ 69cdc937d385e3b94310f760.jsonl[1490] _id=69e28d4b1724f0c9e2f7bd38 ts=2026-04-17T19:43:04.7870000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `164ms: 69cdc937d385e3b94310f760.jsonl[404] _id=69ea79751724f0c9e2fb6283 ts=2026-04-23T19:56:35.7080000Z ~ 69cdc937d385e3b94310f760.jsonl[2342] _id=69ea79751724f0c9e2fb628d ts=2026-04-23T19:56:35.8720000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `701ms: 69cdc937d385e3b94310f760.jsonl[2238] _id=69e7d84c1724f0c9e2f9fcb5 ts=2026-04-21T20:04:28.2540000Z ~ 69cdc937d385e3b94310f760.jsonl[357] _id=69e7d84d1724f0c9e2f9fcc3 ts=2026-04-21T20:04:28.9550000Z`; `994ms: 69cdc937d385e3b94310f760.jsonl[2246] _id=69e7d8601724f0c9e2f9fd59 ts=2026-04-21T20:04:48.5930000Z ~ 69cdc937d385e3b94310f760.jsonl[2248] _id=69e7d8611724f0c9e2f9fd61 ts=2026-04-21T20:04:49.5870000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `106ms: 69cdc937d385e3b94310f760.jsonl[1724] _id=69e7c79e1724f0c9e2f9ace9 ts=2026-04-21T18:53:17.7940000Z ~ 69cdc937d385e3b94310f760.jsonl[1725] _id=69e7c79f1724f0c9e2f9acf3 ts=2026-04-21T18:53:17.9000000Z`; `65ms: 69cdc937d385e3b94310f760.jsonl[1732] _id=69e7c8061724f0c9e2f9ae71 ts=2026-04-21T18:55:01.5510000Z ~ 69cdc937d385e3b94310f760.jsonl[1734] _id=69e7c8061724f0c9e2f9ae79 ts=2026-04-21T18:55:01.6160000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc937d385e3b94310f760.jsonl[1712] _id=69e293361724f0c9e2f7dae4 ts=2026-04-17T20:08:20.5400000Z -> 69cdc937d385e3b94310f760.jsonl[1726] _id=69e7c7cc1724f0c9e2f9ad83 ts=2026-04-21T18:54:04.1100000Z; 47h 34m: 69cdc937d385e3b94310f760.jsonl[2258] _id=69e7d88b1724f0c9e2f9fe23 ts=2026-04-21T20:05:31.0070000Z -> 69cdc937d385e3b94310f760.jsonl[2269] _id=69ea75871724f0c9e2fb57bb ts=2026-04-23T19:39:50.2420000Z; 47h 2m: 69cdc937d385e3b94310f760.jsonl[708] _id=69dd4cf87957a33870f2bb15 ts=2026-04-13T20:07:19.0740000Z -> 69cdc937d385e3b94310f760.jsonl[719] _id=69dfe2987957a33870f46787 ts=2026-04-15T19:10:15.4000000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 443 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f760.jsonl[1412] _id=69e28c221724f0c9e2f7b8be ts=2026-04-17T19:38:09.0930000Z -> 69cdc937d385e3b94310f760.jsonl[1413] _id=69e28c221724f0c9e2f7b8c0 ts=2026-04-17T19:38:09.0960000Z; 3ms: 69cdc937d385e3b94310f760.jsonl[2469] _id=69ea7ae71724f0c9e2fb66dd ts=2026-04-23T20:02:46.5050000Z -> 69cdc937d385e3b94310f760.jsonl[2470] _id=69ea7ae71724f0c9e2fb66df ts=2026-04-23T20:02:46.5080000Z; 3ms: 69cdc937d385e3b94310f760.jsonl[26] _id=69dd4b467957a33870f2b443 ts=2026-04-13T20:00:05.1490000Z -> 69cdc937d385e3b94310f760.jsonl[29] _id=69dd4b467957a33870f2b445 ts=2026-04-13T20:00:05.1520000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 190h 56m 
  - Evidence: 190h 56m: 69cdc937d385e3b94310f760.jsonl[649] _id=69dd4ba17957a33870f2b59b ts=2026-04-13T20:01:36.1940000Z -> 69cdc937d385e3b94310f760.jsonl[312] _id=69e7c8c61724f0c9e2f9b313 ts=2026-04-21T18:58:14.3750000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f760.jsonl[312] _id=69e7c8c61724f0c9e2f9b313 ts=2026-04-21T18:58:14.3750000Z -> 69cdc937d385e3b94310f760.jsonl[1776] _id=69e7c8d91724f0c9e2f9b3a5 ts=2026-04-21T18:58:14.375Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc937d385e3b94310f760.jsonl[1721] _id=69e293771724f0c9e2f7dc2e ts=2026-04-17T20:09:26.4730000Z -> 69cdc937d385e3b94310f760.jsonl[1723] _id=69e7c79c1724f0c9e2f9acd9 ts=2026-04-21T18:53:14.9510000Z; 47h 33m: 69cdc937d385e3b94310f760.jsonl[2251] _id=69e7d87f1724f0c9e2f9fde5 ts=2026-04-21T20:05:19.6350000Z -> 69cdc937d385e3b94310f760.jsonl[2261] _id=69ea753a1724f0c9e2fb56e7 ts=2026-04-23T19:38:33.1230000Z; 47h 0m: 69cdc937d385e3b94310f760.jsonl[39] _id=69dd4d887957a33870f2bc65 ts=2026-04-13T20:09:43.8690000Z -> 69cdc937d385e3b94310f760.jsonl[715] _id=69dfe2937957a33870f46771 ts=2026-04-15T19:10:10.5330000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 38m 
  - Evidence: 144h 38m: 69cdc937d385e3b94310f760.jsonl[1331] _id=69e288bb1724f0c9e2f7acca ts=2026-04-17T19:23:38.0750000Z -> 69cdc937d385e3b94310f760.jsonl[2463] _id=69ea7ab81724f0c9e2fb664f ts=2026-04-23T20:01:59.0060000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 69cdc937d385e3b94310f760.jsonl[1566] _id=69e28ee11724f0c9e2f7ca0c ts=2026-04-17T19:49:52.7050000Z -> 69cdc937d385e3b94310f760.jsonl[1909] _id=69e7cc941724f0c9e2f9c8c7 ts=2026-04-21T19:14:28.2510000Z; 46h 54m: 69cdc937d385e3b94310f760.jsonl[1105] _id=69dff0247957a33870f49ddf ts=2026-04-15T20:08:03.3410000Z -> 69cdc937d385e3b94310f760.jsonl[123] _id=69e283d81724f0c9e2f79894 ts=2026-04-17T19:02:46.6990000Z; 31m 12s: 69cdc937d385e3b94310f760.jsonl[1294] _id=69e285f91724f0c9e2f7a132 ts=2026-04-17T19:11:52.3160000Z -> 69cdc937d385e3b94310f760.jsonl[1488] _id=69e28d491724f0c9e2f7bd2e ts=2026-04-17T19:43:04.4410000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 4m 
  - Evidence: 96h 4m: 69cdc937d385e3b94310f760.jsonl[619] _id=69dd4b057957a33870f2b309 ts=2026-04-13T19:59:01.0090000Z -> 69cdc937d385e3b94310f760.jsonl[1607] _id=69e292261724f0c9e2f7d550 ts=2026-04-17T20:03:49.2000000Z; 95h 54m: 69cdc937d385e3b94310f760.jsonl[294] _id=69e2932c1724f0c9e2f7da8c ts=2026-04-17T20:08:11.7730000Z -> 69cdc937d385e3b94310f760.jsonl[2205] _id=69e7d7c81724f0c9e2f9fb3f ts=2026-04-21T20:02:15.9780000Z; 47h 52m: 69cdc937d385e3b94310f760.jsonl[2205] _id=69e7d7c81724f0c9e2f9fb3f ts=2026-04-21T20:02:15.9780000Z -> 69cdc937d385e3b94310f760.jsonl[2377] _id=69ea790e1724f0c9e2fb6139 ts=2026-04-23T19:54:53.1580000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 4m 
  - Evidence: 96h 4m: 69cdc937d385e3b94310f760.jsonl[618] _id=69dd4b047957a33870f2b305 ts=2026-04-13T19:58:59.3090000Z -> 69cdc937d385e3b94310f760.jsonl[1646] _id=69e2922e1724f0c9e2f7d588 ts=2026-04-17T20:03:57.9630000Z; 95h 54m: 69cdc937d385e3b94310f760.jsonl[1708] _id=69e2932b1724f0c9e2f7da82 ts=2026-04-17T20:08:10.1450000Z -> 69cdc937d385e3b94310f760.jsonl[2212] _id=69e7d7d61724f0c9e2f9fb67 ts=2026-04-21T20:02:30.0300000Z; 47h 49m: 69cdc937d385e3b94310f760.jsonl[2256] _id=69e7d8811724f0c9e2f9fde9 ts=2026-04-21T20:05:21.2090000Z -> 69cdc937d385e3b94310f760.jsonl[2384] _id=69ea79111724f0c9e2fb6143 ts=2026-04-23T19:54:56.6490000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 0m 
  - Evidence: 96h 0m: 69cdc937d385e3b94310f760.jsonl[276] _id=69e292491724f0c9e2f7d5fc ts=2026-04-17T20:04:24.5590000Z -> 69cdc937d385e3b94310f760.jsonl[355] _id=69e7d8491724f0c9e2f9fca1 ts=2026-04-21T20:04:24.8730000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.008s..0.014s shown 
  - Evidence: 8ms: 69cdc937d385e3b94310f760.jsonl[352] _id=69e7d85e1724f0c9e2f9fd49 ts=2026-04-21T20:04:46.3550000Z -> 69cdc937d385e3b94310f760.jsonl[2244] _id=69e7d85e1724f0c9e2f9fd4b ts=2026-04-21T20:04:46.3630000Z; 13ms: 69cdc937d385e3b94310f760.jsonl[2240] _id=69e7d8531724f0c9e2f9fcf3 ts=2026-04-21T20:04:34.9750000Z -> 69cdc937d385e3b94310f760.jsonl[2241] _id=69e7d8531724f0c9e2f9fcf5 ts=2026-04-21T20:04:34.9880000Z; 14ms: 69cdc937d385e3b94310f760.jsonl[357] _id=69e7d84d1724f0c9e2f9fcc3 ts=2026-04-21T20:04:28.9550000Z -> 69cdc937d385e3b94310f760.jsonl[2187] _id=69e7d84d1724f0c9e2f9fcc5 ts=2026-04-21T20:04:28.9690000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f760.jsonl[1718] _id=69e293351724f0c9e2f7dae0 ts=2026-04-17T20:08:20.1870000Z -> 69cdc937d385e3b94310f760.jsonl[1724] _id=69e7c79e1724f0c9e2f9ace9 ts=2026-04-21T18:53:17.7940000Z; 47h 43m: 69cdc937d385e3b94310f760.jsonl[2123] _id=69e7d62a1724f0c9e2f9f44b ts=2026-04-21T19:55:21.8690000Z -> 69cdc937d385e3b94310f760.jsonl[2262] _id=69ea753d1724f0c9e2fb56f1 ts=2026-04-23T19:38:35.9070000Z; 47h 7m: 69cdc937d385e3b94310f760.jsonl[670] _id=69dd4c017957a33870f2b713 ts=2026-04-13T20:03:12.5240000Z -> 69cdc937d385e3b94310f760.jsonl[718] _id=69dfe2967957a33870f46781 ts=2026-04-15T19:10:13.8300000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.008s..0.025s shown 
  - Evidence: 8ms: 69cdc937d385e3b94310f760.jsonl[577] _id=69dd4a5a7957a33870f2b0d5 ts=2026-04-13T19:56:08.7710000Z -> 69cdc937d385e3b94310f760.jsonl[583] _id=69dd4a5a7957a33870f2b0d9 ts=2026-04-13T19:56:08.7790000Z; 9ms: 69cdc937d385e3b94310f760.jsonl[3] _id=69dd48ea7957a33870f2ac57 ts=2026-04-13T19:50:01.6340000Z -> 69cdc937d385e3b94310f760.jsonl[523] _id=69dd48eb7957a33870f2ac5b ts=2026-04-13T19:50:01.6430000Z; 25ms: 69cdc937d385e3b94310f760.jsonl[2] _id=69dd48407957a33870f2a929 ts=2026-04-13T19:47:11.8650000Z -> 69cdc937d385e3b94310f760.jsonl[496] _id=69dd48407957a33870f2a92d ts=2026-04-13T19:47:11.8900000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 2 record(s) match the trigger in 69cdc937d385e3b94310f760.jsonl:69cdc937d385e3b94310f760, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f760.jsonl[1331] _id=69e288bb1724f0c9e2f7acca ts=2026-04-17T19:23:38.0750000Z`; `69cdc937d385e3b94310f760.jsonl[2447] _id=69ea7adb1724f0c9e2fb66ad ts=2026-04-23T20:02:34.7220000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f760.jsonl[175] _id=69e28cb71724f0c9e2f7bac6 ts=2026-04-17T19:40:37.0290000Z`; `69cdc937d385e3b94310f760.jsonl[1846] _id=69e7ca8c1724f0c9e2f9bc87 ts=2026-04-21T19:05:48.0740000Z`; `69cdc937d385e3b94310f760.jsonl[1885] _id=69e7cbb91724f0c9e2f9c37d ts=2026-04-21T19:10:48.7970000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f760.jsonl[2188] _id=69e7d84d1724f0c9e2f9fcc7 ts=2026-04-21T20:04:29.7440000Z`; `69cdc937d385e3b94310f760.jsonl[2242] _id=69e7d8551724f0c9e2f9fd01 ts=2026-04-21T20:04:37.0420000Z`; `69cdc937d385e3b94310f760.jsonl[2243] _id=69e7d8581724f0c9e2f9fd11 ts=2026-04-21T20:04:40.0880000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `69cdc937d385e3b94310f760.jsonl[299] _id=69e7c7d11724f0c9e2f9ad9f ts=?`; `69cdc937d385e3b94310f760.jsonl[1742] _id=69e7c85b1724f0c9e2f9afc3 ts=?`; `69cdc937d385e3b94310f760.jsonl[1925] _id=69e7cd0c1724f0c9e2f9cc49 ts=?`
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f760.jsonl[2377] _id=69ea790e1724f0c9e2fb6139 ts=2026-04-23T19:54:53.1580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f760.jsonl[2241] _id=69e7d8531724f0c9e2f9fcf5 ts=2026-04-21T20:04:34.9880000Z`; `69cdc937d385e3b94310f760.jsonl[2239] _id=69e7d8561724f0c9e2f9fd07 ts=2026-04-21T20:04:38.6880000Z`; `69cdc937d385e3b94310f760.jsonl[359] _id=69e7d8581724f0c9e2f9fd16 ts=2026-04-21T20:04:40.1590000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 231 unmatched 'DialogueStartEvent' (totals: 374 start, 146 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationToolOpen' (totals: 15 open, 15 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 34 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.92s, min -19.12s, max -0.12s over 2511 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f760\coverage.yaml

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
  - Observed: 76 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 5 records 
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

### `DialogueEvent` — 1758 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (1018); Unit 3 Dev (528); Unit 1 Dev (174); Unit 3 Dungeon Dev (38)
- **eventKey:** present on 1238 of 1758 records
- **Intervals:** median 1.07s (p5 0.01s / p95 38.53s, n=1757)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1238; [conversationId, dialogueEventType] x520
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1758/1758 records)
    numeric range 8 .. 103 (32 unique)
data.dialogueEventType  (string, 1758/1758 records)
    "DialogueNodeEvent"  x1238
    "DialogueStartEvent"  x374
    "DialogueFinishEvent"  x146
data.nodeId  (number, 1238/1758 records)
    numeric range 0 .. 286 (207 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 506 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (278); Unit 3 Dev (170); Unit 1 Dev (42); Unit 3 Dungeon Dev (16)
- **Intervals:** median 30.03s (p5 29.96s / p95 44.55s, n=502)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 506/506 records)
data.position.x  (number, 506/506 records)
    numeric range -674.465 .. 1597.68 (287 unique)
data.position.y  (number, 506/506 records)
    numeric range -115.127 .. 158.553 (204 unique)
data.position.z  (number, 506/506 records)
    numeric range -1109.33 .. 2183.51 (288 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 76 records

- **Scenes:** Unit 3 Dev (40); Unit 2 Prod (Refactor) (36)
- **Intervals:** median 14.25s (p5 1.97s / p95 1022.62s, n=75)
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapCloseEvent"  x39
    "MapOpenEvent"  x37
data.featureUsed  (string, 76/76 records)
    "Map"  x76
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 71 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (30); Unit 2 Prod (Refactor) (26); Unit 1 Dev (15)
- **Intervals:** median 6.74s (p5 1.11s / p95 52.68s, n=70)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 71/71 records)
    "argumentationNodeAdd"  x41
    "argumentationNodeRemove"  x30
data.argumentationTitle  (string, 71/71 records)
    "Unit 3 - Pollution Upstream"  x30
    "Unit 2 – Watershed"  x26
    "Unit 1 - Freshwater"  x15
data.nodeName  (string, 71/71 records)
    "I"  x15
    "B"  x13
    "A"  x11
    "II"  x9
    "D"  x6
    "1"  x5
    "4"  x4
    "3"  x3
    "2"  x2
    "C"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 53 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 3 Dev (15); Unit 1 Dev (12); Unit 3 Dungeon Dev (1)
- **eventKey:** present on 53 of 53 records
- **Intervals:** median 149.45s (p5 0.05s / p95 169287.22s, n=52)
- **`data` key-set variants:** [questEventType, questID, questName] x34; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 53/53 records)
    "questActiveEvent"  x34
    "questFinishEvent"  x19
data.questID  (string, 53/53 records)
    15 unique values (see csv/event_unique_values.csv)
data.questName  (string, 53/53 records)
    15 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/53 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationToolEvent` — 30 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 0.92s (p5 0.01s / p95 5.13s, n=29)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "argumentationToolClose"  x15
    "argumentationToolOpen"  x15
data.argumentationTitle  (string, 30/30 records)
    "Unit 3 - Pollution Upstream"  x24
    "Unit 2 – Watershed"  x6
data.toolName  (string, 30/30 records)
    "BackingInfoPanel - Pollution Site Data"  x14
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Watershed Image"  x5
    "BackingInfoPanel - Waterfall Data"  x4
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 144.21s (p5 0.59s / p95 345630.60s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 10/10 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x4
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "Uncaught ReferenceError: onResize is not defined"  x4
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 1 empty-string)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x3
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit2:831:9)"  x1
data.type  (string, 5/5 records)
    "runtime_error"  x4
    "unhandled_rejection"  x1
data.unitId  (string, 5/5 records)
    "unit3"  x3
    "unit2"  x2
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `Soil Key Puzzle` — 4 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 49.23s (p5 37.07s / p95 468635.76s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/4 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/4 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 1 Dev (1)
- **Intervals:** median 343699.09s (p5 34369.91s / p95 653028.27s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "2"  x2
    "1"  x1
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
- `crash` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (30x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*