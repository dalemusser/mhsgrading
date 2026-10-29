# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72d
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f72d.jsonl
- **Records:** 1097 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f72d
- **Time span:** 2026-04-13T17:52:15.997000+00:00 .. 2026-04-23T18:03:05.745000+00:00 (240h 10m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **8 event types**, 1097 records, 3 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 34 INFO, 5 NOT_TESTED, 27 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 567 | 51.69 | 1 | 3 | 419 | 2026-04-13T17:52:34.869000+00:00 | 2026-04-23T18:01:13.256000+00:00 | 240h 8m |
| PlayerPositionEvent | 457 | 41.66 | 1 | 3 | 0 | 2026-04-13T17:52:15.997000+00:00 | 2026-04-23T18:03:05.745000+00:00 | 240h 10m |
| questEvent | 28 | 2.55 | 1 | 3 | 28 | 2026-04-13T17:52:34.835000+00:00 | 2026-04-23T17:59:54.701000+00:00 | 240h 7m |
| Topographic Map Event | 26 | 2.37 | 1 | 2 | 0 | 2026-04-15T18:00:49.040000+00:00 | 2026-04-21T17:58:41.028000+00:00 | 143h 57m |
| Soil Key Puzzle | 8 | 0.73 | 1 | 1 | 0 | 2026-04-15T18:21:38.331000+00:00 | 2026-04-21T17:39:36.736000+00:00 | 143h 17m |
| argumentationNodeEvent | 6 | 0.55 | 1 | 1 | 0 | 2026-04-13T18:34:08.447000+00:00 | 2026-04-13T18:36:28.987000+00:00 | 2m 20s |
| argumentationEvent | 4 | 0.36 | 1 | 1 | 0 | 2026-04-13T18:34:00.843000+00:00 | 2026-04-13T18:36:31.861000+00:00 | 2m 31s |
| EndOfUnit | 1 | 0.09 | 1 | 1 | 0 | 2026-04-13T18:40:19.332000+00:00 | 2026-04-13T18:40:19.332000+00:00 | 0.0s |

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
  - Observed: 30.011s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2210.084s median 
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
  - Observed: 15.97s median 
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
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DialogueEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 567 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 26 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `argumentationEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 4 records 
  - Expected: 14 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 21 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f72d.jsonl[321] _id=69dd37b07957a33870f28a2e ts=2026-04-13T18:36:31.8840000Z`; `69cdc907d385e3b94310f72d.jsonl[36] _id=69e2735e1724f0c9e2f7537a ts=2026-04-17T17:52:29.5580000Z`; `69cdc907d385e3b94310f72d.jsonl[908] _id=69e27c981724f0c9e2f7818e ts=2026-04-17T18:31:25.1370000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 566 | 0.003 | 4.657 | 1527.418 | 109.788 | 339650.501 | 0.04 | 126 | 8 |
| PlayerPositionEvent | 454 | 0.0 | 30.011 | 1530.095 | 32.915 | 339321.661 | 0.04 | 1 | 4 |
| questEvent | 27 | 0.004 | 292.5 | 32016.291 | 172312.154 | 339496.15 | 0.0 | 3 | 11 |
| Topographic Map Event | 25 | 0.413 | 15.926 | 20730.88 | 136460.69 | 345503.746 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 7 | 2.968 | 2210.084 | 73696.915 | 288953.676 | 340718.699 | 0.0 | 0 | 4 |
| argumentationNodeEvent | 5 | 3.583 | 15.97 | 28.108 | 70.179 | 81.448 | 2.13 | 0 | 0 |
| argumentationEvent | 3 | 37.541 | 47.609 | 50.339 | 64.042 | 65.868 | 1.19 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.011s (p5 29.95s, p95 32.92s, n=454) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 20m 
  - Evidence: 94h 20m: 69cdc907d385e3b94310f72d.jsonl[59] _id=69e7ac021724f0c9e2f91607 ts=2026-04-17T18:39:08.376Z -> 69cdc907d385e3b94310f72d.jsonl[979] _id=69e7ad0f1724f0c9e2f91b31 ts=2026-04-21T16:59:58.8770000Z; 48h 2m: 69cdc907d385e3b94310f72d.jsonl[1081] _id=69e7bad11724f0c9e2f95e35 ts=2026-04-21T17:58:41.0450000Z -> 69cdc907d385e3b94310f72d.jsonl[1090] _id=69ea5e691724f0c9e2fb057b ts=2026-04-23T18:01:13.2350000Z; 47h 7m: 69cdc907d385e3b94310f72d.jsonl[365] _id=69dd38867957a33870f29072 ts=2026-04-13T18:40:05.9320000Z -> 69cdc907d385e3b94310f72d.jsonl[367] _id=69dfcf2e7957a33870f40cff ts=2026-04-15T17:47:25.5190000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 126 interval(s) ≤ 0.003s..0.004s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f72d.jsonl[353] _id=69dd382a7957a33870f28dd4 ts=2026-04-13T18:38:33.9210000Z -> 69cdc907d385e3b94310f72d.jsonl[354] _id=69dd382a7957a33870f28dd8 ts=2026-04-13T18:38:33.9240000Z; 4ms: 69cdc907d385e3b94310f72d.jsonl[342] _id=69dd38027957a33870f28c7c ts=2026-04-13T18:37:53.7700000Z -> 69cdc907d385e3b94310f72d.jsonl[343] _id=69dd38027957a33870f28c7e ts=2026-04-13T18:37:53.7740000Z; 4ms: 69cdc907d385e3b94310f72d.jsonl[755] _id=69e271eb1724f0c9e2f749e0 ts=2026-04-17T17:46:18.9530000Z -> 69cdc907d385e3b94310f72d.jsonl[751] _id=69e271eb1724f0c9e2f749e2 ts=2026-04-17T17:46:18.9570000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f72d.jsonl[61] _id=69e7ac021724f0c9e2f9160f ts=2026-04-17T18:40:22.558Z -> 69cdc907d385e3b94310f72d.jsonl[959] _id=69e7ac101724f0c9e2f9162b ts=2026-04-21T16:55:44.2190000Z; 47h 58m: 69cdc907d385e3b94310f72d.jsonl[1086] _id=69e7bb781724f0c9e2f96321 ts=2026-04-21T18:01:27.8600000Z -> 69cdc907d385e3b94310f72d.jsonl[1088] _id=69ea5e1a1724f0c9e2fb0459 ts=2026-04-23T17:59:54.0420000Z; 46h 18m: 69cdc907d385e3b94310f72d.jsonl[564] _id=69dfdae67957a33870f46069 ts=2026-04-15T18:37:26.1960000Z -> 69cdc907d385e3b94310f72d.jsonl[568] _id=69e266321724f0c9e2f722b6 ts=2026-04-17T16:56:17.7490000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72d.jsonl[955] _id=69e27cf21724f0c9e2f7839e ts=2026-04-17T18:33:22.3610000Z -> 69cdc907d385e3b94310f72d.jsonl[956] _id=69e7abfb1724f0c9e2f915ad ts=2026-04-17T18:33:22.361Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 38m 
  - Evidence: 94h 38m: 69cdc907d385e3b94310f72d.jsonl[931] _id=69e27ac81724f0c9e2f77cca ts=2026-04-17T18:24:07.9530000Z -> 69cdc907d385e3b94310f72d.jsonl[988] _id=69e7adb71724f0c9e2f92011 ts=2026-04-21T17:02:46.6520000Z; 46h 42m: 69cdc907d385e3b94310f72d.jsonl[493] _id=69dfd7367957a33870f44259 ts=2026-04-15T18:21:41.3770000Z -> 69cdc907d385e3b94310f72d.jsonl[615] _id=69e2681e1724f0c9e2f731ea ts=2026-04-17T17:04:29.9980000Z; 1h 16m: 69cdc907d385e3b94310f72d.jsonl[621] _id=69e268211724f0c9e2f73206 ts=2026-04-17T17:04:32.9660000Z -> 69cdc907d385e3b94310f72d.jsonl[921] _id=69e27a1d1724f0c9e2f779aa ts=2026-04-17T18:21:16.9670000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 58m 
  - Evidence: 95h 58m: 69cdc907d385e3b94310f72d.jsonl[782] _id=69e275251724f0c9e2f75f5b ts=2026-04-17T18:00:04.7610000Z -> 69cdc907d385e3b94310f72d.jsonl[1077] _id=69e7bac41724f0c9e2f95dbf ts=2026-04-21T17:58:28.5070000Z; 47h 15m: 69cdc907d385e3b94310f72d.jsonl[554] _id=69dfd9bc7957a33870f45471 ts=2026-04-15T18:32:27.5390000Z -> 69cdc907d385e3b94310f72d.jsonl[769] _id=69e2723a1724f0c9e2f74c0c ts=2026-04-17T17:47:37.8270000Z; 31m 2s: 69cdc907d385e3b94310f72d.jsonl[436] _id=69dfd26f7957a33870f42534 ts=2026-04-15T18:01:18.8980000Z -> 69cdc907d385e3b94310f72d.jsonl[553] _id=69dfd9b57957a33870f45435 ts=2026-04-15T18:32:21.1940000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 18m 
  - Evidence: 94h 18m: 69cdc907d385e3b94310f72d.jsonl[43] _id=69e7abfe1724f0c9e2f915db ts=2026-04-17T18:37:31.024Z -> 69cdc907d385e3b94310f72d.jsonl[62] _id=69e7ac131724f0c9e2f9162f ts=2026-04-21T16:55:47.1740000Z; 48h 9m: 69cdc907d385e3b94310f72d.jsonl[1047] _id=69e7b8cb1724f0c9e2f950ed ts=2026-04-21T17:50:02.9760000Z -> 69cdc907d385e3b94310f72d.jsonl[1089] _id=69ea5e1b1724f0c9e2fb045b ts=2026-04-23T17:59:54.7010000Z; 47h 9m: 69cdc907d385e3b94310f72d.jsonl[15] _id=69dd38697957a33870f28f9a ts=2026-04-13T18:39:37.1050000Z -> 69cdc907d385e3b94310f72d.jsonl[377] _id=69dfcfaa7957a33870f40ffb ts=2026-04-15T17:49:30.2600000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.004s..0.018s shown 
  - Evidence: 4ms: 69cdc907d385e3b94310f72d.jsonl[285] _id=69dd36b87957a33870f2847e ts=2026-04-13T18:32:23.7000000Z -> 69cdc907d385e3b94310f72d.jsonl[9] _id=69dd36b87957a33870f28480 ts=2026-04-13T18:32:23.7040000Z; 11ms: 69cdc907d385e3b94310f72d.jsonl[127] _id=69dd2f447957a33870f2521a ts=2026-04-13T18:00:35.6430000Z -> 69cdc907d385e3b94310f72d.jsonl[128] _id=69dd2f447957a33870f2521e ts=2026-04-13T18:00:35.6540000Z; 18ms: 69cdc907d385e3b94310f72d.jsonl[157] _id=69dd30657957a33870f258a0 ts=2026-04-13T18:05:24.4870000Z -> 69cdc907d385e3b94310f72d.jsonl[158] _id=69dd30657957a33870f258a2 ts=2026-04-13T18:05:24.5050000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc907d385e3b94310f72d.jsonl:69cdc907d385e3b94310f72d, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f72d.jsonl[493] _id=69dfd7367957a33870f44259 ts=2026-04-15T18:21:41.3770000Z`; `69cdc907d385e3b94310f72d.jsonl[621] _id=69e268211724f0c9e2f73206 ts=2026-04-17T17:04:32.9660000Z`; `69cdc907d385e3b94310f72d.jsonl[931] _id=69e27ac81724f0c9e2f77cca ts=2026-04-17T18:24:07.9530000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f72d.jsonl[1018] _id=69e7b6591724f0c9e2f93fdb ts=2026-04-21T17:39:36.7360000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 56 unmatched 'DialogueStartEvent' (totals: 102 start, 46 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 5 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 8 unmatched 'questActiveEvent' (totals: 18 start, 10 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.70s, min -339721.11s, max -0.08s over 1097 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72d\coverage.yaml

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
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
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
  - Observed: 26 records 
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

### `DialogueEvent` — 567 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (336); Unit 1 Dev (196); Unit 3 Dev (35)
- **eventKey:** present on 419 of 567 records
- **Intervals:** median 4.66s (p5 0.01s / p95 109.79s, n=566)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x419; [conversationId, dialogueEventType] x148
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 567/567 records)
    numeric range 10 .. 70 (20 unique)
data.dialogueEventType  (string, 567/567 records)
    "DialogueNodeEvent"  x419
    "DialogueStartEvent"  x102
    "DialogueFinishEvent"  x46
data.nodeId  (number, 419/567 records)
    numeric range 0 .. 286 (126 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 457 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (324); Unit 1 Dev (96); Unit 3 Dev (37)
- **Intervals:** median 30.01s (p5 29.95s / p95 32.92s, n=454)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 457/457 records)
data.position.x  (number, 457/457 records)
    numeric range -23.1044 .. 1440.08 (232 unique)
data.position.y  (number, 457/457 records)
    numeric range -73.3627 .. 159.997 (167 unique)
data.position.z  (number, 457/457 records)
    numeric range -121.342 .. 1797.71 (232 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 28 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 1 Dev (12); Unit 3 Dev (2)
- **eventKey:** present on 28 of 28 records
- **Intervals:** median 292.50s (p5 0.01s / p95 172312.15s, n=27)
- **`data` key-set variants:** [questEventType, questID, questName] x18; [questEventType, questID, questName, questSuccessOrFailure] x10
- **Fields under `data`:**

```text
data.questEventType  (string, 28/28 records)
    "questActiveEvent"  x18
    "questFinishEvent"  x10
data.questID  (string, 28/28 records)
    "21"  x4
    "24"  x4
    "22"  x3
    "23"  x3
    "16"  x2
    "28"  x2
    "29"  x2
    "31"  x2
    "32"  x2
    "33"  x2
    "34"  x2
data.questName  (string, 28/28 records)
    "Escape the Ruin"  x4
    "Investigate the Temple"  x4
    "Foraged Forging"  x3
    "Getting the Band Back Together"  x3
    "Defend the Expedition"  x2
    "Gear Up"  x2
    "Getting Your Space Legs"  x2
    "Info and Intros"  x2
    "Supply Run"  x2
    "TK, Reporting In!"  x2
    "What Was That?"  x2
data.questSuccessOrFailure  (string, 10/28 records)
    "Succeeded"  x10
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 26 records

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (2)
- **Intervals:** median 15.93s (p5 1.13s / p95 136460.69s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "MapCloseEvent"  x13
    "MapOpenEvent"  x13
data.featureUsed  (string, 26/26 records)
    "Map"  x26
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8)
- **Intervals:** median 2210.08s (p5 2.99s / p95 288953.68s, n=7)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Started"  x5
    "Finished"  x3
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x8
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationNodeEvent` — 6 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (6)
- **Intervals:** median 15.97s (p5 5.75s / p95 70.18s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationNodeAdd"  x6
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 6/6 records)
    "1"  x2
    "I"  x2
    "A"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 4 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 47.61s (p5 38.55s / p95 64.04s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationSessionClose"  x2
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 4/4 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
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
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*