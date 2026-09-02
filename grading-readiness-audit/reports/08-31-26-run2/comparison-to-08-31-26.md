# Run 08-31-26-run2 vs run 08-31-26 — validation of the 2026-09-01 grading-logic modifications

Both runs audit the **same log dump** (`playthrough-logs-and-results/08-31-26`,
game build 20260826-12286, clean full playthrough, no DEBUGMenu). What changed
between them is the **grading logic**: after the 08-31-26 audit report, three
grading files were modified on 2026-09-01 —

| File | Modification |
|---|---|
| `mhs-unit4-point1-grading.md` | End anchor re-anchored: optional dialogue node `DialogueNodeEvent:88:10` → close of the Unit 4 soil key puzzle (`Soil Key Puzzle` event, `Soil Key Puzzle Status` = `Finished`, `data.Unit` matching `/^Unit 4/`). Unit-4 filter also added to the analytics script (the puzzle fires in Units 2/3/4). |
| `mhs-unit4-point2-grading.md` | Start anchor re-anchored: `DialogueNodeEvent:88:10` (prose) / previous `questActiveEvent:48` (script) → latest Unit 4 soil-key close before the trigger. This also removed the prose-vs-script window divergence this file had. |
| `mhs-unit4-point6-grading.md` | Box-id-independent OR fallback added: final score = max(box-id score, count of correct-soil feedback `DialogueNodeEvent:92:61` after the latest review-start `92:33` in the window, capped 3). Reason-code Determination's inverted box map also fixed (now Box 0=Gravel, 1=Sand, 2=Clay). |

This run answers: **did those modifications fix the previously identified
issues without introducing regressions?**

## Headline comparison

| Metric | 08-31-26 (prev) | 08-31-26-run2 (this) |
|---|---|---|
| Stage 1 READY_FOR_GRADING_TEST | 24 | **26** |
| Stage 1 PARTIALLY_AUDITABLE | 2 (U4P1, U4P2) | **0** |
| Stage 2 PASS | 17 | **18** |
| Stage 2 MISMATCH | 0 | **0** |
| Stage 2 EXECUTED_NO_INDEPENDENT_CHECK | 9 | 8 |
| Production colors changed vs prev run | — | 1 (U4P1 yellow → green) |

## Resolved issues (grading-side fixes verified)

1. **U4P1 "yellow despite completed puzzle" — FIXED.** The 08-31-26 run's
   headline bug: the production window ended on optional node 88:10, which
   never fires on a clean solve (88:10 vs 88:11 are alternate branches), so
   the point graded yellow for a player who completed everything correctly.
   With the soil-key-close anchor the window now closes at
   `_id 6a9615ad485cab4c953dc7c3` (the Unit 4 `Finished` record), production
   grades **green** (score 1.5: correct choice 88:5 +0.5, puzzle duration
   11.188 s +1.0), and the new independent check (rubric formula on
   unwindowed evidence) **PASSes** at MEDIUM confidence.
2. **U4P1/U4P2 PARTIALLY_AUDITABLE — RESOLVED.** Both points' windows now
   anchor exclusively on events that fire deterministically on the observed
   play path (88:0 / soil-key close / quest 48); Stage 1 classifies both
   READY_FOR_GRADING_TEST (U4P1 at HIGH confidence, no flags).
3. **U4P2 prose-vs-script window divergence — RESOLVED.** The Attempt-Window
   block and the production script now describe the same window. The
   summary's "documented window ≠ implemented window" list dropped from 10
   files (prev runs) to 9 — U4P2 left the list.
4. **U4P6 stale reason-code map — RESOLVED.** The WRONG_CHOISE_SELECTED
   Determination line now matches the fixed box→soil map used everywhere else.
5. **U4P6 box-id fragility — mitigated (new insurance, verified offline).**
   Production now grades green through either evidence path. On this dump the
   two paths agree (box score 3, dialogue score 3 — three `92:61` after
   `92:33`, zero `92:62`/`92:63`). A simulated box-id shift (all `boxId`
   values renamed) drops the box score to 0 while the dialogue fallback keeps
   the grade green — the failure mode that motivated the change no longer
   flips this point.

## Issues that remain (unchanged from the previous run)

- **`user_id` vs `playerId`** (schema/identifier change, logging-side): every
  export since 08-13 identifies the player via `user_id`; production scripts
  filter on `playerId`. Stage 2 ran with the declared adaptation. Whether the
  live grading DB changed too is still UNCONFIRMED with the dev team.
- **Dead dialogue reference `70:33` in U1P3 prose** (outdated technical
  reference; the script no longer uses it).
- **Doc-vs-production anchor divergences** (U1P4, U2P5, U2P6, U2P7, U3P1,
  U3P2, U3P3, U5P1) and the **9 remaining prose-vs-script window files**
  (U1P3, U2P1, U2P4, U3P1, U3P2, U3P3, U3P5, U4P3, U4P5) — harmless on a
  first playthrough, fragile on replays. Rubric/spec-side cleanup.
- **Dialogue DB export staleness** (2026-06-10 vs build 20260826-12286) caps
  text-level conclusions at MEDIUM confidence.
- **Stale `tests/` transcriptions — now 9** (was 7): U4P1, U4P2 joined
  U1P3/U2P2/U2P5/U2P6/U2P7/U3P3, and U4P6's entry deepened (fallback not
  transcribed). Stage 2 executed audit-local overrides of the current
  markdown; the tests/ modules should be re-synced, which retires the
  overrides.

## Newly introduced issues / regressions

**None observed.** The only production-color change between runs is the
intended U4P1 yellow → green; all 23 other executable points kept their color
and status, and Stage 1 statuses only improved (2 upgrades, 0 downgrades).
Watch items created by the new logic (not defects, untestable on this dump):

- U4P1/U4P2 now depend on the `Soil Key Puzzle` status records carrying
  `data.Unit` with a scene-name value (`"Unit 4 Dev"` on this build). The
  scripts match by `/^Unit 4/` prefix because scene names are build-flavored;
  a scene rename that drops the "Unit 4" prefix would break both anchors.
- U4P6's dialogue fallback assumes one feedback node per box per review
  round. A re-inspected plant re-firing `92:61` could in principle inflate
  the dialogue score (bounded by the `92:33` round anchor and the cap of 3).

## Logging/schema/identifier changes in this build

None new — same dump as the previous run. (The `user_id` adaptation and the
17 eventKey↔payload mismatch records carry over unchanged.)

## Still untestable on this playthrough (insufficient coverage, not defects)

- The **yellow paths** of U4P1 (slow/failed puzzle), U4P2 (negative conv-102
  feedback — `102:9/10/12/18/23` all 0×), and U4P6 (wrong soil → `92:62`/
  `92:63`, both 0×): the clean playthrough never exercises them. All these
  nodes still exist in the dialogue DB, so they can fire (reconciliation:
  EXPECTED_DIALOGUE_NOT_OBSERVED — counted evidence, zero is a valid input).
- The 8 EXECUTED_NO_INDEPENDENT_CHECK points (U2P2, U2P6, U3P4, U4P4, U5P1,
  U5P2, U5P3, U5P4): production executed cleanly but this playthrough gives
  no doc-window or special-check cross-validation.

## Pipeline compatibility changes made for this run (documented, minimal)

1. `parse_grading_specs.py::_window_part` now only emits a window `key` when
   the backticked token is a real eventKey — U4P1's new eventType-based end
   anchor otherwise mis-parsed the word `Finished` as a phantom anchor and
   would have false-flagged the point PARTIALLY_AUDITABLE.
2. `run_grading_validation.py`: added U4P1/U4P2 overrides and updated the
   U4P6 override to transcribe the 2026-09-01 markdown (with the Unit-4
   prefix filter applied in Python — the harness has no `$regex`); added
   `window_fn` support so override-defined windows are reported correctly;
   added an evidence-based special check for U4P1 and a positive-path branch
   to the U4P2 special check.
3. `mhs-unit4-point6-grading.md` Event Keys cells trimmed to bare keys
   (inline annotations corrupted exact-string key extraction in Phase 1).

## What should be addressed next

1. **Re-sync the 9 stale `tests/` modules** with the current markdown and
   retire the corresponding audit OVERRIDES.
2. **Targeted playthrough** exercising the yellow paths: wrong first choice at
   88:5 + slow soil-key solve (U4P1), failed glyph matches (U4P2 negatives),
   ≥1 wrong garden box + a re-inspected plant (U4P6 fallback overcount
   check).
3. **Dev-team confirmations**: live-DB `user_id` status; whether `data.Unit`
   on Soil Key Puzzle status records will keep the "Unit N" prefix across
   scene renames.
4. **Spec cleanup** (low priority): remaining 9 prose-vs-script window blocks,
   dead key 70:33 in U1P3 prose, refreshed dialogue DB export.
