# Gameplay-Log → Progress-Point Grading Audit — build 09-23-26

- Logs: `playthrough-logs-and-results/09-23-26` — single playthrough, Unit1/Unit2/Unit3/Unit4/Unit5 complete (player `6ab42757bf592cbac358b8c1`).
- Stage 1 = can the current logs still feed each grading rule; Stage 2 = does the production logic then produce a defensible color.
- Detailed evidence: `outputs/*.json|csv`; per-point reports: `reports/progress-points/`.

## Headline numbers

| Stage | Result |
|---|---|
| Progress points examined | 26 |
| Stage 1 — READY_FOR_GRADING_TEST | 26 |
| Stage 2 — PASS | 23 |
| Stage 2 — EXECUTED_NO_INDEPENDENT_CHECK | 2 |
| Stage 2 — MISMATCH_NEEDS_REVIEW | 1 |

## Cross-cutting findings (affect many/all points)

1. **Top-level player field: `user_id` (production scripts filter on `playerId`).** The 05-01-26 export carried `playerId`; every export since 08-13 carries only `user_id`. Unadapted production scripts would match nothing against this export. Stage 2 ran with a declared translation (playerId -> user_id). Whether the live grading DB changed too cannot be verified from this repo — **confirm with the dev team**; if it did, all 26 scripts need the field rename.
2. **1 dead dialogue reference(s)** (absent from both dialogue sources, so they can never fire): `DialogueNodeEvent:70:33` (U1P3).
3. **Doc-vs-production window anchors differ** for: U1P4, U2P3, U2P6, U2P7, U3P1, U3P3, U5P1 — same bug class that produced the round-1 U2P6/U3P3 miscolors. Doc-derived windows DISAGREED with production colors for: U2P6 — active miscolor risk.
4. **Dialogue DB export is 2026-09-21** vs game build 20260914-: text-level conclusions are only as current as that export (MEDIUM confidence ceiling whenever it lags the build).
5. **eventKey↔payload mismatches** exist in 17 DialogueEvent record(s) in this dump; none hit grading keys in this dump, but keyed grading is exposed to them.

## Master table

| PP | Rubric requirement | Required log evidence | Current evidence | Log support | Grading test | Root cause | Recommended action |
|---|---|---|---|---|---|---|---|
| U1P1 | Completion-only check. If the trigger event exists for the player, th… | 2 event keys | 2/2 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U1P2 | Completion-only check. If the trigger event exists for the player, th… | 2 event keys | 2/2 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U1P3 | Check whether the student needed multiple attempts to build the corre… | 3 event keys | 2/3 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U1P4 | Completion-only check. If the trigger event exists for the player, th… | 2 event keys | 2/2 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P1 | Student must complete the map-profile matching independently and with… | 8 event keys | 5/8 observed | READY_FOR_GRADING_TEST | PASS (yellow) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P2 | Windowed rule using client timestamps. Count wrong-direction prompts … | 8 event keys | 2/8 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U2P3 | Windowed rule using client timestamps. Count wrong-direction prompts … | 37 event keys | 2/37 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P4 | Student must complete the watershed-flow matching independently and s… | 7 event keys | 4/7 observed | READY_FOR_GRADING_TEST | PASS (yellow) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P5 | Score-based rule. Count positive (correct) and negative (incorrect) a… | 56 event keys | 8/56 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P6 | Student must select the correct criterion for determining watershed s… | 5 event keys | 3/5 observed | READY_FOR_GRADING_TEST | MISMATCH_NEEDS_REVIEW (green→exp yellow) | GRADING_SEQUENCE_BUG candidate: production attempt window and the doc-derived a… | Manual review of the window/evidence mismatch (see this point's §10–11 for the traced div… |
| U2P7 | Student must successfully build the watershed argument with limited i… | 18 event keys | 3/18 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P1 | Count-based rule. The student must have more than one occurrence of t… | 3 event keys | 3/3 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P2 | Score-based rule with capped penalties. The student starts with 5 poi… | 5 event keys | 3/5 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P3 | Score-based rule with a bonus. Count incorrect argument selections, c… | 20 event keys + 1 event type(s) | 4/21 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P4 | Gate + score-based rule. First, the student must have the gate event … | 11 event keys | 8/11 observed | READY_FOR_GRADING_TEST | PASS (yellow) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P5 | Score-based rule using weighted positive and negative counts. | 6 event keys | 3/6 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P1 | This progress point is a score-based assessment rubric. First, it wil… | 2 event keys + 1 event type(s) | 3/3 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P2 | This progress point will check how many attempts the player used to f… | 7 event keys + 1 event type(s) | 6/8 observed | READY_FOR_GRADING_TEST | PASS (yellow) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P3 | This progress point will check how many times the player interacts wi… | 2 event keys + 1 event type(s) | 3/3 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P4 | This progress point is score based. There are two tasks under this pr… | 7 event keys + 1 event type(s) | 4/8 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P5 | This progress point records how the player performs in the flooding a… | 17 event keys | 3/17 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P6 | This is a score-based progress point. There are three garden boxes, e… | 4 event keys + 1 event type(s) | 4/5 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U5P1 | This progress point is an attempt-based progress. If the player solve… | 6 event keys | 4/6 observed | READY_FOR_GRADING_TEST | PASS (yellow) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U5P2 | This is a score-based progress point. The score starts at 0. On the t… | 2 event keys + 1 event type(s) | 3/3 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U5P3 | This progress point is attempt-based: it counts Dr. Toppo's wrong-ans… | 41 event keys | 2/41 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U5P4 | This progress point is a number-based progress. Firstly, it will chec… | 14 event keys | 3/14 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |

## Answers to the standing audit questions

1. **Examined:** 26 progress points (all).
2. **READY_FOR_GRADING_TEST:** 26.
3. **Needing identifier/schema mapping updates:** none — plus the global `playerId` field question (finding 1) if the live DB changed.
4. **Blocked by missing logging:** none — every window anchor and required evidence family fired in this playthrough.
5. **Not fully evaluable due to unexercised behavior:** 2 point(s) executed but had no independent expectation (U2P2, U5P4).
6. **Affected by game-design/dialogue-flow change (drift candidates):** none (see per-point §11 root causes).
7. **Grading-logic problems:** U2P6; dead rubric keys remain in: U1P3 (`DialogueNodeEvent:70:33`); divergent window anchors: U1P4, U2P3, U2P6, U2P7, U3P1, U3P3, U5P1.
8. **Problematic identifiers across multiple points:** see per-point §8 DOC_PROD_REFERENCE_MISMATCH flags (rubric dialogue tags vs production keys) and the reconciliation table for cross-conversation relocations.
9. **Prioritize for additional playtesting:** U2P2, U2P6, U5P4 — mismatches need targeted replays; unexercised failure paths need a deliberately-imperfect run.
10. **Dev team vs dashboard:** dev team — player-field rename confirmation, dialogue-flow drift candidates (Q6), dialogue-DB export refresh; dashboard — grading-logic problems (Q7), dead-key cleanup, re-sync of stale `rubric-validation/` modules with the current markdown scripts.

## Priorities

### Priority A — logging blocks grading entirely
- None on this build/playthrough. (Watch the `playerId` field question: if the live collection changed, this becomes an A for all 26 points.)

### Priority B — evidence exists but grading mapping/code must change
- **U2P6**: GRADING_SEQUENCE_BUG candidate: production attempt window and the doc-derived activity interval select different evidence
- **U1P3**: remove/replace dead dialogue key(s) `DialogueNodeEvent:70:33` (cannot fire).

### Priority C — additional targeted playthrough required
- Yellow/failure paths for U2P2, U5P4 were never exercised; a deliberately-imperfect run would validate their counting logic.

### Priority D — specification clarification required
- Doc-vs-production window anchors: confirm which interval definition is authoritative per point, then align docs or scripts (U1P4, U2P3, U2P6, U2P7, U3P1, U3P3, U5P1).
- Refresh `Dialogue-ID-Texts.xlsx` / dialogue export to the current build.
