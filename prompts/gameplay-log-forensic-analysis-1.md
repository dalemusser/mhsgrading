# MHS Classroom Gameplay Bug Forensic Investigation

You are working inside the `bug-finding-game-playthrough` project.

Your task is to perform a forensic analysis of gameplay logs collected from students who encountered progression-blocking bugs during a classroom field test of Mission HydroSci.

The primary goal is **not merely to summarize the logs**.

Your goal is to reconstruct what affected students did before the reported failure, identify unusual event sequences or game states, determine what evidence may explain why progression stopped, and generate concrete, testable hypotheses that can help QA and developers reproduce and fix the bugs.

---

# 1. Project Structure

The project contains the following important directories.

## Issue documentation

```text
issue-traker/
```

Start by reading:

```text
issue-traker/README.md
issue-traker/classroom-issue-tracker.md
```

Individual bug descriptions are located under:

```text
issue-traker/issues/
```

The current issue files include approximately:

```text
QA-1693-u2-classifier.md
QA-1694-u3-supply-run-crate1.md
QA-1697-u2-argumentation.md
U4-saving-cadet-anderson.md
```

Treat these files as the authoritative descriptions of:

- what was reported in the classroom;
- which students were associated with each problem;
- what contextual information is currently known;
- what is still uncertain;
- what questions the log analysis should investigate.

Do NOT convert hypotheses described in those files into established facts.

---

## Gameplay logs from affected students

Affected students' gameplay logs are stored under:

```text
players-logs-met-bugs/
```

The filenames generally contain:

1. the classroom field/site the student belongs to; and
2. the student's name.

However, filenames may contain spelling inconsistencies or typographical errors.

Therefore:

- do not require an exact filename match;
- compare names using reasonable fuzzy matching;
- also use the field/site identifier when matching students;
- inspect file contents when needed to confirm identity;
- do not silently assume that two similar names belong to the same student.

Before analyzing a bug, explicitly identify which log file or files you believe correspond to each affected student.

For each mapping, report:

```text
Issue
Student listed in issue tracker
Matched log filename
Match confidence: High / Medium / Low
Reason for match
```

If a mapping is ambiguous, flag it rather than guessing.

Do not rename, modify, or overwrite the source log files.

---

# 2. Initial Repository Inspection

Before performing any bug analysis:

1. Read:

```text
issue-traker/README.md
issue-traker/classroom-issue-tracker.md
```

2. Read every Markdown file under:

```text
issue-traker/issues/
```

3. List the files under:

```text
players-logs-met-bugs/
```

4. Build a mapping between affected students described in the issue files and their likely gameplay logs.

5. Report any:
   - missing student logs;
   - ambiguous filename matches;
   - duplicate candidate logs;
   - apparent naming typos;
   - students with multiple sessions/log files.

Do this before interpreting bug behavior.

---

# 3. Evidence Hierarchy

Throughout the investigation, keep three evidence categories separate.

## Observed

Directly visible in the logs.

Examples:

- an event occurred;
- an expected event is absent from the available sequence;
- a student entered a scene;
- an event was repeated;
- a reload occurred;
- a quest-related value changed.

## Inferred

Strongly suggested by the sequence but not explicitly logged.

Example:

> The quest may have failed to advance because the expected transition event is absent after successful puzzle completion.

## Speculative

Technically plausible but not sufficiently supported by the logs.

Example:

> A race condition may have occurred if the student interacted with the NPC before another state update completed.

Never present an inference or speculation as an observed fact.

---

# 4. Analyze One Bug at a Time

Analyze each issue separately before performing cross-issue comparisons.

For each issue:

1. Read its corresponding Markdown file under:

```text
issue-traker/issues/
```

2. Identify all affected students.

3. Locate their corresponding logs under:

```text
players-logs-met-bugs/
```

4. Reconstruct their gameplay sequence around the suspected failure.

Do not assume that the activity named in the classroom report is necessarily where the underlying problem originated.

A bug visible during one quest may have been caused by state established much earlier.

---

# 5. Reconstruct the Failure Window

For each affected student, determine:

### Last known good state

What is the last point where game progression appears normal?

### Probable failure window

Identify the narrowest reasonable event/time window during which gameplay appears to diverge from expected progression.

### First abnormal state

What is the earliest observable indication that normal progression did not occur?

The exact failure timestamp may not be known.

Infer the likely failure window from evidence rather than assuming that the final log event represents the bug trigger.

---

# 6. Examine the Pre-Failure Sequence

For the suspected failure window, inspect approximately:

- the previous 20–50 meaningful events;
- the first several events after the suspected failure;
- a wider time window when necessary.

Also inspect earlier events when they may establish prerequisite state.

Prioritize semantically meaningful events.

Examples include:

- quest progression;
- objective changes;
- scene transitions;
- object interactions;
- dialogue events;
- classifier events;
- argumentation events;
- puzzle submissions;
- DANI interactions;
- map interactions;
- Chat interactions;
- NPC interactions;
- save/checkpoint events;
- scene loading;
- reload/resume behavior;
- inventory/evidence state;
- trigger interactions;
- activity completion;
- progress-point events.

High-frequency telemetry such as player position should normally be filtered out of the main event sequence.

However, use positional information when it could reveal:

- whether a trigger volume was reached;
- whether a student returned to an unusual location;
- whether an NPC/object was approached;
- whether movement stopped unexpectedly;
- whether the student became physically trapped.

---

# 7. Look for State-Machine Anomalies

Pay particular attention to patterns such as:

- an event starts but its expected completion event never appears;
- an activity completes but no subsequent quest transition occurs;
- the quest advances without the corresponding activity completion;
- duplicated events;
- repeated interaction loops;
- inconsistent object IDs;
- inconsistent quest IDs;
- inconsistent scene names;
- abnormal scene transitions;
- missing initialization events;
- missing NPC dialogue;
- missing objective activation;
- repeated attempts to interact with the same object;
- unusually long inactivity after an interaction;
- save/reload near the suspected failure;
- different state immediately after reload;
- events arriving in unusual order;
- very rapid interactions that could potentially expose timing/race-condition behavior.

Do not assume any one of these causes the bug.

Treat them as signals requiring evaluation.

---

# 8. Sequence Reconstruction

For every affected student, create a compact sequence such as:

```text
timestamp
→ scene
→ quest/activity state
→ interaction
→ resulting event
→ next expected event
→ observed result
```

Try to identify a minimal sequence leading to the failure.

For example:

```text
Entered classifier
→ completed final classification
→ completion event recorded
→ dialogue event recorded
→ expected quest-transition event absent
→ repeated interaction with classifier
→ player remains in same quest state
```

This is only an example structure.

Do not assume this exact pattern exists.

---

# 9. Cross-Student Comparison Within the Same Bug

If multiple students encountered the same reported bug, compare them.

Ask:

- Do they share the same missing event?
- Do they perform the same unusual action?
- Do they interact with objects in the same order?
- Do they share the same previous quest history?
- Do they reload at similar points?
- Do they share the same scene-entry sequence?
- Do they have the same unusual data value?
- Does the failure occur after the same activity completion?
- Is there a repeated sequence common across affected students?

Pay particular attention to patterns that occur across several affected students.

A shared unusual pattern is much more valuable than a one-off anomaly.

---

# 10. Special Analysis: QA-1694 / Unit 3 Supply Run / Crate 1

The issue documentation indicates that some students affected by this Unit 3 problem had previously experienced Unit 2 progression problems and were advanced into Unit 3.

Treat this as contextual information, NOT as a confirmed cause.

Explicitly evaluate at least two competing explanations.

## Hypothesis A

The Crate 1 issue is an independent Unit 3 bug.

## Hypothesis B

The Crate 1 issue results from incomplete or inconsistent persistent state created by abnormal progression through Unit 2.

Investigate whether these students appear to enter Unit 3 with unusual state.

Look especially for differences involving:

- Unit 3 initialization;
- quest-start events;
- scene initialization;
- inventory state;
- collected evidence;
- NPC state;
- quest flags;
- progress-point state;
- save/checkpoint state;
- previous quest completion;
- crate initialization;
- crate delivery triggers.

Search backward into earlier gameplay history if necessary.

---

# 11. Special Analysis: Refresh/Reload Cases

For bugs where the tracker reports that refreshing or reloading allowed the student to continue:

compare the event/state immediately before reload with the event/state immediately after the game resumes.

Determine whether reload appears to:

- recreate an NPC;
- recreate an interaction trigger;
- initialize a quest;
- restore a missing variable;
- advance a quest;
- skip a broken sequence;
- reset scene state;
- reload an object;
- restore UI state.

This can help distinguish among possibilities such as:

- transient scene-state failure;
- broken trigger;
- stale UI;
- incomplete initialization;
- save-state inconsistency;
- quest-state persistence;
- race condition.

These remain hypotheses unless supported by the evidence.

---

# 12. Use Programmatic Analysis

The logs may be too large for reliable manual inspection.

Use Python or another local scripting method where appropriate.

Useful operations may include:

- parsing log records;
- normalizing timestamps;
- sorting chronologically;
- filtering by student;
- filtering by scene;
- filtering by eventType;
- identifying sessions;
- detecting long temporal gaps;
- extracting windows around target activities;
- counting repeated events;
- comparing event sequences;
- detecting missing transitions;
- comparing data-field values;
- detecting unusual ordering.

Create temporary analysis scripts if useful.

Do not modify source logs.

When automated analysis identifies an important anomaly, inspect the raw records around that anomaly before drawing conclusions.

---

# 13. Hypothesis Evaluation

For each suspected explanation, provide:

### Hypothesis

A concise description.

### Supporting evidence

Specific evidence from the log.

### Contradicting evidence

Evidence that weakens the hypothesis.

### Confidence

High / Medium / Low.

### Reproduction experiment

A specific sequence QA can attempt.

### Verification strategy

What developers should inspect or what additional logging would confirm or reject the explanation.

Generate multiple hypotheses where appropriate.

Do not stop after finding the first plausible explanation.

---

# 14. Required Evidence

Whenever possible, support important findings with:

```text
Student
Log filename
Timestamp
Scene
eventType
Relevant data fields
Immediately preceding event
Immediately following event
```

Avoid unsupported statements such as:

> "The quest flag failed."

Prefer:

> "The classifier completion event appears at 10:42:18, but no subsequent quest-transition event appears in the next 37 meaningful events. Instead, the student interacts with the classifier three additional times."

---

# 15. Report Format for Each Bug

Create one Markdown investigation report per issue.

Use filenames such as:

```text
analysis-output/QA-1693-analysis.md
analysis-output/QA-1694-analysis.md
analysis-output/QA-1697-analysis.md
analysis-output/U4-saving-cadet-anderson-analysis.md
```

If `analysis-output/` does not exist, create it.

Each report should contain:

## Executive Finding

Answer:

> What is the most useful thing the gameplay logs tell us about this bug?

Keep this concise and developer-oriented.

## Reported Symptom

Summarize the classroom report without embellishment.

## Students and Log Mapping

Show which log corresponds to each affected student.

## Probable Failure Window

Identify the relevant timestamp/event range.

## Last Known Good State

Describe the last apparently normal state.

## First Abnormal State

Describe the earliest evidence of divergence.

## Event Reconstruction

Provide a chronological table of the most relevant events.

## Shared Patterns Across Affected Students

Identify patterns repeated across multiple affected students.

## Key Anomalies

List abnormalities supported by evidence.

## Ranked Hypotheses

For each:

- hypothesis;
- evidence for;
- evidence against;
- confidence;
- reproduction procedure;
- verification strategy.

## Suggested QA Reproduction Steps

Provide concrete playthrough sequences QA should attempt.

## Recommended Developer Investigation

Identify the systems/state transitions most worth inspecting.

## Logging Gaps

Identify telemetry that would have made diagnosis easier.

## Confidence and Limitations

Explain what can and cannot be concluded.

---

# 16. Final Cross-Issue Report

After completing all individual reports, create:

```text
analysis-output/cross-issue-summary.md
```

Compare the bugs and identify:

- shared failure mechanisms;
- common missing transitions;
- common reload behavior;
- common state inconsistencies;
- evidence of save/load problems;
- evidence of scene initialization problems;
- evidence of interaction-order problems;
- evidence of persistent-state problems;
- relationships between Unit 2 and Unit 3 failures.

End with:

### Top 3 Most Promising Reproduction Experiments

### Top 3 Code/State Areas to Inspect

### Highest-Value Additional Telemetry

---

# 17. Important Analysis Principle

Your purpose is not to force a definitive root cause from incomplete telemetry.

Your purpose is to:

1. reconstruct what happened;
2. identify where gameplay likely diverged;
3. narrow the search space;
4. identify patterns across affected students;
5. generate falsifiable hypotheses;
6. give QA concrete reproduction procedures;
7. give developers concrete systems or state transitions to inspect.

Clearly distinguish:

**what the logs prove**

from

**what the logs suggest**.