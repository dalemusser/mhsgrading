# Grading documentation: issues found and changes made (2026-09-21)

*Dale Musser's team, while bringing the Go grader (`mhsgrader`) up to the
September 2026 grading logic in this repository. Every change below is a
documentation correction with one defensible answer, taken from the
repository's own scripts and validation fixtures; nothing here changes what a
Production Script or a Corresponding Script computes. Items that need a
judgment call from the grading team are in
[grading-team-questions-2026-09.md](grading-team-questions-2026-09.md).*

Verification after the edits: `rubric-validation/run_all.py` and
`reason-code-validation/run_all.py` pass 26/26 on all five fixtures, and the
Go grader's replay harness (which reads these documents for the reason-code
templates) matches the same fixtures 26/26.

## 1. "Attempt Window (Production)" blocks now describe the Production Script

The block in each point document is meant to state the window the Production
Script grades. In sixteen documents it did not: it named the header's
Trigger(Start) event as the window start, while the script anchors on the
previous occurrence of the *end* trigger, or on the *latest* start event
rather than the "previous" one. The 09-14-26-3 grading-readiness audit had
already flagged this ("documented window ≠ implemented window").

| Document | Block said | Script does (block now says) |
|---|---|---|
| mhs-unit1-point3 | start `DialogueNodeEvent:30:98` | previous `questActiveEvent:34` → latest `questActiveEvent:34` |
| mhs-unit2-point1 | previous `DialogueNodeEvent:18:1` | previous `questFinishEvent:21` |
| mhs-unit2-point4 | start `DialogueNodeEvent:22:18` | previous `DialogueNodeEvent:23:17` → latest `23:17` |
| mhs-unit3-point1 | previous `DialogueNodeEvent:10:1` | previous `DialogueNodeEvent:11:22` |
| mhs-unit3-point2 | previous `questFinishEvent:17` | previous `DialogueNodeEvent:11:34` |
| mhs-unit3-point3 | previous `DialogueNodeEvent:11:34` | previous `questFinishEvent:18` |
| mhs-unit3-point5 | previous `DialogueNodeEvent:73:200` | previous `DialogueNodeEvent:10:194` |
| mhs-unit4-point3 | previous `questActiveEvent:48` | previous `questActiveEvent:50` |
| mhs-unit4-point5 | previous `questActiveEvent:36` | previous `questActiveEvent:41` |
| mhs-unit3-point4 | *previous* `questActiveEvent:18` | *latest* `questActiveEvent:18` (window valid only if the end follows it) |
| mhs-unit4-point1 | *previous* `DialogueNodeEvent:88:0` | *latest* `DialogueNodeEvent:88:0` (same guard) |
| mhs-unit4-point4 | *previous* `questActiveEvent:50` | *latest* `questActiveEvent:50` (same guard) |
| mhs-unit4-point6 | *previous* `questActiveEvent:41` | *latest* `questActiveEvent:41` (same guard) |
| mhs-unit5-point1 | *previous* `questActiveEvent:43` | *latest* `questActiveEvent:43` (same guard) |
| mhs-unit5-point2 | *previous* `questFinishEvent:43` | *latest* `questFinishEvent:43` (same guard) |
| mhs-unit5-point4 | *previous* `questFinishEvent:44` | latest `questFinishEvent:44` before the end event |

Each rewritten block carries one added sentence: the Production Script bounds
the window this way, and the header's Trigger(Start) event marks when the
activity begins (it drives the dashboard's in-progress state and the duration
metrics). Whether the *intended* window for a replayed activity is the script's
or the header's remains a question for the grading team (questions document,
item A1); the blocks now at least agree with the scripts they claim to describe.

## 2. Header start events

- **mhs-unit3-point2**: Trigger(Start) `questFinishEvent:17` → `questActiveEvent:17`.
  Quest 17 *finishes* after the point's end trigger (`DialogueNodeEvent:11:34`),
  so the old start could never precede the activity; in the live grader it
  opened a phantom second attempt for every student. Quest 17's *activation*
  precedes the sensor search, matching the Progress-Points source document.
  The grader uses this start (questions document, item A2, for confirmation).
- **mhs-unit2-point3**: Trigger(Start) `DialogueNodeEvent:20:26` →
  `DialogueNodeEvent:20:33`, the START_KEY the Production Script, the Python
  transcriptions and the grader all use.

## 3. Tables and comments

- **mhs-unit2-point4**: the four "Bad Feedback" rows of the Event Keys table
  had been pasted inside the Analytics Script code fence (after
  `const playerId`), so the rendered table showed only Trigger and Success.
  Moved back into the table; the script is unchanged.
- **mhs-unit5-point1**: the Grading Rule table said "score ≥ 1 / score < 1"
  although no score is computed; it now states the actual rule (success node
  `100:44` present and none of `100:38`, `100:39`, `100:43`). The Production
  Script's header comment said `questActiveEvent:39`; it now says
  `questFinishEvent:43`, the trigger the script uses.
- **mhs-unit5-point4**: the Event Keys table listed `questFinishEvent:44` (the
  start) as the Trigger; corrected to `questFinishEvent:45`.
- **Reason-codes-and-instructor-messages.md**: section A used `U5.C1`–`U5.C4`
  for the Unit 5 rows; now `U5P1`–`U5P4` like the rest. Section B still listed
  the March vocabulary (`TOO_MANY_NEGATIVES`, `BAD_FEEDBACK`,
  `WRONG_CHOISE_SELECTED`, …) with the old messages; it is now generated from
  the per-point documents (code, Instructor Message, Teacher Guidance) and says
  so. The per-point documents remain authoritative.
- **Instructor Messages** (14 of 28): em-dashes replaced with commas, colons,
  parentheses or a sentence break (2026-09-20; placeholders unchanged).
- Heading typo "Correspoinding Script" → "Corresponding Script" in eleven
  documents (no script or tool matched the misspelling).
- **reason-code-validation/rc_u5p3.py**: docstring said the 108:63–69 nodes are
  not counted; the code and the document count them since 2026-09-17.
- **docs/issues_and_updates.md**: a 2026-09-21 addendum notes which March items
  the September scripts supersede.
- **ai/context.md**: folder structure and cross-repo notes brought up to the
  current layout (`grading-logic/`, the four validation pipelines, `mhsgrader`
  as its own repository).

## 4. Not changed (needs the grading team)

Everything in [grading-team-questions-2026-09.md](grading-team-questions-2026-09.md):
the items the documents themselves mark "for review" (U3P3 counting `84:36`,
U3P5 2.5 vs 3, U4P4 `107:4` and the machine-1 condition, U5P2 `DualChamber_*`,
U4P6 `92:36`), the client-timestamp fence in U2P2/U2P3, the yellow states
without a reason code, and the logging defects for the game team.
