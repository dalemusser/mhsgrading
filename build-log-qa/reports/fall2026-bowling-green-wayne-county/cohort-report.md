# Per-user build-log QA — fall2026-bowling-green-wayne-county

*Generated 2026-10-25 by `build-log-qa/scripts/audit_per_user.py`; the interpretation lives in `README.md` next to this file.*

## 1. Scope

- Export: `playthrough-logs-and-results/fall2026-bowling-green-wayne-county/stratalog_BowlingGreen_WayneCounty.jsonl` — 1,979,541 records, 218 user_ids.
- Baseline: `build-log-qa/reports/09-23-26` (the newest internal playthrough audit).
- Each user was audited with the unchanged weekly pipeline and an evidence-based coverage manifest (`users/<id>/coverage.yaml`).

## 2. Verdicts

| cohort / roster | users | logging design | A - ready | B - usable with handling | C - partly usable | D - too little data |
|---|---|---|---|---|---|---|
| spring-2026 (accounts created 2026-04-02) | 80 | reduced (older build): 80 | 42 | 32 | 5 | 1 |
| fall-2026 (accounts created 2026-09-27) | 78 | current: 78 | 62 | 13 | 0 | 3 |
| fall-2026 (accounts created 2026-09-11) | 60 | current: 60 | 10 | 44 | 6 | 0 |

## 3. Builds in the export

| build | users | records | envelope recs | sessions | late >5s | late >1d | max delay h | stale-risk % | dlg keyed | dlg mismatch | seq expected | seq missing | resends | recovered | dup puzzle | dup other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 20260401-10923 | 80 | 118380 | 0 | 0 | 1730 | 717 | 94.75 | 1.46 | 54202 | 1407 | 0 | 0 | 0 | 0 | 0 | 2 |
| 20260408-10923 | 78 | 65951 | 0 | 0 | 1019 | 61 | 94.37 | 1.55 | 32861 | 1243 | 0 | 0 | 0 | 0 | 0 | 5 |
| 20260914- | 132 | 853857 | 0 | 0 | 40577 | 13529 | 287.75 | 4.75 | 72919 | 3392 | 0 | 0 | 0 | 106 | 17699 | 93 |
| 20261005-12466 | 117 | 878004 | 878004 | 1107 | 16540 | 41 | 146.09 | 0.0 | 86862 | 0 | 877884 | 0 | 120 | 2272 | 6254 | 1803 |
| 20261016- | 40 | 62902 | 62902 | 108 | 1498 | 10 | 68.93 | 0.0 | 7497 | 0 | 63172 | 278 | 8 | 1337 | 0 | 136 |

## 4. WARNING/FAIL findings by prevalence

`in baseline` = the same finding (status, category, event, field, summary) was raised for the baseline playthrough. Regression-category findings compare the user with the baseline playthrough, so they are about how the student played, not about logging defects. For absent-event (coverage) findings, `fall: unit done` counts the fall users who finished (EndOfUnit) a unit the event belongs to — only those can point at a logging gap rather than unreached content.

| in baseline | fall users | fall: unit done | spring users | status | category | event | field | summary |
|---|---|---|---|---|---|---|---|---|
| NO - new | 101 |  | 42 | WARNING | temporal |  |  | records without a parseable client timestamp |
| NO - new | 94 |  | 31 | WARNING | sequence | questEvent | questEventType | quest lifecycle: finish without preceding start |
| NO - new | 45 |  | 15 | WARNING | schema | questEvent | eventKey | eventKey does not match its documented format |
| NO - new | 42 |  | 16 | WARNING | duplicates | crash |  | exact duplicate records (same timestamp, scene and data) |
| NO - new | 35 |  | 11 | WARNING | sequence | argumentationEvent | actionType | argumentation session: repeated open with no intervening close |
| NO - new | 30 | 25 | 79 | WARNING | coverage | chatEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 29 | 0 | 28 | WARNING | coverage | TerasGardenBox |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 18 | 0 | 35 | WARNING | coverage | SolarStillDesignEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 12 |  | 28 | WARNING | sequence | Soil Key Puzzle | Soil Key Puzzle Status | puzzle start/finish: repeated open with no intervening close |
| NO - new | 12 | 7 | 15 | WARNING | coverage | argumentationToolEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 12 |  | 1 | WARNING | temporal |  |  | single event attributed to a different scene between two runs of the same scene |
| NO - new | 12 |  | 0 | WARNING | sequence | DaniEvent | actionType | tool open/close: repeated open with no intervening close |
| NO - new | 10 | 0 | 10 | WARNING | coverage | soilMachine |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 9 |  | 0 | WARNING | sequence | DaniEvent | actionType | tool open/close: close without preceding open |
| NO - new | 9 |  | 0 | WARNING | sequence | TopographicMapEvent | actionType | map open/close: close without preceding open |
| NO - new | 5 | 0 | 2 | WARNING | coverage | EndOfUnit |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 4 | 0 | 80 | WARNING | coverage | argumentationAnswerEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 4 | 0 | 0 | WARNING | coverage | argumentationEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 4 | 0 | 0 | WARNING | coverage | argumentationNodeEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 3 | 0 | 80 | WARNING | coverage | gameWindowUnfocusEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 3 | 0 | 10 | WARNING | coverage | TopographicMapEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 2 |  | 56 | WARNING | sequence | argumentationToolEvent | actionType | backing-info panel: close without preceding open |
| NO - new | 2 |  | 4 | WARNING | sequence | Soil Key Puzzle | Soil Key Puzzle Status | puzzle start/finish: close without preceding open |
| NO - new | 2 |  | 2 | WARNING | duplicates | PlayerPositionEvent |  | exact duplicate records (same timestamp, scene and data) |
| NO - new | 2 | 0 | 2 | WARNING | coverage | WaterChamberEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 1 |  | 78 | WARNING | cross-event |  |  | Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found |
| NO - new | 1 | 0 | 0 | WARNING | coverage | Soil Key Puzzle |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 1 |  | 0 | WARNING | sequence | chatEvent | actionType | chat open/close: repeated open with no intervening close |
| NO - new | 0 | 0 | 80 | WARNING | coverage | DEBUGMenu |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 0 | 0 | 80 | WARNING | coverage | InputEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 0 | 0 | 80 | WARNING | coverage | ObjectInterEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 0 | 0 | 80 | WARNING | coverage | gameStartEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 0 | 0 | 80 | WARNING | coverage | gameWindowFocusEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 0 |  | 80 | WARNING | frequency | PlayerPositionEvent |  | continuous cadence differs from expectation |
| NO - new | 0 | 0 | 79 | WARNING | coverage | PuzzlePieceVisibleEvent |  | expected event type absent although its content was played — possible logging failure |
| NO - new | 0 |  | 70 | WARNING | cross-event |  |  | waypoint use implies the topographic map was opened: expected corroborating events not found |
| NO - new | 0 |  | 70 | WARNING | schema |  |  | eventType name variants that differ only in spelling/case |
| NO - new | 0 |  | 24 | WARNING | schema | TerasGardenBox |  | field-name variants that differ only in spelling/case |
| NO - new | 0 |  | 2 | WARNING | duplicates | DialogueEvent |  | exact duplicate records (same timestamp, scene and data) |
| NO - new | 0 |  | 1 | WARNING | duplicates | argumentationToolEvent |  | exact duplicate records (same timestamp, scene and data) |
| yes | 138 |  | 0 | WARNING | schema | gameStartEvent | data.<empty> | field name is an empty string |
| yes | 138 |  | 0 | WARNING | schema | gameWindowFocusEvent | data.<empty> | field name is an empty string |
| yes | 135 |  | 78 | WARNING | sequence | DialogueEvent | dialogueEventType | dialogue lifecycle: finish without preceding start |
| yes | 135 |  | 0 | WARNING | duplicates | PuzzlePieceVisibleEvent |  | exact duplicate records (same timestamp, scene and data) |
| yes | 135 |  | 0 | WARNING | schema | gameWindowUnfocusEvent | data.<empty> | field name is an empty string |
| yes | 135 |  | 0 | WARNING | sequence | PuzzlePieceVisibleEvent | actionType | piece visibility: repeated open with no intervening close |
| n/a (comparison with baseline) | 134 |  | 0 | WARNING | regression | argumentationAnswerEvent |  | median interval between records changed substantially |
| yes | 134 |  | 0 | WARNING | sequence | PuzzlePieceVisibleEvent | actionType | camera centering: repeated open with no intervening close |
| yes | 128 |  | 0 | WARNING | values | ObjectInterEvent | data.actionType | values that differ only in spelling/case |
| n/a (comparison with baseline) | 127 |  | 0 | WARNING | regression | gameWindowUnfocusEvent |  | median interval between records changed substantially |
| yes | 125 |  | 80 | WARNING | schema | DialogueEvent | eventKey | eventKey does not match its documented format |
| n/a (comparison with baseline) | 125 |  | 0 | WARNING | regression | gameWindowFocusEvent |  | median interval between records changed substantially |
| yes | 119 |  | 73 | WARNING | sequence | argumentationEvent | actionType | argumentation session: close without preceding open |
| yes | 116 |  | 0 | WARNING | duplicates | InputEvent |  | exact duplicate records (same timestamp, scene and data) |
| n/a (comparison with baseline) | 115 |  | 67 | WARNING | regression | EndOfUnit |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 110 |  | 0 | WARNING | regression | gameStartEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 103 |  | 64 | WARNING | regression | argumentationToolEvent |  | median interval between records changed substantially |
| yes | 101 |  | 0 | WARNING | sequence | argumentationNodeEvent | actionType | node hover: close without preceding open |
| n/a (comparison with baseline) | 100 |  | 49 | WARNING | regression | TopographicMapEvent |  | median interval between records changed substantially |
| yes | 93 |  | 0 | WARNING | sequence | PuzzlePieceVisibleEvent | actionType | piece visibility: close without preceding open |
| n/a (comparison with baseline) | 91 |  | 51 | WARNING | regression | soilMachine |  | median interval between records changed substantially |
| yes | 91 |  | 0 | WARNING | sequence | PuzzlePieceVisibleEvent | actionType | camera centering: close without preceding open |
| yes | 90 |  | 26 | WARNING | sequence | argumentationToolEvent | actionType | backing-info panel: repeated open with no intervening close |
| yes | 89 |  | 0 | WARNING | sequence | chatEvent | actionType | chat open/close: close without preceding open |
| n/a (comparison with baseline) | 75 |  | 0 | WARNING | regression | PuzzlePieceVisibleEvent |  | median interval between records changed substantially |
| yes | 71 |  | 0 | WARNING | sequence | TopographicMapEvent | actionType | map open/close: repeated open with no intervening close |
| n/a (comparison with baseline) | 69 |  | 0 | WARNING | regression | chatEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 67 |  | 80 | WARNING | regression | SolarStillDesignEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 55 |  | 0 | WARNING | regression | InputEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 54 |  | 70 | WARNING | regression | TopographicMapEvent |  | baseline field(s) absent this build |
| yes | 52 |  | 0 | WARNING | duplicates | questEvent |  | exact duplicate records (same timestamp, scene and data) |
| n/a (comparison with baseline) | 51 |  | 47 | WARNING | regression | WaterChamberEvent |  | event type present in baseline 09-23-26 but absent now |
| yes | 47 |  | 0 | WARNING | sequence | argumentationNodeEvent | actionType | node hover: repeated open with no intervening close |
| n/a (comparison with baseline) | 44 |  | 45 | WARNING | regression | TerasGardenBox |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 42 |  | 79 | WARNING | regression | Soil Key Puzzle |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 42 |  | 0 | WARNING | regression | ObjectInterEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 39 |  | 0 | WARNING | regression | DEBUGMenu |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 38 |  | 30 | WARNING | regression | WaterChamberEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 37 |  | 18 | WARNING | regression | TerasGardenBox |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 31 |  | 23 | WARNING | regression | argumentationEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 30 |  | 80 | WARNING | regression | chatEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 25 |  | 27 | WARNING | regression | soilMachine |  | event type present in baseline 09-23-26 but absent now |
| yes | 16 | 12 | 80 | WARNING | coverage | DaniEvent |  | expected event type absent although its content was played — possible logging failure |
| n/a (comparison with baseline) | 12 |  | 15 | WARNING | regression | argumentationToolEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 9 |  | 0 | WARNING | regression | SolarStillDesignEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 7 |  | 0 | WARNING | regression | questEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 5 |  | 2 | WARNING | regression | EndOfUnit |  | event type present in baseline 09-23-26 but absent now |
| yes | 5 |  | 0 | WARNING | duplicates | ObjectInterEvent |  | exact duplicate records (same timestamp, scene and data) |
| n/a (comparison with baseline) | 4 |  | 80 | WARNING | regression | argumentationAnswerEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 4 |  | 1 | WARNING | regression | Soil Key Puzzle |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 4 |  | 0 | WARNING | regression | argumentationEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 4 |  | 0 | WARNING | regression | argumentationNodeEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 3 |  | 80 | WARNING | regression | PuzzlePieceVisibleEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 3 |  | 80 | WARNING | regression | argumentationNodeEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 3 |  | 80 | WARNING | regression | gameWindowUnfocusEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 3 |  | 10 | WARNING | regression | TopographicMapEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 1 |  | 79 | WARNING | regression | Soil Key Puzzle |  | baseline field(s) absent this build |
| n/a (comparison with baseline) | 1 |  | 26 | WARNING | regression | DialogueEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 1 |  | 0 | WARNING | regression | questEvent |  | baseline field(s) absent this build |
| n/a (comparison with baseline) | 0 |  | 80 | WARNING | regression | DEBUGMenu |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 0 |  | 80 | WARNING | regression | InputEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 0 |  | 80 | WARNING | regression | ObjectInterEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 0 |  | 80 | WARNING | regression | PlayerPositionEvent |  | median interval between records changed substantially |
| n/a (comparison with baseline) | 0 |  | 80 | WARNING | regression | gameStartEvent |  | event type present in baseline 09-23-26 but absent now |
| n/a (comparison with baseline) | 0 |  | 80 | WARNING | regression | gameWindowFocusEvent |  | event type present in baseline 09-23-26 but absent now |

## 5. Per-user table

Columns: active min = minutes with no gap > 5 min between records; stale % = share of the student's records that are legacy-envelope uploads more than 5 s late; envelope % = share on builds with the session_id/seq envelope; seq miss = sequence numbers missing inside envelope sessions; FAIL/WARN = pipeline findings (WARN new = not in baseline, regression excluded).

| user_id | cohort | roster | design | builds | envelope % | records | active min | days | units seen | units ended | stale % | seq miss | dlg mism | crash | FAIL | WARN | WARN new | verdict | reasons |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6aa413b141b41dbac0c7f1ed | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 20942 | 333.3 | 9 | 1,2,3,4,5 | 1,3 | 3.89 | 0 | 40 | 3 | 0 | 35 | 3 | B - usable with handling | 814 records (3.89% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1ee | fall-2026 | 2026-09-11 | current | 2 | 14.8 | 11153 | 405.5 | 11 | 1,2,3,4,5 | 1,4 | 4.69 | 0 | 80 | 4 | 0 | 37 | 4 | B - usable with handling | 523 records (4.69% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1ef | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 13186 | 292.3 | 7 | 1,2,3,4,5 | 1,3,4,5 | 4.02 | 0 | 26 | 1 | 0 | 31 | 4 | B - usable with handling | 530 records (4.02% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1f0 | fall-2026 | 2026-09-11 | current | 2 | 8.7 | 16825 | 402.8 | 10 | 1,2,3,4,5 | 1,3,4 | 5.17 | 0 | 39 | 7 | 0 | 39 | 6 | B - usable with handling | 870 records (5.17% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1f1 | fall-2026 | 2026-09-11 | current | 2 | 15.5 | 9198 | 366.6 | 9 | 1,2,3,4 |  | 15.46 | 0 | 97 | 9 | 0 | 42 | 12 | C - partly usable | 1421 records (15.46% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1f2 | fall-2026 | 2026-09-11 | current | 2 | 4.1 | 14845 | 381.7 | 10 | 1,2,3,4 | 1 | 0.13 | 0 | 17 | 0 | 0 | 28 | 2 | A - ready |  |
| 6aa413b141b41dbac0c7f1f3 | fall-2026 | 2026-09-11 | current | 2 | 16.9 | 10885 | 293.9 | 10 | 1,2,3,4 | 1 | 13.51 | 0 | 19 | 5 | 0 | 34 | 5 | C - partly usable | 1470 records (13.51% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1f4 | fall-2026 | 2026-09-11 | current | 2 | 23.3 | 6585 | 286.4 | 7 | 1,2 | 1 | 2.98 | 0 | 19 | 9 | 0 | 33 | 5 | B - usable with handling | 196 records (2.98% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1f5 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 14391 | 360.7 | 9 | 1,2,3,4,5 | 1,3,4,5 | 0.92 | 0 | 41 | 5 | 0 | 34 | 4 | A - ready |  |
| 6aa413b141b41dbac0c7f1f6 | fall-2026 | 2026-09-11 | current | 2 | 2.8 | 11094 | 346.6 | 10 | 1,2,3 | 1 | 3.14 | 0 | 16 | 7 | 0 | 33 | 4 | B - usable with handling | 348 records (3.14% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1f7 | fall-2026 | 2026-09-11 | current | 2 | 6.8 | 13178 | 323.9 | 9 | 1,2,3,4 | 1,3 | 0.85 | 0 | 25 | 1 | 0 | 33 | 5 | A - ready |  |
| 6aa413b141b41dbac0c7f1f8 | fall-2026 | 2026-09-11 | current | 2 | 16.4 | 11047 | 373.9 | 10 | 1,2,3 | 1 | 5.94 | 0 | 20 | 6 | 0 | 34 | 4 | B - usable with handling | 656 records (5.94% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1f9 | fall-2026 | 2026-09-11 | current | 2 | 20.1 | 16646 | 492.7 | 10 | 1,2,3,4,5 | 1,4,5 | 0.77 | 0 | 34 | 3 | 0 | 36 | 4 | A - ready |  |
| 6aa413b141b41dbac0c7f1fa | fall-2026 | 2026-09-11 | current | 2 | 8.3 | 16770 | 382.9 | 10 | 1,2,3,4 | 1,3 | 1.89 | 0 | 25 | 3 | 0 | 34 | 5 | B - usable with handling | 317 records (1.89% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1fb | fall-2026 | 2026-09-11 | current | 2 | 6.0 | 9188 | 289.2 | 8 | 1,2,3 |  | 3.47 | 0 | 11 | 5 | 0 | 38 | 7 | B - usable with handling | 319 records (3.47% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1fc | fall-2026 | 2026-09-11 | current | 2 | 13.9 | 9193 | 293.9 | 8 | 1,2,3,4 | 1 | 3.09 | 0 | 22 | 3 | 0 | 35 | 6 | B - usable with handling | 284 records (3.09% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa413b141b41dbac0c7f1fd | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 12964 | 336.9 | 8 | 1,2,3,4,5 | 1,3,4,5 | 3.19 | 0 | 52 | 3 | 0 | 31 | 4 | B - usable with handling | 414 records (3.19% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f225 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 18827 | 382.1 | 8 | 1,2,3,4,5 | 1 | 31.87 | 0 | 325 | 4 | 0 | 35 | 9 | C - partly usable | 5998 records (31.87% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f226 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 10909 | 334.9 | 8 | 1,2,3,4,5 | 1,2,3,5 | 1.79 | 0 | 25 | 6 | 0 | 31 | 3 | B - usable with handling | 195 records (1.79% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f227 | fall-2026 | 2026-09-11 | current | 2 | 11.3 | 12061 | 376.3 | 9 | 1,2,3,4,5 | 1,3,5 | 0.71 | 0 | 24 | 6 | 0 | 38 | 3 | B - usable with handling | 1 WASM runtime crash(es) |
| 6aa4140b41b41dbac0c7f228 | fall-2026 | 2026-09-11 | current | 2 | 11.5 | 15185 | 406.1 | 10 | 1,2,3,4,5 | 1,3,4,5 | 1.86 | 0 | 40 | 6 | 0 | 38 | 5 | B - usable with handling | 283 records (1.86% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f229 | fall-2026 | 2026-09-11 | current | 2 | 3.5 | 17722 | 380.2 | 10 | 1,2,3,4 | 3 | 1.21 | 0 | 24 | 6 | 0 | 26 | 5 | B - usable with handling | 215 records (1.21% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f22a | fall-2026 | 2026-09-11 | current | 2 | 12.8 | 16646 | 460.9 | 10 | 1,2,3,4 | 1,3 | 2.6 | 0 | 20 | 8 | 0 | 39 | 8 | B - usable with handling | 432 records (2.6% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f22b | fall-2026 | 2026-09-11 | current | 2 | 3.9 | 15301 | 417.8 | 10 | 1,2,3,4,5 | 1,5 | 0.67 | 0 | 33 | 6 | 0 | 35 | 6 | A - ready |  |
| 6aa4140b41b41dbac0c7f22c | fall-2026 | 2026-09-11 | current | 2 | 13.3 | 14167 | 444.6 | 10 | 1,2,3,4,5 | 1,3,4,5 | 1.15 | 0 | 44 | 4 | 0 | 34 | 4 | B - usable with handling | 163 records (1.15% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f22d | fall-2026 | 2026-09-11 | current | 2 | 9.2 | 13698 | 418.4 | 10 | 1,2,3,4 | 1,3 | 2.39 | 0 | 44 | 0 | 0 | 37 | 4 | B - usable with handling | 327 records (2.39% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f22e | fall-2026 | 2026-09-11 | current | 2 | 6.0 | 15769 | 301.7 | 8 | 1,2,3,4 | 1,3 | 0.88 | 0 | 24 | 2 | 0 | 32 | 3 | A - ready |  |
| 6aa4140b41b41dbac0c7f230 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 8432 | 255.8 | 7 | 1,2,3 | 1 | 2.73 | 0 | 18 | 7 | 0 | 30 | 6 | B - usable with handling | 230 records (2.73% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f231 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 17097 | 366.0 | 10 | 1,2,3,4,5 | 1,4,5 | 3.66 | 0 | 40 | 3 | 0 | 33 | 3 | B - usable with handling | 625 records (3.66% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f232 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 11074 | 330.5 | 9 | 1,2,3,4,5 | 1,3,4,5 | 2.08 | 0 | 30 | 4 | 0 | 34 | 5 | B - usable with handling | 230 records (2.08% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4140b41b41dbac0c7f233 | fall-2026 | 2026-09-11 | current | 2 | 0.4 | 10907 | 345.8 | 10 | 1,2,3,4 | 1,3 | 1.09 | 0 | 18 | 0 | 0 | 33 | 3 | B - usable with handling | 119 records (1.09% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f247 | fall-2026 | 2026-09-11 | current | 2 | 5.8 | 12089 | 328.6 | 10 | 1,2,3,4 | 1,3 | 29.36 | 0 | 128 | 4 | 0 | 39 | 8 | C - partly usable | 3548 records (29.36% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f248 | fall-2026 | 2026-09-11 | current | 2 | 12.8 | 9705 | 278.8 | 9 | 1,2,3,4 | 1 | 1.48 | 0 | 13 | 7 | 0 | 33 | 6 | B - usable with handling | 144 records (1.48% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f249 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 13792 | 332.3 | 9 | 1,2,3,4,5 | 1,3,4,5 | 4.78 | 0 | 38 | 3 | 0 | 32 | 4 | B - usable with handling | 659 records (4.78% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f24a | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 13820 | 442.9 | 9 | 1,2,3,4,5 | 1,3,4,5 | 4.99 | 0 | 116 | 8 | 0 | 33 | 6 | B - usable with handling | 689 records (4.99% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f24b | fall-2026 | 2026-09-11 | current | 2 | 17.3 | 17583 | 448.7 | 10 | 1,2,3,4,5 | 1,3,4,5 | 0.85 | 0 | 31 | 2 | 0 | 36 | 5 | A - ready |  |
| 6aa4142c41b41dbac0c7f24c | fall-2026 | 2026-09-11 | current | 2 | 8.6 | 9411 | 301.5 | 8 | 1,2,3,4,5 | 1,3,4 | 1.18 | 0 | 26 | 2 | 0 | 29 | 3 | B - usable with handling | 111 records (1.18% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f24d | fall-2026 | 2026-09-11 | current | 2 | 5.4 | 13126 | 364.6 | 10 | 1,2,3,4,5 | 1,4,5 | 0.99 | 0 | 15 | 4 | 0 | 35 | 5 | A - ready |  |
| 6aa4142c41b41dbac0c7f24e | fall-2026 | 2026-09-11 | current | 2 | 1.2 | 13604 | 337.7 | 10 | 1,2,3,4 | 1 | 2.58 | 0 | 20 | 4 | 0 | 33 | 5 | B - usable with handling | 351 records (2.58% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f24f | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 14185 | 337.3 | 9 | 1,2,3,4,5 | 1,3,4,5 | 1.17 | 0 | 46 | 2 | 0 | 36 | 5 | B - usable with handling | 166 records (1.17% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f250 | fall-2026 | 2026-09-11 | current | 2 | 14.8 | 22550 | 338.5 | 10 | 1,2,3 | 1 | 16.08 | 0 | 84 | 2 | 0 | 34 | 5 | C - partly usable | 3625 records (16.08% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f251 | fall-2026 | 2026-09-11 | current | 2 | 4.2 | 12960 | 375.6 | 10 | 1,2,3,4 | 1,3 | 4.73 | 0 | 29 | 1 | 0 | 31 | 4 | B - usable with handling | 613 records (4.73% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4142c41b41dbac0c7f252 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 17129 | 327.4 | 8 | 1,2,3,4 | 1,3 | 8.43 | 0 | 152 | 5 | 0 | 33 | 5 | B - usable with handling | 1443 records (8.43% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f261 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 14886 | 411.1 | 9 | 1,2,3,4,5 | 3,5 | 1.16 | 0 | 29 | 10 | 0 | 36 | 6 | B - usable with handling | 173 records (1.16% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f262 | fall-2026 | 2026-09-11 | current | 2 | 4.3 | 17920 | 409.6 | 9 | 1,2,3,4,5 | 1,3,5 | 4.24 | 0 | 28 | 2 | 0 | 35 | 3 | B - usable with handling | 759 records (4.24% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f263 | fall-2026 | 2026-09-11 | current | 2 | 5.6 | 9167 | 250.8 | 8 | 1,2,3,4 | 1,3 | 1.95 | 0 | 21 | 0 | 0 | 36 | 6 | B - usable with handling | 179 records (1.95% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f264 | fall-2026 | 2026-09-11 | current | 2 | 12.7 | 14756 | 491.0 | 10 | 1,2,3,4,5 | 1,3,4,5 | 0.92 | 0 | 22 | 7 | 0 | 36 | 6 | A - ready |  |
| 6aa4144c41b41dbac0c7f265 | fall-2026 | 2026-09-11 | current | 2 | 7.8 | 12603 | 345.4 | 10 | 1,2,3,4 | 1,3 | 7.88 | 0 | 96 | 0 | 0 | 36 | 5 | B - usable with handling | 993 records (7.88% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f266 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 5093 | 133.5 | 5 | 1,2 | 1 | 1.32 | 0 | 18 | 2 | 0 | 31 | 3 | B - usable with handling | 67 records (1.32% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f267 | fall-2026 | 2026-09-11 | current | 2 | 14.1 | 14259 | 450.1 | 10 | 1,2,3,4,5 | 3,5 | 13.96 | 0 | 126 | 4 | 0 | 32 | 3 | C - partly usable | 1990 records (13.96% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f268 | fall-2026 | 2026-09-11 | current | 2 | 11.0 | 12156 | 309.3 | 9 | 1,2,3,4,5 | 1,3,4 | 1.15 | 0 | 29 | 2 | 0 | 32 | 2 | B - usable with handling | 140 records (1.15% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f269 | fall-2026 | 2026-09-11 | current | 2 | 13.3 | 15021 | 407.0 | 10 | 1,2,3,4 | 1,3 | 1.94 | 0 | 20 | 3 | 0 | 38 | 5 | B - usable with handling | 292 records (1.94% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f26a | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 12294 | 283.0 | 6 | 1,2,3,4,5 | 1,3,4,5 | 1.05 | 0 | 45 | 6 | 0 | 37 | 4 | B - usable with handling | 129 records (1.05% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f26b | fall-2026 | 2026-09-11 | current | 2 | 13.0 | 13684 | 298.5 | 10 | 1,2,3,4,5 | 1 | 4.99 | 0 | 11 | 3 | 0 | 35 | 8 | B - usable with handling | 682 records (4.99% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f26c | fall-2026 | 2026-09-11 | current | 2 | 3.9 | 14692 | 475.3 | 10 | 1,2,3,4,5 | 1,2,3,5 | 1.33 | 0 | 43 | 2 | 0 | 34 | 4 | B - usable with handling | 196 records (1.33% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f26d | fall-2026 | 2026-09-11 | current | 2 | 1.8 | 15763 | 395.2 | 9 | 1,2,3,4,5 | 1,3,4,5 | 8.63 | 0 | 322 | 11 | 0 | 34 | 4 | B - usable with handling | 1359 records (8.63% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f26e | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 15052 | 342.9 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.9 | 0 | 37 | 0 | 0 | 35 | 5 | A - ready |  |
| 6aa4144c41b41dbac0c7f26f | fall-2026 | 2026-09-11 | current | 2 | 20.5 | 19670 | 437.1 | 10 | 1,2,3,4,5 | 3 | 2.28 | 0 | 39 | 4 | 0 | 35 | 6 | B - usable with handling | 449 records (2.28% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f270 | fall-2026 | 2026-09-11 | current | 1 | 0.0 | 13151 | 326.6 | 10 | 1,2,3,4,5 | 1,3,4,5 | 2.19 | 0 | 27 | 3 | 0 | 28 | 1 | B - usable with handling | 288 records (2.19% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6aa4144c41b41dbac0c7f271 | fall-2026 | 2026-09-11 | current | 2 | 9.9 | 13917 | 438.5 | 10 | 1,2,3,4,5 | 1,4 | 1.98 | 0 | 35 | 8 | 0 | 37 | 7 | B - usable with handling | 276 records (1.98% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a88e9a8420a1e6b56adf | fall-2026 | 2026-09-27 | current | 2 | 86.0 | 9707 | 269.1 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.71 | 0 | 7 | 0 | 0 | 28 | 0 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae0 | fall-2026 | 2026-09-27 | current | 3 | 97.5 | 17095 | 499.4 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 6 | 3 | 0 | 28 | 3 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae1 | fall-2026 | 2026-09-27 | current | 2 | 97.4 | 27385 | 389.8 | 7 | 1,2 | 1 | 0.0 | 0 | 0 | 5 | 0 | 25 | 3 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae2 | fall-2026 | 2026-09-27 | current | 3 | 94.7 | 11441 | 372.4 | 9 | 1,2,3,4,5 | 1,2,3,4 | 0.01 | 0 | 7 | 1 | 0 | 34 | 3 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae3 | fall-2026 | 2026-09-27 | current | 2 | 94.1 | 11850 | 380.0 | 7 | 1,2,3,4 | 1,2,3 | 0.01 | 0 | 7 | 6 | 0 | 33 | 4 | B - usable with handling | 1 WASM runtime crash(es) |
| 6ab9a88e9a8420a1e6b56ae4 | fall-2026 | 2026-09-27 | current | 3 | 89.5 | 10681 | 380.0 | 7 | 1,2,3,4,5 | 1,2,3,4 | 0.49 | 0 | 8 | 0 | 0 | 37 | 2 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae5 | fall-2026 | 2026-09-27 | current | 2 | 83.0 | 9349 | 298.4 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.57 | 0 | 7 | 0 | 0 | 32 | 0 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae6 | fall-2026 | 2026-09-27 | current | 2 | 93.6 | 12943 | 348.6 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 9 | 0 | 0 | 33 | 2 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae7 | fall-2026 | 2026-09-27 | current | 3 | 82.2 | 8501 | 334.4 | 6 | 1,2,3,4 | 1,2,3 | 0.87 | 0 | 7 | 0 | 0 | 33 | 2 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae8 | fall-2026 | 2026-09-27 | current | 3 | 96.5 | 16353 | 591.2 | 9 | 1,2,3,4,5 | 1,2,3,4 | 0.01 | 0 | 7 | 0 | 0 | 34 | 1 | A - ready |  |
| 6ab9a88e9a8420a1e6b56ae9 | fall-2026 | 2026-09-27 | current | 2 | 92.3 | 11687 | 325.1 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 7 | 4 | 0 | 32 | 3 | A - ready |  |
| 6ab9a88e9a8420a1e6b56aea | fall-2026 | 2026-09-27 | current | 2 | 95.8 | 11648 | 369.2 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.03 | 0 | 7 | 3 | 0 | 32 | 3 | A - ready |  |
| 6ab9a88e9a8420a1e6b56aeb | fall-2026 | 2026-09-27 | current | 2 | 97.2 | 11442 | 621.4 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 0 | 2 | 0 | 30 | 2 | B - usable with handling | 1 WASM runtime crash(es) |
| 6ab9a88e9a8420a1e6b56aec | fall-2026 | 2026-09-27 | current | 2 | 94.6 | 13764 | 486.6 | 8 | 1,2,3,4,5 | 1,2,3,4 | 0.01 | 0 | 7 | 1 | 0 | 33 | 3 | A - ready |  |
| 6ab9a88e9a8420a1e6b56aed | fall-2026 | 2026-09-27 | current | 2 | 85.1 | 14320 | 279.5 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.48 | 0 | 7 | 0 | 0 | 29 | 0 | A - ready |  |
| 6ab9a88e9a8420a1e6b56aee | fall-2026 | 2026-09-27 | current | 2 | 84.7 | 14819 | 272.9 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 2.28 | 0 | 7 | 0 | 0 | 33 | 2 | B - usable with handling | 338 records (2.28% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a8bc9a8420a1e6b56b01 | fall-2026 | 2026-09-27 | current | 2 | 90.2 | 17924 | 285.3 | 8 | 1,2,3,4 | 1,2,3 | 0.02 | 0 | 7 | 1 | 0 | 36 | 5 | A - ready |  |
| 6ab9a8bc9a8420a1e6b56b02 | fall-2026 | 2026-09-27 | current | 1 | 0.0 | 328 | 12.9 | 1 | 1 |  | 0.0 | 0 | 0 | 0 | 0 | 28 | 8 | D - too little data | 12.9 active minutes / 328 records, unit(s) 1 |
| 6ab9a8bc9a8420a1e6b56b03 | fall-2026 | 2026-09-27 | current | 3 | 80.4 | 12112 | 308.4 | 8 | 1,2,3,4 | 1,3,4 | 0.97 | 0 | 7 | 1 | 0 | 32 | 4 | A - ready |  |
| 6ab9a8bc9a8420a1e6b56b04 | fall-2026 | 2026-09-27 | current | 1 | 0.0 | 346 | 14.8 | 1 | 1 |  | 0.0 | 0 | 2 | 0 | 0 | 28 | 8 | D - too little data | 14.8 active minutes / 346 records, unit(s) 1 |
| 6ab9a8bc9a8420a1e6b56b05 | fall-2026 | 2026-09-27 | current | 2 | 94.0 | 14526 | 471.4 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 5 | 2 | 0 | 37 | 5 | A - ready |  |
| 6ab9a8bc9a8420a1e6b56b06 | fall-2026 | 2026-09-27 | current | 2 | 90.8 | 12405 | 302.0 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.02 | 0 | 13 | 0 | 0 | 30 | 1 | A - ready |  |
| 6ab9a8bc9a8420a1e6b56b07 | fall-2026 | 2026-09-27 | current | 2 | 82.7 | 12085 | 352.2 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.32 | 0 | 9 | 0 | 0 | 35 | 3 | A - ready |  |
| 6ab9a8bc9a8420a1e6b56b08 | fall-2026 | 2026-09-27 | current | 2 | 83.0 | 9770 | 276.8 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.68 | 0 | 7 | 2 | 0 | 37 | 3 | B - usable with handling | 1 WASM runtime crash(es) |
| 6ab9a8bc9a8420a1e6b56b09 | fall-2026 | 2026-09-27 | current | 2 | 85.2 | 10004 | 281.8 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.42 | 0 | 7 | 1 | 0 | 32 | 3 | A - ready |  |
| 6ab9a8bc9a8420a1e6b56b0a | fall-2026 | 2026-09-27 | current | 2 | 79.6 | 11229 | 276.0 | 8 | 1,2,3,4 | 1,2,3 | 0.38 | 0 | 8 | 1 | 0 | 36 | 3 | B - usable with handling | 1 WASM runtime crash(es) |
| 6ab9a8bc9a8420a1e6b56b0b | fall-2026 | 2026-09-27 | current | 2 | 85.2 | 12217 | 242.9 | 8 | 1,2,3,4 | 2,3 | 0.02 | 0 | 9 | 4 | 0 | 32 | 4 | A - ready |  |
| 6ab9a8bc9a8420a1e6b56b0c | fall-2026 | 2026-09-27 | current | 3 | 93.3 | 13529 | 451.2 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 3 | 1 | 0 | 32 | 2 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b1c | fall-2026 | 2026-09-27 | current | 2 | 86.2 | 15261 | 338.2 | 10 | 1,2,3,4,5 | 1,2,3,4,5 | 0.48 | 0 | 9 | 0 | 0 | 30 | 1 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b1d | fall-2026 | 2026-09-27 | current | 2 | 92.7 | 11644 | 377.0 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 9 | 0 | 0 | 30 | 0 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b1e | fall-2026 | 2026-09-27 | current | 2 | 82.0 | 10124 | 321.1 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.53 | 0 | 8 | 1 | 0 | 36 | 2 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b1f | fall-2026 | 2026-09-27 | current | 2 | 93.1 | 15417 | 424.9 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 8 | 1 | 0 | 33 | 3 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b20 | fall-2026 | 2026-09-27 | current | 2 | 85.4 | 15968 | 311.2 | 7 | 1,2,3,4,5 | 1,2,3,4 | 1.42 | 0 | 8 | 0 | 0 | 28 | 2 | B - usable with handling | 227 records (1.42% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a8e69a8420a1e6b56b21 | fall-2026 | 2026-09-27 | current | 2 | 83.8 | 10723 | 337.3 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.73 | 0 | 7 | 0 | 0 | 30 | 1 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b22 | fall-2026 | 2026-09-27 | current | 3 | 85.9 | 10438 | 327.4 | 9 | 1,2,3,4 | 1,2,3 | 1.11 | 0 | 7 | 1 | 0 | 32 | 3 | B - usable with handling | 116 records (1.11% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a8e69a8420a1e6b56b23 | fall-2026 | 2026-09-27 | current | 2 | 82.7 | 15851 | 311.5 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.21 | 0 | 9 | 0 | 0 | 34 | 1 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b24 | fall-2026 | 2026-09-27 | current | 2 | 81.9 | 9601 | 302.6 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 1.06 | 0 | 7 | 0 | 0 | 32 | 0 | B - usable with handling | 102 records (1.06% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a8e69a8420a1e6b56b25 | fall-2026 | 2026-09-27 | current | 3 | 83.0 | 13148 | 361.3 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.54 | 0 | 8 | 1 | 0 | 35 | 3 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b26 | fall-2026 | 2026-09-27 | current | 2 | 81.0 | 13748 | 290.7 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 1.15 | 0 | 7 | 0 | 0 | 32 | 1 | B - usable with handling | 158 records (1.15% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a8e69a8420a1e6b56b27 | fall-2026 | 2026-09-27 | current | 2 | 100.0 | 13115 | 370.0 | 7 | 1,2,3,4,5 | 1,2,3,4 | 0.0 | 0 | 0 | 1 | 0 | 34 | 4 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b28 | fall-2026 | 2026-09-27 | current | 2 | 80.2 | 13232 | 308.2 | 8 | 1,2,3,4,5 | 1,2,3,4 | 0.23 | 0 | 7 | 0 | 0 | 33 | 2 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b29 | fall-2026 | 2026-09-27 | current | 2 | 79.4 | 10583 | 334.6 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.52 | 0 | 8 | 1 | 0 | 38 | 3 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b2a | fall-2026 | 2026-09-27 | current | 3 | 93.5 | 12024 | 452.3 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.04 | 0 | 10 | 2 | 0 | 30 | 2 | A - ready |  |
| 6ab9a8e69a8420a1e6b56b2b | fall-2026 | 2026-09-27 | current | 3 | 79.7 | 13813 | 340.0 | 9 | 1,2,3,4 | 1,2,3 | 0.62 | 0 | 8 | 1 | 0 | 35 | 3 | A - ready |  |
| 6ab9a9279a8420a1e6b56b6d | fall-2026 | 2026-09-27 | current | 3 | 93.7 | 15272 | 455.9 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 7 | 0 | 0 | 31 | 3 | A - ready |  |
| 6ab9a9279a8420a1e6b56b6e | fall-2026 | 2026-09-27 | current | 3 | 88.1 | 10422 | 250.5 | 7 | 1,2,3,4 | 1,2,3 | 0.91 | 0 | 7 | 0 | 0 | 30 | 3 | A - ready |  |
| 6ab9a9279a8420a1e6b56b6f | fall-2026 | 2026-09-27 | current | 3 | 90.6 | 5880 | 169.5 | 7 | 1,2 | 1 | 0.05 | 0 | 5 | 1 | 0 | 27 | 2 | A - ready |  |
| 6ab9a9279a8420a1e6b56b70 | fall-2026 | 2026-09-27 | current | 3 | 86.1 | 21743 | 355.9 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.92 | 0 | 7 | 0 | 0 | 33 | 2 | A - ready |  |
| 6ab9a9279a8420a1e6b56b71 | fall-2026 | 2026-09-27 | current | 3 | 85.4 | 14091 | 351.1 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.34 | 0 | 7 | 0 | 0 | 32 | 2 | A - ready |  |
| 6ab9a9279a8420a1e6b56b72 | fall-2026 | 2026-09-27 | current | 3 | 92.4 | 17132 | 486.8 | 10 | 1,2,3,4,5 | 1,3,4 | 0.08 | 0 | 7 | 5 | 0 | 34 | 4 | A - ready |  |
| 6ab9a9279a8420a1e6b56b73 | fall-2026 | 2026-09-27 | current | 3 | 92.4 | 15198 | 490.1 | 7 | 1,2,3,4,5 | 1,2,3,4 | 1.2 | 0 | 7 | 1 | 0 | 36 | 2 | B - usable with handling | 183 records (1.2% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a9279a8420a1e6b56b74 | fall-2026 | 2026-09-27 | current | 3 | 97.5 | 8646 | 291.1 | 7 | 1,2,3 | 1 | 0.01 | 0 | 1 | 1 | 0 | 32 | 1 | A - ready |  |
| 6ab9a9279a8420a1e6b56b75 | fall-2026 | 2026-09-27 | current | 3 | 88.5 | 13066 | 399.3 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 1.01 | 0 | 9 | 2 | 0 | 33 | 3 | B - usable with handling | 132 records (1.01% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a9279a8420a1e6b56b76 | fall-2026 | 2026-09-27 | current | 2 | 91.7 | 13042 | 412.9 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 7 | 0 | 0 | 32 | 2 | A - ready |  |
| 6ab9a9279a8420a1e6b56b77 | fall-2026 | 2026-09-27 | current | 3 | 95.0 | 14969 | 481.6 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 5 | 2 | 0 | 31 | 1 | A - ready |  |
| 6ab9a9279a8420a1e6b56b78 | fall-2026 | 2026-09-27 | current | 3 | 88.9 | 13603 | 333.7 | 8 | 1,2,3,4,5 | 1,2,3,4 | 0.64 | 0 | 7 | 2 | 0 | 36 | 5 | A - ready |  |
| 6ab9a9279a8420a1e6b56b79 | fall-2026 | 2026-09-27 | current | 3 | 95.8 | 12010 | 382.5 | 6 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 7 | 0 | 0 | 29 | 1 | A - ready |  |
| 6ab9a9279a8420a1e6b56b7a | fall-2026 | 2026-09-27 | current | 3 | 95.0 | 14592 | 498.3 | 7 | 1,2,3,4,5 | 1,2,3,4 | 0.01 | 0 | 7 | 0 | 0 | 35 | 4 | A - ready |  |
| 6ab9a9279a8420a1e6b56b7b | fall-2026 | 2026-09-27 | current | 2 | 93.8 | 15370 | 428.5 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 7 | 1 | 0 | 33 | 4 | A - ready |  |
| 6ab9a9279a8420a1e6b56b7c | fall-2026 | 2026-09-27 | current | 3 | 92.0 | 15121 | 395.1 | 9 | 1,2,3,4 | 1,2,3,4 | 0.04 | 0 | 10 | 1 | 0 | 31 | 2 | A - ready |  |
| 6ab9a9279a8420a1e6b56b7d | fall-2026 | 2026-09-27 | current | 3 | 93.2 | 15110 | 584.2 | 8 | 1,2,3,4,5 | 1,2,3,4 | 0.01 | 278 | 7 | 2 | 0 | 34 | 5 | B - usable with handling | 278 records lost in transport (1.9% of seq, 1 session(s)) |
| 6ab9a9279a8420a1e6b56b7e | fall-2026 | 2026-09-27 | current | 3 | 87.5 | 8677 | 260.6 | 7 | 1,2,3,4 | 1,2,3 | 0.01 | 0 | 10 | 3 | 0 | 29 | 4 | A - ready |  |
| 6ab9a9279a8420a1e6b56b7f | fall-2026 | 2026-09-27 | current | 2 | 92.5 | 18671 | 546.4 | 10 | 1,2,3,4,5 | 1,2,3,4,5 | 0.08 | 0 | 7 | 1 | 0 | 33 | 2 | A - ready |  |
| 6ab9a9279a8420a1e6b56b80 | fall-2026 | 2026-09-27 | current | 3 | 73.6 | 10922 | 231.3 | 7 | 1,2,3,4 | 1,2,3 | 1.24 | 0 | 11 | 0 | 0 | 31 | 2 | B - usable with handling | 135 records (1.24% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 6ab9a9279a8420a1e6b56b81 | fall-2026 | 2026-09-27 | current | 3 | 87.2 | 8191 | 258.8 | 8 | 1,2,3 | 1,2 | 0.01 | 0 | 7 | 5 | 0 | 31 | 4 | A - ready |  |
| 6ab9a9279a8420a1e6b56b82 | fall-2026 | 2026-09-27 | current | 1 | 0.0 | 805 | 32.6 | 1 | 1 |  | 0.0 | 0 | 2 | 0 | 0 | 28 | 8 | D - too little data | 32.6 active minutes / 805 records, unit(s) 1 |
| 6ab9a9279a8420a1e6b56b83 | fall-2026 | 2026-09-27 | current | 3 | 96.9 | 13148 | 510.7 | 9 | 1,2,3,4,5 | 1,2,3,4 | 0.02 | 0 | 0 | 1 | 0 | 33 | 4 | A - ready |  |
| 6ab9a9439a8420a1e6b56b9d | fall-2026 | 2026-09-27 | current | 2 | 100.0 | 12158 | 408.0 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 0 | 1 | 0 | 31 | 2 | A - ready |  |
| 6ab9a9439a8420a1e6b56b9e | fall-2026 | 2026-09-27 | current | 3 | 98.8 | 10455 | 281.7 | 8 | 1,2,3,4 | 1,2,3 | 0.01 | 0 | 0 | 1 | 0 | 30 | 4 | A - ready |  |
| 6ab9a9439a8420a1e6b56b9f | fall-2026 | 2026-09-27 | current | 2 | 98.4 | 16081 | 328.1 | 7 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 2 | 0 | 0 | 27 | 1 | A - ready |  |
| 6ab9a9439a8420a1e6b56ba0 | fall-2026 | 2026-09-27 | current | 2 | 100.0 | 7776 | 231.8 | 7 | 1,2 | 1 | 0.0 | 0 | 0 | 2 | 0 | 27 | 4 | A - ready |  |
| 6ab9a9439a8420a1e6b56ba1 | fall-2026 | 2026-09-27 | current | 2 | 100.0 | 8987 | 330.9 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 0 | 2 | 0 | 32 | 3 | A - ready |  |
| 6ab9a9439a8420a1e6b56ba2 | fall-2026 | 2026-09-27 | current | 3 | 97.3 | 10848 | 222.5 | 7 | 1,2,3,4 | 1,2,3 | 0.0 | 0 | 3 | 0 | 0 | 30 | 2 | A - ready |  |
| 6ab9a9439a8420a1e6b56ba3 | fall-2026 | 2026-09-27 | current | 2 | 99.5 | 17202 | 522.7 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.01 | 0 | 0 | 2 | 0 | 30 | 2 | A - ready |  |
| 6ab9a9439a8420a1e6b56ba4 | fall-2026 | 2026-09-27 | current | 2 | 100.0 | 14823 | 442.4 | 8 | 1,2,3,4,5 | 1,2,3,4 | 0.0 | 0 | 0 | 1 | 0 | 32 | 5 | A - ready |  |
| 6ab9a9439a8420a1e6b56ba5 | fall-2026 | 2026-09-27 | current | 3 | 98.8 | 12978 | 323.4 | 9 | 1,2,3,4,5 | 1,2,3,4,5 | 0.0 | 0 | 0 | 2 | 0 | 31 | 3 | A - ready |  |
| 6ab9a9439a8420a1e6b56ba6 | fall-2026 | 2026-09-27 | current | 3 | 98.4 | 10161 | 301.8 | 10 | 1,2,3,4,5 | 1,2,3,4 | 0.02 | 0 | 1 | 2 | 0 | 33 | 3 | A - ready |  |
| 6ab9a9dc9a8420a1e6b56bb6 | fall-2026 | 2026-09-27 | current | 2 | 100.0 | 13876 | 496.7 | 7 | 1,2,3,4 | 1,2,3 | 0.0 | 0 | 0 | 1 | 0 | 30 | 3 | A - ready |  |
| 69cdc907d385e3b94310f71f | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1815 | 208.8 | 4 | 1,2,3 | 1,2 | 1.32 | 0 | 15 | 0 | 0 | 39 | 14 | B - usable with handling | 24 records (1.32% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc907d385e3b94310f720 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2859 | 334.9 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 0.49 | 0 | 20 | 1 | 0 | 41 | 16 | A - ready |  |
| 69cdc907d385e3b94310f721 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1770 | 329.9 | 5 | 1,2,3,4 | 1 | 0.17 | 0 | 2 | 0 | 0 | 41 | 17 | A - ready |  |
| 69cdc907d385e3b94310f722 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2990 | 361.5 | 6 | 1,2,3,4,5 | 1,2,3,4 | 1.51 | 0 | 51 | 5 | 0 | 44 | 19 | B - usable with handling | 45 records (1.51% of the student's log) are legacy-envelope uploads >5s late - payload stale; 5 WASM runtime crash(es) |
| 69cdc907d385e3b94310f723 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2316 | 289.2 | 4 | 1,2,3,4 | 1,2,3 | 0.04 | 0 | 5 | 0 | 0 | 39 | 15 | A - ready |  |
| 69cdc907d385e3b94310f724 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1588 | 241.5 | 5 | 1,2,3 | 1 | 0.0 | 0 | 13 | 0 | 0 | 40 | 15 | A - ready |  |
| 69cdc907d385e3b94310f725 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3564 | 466.7 | 8 | 1,2,3,4,5 | 1,2,3,4,5 | 0.06 | 0 | 5 | 7 | 0 | 43 | 18 | B - usable with handling | 5 WASM runtime crash(es) |
| 69cdc907d385e3b94310f726 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2521 | 304.8 | 5 | 1,2,3,4,5 | 1,3,4 | 0.24 | 0 | 4 | 1 | 0 | 43 | 18 | A - ready |  |
| 69cdc907d385e3b94310f727 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2930 | 316.0 | 5 | 1,2,3,4,5 | 1,2,3,4 | 0.07 | 0 | 8 | 0 | 0 | 44 | 18 | A - ready |  |
| 69cdc907d385e3b94310f728 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2534 | 245.6 | 4 | 1,2,3,4,5 | 1,3,4 | 0.0 | 0 | 44 | 2 | 0 | 43 | 17 | A - ready |  |
| 69cdc907d385e3b94310f729 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2422 | 344.5 | 5 | 1,2,3,4 | 1,3 | 0.04 | 0 | 2 | 2 | 0 | 44 | 18 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc907d385e3b94310f72a | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2809 | 313.0 | 5 | 1,2,3,4 | 1,2,3 | 0.11 | 0 | 11 | 2 | 0 | 44 | 18 | A - ready |  |
| 69cdc907d385e3b94310f72b | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1517 | 204.4 | 5 | 1,2,3,4 | 1,3 | 0.07 | 0 | 3 | 1 | 0 | 44 | 18 | A - ready |  |
| 69cdc907d385e3b94310f72c | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1974 | 276.2 | 6 | 1,2,3,4 | 1,2,4 | 25.27 | 0 | 286 | 15 | 0 | 46 | 22 | C - partly usable | 495 records (25.27% of the student's log) are legacy-envelope uploads >5s late - payload stale; 13 WASM runtime crash(es) |
| 69cdc907d385e3b94310f72d | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1097 | 229.0 | 5 | 1,2,3 | 1 | 4.47 | 0 | 21 | 0 | 0 | 35 | 14 | B - usable with handling | 49 records (4.47% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc907d385e3b94310f72e | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2975 | 340.8 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 0.07 | 0 | 19 | 0 | 0 | 44 | 17 | A - ready |  |
| 69cdc907d385e3b94310f72f | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1789 | 241.2 | 5 | 1,2,3 | 1 | 0.06 | 0 | 18 | 3 | 0 | 40 | 15 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc907d385e3b94310f730 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3077 | 415.4 | 6 | 1,2,3,4 | 2,3 | 0.13 | 0 | 9 | 1 | 0 | 45 | 18 | A - ready |  |
| 69cdc907d385e3b94310f731 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1938 | 252.8 | 5 | 1,2,3,4 | 1,3 | 3.67 | 0 | 32 | 1 | 0 | 42 | 16 | B - usable with handling | 71 records (3.67% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc907d385e3b94310f732 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2201 | 341.8 | 5 | 1,2,3,4 | 1,3 | 0.0 | 0 | 6 | 0 | 0 | 42 | 17 | A - ready |  |
| 69cdc907d385e3b94310f733 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2660 | 329.8 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 0.08 | 0 | 8 | 0 | 0 | 39 | 15 | A - ready |  |
| 69cdc907d385e3b94310f734 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2083 | 232.3 | 4 | 1,2,3,4 | 1,3 | 0.05 | 0 | 4 | 4 | 0 | 44 | 18 | B - usable with handling | 3 WASM runtime crash(es) |
| 69cdc907d385e3b94310f735 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3333 | 357.2 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 0.78 | 0 | 98 | 0 | 0 | 43 | 17 | A - ready |  |
| 69cdc907d385e3b94310f736 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1036 | 155.4 | 3 | 1,2,3 | 1 | 0.0 | 0 | 4 | 1 | 0 | 39 | 15 | A - ready |  |
| 69cdc907d385e3b94310f737 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2251 | 342.8 | 5 | 1,2,3,4 | 1,2,3 | 0.27 | 0 | 5 | 1 | 0 | 42 | 16 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc907d385e3b94310f738 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2660 | 293.8 | 4 | 1,2,3,4,5 | 1,2,3,4 | 0.15 | 0 | 22 | 2 | 0 | 43 | 18 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc937d385e3b94310f755 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3215 | 266.0 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 16.08 | 0 | 306 | 0 | 0 | 43 | 17 | C - partly usable | 517 records (16.08% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc937d385e3b94310f756 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2673 | 238.0 | 4 | 1,2,3,4,5 | 1,3,4,5 | 1.76 | 0 | 94 | 0 | 0 | 44 | 17 | B - usable with handling | 47 records (1.76% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc937d385e3b94310f757 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2141 | 209.0 | 3 | 1,2,3,4,5 | 1,3,4,5 | 0.05 | 0 | 7 | 0 | 0 | 45 | 18 | A - ready |  |
| 69cdc937d385e3b94310f758 | spring-2026 | 2026-04-02 | reduced (older build) | 1 | 0.0 | 428 | 90.0 | 2 | 1 |  | 0.0 | 0 | 1 | 0 | 0 | 34 | 12 | A - ready |  |
| 69cdc937d385e3b94310f759 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1006 | 120.1 | 3 | 1,2 | 1 | 0.1 | 0 | 2 | 0 | 0 | 37 | 14 | A - ready |  |
| 69cdc937d385e3b94310f75a | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1781 | 228.3 | 5 | 1,2,3 | 1 | 0.34 | 0 | 5 | 2 | 0 | 41 | 17 | B - usable with handling | 2 WASM runtime crash(es) |
| 69cdc937d385e3b94310f75b | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2342 | 221.2 | 4 | 1,2,3,4 | 1,2,3 | 0.17 | 0 | 16 | 2 | 0 | 41 | 16 | B - usable with handling | 2 WASM runtime crash(es) |
| 69cdc937d385e3b94310f75c | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2200 | 240.0 | 4 | 1,2,3,4,5 | 1,3,4,5 | 0.05 | 0 | 9 | 0 | 0 | 43 | 18 | A - ready |  |
| 69cdc937d385e3b94310f75d | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2195 | 289.2 | 5 | 1,2,3,4 | 1,3 | 0.05 | 0 | 4 | 0 | 0 | 40 | 16 | A - ready |  |
| 69cdc937d385e3b94310f75e | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3034 | 244.0 | 4 | 1,2,3,4,5 | 1,2,3,4,5 | 2.64 | 0 | 181 | 3 | 0 | 48 | 22 | B - usable with handling | 80 records (2.64% of the student's log) are legacy-envelope uploads >5s late - payload stale; 1 WASM runtime crash(es) |
| 69cdc937d385e3b94310f75f | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2707 | 298.6 | 5 | 1,2,3,4 | 1,2,3 | 0.26 | 0 | 11 | 1 | 0 | 41 | 16 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc937d385e3b94310f760 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2516 | 270.4 | 5 | 1,2,3 | 1,2 | 1.0 | 0 | 122 | 5 | 0 | 43 | 17 | B - usable with handling | 25 records (1.0% of the student's log) are legacy-envelope uploads >5s late - payload stale; 4 WASM runtime crash(es) |
| 69cdc937d385e3b94310f761 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2204 | 212.8 | 4 | 1,2,3,4,5 | 1,3,4,5 | 0.09 | 0 | 6 | 0 | 0 | 42 | 17 | A - ready |  |
| 69cdc937d385e3b94310f762 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1891 | 166.1 | 4 | 1,2,3,4,5 | 1,3,4 | 0.16 | 0 | 14 | 2 | 0 | 43 | 18 | A - ready |  |
| 69cdc937d385e3b94310f763 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2425 | 286.9 | 5 | 1,2,3,4,5 | 1,3,4,5 | 0.08 | 0 | 4 | 0 | 0 | 42 | 17 | A - ready |  |
| 69cdc965d385e3b94310f775 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1770 | 223.9 | 6 | 1,2,3 | 1 | 0.11 | 0 | 10 | 1 | 0 | 38 | 15 | A - ready |  |
| 69cdc965d385e3b94310f776 | spring-2026 | 2026-04-02 | reduced (older build) | 1 | 0.0 | 309 | 31.1 | 1 | 3 |  | 0.0 | 0 | 1 | 0 | 0 | 36 | 12 | D - too little data | 31.1 active minutes / 309 records, unit(s) 3 |
| 69cdc965d385e3b94310f777 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2586 | 295.9 | 5 | 1,2,3,4,5 | 1,3,4,5 | 0.04 | 0 | 6 | 3 | 0 | 44 | 20 | B - usable with handling | 3 WASM runtime crash(es) |
| 69cdc965d385e3b94310f778 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2340 | 246.5 | 4 | 1,2,3,4 | 1 | 0.0 | 0 | 69 | 0 | 0 | 40 | 17 | A - ready |  |
| 69cdc965d385e3b94310f779 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2797 | 244.0 | 4 | 1,2,3,4,5 | 1,3,4,5 | 0.07 | 0 | 78 | 1 | 0 | 43 | 19 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc965d385e3b94310f77a | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2356 | 287.0 | 5 | 1,2,3,4,5 | 1,3,4 | 0.13 | 0 | 5 | 2 | 0 | 40 | 17 | A - ready |  |
| 69cdc965d385e3b94310f77b | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2940 | 312.8 | 6 | 1,2,3,4 | 1,2,3 | 0.1 | 0 | 12 | 0 | 0 | 42 | 17 | A - ready |  |
| 69cdc965d385e3b94310f77c | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2179 | 263.4 | 5 | 1,2,3,4,5 | 1,3,4 | 0.18 | 0 | 6 | 0 | 0 | 38 | 17 | A - ready |  |
| 69cdc965d385e3b94310f77d | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1889 | 286.3 | 6 | 1,2,3,4 | 1,3 | 11.43 | 0 | 106 | 0 | 0 | 46 | 21 | C - partly usable | 216 records (11.43% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc965d385e3b94310f77e | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3038 | 250.0 | 4 | 1,2,3,4,5 | 1,2,3,4,5 | 0.13 | 0 | 53 | 0 | 0 | 42 | 16 | A - ready |  |
| 69cdc965d385e3b94310f77f | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 970 | 168.9 | 4 | 1,2,3 | 1 | 0.72 | 0 | 2 | 0 | 0 | 38 | 14 | A - ready |  |
| 69cdc965d385e3b94310f780 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2427 | 288.2 | 5 | 1,2,3,4 | 1,3 | 0.04 | 0 | 7 | 3 | 0 | 45 | 19 | B - usable with handling | 3 WASM runtime crash(es) |
| 69cdc965d385e3b94310f781 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2727 | 282.8 | 5 | 1,2,3,4,5 | 1,2,3,4 | 0.48 | 0 | 9 | 2 | 0 | 42 | 17 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc965d385e3b94310f782 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2275 | 277.1 | 5 | 1,2,3,4 | 1,3 | 27.69 | 0 | 277 | 0 | 0 | 44 | 18 | C - partly usable | 630 records (27.69% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc965d385e3b94310f783 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2673 | 217.1 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 2.96 | 0 | 69 | 0 | 0 | 45 | 18 | B - usable with handling | 79 records (2.96% of the student's log) are legacy-envelope uploads >5s late - payload stale |
| 69cdc965d385e3b94310f784 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2754 | 256.0 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 0.15 | 0 | 19 | 0 | 0 | 41 | 15 | A - ready |  |
| 69cdc965d385e3b94310f785 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3069 | 250.2 | 4 | 1,2,3,4,5 | 1,3,4,5 | 0.07 | 0 | 60 | 0 | 0 | 44 | 18 | A - ready |  |
| 69cdc965d385e3b94310f786 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1922 | 239.3 | 4 | 1,2,3,4 | 1,2 | 0.1 | 0 | 4 | 1 | 0 | 41 | 16 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc965d385e3b94310f787 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2112 | 266.1 | 5 | 1,2,3,4 | 1,3 | 10.06 | 0 | 114 | 4 | 0 | 45 | 20 | C - partly usable | 212 records (10.06% of the student's log) are legacy-envelope uploads >5s late - payload stale; 4 WASM runtime crash(es) |
| 69cdc965d385e3b94310f788 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2774 | 256.7 | 5 | 1,2,3,4,5 | 1,2,3,4,5 | 0.07 | 0 | 6 | 0 | 0 | 42 | 18 | A - ready |  |
| 69cdc965d385e3b94310f789 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1604 | 180.1 | 5 | 1,2,3,4 | 1,3 | 0.12 | 0 | 13 | 4 | 0 | 43 | 18 | B - usable with handling | 4 WASM runtime crash(es) |
| 69cdc965d385e3b94310f78a | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2715 | 298.1 | 5 | 1,2,3,4,5 | 1,3 | 0.04 | 0 | 21 | 0 | 0 | 44 | 18 | A - ready |  |
| 69cdc965d385e3b94310f78b | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2942 | 291.9 | 5 | 1,2,3,4,5 | 1,3,4,5 | 0.03 | 0 | 16 | 1 | 0 | 44 | 19 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc965d385e3b94310f78c | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2042 | 252.7 | 4 | 1,2,3,4 | 1,2,3 | 0.1 | 0 | 5 | 0 | 0 | 39 | 15 | A - ready |  |
| 69cdc98ad385e3b94310f7a7 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2599 | 308.7 | 5 | 1,2,3 | 1,2 | 0.35 | 0 | 8 | 6 | 0 | 44 | 18 | B - usable with handling | 5 WASM runtime crash(es) |
| 69cdc98ad385e3b94310f7a8 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2331 | 276.8 | 4 | 1,2,3,4 | 1,2,3 | 0.09 | 0 | 5 | 1 | 0 | 41 | 16 | A - ready |  |
| 69cdc98ad385e3b94310f7a9 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1958 | 267.6 | 4 | 1,2,3,4 | 1,3 | 2.51 | 0 | 26 | 3 | 0 | 43 | 18 | B - usable with handling | 49 records (2.51% of the student's log) are legacy-envelope uploads >5s late - payload stale; 2 WASM runtime crash(es) |
| 69cdc98ad385e3b94310f7aa | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1937 | 265.5 | 4 | 1,2,3 | 1,2 | 0.05 | 0 | 4 | 2 | 0 | 41 | 15 | B - usable with handling | 2 WASM runtime crash(es) |
| 69cdc98ad385e3b94310f7ab | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3577 | 326.7 | 6 | 1,2,3,4,5 | 1,2,3,4,5 | 0.22 | 0 | 60 | 0 | 0 | 45 | 17 | A - ready |  |
| 69cdc98ad385e3b94310f7ac | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2140 | 256.0 | 4 | 1,2,3,4 | 1,3 | 0.05 | 0 | 5 | 4 | 0 | 41 | 17 | B - usable with handling | 3 WASM runtime crash(es) |
| 69cdc98ad385e3b94310f7ad | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2147 | 264.6 | 4 | 1,2,3,4 | 1,2,3 | 0.0 | 0 | 5 | 0 | 0 | 43 | 17 | A - ready |  |
| 69cdc98ad385e3b94310f7ae | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1671 | 175.3 | 3 | 1,2,3 | 1,2 | 0.12 | 0 | 4 | 2 | 0 | 41 | 15 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc98ad385e3b94310f7af | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2525 | 232.5 | 4 | 1,2,3,4,5 | 1,2,3,4,5 | 0.2 | 0 | 5 | 0 | 0 | 42 | 16 | A - ready |  |
| 69cdc98ad385e3b94310f7b0 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 3365 | 351.2 | 5 | 1,2,3,4,5 | 1,2,3,4 | 0.12 | 0 | 17 | 1 | 0 | 43 | 18 | A - ready |  |
| 69cdc98ad385e3b94310f7b1 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1876 | 211.5 | 4 | 1,2,3 | 1,2 | 0.16 | 0 | 5 | 0 | 0 | 39 | 14 | A - ready |  |
| 69cdc98ad385e3b94310f7b2 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 1924 | 264.2 | 4 | 1,2,3 | 1 | 0.05 | 0 | 8 | 2 | 0 | 39 | 16 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc98ad385e3b94310f7b3 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2744 | 280.5 | 5 | 1,2,3,4,5 | 1,2,3,4 | 0.36 | 0 | 15 | 2 | 0 | 41 | 16 | B - usable with handling | 1 WASM runtime crash(es) |
| 69cdc98ad385e3b94310f7b4 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2268 | 266.6 | 4 | 1,2,3,4 | 1,2,3 | 0.04 | 0 | 13 | 0 | 0 | 39 | 15 | A - ready |  |
| 69cdc98ad385e3b94310f7b5 | spring-2026 | 2026-04-02 | reduced (older build) | 2 | 0.0 | 2703 | 327.1 | 5 | 1,2,3,4,5 | 1,3,4,5 | 0.0 | 0 | 5 | 2 | 0 | 43 | 18 | B - usable with handling | 2 WASM runtime crash(es) |

## 6. Per-unit readiness

Behaviour analysis is usually per unit, and students switched builds mid-unit, so each student x unit is rated separately (`csv/user_unit_summary.csv`). Data quality uses the same thresholds as the student verdict, applied to the unit's own records: ok = under 1% late legacy-envelope uploads; apply late-upload rule = 1–10%; payload unreliable = 10% or more. Counts are students.

| unit | finished | … payload ok | … apply late-upload rule | … payload unreliable | played, not finished | not reached | with transport loss |
|---|---|---|---|---|---|---|---|
| 1 | 205 | 194 | 4 | 7 | 12 | 1 | 0 |
| 2 | 110 | 77 | 32 | 1 | 103 | 5 | 0 |
| 3 | 168 | 162 | 2 | 4 | 40 | 10 | 0 |
| 4 | 115 | 112 | 1 | 2 | 71 | 32 | 1 |
| 5 | 88 | 84 | 4 | 0 | 36 | 94 | 0 |

## 7. Method

- **D - too little data:** fewer than 60 active minutes.
- **C - partly usable:** ≥10% of the student's records are legacy-envelope records uploaded more than 5 s late (their `data` payload is a stale copy, so payload-based measures are unreliable for those periods; eventKey, eventType, sceneName and timestamps stay usable), or ≥5% of envelope sequence numbers missing.
- **B - usable with handling:** 1–10% stale-risk records, any smaller transport loss, a WASM runtime crash, or a FAIL finding.
- **A - ready:** none of the above.
- Not used for the verdict: findings that recur in the baseline playthrough (build-level quirks such as the DialogueEvent `…:0` first-node eventKey or the fixed-node eventKey/payload pairs), regression-category differences (pacing), absent events in units the student did not finish, and pointer-lock `unhandled_rejection` crash telemetry.
- **Logging design:** `current` = the log contains at least one of InputEvent, ObjectInterEvent, gameStartEvent, argumentationAnswerEvent; `reduced (older build)` = none of them (the April 2026 builds log 13 event types).
- Late uploads are serverTimestamp minus client timestamp. On the 20260914- build, 95% of student-days have a median difference within ±2 s, so larger values are upload delay, not clock error.
- Envelope = the `session_id`/`seq`/`entry_id`/`sent_at` fields present from build 20261005-12466; seq starts at 1 per session, so a missing number is a lost record and a repeated `entry_id` is a resend.
