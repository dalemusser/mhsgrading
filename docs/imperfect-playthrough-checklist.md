# Deliberately imperfect playthrough — checklist

Companion to item D4 of `grading-team-questions-2026-09-answers.md`: one
playthrough of the release build that deliberately reaches the code paths no
fixture has covered, so the grader can be verified end to end. Play each item
in the listed unit, then share the log so it can be added as a fixture.

| # | Point | What to do in the game | What the log must show |
|---|-------|------------------------|------------------------|
| 1 | U2P1 Escape the Ruin | Submit four wrong glyph arrangements, decline DANI's offer after the fourth ("No, I'm okay"), then submit the correct one on the fifth attempt. | `68:22` or `68:23` then `68:29`, no assist node → EXCESS_ATTEMPTS, attempt 5. |
| 2 | U2P4 Investigate the Temple | Submit five wrong watershed arrangements (decline the offer if it appears after the fifth), then the correct one on the sixth. | `74:16` or `74:17` then `74:21`, no assist node → EXCESS_ATTEMPTS, attempt 6. |
| 3 | U3P4 (glyph) | Solve the glyph alone after enough wrong submissions to go yellow, without accepting or being forced into DANI's assist. | Success node with no assist node → EXCESS_ATTEMPTS. |
| 4 | U4P2 (glyph) | Same as item 3 for the Unit 4 glyph (conversation 102). | Success node with no assist node → EXCESS_ATTEMPTS. |
| 5 | U5P1 (glyph) | Same as item 3 for the Unit 5 glyph (conversation 100). | Success node with no assist node → EXCESS_ATTEMPTS. |
| 6 | U2P3 Band Back Together II | The still-uncovered branch named in the D4 reply. | Per the reply. |
| 7 | U2P6 Which Watershed? I | Choose "Salinity" (`20:45`) when Toppo asks for the strongest evidence. | `20:45` → WRONG_EVIDENCE_SELECTED, wrong_choice "salinity". |
| 8 | U2P6 Which Watershed? I | Both-options branch, if the build allows a second choice. | `20:44` and `20:45` in one window. |
| 9 | U3P2 Pollution Solution | **Throw one sensor into the ocean at the river mouth** (added 2026-09-24). | Whether `11:30` fires at all, and whether `11:27` fires with it. Decides where, if anywhere, `11:30` belongs in the penalty formula (see the Event Keys note in `mhs-unit3-point2-grading.md`). |
| 10 | U3P4 Forsaken Facility (D3) | Submit three wrong orders, then on the fourth wrong order **accept** DANI's offer ("Sure. I'm stuck"). Note whether the pieces move by themselves or you have to place them. | `78:18` → `78:20` → `78:21`, then `78:24` → SOLVED_WITH_ASSIST, attempt 4 (assist keys added 2026-09-24, path never observed). Placements between `78:21` and `78:24` confirm the auto-solve bug. |
| 11 | U4P6 Desert Delicacies | When Tera first asks "is everything set?", answer **"Actually, let me move some cameras and I'll come back."** (`92:34`), move at least one camera, then answer "I'm all set" at her second check (added 2026-09-24). | `92:34` → `92:35` → `92:36` → the three feedback nodes (`92:61`/`62`/`63`), with no `92:33`. Confirms the second-round route on the release build (seen once on build 20260902, run 09-03-26-2) so `92:36` can be added as a second review anchor (grading-team questions, B list). |
| 12 | U4P5 Saving Cadet Anderson | In the flooding argument, **open both Backing Information orbs** (the warehouse soil-layer/fountain panel and the soil-flow-rate panel) before submitting, and note their on-screen titles (added 2026-09-24). | `argumentationToolEvent` records with `argumentationTitle` "Unit 4 - Flooding" and `toolName` `BackingInfoPanel - Soil Layers and Fountain Data` / `BackingInfoPanel - Soil Flow Rates`. No build since 20260812 has logged any Unit 4 tool event, although the missing `90:48`/`90:49` nudges in runs 09-03-26-3 and 09-14-26-3 imply a panel was opened; decides whether the U4.C5 backing-info bonus can be detected at all. |

Notes

- Items 1, 2, 9 and 11 were checked against the 2026-09-21 dialogue database on
  2026-09-24; the gate conditions for items 1, 2 and 11 are in the export.
- Play the rest of each unit normally so every other point still grades green
  and the run can serve as a fixture for both validation suites.
