> **Note (2026-09-02):** folders referenced below were renamed during the repository refinement: `tests/` → `rubric-validation/`, `gameplay-logs-test/` → `build-log-qa/`, `gameplay-logs-pp-audit/` → `grading-readiness-audit/`. This prompt is kept as a historical task record.

# Task: Build a Reusable Gameplay Log Audit Pipeline for Mission HydroSci

## Background

I regularly conduct gameplay-log investigations for **Mission HydroSci (MHS)**. A new game build is typically released each week, and I play through the build and obtain one or more gameplay log JSON files.

Until now, I have manually examined the logs by asking questions such as:

* What `eventType` values occur in the log?
* How many records exist for each event type?
* In which `sceneName` values does each event type occur?
* What variables/subvariables occur inside `data` for each event type?
* What unique values occur within those variables?
* Are required fields missing, null, empty, or unexpectedly formatted?
* Does an event contain enough information to reconstruct the player's meaningful interaction?
* Does the logged information align with what actually happened in the game?
* Are action names and values consistent with the current game design?
* Are event frequencies reasonable?
* For continuously recorded events such as player position, how frequently are records generated?
* How long was the player in a particular scene according to the earliest and latest timestamps?
* Are events being recorded too often, too rarely, or duplicated?
* Are expected start/end or open/close events paired correctly?
* Do events appear in a reasonable chronological order?
* Do different events describing the same gameplay activity agree with each other?
* Are event types unexpectedly missing from a new build?
* Did an existing event's schema change from the previous build?
* Were new fields, action types, scene names, or event types introduced?
* Did previously fixed logging issues reappear?

I want to convert this manual investigation into a **recursive, reusable, mostly automated weekly process**.

The goal is NOT simply to summarize the JSON files. The goal is to construct a reusable **gameplay logging QA/audit pipeline** that can be applied every week when a new MHS build is released.

## Available Example Data and Output Location

### Example Gameplay Log for Development and Validation

A specific gameplay-log example is available in:

```text
playthrough-logs-and-results/08-25-26
```

This folder contains gameplay log data from the **August 25, 2026 playthrough/build investigation**.

When you need real gameplay data to:

* understand the current JSON structure;
* inspect how existing event types are represented;
* develop the audit functions;
* test the pipeline;
* validate analysis results;
* demonstrate how the pipeline should be used;
* generate an example audit report;

please use the gameplay log file(s) contained in:

```text
playthrough-logs-and-results/08-25-26
```

Treat this dataset as the primary concrete example for developing and validating the reusable audit workflow.

However, do **not** design the pipeline specifically around this single file or build. The pipeline must remain general enough to work with gameplay logs from future weekly builds.

If multiple JSON/log files exist in this folder, first inspect them and determine their roles rather than arbitrarily selecting one.

---

## Preferred Output Location

If it is compatible with the existing repository structure, save the files created for this task under:

```text
gameplay-logs-test/
```

This should preferably serve as the root folder for the reusable gameplay-log audit system.

For example, a reasonable organization could be:

```text
gameplay-logs-test/
│
├── config/
│   ├── event_expectations.yaml
│   ├── event_aliases.yaml
│   └── coverage_manifest.yaml
│
├── src/
│   ├── loader.py
│   ├── normalizer.py
│   ├── inventory.py
│   ├── schema_audit.py
│   ├── value_audit.py
│   ├── frequency_audit.py
│   ├── temporal_audit.py
│   ├── sequence_audit.py
│   ├── coverage_audit.py
│   ├── regression_audit.py
│   └── report_generator.py
│
├── scripts/
│   └── audit_logs.py
│
├── tests/
│
├── reports/
│   └── 08-25-26/
│       ├── audit-report.md
│       └── supporting outputs
│
└── README.md
```

This exact structure is not mandatory.

If the repository's existing organization suggests a substantially better structure, you may adjust it, but:

1. keep the files created specifically for this task well organized;
2. avoid scattering new scripts and generated outputs across unrelated repository folders;
3. preferably keep the work under `gameplay-logs-test/`;
4. explain clearly if you decide that another structure is more appropriate and why.

Do not move, rename, or modify the original gameplay logs under:

```text
playthrough-logs-and-results/08-25-26
```

Treat those files as read-only source data.

---

# Primary Goal

Please inspect the repository, understand the existing gameplay-log documentation, saved in the folder of `playthrough-logs-and-results` and example logs, and then create a modular Python-based system that can:

1. ingest new gameplay log files;
2. characterize their structure comprehensively;
3. check them against expected logging behavior;
4. identify suspicious or inconsistent records;
5. compare them against a previous build when available;
6. export machine-readable intermediate results;
7. automatically generate a clear Markdown examination report for human review.

The system should minimize the amount of manual code I need to rewrite from week to week.

---

# Important Principle: Separate Observation From Expectation

The pipeline must clearly distinguish between:

### A. Observed behavior

What is actually present in the log.

For example:

* observed event types;
* observed scene names;
* observed fields;
* observed action values;
* event counts;
* timing;
* unique values;
* event sequences.

### B. Expected behavior

What the logging specification says SHOULD occur.

Expected behavior should be derived from existing logging documentation in the repository whenever possible.

### C. Coverage limitations

Whether the relevant game content was actually exercised during the playthrough.

This distinction is critical.

For example, if `SolarStillDesignEvent` does not occur, that should NOT automatically be treated as a logging defect if the player never reached the Solar Still activity.

Likewise, if Unit 4 was never reached, Unit 4-specific events should not automatically be reported as missing.

Use statuses such as:

* `PASS`
* `WARNING`
* `FAIL`
* `NOT_TESTED`
* `INFO`

when appropriate.

---

# Step 1 — Inspect the Repository Before Implementing

Before writing the audit system, inspect the repository carefully, especially an example investigation case related to the gameplay log invesgation happened in Aug. 13th 2026, saved in the folder of `playthrough-logs-and-results/08-13-26`.

Look for:

* gameplay log JSON files;
* previous exported log-analysis files;
* logging design documentation;
* Markdown specifications;
* README files;
* scripts already used for gameplay-log analysis;
* sample reports;
* references to event types;
* descriptions of game units/scenes;
* documentation describing expected player interactions.

In particular, search for documentation concerning event types such as, but not limited to:

* `PlayerPositionEvent`
* `PuzzlePieceVisibleEvent`
* `ObjectInterEvent`
* `questEvent`
* `WaterChamberEvent`
* `argumentationNodeEvent`
* `argumentationToolEvent`
* `argumentationEvent`
* `argumentationAnswerEvent`
* `Soil Key Puzzle`
* `TopographicMapEvent`
* `DaniEvent`
* `ChatEvent`
* `SolarStillDesignEvent`

Do NOT assume these examples represent the complete current event-type list.

Discover the current event types from the repository and the logs.

Also search for historical specifications because an event's expected structure may have changed between builds.

When documentation and observed data disagree, report the disagreement rather than silently deciding that one is correct.

---

# Step 2 — Design the Pipeline Before Writing Large Amounts of Code

Design the audit system so that expectations are **configuration-driven rather than hard-coded throughout the Python scripts**.

For example, consider a structure conceptually similar to:

```text
gameplay-log-audit/
│
├── config/
│   ├── event_expectations.yaml
│   ├── event_aliases.yaml
│   └── coverage_manifest.yaml
│
├── src/
│   ├── loader.py
│   ├── normalizer.py
│   ├── inventory.py
│   ├── schema_audit.py
│   ├── value_audit.py
│   ├── frequency_audit.py
│   ├── temporal_audit.py
│   ├── sequence_audit.py
│   ├── coverage_audit.py
│   ├── regression_audit.py
│   └── report_generator.py
│
├── scripts/
│   └── audit_logs.py
│
├── tests/
│
└── reports/
```

This is only a suggested architecture.

If the repository already has a better organizational pattern, follow it.

The important requirement is that **new logging expectations should normally be added through configuration instead of rewriting analysis logic**.

---

# Step 3 — Build a Robust Log Loader

The loader should be able to deal with realistic variations in exported logs.

Determine from the repository whether logs are:

* JSON arrays;
* JSON objects;
* JSON Lines / NDJSON;
* multiple files belonging to one gameplay session;
* multiple sessions stored together.

Do not assume a format without inspecting examples.

The loader should preserve the original records while creating a normalized representation suitable for analysis.

Identify important top-level variables such as:

* timestamp;
* event type;
* scene;
* player/session identifier;
* build/version information;
* `data`;
* device information;

or whatever fields actually exist in the current logging implementation.

Do not invent fields that do not exist.

---

# Step 4 — General Event Inventory

For every new build, automatically create an inventory of all observed event types.

For each `eventType`, calculate at minimum:

* total record count;
* percentage of all events;
* earliest timestamp;
* latest timestamp;
* duration between first and last occurrence;
* number of sessions containing the event;
* observed `sceneName` values;
* count by scene;
* top-level fields observed;
* fields observed under `data`;
* data types of fields;
* missing/null frequency;
* example records.

Export a table similar conceptually to:

```text
eventType
record_count
percent_of_total
session_count
first_timestamp
last_timestamp
observed_scenes
data_fields
missing_field_count
```

---

# Step 5 — Deep Profiling for Every Event Type

One of the most important functions should reproduce the kinds of questions I have repeatedly investigated manually.

For **every event type**, automatically determine:

## Scene information

* all unique `sceneName` values;
* frequency by `sceneName`;
* earliest/latest occurrence in each scene;
* how long the event appears within each scene;
* unexpected scene names;
* spelling/capitalization inconsistencies.

## `data` structure

Identify every subvariable occurring under `data`.

For every subvariable, report:

* data type;
* count;
* missing count;
* null count;
* empty-string count;
* number of unique values;
* unique values when cardinality is reasonably small;
* representative values when cardinality is large.

For nested objects, recursively inspect their structure.

For example, rather than simply reporting:

```text
data exists
```

the system should be able to report something conceptually similar to:

```text
eventType: ExampleEvent

data.actionType
    unique values:
        Open
        Close
        Submit

data.objectName
    unique values:
        Map
        Legend
        Water

data.position
    x: numeric
    y: numeric
    z: numeric
```

Do this generically rather than writing separate code for every event type.

---

# Step 6 — Schema Consistency Audit

For each event type, determine whether records use a consistent schema.

Detect:

* fields that occur only in some records;
* unexpected fields;
* missing required fields;
* null fields;
* type inconsistencies;
* inconsistent nesting;
* field-name spelling differences;
* capitalization differences;
* different representations of equivalent values.

Examples include situations conceptually similar to:

```text
Started
started
Start
```

or:

```text
sceneName = Unit2
sceneName = Unit 2
```

Do not automatically merge them unless the specification explicitly indicates that they are aliases.

Report them first.

---

# Step 7 — Event Semantics and Content Sufficiency

This audit should go beyond syntax.

Where documentation specifies the purpose of an event, evaluate whether the event contains enough information to represent the intended gameplay behavior.

Examples of questions include:

* Can we determine what the player interacted with?
* Can we determine what action the player performed?
* Can we determine what option/value the player selected?
* Can we determine whether an interaction succeeded or failed?
* Can we determine the state before and/or after an interaction where required?
* Can repeated attempts be distinguished?
* Can a player's interaction sequence be reconstructed?

Do not make unsupported assumptions.

Base semantic checks on documentation found in the repository.

If the specification is incomplete, flag the issue as:

```text
SPECIFICATION UNCLEAR
```

rather than declaring the implementation incorrect.

---

# Step 8 — Event-Specific Expectations

Create a configuration mechanism such as `event_expectations.yaml`.

A conceptual event rule might contain information such as:

```yaml
SomeEvent:
  expected_scenes:
    - ExampleScene

  required_fields:
    - data.actionType

  allowed_values:
    data.actionType:
      - Open
      - Close

  sequence_rules:
    - Open should normally precede Close
```

The exact structure can be improved based on the actual repository.

Important:

Do NOT manually hard-code all event expectations without first reading the current documentation.

The configuration should become the central location where I can update expectations when the developers modify the logging design.

---

# Step 9 — Frequency Analysis

Frequency auditing is particularly important.

For every event type calculate:

* total count;
* count per session;
* count per scene;
* count per minute where meaningful;
* time intervals between consecutive records;
* minimum interval;
* median interval;
* mean interval;
* maximum interval;
* useful percentiles such as P5/P25/P75/P95;
* unusually long gaps;
* unusually rapid bursts;
* exact duplicate or near-duplicate records.

Different event types should be interpreted differently.

For example:

### Continuous events

For events such as `PlayerPositionEvent`, determine approximately how often records are generated.

Calculate the distribution of timestamp differences between consecutive records within the same session/scene.

This should help answer questions such as:

> Is one position record generated every second, every five seconds, or irregularly?

Also verify whether position-related values such as `x`, `y`, and `z` actually exist when the specification expects them.

### Interaction events

For click/interact/submit events, do not expect fixed intervals.

Instead look for:

* suspicious duplicated records;
* very large numbers of events from one interaction;
* bursts occurring within extremely small time intervals.

### Start/end events

Determine whether start and completion counts are reasonably balanced.

---

# Step 10 — Temporal and Sequence Analysis

Sort events chronologically within each gameplay session.

Check for logically meaningful sequences where documentation supports such rules.

Examples may include:

```text
Started -> interactions -> Finished
Open -> interactions -> Close
PuzzleStarted -> attempts -> PuzzleFinished
QuestStarted -> gameplay -> QuestCompleted
ToolOpened -> actions -> ToolClosed
Selections -> Submit
```

Look for:

* completion without start;
* close without open;
* repeated starts;
* repeated completions;
* impossible ordering;
* timestamp reversals;
* extremely delayed paired events;
* events from a scene occurring after leaving that scene;
* actions occurring after an activity is supposedly completed.

Do not impose sequence rules on events for which the documentation does not define a meaningful sequence.

---

# Step 11 — Scene-Level Analysis

Create a scene-level timeline.

For each session and scene report:

* first event timestamp;
* last event timestamp;
* approximate observed duration;
* total number of events;
* event types occurring there;
* entry/exit indicators if available.

This should support questions such as:

> According to the logs, how long did the gameplay remain in `Unit 2 Prod (Refactor)`?

Also identify unexpectedly long or short durations that might indicate:

* a player being blocked by a bug;
* idle time;
* duplicated timestamp behavior;
* logging continuing after a scene transition.

Do not automatically classify such cases as bugs; flag them for inspection.

---

# Step 12 — Coverage Analysis

Create a way to distinguish between:

```text
event missing because logging failed
```

and:

```text
event missing because that gameplay content was not tested
```

If possible, create a simple file such as:

```text
coverage_manifest.yaml
```

that I can update after each weekly playtest.

It could conceptually describe:

```yaml
build: 2026XXXX-build-name

tested_content:
  Unit1: complete
  Unit2: partial
  Unit3: complete
  Unit4: skipped
  Unit5: partial

notes:
  - Unable to progress beyond Soil Key Puzzle in Unit 2.
  - Jumped to Unit 4 using debug menu.
```

The exact design can be improved.

The audit report should use this information before declaring expected events missing.

If no coverage manifest exists, infer coverage cautiously from observed scene/quest logs and clearly label the inference.

---

# Step 13 — Cross-Event Consistency

Where multiple event types describe related gameplay behavior, check whether they agree.

Examples might include:

* quest progression vs interaction events;
* argumentation tool events vs argumentation answer events;
* scene transitions vs scene-specific interactions;
* puzzle start/finish events vs actual puzzle interactions;
* map interactions vs map open/close events;
* player position records vs active scene.

Look for contradictions such as:

* puzzle completion without puzzle interaction;
* tool interaction after tool close;
* quest completion before prerequisite activity;
* scene-specific events occurring in another scene.

Only implement a rule when there is evidence from documentation or gameplay design supporting it.

---

# Step 14 — Regression Analysis Between Builds

This should be one of the core weekly functions.

When a previous build's logs or audit outputs are available, compare the new build against the previous build.

Identify:

## Event types

* newly introduced event types;
* removed event types;
* events present previously but absent now.

## Scene names

* new scenes;
* removed scenes;
* renamed scenes.

## Schemas

* newly added fields;
* removed fields;
* changed field types;
* changed nesting.

## Values

* new `actionType` values;
* removed action values;
* renamed values;
* other newly observed categorical values.

## Frequency

Identify major frequency changes such as:

```text
Previous build:
PlayerPositionEvent = approximately every 5 seconds

Current build:
PlayerPositionEvent = approximately every 0.5 seconds
```

or large changes in event volume.

Do NOT automatically assume a change is a defect.

Categorize it as a regression candidate requiring review.

---

# Step 15 — Historical Baseline

If feasible, allow the pipeline to save a normalized audit snapshot for each build.

For example:

```text
reports/
    2026XXXX-build-A/
    2026XXXX-build-B/
    2026XXXX-build-C/
```

The next build can then be compared against:

* the immediately previous build; and/or
* a selected known-good baseline.

This would allow recurring problems to be detected.

---

# Step 16 — Special Attention to Previously Investigated Logging Questions

Use previous logging documentation and repository history to identify known areas of concern.

Examples of the kinds of issues previously investigated include:

### PlayerPositionEvent

Questions such as:

* Which scenes contain it?
* Does `data` actually contain `x`, `y`, and `z`?
* How frequently is a position event recorded?
* How long do position events continue within a scene?

### PuzzlePieceVisibleEvent

Questions such as:

* Which scenes contain it?
* Which fields occur under `data`?
* What unique values occur for each field?
* Are `Visible`/state semantics being represented consistently?

### ObjectInterEvent

Questions such as:

* Which scenes contain it?
* What interaction-related fields exist?
* What objects/actions are observed?

### Argumentation-related events

Investigate:

* scene coverage;
* node/action types;
* answers;
* tool usage;
* missing Unit-specific records;
* relationship among different argumentation event types.

### Soil Key Puzzle

Historically this event contained only limited states such as starting and finishing.

Later logging designs may include interactions such as dragging or manipulating puzzle components.

Read the current specification to determine the CURRENT expected actions.

### TopographicMapEvent

The interaction design changed over time.

For example, map interactions may have moved from drag-based waypoint behavior to click/reset behavior and may include use of legends or other map controls.

Do NOT assume the historical implementation is still correct.

Compare:

```text
current documentation
vs.
current logs
vs.
previous build
```

### ChatEvent

Determine whether the logs capture the interactions currently expected by the specification, such as opening, closing, scrolling, or viewed content if those behaviors are intended to be logged.

### SolarStillDesignEvent

Determine whether design option selections and submission behavior provide sufficient information to reconstruct the player's Solar Still design attempt.

These are examples of the **type of reasoning** the audit system should support.

They should not replace reading the current documentation.

---

# Step 17 — Detect Duplicate and Suspicious Records

Identify:

* exact duplicate JSON records;
* duplicate events with identical timestamps;
* repeated events occurring within extremely short time windows;
* multiple completion events;
* repeated open/close events;
* suspiciously identical interaction sequences.

Export the suspicious records so I can inspect them directly.

Do not remove them from the source logs.

---

# Step 18 — Preserve Examples for Human Inspection

For every event type, export representative raw examples.

Prefer examples such as:

* first occurrence;
* last occurrence;
* common/typical record;
* record with missing fields;
* record with unusual fields;
* record associated with a warning;
* record representing each important action type.

This makes it possible to validate the automatic interpretation against the raw JSON.

---

# Step 19 — Export Machine-Readable Results

At minimum, consider generating files conceptually similar to:

```text
event_type_summary.csv
event_scene_summary.csv
event_field_summary.csv
event_unique_values.csv
event_frequency_summary.csv
scene_timeline.csv
schema_issues.csv
sequence_issues.csv
duplicate_events.csv
coverage_summary.csv
regression_diff.csv
event_examples.json
audit_results.json
```

The exact names may be improved.

Avoid producing dozens of unnecessary files.

Prefer a small set of clearly organized, useful outputs.

---

# Step 20 — Generate a Human-Readable Markdown Report

For each build automatically create something such as:

```text
audit-report.md
```

The report should be useful for both me and potentially the development team.

Recommended structure:

# MHS Gameplay Log Audit Report

## 1. Build Information

* build name;
* audit date;
* log files;
* number of sessions;
* gameplay coverage;
* baseline build used for comparison.

## 2. Executive Summary

Briefly summarize:

* number of event types;
* major PASS findings;
* major warnings;
* possible logging defects;
* new events or schemas;
* regressions;
* areas not tested.

## 3. Event Inventory

Table containing all event types and major statistics.

## 4. New / Removed / Changed Events

Explain differences from the previous build.

## 5. Schema Findings

Summarize missing fields, unexpected fields, type changes, etc.

## 6. Frequency Findings

Highlight suspicious frequency behavior.

## 7. Sequence / Timing Findings

Highlight temporal inconsistencies.

## 8. Coverage Findings

Clearly distinguish untested content from potential logging failures.

## 9. Event-Type Details

For every important event type include:

* purpose if known;
* observed scenes;
* count;
* data fields;
* important unique values;
* timing/frequency;
* expected vs observed;
* warnings;
* representative examples or links to exported examples.

## 10. Regression Comparison

Compare current vs previous build.

## 11. Recommended Follow-Up

Provide a concise list of items requiring:

* developer investigation;
* documentation clarification;
* additional gameplay testing;
* no action.

---

# Step 21 — Prioritize Findings

Not every difference should be treated equally.

Use severity levels conceptually similar to:

### Critical

Logging is missing or malformed in a way that prevents meaningful analysis.

### High

Important interaction information is missing or the implementation clearly conflicts with the current specification.

### Medium

Possible schema, frequency, ordering, or consistency issue that requires investigation.

### Low

Naming inconsistency or minor quality issue.

### Info

New values, new event types, expected changes, descriptive observations.

### Not Tested

No conclusion because relevant content was not exercised.

Include evidence for each issue.

For example:

```text
Finding:
TopographicMapEvent contains a new actionType.

Observed:
actionType = "LegendClick"

Expected:
Current specification lists Open, Close, Reset, and WaypointClick.

Evidence:
23 records in Unit X.

Classification:
INFO / SPECIFICATION REVIEW REQUIRED
```

Do not simply write:

```text
TopographicMapEvent is wrong.
```

---

# Step 22 — Make the Report Evidence-Based

Every warning or failure should ideally include enough evidence to reproduce the finding.

Include information such as:

* event type;
* field;
* observed value;
* expected value;
* count;
* scene;
* session;
* timestamp;
* source log file;
* representative record identifier if one exists.

This is particularly important when I communicate the issue to developers.

---

# Step 23 — Make the Pipeline Easy to Run Weekly

Design a simple command-line entry point.

Conceptually, I should eventually be able to run something similar to:

```bash
python scripts/audit_logs.py \
    --input path/to/new-build-logs \
    --build-id "2026XXXX-new-build" \
    --baseline reports/previous-build \
    --config config/event_expectations.yaml \
    --output reports/2026XXXX-new-build
```

The exact interface may be improved.

If there is only one log file, the pipeline should still work.

If no baseline is supplied, skip regression analysis gracefully.

If no expectation rule exists for an event, still perform descriptive profiling and mark expectation-based checks as unavailable.

---

# Step 24 — Code Quality Requirements

The implementation should be suitable for repeated research use.

Please:

* use clear Python modules/functions;
* add docstrings;
* add type hints where useful;
* avoid unnecessary dependencies;
* use `pandas` where appropriate;
* keep raw-data loading separate from audit logic;
* do not modify raw log files;
* handle malformed records gracefully;
* log warnings instead of crashing whenever possible;
* ensure deterministic outputs;
* make the code understandable enough for me to modify later.

Avoid creating one giant Python script.

---

# Step 25 — Add Tests

Create a small but meaningful test suite using synthetic log records.

Tests should cover important cases such as:

* normal event records;
* missing fields;
* inconsistent field types;
* unknown event types;
* duplicate events;
* start without finish;
* finish without start;
* new action values;
* missing expected scene;
* continuously recorded event frequency;
* no baseline supplied;
* partial gameplay coverage.

Do not require the real gameplay logs for every automated test.

---

# Step 26 — Documentation

Create a short README explaining the recurring workflow.

The README should explain:

1. where to place the new weekly logs;
2. how to identify the build;
3. how to record gameplay coverage;
4. how to run the audit;
5. where generated results are saved;
6. how to interpret PASS/WARNING/FAIL/NOT_TESTED;
7. how to update an event's logging expectations;
8. how to compare with another build;
9. how to add rules for a new event type.

---

# Step 27 — Implementation and Validation Strategy

Do not immediately create a huge framework before understanding the data.

Proceed in this order:

## Phase 1 — Repository Investigation

Inspect the repository and explain:

* where gameplay logs are stored;
* how logging specifications are documented;
* what previous analysis scripts/results exist;
* how event types are currently described;
* what files are relevant to building the recurring audit workflow.

Pay particular attention to:

```text
playthrough-logs-and-results/08-25-26
```

Use its gameplay log file(s) as a concrete example when investigating the actual log structure.

---

## Phase 2 — Current-State Assessment

Using the available documentation and the example gameplay log, identify:

* what can already be analyzed generically;
* what event-specific expectations can be extracted;
* what information is missing from the specifications;
* what parts require configurable rules;
* what kinds of manual questions from previous investigations can be automated.

Do not start by hard-coding assumptions from the example log.

---

## Phase 3 — Architecture

Propose the concrete reusable architecture that best fits this repository.

Prefer saving the implementation under:

```text
gameplay-logs-test/
```

when appropriate.

Explain:

* what each module does;
* which components are generic;
* which components depend on configuration;
* how new event types will be supported;
* how weekly builds will be compared.

---

## Phase 4 — Core Implementation

Implement:

* loader;
* normalization;
* general event inventory;
* field/value profiling;
* scene profiling;
* frequency analysis;
* duplicate detection;
* report generation.

---

## Phase 5 — Rule-Based QA

Add:

* expectation configuration;
* schema checks;
* sequence checks;
* coverage logic;
* semantic/content-sufficiency checks where supported by documentation.

---

## Phase 6 — Regression Analysis

Add support for comparing:

* the current build;
* the immediately previous build;
* optionally a selected known-good baseline.

The first example run does not need a baseline if an appropriate previous build has not yet been configured.

---

## Phase 7 — Test the Pipeline Using the Provided Gameplay Log

After implementing the core system, actually run the pipeline using the gameplay log file(s) under:

```text
playthrough-logs-and-results/08-25-26
```

Do not merely state that the code should work.

Use this dataset to verify that the pipeline successfully performs tasks such as:

* reading and normalizing the log;
* discovering all event types;
* counting event frequencies;
* extracting unique `sceneName` values;
* recursively profiling `data`;
* identifying unique categorical values;
* calculating timestamp/frequency information;
* generating scene-level timelines;
* detecting missing/inconsistent fields;
* detecting duplicate or suspicious records;
* applying available expectation rules;
* generating supporting CSV/JSON outputs;
* generating the Markdown audit report.

When the output reveals something unexpected, inspect the source records and determine whether the behavior reflects:

* a logging problem;
* incomplete gameplay coverage;
* an unclear specification;
* an expected gameplay behavior;
* or simply an informative observation.

Do not alter the raw data in order to make tests pass.

---

## Phase 8 — Validate the Generated Results

Manually inspect several results from the `08-25-26` example to verify that the automated outputs correspond to the underlying JSON records.

At minimum, validate examples from several different types of events, preferably including:

* a high-frequency event;
* an interaction event;
* an event containing categorical `data` fields;
* an event with meaningful temporal ordering;
* an event with a known logging specification.

Cross-check representative findings against the raw records.

The goal is to verify not only that the scripts execute successfully, but that the audit logic produces meaningful and trustworthy results.

---

## Phase 9 — Demonstrate How I Should Use the Pipeline

After the example audit is complete, provide a practical walkthrough using:

```text
playthrough-logs-and-results/08-25-26
```

as the example.

Show me the actual workflow I would follow each week.

For example, explain:

1. where I should place or identify the new gameplay log;
2. whether I need to create/update a coverage manifest;
3. how I specify the new build ID;
4. how I select a previous build as the baseline;
5. what command I run;
6. which outputs I should inspect first;
7. where the detailed event-level findings are stored;
8. how I add or modify an expectation when an event design changes;
9. how I interpret `PASS`, `WARNING`, `FAIL`, `INFO`, and `NOT_TESTED`;
10. how I compare this week's build with last week's build.

Where useful, provide concrete commands based on the `08-25-26` example rather than only giving abstract instructions.

For example, the demonstrated command might eventually resemble:

```bash
python gameplay-logs-test/scripts/audit_logs.py \
    --input playthrough-logs-and-results/08-25-26 \
    --build-id "08-25-26" \
    --config gameplay-logs-test/config/event_expectations.yaml \
    --output gameplay-logs-test/reports/08-25-26
```

This is only an example.

Use the actual CLI structure you implement.

---

## Phase 10 — Documentation

Create a README for the recurring workflow.

The README should use the `08-25-26` log as an example so that I can follow the same steps with a future build.

Document both:

### First-time setup

How the audit system is configured and initialized.

### Weekly recurring usage

The minimal sequence needed when a new build arrives.

Ideally, the weekly workflow should require only something conceptually similar to:

```text
1. Add/select new log.
2. Update gameplay coverage.
3. Specify build ID and previous baseline.
4. Run one command.
5. Review generated report.
```

The system should minimize repetitive manual work.


---

# Very Important Reasoning Rules

While implementing this system:

1. **Do not equate absence with failure.**
   Always consider gameplay coverage.

2. **Do not assume historical specifications are current.**
   Check the latest documentation.

3. **Do not hard-code assumptions when they can be configuration rules.**

4. **Do not hide unexpected values.**
   Unexpected values are often exactly what I need to discover.

5. **Do not automatically normalize suspicious naming inconsistencies.**
   Report them before deciding whether they are equivalent.

6. **Do not evaluate every event using the same frequency assumptions.**
   Continuous telemetry and player-triggered interactions behave differently.

7. **Preserve raw evidence.**

8. **Make every important finding traceable back to the original log record.**

9. **When uncertain whether something is a logging defect or a specification issue, say so explicitly.**

10. **Prefer an interpretable QA pipeline over an unnecessarily complicated system.**

---

# Final Deliverables

After completing the work, provide:

1. a summary of the repository/logging structure you discovered;
2. the architecture of the audit system;
3. the implemented reusable Python scripts/modules;
4. the expectation/configuration files;
5. the gameplay coverage mechanism;
6. regression-comparison functionality;
7. automated Markdown report generation;
8. CSV/JSON supporting exports;
9. tests;
10. README instructions;
11. **a completed example audit run using the gameplay log file(s) in `playthrough-logs-and-results/08-25-26`;**
12. **the generated outputs from that example run, preferably saved under `gameplay-logs-test/reports/08-25-26`;**
13. **a practical step-by-step demonstration of how I would repeat the same process when next week's game build arrives;**
14. **example commands using the actual CLI that you implement;**
15. a short explanation of how I can update the configuration when developers add or modify event types.

If appropriate for the repository structure, keep the implementation, configuration, tests, documentation, and generated example outputs organized under:

```text
gameplay-logs-test/
```

Most importantly, do not stop after writing the scripts. **Run and validate the pipeline using the provided `08-25-26` gameplay log so that we know the workflow actually works on real MHS gameplay data.**