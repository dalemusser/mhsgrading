# mhsgrading

Grading in Mission HydroSci for use by mhsgrader.

## Repository layout

| Folder | Contents |
| ------ | -------- |
| [grading-logic/](grading-logic/) | The dashboard color-grading logic for every unit and progress point (see index below), plus [Reason-codes-and-instructor-messages.md](grading-logic/Reason-codes-and-instructor-messages.md), [mhs-unit-start.md](grading-logic/mhs-unit-start.md), and [original-score-rubric-table-and-dialogue-database/](grading-logic/original-score-rubric-table-and-dialogue-database/) — the assessment source documents (EA working doc, Progress-Points spec) and the dialogue databases (ID↔text map, Unity dialogue export) used to resolve `DialogueNodeEvent` keys. |
| [feedback-message-for-each-pp/](feedback-message-for-each-pp/) | Context and outputs for the teacher-facing feedback behind yellow cells. Four folders hold one `unitX-pp-Y.md` per graded point (U1P3, U2P1–7, U3P1–5, U4P1–6, U5P1–4 — 23 files each): [assessment-score-rubric-for-each-pp/](feedback-message-for-each-pp/assessment-score-rubric-for-each-pp/) (narrative rendering of each row of the EA working-doc score table), [curriculum-goal-for-each-pp/](feedback-message-for-each-pp/curriculum-goal-for-each-pp/), [potential-strategy-for-each-pp/](feedback-message-for-each-pp/potential-strategy-for-each-pp/), and [context-dialogue-for-each-pp/](feedback-message-for-each-pp/context-dialogue-for-each-pp/) (per-unit subfolders with the dialogue each point depends on). [game-combo-doc/](feedback-message-for-each-pp/game-combo-doc/) has the five unit narrative combo docs. [example-pop-up-feedback/](feedback-message-for-each-pp/example-pop-up-feedback/) holds the finished examples — see "Generating teacher feedback for yellow points" below. |
| [rubric-validation/](rubric-validation/) | Rubric/scoring validation suite for the 26 point-grading scripts — one `test_uXpY.py` per point, a MongoDB-like harness, a fixture manifest with expected colors, and an aggregate runner. See [rubric-validation/README.md](rubric-validation/README.md). |
| [reason-code-validation/](reason-code-validation/) | Reason-code validation suite for the pop-up messages behind yellow points — one `rc_uXpY.py` per point transcribing the markdown's "Corresponding Script", a fixture manifest with expected triggered codes + message variables, and a runner that renders every instructor message and checks it agrees with the cell color. Writes `outputs/<fixture>/results.md` and `results.json` (per point: color, window, triggered codes, variables, rendered message — the machine-readable input for feedback generation). See [reason-code-validation/README.md](reason-code-validation/README.md). |
| [playthrough-logs-and-results/](playthrough-logs-and-results/) | Captured gameplay log dumps and their results, organized by playthrough date (`05-01-26/` … `09-03-26-4/`; a `-N` suffix distinguishes several sessions of the same build, e.g. `09-03-26-2/-3/-4`). [08-13-26/Investigation-results/](playthrough-logs-and-results/08-13-26/Investigation-results/) holds the de facto per-event-type log-format specifications (position, puzzle, quest, argumentation, chat, etc.). |
| [build-log-qa/](build-log-qa/) | Weekly build-log QA pipeline (event-level): config-driven expectation checks, frequency/sequence/duplicate analysis, build-vs-build regression, and auto-generated audit reports. See [build-log-qa/README.md](build-log-qa/README.md). |
| [grading-readiness-audit/](grading-readiness-audit/) | Two-stage grading-readiness pipeline (grading-level): Stage 1 checks whether a build's logs still provide the evidence each grading rule needs; Stage 2 executes the production grading logic and validates the resulting colors. Per-run results under `outputs/<run>/` and `reports/<run>/` (`08-25-26`, `08-31-26`, `08-31-26-run2`, `09-03-26-2`, `09-03-26-3`, `09-03-26-4`), each with an `audit-summary.md`, per-point reports, and a run-vs-run comparison doc. See [grading-readiness-audit/README.md](grading-readiness-audit/README.md). |
| [prompts/](prompts/) | Task prompts that produced the major work products: initial grading logic, the teacher-feedback task spec ([adaptive-feedback-1.md](prompts/adaptive-feedback-1.md) — what a yellow-cell pop-up must cover and which folders are evidence), the gameplay-log QA pipeline ([gamelog-test-1.md](prompts/gamelog-test-1.md)), and the progress-point audit pipeline ([gameplay-logs-pp-audit.md](prompts/gameplay-logs-pp-audit.md)). |
| [docs/](docs/) | Project notes — [issues_and_updates.md](docs/issues_and_updates.md). |

## The four gameplay-log analysis features

Four pipelines look at gameplay logs, each answering a different question —
they stay separate on purpose:

```text
Gameplay build (weekly log dump in playthrough-logs-and-results/<MM-DD-YY>/)
      │
      ├── build-log-qa/            — Build Log QA
      │     → What events did this build actually generate, and are there
      │       logging-implementation problems to report to the developers?
      │
      ├── grading-readiness-audit/ — Grading Readiness Audit
      │     → Does this build still emit the events/data each progress-point
      │       rubric depends on, and do the computed colors hold up?
      │
      ├── rubric-validation/       — Rubric Validation
      │     → Given a known gameplay-log fixture, does the grading logic
      │       produce the expected result/color for every progress point?
      │
      └── reason-code-validation/  — Reason-Code Validation
            → For the same fixture, does each yellow point trigger the right
              reason code(s), with the right message variables, and does the
              rendered instructor message agree with the cell color?
```

| Feature | Use it when | Input | Primary output | Command |
| ------- | ----------- | ----- | -------------- | ------- |
| [build-log-qa/](build-log-qa/) | A new weekly build's logs arrive and you want logging QA for the dev team | log dump folder + coverage manifest | `build-log-qa/reports/<build-id>/audit-report.md` (+ CSV/JSON evidence) | `python build-log-qa/scripts/audit_logs.py --input … --build-id …` |
| [grading-readiness-audit/](grading-readiness-audit/) | You need to know whether that build can still be graded correctly | log dump folder + coverage manifest + grading markdowns | `grading-readiness-audit/reports/<run>/audit-summary.md` (+ per-point reports) | `python grading-readiness-audit/scripts/run_audit.py …` |
| [rubric-validation/](rubric-validation/) | Grading logic (or a test transcription) changed and you want to regression-test it | fixture from `rubric-validation/config/fixtures.yaml` | pass/fail table + `rubric-validation/outputs/<fixture>/results.md` | `cd rubric-validation && python run_all.py` |
| [reason-code-validation/](reason-code-validation/) | A Reason Codes section (script, key list, threshold, or message wording) changed and you want to see every pop-up message it now produces, checked against the cell colors | fixture from `reason-code-validation/config/expectations.yaml` | pass/fail table + rendered instructor messages + `reason-code-validation/outputs/<fixture>/results.md` | `cd reason-code-validation && python run_all.py` |

Each feature's README covers inputs, configuration, outputs, and examples.
Python dependencies for all four: `pip install -r requirements.txt`.

A fifth, document-only workflow builds on the last two: the teacher-facing
feedback for yellow points (no code yet — the reason-code results plus the
per-point context folders are its inputs; see
"Generating teacher feedback for yellow points" below).

## Where to find what

- **How a progress point is graded** (rule, attempt window, event keys, production script, reason codes): `grading-logic/mhs-unitX-pointY-grading.md` — index below.
- **What the rubric originally intended / what a dialogue ID says**: [grading-logic/original-score-rubric-table-and-dialogue-database/](grading-logic/original-score-rubric-table-and-dialogue-database/).
- **Whether the latest build's logs still support the grading and whether the colors come out right**: newest run under [grading-readiness-audit/reports/](grading-readiness-audit/reports/) — start with `audit-summary.md`, then the per-point `progress-points/uXpY.md`, then the `comparison-to-<prev>.md` for what changed between builds.
- **Whether the build's logging itself is healthy** (event schemas, frequencies, duplicates, regressions): newest report under [build-log-qa/reports/](build-log-qa/reports/).
- **What a log record/event type means**: [playthrough-logs-and-results/08-13-26/Investigation-results/](playthrough-logs-and-results/08-13-26/Investigation-results/) and `build-log-qa/config/event_expectations.yaml`.
- **Which reason code a yellow point fired, with what numbers and wording**: `reason-code-validation/outputs/<fixture>/results.md` (human) / `results.json` (machine).
- **Everything needed to explain one point to a teacher** (rubric, curriculum goal, strategies, the dialogue involved): the `unitX-pp-Y.md` file of that point in each [feedback-message-for-each-pp/](feedback-message-for-each-pp/) subfolder, plus the point's grading markdown.
- **Teacher-facing feedback text for yellow points**: [feedback-message-for-each-pp/example-pop-up-feedback/](feedback-message-for-each-pp/example-pop-up-feedback/) — full evidence form and pop-up-only form, see below.

## Grading logic by unit

- [Unit 1 - Get Your Space Legs](grading-logic/mhs-unit1-grading.md)
  - [Point 1 - Getting Your Space Legs](grading-logic/mhs-unit1-point1-grading.md)
  - [Point 2 - Info and Intros](grading-logic/mhs-unit1-point2-grading.md)
  - [Point 3 - Defend the Expedition](grading-logic/mhs-unit1-point3-grading.md)
  - [Point 4 - What Was That?](grading-logic/mhs-unit1-point4-grading.md)
- [Unit 2 - Find the Flow](grading-logic/mhs-unit2-grading.md)
  - [Point 1 - Escape the Ruin](grading-logic/mhs-unit2-point1-grading.md)
  - [Point 2 - Foraged Forging](grading-logic/mhs-unit2-point2-grading.md)
  - [Point 3 - Getting the Band Back Together Part II](grading-logic/mhs-unit2-point3-grading.md)
  - [Point 4 - Investigate the Temple](grading-logic/mhs-unit2-point4-grading.md)
  - [Point 5 - Classified Information](grading-logic/mhs-unit2-point5-grading.md)
  - [Point 6 - Which Watershed? Part I](grading-logic/mhs-unit2-point6-grading.md)
  - [Point 7 - Which Watershed? Part II](grading-logic/mhs-unit2-point7-grading.md)
- [Unit 3 - Clean the Stream](grading-logic/mhs-unit3-grading.md)
  - [Point 1 - Good Morning Cadet + Establishing a Foothold](grading-logic/mhs-unit3-point1-grading.md)
  - [Point 2 - Pollution Solution](grading-logic/mhs-unit3-point2-grading.md)
  - [Point 3 - Pollution Argument](grading-logic/mhs-unit3-point3-grading.md)
  - [Point 4 - Forsaken Facility](grading-logic/mhs-unit3-point4-grading.md)
  - [Point 5 - Plant the Superfruit Seeds](grading-logic/mhs-unit3-point5-grading.md)
- [Unit 4 - Dig Deeper](grading-logic/mhs-unit4-grading.md)
  - [Point 1 - Well What Have We Here?](grading-logic/mhs-unit4-point1-grading.md)
  - [Point 2 - Power Play- Floors 1 & 2](grading-logic/mhs-unit4-point2-grading.md)
  - [Point 3 - Power Play- Floors 3 & 4](grading-logic/mhs-unit4-point3-grading.md)
  - [Point 4 - Power Play- Floor 5](grading-logic/mhs-unit4-point4-grading.md)
  - [Point 5 - Saving Cadet Anderson](grading-logic/mhs-unit4-point5-grading.md)
  - [Point 6 - Desert Delicacies](grading-logic/mhs-unit4-point6-grading.md)
- [Unit 5 - Rise and Return](grading-logic/mhs-unit5-grading.md)
  - [Point 1 - If I Had a Nickel- Floors 1 & 2](grading-logic/mhs-unit5-point1-grading.md)
  - [Point 2 - If I Had a Nickel- Floors 3 & 4](grading-logic/mhs-unit5-point2-grading.md)
  - [Point 3 - What Happened Here?](grading-logic/mhs-unit5-point3-grading.md)
  - [Point 4 - Water Problems Require Water Solutions](grading-logic/mhs-unit5-point4-grading.md)

## Validating the grading logic

Quick regression check of the 26 point-grading scripts against the verified
fixture (expected colors in `rubric-validation/config/fixtures.yaml`):

```bash
cd rubric-validation
python run_all.py                 # full table + diagnostics
python run_all.py --log PATH.json # grade an arbitrary dump (informational)
```

Details in [rubric-validation/README.md](rubric-validation/README.md). The
test modules were re-synced with the grading markdowns on 2026-09-02; keep
them in sync when a "Production Script" changes.

The same check for the **reason codes** (which pop-up fires for a yellow
point, with which numbers, saying what — expectations in
`reason-code-validation/config/expectations.yaml`):

```bash
cd reason-code-validation
python run_all.py                 # table + every triggered code's rendered message
python run_all.py --all-codes     # also the codes that did not trigger, with their variables
python run_all.py --log PATH.json # any dump: pop-up/cell consistency + placeholder checks only
```

Details in [reason-code-validation/README.md](reason-code-validation/README.md);
keep an `rc_uXpY.py` in sync when its "Corresponding Script" changes.

## Generating teacher feedback for yellow points

When a teacher opens a yellow cell, the dashboard shows the reason-code pop-up
(the Instructor Message validated above). A button inside that pop-up then
shows an AI-summarized paragraph about the player's performance. The task
spec is [prompts/adaptive-feedback-1.md](prompts/adaptive-feedback-1.md);
the inputs for one point are:

```text
reason-code-validation/outputs/<fixture>/results.json   which code fired, variables, message
grading-logic/mhs-unitX-pointY-grading.md               the yellow trigger + attempt window
feedback-message-for-each-pp/
    assessment-score-rubric-for-each-pp/unitX-pp-Y.md   what the rubric scores
    curriculum-goal-for-each-pp/unitX-pp-Y.md           the learning goal the point targets
    potential-strategy-for-each-pp/unitX-pp-Y.md        in-game supports the player could use
    context-dialogue-for-each-pp/unitX/unitX-pp-Y.md    the dialogue the point depends on
    game-combo-doc/LIVE Unit X Narrative Combo Doc.md   task sequence and storyline
playthrough-logs-and-results/<run>/…logdata.json        evidence, read inside the attempt window
```

The finished examples in
[feedback-message-for-each-pp/example-pop-up-feedback/](feedback-message-for-each-pp/example-pop-up-feedback/)
come in two forms and are kept in sync:

| File | Form | Covers |
| ---- | ---- | ------ |
| [yellow-pp-teacher-feedback-units1-5-090326-3.md](feedback-message-for-each-pp/example-pop-up-feedback/yellow-pp-teacher-feedback-units1-5-090326-3.md) | Full evidence form — per point: yellow trigger, performance summary, gameplay evidence, learning need, underused support, suggested intervention, pop-up text; plus a summary table and verification notes | all 20 yellow points of run `09-03-26-3` |
| [yellow-pp-ai-summarized-pop-up-text-units1-5-090326-3.md](feedback-message-for-each-pp/example-pop-up-feedback/yellow-pp-ai-summarized-pop-up-text-units1-5-090326-3.md) | Teacher view — only the point title and the pop-up paragraph (80–150 words) the dashboard displays | same 20 points |
| [yellow-pp-teacher-feedback-units1-2.md](feedback-message-for-each-pp/example-pop-up-feedback/yellow-pp-teacher-feedback-units1-2.md) | First example, full form | U1P3, U2P2, U2P7 of run `05-01-26` |

Rules the examples follow: definitive wording only for facts the log records
(attempt counts, submissions, tool opens); cautious wording for anything the
log cannot show (videos watched, hover text read); documentation
inconsistencies are reported in the verification notes, not silently
resolved.

## Auditing a new build end-to-end

For each new weekly build/playthrough, run both pipelines (write the coverage
manifest under `build-log-qa/config/coverage/` first):

```bash
# 1. Event-level log QA (schemas, frequencies, anomalies, build regression)
python build-log-qa/scripts/audit_logs.py \
    --input playthrough-logs-and-results/<MM-DD-YY> \
    --build-id <MM-DD-YY> \
    --baseline build-log-qa/reports/<previous-build>
# 2. Progress-point grading-readiness audit (log support + color validation)
python grading-readiness-audit/scripts/run_audit.py \
    --log-dir playthrough-logs-and-results/<MM-DD-YY> \
    --build-label <MM-DD-YY> \
    --coverage-yaml build-log-qa/config/coverage/<MM-DD-YY>.yaml \
    --outputs-dir outputs/<MM-DD-YY> \
    --reports-dir reports/<MM-DD-YY>
```

Results land in `build-log-qa/reports/<MM-DD-YY>/` and
`grading-readiness-audit/reports/<MM-DD-YY>/` — read each `audit-report.md` /
`audit-summary.md` first. Details in
[build-log-qa/README.md](build-log-qa/README.md) and
[grading-readiness-audit/README.md](grading-readiness-audit/README.md).
