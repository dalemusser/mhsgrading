# QA 1694 — Unit 3 Supply Run / Crate 1 Issue

## Source tracker record

- **Email date:** 2026-09-29
- **Collection:** `MHS-Release_V1.0.0`
- **Reporting organization:** Maryville
- **Students field, verbatim:** `Lawyer2/Reed Henggeler, Isabella Ruminer Lawyer5/Corah Thompson, Molli Kelme`
- **Unit / Activity:** `U3/Supply Run/Crate 1`
- **Affected field, verbatim:** `Players that were skipped ahead from Unit 2 after experiencing the above classifier or argumentation bug`
- **Status:** Identified
- **Hansoft ID:** QA 1694
- **Notes:** Source workbook cell evaluated as `#VALUE!`; no reliable note content is available from the uploaded workbook.

## Reported issue and critical context

This issue concerns Unit 3 Supply Run / Crate 1 and specifically identifies players who were skipped ahead from Unit 2 after encountering the previously reported Unit 2 Classifier or Argumentation progression problems.

That history is potentially important, but it must be treated as **context rather than a confirmed cause**.

The analysis should explicitly compare two explanations:

- **Independent-U3 hypothesis:** the Supply Run / Crate 1 problem is a Unit 3 defect that can occur regardless of earlier Unit 2 state.
- **Carryover-state hypothesis:** skipping affected players forward from Unit 2 may have left required persistent state incomplete or inconsistent, contributing to the Unit 3 problem.

## What is known

- The issue is associated with Unit 3 Supply Run / Crate 1.
- The tracker specifically selects players who had previously encountered the Unit 2 Classifier or Argumentation problem.
- Those players were skipped ahead from Unit 2.
- The issue status was `Identified` at the time of the tracker entry.

## What is not known

The tracker does not establish:

- exactly how the students were skipped ahead;
- which quest flags, inventory/evidence state, NPC state, progress-point state, or other persistent values were present after the skip;
- whether all affected students fail at the same precise Crate 1 step;
- whether normally progressing students can encounter the same Unit 3 issue;
- whether the observed problem originates in Unit 3 or earlier.

## Primary log-analysis objective

Determine whether the affected players enter and progress through Unit 3 differently from comparable students who reached Unit 3 through normal progression, with special attention to initialization and prerequisite state.

## Questions to answer from the logs

### A. Unit 3 entry state

1. What is the first Unit 3 event for each affected student?
2. What initialization, quest-start, NPC, inventory/evidence, save/progress, or scene-entry events normally occur for successful students entering Unit 3?
3. Are any expected initialization events or state values missing from affected cases?
4. Are there unusual events that appear only because the student was skipped ahead?

### B. Supply Run / Crate 1 sequence

1. What exact action/state precedes the point where normal Crate 1 progression stops?
2. Which crate-related interactions are recorded?
3. Is an expected object interaction, delivery, dialogue, trigger, or quest transition absent?
4. Do affected students repeat interactions or revisit locations in a way that suggests the game did not recognize completion?
5. Does a successful student produce a different event/data-field sequence at the same milestone?

### C. Relationship to Unit 2

1. Do students affected by QA 1694 share a persistent-state pattern that distinguishes them from normally progressing Unit 3 students?
2. Can the potentially missing/different state be traced back to Unit 2 completion?
3. If comparable students who progressed normally through Unit 2 also show the same Unit 3 failure, does that weaken the carryover-state hypothesis?

## Suggested comparison groups

Use at least two comparison types if data are available:

1. **Normal Unit 3 controls:** students who completed Unit 2 normally and successfully passed Supply Run / Crate 1.
2. **Skipped/abnormal-progression controls:** any students who were skipped or reloaded around earlier units but did *not* encounter the Crate 1 issue.

The second group is especially valuable because it can help distinguish the effect of being skipped from the specific failure condition.

## Evidence to extract

Compare:

- final Unit 2 events/state when available;
- first Unit 3 session and scene-entry events;
- quest/objective initialization;
- save/progress-point information;
- inventory/evidence-related fields;
- NPC/dialogue state;
- crate/object interaction events;
- relevant object identifiers;
- repeated or missing interactions;
- expected post-delivery transitions;
- reload/resume behavior.

## Hypotheses to evaluate, not assume

Potential explanations worth testing include:

- a normally established Unit 2 state was absent after the skip;
- Unit 3 initialization assumes a prerequisite state that the affected students did not have;
- Crate 1 has an independent object/trigger problem unrelated to the Unit 2 history;
- the skip itself altered a progress/save state but only under certain prior conditions;
- the students' visible stuck point is downstream of an earlier state divergence.

## Desired developer-facing result

The ideal result should answer:

1. **What is the first concrete difference between affected and successful Unit 3 playthroughs?**
2. **Does that difference already exist when Unit 3 begins, or does it first appear during Crate 1?**
3. **What specific state/trigger/code path should QA or developers inspect next?**

Do not conclude that Unit 2 caused QA 1694 solely because the affected students had earlier Unit 2 problems.
