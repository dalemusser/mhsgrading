# Rubric Validation (`rubric-validation/`)

Validates the **rubric/scoring implementations** behind the 26 dashboard
progress points: given a controlled gameplay-log fixture with known expected
results, does each point's production grading logic produce the expected
dashboard color (green/yellow)?

```text
gameplay-log fixture  +  expected colors     (config/fixtures.yaml)
        ↓
rubric execution                             (test_uXpY.py — 1:1 transcriptions
        ↓                                     of each "Production Script")
actual color  vs  expected color
        ↓
pass/fail table + reason-code diagnostics    (terminal + outputs/<fixture>/)
```

**How this differs from the other two features:** [build-log-qa/](../build-log-qa/)
QAs what a build's *logging* actually captured (developer-facing);
[grading-readiness-audit/](../grading-readiness-audit/) audits whether a new
build's logs still *support* grading and derives expectations for it. This
suite assumes the fixture and its expected colors are already established and
regression-tests the *grading logic itself* — run it after editing a
`grading-logic/mhs-unitX-pointY-grading.md` production script or a test
module transcription.

## Layout

| File | Purpose |
|------|---------|
| `run_all.py` | **Entry point.** Runs all 26 points against a fixture, prints the pass/fail table + diagnostics, writes `outputs/<run-id>/`. |
| `config/fixtures.yaml` | Fixture manifest: log path, expected color per point, provenance. The single source of truth for expected results. |
| `mhs_harness.py` | In-memory, MongoDB-like query layer over the log dump (`find_one`/`find`/`count_documents`, `_id`/`timestamp` ranges, `$in`, `$regex`, sorting, dotted paths) plus fixture resolution. |
| `mhs_report.py` | Shared evaluation/printing helpers used by every test. |
| `test_uXpY.py` | One per grading point (26 total). Defines `META`, `grade(coll, pid)` (production color logic) and `diagnose(coll, pid)` (reason codes). Kept in sync with the "Production Script (Attempt-Based)" in the point's grading markdown. |
| `outputs/<run-id>/` | Generated results (`results.md`, `results.json`), one folder per fixture (or `adhoc-<name>/` for `--log` runs). Safe to delete and regenerate. |

Fixture logs themselves stay under
[playthrough-logs-and-results/](../playthrough-logs-and-results/) — the
manifest references them by repo-relative path; nothing is copied.

## Running

Requires Python 3.10+ with `pyyaml` (for the fixture manifest); no other
dependencies.

```bash
cd rubric-validation
python run_all.py                     # default fixture (see config/fixtures.yaml)
python run_all.py --fixture 08-31-26  # a specific fixture from the manifest
python run_all.py --quiet             # table only
python run_all.py --log PATH.json     # ad-hoc: grade any dump (informational —
                                      # no expected colors, no pass/fail)
python run_all.py --no-report         # skip writing outputs/<run-id>/
python test_u3p3.py                   # one point vs the default fixture
                                      # (exit 0 = matches expected color)
```

`run_all.py` exits non-zero if any point's production color differs from the
fixture's expected color. Results are also written to
`outputs/<fixture-id>/results.md` and `results.json` (the folder is created
automatically; re-running the same fixture overwrites its results, which is
intended — same code + same fixture should give the same result, and changes
show up as a git diff). Ad-hoc `--log` results go to `outputs/adhoc-<name>/`
(gitignored scratch).

## Fixtures and expected colors

Expected colors live **per fixture** in `config/fixtures.yaml`, not in the
test modules — the same rubric gives different colors on different
playthroughs. Current fixture:

* **`08-31-26`** (default) — full playthrough of the 08-31-26 build.
  Expected colors were established by the grading-readiness-audit run
  `08-31-26-run2`: U1P3 yellow, all other points green. 18 of the 26 were
  verified against an independent expectation; 8 (U2P2, U2P6, U3P4, U4P4,
  U5P1–U5P4) are reviewed regression baselines (the audit executed them
  without an independent cross-check).

Newer log exports identify the player via top-level `user_id` instead of
`playerId`; the loader detects this and copies `user_id` into `playerId` so
the production-script queries apply unchanged (the run banner shows when this
adaptation is active — the same declared adaptation the
grading-readiness-audit makes).

### Adding a fixture for a new build

1. Drop the log dump under `playthrough-logs-and-results/<build-id>/`.
2. Establish expected colors independently — normally by running the
   [grading-readiness-audit](../grading-readiness-audit/) on that build and
   reviewing its `grading-validation` output.
3. Add an entry to `config/fixtures.yaml` (log path, 26 expected colors,
   provenance note); update `default_fixture` if it should become the default.

### The historical 05-01-26 log

The suite's original fixture (round 1, 2026-06-02; results preserved in
[TEST_RESULTS.md](../playthrough-logs-and-results/05-01-26/TEST_RESULTS.md))
predates several grading-logic fixes, so it has no entry in the manifest —
its old expected colors describe an earlier rubric. Grading it ad-hoc with
the current rubric (`python run_all.py --log
../playthrough-logs-and-results/05-01-26/wenyi050126-1.stratalog.logdata.json`)
shows the fixes behaving as intended on the old data: U2P6 now green and U3P3
now yellow (the round-1 window-anchor bugs, fixed 2026-07-22), and U4P6
yellow (the pre-2026-08-31 script used an inverted box→soil map, so its old
"green" was an artifact of the inverted map).

## How the attempt window works

Most production scripts grade only the **latest attempt**: they find the latest
*trigger* event, the previous trigger (the attempt boundary), and count/inspect
the relevant event keys whose `_id` falls in `(prevTrigger, latestTrigger]`.
`mhs_harness.latest_trigger_window()` implements this shared pattern; points
with distinct start/end anchors (e.g. U2P2, U2P6, U4P6, U5P1) inline their own
window, and U4P1/U4P2 anchor on the Unit-4 soil-key-puzzle close (an
eventType + data match, exposed to the audit via `attempt_window()`).

ObjectId ordering is reproduced via lexicographic comparison of the 24-char hex
`_id` strings, which matches both MongoDB's byte ordering and generation/arrival
time — so the windowing matches production exactly.

## Updating for a new build / grading change

When a grading markdown's "Production Script (Attempt-Based)" changes, edit
that point's `grade()`/`diagnose()` to match (the modules were last re-synced
with the markdowns on 2026-09-02 — including the 2026-07-22 U2P6/U3P3
window fixes and the 2026-08-31/09-01 updates to U1P3, U2P2, U2P5, U2P7,
U4P1, U4P2, U4P6). Then re-run `python run_all.py`: an expected color that
legitimately changes belongs in `config/fixtures.yaml`, with the reasoning
recorded in the fixture's provenance note.

The grading-readiness-audit imports `mhs_harness` and the 26 modules directly
(config key `tests_dir`) as its Stage-2 executor — keep module/function names
stable or update that pipeline together with this one.
