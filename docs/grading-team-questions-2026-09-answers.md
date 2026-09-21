# Answers to the Questions
## A. Decisions we made — please confirm or correct
---
1. **Grading window:** Confirmed for now: implement the Production Scripts as written. The header Trigger(Start) keys are the intended window anchors. I added them to every point, but only switched the production window to start-anchored for the points that had misgraded under the previous-END logic, and left the others alone because they had never produced a wrong colour. In the next release I will move all points to a start-and-end window (latest start to the end trigger), which is more consistent and safer on replays. When a student re-enters an activity after finishing it, the grade of the completed attempt should stand; I will write the new windows that way. I will list the affected points when the change lands so the Go rules can be updated in step.
---
2. **U3P2 start event:** Confirmed: questActiveEvent:17 is the correct start for U3P2.
---
3. **U3P4 start event:** Confirmed: questActiveEvent:18 is the intended start for U3P4.
---
4. **U4P1 end/U4P2 start:** Confirmed: keep the Soil Key Puzzle event with Soil Key Puzzle Status = Finished and Unit starting with "Unit 4" as the U4P1 end and U4P2 start. It was chosen because the earlier questActiveEvent:39 anchor fires before the answer and the puzzle, so it could never award the duration points. The puzzle's Started/Finished records carry no eventKey, so an eventType + data match is the only usable anchor. If the game team later adds an eventKey for the puzzle close, we will switch to it; until then this stays. 
---
5. **U3P5 threshold:** Green at sum_score >= 2.5 is intended. With four seeds, 2.5 means at most one wrong planting, which matches the rubric's on-track band (3 to 4 points, one wrong planting allowed) and the instructor message. A threshold of 3 would require zero wrong plantings and is stricter than the rubric. I will correct the Grading Rule table and the Analytics Script in mhs-unit3-point5-grading.md to 2.5 so all copies agree.
---
6. **U4P4 machine-1 condition:** Confirmed: top = 1 AND bottom = 1. The rubric says the bottom canister is left untouched, but in the game as built the player has to set both the top and bottom canisters to solve the fifth-floor puzzle, so a first-attempt solution is exactly one change on each. The scripts follow the game, not the rubric. I will correct the Grading Rule prose in mhs-unit4-point4-grading.md ("bottom machine with zero time" becomes "bottom machine one time"); March item 4 in issues_and_updates.md is superseded, as your addendum already notes.
---
7. **U2P2/U2P3:** The fence is intended and should stay. The rule is defined on client time, and _id is server arrival order, which can disagree with client order after batched uploads (in our dumps about 2.6% of adjacent records, by up to about 76 seconds). Requiring the counted events to lie between the anchors' client timestamps as well as their _ids keeps the count on the play order. It began as a carry-over from the timestamp-based analytics scripts, but we keep it on purpose. The U2P3 reason script lacking it is an omission: I will add the same timestamp fence there so the pop-up count can never differ from the colour. Anchors with no client timestamp: every DialogueEvent and questEvent record carries one, so that branch should not occur in practice; keep the literal behaviour (yellow, no code).
---
8. **Re-fired and triggers:** Agreed: ignoring an END that re-fires with no new start event in between is the right guard. Once the windows move to start-and-end anchoring (A1), that case disappears on our side too. The double firing of questActiveEvent:36 and questFinishEvent:45 is noted for the game team.
---
9. **Yellow with no reason code:** No new codes are needed; the generic text is the right fallback for all of these.
- U2P1, U2P4, U4P2 and U5P1 are the glyph and ordering puzzles. In the current build a player leaves the puzzle only by solving it (the success node fires) or by DANI solving it (an assist node fires), so a closed window with neither should not occur. If it does, it means a dialogue event was dropped by the logger or an assist node we have not listed yet. The 09-14 run exposed exactly that for U2P1 and U4P2, and the key lists were extended on 2026-09-16. I will keep checking new playthroughs for unlisted nodes.
- U2P6 is a dialogue choice the player must make to progress. If neither wrong node (20:44, 20:45) fired, the correct choice was made and the point is green, so a yellow without either node cannot happen unless the game content changes.
- A missing window gets no code on purpose. We removed the old NO_TRIGGER codes because a point with no window is not started or still in progress, and the dashboard's white and pencil states already say that (see A10 and your not-reached finding). A yellow with a reason would mislead teachers there.
---
10. **When not start exists:** Agreed: a graded estimate is better than an automatic yellow. Please keep the "window: no start event found" note on the grade and make it visible on the dashboard or in the grade record, so we can tell a logging gap from a real result. Separately, I will check each release build's logs to confirm every start and end anchor still fires.
---
## B. Items the documents themselves mark "for review" — implemented as scripted
1. **U3P3:** Reviewed on 2026-09-17 against the Unity dialogue export: keep as scripted. 84:36 is counted on purpose so that the count equals the number of attempts, which makes the base-score bands (3 or fewer / 4 / 5 / 6 or more) equal the rubric's attempt bands. 84:38 is a branch gate that never logs, so it is inert. The "for review" wording in the document can be dropped. I will re-check the full key list once the dev team shares the updated dialogue-system export for the release build, which Neil has requested.
---
2. **U3P5:** I'll update this as answered in A5.
---
3. **U4P4:** Please move 107:4 from SUCCESS_KEYS to the negative set. The rubric says layer 3 or layer 4 earns credit, but in the game as built only the fourth floor (107:5) yields clean water; the middle choice (107:4) yields contaminated water and the task continues until 107:5 is chosen, so a middle-then-fourth player has in fact used two attempts. We follow the game here. I will change both colour scripts and the SCORE_BELOW_THRESHOLD script in mhs-unit4-point4-grading.md, and note it in the unit4-pp-4 rubric file.
---
4. **U5P2:** Approved: add DualChamber_Condenser and DualChamber_Evaporator to VALID_TYPES in both colour scripts and the reason script (floor 3 logs them alongside Condenser and Evaporator). I will make the change here.
---
5. **U4P6:** Agreed in principle: the review can start at 92:36 as well as 92:33, so the 92:61 count should anchor on the latest of the two. I will confirm the second-round flow in the next playthrough of the release build before changing the scripts.
---
## D. Data questions we could not answer from the repositories
1. In all four complete fixture playthroughs, DialogueNodeEvent:96:1 fired exactly once. I have not seen it repeat; I will keep checking in future playthroughs.
---
2. No. By design the correct-river dialogue is not used in the bonus-crate segment, and in the five fixture logs 10:30 never fires after U3P1's end (11:22): it fires up to three times before the end and zero times after. I will keep checking in future playthroughs.
---
3. Not yet confirmed: the accepted-assist path at U3P4 has not been reached in any log so far. I will try to trigger it in the next playthrough test and confirm the execution node.
---
4. Agreed. I will run a deliberately imperfect playthrough of the release build aimed at those eight paths (EXCESS_ATTEMPTS at U2P1, U2P4, U3P4, U4P2 and U5P1, the uncovered U2P3 branch, and the U2P6 salinity and both-options branches) and share the log so the grader can be verified end to end.
---
## When to conduct the next step
Within this week.