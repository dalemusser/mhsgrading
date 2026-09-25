# EA Scores for the End-of-Game Ceremony — Questions and Answers
1. U2.C3 (D1). Does U2.C3 include the Aryn search, so that Jasper's warmer line needs 2 of 4? If it should be Tera only (2 of 2½), say so. If you would rather raise the bar to 3 when Aryn is included, say that instead. 
**Yes, this checkpoint includes both Tera and Aryn. Leave as is.**

---
2. U2.C5 (D2). Is a maximum of 6 right, and is the raw form (not the proportional formula) what you intend? 
**Yes, max score is 6 (1 pt. for each correct classification, 6 needed to progress). Using raw form: +1 for each correct –(1/3) for each incorrect.**

---
3. Critique (D3). Which conversation is the "Critique Jasper's argument" checkpoint: 23 (Jasper asks; correct answer "No. Jasper, you forgot evidence"), 20 (Toppo asks), or both? Do repeated attempts all count in the denominator? 
**This should not be included in Embedded Assessment**

---
4. U3.C2 (D4). Which dialogue node is the "We are at the ocean downstream of Tera's base" line? Is it acceptable to keep the production script's grouping until then? 
**The line is `DialogueNodeEvent:11:30` (conversation 11, U3/DANI): "We are at the ocean downstream of Tera's base, logically, there will be pollution here. I recommend proceeding upstream." Yes, keep the production script's grouping for now. Because, based on my playthrough experience, the game didn't implement this reminder dialogue as designed (when throwing sensors to the downstream of the river (ocean), no reminder dialogue triggered)**

---
5. U3.C5 (D5). Is 2.5 (three correct plots, one wrong) the right bar for Tera's warmer line, or must all four plots be correct? 
**Yes, let’s use 2.5 as the bar for Tera’s warmer line.**

---
6. U5.C4 (D6). First submission only, or the best submission? 
**First submission as the player only submits once for this task.**

---
7. Star totals (D7). What per-unit totals are the bands based on? If the bands were written for an earlier list of checkpoints, please restate them for the current list, or confirm the percentage reading.
**Please see the updated star charts for U2, U3 and U4.**

| Unit | 1 star | 2 stars | 3 stars |
|------|--------|---------|---------|
| U2 | 0 – 10.49 | 10.5 – 14.49 | 14.5 – 17.5 |
| U3 | 0 – 10.99 | 11 – 14.99 | 15 – 18 |
| U4 | 0 – 10.49 | 10.5 – 14.49 | 14.5 – 17.5 |

Bands are inclusive at both ends; each unit's 3-star ceiling is its maximum EA score (17.5 for U2 and U4, 18 for U3).

---
8. Attempt counting for glyph tasks (U2.C1, U2.C4, U3.C4, U4.C2, U5.C1). We count attempts from the attempt-numbered feedback nodes listed in §2. Is a DANI-assisted solve (the assist and auto-solve nodes) a 0, as we assume? 
**We would prefer to assume auto solve is 0, but for assist refer to number of attempts to determine score.**
---
9. Backing info (U3.C3, U4.C5). For U4.C5 we will detect the warehouse layout panel the same way U3.C3 detects the pollution site data panel. What is that panel's tool name in the logs? 
**The panel logs as an `argumentationToolEvent` with `argumentationTitle` "Unit 4 - Flooding" and `toolName` "BackingInfoPanel - Soil Layers and Fountain Data". But be aware that no build since August has logged any Unit 4 panel event, so the U4.C5 bonus cannot be detected on the current build until the game team restores that logging. I will check this further with new game playthrough, and if this is not logged, I'll let Neil know and fix it.**
---
10. Anything the ceremony should not say. The dialogue lines were approved in script v4. If any line should be held back for a student with no score at all (never reached the task), tell us which.
**For the partial units, lets use the threshold below to trigger the scripted NPC responses instead of a the  "I don’t have a record for your work" dialog**
- U1: complete at least 2 of the 4 progress points

- U2: complete at least 3 of the 7 progress points

- U3: complete at least 2 of the 5 progress points

- U4: complete at least 2 of the 6 progress points

- U5: complete at least 2 of the 4 progress points

