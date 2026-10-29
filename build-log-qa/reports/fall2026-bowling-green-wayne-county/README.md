# Field-test log quality — Bowling Green / Wayne County export (fall 2026)

**Audited:** 2026-10-22.
**Input:** `playthrough-logs-and-results/fall2026-bowling-green-wayne-county/stratalog_BowlingGreen_WayneCounty.jsonl` — 1,979,541 records, 218 `user_id`s, no malformed lines.
**Method:** the weekly `build-log-qa` audit, run once per `user_id`. Each student got an evidence-based coverage manifest. On top of that, classroom-specific data-quality metrics were computed.
**Baseline:** the newest internal playthrough audit, [`reports/09-23-26`](../09-23-26/) (build `20260914-`).

This file is the interpretation. Supporting files:
- [`cohort-report.md`](cohort-report.md) — the generated tables, including all 218 students;
- [`csv/user_summary.csv`](csv/user_summary.csv) — one row per student;
- [`users/<user_id>/`](users/) — the standard audit report for every student.

---

## Short answer

1. **Fall 2026 field test (138 user_ids): yes, the logs support behaviour analysis.**
   - **Verdicts:** 129 of 138 students are usable (72 *ready*, 57 *usable with one handling rule*), 6 are *partly usable*, and 3 have *too little data*.
   - **No FAIL** for any student.
   - **Same warnings as the internal test:** a median of 33 warnings per student versus 31 for the internal playthrough, and the build-level quirks are the same ones.
   - **New warnings are explained:** each student has a median of 3 warnings not seen internally. All of them are classroom effects described in §3.2, not new logging defects.
   - **No content gaps:** no event family is missing from content a student actually finished.
2. **The one real classroom data-quality problem is late uploads on build `20260914-`.**
   - School devices buffered records offline. On that build, a late-uploaded record carries a **stale copy of the `data` payload**, while `eventKey`, `eventType`, `sceneName` and the timestamps stay correct.
   - This affects 40,577 records, 2.3% of all fall data. 93% of them (37,569) belong to the students whose accounts were created on 2026-09-11, the group that played mostly on this build.
3. **Build `20261005-12466` fixed it.**
   - Late uploads now carry correct payloads.
   - Its new `session_id`/`seq` delivery envelope shows **99.97% of records arrived**: 278 missing out of 941,056.
4. **80 of the 218 user_ids are not part of this fall's field test.** They played on 2026-04-13 → 05-03 on builds `20260401/20260408-10923`. Those builds use an older, reduced logging design: 13 event types, with no input, interaction, puzzle-piece or argumentation-answer events. Their logs are internally sound but **not comparable** with the newest build (§4).

---

## 1. What is in the export

| group | user_ids | played (UTC) | builds | records | median active time | devices |
|---|---|---|---|---|---|---|
| Fall, accounts created **2026-09-11** | 60 | 09-22 → 10-07 (52 started 09-23) | mostly `20260914-`; a few days of `20261005-12466` at the end (median 6% of records) | 820k | 354 min over 10 days | all Intel UHD, 1920×1080 |
| Fall, accounts created **2026-09-27** | 78 | 10-05 → 10-19 | mostly `20261005-12466` (median 92%), some `20260914-` on day 1, `20261016-` for 40 students | 975k | 338 min over 8 days | ARM Mali-G52/G57, 1366×768; some evening play (launches 00–05 UTC) |
| Spring, accounts created **2026-04-02** | 80 | 04-13 → 05-03 | `20260401-10923`, `20260408-10923` | 184k | 266 min over 5 days | — |

**Group labels.** "Accounts created" is the date stored in the Mongo ObjectId of the `user_id`, i.e. when the roster was loaded. Each fall group sits in a different district's devices and calendar. The logs cannot tell which group is Bowling Green and which is Wayne County.

**Builds in the fall data** (crash telemetry carries app versions 2.8.x/2.9.x instead and is counted separately):

| build | students | records | delivery envelope | late uploads > 5 s | late > 1 day (max) | stale payloads |
|---|---|---|---|---|---|---|
| `20260914-` | 132 | 853,857 | no | 40,577 (4.8%) | 13,529 (12 days) | **all 40,577** |
| `20261005-12466` | 117 | 878,004 | yes, 1,107 sessions | 16,540 | 41 (6 days) | none |
| `20261016-` | 40 | 62,902 | yes, 108 sessions | 1,498 | 10 (3 days) | none |

Two version strings are truncated (`20260914-`, `20261016-`), so neither identifies an exact build. 117 of the 138 fall students played on two or three builds.

---

## 2. Per-student verdict

| verdict | meaning for the analyst | fall, 09-11 group | fall, 09-27 group | spring |
|---|---|---|---|---|
| **A – ready** | analyse as is, after the standard cleaning in §5 | 10 | 62 | 42 |
| **B – usable with handling** | apply the late-upload rule (§5, rule 4) to 1–10% of the student's records, or note a crash or the one transport hole | 44 | 13 | 32 |
| **C – partly usable** | ≥10% of the student's records have stale payloads. eventKey-based measures (dialogue path, quest progress, timing) are fine, but payload-based measures (answers, choices, positions, inputs) are unreliable for the affected periods | 6 | 0 | 5 |
| **D – too little data** | under 60 active minutes | 0 | 3 | 1 |

**Fall students in C:**
- `6aa4140b41b41dbac0c7f225` — 31.9% of records stale;
- `6aa4142c41b41dbac0c7f247` — 29.4%;
- `6aa4142c41b41dbac0c7f250` — 16.1%;
- `6aa413b141b41dbac0c7f1f1` — 15.5%;
- `6aa4144c41b41dbac0c7f267` — 14.0%;
- `6aa413b141b41dbac0c7f1f3` — 13.5%.

**Fall students in D:** `6ab9a8bc9a8420a1e6b56b02`, `6ab9a8bc9a8420a1e6b56b04` and `6ab9a9279a8420a1e6b56b82`.
- They have 13–33 active minutes, Unit 1 only, on one day (10-05 / 10-06), on build `20260914-` only.
- They look like spare or abandoned accounts. Worth checking with the teacher before excluding them.

**Fall students in B, by reason:**
- 51 for late-upload stale payloads;
- 5 for a WASM `memory access out of bounds` crash;
- 1 for transport loss.

Thresholds and rules: [`cohort-report.md` §6](cohort-report.md#6-method).

---

## 3. Comparison with the internal baseline (09-23-26)

### 3.1 The same as the internal playthrough

The fall classroom logs show the same build-level logging quirks the 09-23-26 audit reported. Counts are fall students out of 138:

| quirk | students |
|---|---|
| empty-string field name in `gameStartEvent` / `gameWindow*Event` | 138 |
| `DialogueEvent` eventKey format warnings: the `…:0` first-node keys and late uploads, all on the September build (corrected 2026-10-24, see the note below) | 125 |
| dialogue finish without start | 135 |
| `PuzzlePieceVisibleEvent` exact duplicates and repeated opens | 135 |
| `ObjectInterEvent` casing variants ("Press E To Scan" / "to Scan") | 128 |
| argumentation close without open | 119 |
| `InputEvent` exact duplicates | 116 |

**Correction (2026-10-24):** the first version of this report counted 138 students for the eventKey-format row. This classroom export writes every number as a decimal (`"conversationId": 30.0`, while internal exports write `30`), and the audit compared keys as text. It therefore flagged every dialogue record as a mismatch. The audit now writes whole-number decimals as integers when it rebuilds the key; its counts equal the `dialogue_mismatch` column for all 218 students, and the October builds have no mismatches.

The internal `DaniEvent` "absent" false alarm also recurs: the DANI panel is player-optional.

No student produced a FAIL. Differences in cadence and volume against the baseline (the "regression" warnings) reflect how students play. They play slowly, over many class periods, with a median of 16–19 launches each against 6 in the internal run. They are not logging changes.

The baseline sees far fewer distinct values than the students, because one tester didn't press the arrow keys, Pause or SkipCinematic and didn't submit most answer combinations. New values against the baseline are therefore expected and are listed per student in `users/<id>/csv/regression_diff.csv`.

### 3.2 New in the classroom logs

**a) Late uploads carry stale payloads on `20260914-`.** School devices buffer records while offline and upload them later, sometimes days later. On this build the payload of a buffered record is not the one from when the event happened:

| evidence (build `20260914-`) | uploaded on time | uploaded > 5 s late |
|---|---|---|
| `DialogueEvent` eventKey agrees with `data.conversationId/nodeId` | 97% | 60% at 5–60 s, **3%** beyond 1 min |
| `questEvent` eventKey agrees with `data.questID` | 98.1% | **55.6%** |
| `argumentationNodeEvent` payload identical to the previous one | 2.9% | **99.3%** |
| `InputEvent` payload identical to the previous one | 47.7% | **94.9%** |
| `ObjectInterEvent` payload identical to the previous one | 30.5% | **88.5%** |
| `PlayerPositionEvent` payload identical to the previous one | 65.1% | **89.7%** |

- A late batch repeats one payload, so the defect hits **every event type**, not only the keyed ones.
- The eventKey, eventType, sceneName and client timestamp of late records are correct; only `data` is unreliable.
- The same family explains two new warnings:
  - `questEvent` eventKey ≠ questID (45 students);
  - the small on-time `DialogueEvent` mismatches (also in the internal run). The payload is captured a moment after the dialogue has advanced: in 1,890 of 1,892 cases it equals the next node's eventKey, which fired a median 16 ms later. Both disappear in the fixed build.
- **Correction (2026-10-23):** the `questEvent` "finish without preceding start" warning (94 students) is mostly NOT this stale-payload effect. Counted with the audit's own pairing logic on the 129-student analysis set (222 flagged finishes, 89 students):
  - **155 finishes (72 students) are a quest finished a second time after a relaunch.** The game resumed from a checkpoint and the student finished the quest again, but the relaunch did not re-log `questActiveEvent`. These happen on all three builds, mostly for quests 47 "Power Play – Floor 2", 16 "Supply Run", 51 and 43, typically about 1–6 minutes after the relaunch.
  - **41 finishes (32 students) have no start anywhere in the log.** 33 of them are quest 46 "Power Play – Floor 1", which lacks its start for 26 of the 111 students who finished it (24%).
    - **Correction (2026-10-27):** `questActiveEvent:46` does not fire on entering the dungeon. DANI's arrival conversation hands it out: conversation 91, nodes 0/120–125 → 1 → 5 → the student's reply at node 9/10 → DANI's answer at node 11/12 → `questActiveEvent:46` → node 13. That is a median 59 s after arrival, for all 85 students who have the start, and in the internal run.
    - In all 26 students without the start, nodes 9–12 never appear:
      - **20 students:** the arrival conversation never played at all. Their first conversation-91 record is a later room, node 14 (the mural) or node 19 (the sand particles). On the October builds the delivery envelope shows no missing `seq`, so the game never emitted these records; they were not lost in transit.
        - **All 20 relaunched in the middle of Unit 4**, after quest 39 started and before their first dungeon entry. The game resumed from a save: quest 39 was re-logged at once and conversation 88 picked up at node 3. 16 came back after a break, usually the next class day; 4 restarted within 3–37 minutes.
        - Only 1 of the 85 students who got the conversation had a mid-Unit-4 relaunch (`…6b72`, also on `20261005-12466`). So 20 of the 21 students who resumed mid-Unit 4 skipped it.
        - The students who got the conversation and relaunched did so between the end of Unit 3 and the start of Unit 4, so Unit 4 began fresh (conversation 88 from node 0, then quest 39).
      - **6 students:** the conversation started, but the game was relaunched before node 9. Five came back the next class day and one after 15 minutes. The game resumed on the surface (quest 39 re-logged), and the arrival conversation was not replayed when the student went back down.
      - **The same mechanism covers all 26:** once Unit 4 resumes from a save before DANI hands out the quest, the arrival conversation does not play.
        - It is not a device effect. The missing-start rate is 27% on the Intel UHD (09-11) devices and 21% on the Mali-G52 (09-27) devices, and on both types nearly every student who resumed mid-Unit 4 missed it.
        - It is not crash-related. Only 3 crash records fall near these relaunches, all the "A user gesture is required to request Pointer Lock" warning, which makes up 59% of all crash records (80 of 129 students).
        - This is a save/restore bug for the developers; the `20261016-` build is untested because no student resumed mid-Unit 4 on it.
    - The internal run 09-03-26-2 shows the same pattern: the conversation jumped from node 122 to node 19, and there is a finish for quest 46 with no start.
    - So quest 46's start marks progress through the conversation, not entry to the dungeon. Use the first `Unit 4 Dev - Dungeon` record as the dungeon entry time; all 111 students have it. No grading script uses quest 46.
    - The other quests with this gap are rare: 29 (3%), 24 (2%) and 41 (1%). 26 of the 30 quests finished by at least 10 students never show it.
  - **20 finishes (17 students)** come from stale `data.questID` payloads on the September build. Pairing by `eventKey` removes all of them.
  - **6 finishes (3 students)** are a second finish without a relaunch. 3 of them are resends (same `entry_id`); the rest followed a return to the dungeon scene in the same session.
- The same pattern appears in the April builds.

**b) Fixed in `20261005-12466` and `20261016-`.**
- eventKey/payload agreement: 94,359 of 94,359 keyed dialogue records and 5,548 of 5,548 quest records.
- Late records are no more repetitive than on-time ones (InputEvent 41% vs 43%; argumentation nodes 0% vs 0%).
- **The eventKey values themselves did not change**: the same `…:0` keys and fixed node pairs still fire, now with matching payloads. Dashboard scripts that key on `eventKey` are therefore unaffected by the fix.

**c) The new delivery envelope** on `20261005-12466` and later gives every record a `session_id`, `seq` (1, 2, 3 … per launch), `entry_id`, `sent_at` and, for records persisted locally and sent after a reload, `recovered: true`. This lets loss be measured for the first time:
- **1,215 sessions; 941,056 sequence numbers expected; 278 missing (0.03%).**
- All 278 missing records are in one session: `6ab9a9279a8420a1e6b56b7d`, 2026-10-19, Unit 4 dungeon, build `20261016-`.
  - Records up to seq 170 (12:54:38 UTC) arrived live.
  - Seq 449 onward (from 13:05:20) arrived 50 minutes later, flagged `recovered`.
  - About 11 minutes of play in between never arrived. This is a gap at the start of an offline period in the recovery mechanism.
- **128 resends:** a repeated `entry_id`. Drop them by `entry_id`.
- **3,609 recovered records**, plus 106 `20260914-` records that were stranded on a device and delivered later by the newer build's recovery.

**d) Crash telemetry** (`crash` eventType; none in the baseline run): 336 fall records across 101 students.
- Most are browser noise:
  - "A user gesture is required to request Pointer Lock" — 200;
  - "Permissions check failed" (`isPWA: true`) — 112, mainly in the 09-11 group;
  - other pointer-lock / permission messages — 17;
  - "Failed to start the audio device" — 1.
- Real crashes are rare:
  - WASM `memory access out of bounds` — 5 students, 4 of them on the ARM Mali devices;
  - one `load_stalled` launch.
- Crash records have no client `timestamp` and no `sceneName`. This explains the "records without a parseable client timestamp" warning (101 students) and the duplicate-crash warning (42).

**e) Reload/resume artefacts in sequences.** Students reload mid-activity far more than the internal tester did. This produces a handful of sequence warnings not seen internally:
- argumentation session opened twice (35 students);
- `DaniEvent` and topographic-map close-without-open (9–12);
- one record attributed to a different scene between two runs of the same scene (12).

They describe player and reload behaviour, not lost data.

**f) Absent events: none in finished content.** Every "expected event absent" warning for a fall student is in a unit that student never finished: garden box, soil machine, solar still, water chamber, argumentation in unreached units. The exceptions are player-optional panels in finished units:
- `DaniEvent` (12 students);
- the backing-info panel `argumentationToolEvent` (7);
- `chatEvent` (25, all through Unit 1 completion).

Every student who entered a Unit 5 scene has the Unit 5 chat record.

**g) Small value items:**
- `SolarStillDesignEvent` `optionSelected` with `selectedOption: ""` (39 students);
- empty `argumentationAnswerEvent.answerSubmitted` (35 students; seen once internally on 09-14);
- `InputEvent` `ToggleDebug` with `key: ""` (66 students). The debug menu itself never opened: there is no `isOpened: true` anywhere in the export.

### 3.3 Context for analysis (not logging problems)

- **Progress:**
  - 89 of the 138 fall students reached Unit 5, and 41 logged `EndOfUnit` for all five units: 1 of the 60 in the 09-11 group and 40 of the 78 in the 09-27 group.
  - **58 students played Unit 3+ without `EndOfUnit 2`.** None of them finished quest 54, the last Unit 2 quest in the internal run. They were moved past Unit 2, which fits the Unit 2 blocker under investigation in `bug-finding-game-playthrough/`. EndOfUnit 2 did fire; the students simply never got that far.
- **Old Unit 4 crop prompts:** both crop-prompt sets ("collect broccoli / peas / potatoes" and "collect mega turnips / super orange / ultra corn") occur on all three fall builds. The crop names therefore don't identify a build, which corrects an inference from the 09-23-26 audit.

---

## 4. The spring 2026 user_ids (80)

These students played in April–May 2026 on builds older than anything audited internally (the earliest internal audit is 08-13-26, build `20260812`).
- **Data quality:** their logs are internally consistent. There are no FAILs, and on data quality alone they score 42 A / 32 B / 5 C / 1 D. The April builds have the same late-upload stale-payload behaviour.
- **What the April builds don't log:**
  - only 13 event types;
  - no `InputEvent`, `ObjectInterEvent`, `PuzzlePieceVisibleEvent` or `argumentationAnswerEvent`;
  - no `gameStartEvent` / window focus, `DEBUGMenu`, `chatEvent`, `DaniEvent` or `SolarStillDesignEvent`.
- **What they log differently:**
  - positions every 30 s instead of 10 s;
  - topographic-map open/close under a different event name, `"Topographic Map Event"`;
  - `TerasGardenBox` uses both `boxID` and `boxId`.
- **Other:** 29 of 80 had WASM runtime crashes.

**What they can support:** dialogue, quest and argumentation-node analysis. They cannot support input, interaction or answer-level analysis, and they should not be pooled with the fall cohort. Please confirm whether they belong in this export at all (§7).

---

## 5. Data-handling rules for behaviour analysis

1. **Scope.** Use the 138 fall students. Check the 3 D accounts with the teacher. Analyse the spring user_ids separately, if at all.
2. **Order.** Sort by client `timestamp`, never by `_id`. Within a `session_id`, `seq` gives the exact emission order.
3. **De-duplicate.**
   - On envelope builds, drop repeated `entry_id`s (resends).
   - Then collapse exact duplicates (same eventType, sceneName, timestamp and data). These are mostly `PuzzlePieceVisibleEvent`, which improved from 6.9% of those records on `20260914-` to 2.8% on `20261005-12466`, and `InputEvent`.
4. **Late-upload rule.** A record without `session_id` (builds `20260914-` and April) whose `serverTimestamp − timestamp` exceeds 5 s:
   - keep `eventType`, `eventKey`, `sceneName` and the timestamps;
   - treat `data` as missing.

   `csv/user_summary.csv` → `stale_risk_records` / `stale_risk_pct` gives the count per student.
5. **Identity.** On legacy builds, identify dialogue nodes and quests by `eventKey`, never by `data.conversationId/nodeId/questID`.
6. **Sessions.** On envelope builds, one `session_id` is one launch. On `20260914-`, use `gameStartEvent` as the session boundary.
7. **Crash records** have no client timestamp; place them by `serverTimestamp`. Pointer-lock and permission rejections are browser noise, not gameplay events.
8. **Build as a covariate.** Most students crossed builds mid-unit. Keep `version` in every analysis table.
9. **Unit 2.** For the 58 students who were moved past Unit 2, Unit 2 measures are incomplete by design. They are not missing data.

---

## 6. For the developers (Dale Musser's team)

1. **Stale-payload defect on `20260914-`** — confirmed in classroom data for every event type (§3.2a), and fixed in `20261005-12466` (§3.2b). Please confirm the fix was deliberate and is kept. About 40,000 classroom records from the September weeks are affected and cannot be repaired.
2. **Recovery gap:** one offline period lost seq 171–448 while later records were recovered (§3.2c). Worth checking what happens to records queued in memory before persistence kicks in.
3. **The version string is truncated again** on `20261016-`, as `20260914-` was.
4. **Crash telemetry noise:** about 300 pointer-lock and "Permissions check failed" `unhandled_rejection`s. Also, crash records carry no client timestamp or sceneName.
5. **WASM `memory access out of bounds`** on 4 ARM Mali Chromebooks (the 09-27 group) and 1 Intel device in the fall data.
6. **Unchanged from the internal audit:**
   - empty-string field name in `gameStartEvent` / `gameWindow*Event`;
   - `ObjectInterEvent` casing variants;
   - `PuzzlePieceVisibleEvent` duplicates;
   - empty `SolarStillDesignEvent.selectedOption`;
   - `ToggleDebug` with an empty `key`.

---

## 7. Open questions for you

1. **Spring user_ids:** should the 80 April–May user_ids be part of this field-test dataset? They make up the gap between the 138 fall students and the "over 200" in the brief.
2. **Districts:** which roster group (accounts created 09-11 vs 09-27) is Bowling Green and which is Wayne County?
3. **D accounts:** are the three short D accounts students who later switched to another account?

---

## 8. Files and re-running

| file | contents |
|---|---|
| `cohort-report.md` | generated tables: verdicts, builds, WARNING/FAIL prevalence vs baseline, all 218 students, method |
| `csv/user_summary.csv` | one row per student: builds, activity, progress, delay and stale-payload counts, eventKey agreement, transport loss, duplicates, crashes, finding counts, verdict and reasons |
| `csv/finding_prevalence.csv` | every WARNING/FAIL finding: number of fall/spring students, whether the baseline had it, an example |
| `csv/build_summary.csv` | the same metrics per build |
| `csv/transport_sessions.csv` | one row per `session_id`: span, missing seq ranges, resends, recovered records |
| `users/<user_id>/` | the standard weekly audit for that student (`audit-report.md` first), plus the `coverage.yaml` it was run with |
| `cohort_data.json` | cached per-student results; lets the tables be re-rendered with `--reuse` |

Every finding references `<user_id>.jsonl[i] _id=…`. The `_id` is unique and can be searched for in the original export.

To re-run (about 40 s), from the repository root:

```bash
python build-log-qa/scripts/audit_per_user.py \
    --input playthrough-logs-and-results/fall2026-bowling-green-wayne-county/stratalog_BowlingGreen_WayneCounty.jsonl \
    --build-id fall2026-bowling-green-wayne-county \
    --baseline build-log-qa/reports/09-23-26
```
