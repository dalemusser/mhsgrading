# Unit 4 — Saving Cadet Anderson (refresh-resolved): Forensic Analysis (first pass)

*Log: `meyer1.ella.preble.stratalog.logdata.json` (build string `20260914-`).*
*Comparisons: five classmates who reached the same quest (Katelyn, Liv, Walton from Goodhue; Corah, Molli from Maryville) and the internal playthroughs 09-14-26-3 / 09-23-26.*
*Times: client `timestamp`, UTC, 2026-10-05.*
*Labels: **[O]** observed · **[I]** inferred · **[S]** speculative.*

---

## Executive Finding

**[O]** Ella's Saving Cadet Anderson conversation at Anderson's base door **stopped after its fourth line** (`82:5`, the "[Sahara 1] is experiencing catastrophic failure…" alarm) **3.4 seconds before she pressed Pause (Tab)**. It never continued and never logged an end. Within 2 seconds she could move again. For the rest of the session (about 5 hours, until the log ends at 18:51) she pressed Interact 41 times around the base (29 right away, 12 more about 5 hours later), but **no dialogue and no object interaction ever happened again**.

**[I]** The line that hands the player the next objective, `82:14` ("We will return shortly. Marking a waypoint."), never ran. In the dialogue export `82:14` is the only node that sets entry 1 success / entry 2 active, and the fountain step (`82:26`) requires entry 2. So the quest could not advance. A refresh plausibly cleared the hung conversation and replayed the door conversation.

**[O]** All seven other runs of this scene played `82:5 → 82:6` automatically about 5 s later:
- five classmates;
- the two internal playthroughs.

None of them pressed Pause. The same "hung conversation" signature (linked node, no continuation, no end, player regains movement, NPC unresponsive) appears exactly once elsewhere in the dataset, in Reed's Unit 2 Jasper conversation (QA 1693).

**The refresh itself is not in this export.** There is no new game start after 13:20 on 10-05, so the post-refresh state cannot be compared directly.

## Reported Symptom

The tracker reports: Unit 4 / Saving Cadet Anderson — "Unsure, got around by refreshing" (Goodhue, Meyer1: Ella Preble). Email date 2026-10-05. Status: New. No Hansoft ID.

## Students and Log Mapping

| Student (tracker) | Log file | Confidence |
|---|---|---|
| Meyer1 / Ella Preble | `meyer1.ella.preble.stratalog.logdata.json` | High (exact name and class; Meyer1 account batch) |

## Probable Failure Window

**10-05 13:56:29.672 – 13:56:35** is the window from `82:5` to the first movement input after the Pause press.

## Last Known Good State

**[O]** Ella's Unit 4 had progressed normally up to this point:

1. 13:20:33: loaded Unit 4 from the main menu, after `EndOfUnit 3` on 10-01.
2. 13:24:01: `questActiveEvent:39`.
3. 13:30–13:48: Power Play dungeon floors 1–5 (quests 46 → 50).
4. 13:48:27: `questActiveEvent:40`; drill `107:5` → `107:9`.
5. 13:54:00: `questFinishEvent:40`.
6. 13:54:05–13:54:28: Anderson's emergency call `82:15…82:22` → `questActiveEvent:36` + `82:24` "Affirmative. Placing waypoint." (sets the quest active and entry 1 active) → DialogueFinish 82 at 13:54:31.
7. She travelled about 1,500 units to Anderson's base and, at 13:56:03, the door conversation started (`82:0`) at (1438.3, −84.5, −720.9).

The last known good node is **`82:5` at 13:56:29.672**.

## First Abnormal State

**[O] 13:56:33.036, `InputEvent` Pause (key `tab`)**, while `82:5` was displayed:
- From 13:56:35 Move/Sprint inputs are logged and positions change. Normally the player is locked during a conversation.
- **No `82:6`** "CAN. ANYONE. HEAR. ME?" (unconditional link from `82:5`).
- **No `DialogueFinish` for conversation 82.**
- No further `DialogueEvent` of any kind for the rest of the log.

## Event Reconstruction

**Pre-refresh window (Ella; all records timely, 0 of 465 delayed):**

| Time (UTC) | Scene | eventType | Data | Note |
|---|---|---|---|---|
| 13:54:28.268 | Unit 4 Dev | questEvent | `questActiveEvent:36` | Saving Cadet Anderson |
| 13:54:28.274 | ″ | DialogueEvent | `82:24` (script: quest active, entry 1 active) | waypoint to the base |
| 13:54:31.087 | ″ | DialogueEvent | DialogueFinish 82 | |
| 13:54:32–13:56:00 | ″ | Position / InputEvent | (−88, −19, −323) → (1438, −85, −721) | travel |
| 13:56:03.499 | ″ | DialogueEvent | `82:0` + DialogueStart 82 | base-door conversation |
| 13:56:20.422 | ″ | DialogueEvent | `82:1` "I like it—looks cozy!" (cond: entry 1 active) | player reply chosen |
| 13:56:27.055 | ″ | DialogueEvent | `82:3` "That is one adjective that may be applicable." | |
| **13:56:29.672** | ″ | DialogueEvent | **`82:5`** "[Sahara 1] is experiencing catastrophic failure…" | **last node** |
| **13:56:33.036** | ″ | InputEvent | **Pause, key `tab`** | |
| 13:56:35 → 13:58:31 | ″ | InputEvent | Move / Sprint / Hoverboard; **29 × Interact** (13:56:46–13:58:31) | movement re-enabled; **no dialogue** |
| 13:56:46 → 13:58:31 | ″ | PlayerPositionEvent | 1435–1548, −85, −700…−725 (around the door) | |
| 13:58:36 → 14:30:37 | ″ | PlayerPositionEvent (sparse) | fixed at (1438.5, −85.1, −722.2) | idle |
| 14:30:37 → 18:49:45 | — | **259-minute gap** | | tab hidden / device asleep **[I]** |
| 18:49:45 → 18:50:14 | ″ | InputEvent | 12 × Interact; movement to (1548, −85, −706) | another attempt; **no dialogue** |
| 18:51:25 | ″ | PlayerPositionEvent | last record in the export | **no refresh logged** |

**Successful reference** (`scripts/q36_conv82.py`; identical in Katelyn, Liv, Walton, Corah, Molli and both internal runs):

```text
questActiveEvent:36 → 82:24 → [travel] → 82:0 → 82:1|82:2 → 82:3|82:4 → 82:5 → 82:6 → 82:7 → 82:8 → 82:9
→ 82:10|82:11 → 82:12|82:13 → 82:14 (entry 1 success, entry 2 active)
→ [fountain] ObjectInterEvent "Press E to deactivate the fountain" + 82:26 (cond: entry 2 active) → 82:27 → 82:28 (entry 3 active)
→ [door] 82:29 … 82:40 (entry 4 active) → scene "Unit 4 Dev - Anderson Base" → questActiveEvent:36 → 82:41 …
```

```text
Ella:  questActiveEvent:36 → 82:24 → [travel] → 82:0 → 82:1 → 82:3 → 82:5 → PAUSE → (nothing)
```

**Post-refresh window:** not present in the export. The last uploaded record is 18:51:27 client / 18:51:28 server, and no `gameStartEvent` exists after 13:20:04.

## Shared Patterns Across Affected Students

Only one student is listed. Related observations from the rest of the dataset:

- **[O] Hung-conversation signature, 2 occurrences in 10 logs and 0 in the internal controls** (`scripts/hungdlg.py`):

  | | Ella, Unit 4 | Reed, Unit 2 |
  |---|---|---|
  | Last node | `82:5` | `23:30` |
  | Linked node that never played | `82:6` | `23:31` |
  | Silence afterwards | 295 min | 95 h (session ended) |
  | Interact presses | 41 | 146 |

  Both stopped at a node that has an outgoing link, logged no continuation and no conversation end, gave movement back to the player, and left the NPC unresponsive.
- **[O] Pause pressed during a conversation: 2 timely occurrences in all logs.**
  - Reed at `74:4`, a node with **no** outgoing link: his conversation finished normally 7.4 s later.
  - Ella at `82:5`, a node **with** an outgoing link: the conversation never continued.
- **[O] Restores *inside* quest 36 work.** Corah and Molli reloaded inside Anderson's base (10-02). The game restored `questActiveEvent:36` and replayed `82:41`, and both finished the quest normally. This differs from quests 25 and 16 (QA 1693/1694).
- **[O] A second Unit 4 "refresh" in the same class, same day (not this quest):**
  - Katelyn hit a WebGL/wasm crash (`RuntimeError: memory access out of bounds`, server time 15:00:06) in Desert Delicacies (quest 41), 0.5 s after `92:62` at Garden Box 3.
  - She refreshed at 15:01:07, was restored to `questActiveEvent:41`, and finished Unit 4 at 15:12.
  - **[I]** If the teacher's note conflates the two events, "refresh fixed it" may also describe Katelyn's crash.

## Key Anomalies

1. **[O]** The door conversation stopped at `82:5`; no `82:6` and no DialogueFinish.
2. **[O]** Pause was pressed 3.4 s after `82:5`, and movement resumed about 2 s later while the conversation was unfinished.
3. **[O]** 41 Interact presses over two attempts (29 at 13:56–13:58, 12 at 18:49–18:50) near the base door and fountain area produced **no** `DialogueEvent` and **no** `ObjectInterEvent`.
4. **[O]** The game stayed in this state for about 5 hours without a reload.
5. **[O]** There is no refresh in the export, even though the tracker reports one.

## Ranked Hypotheses

### H1 — Pausing during a conversation line hangs the conversation, re-enables movement, and blocks the next quest step (**Medium–High** for this case; single observation)

- **Hypothesis:** opening and closing the pause menu while `82:5` was on screen stopped the sequencer/subtitle from advancing (or stopped the conversation without an end callback), and returned player control.
  - The conversation stays "active", so the base-door trigger and the fountain conversation cannot start.
  - `82:14` never runs, so entry 2 (fountain) is never activated.
  - A refresh discards the hung conversation; walking back to the door replays `82:0` (entry 1 is still active) and the quest proceeds.
- **Evidence for:**
  - **[O]** The exact timing.
  - **[O]** The unique deviation versus 7 comparison runs.
  - **[O]** No dialogue at all for 5 hours despite 41 Interact presses.
  - **[O]** Export gating (`82:5 → 82:6` unconditional; `82:14` is the only setter of entry 2; `82:26` needs entry 2).
  - **[O]** The Pause during a terminal node (Reed `74:4`) was harmless, as expected if the problem is "the next node never starts".
- **Evidence against:**
  - **[O]** Only one occurrence.
  - Escape and window-focus changes are not logged, so other interrupting inputs cannot be excluded.
  - The post-refresh confirmation is missing.
- **Reproduction:** QA steps 1–3.
- **Verification:**
  - After Tab → resume, check `DialogueManager.IsConversationActive`, the current entry, `Time.timeScale`, and the player-controller enabled state.
  - Check whether the pause handler calls `StopConversation`, hides the dialogue UI, or toggles input maps.

### H2 — A general conversation-hang defect, not specific to Pause (**Medium**)

- **Hypothesis:** any interruption, such as a fast reply, movement or focus change, can leave a conversation stuck after a linked node.
- **Evidence for:** **[O]** Reed's Jasper conversation hung with the same signature and **no** Pause press.
- **Evidence against:** two occurrences in ten classroom logs and many thousands of normal node transitions.
- **Reproduction:** QA step 4.

### H3 — The base-door trigger cannot re-fire after an interrupted conversation (**Low–Medium**, contributes to H1/H2)

- **Evidence for:** **[O]** Ella left the door area (about 100 units) and returned twice without `82:0` restarting, although `82:1`'s condition (entry 1 active) should still hold.
- **Evidence against:** it is indistinguishable from "a conversation is still active" (H1).
- **Verification:** check the trigger's "once" / persistence settings and whether a still-active conversation blocks it.

### H4 — WebGL instability on classroom Chromebooks (**Low** for Ella; relevant for Katelyn)

- **Evidence:**
  - **[O]** Katelyn's wasm out-of-bounds crash on the same day; refresh recovered.
  - **[O]** Ella has no crash record and her heartbeat continued, so her client did not crash.

## Suggested QA Reproduction Steps

1. **Pause during the alarm.**
   1. Play to Saving Cadet Anderson and walk to the base door.
   2. When "[Sahara 1] is experiencing catastrophic failure…" appears, press **Tab** (pause), wait 2 s, and resume.
   3. *Expected under H1:* the next line ("CAN. ANYONE. HEAR. ME?") never appears, the player can walk, and the fountain shows no "Press E to deactivate the fountain" prompt or does nothing.
   4. Walk away and back to the door.
   5. Then refresh, and confirm the door conversation replays and the quest proceeds.
2. Repeat step 1 with **Esc**, with alt-tab / clicking outside the browser, and at other lines (`82:3`, `82:8`, `82:9`, which has a reply menu).
3. Repeat with the pause press timed at the very start of a line versus after the line's text has fully appeared, to find the timing window.
4. **Generalisation:** press Tab during a multi-line NPC conversation in Unit 2 (Jasper, Tera) and Unit 3 (Tera). Also choose replies very quickly while holding a movement key (Reed's pattern).
5. **Katelyn's crash:** place cameras in all three garden boxes in Desert Delicacies on a 4 GB Chromebook and watch for a `memory access out of bounds` crash.

## Recommended Developer Investigation

1. **Pause-menu interaction with the Dialogue System:**
   - what opening and closing the pause menu does to an active conversation (time scale, sequencer waits, subtitle continue mode, input-map switching);
   - whether resume unconditionally re-enables the player controller.
2. **Conversation end handling:** make sure stopped or cancelled conversations emit an end event, release the conversation lock, and do not leave quest entries half-applied.
3. **The `82:0` base-door `DialogueSystemTrigger` configuration** (trigger type, "once" flag, condition) and its behaviour while another conversation is active.
4. **The restore point for quest 36:** confirm that a refresh before entering the base restores to the waypoint step (entry 1 active), which would explain the workaround.

## Logging Gaps

- **Pause menu open/close events.** Only the Pause key press is logged; the menu state and the resume are not.
- Conversation cancel/stop/abort events with a reason. Today a hung or cancelled conversation simply goes silent.
- Page unload / refresh / visibility-change events. The 259-minute silence and the unlogged refresh cannot be explained.
- A session identifier and a "first record after reload" marker.
- Quest-entry state changes, so "entry 2 never activated" can be observed rather than inferred.
- **Data pull:** re-export Ella's records after 2026-10-05 18:51 UTC. If the refresh happened later, the post-refresh records should exist on the server now, and would allow the before/after comparison this ticket asks for.

## Confidence and Limitations

- **The logs prove:**
  - the door conversation stopped at `82:5` immediately around a Pause press;
  - the player regained movement without the conversation ending;
  - for about 5 hours nothing she did produced dialogue or an object interaction;
  - every other run of this scene continued automatically.
- **The logs suggest** that pausing during a line caused the hang, and that a refresh cleared it.
- **The logs cannot show** the refresh, the post-refresh state, or what was on screen.
- One case only: confidence in the Pause trigger is **medium**. Confidence that the conversation hang is what blocked progress is **high**.
