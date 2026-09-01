# Gameplay-Log → Progress-Point Grading Audit — build 08-25-26

- Logs: `playthrough-logs-and-results/08-25-26` — single full playthrough, all 5 units complete (player `6a8db41fa68c657728943067`).
- Stage 1 = can the current logs still feed each grading rule; Stage 2 = does the production logic then produce a defensible color.
- Detailed evidence: `outputs/*.json|csv`; per-point reports: `reports/progress-points/`.

## Headline numbers

| Stage | Result |
|---|---|
| Progress points examined | 26 |
| Stage 1 — READY_FOR_GRADING_TEST | 23 |
| Stage 1 — PARTIALLY_AUDITABLE | 3 |
| Stage 2 — PASS | 15 |
| Stage 2 — EXECUTED_NO_INDEPENDENT_CHECK | 9 |
| Stage 2 — MISMATCH_NEEDS_REVIEW | 2 |

## Cross-cutting findings (affect many/all points)

1. **Top-level player field changed: `playerId` → `user_id`.** The 05-01-26 export carried `playerId`; the 08-13/08-25 exports carry only `user_id`. Every production script filters on `playerId` and would match nothing against these exports. Stage 2 ran with a declared translation (playerId -> user_id). Whether the live grading DB changed too cannot be verified from this repo — **confirm with the dev team**; if it did, all 26 scripts need the field rename.
2. **7 dead dialogue references** (absent from both dialogue sources, so they can never fire): `DialogueNodeEvent:26:171` (U2P5); `DialogueNodeEvent:27:19` (U2P7); `DialogueNodeEvent:27:21` (U2P7); `DialogueNodeEvent:27:22` (U2P7); `DialogueNodeEvent:27:23` (U2P7); `DialogueNodeEvent:27:24` (U2P7); `DialogueNodeEvent:70:33` (U1P3).
3. **Stale test transcriptions**: `tests/test_u2p6.py` and `tests/test_u3p3.py` still implement the pre-2026-07-22 production windows; the audit used corrected overrides (see grading-validation.json). The tests should be re-synced with the markdown.
4. **Doc-vs-production window anchors differ** for: U1P3, U1P4, U2P4, U2P5, U2P6, U2P7, U3P1, U3P2, U3P3, U4P1, U4P2, U5P1 — same bug class that produced the round-1 U2P6/U3P3 miscolors. On this playthrough the doc-derived windows agreed with production colors wherever both were computable, but the divergent anchors remain fragile on replays.
5. **Dialogue DB export is 2026-06-10** vs build 2026-08-19: text-level conclusions carry that staleness caveat (MEDIUM confidence ceiling).
6. **eventKey↔payload mismatches** exist in 15 DialogueEvent records (weekly QA finding); none hit grading keys in this dump, but keyed grading is exposed to them.
7. **Documented window ≠ implemented window** inside 8 grading files: the 'Attempt Window (Production)' block cites an anchor the production script never queries — the script bounds the window with the previous occurrence of its END trigger instead: U2P1 (`DialogueNodeEvent:18:1`), U3P1 (`DialogueNodeEvent:10:1`), U3P2 (`questFinishEvent:17`), U3P3 (`DialogueNodeEvent:11:34`), U3P5 (`DialogueNodeEvent:73:200`), U4P2 (`DialogueNodeEvent:88:10`), U4P3 (`questActiveEvent:48`), U4P5 (`questActiveEvent:36`). This is the same anchor-divergence class that produced the round-1 U2P6/U3P3 miscolors; harmless on a first playthrough, fragile on replays.

## Master table

| PP | Rubric requirement | Required log evidence | Current evidence | Log support | Grading test | Root cause | Recommended action |
|---|---|---|---|---|---|---|---|
| U1P1 | Completion-only check. If the trigger event exists for the player, th… | 2 event keys | 2/2 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U1P2 | Completion-only check. If the trigger event exists for the player, th… | 2 event keys | 2/2 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U1P3 | Check whether the student needed multiple attempts to build the corre… | 3 event keys | 1/3 observed | PARTIALLY_AUDITABLE | PASS (green) | — | Grading code: replace/confirm the dead dialogue references (they can never fire per the c… |
| U1P4 | Completion-only check. If the trigger event exists for the player, th… | 2 event keys | 2/2 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P1 | Student must complete the map-profile matching independently and with… | 8 event keys | 3/8 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P2 | Windowed rule using client timestamps. Count wrong-direction prompts … | 11 event keys | 2/11 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U2P3 | Windowed rule using client timestamps. Count wrong-direction prompts … | 36 event keys | 3/36 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P4 | Student must complete the watershed-flow matching independently and s… | 6 event keys | 2/6 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U2P5 | Score-based rule. Count positive (correct) and negative (incorrect) a… | 48 event keys | 5/48 observed | PARTIALLY_AUDITABLE | PASS (green) | — | Grading code: replace/confirm the dead dialogue references (they can never fire per the c… |
| U2P6 | Student must select the correct criterion for determining watershed s… | 5 event keys | 3/5 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U2P7 | Student must successfully build the watershed argument with limited i… | 22 event keys | 2/22 observed | PARTIALLY_AUDITABLE | PASS (green) | — | Grading code: replace/confirm the dead dialogue references (they can never fire per the c… |
| U3P1 | Count-based rule. The student must have more than one occurrence of t… | 3 event keys | 3/3 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P2 | Score-based rule with capped penalties. The student starts with 5 poi… | 5 event keys | 2/5 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P3 | Score-based rule with a bonus. Count incorrect argument selections, c… | 20 event keys + 1 event type(s) | 4/21 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U3P4 | Gate + score-based rule. First, the student must have the gate event … | 11 event keys | 3/11 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U3P5 | Score-based rule using weighted positive and negative counts. | 6 event keys | 3/6 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P1 | This progress point is a score-based assessment rubric. First, it wil… | 4 event keys + 1 event type(s) | 5/5 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U4P2 | This progress point will check how many attempts the player used to f… | 8 event keys | 2/8 observed | READY_FOR_GRADING_TEST | MISMATCH_NEEDS_REVIEW (yellow→exp green) | SEMANTIC_DRIFT: success dialogue 88:11 did not fire although the puzzle was com… | Dev team + replay: confirm whether the post-glyph success dialogue (88:11) still fires in… |
| U4P3 | This progress point will check how many times the player interacts wi… | 2 event keys + 1 event type(s) | 3/3 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P4 | This progress point is score based. There are two tasks under this pr… | 7 event keys + 1 event type(s) | 4/8 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U4P5 | This progress point recording how players perform within the argument… | 17 event keys | 3/17 observed | READY_FOR_GRADING_TEST | PASS (green) | — | None — supported and validated on this playthrough; keep monitoring weekly. |
| U4P6 | This is a score-based progress point. There are three garden boxes, e… | 2 event keys + 1 event type(s) | 3/3 observed | READY_FOR_GRADING_TEST | MISMATCH_NEEDS_REVIEW (yellow→exp green) | GRADING_COLOR_MAPPING_BUG: production box->soil map contradicts the grading fil… | Grading code + spec: confirm the intended box→soil mapping with game design, then fix the… |
| U5P1 | This progress point is a attempt-based progress, if the player solved… | 7 event keys | 4/7 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U5P2 | This progress point is a score-based progress, at the beggining the s… | 2 event keys + 1 event type(s) | 3/3 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U5P3 | This progress point is an attempt-based, if the total number of follo… | 35 event keys | 2/35 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |
| U5P4 | This progress point is a number-based progress. Firstly, it will chec… | 14 event keys | 3/14 observed | READY_FOR_GRADING_TEST | EXECUTED_NO_INDEPENDENT_CHECK (green) | — | More playtesting: production executed cleanly, but this playthrough gave no independent w… |

## Answers to the standing audit questions

1. **Examined:** 26 progress points (all).
2. **READY_FOR_GRADING_TEST:** 23.
3. **Needing identifier/schema mapping updates:** 0 blocking today, but the global `playerId`→`user_id` rename (finding 1) applies to all 26 if the live DB changed; U4P2's success marker is a drift candidate.
4. **Blocked by missing logging:** 0 — every window anchor and required evidence family fired in this playthrough.
5. **Not fully evaluable due to unexercised behavior:** 9 points executed but had no independent expectation (custom windows; error paths never exercised).
6. **Affected by game-design/dialogue-flow change:** U4P2 (success dialogue did not fire on a clean solve — drift candidate); the U2 help-dialog conversations (28/59) and several feedback conversations never fired, consistent with flow changes but not provable from one playthrough.
7. **Grading-logic problems:** U4P6 (box→soil map inverted vs prose/analytics/Go), plus 3 points carrying dead rubric keys (U1P3 `70:33`, U2P5 `26:171`, U2P7 `27:19/21/22/23/24`), plus divergent window anchors (finding 4).
8. **Problematic identifiers across multiple points:** conversation-ID sets in the source docs vs production differ for most scored points (see per-point §8); dead node IDs cluster in feedback conversations 26/27/70.
9. **Prioritize for additional playtesting:** U4P2 (clean replay, no debug menu), U4P6 (replay after mapping decision), plus any point whose yellow paths were never exercised (U2P1, U2P6, U3P4, U5P1, U5P3, U5P4).
10. **Dev team vs dashboard:** dev team — player-field rename confirmation, U4P2 dialogue flow, dialogue-DB export refresh; dashboard — U4P6 mapping fix, dead-key cleanup, re-sync of tests with the fixed markdown scripts.

## Priorities

### Priority A — logging blocks grading entirely
- None on this build/playthrough. (Watch the `playerId`→`user_id` question: if the live collection changed, this becomes an A for all 26 points.)

### Priority B — evidence exists but grading mapping/code must change
- **U4P6**: box→soil mapping inverted in the production script (player's correct-looking placements graded yellow).
- **U1P3 / U2P5 / U2P7**: remove/replace dead dialogue keys (cannot fire).
- **tests/**: re-sync `test_u2p6.py`, `test_u3p3.py` with the 2026-07-22 markdown fixes.

### Priority C — additional targeted playthrough required
- **U4P2**: clean replay without the debug menu to establish whether the success dialogue (88:11) still fires.
- Yellow/failure paths for U2P1, U2P6, U3P4, U5P1, U5P3, U5P4 were never exercised; a deliberately-imperfect run would validate their counting logic.

### Priority D — specification clarification required
- Intended box→soil assignment for U4P6 (three implementations disagree).
- Doc-vs-production window anchors (finding 4): confirm which interval definition is authoritative per point, then align docs or scripts.
- Refresh `Dialogue-ID-Texts.xlsx` / dialogue export to the current build.
