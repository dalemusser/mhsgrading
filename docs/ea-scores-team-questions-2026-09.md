# EA Scores for the End-of-Game Ceremony — Decisions and Questions

*2026-09-21. For the grading team and the designers. Please answer the
numbered questions in §4 the way you answered `grading-team-questions-2026-09.md`;
a new file `ea-scores-team-questions-2026-09-answers.md` next to this one is
ideal.*

## Why you are reading this

Mission HydroSci gets an **end-of-game ceremony**: after Unit 5 the five
characters (Toppo, Jasper, Tera, Anderson, Aryn) take the stage in a short 3D
award show, recap the student's journey unit by unit, and finish with a star
board (one to three stars per unit) and the Planetary Water Steward award.
Eight of the characters' lines exist in two versions, a warmer one (A) and a
gentler one (B), and the version that plays depends on the student's
**Embedded Assessment (EA) checkpoint scores** from the EA working document.

Today the grader computes the dashboard colours (green, yellow) but not EA
scores. We are adding EA scores to the grader now, for **every** checkpoint in
the working document, because the star board needs each unit's total. We want a
playable ceremony as soon as possible, so wherever information was missing we
made a **provisional decision** (marked *Decision* below). Everything here can
be corrected later without holding the build: tell us what to change and we
will regrade.

## 1. What the ceremony needs

### 1.1 Nine checkpoint scores choose the dialogue

| Character | Line topic | Warmer line plays when | EA checkpoint(s) |
|---|---|---|---|
| Jasper | Finding the missing team | U2.C2 + U2.C3 ≥ 2 | Find Toppo, Find Tera (+ Aryn, see D1) |
| Jasper | Fixing DANI | U2.C5 ≥ 4 | Classify argument components |
| Jasper | Which watershed is bigger | U2.C7 ≥ 2 | Argue which watershed is bigger |
| Tera | Crates | U3.C1 ≥ 2 | Placement of crates |
| Tera | Superfruit garden | U3.C5 ≥ 2.5 (was 3, see D5) | Plant superfruit seeds |
| Anderson | Soil for the seedlings | U4.C6 ≥ 2 | Tera's garden boxes |
| Aryn | The plant | U5.C3 > 0 | What happened to the water? |
| Aryn | The solar still | U5.C4 > 0 | Solar still activity |

A checkpoint the student never reached, or that has not been graded yet,
plays the gentler line. We never invent a 0 for a missing score, because a 0
would assert poor performance where we simply do not know.

### 1.2 Stars per unit

The star board uses the working document's "Unit Summary Scores for
Dashboard" bands, applied to the **total of all of that unit's checkpoints**:

| Unit | One star | Two stars | Three stars |
|---|---|---|---|
| 2 Topography | 0–8.9 | 9–12.49 | 12.5–15 |
| 3 Surface Water | 0–6.9 | 7–9.9 | 10–12 |
| 4 Groundwater | 0–8.4 | 8.5–12.4 | 12.5–16 |
| 5 Atmospheric Water | 0–5.99 | 6–8.99 | 9–10.5 |

See D7: the checkpoint maxima in the document add up to more than the top of
the three-star band for Units 2, 3 and 4.

### 1.3 Which attempt counts

A student can replay a task. For each checkpoint we use the **latest finished
attempt**, the same rule the dashboard uses for colours. EA scores are computed
in the same event windows as the colours, so when the windows move to
start-and-end anchoring (your answer A1) both move together.

## 2. Checkpoint by checkpoint

"Rule" is the grader's progress-point rule whose window and events the EA
score is computed from. "Status": **Ready** = the rule already records what
the EA score needs; **Nodes** = needs counting of dialogue nodes we located in
the 2026-09-21 dialogue export; **Input** = needs your answer.

| EA | Task | Max | Rule | EA score derivation | Status |
|---|---|---|---|---|---|
| U1.C3 | Build first argument | 1 | u1p3 | 1 if no wrong argument in the window, else 0 (no star row for Unit 1; computed for completeness) | Ready |
| U2.C1 | Topographic map matching glyph | 2 | u2p1 | attempts = 1 + count of the attempt feedback nodes 68:4, 68:5, 68:6, 68:7, 68:17, 68:18 before the solve 68:29; 2 for ≤ 2 attempts, 1 for 3–4, else 0 | Nodes |
| U2.C2 | Find Toppo | 1 | u2p2 | help dialogs ≤ 1 → 1; 2 → ½; more → 0 | Ready |
| U2.C3 | Find Tera **and** Find Aryn | 3 | u2p3 | each search separately: help dialogs ≤ 1 → 1½; 2–3 → 1; 4 → ½; more → 0; U2.C3 = Tera + Aryn (the rule already tracks both key sets and the point where the Aryn search starts, 18:231) | Ready, see D1 |
| U2.C4 | Watershed size / flow rate glyph | 2 | u2p4 | attempts from 74:4 (1st), 74:5 or 74:6 (2nd), 74:9 or 74:10 (3rd), 74:15 (4th) before the solve 74:21; 2 for ≤ 3 attempts, 1 for 4–5, else 0 | Nodes |
| U2.C5 | Classify argument components | 6 (see D2) | u2p5 | the rule's score: +1 per correct placement, −⅓ per incorrect | Ready |
| U2.C6 | Evidence selection | ½ | u2p6 | ½ if "Flow rate" (20:43) was chosen, 0 if 20:44 or 20:45 | Ready |
| U2.C7 | Argue which watershed is bigger | 3 | u2p7 | attempts = wrong submissions + 1 when the argument succeeded; ≤ 3 → 3; 4 → 2; 5 → 1; else 0 | Ready |
| (Unit 2) | Critique Jasper's argument | 1 | none | correct choices ÷ all choices in conversation 23: 23:52 "No. Jasper, you forgot evidence" is correct; 23:51 "you are right" and 23:53 "forgot a claim" are not | Input, see D3 |
| U3.C1 | Placement of crates | 3 | u3p1 | number of correct placements (10:30) | Ready |
| U3.C2 | Pollution sensors | 5 | u3p2 | the rule's 5-point score from the reminder counts (11:27 "test further upstream"; 11:29 "clean sensor" + 11:230 "top of branch") | Ready, see D4 |
| U3.C3 | Convince Tera | 4 | u3p3 | attempts band 3/2/1/0 + 1 if the backing-info panel was opened (the rule's total score) | Ready |
| U3.C4 | Glyph: dissolved particles | 2 | u3p4 | 2 if solved on the first attempt (no attempt feedback node), 1 on the second, else 0, from the rule's attempt nodes (78:4, 78:3 first attempt; 78:7 second; 78:9, 78:10 third …) | Nodes |
| U3.C5 | Plant superfruit seeds | 4 | u3p5 | the rule's score: correct − ½ × incorrect | Ready, see D5 |
| U4.C1 | Well wishes + soil puzzle key | 1½ | u4p1 | ½ for "boundary between saturated and unsaturated" (88:5) + 1 / ½ / 0 for a soil-key puzzle under 30 s / 90 s / longer (the rule's score) | Ready |
| U4.C2 | Glyph: infiltration | 2 | u4p2 | 2 if solved on the first attempt, 1 on the second, else 0; attempt nodes 102:3, 102:4 (first attempt) and the later ones in conversation 102, solve 88:11 | Nodes |
| U4.C3 | Dungeon levels 3 and 4 | 3 | u4p3 | 1 if gravel on the first try (level 3) + 2 / 1 / 0 for sand on the first / second / later try (level 4): the rule's score | Ready |
| U4.C4 | Dungeon level 5 + drill | 4 | u4p4 | the rule's score, with your change B3 (107:4 counts as a wrong drill choice) | Ready |
| U4.C5 | Saving Cadet Anderson | 4 | u4p5 | attempts band 3/2/1/0 + 1 if the warehouse-layout backing info was opened (new detection, same mechanism as U3.C3) | Nodes |
| U4.C6 | Tera's garden boxes | 3 | u4p6 | boxes with the right soil (the rule's score) | Ready |
| U5.C1 | Glyph: evaporation rate | 2 | u5p1 | 2 on the first attempt, 1 on the second or third, else 0; attempt nodes 100:33, 100:34 (1st), 100:35 (2nd), 100:36, 100:37 (3rd), 100:38, 100:39 (4th), 100:43 (5th), solve 100:44 | Nodes |
| U5.C2 | Chambers, levels 3 and 4 | 4 | u5p2 | the rule's score (its formula equals the working document's) | Ready |
| U5.C3 | What happened to the water? | 3 | u5p3 | attempts = wrong arguments + 1; ≤ 3 → 3; 4 → 2; 5 → 1; else 0 | Ready |
| U5.C4 | Solar still | 1½ | u5p4 | ½ each for Tilted Out, Uncovered ("X mark for no extra converting") and Cold, read from the outcome node of the **first** submission (see D6) | Ready |

## 3. Provisional decisions

**D1 — U2.C3 covers both the Tera and the Aryn search (max 3).** The working
document (v2) lists "Find Aryn" as row 2.4 directly under U2.C3 with a blank
checkpoint cell. The document uses a blank cell to continue the previous
checkpoint everywhere else (4.2 soil puzzle key under U4.C1, 4.5 under U4.C3,
4.7 under U4.C4, 5.3 under U5.C2), and the grader's rule for that stretch of
play already scores both searches together. So U2.C3 = Tera (max 1½) + Aryn
(max 1½), and Jasper's warmer line needs 2 of a possible 4 across finding
Toppo, Tera and Aryn. If you meant Tera only, the same line needs 2 of 2½.

**D2 — U2.C5 uses the raw score, maximum 6.** The document's points column
(+1 per correct, −⅓ per incorrect) is what the grader computes and what the
ceremony's "≥ 4" bar was written against; its formula column describes a
proportional version we are not using. "Need 6 correct for completion" gives
the maximum.

**D3 — "Critique Jasper's argument" is left out of the Unit 2 total for now.**
The document gives it 1 point (correct choices ÷ all choices) but no node ids.
The export shows the choice in conversation 23 (23:51, 23:52, 23:53) and a
similar one in conversation 20 (20:92, 20:93, 20:94, asked by Toppo). We will
add it once you confirm which conversation counts.

**D4 — U3.C2 reuses the grader's 5-point sensor score.** The document's three
parts (2 points for the "test further upstream" reminder, 2 for the "clean
sensor" reminder, 1 for never hearing the "we are at the ocean" line) map to
the production script's score except for the ocean line, whose node we could
not find in the export. Until we have it, the production script's grouping
(11:29 with 11:230) stands in for it.

**D5 — Tera's superfruit line plays the warmer version at U3.C5 ≥ 2.5, not
≥ 3.** The script says "3 correct garden plots". With four boxes and the
document's own formula (correct − ½ × incorrect), three correct plots and one
wrong is 2.5, and your answer A5 set the dashboard's green bar at 2.5 for the
same reason. At ≥ 3 a student with one wrong planting would be green on the
dashboard but hear the gentler line.

**D6 — U5.C4 is read from the outcome node.** The twelve solar-still outcome
nodes each name the settings that produced them (roof Tilted In / Flat / Tilted
Out, Covered / Uncovered, glass Cold / Hot), so the three half-points follow
directly: for example 106:28 (Tilted Out, Covered, Cold) scores 1, 106:35
(Tilted Out, Uncovered, Cold) scores 1½. We score the **first** submission,
since the activity is designed as one chance; a student who eventually reaches
106:35 after wrong tries keeps their first-submission score.

**D7 — Stars are banded by share of the unit maximum until the totals are
confirmed.** Adding the document's checkpoint maxima gives Unit 2 = 18½ (with
Aryn and the critique), Unit 3 = 18, Unit 4 = 17½, Unit 5 = 10½, but the
three-star bands top out at 15, 12, 16 and 10½. Only Unit 5 agrees. Read as
shares of the top value, the bands are consistent (two stars from about 57 %,
three from about 83 %), so until you confirm the intended totals the grader
awards three stars at ≥ 83 % of the unit's implemented maximum, two at ≥ 57 %,
otherwise one. A unit with no graded checkpoint gets no star row.

**D8 — Unit 1 has no star row.** The document's band table starts at Unit 2.
U1.C3 is still computed and stored.

**D9 — Existing students are backfilled.** Students graded before EA scores
existed get them by re-running the stored attempts; no colour changes.

**D10 — The ceremony is offered only after Unit 5 for now.** How a student who
stops after Unit 3 should be treated (which characters speak, whether the
award is given, what the star board shows for unplayed units) is a separate
decision for later; nothing in this document depends on it.

## 4. Questions

1. **U2.C3 (D1).** Does U2.C3 include the Aryn search, so that Jasper's warmer
   line needs 2 of 4? If it should be Tera only (2 of 2½), say so. If you would
   rather raise the bar to 3 when Aryn is included, say that instead.
2. **U2.C5 (D2).** Is a maximum of 6 right, and is the raw form (not the
   proportional formula) what you intend?
3. **Critique (D3).** Which conversation is the "Critique Jasper's argument"
   checkpoint: 23 (Jasper asks; correct answer "No. Jasper, you forgot
   evidence"), 20 (Toppo asks), or both? Do repeated attempts all count in the
   denominator?
4. **U3.C2 (D4).** Which dialogue node is the "We are at the ocean downstream
   of Tera's base" line? Is it acceptable to keep the production script's
   grouping until then?
5. **U3.C5 (D5).** Is 2.5 (three correct plots, one wrong) the right bar for
   Tera's warmer line, or must all four plots be correct?
6. **U5.C4 (D6).** First submission only, or the best submission?
7. **Star totals (D7).** What per-unit totals are the bands based on? If the
   bands were written for an earlier list of checkpoints, please restate them
   for the current list, or confirm the percentage reading.
8. **Attempt counting for glyph tasks (U2.C1, U2.C4, U3.C4, U4.C2, U5.C1).**
   We count attempts from the attempt-numbered feedback nodes listed in §2.
   Is a DANI-assisted solve (the assist and auto-solve nodes) a 0, as we
   assume?
9. **Backing info (U3.C3, U4.C5).** For U4.C5 we will detect the warehouse
   layout panel the same way U3.C3 detects the pollution site data panel. What
   is that panel's tool name in the logs?
10. **Anything the ceremony should not say.** The dialogue lines were approved
    in script v4. If any line should be held back for a student with no score
    at all (never reached the task), tell us which.

## 5. What happens next

The grader work starts now against the decisions above. Your answers are
applied as they arrive: a changed derivation is a rule edit and a regrade, a
changed threshold is a one-line change in the ceremony. Nothing here needs to
be settled before the first playable version.
