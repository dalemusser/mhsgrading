# QA 1697 — Unit 2 Argumentation: Forensic Analysis (first pass)

*Logs: `players-logs-met-bugs/` (build string `20260914-`).*
*Controls: Ella Preble (Meyer1, completed Unit 2 on the same build) and internal playthroughs 09-14-26-3 / 09-23-26.*
*Times: client `timestamp`, UTC, 2026. Meyer1 class ≈ 13:15–14:05 UTC, Meyer2 ≈ 14:10–15:00 UTC; sessions outside those hours were played away from class.*
*Labels: **[O]** observed · **[I]** inferred · **[S]** speculative.*

---

## Executive Finding

**[O] None of the five QA 1697 students ever reached the Unit 2 argumentation activity.** There is no `20:63` "{{PLACEHOLDER – ARGUMENTATION}}", no `argumentationEvent`, no `argumentationAnswerEvent` and no conversation-27 feedback in Unit 2 for any of them. All five stopped earlier, inside "Which Watershed?" (quest 25).

The most useful finding is that this ticket and QA 1693 are largely **the same defect**:

- **[O]** Katelyn and Walton show exactly the QA 1693 freeze. After a reload with the Classifier already completed, DANI's lines `21:46 → 21:51` replay, conversation 21 finishes, the Classifier conversation (8) never starts, and the player produces **zero input events**. This happened 1 time for Katelyn and 3 times for Walton.
- **[I]** The frozen screen is DANI talking about her *argumentation* module, plus `21:46`'s alert "Error: Argumentation Points Cannot Be Classified". That plausibly explains why this classroom called it an "Argumentation" problem.

The other three students did not hit that freeze before the teacher skipped them:

| Student | What the log shows before the skip |
|---|---|
| Mae | The reload restarted **Unit 2 from the very beginning** (quest 21), a different save anomaly |
| Taye | A **13-minute window with no telemetry at all**, right after the drone's ocean scan (possible freeze; single case) |
| Liv | Mid-drone-phase and mostly idle (window unfocused), then skipped; no blocking event visible |

The tracker's "same idea as the Classifier bug" is therefore supported for Katelyn and Walton.

## Reported Symptom

The tracker reports: "Same idea as the Classifier bug" — Unit 2 / Argumentation (Goodhue; Meyer1: Katelyn Ballman, Taye Roschen; Meyer2: Liv Brinkman, Mae Schuller, Walton Gronvall). Status: Tested.

## Students and Log Mapping

| Student (tracker) | Log file | Confidence |
|---|---|---|
| Meyer1 / Katelyn Ballman | `meyer1.katelyn.ballman.stratalog.logdata.json` | High |
| Meyer1 / Taye Roschen | `meyer1.taye.roschen.stratalog.logdata.json` | High |
| Meyer2 / Liv Brinkman | `meyer2.liv.brinkman.stratalog.logdata.json` | High |
| Meyer2 / Mae Schuller | `meyer2.mae.schuller.stratalog.logdata.json` | High |
| Meyer2 / Walton Gronvall | `meyer2.walton.gronrall.stratalog.logdata.json` | Medium-High (`gronrall` ↔ Gronvall) |

## Probable Failure Window

| Student | Last known good | Failure window / first abnormal | Then |
|---|---|---|---|
| Katelyn | 09-30 21:00:13: `18:141` (drone: "begin with the eastern watershed"), session ends 21:00:22 | **10-01 13:24:36–13:25:19**: reload → `21:46…21:51` → Finish 21 → 0 inputs | skipped to Unit 3 at 13:27:35 |
| Walton | 09-30 16:48:13: `20:35` (Toppo: "Deputy, I trust you've made good progress…"); waits at the reply prompt, window unfocused 141 min | **09-30 23:29:09–23:29:56**: reload → frozen; repeated 23:31 and 10-01 13:10 (62.6 min, 0 inputs) | skipped 10-01 14:13:37 |
| Taye | 10-01 13:32:47: `18:141`; Finish 18 at 13:32:55; two inputs at 13:32:56/59 | **10-01 13:32:59–13:45:59**: no records of any kind for 13 minutes | MainMenu → Unit 3 at 13:46:10 |
| Liv | 10-01 12:23:21: `18:141` | none visible; 111 minutes in drone mode, never reaching the eastern-river point `18:142`, with long unfocused gaps | skipped 14:15:11 |
| Mae | 09-30 21:20:24: `18:166` ("Placing the waypoint for the western waterfall"), session ends 21:20:47 | **10-01 14:13:02–14:14:30**: reload restores *no* Unit 2 checkpoint; Unit 2 intro `18:1` replays and `questActiveEvent:21` fires | skipped 14:20:48 |

## Last Known Good State

All five followed the normal quest-25 path up to their last step. The intermediate milestones (`8:12` → `26:136` → `18:121` → `18:130` → `19:32` → `21:76` → `23:38` → `23:42` → ocean scan `18:136` → `18:141`) appear in the same order and at similar intervals as in the internal controls (`scripts/q25steps.py`, `scripts/drone.py`).

**Walton** got furthest. He completed all seven drone scans, `18:169` (data table), `18:176/18:284` (Toppo call, entry 16 active) and Toppo's `20:35`. The next step is the player reply `20:36` and then the argument `20:63`.

## First Abnormal State

**Katelyn (timely records, lag ≈ 0 s)**:

| Time (UTC) | Scene | eventType | Data | Note |
|---|---|---|---|---|
| 10-01 13:24:27.7 | MainMenu | gameStartEvent | — | new session (class) |
| 13:24:35.8 | Unit 2 Prod (Refactor) | PlayerPositionEvent | (1095.8, 153.1, 1366.4) | spawn |
| 13:24:36.494 | ″ | questEvent | `questActiveEvent:25` | restored inside quest 25 |
| 13:24:36.500 | ″ | DialogueEvent | `21:46` + DialogueStart 21 | conversation 21 resumed at node 46 |
| 13:24:46.8 | ″ | PlayerPositionEvent | (1422.7, 101.2, 1133.7) | teleported to the camp |
| 13:24:47 → 13:25:13.1 | ″ | DialogueEvent | `21:47`, `21:48`, `21:50`, `21:51` | |
| 13:25:18.876 | ″ | DialogueEvent | **DialogueFinish 21** | normal flow: `21:51 → 8:2` |
| 13:25:26 → 13:26:36 | ″ | PlayerPositionEvent ×8 | fixed (1422.7, 101.2, 1133.7); **0 InputEvents** | frozen |
| 13:27:27.9 → 13:27:35 | MainMenu → Unit 3 Dev | — | no `EndOfUnit 2` | teacher/student skip |

**Walton:** the same sequence on all three reloads (Finish 21 at +6.5 s, +5.9 s, +6.6 s after `21:51`; 0 inputs; position fixed at (1421, 102, 1135)).

**Mae:** her 10-01 load emitted two `DEBUGMenu` scene-load records 8 s apart (14:13:02, 14:13:10) and **no** quest restore. Then `18:1` "C-c-c-communication systems are re-restoring" (the Unit 2 intro, 14:13:30), `18:3…18:10`, `questActiveEvent:21` "Escape the Ruin" (14:14:30) and topography-glyph pickups followed. This is a fresh Unit 2.

**Taye:** his last records before the hole were uploaded **after** his next game start (server 13:51:52–55). So the offline queue survived the page reload, and **[I]** the hole is not lost data; the game generated nothing for 13 minutes.

## Event Reconstruction

**Walton** (furthest progress; best illustration of the freeze):

| Time (UTC) | eventType | Data / node | Meaning |
|---|---|---|---|
| 09-30 16:33:36 | questEvent | `questActiveEvent:25` | "Which Watershed?" |
| 16:37:16 | DialogueEvent | `26:136` | Classifier complete |
| 16:38:00 | DialogueEvent | `18:130` | entry 2 active |
| 16:39:54 / 16:41:33 / 16:42:36 | DialogueEvent | `19:32` / `21:76` / `23:38` | Anderson, Tera, Jasper |
| 16:42:53 | DialogueEvent | `23:42` LAUNCH DRONE | |
| 16:43:24 → 16:47:15 | ObjectInterEvent + DialogueEvent | 7 scans; `18:136…18:167` | object names in this batch are stale (buffered) and unusable; `eventKey` node order matches the control |
| 16:47:32 / 16:47:54 | DialogueEvent | `18:169` / `18:284` | data table; Toppo call ends (entry 16 active) |
| 16:48:13 | DialogueEvent | `20:0`, `20:35` | Toppo opens the pre-argument conversation |
| 16:48:23 → 19:10:33 | (2 records, 141-min gap, window un/focus) | — | idle at the reply prompt |
| 23:29:09 | questEvent | `questActiveEvent:25` (after gameStart) | restore inside quest 25 |
| 23:29:1x–23:29:51 | DialogueEvent | `21:46…21:51` → Finish 21 (+6.5 s) | **first abnormal** |
| 23:30:55 | (MainMenu → Transition → Unit 2) | same replay | frozen; 819.8 min until the next start |
| 10-01 13:10:52 | ″ | same replay | frozen 62.6 min, 0 inputs |
| 14:13:37 | Unit 3 Dev | (from MainMenu) | skipped; no `EndOfUnit 2` |

**Control (Ella Preble, same class and build):** quest 25 from 09-30 14:22 to 16:23. She reached Toppo `20:35` at 15:30:01, replied (`20:36`, `20:37`, `20:41`, `20:42`, `20:45`, `20:46`), opened the argument (`20:63`) at 15:32:22, and submitted **33 times** over 51 minutes (feedback `27:11/13/20/12/18/28/26/30`) before `27:7` success (16:23:04) and `questFinishEvent:25`. She had **no reload inside quest 25**. Ella is the only classroom student whose log contains Unit 2 argumentation, and she shows that the activity works but can take a long time.

## Shared Patterns Across Affected Students

| Pattern | Katelyn | Walton | Taye | Liv | Mae |
|---|---|---|---|---|---|
| Reached `questActiveEvent:25` | ✓ | ✓ | ✓ | ✓ | ✓ |
| Completed Classifier (`26:136`) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Furthest step | `18:141` | `20:35` | `18:141` | `18:141` | `18:166` |
| Reached the argument (`20:63`) | ✗ | ✗ | ✗ | ✗ | ✗ |
| Reload after the Classifier | 1 | 3 | 0 | 0 | 1 |
| Outcome of that reload | **frozen** | **frozen ×3** | — | — | Unit 2 reset |
| Skipped to Unit 3 without `EndOfUnit 2` | 10-01 13:27 | 10-01 14:13 | 10-01 13:46 | 10-01 14:15 | 10-01 14:20 |

- **[O]** Skip timing: all five moved to Unit 3 from the main menu on **10-01 within the first minutes of class**. Meyer1 went at 13:27 and 13:46, Meyer2 at 14:13, 14:15 and 14:20. **[I]** This is consistent with a teacher-led decision to advance the class rather than five independent stalls. Taye and Liv may have been advanced while still able to play.
- **[O]** Katelyn's, Mae's and Walton's last quest-25 progress happened in sessions **outside their class period**: Katelyn 09-30 20:49–21:00 UTC; Mae 16:41–21:20 UTC; Walton 16:33–16:48 UTC. Those sessions ended mid-quest, so their next attempt began with a reload, which is exactly the condition that triggers the freeze.
- **[O]** Comparison with QA 1693: the frozen signature is identical in both tickets: the same nodes, finish of conversation 21 5–10 s after `21:51`, no conversation 8, 0 inputs, the same camp position. It covers 13/13 post-Classifier reloads across Isabella (1693), Corah and Molli (1694), and Katelyn and Walton (1697).

## Key Anomalies

1. **[O]** The frozen reload state (see QA 1693 for the full mechanism and export evidence).
2. **[O]** **Mae: Unit 2 save not restored at all.** She completed the Classifier and was at entry 12 when she stopped. Her next load had **no** restore and replayed Unit 2 from `18:1`. *Context:* every one of her records from 09-30 14:30 onward was uploaded only on 10-01 14:13–14:18, i.e. she was offline for the rest of Unit 2. Liv's offline-written checkpoint *was* restored, though, so offline status alone does not explain this. **[S]** Possible causes: a lost or overwritten local save, a deliberate "restart" choice in the menu (the two scene loads 8 s apart fit this), or a server/local save race.
3. **[O]** **Taye: 13-minute telemetry hole** right after the drone's ocean scan, with no position heartbeat (normally every ~10 s, even when idle), followed by a main-menu return. **[S]** A WebGL hang or a hidden tab; there is no unfocus event and no crash record at that time (his only crash record, a Pointer Lock rejection, is in Unit 3 at 13:53).
4. **[O]** Liv was offline for long stretches. Most of her drone-phase records are buffered, so their `actionType` / `playerOrDrone` payloads cannot be trusted (see telemetry caveats). The large "Descend" count in that window is not reliable evidence.
5. **[O, telemetry]** Stale payloads in delayed uploads are very common in this class. They are why a naïve read of `data.conversationId` shows Walton at `20:35` ×154 and Katelyn at `18:284` ×139: those are the last node before each upload batch, not repeated dialogue.

## Ranked Hypotheses

### H1 — Same defect as QA 1693: a post-Classifier reload restores quest 25 into a dead-end replay and input lock (**High** for Katelyn and Walton)

- **Evidence for [O]:**
  - 4/4 of their quest-25 reloads froze identically.
  - Both had completed the Classifier.
  - The signature matches QA 1693 exactly.
  - The `21:51 → 8:0` link is gated on `classifierDone == false` in the export.
- **Evidence against:** the save contents are not visible. The mechanism detail is **[I]**, as in QA 1693.
- **Reproduction and verification:** see QA 1693 (H1). Additionally reload **at Toppo's `20:35` reply prompt**, which was Walton's exact state.

### H2 — The "Argumentation" label describes the frozen screen, not the argumentation activity (**Medium**)

- **Evidence for:**
  - **[O]** No QA 1697 student reached `20:63` or any argumentation event.
  - **[O]** The frozen state displays DANI's "argumentation module… retrain my argumentation algorithm…" lines.
  - **[O]** `21:46` runs `ShowAlert("Error: Argumentation Points Cannot Be Classified")`.
- **Evidence against:**
  - The teachers' notes are unavailable (the `Notes` cell is `#VALUE!`).
  - Another possibility is that the label reflects where students *expected* to go next (Walton was one reply away from the argument).
- **Verification:** ask the Goodhue teacher what was on screen, or show them a screenshot of the frozen state.

### H3 — Mae: Unit 2 checkpoint lost or reset on reload (**Low–Medium**, single case)

- **Evidence for [O]:** no restore was emitted and the Unit 2 intro replayed. The whole post-14:30 progress was offline.
- **Evidence against [O]:** another offline student's checkpoint restored fine. A user-initiated restart cannot be excluded.
- **Reproduction:** play Unit 2 to quest 25 with the network disabled from quest 23 onwards, close the tab, reconnect and reload. Separately, test any "restart unit" path in the menu.
- **Verification:** inspect where the save lives (server vs. browser storage) and whether a save written offline is synced, queued or dropped.

### H4 — Taye: a client hang during the drone phase (**Low**, single case)

- **Evidence for [O]:** a 13-minute absence of all events, including the position heartbeat, right after `18:141` / Finish 18 in drone mode.
- **Evidence against:** no crash record and no unfocus event. A closed lid or a suspended tab would look the same.
- **Reproduction:** on a Chromebook, run the drone segment after the ocean scan, alternating focus, and watch for hangs. Add a heartbeat with a frame counter.

### H5 — Liv: no defect; advanced while idle (**Medium** as an explanation of *her* entry)

- **[O]** There is no anomaly in her timely records. She spent long unfocused periods in drone mode and was skipped together with her classmates.

## Suggested QA Reproduction Steps

1. Run **QA 1693 step 1** (complete the Classifier → refresh → expect the freeze) and verify that the frozen screen shows the "Argumentation Points Cannot Be Classified" alert. If it does, QA 1693 and QA 1697 can be tracked as one defect.
2. **Walton's state:** play to Toppo's "Deputy, I trust you've made good progress…" (`20:35`), leave the reply prompt open, switch tabs for several minutes, then refresh. *Expected under H1:* freeze.
3. **Out-of-class session pattern:** stop mid-drone-phase (after "I recommend beginning with the eastern watershed"), close the browser, reopen the next day. *Expected:* freeze.
4. **Mae's pattern:** see H3.
5. **Taye's pattern:** see H4.

## Recommended Developer Investigation

- The same as QA 1693: quest-25 restore path, `21:51 → 8:0` gating, input/controller restoration on conversation end, and checkpoint write timing.
- Save persistence under offline conditions (Mae) and whether two scene loads 8 s apart indicate a "new game" path being taken.
- WebGL main-loop stalls on Chromebook hardware during the drone camera (Taye). Unity WebGL stops emitting when the tab is hidden; verify whether `gameWindowUnfocusEvent` is reliable on ChromeOS.

## Logging Gaps

- **Most important:** checkpoint save/load events with quest-entry states and key Lua variables.
- A "restart unit" vs. "continue" choice in the main menu, and the selected unit when skipping ahead.
- Player input enabled/disabled state, and a frame-counter heartbeat to separate a hang from an idle player.
- Teachers' notes for the ticket. Telemetry cannot tell whether a student was blocked or advanced pre-emptively.
- Payload freshness in offline batches (see the cross-issue summary).

## Confidence and Limitations

- **The logs prove:**
  - none of the five reached the argumentation activity;
  - Katelyn and Walton entered the same non-recoverable post-reload state as the QA 1693 students;
  - Mae's reload restarted Unit 2;
  - Taye's client produced no events for 13 minutes before he left Unit 2;
  - all five were moved to Unit 3 at the start of class on 10-01.
- **The logs cannot show** what was on screen, whether the teacher skipped students who were still able to play (Liv, possibly Taye), or the contents of the save files.
- The QA 1697 / QA 1693 equivalence is strong for two of five students and plausible for the classroom-level report.
