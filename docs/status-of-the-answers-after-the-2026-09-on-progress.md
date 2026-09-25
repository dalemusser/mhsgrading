## Status of the answers after the 2026-09-24 refinement round

Legend: DONE = implemented in the grading scripts, their Python transcriptions and the rubric files, both validation suites 26/26 on all five fixtures. NEEDS DATA = waits for the imperfect playthrough of the release build. FUTURE = a decision or adjustment for a later round. Nothing below is committed yet; the Go rules must follow (list in section F).

### A. Decisions
1. **Grading window — DONE.** All 26 points now use the start-and-end window: latest end trigger, latest start trigger before it, grade from the start of the log when no start exists (A10). Windows changed on 19 points: U1P3, U2P1, U2P4, U2P5, U2P6, U2P7, U3P1, U3P2, U3P3, U3P4, U3P5, U4P1, U4P3, U4P4, U4P5, U4P6, U5P1, U5P2, U5P3. Unchanged: U1P1/U1P2/U1P4 (completion-only), U2P2/U2P3 (already start-and-end, with the timestamp fence), U4P2 and U5P4 (already start-and-end). On every log the new windows contain exactly the same events as the old ones; no fixture colour moved.
2. **U3P2 start — DONE.** questActiveEvent:17 confirmed and re-verified on all logs.
3. **U3P4 start — DONE.** questActiveEvent:18 confirmed. It fires two or three times per playthrough (quest stages); the latest one before the end is the glyph-room entry and every graded node follows it.
4. **U4P1 end / U4P2 start — DONE (kept).** Re-verified; the scene value is still "Unit 4 Dev" on build 20260914-, so the prefix match stays. FUTURE: switch to an eventKey if the game team adds one for the puzzle close.
5. **U3P5 threshold — DONE.** 2.5 in the rule table, the Analytics script, the reason code and the rubric file's Implementation Note.
6. **U4P4 machine-1 condition — DONE.** Grading Rule prose corrected to "top once AND bottom once"; clause added to the rubric file.
7. **U2P2/U2P3 fence — DONE.** The U2P3 reason script now carries the client-timestamp fence. Fenced and unfenced counts agree on every log, and no dialogue or quest record lacks a timestamp.
8. **Re-fired triggers — DONE through A1.** The end-anchored windows absorb the double firings (questActiveEvent:36 and questFinishEvent:45 twice per playthrough). Still noted for the game team.
9. **Yellow with no reason code — no change, confirmed.** The accepted-assist paths of U4P2 and U5P1 are covered by observed logs; U3P4's accepted nodes 78:20/78:21 were added from the export gates ahead of observation (see D3).
10. **No start event — DONE on our side.** Every window falls back to the zero ObjectId. FUTURE (Go side): keep the "window: no start event found" note visible on the grade record. Anchor check for build 20260914- done: every start and end fires (36 and 45 twice, 18 two to three times, all others once).

### B. Items marked "for review"
1. **U3P3 — DONE.** Key list re-checked against the 2026-09-21 dialogue export (conversation 84 unchanged); 84:36 stays; "for review" wording dropped.
2. **U3P5 — DONE** (A5).
3. **U4P4 — DONE.** 107:4 moved to the negative set in both colour scripts and the reason script; rubric file note added. No fixture colour moved.
4. **U5P2 — DONE.** DualChamber_Condenser / DualChamber_Evaporator counted in all three scripts. Third-floor counts on the yellow fixtures rise from 8 to 24 and 8 to 21 (colours unchanged); the older log 05-01-26 would move from green to yellow, which the rubric intends. See E2 for a weakness this exposed.
5. **U4P6 — NEEDS DATA.** The second-round route (92:34 → 92:35 → 92:36) was observed once on build 20260902 and the existing whole-window fallback counted it correctly, so the scripts are unchanged. Checklist item 11 covers it on the release build; then 92:36 becomes a second review anchor.

### D. Data questions
1. **96:1 once — confirmed again** on all seven complete logs (twice, 13 s apart, on the August build 20260812; harmless under the end-anchored window). Keep checking.
2. **10:30 after 11:22 — confirmed again:** never, on eight logs. Keep checking.
3. **U3P4 accepted assist — NEEDS DATA.** Still unobserved; checklist item 10. Related finding: on build 20260914- DANI's assist does not place the pieces at U3P4 (forced path) or at U5P1 (accepted path); the student still solves the puzzle, so the game's "solved by player" node fires after the "auto-solve" node. Grading holds because assistance is detected from the assist nodes, never from the success node; the message wording "DANI ordered the pieces/tablets" should become "showed the correct order" if the bug ships.
4. **Imperfect playthrough — NEEDS DATA.** docs/imperfect-playthrough-checklist.md now lists 11 paths: the original eight, the ocean-sensor throw at U3P2 (item 9), the accepted assist at U3P4 (item 10) and the second-round review at U4P6 (item 11).

### E. New items from this round (FUTURE unless marked)
1. **U4P5 colour band.** The dashboard is green only with at most 2 wrong submissions, while the rubric's "Green: 2–4 points" includes a 4th-attempt success (2 points). One-attempt difference; documented in the rubric file; decide which band the rubric intends.
2. **U5P2 zero-interaction floor.** A floor with no logged interactions scores 2 points, while the rubric gives 0 for a floor not completed. Seen only in fixture 09-03-26-2, where floor 3 was skipped with the debug menu, so that fixture's green rests on the skip. If we want it closed: require the rubric minimum (5 on floor 3, 4 on floor 4) before a floor earns points; that changes the Go rule and that fixture's expected colour.
3. **U3P2 ocean-sensor node 11:30.** Kept out of all scripts; decide after checklist item 9 (NEEDS DATA).
4. **Forced-node counting aligned — DONE.** U3P4, U4P2 and U5P1 now count the fifth wrong order that forces DANI's assist, as U2P1 and U2P4 always did. Expected attempt numbers moved from 4 to 5 on U3P4 (09-14-26-3), U4P2 (09-03-26-3) and U5P1 (09-03-26-3).
5. **Dialogue database changes absorbed (2026-09-21 export) — DONE.** U2P1: assist outcome node 68:30 added. U2P3: reminder nodes 28:195 and 59:195 added. U2P4: retired node 74:25 removed, forced node 74:20 counted. U3P4: accepted-assist nodes 78:20/78:21 added. Conversations 11, 68, 74, 92, 100 and 106 changed without affecting any graded key.
6. **Logging notes for the game team.** TerasGardenBox records other than cameraPlaced log an empty actionType since build 20260902 (was soilSelected). Sensor drops at U3P2 cannot be located (no drop event; PlayerPositionEvent follows the player, not the drone). Auto-solve does not move puzzle pieces (D3).
7. **Optional hardening, not applied.** Filter the U4P3/U4P4 soilMachine counts on actionType "ChangeCanister" (the only action type seen today).

### F. Go rules to update in step
- Window moved to start-and-end: u1p3, u2p1, u2p4, u2p5, u2p6, u2p7, u3p1, u3p2, u3p3, u3p4, u3p5, u4p1, u4p3, u4p4, u4p5, u4p6, u5p1, u5p2, u5p3.
- Key or logic changes: u2p1 ASSIST_KEYS += 68:30; u2p3 targets += 28:195, 59:195 in colour rule and reason code, reason code gains the timestamp fence; u2p4 ASSIST_KEYS = 74:18/20/22, NEGATIVE_KEYS += 74:20; u3p4 ASSIST_KEYS = 78:20/21/23, NEGATIVE_KEYS += 78:23; u4p2 NEGATIVE_KEYS += 102:23; u4p4 SUCCESS_KEYS = 107:5 only, NEG_KEYS += 107:4; u5p1 NEGATIVE_KEYS += 100:43; u5p2 VALID_TYPES += DualChamber_Condenser, DualChamber_Evaporator.
- Documentation only, no Go change: u4p2 window, u5p4, u3p5 threshold (already 2.5 in production).
