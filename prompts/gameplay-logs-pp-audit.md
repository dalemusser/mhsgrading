> **Note (2026-09-02):** folders referenced below were renamed during the repository refinement: `tests/` → `rubric-validation/`, `gameplay-logs-test/` → `build-log-qa/`, `gameplay-logs-pp-audit/` → `grading-readiness-audit/`. This prompt is kept as a historical task record.

# Task: Build a Gameplay-Log-to-Dashboard-Grading Audit Pipeline for Mission HydroSci

## Background

The Mission HydroSci game has undergone substantial changes since the previous dashboard grading-logic validation work was conducted.

Previously, we created a testing workflow to determine whether the existing dashboard grading logic produced the expected progress-point colors and, when it did not, identify problems in the grading logic.

However, before testing grading logic against the newest version of the game, we now need an earlier audit stage.

The current gameplay logs themselves may have changed because of updates to game tasks, dialogues, event types, event keys, scene structure, interaction design, or logging implementation.

Therefore, the new audit pipeline must answer **two sequential questions**:

### Stage 1 — Gameplay Log Support Audit

Determine whether the current gameplay logs still provide the events, variables, event keys, interaction records, dialogue markers, argumentation records, or other information required by the existing dashboard grading logic for each progress point.

### Stage 2 — Grading Logic Validation

Only after understanding whether the required log evidence still exists, determine whether the current production grading logic correctly interprets those logs and produces the expected progress-point/dashboard colors.

The immediate focus of this task is to build the audit pipeline, with particular emphasis on **Stage 1: verifying that the current gameplay logs still support the current grading logic**.

---

# Repository Materials

Use the repository itself as the primary source of evidence. Do not assume that old event names, dialogue IDs, event keys, or grading assumptions are still valid without checking them against the current gameplay logs.

## 1. Embedded Assessment Working Document

File:

`grading-logic/original-score-rubric-table-and-dialogue-database/MHS-2.0-Embedded-Assessment-Working-Doc.docx`

This document contains information such as:

* progress-point number;
* curriculum topic associated with the progress point;
* game task that the player needs to perform;
* score awarded for relevant actions;
* log tags or dialogue event keys associated with the rubric;
* formulas or rules used to calculate the score;
* other information required to interpret the embedded assessment.

Some log tags or technical references in this document may be outdated relative to the current game build.

Treat this document primarily as evidence of the **assessment/rubric intent**, rather than automatically assuming every technical log identifier is still current.

---

## 2. Progress Point Specification

File:

`grading-logic/original-score-rubric-table-and-dialogue-database/Progress-Points.docx`

This document contains more detailed specifications for individual progress points, including information such as:

* progress-point item number;
* progress-point name;
* progress-point description;
* start event key;
* end event key;
* dialogue text associated with start/end markers;
* rules for determining the progress-point color;
* log marks corresponding to progress-point colors;
* events used to identify argumentation attempts;
* other gameplay-log information required by the grading logic.

This should be used together with the Embedded Assessment Working Document to reconstruct what each progress point is intended to measure.

---

## 3. Dialogue ID and Text Mapping

File:

`grading-logic/original-score-rubric-table-and-dialogue-database/Dialogue-ID-Texts.xlsx`

(Replaced on 2026-09-21 to match build 20260914-; the previous mapping is kept as `Dialogue-ID-Texts-Old.xlsx` for historical comparison only.)

This file contains mappings among:

* conversation ID;
* dialogue node ID;
* corresponding dialogue text.

This is particularly important because many gameplay logs contain event keys resembling:

`DialogueNodeEvent1(conversation ID):12(dialogue ID)`

Use this mapping to determine whether dialogue-based event keys referenced by the rubric or grading logic still correspond to the intended dialogue in the current game.

Do not assume that an old numeric dialogue/event key is still valid simply because it appears in an old grading specification.

---

## 4. Current Dialogue Database Export

File:

`grading-logic/original-score-rubric-table-and-dialogue-database/2026-09-21-MHSDialogueExport.csv`

(The 2026-06-10 export it replaced on 2026-09-23 is still in the folder; audit runs up to `09-14-26-3` used it.)

This contains more detailed information extracted from the Unity dialogue database.

Use this as additional evidence when resolving:

* dialogue IDs;
* conversation IDs;
* dialogue text;
* potentially renamed or changed dialogue nodes;
* ambiguity between historical rubric references and the more recent dialogue database.

---

## 5. Existing Progress-Point Grading Logic

Folder:

`grading-logic`

Markdown files in this folder contain the specific grading implementations used to determine progress-point/dashboard colors.

For example:

`mhs-unit1-point1-grading.md`

corresponds to the first progress point in Unit 1, such as `U1.C1` / `U1.P1`, depending on the naming convention used by the source documents.

Each file may contain explanation, development history, examples, and code.

For this audit, locate and prioritize the section named approximately:

`Production Script`

or the equivalent section containing the final production grading implementation.

The production script should be treated as the **currently implemented grading behavior**, but not automatically as the correct behavior.

The audit must compare:

1. assessment intent;
2. expected log evidence;
3. actual current logs;
4. current production grading code.

---

## 6. Current Gameplay Logs

Folder:

`playthrough-logs-and-results/08-25-26`

The JSON gameplay-log files in this folder represent the newest playthrough data currently available for validating the audit pipeline.

Use these logs to investigate whether the game currently emits the events and data needed by each progress-point grading rule.

These logs are observational evidence from a particular playthrough. Therefore:

**Absence of an event from this playthrough does not automatically prove that the game can never generate it.**

The audit must distinguish among:

* definitely present;
* likely supported but not triggered in this playthrough;
* expected but apparently missing;
* changed/renamed/restructured;
* impossible to determine from available evidence.

---

# Output Location

Save newly generated audit scripts, intermediate machine-readable results, documentation, and reports under:

`gameplay-logs-pp-audit`

Create this directory if it does not already exist.

Do not overwrite the original grading specifications, source documents, production grading files, or gameplay logs.

---

# Core Objective

Build a reproducible audit pipeline that determines, for every dashboard progress point:

> **Can the current gameplay logging system still provide the evidence required for the current grading logic to calculate this progress point correctly?**

Then, where sufficient evidence exists:

> **Does the current grading logic correctly transform that evidence into the intended dashboard color?**

The pipeline should make it possible to rerun this audit against future gameplay-log folders with minimal modification.

---

# Important Conceptual Model

For every progress point, explicitly reconstruct the following chain:

`Assessment Intent`
→ `Required Player Behavior`
→ `Expected Gameplay Evidence`
→ `Actual Current Log Representation`
→ `Production Grading Logic`
→ `Calculated Score/State`
→ `Dashboard Color`

The audit should identify exactly where this chain succeeds or breaks.

Do not collapse these stages into a single pass/fail result.

---

# Required Workflow

## Phase 0 — Inspect the Repository Before Writing the Audit

Before implementing the pipeline:

1. inspect the relevant repository structure;
2. identify all progress-point grading markdown files;
3. inspect the source assessment documents;
4. inspect the dialogue mapping files;
5. inspect the structure of the August 25 gameplay logs;
6. determine the naming conventions used for progress points;
7. identify how production grading scripts consume log records.

Create a concise inventory of relevant files before designing the pipeline.

Do not begin by guessing the schema.

---

# Phase 1 — Build a Progress-Point Dependency Specification

For each progress point, reconstruct the grading requirements from the source documents and current production script.

Create a structured representation containing at least:

* canonical progress-point ID;
* alternate progress-point IDs/names found in source documents;
* unit;
* progress-point title;
* curriculum/assessment intent;
* expected player task;
* relevant game phase or scene if known;
* start marker;
* end marker;
* dialogue text associated with start/end markers;
* required event types;
* required event keys;
* required fields/subvariables;
* required field values;
* relevant ordering or sequencing requirements;
* scoring formula;
* argumentation-attempt definition, if applicable;
* color determination rule;
* current production grading file;
* production-code dependencies;
* source document(s) supporting each requirement.

Very importantly, separate:

### Conceptual requirement

Example:

> Player must inspect three relevant evidence objects before submitting an argument.

from:

### Historical technical implementation

Example:

> Count `ObjectInterEvent` records whose `data.objectName` equals X, Y, or Z.

The conceptual requirement may still be valid while the historical log implementation has changed.

---

# Phase 2 — Build a Current Gameplay Log Inventory

Parse all JSON gameplay-log files under:

`playthrough-logs-and-results/08-25-26`

Build a reusable inventory describing what the current game actually logs.

At minimum, identify:

* all unique `eventType` values;
* frequency of each event type;
* scenes associated with each event type;
* timestamp/time range if available;
* event-key structures;
* unique or representative `data` structures per event type;
* nested field names;
* representative values;
* conversation IDs;
* dialogue node IDs;
* dialogue event keys;
* object-interaction identifiers;
* puzzle events;
* argumentation events;
* assessment-related events;
* progress-point/color markers if present;
* start/end markers;
* other event families referenced by grading logic.

Avoid dumping every raw value into a huge Markdown document.

Instead, produce machine-readable inventories and concise summaries.

If an event contains high-cardinality values such as coordinates or timestamps, summarize their structure rather than listing every value.

---

# Phase 3 — Dialogue/Event-Key Reconciliation

Dialogue-based grading markers require special attention.

For each dialogue-based event key referenced by the grading rubric or production logic:

1. parse its conversation ID and node/dialogue ID;
2. resolve it using `Dialogue-ID-Texts.xlsx`;
3. compare it with `2026-09-21-MHSDialogueExport.csv`;
4. identify the expected dialogue text;
5. search the August 25 gameplay logs for the corresponding dialogue event;
6. determine whether the same numeric identifier still exists;
7. where possible, determine whether the same dialogue text now exists under a different identifier.

Classify each dialogue dependency as one of:

* `EXACT_MATCH`
* `TEXT_MATCH_DIFFERENT_ID`
* `ID_EXISTS_DIFFERENT_TEXT`
* `EXPECTED_DIALOGUE_NOT_OBSERVED`
* `DIALOGUE_REMOVED_OR_CHANGED`
* `AMBIGUOUS`
* `NOT_APPLICABLE`

Never silently substitute a new dialogue ID.

Record the evidence supporting any proposed mapping.

---

# Phase 4 — Progress-Point Log Support Audit

For every progress point, compare the required evidence from Phase 1 with the actual current logging schema from Phases 2–3.

Evaluate each dependency separately.

Suggested dependency statuses:

* `SUPPORTED_EXACTLY`
* `SUPPORTED_WITH_SCHEMA_CHANGE`
* `SUPPORTED_WITH_IDENTIFIER_CHANGE`
* `PARTIALLY_SUPPORTED`
* `NOT_OBSERVED_IN_PLAYTHROUGH`
* `LIKELY_MISSING_FROM_CURRENT_LOGGING`
* `AMBIGUOUS`
* `NOT_REQUIRED`

For each required event/log dependency, record:

* what the existing grading logic expects;
* what the source rubric intends;
* what exists in current logs;
* whether the event was actually observed;
* relevant example log records;
* detected schema differences;
* detected event-name differences;
* detected field/value differences;
* detected dialogue-ID changes;
* whether the current grading script could successfully consume the current record;
* confidence level;
* recommended next investigation.

---

# Critical Distinction: Missing Event vs. Untested Event

Do not treat:

> event not found in the August 25 playthrough

as automatically equivalent to:

> the current game does not log this event.

Use contextual evidence.

For example, determine whether:

* the corresponding game task was actually reached;
* the player performed the relevant interaction;
* the progress-point start/end interval was reached;
* another log event indicates that the relevant game activity happened;
* similar related interactions generated records while this one did not.

Where the gameplay clearly shows that the action occurred but its expected event is absent, this is stronger evidence of a logging problem.

Where the action was never performed, classify the dependency as `NOT_OBSERVED_IN_PLAYTHROUGH` rather than `MISSING`.

---

# Phase 5 — Detect Semantic Drift

Do not only check whether an event name exists.

Check whether the current event still means what the grading logic assumes it means.

Examples of semantic drift include:

* an event still exists but now fires at a different moment;
* `Visible` changed from "player viewed item" to "object loaded in scene";
* interaction identifiers were renamed;
* a puzzle changed from drag behavior to click behavior;
* multiple historical events were consolidated;
* one historical event was split into several event types;
* a dialogue node was renumbered;
* a task no longer requires an action assumed by the old rubric implementation;
* an event now fires multiple times where the grading code assumes one record;
* duplicate records exist;
* a previously discrete event is now represented by a state object.

Flag these separately from simple schema mismatches.

Use a category such as:

`SEMANTIC_DRIFT`

and explain exactly why the existing grading logic could be unreliable even though technically matching event records are present.

---

# Phase 6 — Determine Progress-Point Audit Status

After evaluating all dependencies for a progress point, assign an overall status.

Recommended statuses:

### `READY_FOR_GRADING_TEST`

All essential log evidence appears available and compatible enough to test the grading logic.

### `READY_WITH_MAPPING_UPDATE`

The necessary behavioral evidence exists, but identifiers/event names/schema changed and the grading logic needs an updated mapping.

### `PARTIALLY_AUDITABLE`

Some required evidence exists, but one or more dependencies cannot be confidently validated using the current playthrough.

### `BLOCKED_BY_LOGGING`

The player behavior appears to occur, but required evidence is not emitted or is insufficient for the rubric calculation.

### `BLOCKED_BY_RUBRIC_AMBIGUITY`

The source documents do not provide enough information to determine the intended calculation reliably.

### `BLOCKED_BY_GAME_DESIGN_CHANGE`

The current game task or interaction structure differs enough from the historical rubric that the old grading approach may no longer represent the intended assessment.

### `NEEDS_MANUAL_REVIEW`

Evidence is conflicting or insufficient for an automated conclusion.

---

# Phase 7 — Validate Current Production Grading Logic

For progress points classified as sufficiently supported, run or reproduce the current production grading logic against the August 25 gameplay logs.

The purpose is to determine whether the grading logic works **given the current log representation**.

Do not modify the production implementation before establishing its current behavior.

For each testable progress point, report:

* whether the production logic executes;
* which records it selects;
* intermediate quantities calculated;
* scores calculated;
* thresholds used;
* resulting color;
* expected color according to the rubric and observed gameplay;
* pass/fail;
* explanation of any discrepancy.

Where possible, provide a trace such as:

`raw log records`
→ `filtered relevant records`
→ `attempt count / score components`
→ `score`
→ `threshold`
→ `color`

This traceability is extremely important.

---

# Phase 8 — Root-Cause Classification

When a progress point fails, do not simply report that the color is wrong.

Classify the root cause.

Use categories such as:

* `LOGGING_MISSING_EVENT`
* `LOGGING_MISSING_FIELD`
* `LOGGING_DUPLICATE_EVENT`
* `LOGGING_SCHEMA_CHANGED`
* `LOGGING_IDENTIFIER_CHANGED`
* `DIALOGUE_ID_CHANGED`
* `SEMANTIC_DRIFT`
* `GAME_TASK_CHANGED`
* `OUTDATED_RUBRIC_TECHNICAL_REFERENCE`
* `GRADING_FILTER_BUG`
* `GRADING_COUNTING_BUG`
* `GRADING_SEQUENCE_BUG`
* `GRADING_THRESHOLD_BUG`
* `GRADING_COLOR_MAPPING_BUG`
* `INSUFFICIENT_PLAYTHROUGH_COVERAGE`
* `AMBIGUOUS_SOURCE_SPECIFICATION`
* `OTHER`

A single progress point may have more than one contributing cause.

Clearly distinguish between:

### Logging-side problem

The current game fails to provide sufficient evidence.

### Grading-side problem

The evidence exists, but the dashboard logic interprets it incorrectly.

### Specification-side problem

The grading requirement itself is unclear or no longer aligns with current game design.

---

# Phase 9 — Build the Audit as a Reusable Pipeline

The final result should not be only a one-time report.

Create reusable code so that future gameplay-log folders can be audited.

Prefer a modular Python implementation.

For example, the folder could contain components resembling:

```text
gameplay-logs-pp-audit/
├── README.md
├── config/
│   └── ...
├── scripts/
│   ├── parse_grading_specs.py
│   ├── inventory_gameplay_logs.py
│   ├── reconcile_dialogues.py
│   ├── audit_progress_points.py
│   ├── run_grading_validation.py
│   └── generate_report.py
├── outputs/
│   ├── current-log-inventory.json
│   ├── progress-point-dependencies.json
│   ├── dialogue-reconciliation.csv
│   ├── pp-log-support-audit.csv
│   ├── pp-log-support-audit.json
│   ├── grading-validation.csv
│   └── ...
└── reports/
    ├── audit-summary.md
    └── progress-points/
        ├── u1-p1.md
        ├── ...
```

This structure is illustrative rather than mandatory. Adapt it if the repository structure suggests a better organization.

Avoid one huge Python script.

---

# Machine-Readable Audit Output

Create a machine-readable result for every progress point.

A record should conceptually contain information similar to:

```json
{
  "progress_point": "U1.P1",
  "progress_point_name": "...",
  "assessment_intent": "...",
  "grading_file": "...",
  "required_dependencies": [],
  "observed_dependencies": [],
  "dialogue_mapping_status": "...",
  "log_support_status": "READY_FOR_GRADING_TEST",
  "grading_test_status": "...",
  "expected_color": "...",
  "actual_color": "...",
  "root_causes": [],
  "confidence": "...",
  "evidence": [],
  "recommended_action": "..."
}
```

Do not copy this schema blindly if more fields are needed.

Design a useful structured schema that allows subsequent automated analysis.

---

# Human-Readable Summary Table

Generate a concise master table containing at least:

| Progress Point | Rubric Requirement | Required Log Evidence | Current Evidence | Log Support Status | Grading Test | Root Cause | Recommended Action |
| -------------- | ------------------ | --------------------- | ---------------- | ------------------ | ------------ | ---------- | ------------------ |

Keep the master summary concise.

Put detailed evidence in individual progress-point reports or machine-readable files.

---

# Per-Progress-Point Reports

Generate a separate detailed Markdown audit file for each progress point rather than placing all details into one extremely long report.

Each progress-point report should include:

## 1. Progress Point

* ID
* title
* unit
* source grading file

## 2. Assessment Intent

Explain what student/player behavior is intended to be assessed.

## 3. Current Production Logic

Summarize what the current code actually does.

## 4. Required Log Evidence

List the exact dependencies.

## 5. Evidence Found in Current Logs

Show concise representative examples.

## 6. Dependency Audit

Explain which required pieces are present, changed, absent, ambiguous, or untested.

## 7. Dialogue Reconciliation

If applicable.

## 8. Semantic Drift

If applicable.

## 9. Overall Log Support Status

Provide the classification and rationale.

## 10. Grading Validation

If sufficient logging support exists, show the calculation trace and resulting color.

## 11. Root Cause

If something fails.

## 12. Recommended Action

Clearly state whether the likely action belongs to:

* gameplay logging;
* grading code;
* rubric/specification;
* more playtesting;
* manual investigation.

---

# Evidence Requirements

Every important conclusion should be traceable to evidence.

When claiming that a required gameplay event exists or does not exist, provide information such as:

* source gameplay-log file;
* event type;
* timestamp if available;
* scene;
* event key;
* relevant `data` values;
* representative record identifier if available.

When claiming that grading logic depends on something, identify:

* grading Markdown file;
* relevant production-code condition;
* supporting rubric/document source.

When identifying dialogue mappings, identify:

* conversation ID;
* node ID;
* dialogue text;
* source mapping file.

Avoid unsupported conclusions.

---

# Important Audit Principles

## 1. Do Not Assume the Existing Grading Logic Is Correct

The current code is one object being audited.

It is not the ground truth.

---

## 2. Do Not Assume Historical Technical Log Tags Are Current

The assessment intent may remain correct while event identifiers changed.

---

## 3. Do Not Modify Production Grading Files During the Initial Audit

First establish:

* current behavior;
* current dependencies;
* current incompatibilities.

If fixes are later recommended, place proposed code separately under the audit folder unless explicitly asked to modify production files.

---

## 4. Preserve Raw Evidence

Do not alter source gameplay logs.

---

## 5. Prefer Behavioral Meaning Over Identifier Matching

For example, a changed dialogue ID should not automatically imply lost assessment evidence if the same dialogue/task can be reliably identified in the current game.

At the same time, do not automatically infer equivalence.

Document the evidence.

---

## 6. Distinguish "Not Observed" from "Not Logged"

This distinction is mandatory.

---

## 7. Check Both Structural and Semantic Compatibility

An event can match the expected schema and still no longer represent the intended behavior.

---

## 8. Avoid False Precision

Use confidence labels when conclusions depend on incomplete playthrough coverage.

Suggested values:

* `HIGH`
* `MEDIUM`
* `LOW`

Explain uncertainty when necessary.

---

# Initial Exploratory Analysis

Before auditing individual progress points, produce an exploratory overview of the August 25 gameplay dataset.

At minimum summarize:

* number of JSON files;
* approximate number of records;
* unique event types;
* event counts;
* scenes;
* broad chronological coverage;
* dialogue-event structure;
* argumentation-event structure;
* object-interaction structure;
* puzzle-event structure;
* potentially assessment-relevant events.

Also identify obvious anomalies such as:

* duplicated events;
* malformed records;
* unexpected null values;
* inconsistent event naming;
* inconsistent schemas for the same event type.

These findings may explain later grading failures.

---

# Special Attention to Event Names and Casing

Event names may differ only in capitalization, spacing, or naming style.

Examples may include differences resembling:

* `ObjectInterEvent`
* `objectInterEvent`

Do not silently normalize these differences during the audit.

First report the raw names actually present.

Then determine whether production grading logic treats the distinction as significant.

You may create normalized fields for analysis, but preserve the original values.

---

# Special Attention to Argumentation Attempts

For progress points whose color depends on argumentation attempt counts:

1. reconstruct exactly how an "attempt" is defined in the source specification;
2. identify every event type involved;
3. determine whether the current logs still expose all required information;
4. check whether duplicate events could inflate attempt counts;
5. check whether renamed events or changed submission behavior could undercount attempts;
6. compare the conceptual definition with the production implementation.

Do not assume that every argumentation-related event represents one independent attempt.

---

# Special Attention to Progress-Point Boundaries

Where grading uses start/end dialogue events or similar markers:

1. verify that both markers still exist;
2. verify that they occur in the expected chronological order;
3. determine whether the relevant gameplay evidence occurs inside the intended interval;
4. inspect whether changed dialogue flow causes unrelated records to be included or valid records to be excluded;
5. flag progress points where the historical interval logic is no longer reliable.

---

# Validation and Testing

Add automated checks where feasible.

Examples:

* expected grading files discovered;
* progress points successfully mapped to grading files;
* required columns read from Excel/CSV;
* JSON logs parse successfully;
* dialogue keys can be parsed;
* duplicate keys detected;
* production dependencies found in current schema;
* progress-point boundaries occur in valid order;
* grading functions execute without error;
* machine-readable audit outputs conform to expected schema.

Include informative warnings instead of silently skipping malformed or unresolved items.

---

# README

Create:

`gameplay-logs-pp-audit/README.md`

Explain:

* purpose of the audit;
* conceptual pipeline;
* folder structure;
* data sources;
* how to run the audit;
* how to point the pipeline to a new gameplay-log folder;
* generated outputs;
* meaning of audit statuses;
* known limitations;
* difference between logging support audit and grading correctness audit.

The goal is that another researcher or developer can rerun the process later without needing to reconstruct the methodology from scratch.

---

# Final Audit Summary

Create a top-level report such as:

`gameplay-logs-pp-audit/reports/audit-summary.md`

The report should answer:

1. How many progress points were examined?
2. How many are currently `READY_FOR_GRADING_TEST`?
3. How many require identifier/schema mapping updates?
4. How many are blocked by apparently missing logging?
5. How many could not be evaluated because the relevant behavior was not exercised during the August 25 playthrough?
6. How many appear affected by changes in game design?
7. How many appear to have grading-logic problems?
8. Which event types or identifiers create problems across multiple progress points?
9. Which progress points should be prioritized for additional playtesting?
10. Which problems should be communicated to the game-development team versus fixed in dashboard grading logic?

Include a concise prioritization section such as:

### Priority A — Logging blocks grading entirely

### Priority B — Evidence exists but grading mapping/code must change

### Priority C — Additional targeted playthrough required

### Priority D — Specification clarification required

---

# Recommended Execution Strategy

Work incrementally.

Do **not** attempt to generate the entire audit framework based only on filenames and assumptions.

A good sequence is:

1. inspect source documents and repository structure;
2. inventory progress-point grading implementations;
3. inspect current gameplay-log schemas;
4. build the dependency model;
5. reconcile dialogue references;
6. audit log support;
7. validate grading behavior where possible;
8. generate reports;
9. run consistency checks;
10. summarize cross-progress-point findings.

After implementing each major stage, inspect its outputs before depending on them in the next stage.

---

# Important Requirement About Existing Files

Before writing new code, search the repository for any previous:

* grading audit scripts;
* color-validation pipeline;
* grading test scripts;
* progress-point analysis;
* gameplay-log parsers;
* dialogue mapping utilities;
* reusable functions.

The previous grading-logic audit work may already contain useful components.

Reuse appropriate code where possible, but do not assume that its event mappings remain valid.

If previous audit logic is reused, document:

* which component was reused;
* why it is still applicable;
* what needed to change for the current game version.

---

# What Not to Do

Do not:

* immediately rewrite all grading scripts;
* assume missing records indicate missing game logging;
* treat the old event IDs as authoritative;
* use only event-name matching without inspecting payload semantics;
* generate only a prose report with no reproducible audit code;
* put every progress point into one enormous Markdown file;
* overwrite production grading logic;
* silently repair mismatches while auditing;
* infer expected colors without explaining the evidence and rubric calculation;
* declare a grading bug when the real issue is missing log evidence;
* declare a logging bug when the required action was never exercised during the playthrough.

---

# Final Goal

At the end of this task, we should be able to answer for every dashboard progress point:

> **What behavior is this progress point intended to assess?**

> **What log evidence does the current grading implementation require?**

> **Does the current version of Mission HydroSci actually generate that evidence?**

> **If the representation changed, can the same behavioral evidence still be reliably identified?**

> **If sufficient evidence exists, does the production grading logic calculate the correct progress-point score/color?**

> **If something fails, is the root cause in the gameplay logging, game design, grading implementation, outdated technical specification, or insufficient test coverage?**

Most importantly, the resulting pipeline should be reusable against future gameplay builds so that we can detect logging/grading regressions systematically rather than manually rediscovering them after every major game update.
