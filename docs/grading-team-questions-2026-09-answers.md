# Answers to the Questions
## A. Decisions we made — please confirm or correct
---
1. **Grading window:** Thanks for pointing this out, I marked all start event keys for all the progress points. However, I just applied those keys for progress points that had wrong grading results with "only-end-event-key" logic previously. I didn't touch the progress points that never produced wrong results before. I think applying the "start-and-end-event-key" logic for all progress points is safer and more consistent plan for the future. So, I'll do it in the next release.
---
2. **U3P2 start event:** You are right, I'll correct it immediately and the next release will apply this update.
---
3. **U3P4 start event:** You are right, I'll correct it immediately and the next release will apply this update.
---
4. **U4P1 end/U4P2 start:** Yeah, I used this plan because in a certain game version before, the previous eventkeys we used for the U4P1 always produced unexpected results, so I changed the start and end points of the window into the current version. I'll update this in the next release since it seems if we could hook the start and end points to log events with eventkeys, that would be better. 
---
5. **U3P5 threshold:** Thanks for pointing this out, I'll correct this in the next release.
---
6. **U4P4 machine-1 condition:** For this one, the misalignment is because the game content is different from what was designed in the combo doc. Within the game, the player needs to adjust both top and bottom machines to solve the puzzle. So, the current logic is aligned with what the game realizes instead of the combo doc designed. So I suggest using the current logic.
---
7. **U2P2/U2P3:** For this one, If I understand it correctly, it should be a fence particularly for the reason codes. Since the progress point combines two quests and the reason codes calculate reminder dialogues triggering seperately for each quest; Since the same reminder dialouges may be happened in those two quests, so a time fence for it creates a safe buffer to ensure the summation calculation happened seperately in those two quests.
---
8. **Re-fired and triggers:** Thanks for identifying this, like I said in previous answers, I'll update all listed progress points that still using previous-end and end logic to latest-start and latest-end logic, and also ensure the hook log envent has eventkeys.
---
9. **Yellow with no reason code:** Thanks for pointing this out! To my knowledge, progress points U2P1, U2P4, U4P2 and U5P1 are all glyphs-puzzle-solving quests (with different curriculum topics). In current game version, there are only two ways passing this kind of quests, either the player solving themselves, which will trigger the dialogue "success" eventkey, or solved by DANI, which will trigger DANI helped dialouge eventkeys. There is no possibility that the success node is absent and no DANI assist fired. But I'll keep an eye regarding those quests to ensure there is no such a possibility. For U2P6, this is a dialogue-choice-based progress point, the player has to choose one to make game progress, so the only situation where neither the two wrong choices are choiced is that the correct one was choosed, which will turn the progress point to green. So, unless the game content changed, the current logic for U2P6 will work fine.
---
10. **When not start exists:** I'll check event logs to ensure each start- and end-anchored point exists within the game logs for the game release version.

---
## B. Items the documents themselves mark "for review" — implemented as scripted
1. **U3P3:** I'll review this and correct the logic to ensure it aligns with the assessment rubric and current game version. According to Neil, Dev team needs to update the dialogue system export form and share to the Drive to ensure our logic in this repository can be fully aligned with the current game version.
---
2. **U3P5:** I'll update this as answered in A5.
---
3. **U4P4:** This one is because of a misalignment between the assessment rubric and the current game design, in the rubric choosing both dialogue nodes can gain an credit, while in the game, only one dialogue node can pass the quest. I suggest to follow the game logic since anyway the student will never know choosing "middle layer" will offer them some credits.
---
4. **U5P2:** Thanks for reminding me of this, I'll update the grading logic accordingly.
---
5. **U4P6:** Thanks for pointing this out, I'll check it further with additional test running of the game release version.
---
## D. Data questions we could not answer from the repositories
1. I'll test run the game again to confirm it.
---
2. If I understand the question correctly, based on current game design, no, after the end of U3P1, there is no chance to fire the correct river feedback dialogue. But, I can ensure it in a future game playthrough test.
---
3. I'll confirm this is confirmed in another game playthrough test.
---
4. I'll conduct another round of game playthrough to test whether the reason codes (EXCESS-ATTEMPTS) can be triggered.
---
## When to conduct the next step
After getting the most updated dialogue system export form, aligning with game release version.