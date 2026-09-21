# Questions and findings for the grading team — September 2026 grader update

*From Dale Musser's team, 2026-09-20 (updated 2026-09-21). Context: the Go grader (`mhsgrader`) was
brought up to the September 2026 grading specification in `mhsgrading/` and
verified against the five playthrough fixtures in `rubric-validation/` and
`reason-code-validation/` (all 26 points, colours + reason codes + message
variables). While doing that we implemented every "Production Script" and
"Corresponding Script" exactly as written, and we made a few judgment calls
where the documents disagree with themselves. This document lists (A) the
decisions we made that you may want to confirm or overrule, (B) items the
documents themselves mark "for review", and (C) internal inconsistencies in the
markdown that will trip up the next implementer. Nothing here blocks the
dashboard; changes you request will be applied in a follow-up release.*

## A. Decisions we made — please confirm or correct

1. **Grading window = the production script's window, not the "Attempt Window
   (Production)" prose block.** In nine files the block names a start anchor
   (e.g. U2P1 "previous `DialogueNodeEvent:18:1`") that the script never
   queries; the script bounds the window with the previous occurrence of its
   own END trigger. We implemented the scripts. Affected: U1P3, U2P1, U2P4,
   U3P1, U3P2, U3P3, U3P5, U4P3, U4P5. The two agree on a first playthrough and
   differ only on replays.

2. **U3P2 start event.** The doc's Trigger(Start) is `questFinishEvent:17`, which
   fires *after* the end trigger `DialogueNodeEvent:11:34` (quest 17 finishes when
   the argument in U3P3 succeeds). Using it opened a phantom second attempt for
   every student. We use **`questActiveEvent:17`** (the quest's activation,
   which the Progress-Points document names) as the start of U3P2. Please
   confirm, and update the doc header.

3. **U3P4 start event.** The Go grader used `questFinishEvent:18`, which fires
   after the glyph puzzle, so every student was flagged regardless of
   performance. We now use the doc's **`questActiveEvent:18`**.

4. **U4P1 end / U4P2 start.** Implemented as the doc specifies: the Unit-4
   `Soil Key Puzzle` event with `Soil Key Puzzle Status = Finished` and `Unit`
   starting with "Unit 4" (an eventType + data match; these events carry no
   eventKey). The old Go trigger `questActiveEvent:39` fires before the answer
   and the puzzle, so it could never award the duration points.

5. **U3P5 threshold.** Green at `sum_score ≥ 2.5` (production script and
   instructor message) rather than `≥ 3` (rule table and analytics script).
   With four seeds this is the difference between allowing one wrong planting
   or none. Please settle which is intended.

6. **U4P4 machine-1 condition.** Implemented `top = 1 AND bottom = 1` (analytics
   script, production script, reason script and message) rather than the
   Grading Rule prose "top one time and bottom zero time". `issues_and_updates.md`
   item 4 (March) recorded the opposite fix; the scripts never changed. Please
   confirm `1 AND 1`.

7. **U2P2 / U2P3 client-timestamp fence.** Implemented as the colour scripts
   specify (counts restricted to client `timestamp` between the anchors, on top
   of the `_id` window). Note the U2P3 *reason* script drops that fence, so the
   pop-up numbers could in principle differ from the colour after out-of-order
   log uploads. Is the fence intended, or a leftover of the older
   timestamp-based analytics scripts?

8. **Re-fired end triggers.** For points whose window is "previous END → END",
   an END event that fires again with no new start event in between (a scene
   reload re-activating a quest, for example) would produce an empty window and
   a spurious yellow. The grader ignores such re-fires. No fixture contains one;
   the guard is a precaution. `questActiveEvent:36` (U4P4) and
   `questFinishEvent:45` (U5P4) do fire twice in every playthrough, but those
   points use latest-start/latest-end windows, which are unaffected.

9. **Yellow with no reason code.** The scripts leave some yellow states without a
   code: U2P1 / U2P4 / U4P2 when the success node is absent and no assist fired;
   U2P6 when neither wrong-option node fired; U5P1 when only `100:44` is
   missing; every point whose window is missing. The dashboard shows "The game
   did not record enough detail to say why this task was flagged" for those.
   If you would rather define codes for them, tell us.

10. **When no start event exists** for a start-anchored point, the scripts yield
    yellow (no window). The grader instead grades from the beginning of the
    student's log and notes `window: no start event found` in the grade. We
    think a graded estimate serves teachers better than an automatic yellow;
    say if you disagree.

## B. Items the documents themselves mark "for review" — implemented as scripted

- **U3P3:** the success node `84:36` is counted in the colour sum (so the count
  equals the number of attempts). `84:38` is listed but never logs.
- **U3P5:** 2.5 vs 3 (see A5).
- **U4P4:** `107:4` ("middle" layer) is in the success list; moving it to the
  negatives would change middle-then-fourth from +2 to +1.
- **U5P2:** `DualChamber_Condenser` / `DualChamber_Evaporator` interactions on
  floor 3 are not counted ("add to both scripts once approved").
- **U4P6:** the review can also start at `92:36` (second-round "see the
  results"); the dialogue fallback only anchors on `92:33` today.

## C. Documentation corrections already made

The internal inconsistencies we found in the markdown (window blocks that did not
match their scripts, a table pasted inside a code fence, stale header events and
comments, the March-vocabulary index table) have been corrected in this repository;
see [grading-doc-changes-2026-09-21.md](grading-doc-changes-2026-09-21.md) for the
list. Nothing in those edits changes what a script computes.

## D. Data questions we could not answer from the repositories

- Whether `DialogueNodeEvent:96:1` (U5P2 end / U5P3 start) can fire more than
  once in a playthrough.
- Whether `10:30` (correct river) can fire in the ungraded bonus-crate segment
  after U3P1's end.
- The U3P4 accepted-assist execution node (the doc says unconfirmed; the gate
  check covers it).
- Eight code paths no fixture reaches (EXCESS_ATTEMPTS at U2P1 / U2P4 / U3P4 /
  U4P2 / U5P1, and the U2P3 / U2P6 salinity / both-options branches) — a
  deliberately imperfect playthrough that hits them would let us verify the
  grader end to end.

## E. Findings from the rule-by-rule implementation (2026-09-20)

- **U3P4 `SOLVED_WITH_ASSIST` vs colour.** The code's trigger is `assisted OR no gate`,
  not a mirror of the colour rule. If DANI's assist node `78:23` could appear with two
  or fewer colour keys, the cell would be green while the code says triggered. Per the
  node map the assist is only offered after the 4th attempt, so we treat it as
  unreachable; the grader evaluates reason codes only on yellow cells.
- **Latest-start / latest-end scripts (U2P6, U3P4, U4P1, U4P4, U4P6, U5P1–U5P3).** The
  scripts return "no window → yellow, no code" when a *later* start event follows the
  latest end event (a student re-entering the activity after finishing). The grader
  grades at the moment the end event arrives and keeps that grade; a re-entered start
  shows on the dashboard as "started again" over the finished grade. Same result on
  every fixture; different only in that replay situation.
- **Not-reached points.** The colour scripts return "yellow" for a point the student
  never reached (fixture 09-03-26-4, Unit 5 truncated), and the reason scripts return no
  code for it. The grader records nothing for such a point and the dashboard shows it
  as not started (white/pencil), which we believe is what teachers should see. The
  Python colour manifest labels these "not-played artifacts"; consider giving them a
  distinct expected value.
- **Metric meanings that changed** (analytics tab, not the colour): U5P1 `mistakeCount`
  now counts incorrect arrangements over the seven feedback nodes 100:33–100:39 (the
  number the message quotes) rather than the three colour negatives; U4P4
  `mistakeCount` is the wrong-depth count over 107:2/3/4/6; U4P1's puzzle duration is
  absent (not 0) when it could not be measured; U4P6 stores `boxScore`,
  `dialogueScore` and their maximum as `score`.
- **Duplicate end events.** `questFinishEvent:45` (U5P4) logs twice back to back and
  `questActiveEvent:36` (U4P4) re-fires on the scene change to Anderson Base, so those
  points record two identical attempts per playthrough. Harmless, but if the game
  team can de-duplicate those events the attempt counts become meaningful.
- **U2P3 colour window vs reason window.** The colour script fences by client
  `timestamp` and `_id` and goes yellow when either anchor lacks a timestamp; the
  reason script uses `_id` only. Implemented both as written (the pop-up's
  `triggering_number` is the unfenced count). They agree unless events were uploaded
  out of order.
- **U2P2 / U2P3 runs whose anchors carry no client timestamp** are yellow with no code
  under the scripts (implemented literally). Confirm that is intended rather than
  falling back to the `_id` window.
- **U2P1 assisted path also fires the success node.** In fixture 09-03-26-4 both
  `68:29` (solved on own) and the forced assist `68:28` fire in one window; the scripts
  (and the grader) let the assist win. The game team should confirm whether `68:29`
  is meant to fire on the assisted path.

## F. For the game/dev team: log records with a string `data` payload

Two `DialogueEvent` records from build `20260819-12226` (eventKey
`DialogueNodeEvent:10:1`, 2026-08-24, on the dev sentinel account) carry
`data: "System.Collections.Generic.Dictionary`2[System.String,System.Object]"` —
the dictionary's `ToString()` instead of its contents. 1,188 `PlayerPositionEvent`
records from build `20260323-` (2026-08-25) also have string payloads. The grader
now tolerates these (a JSON string is parsed, anything else is kept as `_raw`),
but any grading key inside such a payload is lost for that record. Worth a check
in the logger's serialization path.

