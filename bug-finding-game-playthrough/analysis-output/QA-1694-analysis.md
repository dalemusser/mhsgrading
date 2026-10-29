# QA 1694 — Unit 3 Supply Run / Crate 1: Forensic Analysis (first pass)

*Logs: `players-logs-met-bugs/` (build string `20260914-`).*
*Comparison groups:*
- *normal-progression control: Ella Preble;*
- *skipped-but-unaffected: Katelyn, Taye, Liv, Mae, Walton;*
- *internal playthroughs 09-14-26-3 / 09-23-26.*

*Times: client `timestamp`, UTC, 2026. Lawyer2 class ≈ 13:10–13:50 UTC, Lawyer5 ≈ 15:08–15:50 UTC.*
*Labels: **[O]** observed · **[I]** inferred · **[S]** speculative.*

---

## Executive Finding

**[O]** All four students reached Supply Crate 1 normally in their **first** Unit 3 session. The failure appears only **after a reload that restores Supply Run (quest 16) as active**. In all **26 of 26** such sessions:
- the game emits `questActiveEvent:16`, then **no `DialogueEvent` of any kind** for the whole session;
- this holds even though the player spawns beside Tera and presses Interact up to 243 times;
- the upstream trigger `10:205` never fires, DANI's crate briefing `11:1` never fires, and **no crate interaction** is logged;
- the student repeatedly stands within 0.5–7 units of Crate 1.

Hypotheses A and B compared:
- **Unit 3 entry itself looks identical** for skipped and normally progressing students.
- **Five other skipped students (Goodhue) finished Supply Run without problems**, because they did it in one uninterrupted sitting.
- **Hypothesis A** (a Unit 3 restore defect) is therefore favoured: **Medium**.
- **Hypothesis B** (Unit 2 carry-over) cannot be excluded: **Low–Medium**. The two skipped students whose reload into quest 16 *did* work had left Unit 2 cleanly, while all four blocked students had left Unit 2 in a broken dialogue state. That difference is confounded by school and date (09-25…30 vs 10-05).

**[I] Why only the Maryville students hit it:** Supply Run straddled a session boundary for each of them.
- Corah and Molli were advanced with only 7–10 minutes of their session left.
- Reed reloaded 5 minutes in.
- Isabella finished it but was regressed to quest 16 by her next reload.

The Goodhue students needed 8–14 minutes for Supply Run and finished it in the same sitting.

## Reported Symptom

The tracker reports: Unit 3 / Supply Run / Crate 1 — "Players that were skipped ahead from Unit 2 after experiencing the above classifier or argumentation bug" (Maryville; Lawyer2: Reed Henggeler, Isabella Ruminer; Lawyer5: Corah Thompson, Molli Kelme). Status: Identified.

## Students and Log Mapping

| Student (tracker) | Log file | Confidence |
|---|---|---|
| Lawyer2 / Reed Henggeler | `lawyer2.read.henggeler.stratalog.logdata.json` | High (`read` ↔ Reed) |
| Lawyer2 / Isabella Ruminer | `lawyer2.isabella.ruminer.stratalog.logdata.json` | High |
| Lawyer5 / Corah Thompson | `lawyer5.corah.thompson.stratalog.logdata.json` | High |
| Lawyer5 / Molli Kelme | `lawyer5.molli.kelme.stratalog.logdata.json` | High |

**[O]** Corah's and Molli's Unit 2 logs show the post-Classifier freeze described in QA 1693. This is consistent with the tracker's statement that they experienced the Unit 2 bug before being skipped.

## Probable Failure Window

| Student | Last known good (first Unit 3 session) | Session boundary | First abnormal state |
|---|---|---|---|
| Isabella | 09-25 13:36:14 `questActiveEvent:17` (Supply Run finished via Tera's failure branch `10:199`) | 09-25 ≈13:50 (class end) | **09-29 13:14:23**: reload emits `questActiveEvent:16` (finished quest re-activated); no dialogue for 7 sessions |
| Reed | 09-29 13:16:41 `questActiveEvent:16` + `10:16` (quest just started; still at Tera's camp) | 09-29 13:18:30 reload (cause not visible) | **09-29 13:18:35**: restored `questActiveEvent:16`; no dialogue for 9 sessions |
| Corah | 09-24 15:48:27 "Push E To Grab Crate" (Crate 1 on the hoverboard) | 09-24 ≈15:48 (class end) | **09-25 15:25:54**: restored `questActiveEvent:16`; no dialogue for 8 sessions |
| Molli | 09-24 ≈15:47 `10:30` (first crate delivered correctly) | 09-24 ≈15:48 (class end) | **09-29 15:10:51**: restored `questActiveEvent:16`; no dialogue for 2 sessions |

## Last Known Good State

Normal Supply Run (identical in both internal runs and the six classmates who completed it), with gating from the dialogue export:

1. Talk to Tera (`10:3…10:15`).
2. `questActiveEvent:16` + `10:16` (`SetQuestState("Supply Run","active")`, entry 12 active).
3. Head upstream → **trigger `10:205`** (entry 12 success, entry 1 active).
4. At Crate 1 (≈305, −59, −104) → **DANI `11:0/11:1`** (condition: entry 1 active) → `11:2…11:11` (map briefing; `11:11` carries a scene event).
5. "Push E To Place Crate On Hoverboard" (Supply Crate 1) → "Push E To Grab Crate" → `10:29` "I see a crate coming" → `10:30` correct / `10:31` lost.
6. After 3 crates: `10:195` → `11:22` → Tera `10:198` (or failure branch `10:199`) → `questFinishEvent:16`.

The first Unit 3 sessions of all four students follow this sequence up to the point where the class period ended. Isabella went through to completion via the failure branch.

## First Abnormal State

Example: **Reed, 09-30 13:18–13:43**, the longest stuck session (25 minutes, timely uploads):

| Time (UTC) | eventType | Data | Note |
|---|---|---|---|
| 13:18:02 | gameStartEvent | — | |
| 13:18:06.4 | PlayerPositionEvent | (330.3, −73.0, 174.6) | spawn at Tera's camp |
| 13:18:06.8 | questEvent | `questActiveEvent:16` | restore |
| 13:18:20–13:18:28 | InputEvent | 25 × Interact (`e` / `leftButton`) | right after spawn, beside Tera: **no conversation** |
| 13:19:16–13:19:34 | Position / InputEvent | (274, −48, −128) → (323, −59, −90); ≈ 30 × Interact | within ≈ 25 u of Crate 1: **no `11:1`, no crate prompt** |
| … 13:43:27 | — | **243 Interact presses**, 10 position samples ≤ 25 u from Crate 1, **0 DialogueEvents, 0 ObjectInterEvents** | |
| 13:43:34 | (MainMenu → Unit 4 Dev) | — | moved on to Unit 4 |

Every other post-reload session of the four students has the same shape (`scripts/u3_blackout.py`, `scripts/crate1prox.py`):

| Student | Post-reload Unit 3 sessions | DialogueEvents | Crate ObjectInterEvents | Sessions reaching ≤ 10 u of Crate 1 | Interact presses near Crate 1 (max per session) |
|---|---|---|---|---|---|
| Isabella | 7 (09-29, 09-30) | **0** | **0** | 5 | 12 |
| Reed | 9 (09-29, 09-30) | **0** | **0** | 6 | 78 |
| Corah | 8 (09-25, 09-29, 09-30) | **0** | **0** | 7 | 59 |
| Molli | 2 (09-29, 09-30) | **0** | **0** | 1* | 53* |

\* Molli's 09-29 records were 78% offline-buffered, so their position payloads may be stale.

By contrast, **every session in which the dialogue system worked** produced dialogue within seconds of spawning. This includes the first sessions of all nine skipped students, Ella's and both controls'. Once at the crate, players needed only about 2 Interact presses to get the crate prompt.

## Event Reconstruction

**Isabella** (shows both the normal first session and the regression):

| Time (UTC) | Scene | eventType | Data | Meaning |
|---|---|---|---|---|
| 09-25 13:21:34 | Unit 3 Dev | (load from MainMenu) | no restore events | skipped in from Unit 2 (quest 25 still active, no `EndOfUnit 2`) |
| 13:24:21 | ″ | questEvent | `questActiveEvent:16` + `10:16` | Supply Run starts |
| 13:24:46 / 13:28:46 | ″ | DialogueEvent | `10:206` ×2 "Whoa there… upstream" | wrong direction (designed hint) |
| 13:29:13 / 13:29:30 | ″ | DialogueEvent | `10:205` / `11:1` | upstream trigger; DANI at Crate 1 |
| 13:30:34–13:30:46 | ″ | DialogueEvent / TopographicMapEvent | `11:11`, waypoint set | map briefing |
| 13:30:51 / 13:30:59 | ″ | ObjectInterEvent | "Push E To Place Crate On Hoverboard" (Supply Crate 1) / "Push E To Grab Crate" | **Crate 1 interaction works** |
| 13:31:35 | ″ | DialogueEvent | `10:31` "locator… aaaand it's gone" | crate lost (wrong river) |
| 13:33:16 → 13:34:08 | ″ | DialogueEvent / questEvent | `10:199` "we lost the video equipment…" → `questFinishEvent:16` | quest closes on the **failure branch after one lost crate** (design path) |
| 13:36:14 | ″ | questEvent | `questActiveEvent:17` | Pollution Solution |
| 09-29 13:14:23 | Unit 3 Dev | questEvent | `questActiveEvent:16` (after gameStart) | **regression**: finished quest re-activated |
| 09-29 13:14 → 09-30 13:18 | ″ | — | 7 sessions, **0 DialogueEvents**, 0 crate events, at Crate 1 in 6 sessions | blackout |
| 09-30 13:18:55 | Unit 4 Dev | (MainMenu) | — | moved on |

**Corah (first session, the in-progress case):** `questActiveEvent:16` 15:43:50 → `10:205` 15:45:12 → `11:1` 15:46:21 → Crate 1 on the hoverboard 15:47:59 → grab 15:48:27 → session ends (class). Every later session: restore `questActiveEvent:16`, then nothing.

## Unit 3 entry-state comparison (Hypothesis B, part 1)

| Aspect | Skipped Maryville (4) | Skipped Goodhue (5) | Normal (Ella, internal runs) |
|---|---|---|---|
| How Unit 3 was entered | MainMenu → Unit 3; no `EndOfUnit 2`; quest 25 never finished; quest 54 never activated | same | after `EndOfUnit 2` |
| Quest events at first Unit 3 load | none | none | none |
| Opening sequence (`10:1`, `10:2`, `10:224`, Tera `10:3…10:15`, `questActiveEvent:16`, `10:16`) | identical | identical | identical |
| Spurious `10:31` at scene load | not seen | Katelyn | Ella (not in internal runs) |
| `10:205`, `11:1`, crate prompts in the first session | ✓ | ✓ | ✓ |
| Supply Run completed in the first session | Isabella only (failure branch) | **all 5**, 6–10 min after quest start, in one sitting | ✓ |

**[O] No observable difference at Unit 3 initialisation.** Quest flags, NPC dialogue, triggers and crate interactions all behaved normally for skipped students until a reload.

## Reload comparison (Hypothesis B, part 2)

| | Maryville post-reload (26 sessions) | Taye 10-05 | Mae 10-05 | Walton 10-05 (Unit 3, later quest) |
|---|---|---|---|---|
| Restored state | `questActiveEvent:16` | `questActiveEvent:16` (regressed from 17) | `questActiveEvent:16` (regressed from 17) | `questActiveEvent:55` |
| Supply Run progress at save | started / at Crate 1 / 1 crate / completed via failure branch | completed (success branch) | completed (failure branch) | completed |
| How the student left Unit 2 | frozen post-reload state (Isabella, Corah, Molli) / hung Jasper conversation (Reed) | no freeze (13-min hole, then skip) | Unit 2 restarted from quest 21, then skip | frozen post-reload state |
| Dialogue after load | **none** | Tera `10:0 → 10:198` after 30 s | Tera `10:0 → 10:199` after 2 min | conversation 104 runs |
| Outcome | blocked | `questFinishEvent:16` in 54 s | `questFinishEvent:16` in 2 m 46 s | quest 55 + `EndOfUnit 3` |

**Closest pair: Isabella vs Mae.** Both finished Supply Run on Tera's failure branch, both reloaded during quest 17 and both were regressed to quest 16. Isabella got a total blackout; Mae re-finished the quest by talking to Tera. The remaining differences are the Unit 2 exit state, school and date.

## Shared Patterns Across Affected Students

1. **[O]** All four reached Crate 1 and triggered DANI's briefing in their first session. There is no evidence of an initialisation problem at Unit 3 start.
2. **[O]** All four had a session boundary while Supply Run was active (or regressed to active), and every reload restored `questActiveEvent:16`.
3. **[O]** After every such reload the dialogue system was silent: no ambient, NPC, trigger or briefing dialogue. Interact presses at Tera and at Crate 1 produced nothing.
4. **[O]** All four were moved to Unit 4 on 09-30 after 2–9 stuck sessions.
5. **[O] Timing exposure:**

   | Student | Moved to Unit 3 (UTC) | First session outcome |
   |---|---|---|
   | Corah | 09-24 15:41 | session ended 15:48 at Crate 1 |
   | Molli | 09-24 15:38 | session ended 15:48 after one crate |
   | Reed | 09-29 13:13 | reloaded at 13:18, 2 min after quest start |
   | Isabella | 09-25 13:21 | finished the quest at 13:34; the next reload regressed it |

   The five Goodhue students (moved 10-01 13:27–14:20) finished Supply Run 8–14 minutes after entering Unit 3, in the same sitting:

   | Student | Moved | Supply Run finished |
   |---|---|---|
   | Katelyn | 13:27 | 13:36 |
   | Taye | 13:46 | 13:54 |
   | Walton | 14:13 | 14:22 |
   | Liv | 14:15 | 14:27 |
   | Mae | 14:20 | 14:34 |

6. **[O]** The **quest-17 → quest-16 regression on reload** appears in 3 students (Isabella, Taye, Mae). **[I]** The Unit 3 checkpoint is not rewritten between quest 16's start and quest 18.

## Key Anomalies

1. **[O] Total dialogue blackout after reload with Supply Run active** (26/26 sessions, 4 students).
2. **[O] Finished quest re-activated on reload** (`questFinishEvent:16` → reload → `questActiveEvent:16`). This happens to affected and unaffected students alike, so the regression is not itself the blocker.
3. **[O] Supply Run can close after a single lost crate** (Isabella and Mae: `10:31` → Tera `10:199` → finish), without `10:195` (≥ 3 crates). The export conditions allow this ("entry 4 or 7 … failure"). It is a design path, worth confirming as intended.
4. **[O] Spurious `10:31` with start and finish 20 ms apart at Unit 3 scene load** (Katelyn, Ella, Walton ×2). It lies outside the U3P1 grading window (which starts at `10:1`), but it is a phantom "crate lost" event.
5. **[O, likely benign]** `unhandled_rejection: "A user gesture is required to request Pointer Lock."` crash records cluster at Unit 3 loads: Corah 09-24 15:41 and 09-25 15:33; Reed 09-29 13:45, 09-30 13:13 and 13:39. They also occur at loads that worked, so they are probably not causal.

## Ranked Hypotheses

### H-A — An independent Unit 3 restore defect: loading a checkpoint with Supply Run active leaves the dialogue system non-functional, so Crate 1 cannot progress (**Medium**)

- **Supporting evidence:**
  - **[O]** 26/26 post-reload sessions blacked out, across 4 students and 2 classes.
  - **[O]** Reed's save was taken 2 minutes after the quest started, before any crate interaction, and was still blocked. So the defect does not depend on how far into Supply Run the student was.
  - **[O]** The first sessions, entered by the same unusual skip, worked fully.
  - **[O]** Unit 3 entry state is indistinguishable from normal.
  - **[I]** The proximity-started conversations involved (`10:205`, `11:0`) have **no incoming links** in the export, so they depend entirely on scene trigger components and their persisted state.
- **Contradicting evidence:**
  - **[O]** Taye's and Mae's restores into quest 16 worked.
  - **[O]** No *non-skipped* student was observed reloading while Supply Run was active, so we lack the decisive control.
- **Reproduction:** see QA steps 1–3 (normal Unit 2 completion, then reload inside Supply Run).
- **Verification:**
  - After the reload, check `DialogueManager.IsConversationActive`, the current conversation, the enabled state of the `DialogueSystemTrigger`s for `10:205`, `11:0` and Tera, and any "Once / already fired" persistent flags.
  - Check whether the `11:11` scene event (EventGuid) enables the crates/hoverboard prompt.

### H-B — Carry-over from the abnormal Unit 2 exit: persistent dialogue state from the Unit 2 freeze/hang is re-applied when a Unit 3 checkpoint loads (**Low–Medium**)

- **Supporting evidence:**
  - **[O]** All 4 blocked students left Unit 2 with a broken conversation state: the dead-end `21:51 → 8:0` replay (Isabella, Corah, Molli) or the hung conversation 23 (Reed).
  - **[O]** The two students whose quest-16 reload worked had not left Unit 2 that way.
  - **[O]** The first Unit 3 session, where no checkpoint is applied ("no restore events"), always worked.
- **Contradicting evidence:**
  - **[O]** Walton left Unit 2 frozen, yet his later Unit 3 reload (at quest 55) had working dialogue.
  - **[O]** The confounders are not separable in this data: school (Maryville vs Goodhue) and dates (09-25–09-30 vs 10-05).
  - **[O]** Nothing unusual is visible at Unit 3 initialisation.
- **Reproduction:** QA step 4 (freeze Unit 2 → skip → start Supply Run → reload).
- **Verification:** diff the Unit 3 save of a skipped-from-frozen student against a normally progressing student (active-conversation record, Lua variables such as `classifierDone`, the quest-25 state, input/cutscene flags).

### H-C — Exposure: the skip timing made a mid-quest reload likely (**High** as a description, not a root cause)

- **[O]** The session timing above. Each Maryville student had a session boundary inside Supply Run, or right after it in Isabella's case; no Goodhue student did.
- This explains *who* met the defect, and is compatible with both H-A and H-B.

### H-D — Hidden build or server change between 09-30 and 10-05 (**Low**)

- **[O]** All blackouts occurred 09-25–09-30; both working quest-16 restores occurred on 10-05. The build string is truncated (`20260914-`) and cannot reveal a re-deploy.
- **[O] Against:** no event-schema change appears across dates, and the crash app version stays `2.8.1`.
- **Verification:** confirm the deployment history for MHS-Release_V1.0.0 between 2026-09-24 and 2026-10-05.

### H-E — Supply Run world triggers only (narrow form of H-A) (**Low** as the complete explanation)

- **Hypothesis:** only the upstream trigger / crate prompt fail to re-arm.
- **[O] Against:** Tera's own talk conversation also failed after reload, so the failure is broader than the crate triggers.

## Suggested QA Reproduction Steps

1. **H-A, normal path.**
   1. Complete Unit 2 normally and enter Unit 3.
   2. Talk to Tera until "My equipment crates landed upstream…" (`10:16`).
   3. **Refresh** before going upstream.
   4. *Expected under H-A:* no dialogue anywhere (Tera, upstream, Crate 1) and Crate 1 has no prompt.
2. **H-A, at the crate.**
   1. Same path, but go upstream and let DANI's crate briefing (`11:1…11:11`) play.
   2. Place Crate 1 on the hoverboard.
   3. Refresh.
3. **Regression path.**
   1. Finish Supply Run (both success and failure branches).
   2. Start "Pollution Solution" (quest 17), then refresh.
   3. *Expected:* quest 16 re-activates. Check whether talking to Tera re-closes it (as for Taye and Mae) or is silent (as for Isabella).
4. **H-B.**
   1. Reproduce the Unit 2 freeze (QA 1693 step 1).
   2. From the main menu, load Unit 3 (the teacher skip).
   3. Start Supply Run, then refresh at the same points as steps 1–3. Compare with steps 1–3.
5. **Timing.** Run steps 1–2 on a school Chromebook in PWA mode, closing the lid instead of refreshing, to mirror the end-of-class pattern.

## Recommended Developer Investigation

1. **Unit 3 checkpoint/restore.**
   - What is saved at the quest-16 checkpoint.
   - Why the restore re-activates quest 16 when quest 17 is active (no checkpoint between quests 16 and 18?).
   - What runs on load: resumed conversations, re-enabled triggers, scene events.
2. **Dialogue System state on load.**
   - Is a conversation left "active" (blocking all others)?
   - Are the `DialogueSystemTrigger`s for Tera (`10:0`), upstream (`10:205`) and DANI-at-crate (`11:0`) enabled, and are their conditions true? Entry 12 / entry 1 states are needed.
3. **Crate interactables:** whether the "Push E To Place Crate On Hoverboard" prompt is enabled by a dialogue scene event (`11:11`, EventGuid) that a restore never replays.
4. **The Unit 2 → Unit 3 skip path:** what the main-menu unit load writes into the persistent Dialogue System data (H-B).
5. **Design check:** Supply Run closing on the first lost crate (`10:199` condition).

## Logging Gaps

- **Most important:** a checkpoint save/load event, plus a "dialogue system state" snapshot on load (active conversation, enabled triggers).
- Trigger evaluations: a trigger was entered, its condition was false, or it was refused because a conversation is active. Without these, a dead trigger and an unvisited trigger look the same except through positions.
- Quest-entry state changes.
- Interact attempts carry no target. An `InputEvent` Interact should say what (if anything) was in range.
- Unit selection from the main menu (the skip) is not logged explicitly. It was inferred from MainMenu → Unit 3 without `EndOfUnit 2`.
- Stale payloads in offline batches (Molli's positions and object names).

## Confidence and Limitations

- **The logs prove:**
  - the four students could interact with Crate 1 in their first session;
  - after every reload with Supply Run active, they had no dialogue and no crate interaction at all, even while standing at the crate and pressing Interact repeatedly;
  - five other skipped students finished Supply Run without a reload.
- **The logs suggest** a restore-time failure of the dialogue/trigger system (H-A). They cannot exclude a Unit 2 carry-over component (H-B), because every blocked student also had a broken Unit 2 exit and the two successful quest-16 restores came from a different school and a later date.
- A single QA run of steps 1 and 4 should separate H-A from H-B.
