# QA 1693 — Unit 2 Classifier: Forensic Analysis (first pass)

*Logs: `players-logs-met-bugs/` (build string `20260914-`).*
*Controls: Ella Preble (same build, Goodhue) and two internal playthroughs (09-14-26-3, 09-23-26).*
*All times are client `timestamp`, UTC, 2026. The classes run about 13:10–13:50 UTC (Lawyer2) and 15:08–15:50 UTC (Lawyer5).*
*Evidence labels: **[O]** observed in the logs · **[I]** inferred · **[S]** speculative.*

---

## Executive Finding

There are two different mechanisms behind this ticket. The more important one is reproducible and affects most of the students.

1. **Reload after the Classifier freezes the game; this is the main mechanism.**
   - **[O]** If a student completes the Classifier in "Which Watershed?" (quest 25) and then refreshes, reloads or starts a new session, every reload lands in the same frozen state:
     1. `questActiveEvent:25`.
     2. DANI's quest-opening lines `21:46 → 21:51` replay.
     3. `DialogueFinish` for conversation 21.
     4. The Classifier conversation (8) **never starts**.
     5. The player is left standing still with **zero input events** until the next reload.
   - This happened in **13 of 13** such reloads across 5 students: Isabella from this ticket, Corah and Molli from QA 1694, and Katelyn and Walton from QA 1697. It never resolved.
   - **[I]** In the dialogue export, `21:51` links only to `8:0`. All of `8:0`'s branches require `Variable["classifierDone"] == false`. A student who already finished the Classifier therefore has no valid path, the conversation ends, and the game is left waiting for a Classifier that cannot open.
2. **A hung Jasper conversation (Reed only, in-session, single observation).**
   - **[O]** Reed picked the reply `23:30` ("I need watersheds and sizes! Now!"). Its unconditional follow-up `23:31` never played and no conversation end was logged.
   - He regained movement and pressed Interact 146 times over 5.8 minutes, standing within 3–15 units of Jasper at times, without the conversation restarting. Jasper's conversation is the gate to the drone step.

**Developer action:** inspect what the Unit 2 save restores for quest 25 (quest and entry states, Lua variables, and a "resume conversation 21 at node 46" behaviour) and the `21:51 → 8:0` hand-off conditions.

## Reported Symptom

The tracker reports: "Players who stop after U2 Classifier, but before finishing U2" (Maryville, Lawyer2: Reed Henggeler, Isabella Ruminer). Status: Tested.

## Students and Log Mapping

| Student (tracker) | Log file | Confidence | Note |
|---|---|---|---|
| Lawyer2 / Reed Henggeler | `lawyer2.read.henggeler.stratalog.logdata.json` | High | filename typo `read` → Reed |
| Lawyer2 / Isabella Ruminer | `lawyer2.isabella.ruminer.stratalog.logdata.json` | High | |

Supporting evidence comes from Corah Thompson and Molli Kelme. They are listed only under QA 1694, but their Unit 2 logs show the same freeze as Isabella. This is consistent with the tracker's statement that the QA 1694 students had "experienced the above classifier or argumentation bug". Details are in `student-log-mapping.md`.

## Probable Failure Window

| Student | Last known good | Failure window | Mechanism |
|---|---|---|---|
| Isabella | 09-24 13:47:15: `18:130` (entry 2 "talk to Anderson" active) | 09-24 13:48:56 (session ends) → **09-25 13:17:00–13:18:14** (first reload into the frozen state) | Reload after the Classifier |
| Reed | 09-25 13:44:35: `21:76` (Tera done, entry 4 "talk to Jasper" active) | **09-25 13:44:50.3–13:44:53.9** (Jasper conversation starts, reply `23:30`, follow-up missing, movement resumes) | Hung conversation |

## Last Known Good State

- **Isabella [O]:** she followed the normal quest-25 path:
  1. `questActiveEvent:25` (09-24 13:37:33).
  2. Classifier intro end `8:12` (13:40:13).
  3. Six correct (`26:141` ×6) and six wrong (`26:138` ×6) classifications.
  4. `26:136` "Now making arguments should be a breeze!" (13:46:09).
  5. `18:121` "argumentation algorithm has been fully retrained" (sets entry 1 success, 13:46:18).
  6. `18:130` (sets entry 2 active, 13:47:15).

  This matches the internal controls step for step. Her last record is 13:48:56, about 2 minutes before her class period ended. The logs show no stuck behaviour inside that session.
- **Reed [O]:**
  1. On 09-24 his first quest-25 attempt was lost to two reloads that restored the older `A22+A24` checkpoint. He replayed quests 24 and 22 and lost no further ground.
  2. On 09-25 he restarted quest 25 (13:29:43) and completed the Classifier (`26:136`, 13:38:51).
  3. He talked to Anderson (`19:32`, 13:41:56) and Tera (`21:76`, 13:44:35). All of this is normal.

## First Abnormal State

- **Isabella, 09-25 13:17:00–13:18:14 [O]:**
  1. The first load after the break emits `questActiveEvent:25`.
  2. Conversation 21 starts **at node 46** (not 45), and nodes 46–51 play.
  3. `DialogueFinish` for conversation 21 follows 6.6 s after `21:51`.
  4. No conversation-8 node follows.
  5. The player stands at (1416, 102, 1105) with no input events until a reload at 13:19:01. That reload repeats the same sequence (finish 9.6 s after `21:51`).
  6. At 13:21:27 she returns to MainMenu and loads **Unit 3** directly, with no `EndOfUnit` for Unit 2. This is the "skip ahead" referenced in QA 1694.
- **Reed, 09-25 13:44:52.870 [O]:**
  1. Conversation 23 (Jasper) starts at 13:44:50.3 with `23:28`.
  2. Reed chooses `23:30` 2.5 s later.
  3. The export links `23:30 → 23:31` unconditionally, but `23:31` never appears and no `DialogueFinish 23` is logged.
  4. One second later Move inputs resume.

## Event Reconstruction

**Normal reference (control 09-23-26, quest 25, 15 minutes):**

`questActiveEvent:25` + `21:45` → `21:46–21:51` → **`8:2`** Classifier intro (5.6 s after `21:51`, no finish of conv 21) → `8:12` → 6 × (`26:0` → feedback → `26:141`) → `26:136` → `18:120–18:130` → Anderson `19:16…19:32` → Tera `21:60…21:76` → Jasper `23:28…23:38 → 23:41 → 23:42` LAUNCH DRONE → 7 drone scans with `18:136…18:167` → `18:169` → Toppo call `18:173–18:176` (entry 16) → Toppo `20:35 → 20:43/44/45 → 20:46 → 20:63` ARGUMENTATION → submit → `27:7` → `questFinishEvent:25` → `20:64…20:74` → `questActiveEvent:54` → conv 103 → `questFinishEvent:54` → `EndOfUnit 2`.

**Isabella:**

| Time (UTC) | Scene | eventType | Data / node | Meaning |
|---|---|---|---|---|
| 09-24 13:37:33.5 | Unit 2 Prod (Refactor) | questEvent | `questActiveEvent:25` | "Which Watershed?" starts |
| 13:40:13 | ″ | DialogueEvent | `8:12` | Classifier intro ends |
| 13:40:59–13:46:00 | ″ | DialogueEvent | `26:141` ×6, `26:138` ×6 | 6 correct, 6 wrong classifications |
| 13:46:09 | ″ | DialogueEvent | `26:136` | Classifier complete |
| 13:46:18 | ″ | DialogueEvent | `18:121` (script: entry 1 success) | DANI retrained |
| 13:47:15 | ″ | DialogueEvent | `18:130` (script: entry 2 active) | **Last known good** |
| 13:48:56 | ″ | — | last record of the session | session ends (class period) |
| 09-25 13:16:52.8 | MainMenu | gameStartEvent | — | new session |
| 13:17:00.4 | Unit 2 Prod (Refactor) | questEvent | `questActiveEvent:25` | checkpoint restored *inside* quest 25 |
| 13:17:0x–13:18:08 | ″ | DialogueEvent | `21:46` (+DialogueStart 21), `21:47`, `21:48`, `21:50`, `21:51` | quest-opening lines replay |
| 13:18:14 | ″ | DialogueEvent | DialogueFinish conv 21 | **First abnormal:** normal flow goes `21:51 → 8:2` with no finish |
| 13:18:14–13:19:01 | ″ | PlayerPositionEvent only | position fixed (1416, 102, 1105), **0 InputEvents** | frozen |
| 13:19:01 → 13:21:27 | ″ | (same sequence after reload) | `21:46…21:51` → Finish 21 (+9.6 s) → 0 inputs | frozen again |
| 13:21:34 | Unit 3 Dev | (scene load from MainMenu) | no `EndOfUnit 2`; quest 25 never finished | skipped ahead |

**Reed:**

| Time (UTC) | eventType | Data / node | Meaning |
|---|---|---|---|
| 09-24 13:24:36 | questEvent | `questActiveEvent:25` | first attempt |
| 13:31:51 / 13:37:21 | (reloads) | restored `questActiveEvent:22` + `:24` | **progress loss**: restore to the pre-quest-25 checkpoint |
| 09-25 13:29:43 | questEvent | `questActiveEvent:25` | second attempt |
| 13:38:51 → 13:44:35 | DialogueEvent | `26:136`, `18:130`, `19:32`, `21:76` | Classifier, Anderson, Tera: normal |
| 13:44:44.6 | DialogueEvent | Finish conv 21 | Tera conversation ends normally |
| 13:44:50.3 | DialogueEvent | `23:0`, Start 23, `23:28` | Jasper conversation starts (entry 4 gate passes) |
| 13:44:52.870 | DialogueEvent | `23:30` (reply "I need watersheds and sizes! Now!") | next node must be `23:31` |
| 13:44:53.887 | InputEvent | Move `w` | **movement resumes mid-conversation; `23:31` and Finish 23 absent** |
| 13:44:54 → 13:50:22 | InputEvent / Position | 482 inputs incl. **146 Interact**; within 3–15 units of Jasper (≈1416, 1134) at 13:44:43–13:45:23 and 13:46:33–13:46:53 | no further DialogueEvent in the session |
| 09-29 13:13:30 | (scene load) | Unit 3 Dev from MainMenu, no `EndOfUnit 2` | skipped ahead |

## Shared Patterns Across Affected Students

- **[O] Every Unit-2-affected student stops inside quest 25.** All nine Unit 2 students in QA 1693/1694/1697 reach `questActiveEvent:25` and **none** log `questFinishEvent:25`, `questActiveEvent:54` or `EndOfUnit 2`. Ella (control) and both internal runs complete them.
- **[O] Reload after the Classifier always produces the same frozen state** (`scripts/frozen_q25.py`):

  | Student | Issue | Classifier completed | Reloads into quest 25 | Outcome |
  |---|---|---|---|---|
  | Isabella | 1693 | 09-24 13:46:09 | 2 | frozen ×2 |
  | Corah | 1694 | 09-24 15:27:09 | 1 | frozen |
  | Molli | 1694 | 09-24 02:18:10 | 6 | frozen ×6 |
  | Katelyn | 1697 | 09-30 20:53:52 | 1 | frozen |
  | Walton | 1697 | 09-30 16:37:16 | 3 | frozen ×3 (one of them 62.6 minutes during class) |

  Each of the 13 sessions shows the same five replayed nodes (or a prefix of them, in two very short sessions), `DialogueFinish 21` 5.4–9.6 s after `21:51`, no conversation-8 node and **0 InputEvents**.
- **[O] Reloading before Classifier completion is recoverable.** Reed (09-24), Molli (09-24 01:55) and Liv (09-30 20:30) reloaded with quest 25 active but the Classifier unfinished. The game restored the earlier `questActiveEvent:22 + :24` checkpoint, the students replayed quests 24/22, and quest 25 later restarted cleanly through Tera's `21:45`. The difference in outcome lines up exactly with Classifier completion.
- **[O] The last pre-break step varies.** Students stopped after `18:130`, at the drone launch, after the ocean scan, after `18:141` and at `20:35`. This shows the freeze is not tied to the step the student had reached, only to whether the Classifier was done when the reload happened.
- **[I]** The same freeze explains the different classroom labels. The frozen screen is DANI's "argumentation module… retrain my argumentation algorithm" dialogue, and `21:46` also runs `ShowAlert("Error: Argumentation Points Cannot Be Classified")`. A teacher could reasonably call it "stuck after the Classifier" (Maryville) or "stuck at Argumentation" (Goodhue).

## Key Anomalies

1. **[O]** On every quest-25 reload, conversation 21 is resumed **at node 46** (the node after the quest-activation node `21:45`) and the player is teleported from the Unit 2 spawn (1096, 153, 1366) to about (1409–1423, 102, 1104–1135) near the camp.
2. **[O]** On reload, `DialogueFinish` for conversation 21 appears after `21:51`. The normal flow never logs a finish there because `21:51` links into conversation 8.
3. **[O]** No InputEvents for the rest of every frozen session (including a 62.6-minute session), while normal play produces inputs within about 1 s of any conversation end.
4. **[O]** Reed: a conversation stopped at a linked node with no continuation and no finish, and movement returned 1 s later. The hung-conversation scan (`scripts/hungdlg.py`) finds this signature exactly twice in all logs: here and in Ella's Unit 4 case.
5. **[O]** Checkpoint restores often lag the player's real progress, for example `questActiveEvent:22 + :24` restored while quest 25 was active. This costs time without blocking.
6. **[O, probably unrelated]** Isabella's file contains one crash record, `unhandled_rejection: "Permissions check failed"` (unit2, server time 09-23 13:22:20, at her first Unit 2 load). Most other crash records in the dataset are `Pointer Lock` rejections.
7. **[O, telemetry]** 92% of dialogue-node records delayed by more than 60 s (1,970 of 2,135, all classroom files) carry a **stale `data.conversationId/nodeId`**, while `eventKey` remains correct. All node identities in this report come from `eventKey`.

## Ranked Hypotheses

### H1 — Restoring "Which Watershed?" after the Classifier replays a conversation segment that dead-ends, leaving the player input-locked (**High**)

- **Hypothesis:** the Unit 2 checkpoint taken after Classifier completion restores quest 25 and then resumes conversation 21 at node 46. In the export, `21:51` links only to `8:0`, whose three children (`8:1`, `8:2`, `8:3`) all require `classifierDone == false`. With `classifierDone == true` persisted, the link has no valid target. The conversation ends, the Classifier UI/scene event (EventGuid on `8:2`) never runs, and player control is never handed back.
- **Evidence for:**
  - **[O]** 13/13 reload sessions show the identical sequence across 5 students and 2 schools.
  - **[O]** 0 inputs in every one.
  - **[O]** Conversation 8 never appears.
  - **[O]** The finish of conversation 21 appears only in this path.
  - **[O]** The export gating supports it (`scripts/dlgdb.py`; `OutgoingLinks` shows `21:51 → 8:0` as the only link into conversation 8).
  - **[O]** Reloads before Classifier completion restored an earlier checkpoint and worked.
- **Evidence against / gaps:**
  - The save contents are not logged, so `classifierDone` being persisted and the "resume at 21:46" behaviour are both **[I]**.
  - Mae completed the Classifier but her 10-01 reload restarted Unit 2 from quest 21 instead (see QA 1697).
  - We cannot see whether input is disabled or merely unlogged. The latter is unlikely, given heavy input logging in other stuck sessions.
- **Reproduction:**
  1. Complete the Classifier.
  2. Refresh the browser (or quit to the main menu and continue).
  3. Expect DANI's `21:46–21:51` lines plus the alert, then no control.
- **Verification:**
  - Before the reload, dump `Variable["classifierDone"]`, `Variable["classifierIntroduced"]` and the quest-entry states of "Which Watershed?".
  - After the reload, check `DialogueManager.isConversationActive`, the active input map, and whether the `8:2` scene event fires.
  - Add a `classifierDone == true` branch from `8:0` (e.g. to `8:10` → `18:120`), or skip the replay when entry 1 is already `success`, and re-test.

### H2 — In-session conversation hang after a reply (Reed, at Jasper) (**Medium**; one observation, but timely records)

- **Hypothesis:** under some interaction pattern a conversation stops advancing after a reply. The UI releases movement, but the conversation never ends, so the NPC cannot be re-engaged. Here it blocks entry 4 → `23:38` → drone.
- **Evidence for:**
  - **[O]** The sequence above: `23:30` with no `23:31`, no finish, movement after 1 s, and 146 unanswered Interact presses near Jasper.
  - **[O]** The same signature appears once more, in Ella's Unit 4 case.
- **Evidence against:**
  - It is a single Unit 2 instance.
  - The cause of the stop is invisible: Escape is not logged, and walking out of a proximity trigger is possible.
  - Reed was skipped before any reload, so we do not know whether a refresh would have fixed it.
- **Reproduction:**
  1. With entry 4 active, start Jasper's conversation and pick "I need watersheds and sizes! Now!" within about 2 s while holding W.
  2. Repeat, pressing Esc or Tab immediately after the reply.
  3. Check whether `23:31` plays and Jasper can be talked to again.
- **Verification:** log conversation stop/cancel events with a reason, and log when a conversation trigger is refused because a conversation is already active.

### H3 — The divergence originates earlier, in the checkpoint written during quest 25 (**Low–Medium**)

- **Hypothesis:** the checkpoint written after the Classifier stores a stale "active conversation = 21 @ 46" record. In the normal flow, conversation 21 never formally ends (it hands off to 8), so a conversation-state saver could retain it. That record would then drive the bad replay.
- **Evidence for:**
  - **[O]** The resume starts exactly at node 46.
  - **[O]** The normal flow has no `DialogueFinish 21`.
- **Evidence against:** this is pure inference, with no save telemetry. **[S]**
- **Verification:** inspect the saved conversation state, and check when the Unit 2 checkpoint is written (Classifier completion, entry-state change, or a timer).

### H4 — Classroom network/offline conditions cause the restore problems (**Low**)

- **Evidence against:**
  - **[O]** The restore type does not track offline status. Isabella's freezes have 0% delayed records; Molli's have 100%.
  - **[O]** Liv's checkpoint written while offline was still restored.
- Network buffering matters for telemetry quality, not for this freeze.

## Suggested QA Reproduction Steps

1. **Freeze (H1), main test.**
   1. Fresh account, Unit 2. Play to "Which Watershed?" and finish the Classifier, until DANI says "I can confirm my argumentation algorithm has been fully retrained".
   2. Refresh the browser tab (Chromebook / PWA if possible).
   3. *Expected if H1 holds:* DANI's argumentation-module lines replay with the "Error: Argumentation Points Cannot Be Classified" alert, then the player cannot move. Reload 3 times; it should repeat every time.
2. **Freeze at later steps.** Repeat step 1 but reload after each of:
   - Anderson's watershed talk;
   - Tera's talk;
   - "LAUNCH DRONE";
   - the ocean scan;
   - Toppo's call;
   - Toppo's "Deputy, I trust you've made good progress…".

   All should freeze identically.
3. **Negative control.** Reload in the middle of the Classifier (after 2–3 orbs). *Expected:* the game restores to "Getting the Band Back Together / Investigate the Temple" and quest 25 restarts normally.
4. **Workaround check.** In the frozen state, try Esc, Tab, M and clicking, to confirm nothing restores control. Then try the main-menu path the teachers used (load Unit 3) to confirm it bypasses the freeze.
5. **Jasper hang (H2).** As described under H2. Also try the same rapid-reply pattern on Anderson and Tera.

## Recommended Developer Investigation

1. **Unit 2 save/restore for quest 25:**
   - which quest states, quest-entry states and Lua variables are written;
   - **when** the checkpoint is written (the logs show it exists only after Classifier completion);
   - what the load path replays (resume of conversation 21 at node 46, the teleport to the camp).
2. **The `21:51 → 8:0` hand-off:** conversation-8 entry conditions (`classifierDone == false` on all branches) and the `EventGuid` scene events on `8:2` / `8:12` (likely the Classifier UI and camera). Add a completed-Classifier branch, or make restore skip completed entries.
3. **Controller/input restoration when a conversation ends with no valid link:** make sure `OnConversationEnd` always re-enables player control and closes any Classifier camera/cutscene state.
4. **Conversation lifecycle** for conversation 23 (`23:30 → 23:31`): response-menu handling under fast input and movement, and the proximity-trigger "stop on exit" settings.

## Logging Gaps

- No checkpoint-write or checkpoint-load event, and no snapshot of quest-entry states or key Lua variables (`classifierDone`, `classifierIntroduced`) in either.
- Quest **entry** state changes (`SetQuestEntryState`) are not logged, only quest-level active/finish. The quest-25 sub-steps had to be inferred from dialogue nodes.
- No conversation cancel/stop event with a reason, no "conversation link had no valid destination" event, and no "trigger refused: conversation already active" event.
- No player-input-enabled/disabled state event. A frozen player and an idle player look the same apart from positions.
- Escape and other keys outside the action map are not logged.
- Buffered uploads serialise **stale payloads**: `data.conversationId/nodeId`, `objectName` and `playerOrDrone`. Only `eventKey`, eventType, scene and timestamps can be trusted in delayed batches.
- There is no session identifier; sessions were derived from `gameStartEvent`.

## Confidence and Limitations

- **The logs prove:**
  - all affected students stalled inside quest 25;
  - every reload after Classifier completion produced the same non-recoverable state (13/13);
  - the Classifier conversation never started in those sessions and the player produced no input;
  - Reed's Jasper conversation stopped at `23:30` while he kept trying to interact.
- **The logs suggest** the dead-end `21:51 → 8:0` gating (via `classifierDone`) and a persisted "resume conversation" record as the mechanism.
- Neither can be confirmed without save-file or engine-state inspection.
- Only one QA 1693 student (Isabella) shows the freeze directly. Reed's stop is a different, single-occurrence mechanism.
- No same-build control reloaded inside quest 25, so the "reload is always fatal" claim rests on the affected group plus the export logic.
