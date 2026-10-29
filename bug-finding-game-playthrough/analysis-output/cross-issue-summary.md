# Cross-Issue Summary — Classroom Bug Forensics (first pass, 2026-10-06)

*Scope: QA 1693 (U2 Classifier), QA 1694 (U3 Supply Run / Crate 1), QA 1697 (U2 Argumentation), and the U4 Saving Cadet Anderson report.*
*Data:*
- *10 classroom logs (MHS-Release_V1.0.0, build string `20260914-`, 2026-09-18 → 10-05);*
- *2 internal playthroughs on the same build string as controls;*
- *the 2026-09-21 dialogue-database export, for node text, conditions and links.*

*Labels: **[O]** observed · **[I]** inferred · **[S]** speculative.*

---

## The picture in one paragraph

The four tickets come down to **two ways a conversation-driven quest can stop progressing**, both made visible by how often classroom play is interrupted (class periods end, Chromebooks sleep, students refresh):

- **Restore-time dead states:** loading a checkpoint *inside* a multi-step quest.
  - **Unit 2 "Which Watershed?":** the restore replays a quest-opening conversation whose hand-off to the Classifier is gated off for students who already finished it. The player is left input-locked. This is **QA 1693 and QA 1697, one defect.**
  - **Unit 3 "Supply Run":** after the restore no dialogue fires at all, so Crate 1 can never be used. This is **QA 1694**.
- **In-session conversation hangs:** a conversation stops after a node that should continue, no end event is logged, movement returns, and the NPC no longer responds.
  - **Unit 4 Saving Cadet Anderson:** right after a Pause press. Only a refresh helps.
  - **Unit 2 Jasper (Reed):** after a fast reply.

The student-level evidence is strong and consistent:
- **13/13** post-Classifier reloads froze;
- **26/26** post-reload Supply Run sessions had zero dialogue;
- the hang appears **2/2** times with the same signature.

The **exact code mechanism is inferred** from the dialogue export and needs engine-side confirmation.

## Issue-by-issue verdict

| Issue | What the logs show | Mechanism (confidence) | Students showing it |
|---|---|---|---|
| QA 1693 | All Unit-2 students stall inside quest 25. After a reload with the Classifier done, `21:46…21:51` replays → Finish 21 → no conversation 8 → 0 inputs | **Restore dead-end + input lock** (High that it is the blocker; Medium-High for the `classifierDone` gating detail) | Isabella; also Corah and Molli (listed under 1694) |
| | Reed: Jasper conversation hung at `23:30` | **In-session conversation hang** (Medium, one case) | Reed |
| QA 1697 | Nobody reached the argument; the same freeze as QA 1693 | **Same defect as QA 1693** (High for Katelyn and Walton) | Katelyn, Walton |
| | Mae's reload restarted Unit 2; Taye had a 13-min telemetry hole; Liv was idle then skipped | Separate or unclear (Low) | Mae, Taye, Liv |
| QA 1694 | First Unit 3 session normal; every reload with quest 16 active → **no dialogue at all**, Crate 1 dead | **Restore-time dialogue blackout** (Medium for "independent U3 defect"; Low–Medium for Unit 2 carry-over) | Isabella, Reed, Corah, Molli |
| U4 Anderson | Door conversation stopped at `82:5` right around a Pause press; next objective never set; 5 h stuck; refresh not in export | **In-session conversation hang** (Medium-High for this case) | Ella |

## Student outcome matrix

| Student (class) | Unit 2 stop | Unit 2 blocker in log | Moved to U3 (no `EndOfUnit 2`) | Unit 3 Supply Run | Unit 4 |
|---|---|---|---|---|---|
| Isabella (L2) | after `18:130` | restore freeze ×2 | 09-25 13:21 | done (failure branch) → reload regressed to 16 → **blackout ×7** | in progress (no issue seen) |
| Reed (L2) | at Jasper `23:30` | conversation hang | 09-29 13:13 | reload 5 min in → **blackout ×9** | in progress |
| Corah (L5) | after drone launch | restore freeze ×1 | 09-24 15:41 | at Crate 1, class ended → **blackout ×8** | completed U4 and U5 |
| Molli (L5) | after ocean scan | restore freeze ×6 | 09-24 15:38 | 1 crate, class ended → **blackout ×2** | completed U4 |
| Katelyn (M1) | after `18:141` | restore freeze ×1 | 10-01 13:27 | completed in one sitting | completed (wasm crash → refresh in quest 41) |
| Taye (M1) | after `18:141` | 13-min record hole | 10-01 13:46 | completed; later reload regressed 17→16, re-finished via Tera | — |
| Liv (M2) | after `18:141` | none visible | 10-01 14:15 | completed in one sitting | in progress |
| Mae (M2) | after `18:166` | reload restarted Unit 2 | 10-01 14:20 | completed; later reload regressed 17→16, re-finished via Tera | — |
| Walton (M2) | at Toppo `20:35` | restore freeze ×3 | 10-01 14:13 | completed in one sitting | in progress |
| Ella (M1, control) | — (completed U2, 51 min on the argument) | — | after `EndOfUnit 2` | completed | **hung door conversation** (`82:5`) |

## Shared failure mechanisms

### M1 — Loading a checkpoint inside certain multi-step quests produces a dead state **[O]**

| Restore point (quest active at load) | Sessions | Outcome |
|---|---|---|
| 25 "Which Watershed?", Classifier already completed | 13 (5 students) | **frozen**: conversation 21 replays from node 46 → Finish 21 → no Classifier → 0 inputs |
| 22 / 22+24 / 23 (checkpoints before quest 25) | 20 (Reed, Corah, Molli, Isabella, Liv, Taye) | normal (quests replayed; progress lost) |
| 16 "Supply Run" (Maryville, 09-25…09-30) | 26 (4 students) | **dialogue blackout**: 0 DialogueEvents, no crate prompt |
| 16 "Supply Run" (Goodhue, 10-05; quest previously completed) | 2 | normal (Tera re-closes the quest) |
| 18 / 55 / finished-16 (Unit 3, later quests) | 4 (Ella, Liv, Walton ×2) | normal |
| 36 Saving Cadet Anderson (inside the base) | 2 | normal (`82:41` replays) |
| 39 / 41 / 48 (Unit 4) | 10 | normal (progress may be lost, e.g. Isabella 47 → 39 three times) |
| 43 / 45 / 51 (Unit 5) | 5 | normal |
| 29 / 32 (Unit 1) | 2 | normal |

*Counts: `scripts/reloads.py`; a restore = quest events emitted within 15 s of the scene load after a `gameStartEvent`.*

**[I]** The two failing restores share a design feature: the next required step depends on dialogue that a restore does not replay correctly.
- **Unit 2:** a cross-conversation link `21:51 → 8:0` whose branches all require `classifierDone == false`.
- **Unit 3:** proximity-started conversations (`10:205`, `11:0`) with **no incoming links in the export**, plus scene events attached to dialogue nodes (`11:11`, `8:2`, `18:130`, `23:42`, `20:63` carry `EventGuid` scene events).

The working restores (quests 36, 48) replay a conversation that has valid branches for the restored state.

### M2 — Conversations can hang mid-branch while the player regains control **[O]**

The signature is a node with an outgoing link, then no next node, no `DialogueFinish`, movement inputs within 1–2 s, and no later dialogue despite repeated Interact presses. It was found **twice**:
- Ella `82:5`, 3.4 s before a Pause (Tab) press;
- Reed `23:30`, 2.5 s after the conversation started, while holding a movement key.

It never appears in the internal runs. In both cases the skipped nodes held the script that activates the next objective (`82:14`; Jasper's `23:38`).

### M3 — Checkpoints are sparse; restores often lag the player's real progress **[O]**

- **19 reloads** re-activated a quest that the log had already shown finished, including **one in the internal control run** (09-25, quest 23).
- Typical lags:
  - quest 25 → `A22+A24`;
  - quest 17 → `A16` (Isabella, Taye, Mae);
  - quest 47 → `A39`;
  - quest 50 → `A48`.
- **[I]** This is the design rather than a defect, but it is what puts players back *inside* the vulnerable quests of M1.

## Cross-cutting findings

| Topic | Finding |
|---|---|
| **Common missing transitions** | `21:51 → 8:x` (U2 freeze); *any* dialogue after an `A16` restore (U3); `82:5 → 82:6` and `23:30 → 23:31` (hangs) |
| **Common reload behaviour** | A reload re-emits the checkpoint's `questActiveEvent` and sometimes replays the quest's opening conversation (U2 `21:46`, U4 `82:41`). It never restores fine-grained progress (quest entries, NPC talks done) *inside* a quest beyond what the checkpoint held. Refresh *fixes* a hang (U4) but *causes* the U2/U3 dead states |
| **State inconsistencies** | Finished quests re-activated (19×). `DialogueFinish 21` only in the restored path. Supply Run can close after one lost crate (design path; Isabella, Mae) |
| **Save/load problems** | M1 and M3. Mae's reload restored **no** Unit 2 checkpoint (Unit 2 replayed from quest 21). Liv's reload placed her at quest 18 in the dungeon although her last logged state was mid-argument in quest 17 (records may be missing, or the save moved forward) |
| **Scene initialisation** | First entry into every unit initialised normally for skipped and non-skipped students alike. Minor: a phantom `10:31` "crate lost" line fires at some Unit 3 loads (Katelyn, Ella, Walton); quick unit → MainMenu → unit bounces at some first loads |
| **Interaction-order problems** | Pause during a line (U4), a fast reply while moving (U2 Jasper). No evidence that interaction order *before* the Classifier matters: the freeze depends only on Classifier completion at reload time |
| **Persistent-state problems** | Restored Lua and quest state is internally inconsistent with the replayed dialogue (U2). Restored quest-16 state leaves the dialogue system silent (U3). Exact persisted contents are not observable |
| **Unit 2 ↔ Unit 3** | All 9 Unit-2-affected students were moved to Unit 3 from the main menu with quest 25 still active and no `EndOfUnit 2`. Unit 3 initialisation was indistinguishable from normal, and the 5 Goodhue students finished Supply Run normally. The Maryville blackout appears only after a reload inside Supply Run. **Unit 3 defect favoured (Medium)**; carry-over not excluded (all 4 blocked students left Unit 2 in a broken dialogue state, and the only clean quest-16 restores were at another school on a later date) |

## Telemetry integrity (affects every analysis of classroom data)

1. **[O] Offline buffering is pervasive in the classroom and absent in the controls.**
   - In 9 of 10 classroom files, 777–5,204 records reached the server more than 5 minutes after their client time (up to 144 h). Corah's file is the exception, with 11.
   - Taye's *median* lag is 2.1 h.
   - The internal runs have none.
2. **[O] Buffered records carry stale payloads.**
   - 92% of delayed `DialogueNodeEvent`s (1,970 of 2,135) have a `data.conversationId/nodeId` different from their `eventKey`, against 0.8% of timely ones.
   - `ObjectInterEvent.objectName` and `InputEvent.playerOrDrone` are also stale in those batches.
   - **[I]** The payload object is serialised at upload time, not at event time.
   - **`eventKey`, eventType, scene and timestamps are reliable**; every node identity in these reports comes from `eventKey`.
   - **For this repo's grading pipeline:** rules keyed on `eventKey` are safe. Anything that reads `data.conversationId/nodeId`, `objectName`, `playerOrDrone` or positions from classroom data must treat delayed records as unreliable.
3. **[O] Duplicates on resend:** a record delivered before Katelyn's crash was delivered again after the refresh (`92:62`, same client timestamp).
4. **[O] Other limits:**
   - crash records have no client timestamp;
   - the build string is truncated (`20260914-`), so a silent re-deploy between 09-30 and 10-05 cannot be ruled out;
   - there is no session ID;
   - the refresh in the U4 case is not in the export.

---

### Top 3 Most Promising Reproduction Experiments

1. **Post-Classifier refresh in Unit 2 (QA 1693 + 1697).**
   1. Complete the Classifier in "Which Watershed?" ("…fully retrained").
   2. Refresh.
   3. *Prediction:* DANI's "argumentation module" lines and the "Error: Argumentation Points Cannot Be Classified" alert replay, then the player cannot move, every time.
   4. *Control:* refresh mid-Classifier → restore to quests 22/24 and normal replay.
   5. One run confirms or kills the main hypothesis; also inspect `classifierDone` before and after.
2. **Refresh inside Supply Run, normal versus skipped history (QA 1694).**
   1. (a) After a normal Unit 2 completion, talk to Tera ("crates landed upstream…") and refresh; then do the same at Crate 1.
   2. (b) Repeat on an account that reached Unit 3 via the Unit 2 freeze and a main-menu skip.
   3. *Prediction under H-A:* both lose all dialogue.
   4. *Prediction under H-B:* only (b) does.
   5. Also: finish Supply Run, start quest 17, refresh → does Tera re-close quest 16?
3. **Pause during a conversation line (U4, generalising to all NPC dialogue).**
   1. At Anderson's base door, press Tab while "[Sahara 1] is experiencing catastrophic failure…" is shown, then resume.
   2. *Prediction:* the next line never plays, the player can walk, and the fountain cannot be used; refresh restores progress.
   3. Repeat with Esc, alt-tab, and the fast-reply-while-moving pattern at Jasper (Unit 2).

### Top 3 Code/State Areas to Inspect

1. **Checkpoint save/restore of Dialogue System state.**
   - What is written (quest states, **quest-entry states**, Lua variables such as `classifierDone` / `suppliesRecovered_U3`, any saved "active conversation") and **when** (the Unit 2 checkpoint appears only after Classifier completion; Unit 3 is not rewritten between quests 16 and 18).
   - What the load path replays: conversation 21 resumed at node 46; teleport to the camp; why an `A16` restore leaves every conversation trigger silent.
2. **Conversation hand-offs and gating that ignore restored state.**
   - `21:51 → 8:0` with all branches requiring `classifierDone == false`: add a completed branch (e.g. `8:10` → `18:120`) or skip the replay when entry 1 is already `success`.
   - The `EventGuid` scene events on `8:2/8:12/18:130/23:42/20:63/11:11/10:195` that set up world state and are never replayed on restore.
   - The proximity triggers `10:205` / `11:0` / `82:0` and their persisted "once / fired" flags.
3. **Conversation lifecycle under interruption and controller ownership.**
   - Pause-menu open/close during a subtitle, fast reply selection, movement during a conversation, and conversations that end through a dead link.
   - Guarantee that a conversation either advances or ends cleanly: emit the end event, release the "conversation active" lock, and re-enable the player controller exactly once.

### Highest-Value Additional Telemetry

1. **Checkpoint events:**
   - `checkpointSaved` and `checkpointLoaded`, each with checkpoint ID, unit, quest states, **quest-entry states**, key Lua variables, and any resumed conversation;
   - a `sessionId` on every record, plus a "first record after load" marker.
2. **Dialogue lifecycle events:**
   - quest-entry state changes (`SetQuestEntryState`);
   - conversation stop/cancel with a reason;
   - "link had no valid destination";
   - "trigger entered / condition false / refused because a conversation is active";
   - player-controller and input-map enable/disable;
   - pause-menu open/close.
3. **Telemetry hygiene:**
   - serialise payloads **at event time** (fixes the stale `data` fields);
   - a per-record UUID for de-duplication;
   - the full build number (not `20260914-`);
   - client timestamps on crash records;
   - page `visibilitychange` / `beforeunload` events, to tell hangs from hidden tabs and to capture refreshes.

## Confidence and limitations

- **Proven by the logs:**
  - where every affected student stopped;
  - that all U2-affected students stalled inside quest 25;
  - the 13/13 freeze and 26/26 blackout signatures;
  - that Unit 3 initialisation looked normal for skipped students;
  - that five skipped students completed Supply Run;
  - the two hung-conversation events and the Pause timing in the U4 case.
- **Suggested, not proven:**
  - the `classifierDone` gating as the cause of the U2 freeze;
  - why the U3 restore silences dialogue;
  - Pause as the trigger of the U4 hang;
  - the H-A vs H-B split for QA 1694.
- **Not observable:** save contents, engine state, what was on screen, teachers' notes (`#VALUE!`), and the U4 refresh itself.
- No unaffected classmates' logs were provided beyond the comparison groups listed above.
