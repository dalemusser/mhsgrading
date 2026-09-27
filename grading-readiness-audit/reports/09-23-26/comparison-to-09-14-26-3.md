# Run comparison — 09-23-26 vs 09-14-26-3

Hand-written companion to `audit-summary.md` (audit run 2026-09-26). The
previous full-coverage run is `reports/09-14-26-3` (version string
`20260914-`, audited 2026-09-16), so that is the comparison base.

## The two playthroughs

| | 09-14-26-3 | 09-23-26 |
|---|---|---|
| Build `version` | `20260914-` on every record (build number missing) | `20260914-` on every record — **but the Unit 4 garden crops changed** (`collect broccoli / peas / potatoes` → `collect mega turnips / super orange / ultra corn`), so this is most likely a newer build behind the same truncated string |
| Player (`user_id`) | `6aa8589346b3c45b562092f8` | `6ab42757bf592cbac358b8c1` |
| Coverage | Units 1–5 complete, two sittings (~13 h break) | Units 1–5 complete in ONE sitting (2026-09-25 20:06Z–23:55Z, 3 h 49 m); Unit 2 resumed once from a checkpoint (quest 23 "Foraged Forging" replayed — outside every graded window) |
| Records / event types | 12,318 / 23 | 11,648 / 22 (no `DaniEvent`: the DANI panel was never opened) |
| Debug menu | never opened (13 scene-load `isOpened=false` emissions) | never opened (12 scene-load emissions) |
| `crash` records | none | none |
| eventKey ↔ payload mismatches | 53, no grading key | 17, no grading key (pattern below) |
| Play style | imperfect everywhere (23 yellow) | **every non-glyph activity first try; the five glyph puzzles deliberately failed** (5 yellow) |

## Headline result: 21 green / 5 yellow, every yellow on a glyph puzzle

| Metric | 09-14-26-3 (as run 2026-09-16) | 09-23-26 |
|---|---|---|
| Stage 1 READY_FOR_GRADING_TEST | 26 / 26 | 26 / 26 |
| Stage 2 PASS / MISMATCH / no-independent-check | 18 / 0 / 8 | **23 / 1 / 2** |
| Validator failures / warnings | 0 / 14 | 0 / 4 |
| Green / yellow | 3 / 23 | 21 / 5 |

The five yellows are exactly the glyph-puzzle paths the imperfect-playthrough
checklist was waiting for:

| PP | Color | Stage 2 | Conversation sequence (payload nodes, `_id` order) | Reason code |
|---|---|---|---|---|
| U2P1 Escape the Ruin | yellow | PASS (doc window agrees) | 68: 5, 7, 18, 20 (decline), 23 (offer), 25 (decline), 27 (5th-try offer), 33 (decline), **29 SolvedSolo** — 5 negatives, no assist key | EXCESS_ATTEMPTS, attempt 6 |
| U2P4 Investigate the Temple | yellow | PASS | 74: 4, 6, (11/23 lesson), 10, (13/24/27 video), 15, 16, **21 SolvedSolo** — 5 negatives, no forced 74:20 | EXCESS_ATTEMPTS, attempt 6 |
| U3P4 Forsaken Facility | yellow | PASS | 78: 4, 7, 9, 12, **23 forced** → 24 OnSolve — gate present, 5 target nodes → score 0 | SOLVED_WITH_ASSIST, attempt 5 |
| U4P2 Infiltration Glyph | yellow | PASS (special check) | 102: 3, 7, 10, 18 (offer), 19 (decline), **23 forced** → 88:11 20 s later | SOLVED_WITH_ASSIST, attempt 5 |
| U5P1 If I Had a Nickel 1–2 | yellow | PASS | 100: 34, 35, 36, 38, **44 OnPlayerSolve** — 4 negatives, no offer (39), no assist | EXCESS_ATTEMPTS, attempt 5 |

First observations on this build: the EXCESS_ATTEMPTS branch of U2P1, U2P4 and
U5P1 (previously transcription-verified only), the declined-offer nodes
68:20 / 68:25 / 68:33 ("Nah, I don't need to." / "No, I'm okay.") and
102:19, and the forced 5th-attempt assist of U3P4 and U4P2 on `20260914-`.

**Auto-solve still does not solve the puzzle.** After forced `78:23`
(22:06:56Z) the player made two more "Press E To Place Glyph" actions (Glyph
Dock B, Glyph Dock C) before `78:24` fired at 22:07:15Z — the same behaviour
as 09-14-26-3. After forced `102:23` (22:36:23Z) four Interact inputs preceded
`88:11` by 20 s (no placement ObjectInterEvents are logged in Unit 4 on this
build, so the evidence is weaker; the 09-14-26-3 accepted path solved in 4 s
with zero interacts). The "DANI ordered the pieces" wording caveat stands.

## All 26 colors with the Stage-2 diagnostic

| PP | 09-14 | 09-23 | Stage 2 | 09-23-26 evidence (raw windowed counts) |
|---|---|---|---|---|
| U1P1 | green | green | PASS | completion-only |
| U1P2 | green | green | PASS | completion-only |
| U1P3 | yellow | **green** | PASS | one submission, 70:7 success |
| U1P4 | green | green | PASS | completion-only |
| U2P1 | yellow | yellow | PASS | 5 negatives (> 4), 68:29 present |
| U2P2 | yellow | **green** | no check | 0 wrong-direction prompts (28:179/182/183) |
| U2P3 | yellow | **green** | PASS | 0 nav reminders (conv 28 silent) |
| U2P4 | yellow | yellow | PASS | 5 negatives (> 5 attempts), 74:21 present |
| U2P5 | yellow | **green** | PASS | 26:141 ×6, 26:138 ×0 → score 6 |
| U2P6 | yellow | **green** | MISMATCH (doc marker, see below) | correct choice 20:43 "Flow rate." |
| U2P7 | yellow | **green** | PASS | one submission, 27:7 success, 0 negatives |
| U3P1 | yellow | **green** | PASS | 10:30 ×3, 10:31/32 ×0 |
| U3P2 | yellow | **green** | PASS | 11:27 ×3 (penalty 1), 11:29/230 ×0 → score 4 |
| U3P3 | yellow | **green** | PASS | one submission 84:36 (+ Pollution Site Data panel opened) |
| U3P4 | yellow | yellow | PASS | gate 78:24; targets 4/7/9/12/23 → 5 → score 0 |
| U3P5 | yellow | **green** | PASS | 73:163 ×4, no 164/168/171 |
| U4P1 | yellow | **green** | PASS (special check) | 88:5 correct; soil key 22:33:48 → 22:34:03 = 15 s → 1.5 |
| U4P2 | yellow | yellow | PASS (special check) | negatives 3/7/10/18/23 present, 88:11 present |
| U4P3 | yellow | **green** | PASS | soilMachine floor 3 ×1, floor 4 ×1 |
| U4P4 | yellow | **green** | PASS | machine 1 top + bottom once each, machine 2 once; drill 107:5 first |
| U4P5 | yellow | **green** | PASS | one submission, 90:50 success |
| U4P6 | yellow | **green** | PASS (special check) | final boxes Gravel/Sand/Clay, 92:61 ×3 |
| U5P1 | yellow | yellow | PASS | negatives 34/35/36/38 (zero-negatives rule) |
| U5P2 | yellow | **green** | PASS | floor 3 = 9 (4 Condenser + 3 DualChamber_Condenser + 2 DualChamber_Evaporator) → +1; floor 4 = 4 → +2 |
| U5P3 | yellow | **green** | PASS | conversation 108 never entered a wrong-answer node |
| U5P4 | yellow | **green** | no check | 106:35 "12 - Tilted Out, Uncovered, Cold" (success) |

## The U2P6 MISMATCH is a doc-marker artifact, not a grading defect

The Progress-Points row for U2.C6 ends the activity at `DialogueNodeEvent:18:284`
(task 2.3) and grades 20:43 vs 20:44/45. In every log the choice node fires
about a minute AFTER 18:284 and immediately before the production end 20:46:

| Log | 23:42 (start) | 18:284 (doc end) | choice | 20:46 (production end) |
|---|---|---|---|---|
| 09-23-26 | 21:35:23Z | 21:39:44Z | 20:43 at 21:40:36Z | 21:40:38Z |
| 09-14-26-3 | 15:21:37Z | 15:28:34Z | 20:44 at 15:30:44Z | 15:31:41Z |
| 09-03-26-2 | 18:25:36Z | 18:28:11Z | 20:43 at 18:28:21Z | 18:28:22Z |

A doc-bounded window `(23:42, 18:284]` therefore never contains the choice
and always evaluates to "pass node absent → yellow". On 09-14-26-3 that
coincided with the real yellow; on any green run it disagrees. The production
window `(23:42, 20:46]` is the correct one (already recorded as a
doc-vs-production anchor divergence, cross-cutting finding 3). Expected color:
**green**.

## Two audit-tooling fixes made for this run (2026-09-26)

The first run of this audit reported only **7 PASS / 19 no-check**. Cause:
the 2026-09-24 realignment moved every `rubric-validation/test_uXpY.py` from
`TRIGGER_KEY` + `latest_trigger_window` to a module-level `_window(coll, pid)`
of the start-and-end form, and

1. `run_grading_validation.py` only cross-checked modules with a `TRIGGER_KEY`
   (it pinned the doc window by patching `latest_trigger_window`). It now also
   patches `_window`, so the doc-derived window is applied to every
   start-and-end module (U4P1/U4P2 keep their special checks; U2P2's
   timestamp-fenced window and U5P4's missing doc end marker remain
   no-check).
2. `parse_grading_specs.py::_window_part` required the boundary word
   immediately after the backticked key, so the realigned phrasing
   "Latest `KEY` before the end event (exclusive; zero ObjectId …)" yielded
   no start key in `progress-point-dependencies.json` (only end keys were
   parsed). The regex now tolerates prose between the key and the
   parenthesised boundary word.

Regression check: re-auditing `09-14-26-3` with the fixed scripts (into a
scratch folder, deleted afterwards) gave 24 PASS / 0 MISMATCH / 2 no-check —
six points that were "no check" on 2026-09-16 (U2P6, U3P4, U4P4, U5P1, U5P2,
U5P3) now carry an agreeing doc-window check; no verdict changed.

## Expected diffs vs the 09-14-26-3 outputs (from the 2026-09-21/24 doc work)

- `progress-point-dependencies.json`: `trigger_start` U2P3 `20:26 → 20:33`,
  U3P2 `questFinishEvent:17 → questActiveEvent:17`; the U2P4 (74:16/17/20/22)
  and U5P1 (`questActiveEvent:39`) "keys absent from Event Keys table"
  warnings are gone; every Attempt Window block now parses to
  latest-start / latest-end keys (`which: latest` on both parts).
- Validator warnings 14 → 4: the nine "Attempt Window block cites X but the
  production script never queries it" warnings are gone (the blocks were
  rewritten to match the scripts); the remaining four are re-fired anchors
  (below). `questActiveEvent:28` fired once this run (no Unit 1 restart).
- Doc-vs-production anchor list 8 → 7 (U2P5 dropped: its parsed start now
  equals the doc start 23:17).
- Dialogue reconciliation now runs against the 2026-09-21 export.

## Windowing checks on the re-fired anchors

| Anchor | Firings | Cause | Effect |
|---|---|---|---|
| `questActiveEvent:18` | 22:03:00Z (Unit 3 Dev), 22:05:35Z (Unit 3 Dungeon Dev) | re-emitted on scene change | U3P4 window starts at the later one; all conv-78 nodes follow it |
| `questActiveEvent:36` | 22:53:09Z (Unit 4 Dev), 22:58:02Z (Anderson Base) | re-emitted on scene change | U4P4 window extends 5 min (no conv-107 / floor-5 records in the gap); U4P5 starts at the later one, all conv-90 nodes follow |
| `questFinishEvent:45` | 23:49:49Z ×2 | exact duplicate upload | U5P4 window ends on the later `_id`; harmless (`questActiveEvent:45` is also duplicated at 23:44:04Z) |

## eventKey ↔ payload mismatches: a START-record pattern

14 of the 17 mismatched records are a conversation START record
(`eventKey = DialogueNodeEvent:<conv>:0`) whose payload already carries the
node that follows it a few milliseconds later; that next node then logs its
own, correctly keyed record (e.g. `74:0` with payload 74:15 at 21:18:03.725Z,
then `74:15` at 21:18:03.741Z). The other three carry the previous node's
key with the next node's payload (`20:111`→20:33, `73:211`→73:212,
`92:38`→92:64). Keyed grading is unaffected; payload-based analysis would
double-count the second node. Dev-reportable as before.

## Other observations relevant to the open questions

- `92:36` results route again (`92:33` never fired; 34 → 36 → 61 ×3): the
  whole-window feedback fallback counted all three — checklist item 11
  remains a functional no-op today.
- `11:30` (ocean sensor) did not fire (item 9 still open); `10:31` never
  fired after `11:22` this run.
- No Unit 4 `argumentationToolEvent` at all (item 12 / EA Q9 gap persists).
- `96:1` once, `107:4` never, `questFinishEvent:43` once (U5P1 window valid).
- `SolarStillDesignEvent` DesignSubmitted = Tilted Out / Uncovered / Cold,
  matching 106:35 (ungraded cross-check holds).

## Standing items (unchanged)

- `playerId` vs `user_id` — Stage 2 still translates; live-DB status unconfirmed.
- Dead key `DialogueNodeEvent:70:33` (U1P3).
- 7 doc-vs-production anchor divergences (U1P4, U2P3, U2P6, U2P7, U3P1,
  U3P3, U5P1) — U2P6's is now demonstrably the doc's problem (above).
- Version string `20260914-` still truncated — and now hiding a content change.

## Follow-ups

1. **Fixtures**: added the same day to both suites as `09-23-26`
   (rubric-validation 21 green / 5 yellow; reason-code 5 codes with
   attempt numbers 6 / 6 / 5 / 5 / 5); all six fixtures pass 26/26 in both.
   The Go grader's `TestFixtureReplay` set should gain this fixture too.
2. **Dev report**: crop-name change under an identical version string;
   START-record eventKey pattern; forced assist still not auto-solving
   (78:23, probably 102:23); duplicate `questActiveEvent:45` /
   `questFinishEvent:45`.
3. **Checklist**: mark the EXCESS_ATTEMPTS paths of U2P1/U2P4/U5P1 and the
   forced-assist paths of U3P4/U4P2 as observed; still unobserved:
   EXCESS_ATTEMPTS at U3P4/U4P2 (solve on attempt 4–5 after declining), the
   U2P3/U2P6 salinity and both-options branches, the 11:30 ocean sensor, a
   clean replay of U5P2 without the floor-3 dual chamber.
4. **Audit tooling**: U2P6's doc marker could be excluded from the doc-window
   check (it is structurally unable to agree on a green run); left as a
   surfaced divergence for now.
