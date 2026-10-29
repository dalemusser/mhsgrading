# QA 1693 — Unit 2 Classifier Progression Issue

## Source tracker record

- **Email date:** 2026-09-23
- **Collection:** `MHS-Release_V1.0.0`
- **Reporting organization:** Maryville
- **Students field, verbatim:** `Lawyer2/Reed Henggeler, Isabella Ruminer`
- **Unit / Activity:** `U2/Classifier`
- **Affected field, verbatim:** `Players who stop after U2 Classifier, but before finishing U2`
- **Status:** Tested
- **Hansoft ID:** QA 1693
- **Notes:** Source workbook cell evaluated as `#VALUE!`; no reliable note content is available from the uploaded workbook.

## Reported issue

The tracker identifies players who reach or complete the Unit 2 Classifier portion of gameplay but do not subsequently finish Unit 2.

This establishes a **reported progression boundary**, but it does not establish that the Classifier itself is the root cause.

## What is known

- The affected case is associated with Unit 2 and the Classifier activity.
- The students fail to progress to normal completion of Unit 2 after the Classifier boundary described in the tracker.
- The issue was already marked `Tested` in the tracker.

## What is not known

The tracker alone does not establish:

- the exact timestamp when progression first became abnormal;
- whether the Classifier activity itself completed correctly;
- whether an expected quest/progress transition fired;
- whether a later interaction actually triggered the stuck state;
- whether save/load behavior contributed;
- whether a UI state and underlying quest state became inconsistent;
- whether the same suspicious event pattern occurs in successful players.

## Primary log-analysis objective

Reconstruct the affected students' event sequence from the final clearly normal Unit 2 state through the point at which normal progression stops, then compare this sequence against successful students who pass the Classifier and finish Unit 2.

## Questions to answer from the logs

1. What is the last event/state that appears normal before the affected sequence diverges from successful playthroughs?
2. Is there clear evidence that the Classifier was completed?
3. What events normally occur immediately after successful Classifier completion?
4. Are any of those expected events missing in the affected playthroughs?
5. Are any events duplicated or emitted in an unexpected order?
6. Do affected students perform an unusual interaction between Classifier completion and the expected next quest step?
7. Is there evidence of a save, reload, scene transition, DANI/tool interaction, NPC interaction, or other state-changing action in the failure window?
8. Does the same suspected pattern appear in successful controls?

## Suggested comparison controls

Prefer students who:

- used `MHS-Release_V1.0.0`;
- played Unit 2 in the same classroom deployment when possible;
- completed the Classifier successfully; and
- subsequently completed or clearly progressed beyond the relevant Unit 2 quest transition.

## Evidence to extract

For the suspected failure window, report:

- timestamps;
- `sceneName`;
- `eventType`;
- relevant `data` fields;
- quest/progress-point changes;
- Classifier-related completion/submission events;
- scene transitions;
- save/reload events;
- relevant NPC/object interactions;
- the immediately preceding and following meaningful events.

## Hypotheses to evaluate, not assume

Examples of testable possibilities include:

- an expected post-Classifier quest transition did not occur;
- the activity completed visually but a required underlying state was not recorded;
- an interaction/order/timing condition prevented the next trigger from firing;
- the actual divergence occurred before the Classifier and only became visible afterward.

These are hypotheses only. Rank them using affected-versus-successful log evidence.

## Desired developer-facing result

The most useful outcome is a minimal sequence such as:

`last normal quest state -> Classifier interaction/completion -> distinguishing event/state -> expected transition absent or abnormal -> player no longer progresses`

If no reliable distinction from successful playthroughs can be found, state that explicitly and identify what additional telemetry would be needed.
