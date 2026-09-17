# Run comparison — 09-14-26-3 vs 09-03-26-3

Hand-written companion to `audit-summary.md` (audit run 2026-09-16). The
previous full-coverage run with imperfect play is `reports/09-03-26-3`
(build 20260902-12353, audited 2026-09-06), so that is the comparison base.

## The two playthroughs

| | 09-03-26-3 | 09-14-26-3 |
|---|---|---|
| Build `version` | `20260902-12353` (plus a Unit-1 stub on `20260721-11840`) | `20260914-` on every record — build number missing after the dash |
| Player (`user_id`) | `6a9a0779e2ada9cb13ea75c0` | `6aa8589346b3c45b562092f8` |
| Coverage | Units 1–5 complete, one sitting | Units 1–5 complete, two sittings (~13 h break mid-Unit 2); Unit 1 started twice (first attempt abandoned after 6 min) |
| Records / event types | — / 23 | 12,318 / 23 (57 dialogue conversations, 34 quests) |
| Debug menu | opened briefly (Unit 3, Unit 5 dungeon) | never opened — the 13 `DEBUGMenu` records are `isOpened=false` scene-load emissions (new build behaviour) |
| `crash` records | present (WASM out-of-bounds) | none |
| eventKey ↔ payload mismatches | 38, touching U4P1 grading keys | 53, touching **no** grading key |
| Exact-duplicate groups | — | 92; one duplicates `questFinishEvent:45` (U5P4 end anchor; see below) |

## Headline result: identical pipeline outcome, 3 more yellows

| Metric | 09-03-26-3 | 09-14-26-3 |
|---|---|---|
| Stage 1 READY_FOR_GRADING_TEST | 26 / 26 | 26 / 26 |
| Stage 2 PASS / MISMATCH / no-independent-check | 18 / 0 / 8 | 18 / 0 / 8 |
| Validator failures / warnings | 0 / 14 | 0 / 14 |
| Green / yellow | 6 / 20 | 3 / 23 |

Every point that had an independent expectation (18 doc-window or
completion checks) matched the production color. Nothing flipped
yellow→green; three points flipped green→yellow, all explained by the
tester's play, not by logging or grading changes:

| PP | 09-03-26-3 | 09-14-26-3 | Check | Why it changed |
|---|---|---|---|---|
| U2P1 Escape the Ruin | green | yellow | PASS (doc window agrees) | success node `68:29` absent; 5 wrong map-terrain matches (green needs ≤ 4) |
| U2P3 Getting the Band Back Together II | green | yellow | PASS (doc window agrees) | 14 wrong-direction reminders (green needs < 6 — the 2026-09-06 tightened rule) |
| U3P4 Forsaken Facility | green | yellow | no independent check | gate `78:24` present but 5 target-feedback nodes in window → score 0 (09-03: 1 node → score 1) |

This is the first run in which U2P1, U2P3 and U3P4 exercise their yellow
branch, and U3P4's yellow is the first observed for a point that has never
had an independent check.

## All 26 colors with the Stage-2 diagnostic

| PP | 09-03 | 09-14 | Stage 2 | 09-14-26-3 diagnostic (from the 1:1 transcription) |
|---|---|---|---|---|
| U1P1 | green | green | PASS | completion-only |
| U1P2 | green | green | PASS | completion-only |
| U1P3 | yellow | yellow | PASS | yellow node hit 1× → attempt 2 |
| U1P4 | green | green | PASS | completion-only |
| U2P1 | green | **yellow** | PASS | no `68:29`; 5 wrong matches (> 4) |
| U2P2 | yellow | yellow | no check | 4 wrong-direction prompts (threshold ≤ 1) |
| U2P3 | green | **yellow** | PASS | 14 nav reminders (green < 6) |
| U2P4 | yellow | yellow | PASS | no `74:21`; 6 attempts (> 5) |
| U2P5 | yellow | yellow | PASS | 8 wrong; score 3.33 (< 4) |
| U2P6 | yellow | yellow | no check | pass node `20:43` absent; first choice "waterfall height" |
| U2P7 | yellow | yellow | PASS | 8 negative selections (> 3) |
| U3P1 | yellow | yellow | PASS | wrong river 3× (≥ 2) |
| U3P2 | yellow | yellow | PASS | score 1; 13 sensor reminders (> 6) |
| U3P3 | yellow | yellow | PASS | 7 wrong reasoning picks; total 1 |
| U3P4 | green | **yellow** | no check | gate ok; 5 target nodes → score 0 |
| U3P5 | yellow | yellow | PASS | 4 wrong plantings; score −2 |
| U4P1 | yellow | yellow | PASS | `88:5` absent; soil key 168 s (> 30 s) |
| U4P2 | yellow | yellow | PASS | negative-feedback node present |
| U4P3 | yellow | yellow | PASS | floor-3 10 / floor-4 15 machine interactions |
| U4P4 | yellow | yellow | no check | score 0; 18 interactions; 3 negatives (09-03: 16 / 6) |
| U4P5 | yellow | yellow | PASS | success + 10 negatives (09-03: 14) |
| U4P6 | yellow | yellow | PASS | 0/3 boxes correct (Clay/Gravel/Sand vs Gravel/Sand/Clay) |
| U5P1 | yellow | yellow | no check | 1 negative node (zero-negatives rule) |
| U5P2 | yellow | yellow | no check | floor-3 8 (> 6) / floor-4 10 (> 5); score 1 |
| U5P3 | yellow | yellow | no check | 4 wrong arguments (≥ 4) |
| U5P4 | yellow | yellow | no check | success node `106:35` absent |

## Executor currency (checked before trusting Stage 2)

Commit `f4fcfc6` (2026-09-11, reason-code rewrite) rewrote 23 grading
markdowns after the executors were last synced in `4069a9e`. Verified:

- All 26 **Production Script** code fences are byte-identical between
  `4069a9e` and HEAD (whitespace-normalised compare). The rewrite touched
  only reason-code / prose sections, so `rubric-validation/test_uXpY.py`
  is still a faithful transcription — no re-sync needed.
- `progress-point-dependencies.json` differs from the 09-03-26-3 run only in
  the `reason_codes` label lists (e.g. `BAD_FEEDBACK` → `EXCESS_NAV_REMINDERS`,
  `MISSING_SUCCESS_NODE`/`TOO_MANY_NEGATIVES` → `SOLVED_WITH_ASSIST`/`EXCESS_ATTEMPTS`)
  and in U2P5, where the argument-part rubric table is now parsed as extra
  `kind: other` counted-evidence rows (parse artifact, ignored by grading).
  `trigger_start`, `trigger_end`, `attempt_window` and `production` are
  unchanged for all 26 points.
- Parser caveat: the parsed `reason_codes` list is now **empty** for U4P1,
  U4P3, U4P4 and U5P2 (their renamed codes are not recognised by
  `parse_grading_specs.py`). The audit does not use that field for colors;
  the `reason-code-validation/` suite is the authority for reason codes.

## Windowing checks on the re-fired anchors

`validate_outputs.py` warned that five anchors fired twice. None affected a color:

| Anchor | Firings | Cause | Effect |
|---|---|---|---|
| `questActiveEvent:28` | 00:23:06Z, 00:45:50Z | Unit 1 restart | U1P1 is completion-only |
| `questActiveEvent:18` | 16:56:56Z (Unit 3 Dev), 16:59:08Z (Unit 3 Dungeon Dev) | re-emitted on scene change | U3P4 window starts at the later one; 0 target/gate records lie between the two |
| `questActiveEvent:36` | 17:53:05Z (Unit 4 Dev), 17:59:14Z (Anderson Base) | re-emitted on scene change | U4P4 window extends 6 min; the gap holds only conversation-82 dialogue, none of U4P4's conv-107 keys and no floor-5 `soilMachine` records; U4P5 doc window still agrees |
| `questFinishEvent:45` | 18:59:25.517Z ×2 | exact duplicate upload (only `_id` and a 49 ms `serverTimestamp` differ) | U5P4 window ends on the later `_id`; harmless (flagged LOGGING_DUPLICATE_EVENT) |

## Minor drift found while checking

- `rubric-validation/test_u3p4.py` `diagnose()` emits `TOO_MANY_NEGATIVES`
  only when `total_count > 3`, but the color turns yellow at `total_count >= 3`
  (the markdown's reason-code script uses `colorCount >= 3`). A count of
  exactly 3 would yield a yellow with no diagnostic. No color impact (this
  run: 5); the transcription's `grade()` is correct.
- The transcription `diagnose()` labels still use the pre-September names
  (`BAD_FEEDBACK`, `WRONG_ARG_SELECTED`, …). They are informal trace labels,
  not the production reason codes.

## Standing items (unchanged since 09-03-26-3)

- `playerId` vs `user_id` — Stage 2 still translates; live-DB status unconfirmed.
- Dead key `DialogueNodeEvent:70:33` (U1P3).
- 8 doc-vs-production anchor divergences (U1P4, U2P5, U2P6, U2P7, U3P1, U3P2, U3P3, U5P1) and 9 markdown-internal window divergences (same list as before).
- Dialogue export still 2026-06-10.

## Follow-ups

1. **Fixture**: this run is a good `rubric-validation/config/fixtures.yaml`
   candidate (3 green / 23 yellow, provenance = this audit) — it is the
   first fixture that would cover the U2P1, U2P3 and U3P4 yellow branches.
2. **Dev report**: `version` is literally `20260914-` (build number missing).
3. **Rubric-validation**: align `test_u3p4.py` `diagnose()` threshold to `>= 3`.
4. **Playtesting**: the 8 no-independent-check points are unchanged
   (U2P2, U2P6, U3P4, U4P4, U5P1–U5P4); their yellows here are all
   behaviourally explained by the diagnostics above, but a clean green
   replay of U3P4/U4P4/U5P1–U5P4 on this build is still the missing case.

## Re-run 2026-09-17 (after the U5P3 key-list extension)

The tester noticed that the U5P3 pop-up reported only claim feedback although
reasoning and evidence feedback had been received. Review of conversation 108
against the Unity dialogue export showed six wrong-answer feedback nodes
missing from the 33-key list — the generic/specific pairs on the "one correct
piece of evidence" branch (`108:63/64` reasoning 3, `108:65/66` reasoning 4)
and the "two pieces of evidence other than C+D" branch (`108:68/69`). All six
were added to the color scripts and the reason-code script, and the two
transcriptions were re-synced. Re-running this audit into the same folders:

- Pipeline outcome unchanged: 26/26 READY, 18 PASS / 0 MISMATCH / 8 no-check,
  0 failures / 14 warnings, colors unchanged (3 green / 23 yellow).
- U5P3 now audits 39 target keys; `108:64` and `108:65` are SUPPORTED_EXACTLY
  (x1 each), the Stage-2 count is 6 (was 4), still yellow; dialogue
  reconciliation 4/40 exact (was 2/34).
- No other point changed. The reason-code expectation for this run moved to
  6 flagged (4 claim, 1 reasoning, 1 evidence); no other fixture log fires any
  of the six nodes.
