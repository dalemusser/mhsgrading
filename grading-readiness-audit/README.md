# Grading Readiness Audit (`grading-readiness-audit/`)

A reusable pipeline that answers two sequential questions for each of the 26
Mission HydroSci dashboard progress points, against any gameplay-log dump:

1. **Stage 1 — log support**: does the current build still emit the events,
   event keys, dialogue markers, and payload fields the production grading
   logic depends on?
2. **Stage 2 — grading validation**: where the evidence exists, does the
   production grading logic turn it into a defensible progress-point color?

The two stages are deliberately separate: a wrong color can come from missing
logging, changed identifiers, changed game design, an outdated rubric
reference, or a grading bug — and the pipeline classifies which.

**How this differs from the other two features:**
[build-log-qa/](../build-log-qa/) QAs the build's logging implementation
event-by-event with no grading knowledge (developer-facing);
[rubric-validation/](../rubric-validation/) regression-tests the grading
logic against fixtures whose expected colors are already known. Run THIS
pipeline when a **new build/playthrough** arrives and you need to know
whether it can still be graded — its grading-validation output is also how
expected colors for new rubric-validation fixtures are established.

## Conceptual chain

For every progress point the audit reconstructs and tests this chain:

```
Assessment intent            (Progress-Points.docx, EA working doc)
  → required player behavior
  → expected gameplay evidence (event keys / event types / fields)
  → actual current log records (the dump under audit)
  → production grading logic   (grading-logic/mhs-unitX-pointY-grading.md,
                                "Production Script" section)
  → calculated score/state → dashboard color
```

## Folder structure

```
grading-readiness-audit/
├── README.md
├── config/
│   ├── audit-config.yaml          # paths + options (edit for a new build)
│   ├── audit-config.override.yaml # generated per-run by run_audit.py (gitignored)
│   └── dependency-semantics.yaml  # role → expectation-class mapping
├── scripts/                       # run in this order (or via run_audit.py)
│   ├── audit_lib.py               # shared helpers
│   ├── parse_grading_specs.py     # 1a: grading MDs → dependency spec
│   ├── parse_source_docs.py       # 1b: docx sources → assessment intent
│   ├── inventory_gameplay_logs.py # 2:  raw logs → event/key inventory
│   ├── reconcile_dialogues.py     # 3:  dialogue refs ↔ DBs ↔ logs
│   ├── audit_progress_points.py   # 4-6: dependency + PP support statuses
│   ├── run_grading_validation.py  # 7:  execute production logic + trace
│   ├── generate_reports.py        # 8:  summary + per-point reports
│   ├── validate_outputs.py        # consistency checks (exit 1 on failure)
│   └── run_audit.py               # orchestrator for all of the above
├── outputs/<run-label>/           # machine-readable results, one dir per run
│   ├── progress-point-dependencies.json
│   ├── source-doc-intent.json
│   ├── current-log-inventory.json
│   ├── eventkey-inventory.csv
│   ├── dialogue-reconciliation.json / .csv
│   ├── pp-log-support-audit.json / .csv
│   └── grading-validation.json / .csv
└── reports/<run-label>/           # one dir per run
    ├── audit-summary.md           # master table, findings, priorities
    ├── comparison-to-<prev>.md    # hand-written run-vs-run comparison
    └── progress-points/uXpY.md    # one detailed report per point
```

Run labels so far: `08-25-26` (first run; also holds the one-off
`phase0-repo-inventory.md` inspection notes and the docx `*.extracted.txt`
working files), `08-31-26`, `08-31-26-run2` (same logs re-audited after the
2026-09-01 grading-logic edits).

## Data sources

| Source | Used as |
|---|---|
| `grading-logic/mhs-unit*-point*-grading.md` | current production behavior (audited, **not** ground truth; never modified) |
| `.../Progress-Points.docx`, `.../MHS-2.0-Embedded-Assessment-Working-Doc.docx` | assessment intent; their technical IDs are treated as historical claims |
| `.../Dialogue-ID-Texts.xlsx` | (conversation, node) → text map (config key `dialogue_xlsx`); replaced on 2026-09-21 (commit 68417c8) to match build 20260914-, the previous copy is kept as `Dialogue-ID-Texts-Old.xlsx` for historical comparison only |
| `.../2026-09-21-MHSDialogueExport.csv` | Unity dialogue DB export matching that build (config key `dialogue_export_csv`; switched from the 2026-06-10 export on 2026-09-23 — runs up to `09-14-26-3` reconciled against the old xlsx + 2026-06-10 export; report wording takes the export date from the file name) |
| `playthrough-logs-and-results/<build>/*.json` | observational evidence from one playthrough |
| `build-log-qa/config/coverage/<build>.yaml` | which units the tester actually played (separates "not logged" from "not exercised") |
| `rubric-validation/test_uXpY.py` + `rubric-validation/mhs_harness.py` | 1:1 Python transcriptions of the production scripts, reused as the Stage-2 executor (config key `tests_dir`) |

## How to run

From the repository root (Python 3.13; needs `pyyaml`, `openpyxl`):

```
python grading-readiness-audit/scripts/run_audit.py
```

Phases can also be run individually in the order listed above; each phase
only reads the outputs of earlier phases.

### Pointing at a new build

```
python grading-readiness-audit/scripts/run_audit.py ^
    --log-dir playthrough-logs-and-results/09-08-26 ^
    --build-label 09-08-26 ^
    --coverage-yaml build-log-qa/config/coverage/09-08-26.yaml ^
    --outputs-dir outputs/09-08-26 ^
    --reports-dir reports/09-08-26
```

or edit `config/audit-config.yaml`. Write the coverage manifest for the new
playthrough first (see `build-log-qa/README.md`), otherwise the audit
cannot distinguish unexercised behavior from missing logging.

`--outputs-dir` / `--reports-dir` give each run its own directory so earlier
runs are preserved — every run (08-25-26 included, relocated 2026-09-01)
lives in its own dated subdirectory of `outputs/` and `reports/`. Without
them, outputs are overwritten in place.

## Status vocabulary

**Per dependency (Stage 1):** `SUPPORTED_EXACTLY`,
`SUPPORTED_WITH_SCHEMA_CHANGE`, `SUPPORTED_WITH_IDENTIFIER_CHANGE`,
`PARTIALLY_SUPPORTED`, `NOT_OBSERVED_IN_PLAYTHROUGH`,
`LIKELY_MISSING_FROM_CURRENT_LOGGING`, `AMBIGUOUS`, `NOT_REQUIRED`.

`NOT_OBSERVED_IN_PLAYTHROUGH` vs `LIKELY_MISSING…` is decided by behavioral
reachability (did the activity demonstrably happen?), the dependency's
expectation class (`config/dependency-semantics.yaml` — e.g. wrong-answer
feedback keys are *counted evidence* whose absence is normal good play), and
whether sibling evidence (same conversation/quest) fired.

**Per dialogue reference (Phase 3):** `EXACT_MATCH`,
`TEXT_MATCH_DIFFERENT_ID`, `ID_EXISTS_DIFFERENT_TEXT`,
`EXPECTED_DIALOGUE_NOT_OBSERVED`, `DIALOGUE_REMOVED_OR_CHANGED`, `AMBIGUOUS`,
`NOT_APPLICABLE`. Relocation candidates are reported, never auto-applied.

**Per progress point (Stage 1):** `READY_FOR_GRADING_TEST`,
`READY_WITH_MAPPING_UPDATE`, `PARTIALLY_AUDITABLE`, `BLOCKED_BY_LOGGING`,
`BLOCKED_BY_RUBRIC_AMBIGUITY`, `BLOCKED_BY_GAME_DESIGN_CHANGE`,
`NEEDS_MANUAL_REVIEW`.

**Per progress point (Stage 2):** `PASS`, `MISMATCH_NEEDS_REVIEW`,
`EXECUTED_NO_INDEPENDENT_CHECK`, `ERROR` — with the expected color derived
from completion evidence, a doc-marker-derived activity window, or a
documented special-case check; `expected_confidence` says how solid that
expectation is.

## Declared adaptations (never silent)

* Exports since 08-13-26 identify the player via top-level `user_id`;
  production scripts filter on `playerId`. Stage 2 translates the field and
  records the translation in `grading-validation.json`. Whether the live
  grading DB changed too must be confirmed with the dev team.
* The `rubric-validation/` modules were re-synced with the current grading
  markdown on 2026-09-02, retiring the audit-local `OVERRIDES` that earlier
  runs (through `08-31-26-run2`) carried for stale transcriptions — those
  runs' outputs label the affected executors "+ audit override". If a module
  goes stale again, re-sync it rather than reintroducing an override.

## Known limitations

* One playthrough is observational: yellow/failure paths that the tester
  never hit cannot be validated (`EXECUTED_NO_INDEPENDENT_CHECK`).
* The dialogue export predates the audited build by ~10 weeks; text-level
  verdicts are capped at MEDIUM confidence.
* `_id`-window semantics mirror production (arrival order), which can differ
  from client-timestamp order for ~2.6% of adjacent pairs (batched uploads).
* Debug-menu use during a playthrough taints affected intervals (flagged in
  the per-point reports where relevant).
