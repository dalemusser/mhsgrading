# mhsgrading

Grading in Mission HydroSci for use by mhsgrader.

## Repository layout

| Folder | Contents |
| ------ | -------- |
| [grading-logic/](grading-logic/) | The dashboard color-grading logic for every unit and progress point (see index below), plus [Reason-codes-and-instructor-messages.md](grading-logic/Reason-codes-and-instructor-messages.md), [mhs-unit-start.md](grading-logic/mhs-unit-start.md), and [original-score-rubric-table-and-dialogue-database/](grading-logic/original-score-rubric-table-and-dialogue-database/) — the assessment source documents (EA working doc, Progress-Points spec) and the dialogue databases (ID↔text map, Unity dialogue export) used to resolve `DialogueNodeEvent` keys. |
| [feedback-message-for-each-pp/](feedback-message-for-each-pp/) | Source material and outputs for per-progress-point pop-up feedback: assessment score rubrics, curriculum goals, potential strategies, context dialogue (docx), game narrative combo docs, and example pop-up feedback (e.g. [yellow-pp-teacher-feedback-units1-2.md](feedback-message-for-each-pp/example-pop-up-feedback/yellow-pp-teacher-feedback-units1-2.md)). |
| [rubric-validation/](rubric-validation/) | Rubric/scoring validation suite for the 26 point-grading scripts — one `test_uXpY.py` per point, a MongoDB-like harness, a fixture manifest with expected colors, and an aggregate runner. See [rubric-validation/README.md](rubric-validation/README.md). |
| [playthrough-logs-and-results/](playthrough-logs-and-results/) | Captured gameplay log dumps and their results, organized by playthrough date (`05-01-26/` … `08-31-26/`). [08-13-26/Investigation-results/](playthrough-logs-and-results/08-13-26/Investigation-results/) holds the de facto per-event-type log-format specifications (position, puzzle, quest, argumentation, chat, etc.). |
| [build-log-qa/](build-log-qa/) | Weekly build-log QA pipeline (event-level): config-driven expectation checks, frequency/sequence/duplicate analysis, build-vs-build regression, and auto-generated audit reports. See [build-log-qa/README.md](build-log-qa/README.md). |
| [grading-readiness-audit/](grading-readiness-audit/) | Two-stage grading-readiness pipeline (grading-level): Stage 1 checks whether a build's logs still provide the evidence each grading rule needs; Stage 2 executes the production grading logic and validates the resulting colors. Per-run results under `outputs/<run>/` and `reports/<run>/` (`08-25-26`, `08-31-26`, `08-31-26-run2`), each with an `audit-summary.md`, per-point reports, and a run-vs-run comparison doc. See [grading-readiness-audit/README.md](grading-readiness-audit/README.md). |
| [prompts/](prompts/) | Task prompts that produced the major work products: initial grading logic, adaptive feedback, the gameplay-log QA pipeline ([gamelog-test-1.md](prompts/gamelog-test-1.md)), and the progress-point audit pipeline ([gameplay-logs-pp-audit.md](prompts/gameplay-logs-pp-audit.md)). |
| [docs/](docs/) | Project notes — [issues_and_updates.md](docs/issues_and_updates.md). |

## The three gameplay-log analysis features

Three pipelines look at gameplay logs, each answering a different question —
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
      └── rubric-validation/       — Rubric Validation
            → Given a known gameplay-log fixture, does the grading logic
              produce the expected result/color for every progress point?
```

| Feature | Use it when | Input | Primary output | Command |
| ------- | ----------- | ----- | -------------- | ------- |
| [build-log-qa/](build-log-qa/) | A new weekly build's logs arrive and you want logging QA for the dev team | log dump folder + coverage manifest | `build-log-qa/reports/<build-id>/audit-report.md` (+ CSV/JSON evidence) | `python build-log-qa/scripts/audit_logs.py --input … --build-id …` |
| [grading-readiness-audit/](grading-readiness-audit/) | You need to know whether that build can still be graded correctly | log dump folder + coverage manifest + grading markdowns | `grading-readiness-audit/reports/<run>/audit-summary.md` (+ per-point reports) | `python grading-readiness-audit/scripts/run_audit.py …` |
| [rubric-validation/](rubric-validation/) | Grading logic (or a test transcription) changed and you want to regression-test it | fixture from `rubric-validation/config/fixtures.yaml` | pass/fail table + `rubric-validation/outputs/<fixture>/results.md` | `cd rubric-validation && python run_all.py` |

Each feature's README covers inputs, configuration, outputs, and examples.
Python dependencies for all three: `pip install -r requirements.txt`.

## Where to find what

- **How a progress point is graded** (rule, attempt window, event keys, production script, reason codes): `grading-logic/mhs-unitX-pointY-grading.md` — index below.
- **What the rubric originally intended / what a dialogue ID says**: [grading-logic/original-score-rubric-table-and-dialogue-database/](grading-logic/original-score-rubric-table-and-dialogue-database/).
- **Whether the latest build's logs still support the grading and whether the colors come out right**: newest run under [grading-readiness-audit/reports/](grading-readiness-audit/reports/) — start with `audit-summary.md`, then the per-point `progress-points/uXpY.md`, then the `comparison-to-<prev>.md` for what changed between builds.
- **Whether the build's logging itself is healthy** (event schemas, frequencies, duplicates, regressions): newest report under [build-log-qa/reports/](build-log-qa/reports/).
- **What a log record/event type means**: [playthrough-logs-and-results/08-13-26/Investigation-results/](playthrough-logs-and-results/08-13-26/Investigation-results/) and `build-log-qa/config/event_expectations.yaml`.
- **Teacher-facing feedback text for yellow points**: [feedback-message-for-each-pp/example-pop-up-feedback/](feedback-message-for-each-pp/example-pop-up-feedback/).

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
