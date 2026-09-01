# Audit Comparison — 08-31-26 run vs 08-25-26 run

New playthrough: `playthrough-logs-and-results/08-31-26` (build **20260826-12286**, 5,977 records, single player `6a95b79ce2ada9cb13ea6f13`, all 5 units complete, **zero debug-menu use**).
Audited against the **updated** grading logic (2026-08-31 edits to U1P3, U2P2, U2P4, U2P5, U2P7, U4P6).
Full details: `reports/08-31-26/audit-summary.md` and `reports/08-31-26/progress-points/`. Previous run: `reports/08-25-26/audit-summary.md` (08-25-26, build 20260819-12237; relocated 2026-09-01 from the reports/ root into its per-run dir).

## Headline

| Metric | 08-25-26 | 08-31-26 |
|---|---|---|
| Stage 1 READY_FOR_GRADING_TEST | 23 | **24** |
| Stage 1 PARTIALLY_AUDITABLE | 3 (U1P3, U2P5, U2P7 — dead keys) | 2 (U4P1, U4P2 — unfired prose anchor 88:10) |
| Stage 2 PASS | 15 | **17** |
| Stage 2 MISMATCH_NEEDS_REVIEW | 2 (U4P6, U4P2) | **0** |
| Stage 2 EXECUTED_NO_INDEPENDENT_CHECK | 9 | 9 |
| Dead dialogue references | 7 | 1 (rubric-doc-only) |

Both previous Stage-2 mismatches are resolved. One **new** color-affecting issue surfaced: **U4P1 grades yellow despite a completed activity** (details below).

## Issues resolved by the grading-logic modifications

1. **U4P6 box→soil mapping fix — verified working.** The player placed Gravel/Sand/Clay in boxes 0/1/2; the fixed script scores 3/3 → **green**, agreeing with the rule prose and the analytics/Go mapping. Under the old inverted map this same play would again have graded yellow (only box 1 correct). Status: MISMATCH_NEEDS_REVIEW → **PASS**.

2. **U4P2 success-dialogue drift hypothesis — refuted; point now passes.** This was the clean replay the last audit asked for (no DEBUGMenu events anywhere in the dump). The glyph quest completed with zero conv-102 hint/wrong-answer nodes, and this time the success node `88:11` **did fire**; production grades **green**, the doc-derived window agrees. The 08-25 non-firing was almost certainly the debug-menu confound, not a changed dialogue flow. No grading change needed. Status: MISMATCH_NEEDS_REVIEW → **PASS**.

3. **Dead-key cleanup (U1P3 `70:33`, U2P5 `26:171`, U2P7 `27:19/21–24`) — effective.** All three points moved PARTIALLY_AUDITABLE → **READY_FOR_GRADING_TEST**. None of the removed keys appeared in the new logs (they were unfireable), so the removals are behavior-neutral while making the rules honest.

4. **U2P5 key remap — validated live.** Two of the newly added positive keys (`26:142`, `26:146`) actually fired and counted (pos = 6, neg = 0 → green). Under the old key set the score would have been exactly 4 — right at the threshold — so the remap materially improves evidence capture. The classification matches the dialogue text semantics ("Nice Job/Great" = positive, "Too bad/Oh no" = negative); the unclassified conv-26 nodes that fired (136, 141) are a wrap-up line and an empty hub node — correctly excluded.

5. **U2P2 conv-18 key removal — executed cleanly.** Window built, 0 wrong-direction prompts → green. The removed keys (`18:99/223/224`) never fired this run, so no old-vs-new divergence was observable (this point still has no independent cross-check).

6. **Bonus: U1P3's yellow path exercised for the first time.** The player picked a wrong argument (`70:25` at 17:38:44) before succeeding (`70:7`), inside the window → production **yellow**, doc-derived window agrees → PASS. The failure branch of this rule is now validated on real behavior (it was never exercised in prior runs).

## New issue

**U4P1 grades yellow although the activity was completed — anchor-robustness bug (grading logic, not logging).**
The (unmodified) U4P1 production script windows on latest `88:0` → latest `88:10`. Node `88:10` is an optional "[Conjecture] That is a… drill?" line; this run's player path through conversation 88 was 0→19→1→2→3→4→5→8→9→**11**→12, skipping 10 — so no window → default yellow, even though the Soil Key Puzzle was demonstrably done (Started ×4 / Finished ×4). The 08-25 run got green only because that player happened to hit 88:10. Note the mirror image: 08-25 fired 88:10 but not 88:11; 08-31 fired 88:11 but not 88:10 — **both are branch-dependent nodes and neither is a safe anchor**. Recommend re-anchoring U4P1's window end on a guaranteed-on-path event (e.g. `questActiveEvent:39` or the `Soil Key Puzzle` Finished record, per design intent).

## Issues that still remain

1. **Documented window ≠ implemented window grew from 8 to 10 files.** The U1P3 and U2P4 edits changed only the "Attempt Window (Production)" prose blocks (now citing `30:98` / `22:18` as start anchors) — **the production scripts below them were not changed** and still window on previous/latest of their end trigger. If the new prose anchors are the intent, the scripts need the matching edit; if not, the prose should be reverted. (Full list of 10 in audit-summary finding 7.)
2. **U2P4 markdown corruption introduced by the edit:** four "Bad Feedback" table rows are pasted *inside* the Analytics Script code fence (`mhs-unit2-point4-grading.md` ~lines 41–44) instead of the Event Keys table. Grading is unaffected (the production fence is intact) but the file should be repaired.
3. **U4P6 leftover stale prose:** the WRONG_CHOISE_SELECTED "Determination" line still says "Box 0 = Clay, Box 1 = Sand, Box 2 = Gravel" — contradicting the fixed scripts. One-line fix.
4. **Rubric doc still cites dead node `70:33`** (Progress-Points.docx U1P3 tags). Production no longer references it; the source doc should drop it at the next revision.
5. **7 stale `tests/` transcriptions** (u1p3, u2p2, u2p5, u2p6, u2p7, u3p3, u4p6) — Stage 2 ran audit-local overrides of the current markdown; re-sync the test modules to retire the overrides.
6. **`playerId` → `user_id`** field question unchanged — still needs dev-team confirmation for the live grading DB.
7. **Dialogue export staleness** — 2026-06-10 export vs build 20260826-12286 (text-level conclusions capped at MEDIUM confidence).
8. **9 points still have no independent check** (U2P2, U2P6, U3P4, U4P1, U4P4, U5P1, U5P2, U5P3, U5P4): their failure/yellow paths were never exercised in any playthrough so far.

## Logging / schema changes in the new build

None that affect grading. Same record schema, same `user_id` player field, 22 event types observed (the "missing" 23rd is `DEBUGMenu` — simply unused this run, which is good). eventKey↔payload mismatches: 17 records (was 15), still none touching grading keys. New this run: several anchors fired 2× (U3P4, U4P4, U4P5, U5P4 — the tester replayed sections), a useful stress of the "previous trigger" windows; all checkable colors still passed.

## Regressions

No grading-logic regressions from the 2026-08-31 modifications: every point that passed on 08-25 still passes, and the changed rules behaved exactly as their updated scripts specify. The U4P1 yellow is **not** a regression (its logic is unchanged) — it is a latent anchor bug newly exposed by this play path.

## Attribution of remaining problems

- **Grading logic / documentation:** U4P1 anchor choice; prose-vs-script window divergence (10 files); U2P4 markdown corruption; U4P6 stale reason-code line; stale tests.
- **Rubric/source docs:** dead tag 70:33; dialogue export refresh.
- **Gameplay logging:** nothing blocking on this build.
- **Playthrough coverage:** 9 unexercised failure paths.

## What to address next (ordered)

1. **Fix U4P1's window end anchor** — the only issue producing a wrong color on this run.
2. **Repair `mhs-unit2-point4-grading.md`** (move the Bad Feedback rows back into the Event Keys table).
3. **Decide the U1P3/U2P4 window intent** — align the production scripts with the new prose anchors (30:98 / 22:18) or revert the prose; same decision for the other 8 divergent files.
4. **One-line cleanups:** U4P6 Determination line; drop 70:33 from the rubric doc.
5. **Re-sync the 7 stale `tests/` modules** with the current markdown (retires the audit overrides).
6. **Deliberately-imperfect replay** to exercise the 9 unvalidated failure paths.
7. Standing items: confirm `playerId`→`user_id` with the dev team; refresh the dialogue export.
