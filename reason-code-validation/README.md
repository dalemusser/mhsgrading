# Reason-Code Validation (`reason-code-validation/`)

Validates the **reason-code scripts** behind the dashboard pop-up messages:
given a controlled gameplay-log fixture, does each progress point's
"Corresponding Script" trigger the right reason code(s), return the right
message variables, and render an instructor message that agrees with the
cell color?

```text
gameplay-log fixture  +  expected codes/variables     (config/expectations.yaml)
        ↓
reason-code execution                                 (rc_uXpY.py — 1:1 transcriptions
        ↓                                              of each "Corresponding Script")
triggered codes + variables  →  rendered Instructor Message
        ↓
checks: expected codes/variables · pop-up ↔ cell consistency · message placeholders
        ↓
pass/fail table + rendered messages                   (terminal + outputs/<fixture>/)
```

**How this differs from the other features:**
[rubric-validation/](../rubric-validation/) validates the *color* each point
gets (the "Production Script"); this suite validates the *explanation* shown
when that color is yellow (the "Reason Codes" section of the same grading
markdown: which code fires, with which numbers, saying what). It imports the
color graders and the Mongo-like harness from `rubric-validation/` read-only
and never modifies them. [grading-readiness-audit/](../grading-readiness-audit/)
and [build-log-qa/](../build-log-qa/) are unchanged and unaware of this folder.

## Layout

| File | Purpose |
|------|---------|
| `run_all.py` | **Entry point.** Runs all 26 points against a fixture, prints the table + every triggered code's rendered instructor message, writes `outputs/<run-id>/`. |
| `config/expectations.yaml` | Fixture manifest: log path, expected triggered codes and variable values per point, provenance. Single source of truth for expected results. |
| `rc_common.py` | Path bootstrap (imports `mhs_harness` + `test_uXpY` from `../rubric-validation/`), query helpers, Reason-Codes markdown parser, message rendering, the per-point evaluation with all checks, report/printing helpers. |
| `rc_uXpY.py` | One per progress point (26; U1P1/U1P2/U1P4 declare no codes). Defines `META`, `attempt_window(coll, pid)` and one function per reason code returning `{"triggered": bool, <variable>: value, ...}` — a 1:1 transcription of the markdown's Corresponding Script. `CODES` maps code name → function in markdown order. |
| `outputs/<run-id>/` | Generated `results.md` (table, check failures, rendered messages, every code's variables) and `results.json`. Safe to delete and regenerate; `adhoc-*` runs are gitignored. |

## Running

Requires Python 3.10+ with `pyyaml`; nothing else.

```bash
cd reason-code-validation
python run_all.py                        # default fixture (09-03-26-3)
python run_all.py --fixture 09-03-26-4   # another fixture from the manifest
python run_all.py --all-codes            # also show codes that did NOT trigger (with their variables)
python run_all.py --quiet                # table only
python run_all.py --log PATH.json        # ad-hoc: any dump — no expected codes, but the
                                         # structural checks below still pass/fail
python run_all.py --no-report            # skip writing outputs/<run-id>/
python rc_u4p4.py                        # one point vs the default fixture (exit 0 = all checks pass)
```

Exit code is 1 if any check fails on any point.

## What is checked, per point

| Check | Meaning | Fails when |
|-------|---------|-----------|
| `code-set` | The module transcribes exactly the `### CODE` headings under `## Reason Codes` in the grading markdown. | A code was added/renamed in the markdown but not here (or vice versa). |
| `placeholders:<CODE>` | Every `{variable}` in the Instructor Message is a key of the script's return object. | Message and script drifted apart — the pop-up would show a raw `{placeholder}`. |
| `color-consistency` | Pop-up ↔ cell: with a valid attempt window, a **yellow** cell (per `rubric-validation/test_uXpY.grade()`) triggers ≥ 1 code and a **green** cell triggers none. With **no window** (point not reached / truncated), no code may trigger — the dashboard shows the pencil/white state, not a pop-up. | A yellow cell would open an empty pop-up, or a green cell would carry a reason. |
| `expected-codes` | The triggered set equals the fixture's `codes`. | Fixture mode only. |
| `expected-variables:<CODE>` | Each variable listed in the fixture equals the script's value (exact). | Fixture mode only. |

The Instructor Message text and Teacher Guidance are **read from the grading
markdown at run time**, not copied into the modules — so the markdown stays the
single source of truth for wording, and this suite catches message/script
drift the moment either side changes.

## Fixtures

| Fixture | Role |
|---------|------|
| `09-03-26-3` (default) | Deliberately imperfect run, 20 yellow points — exercises 20 of the 29 codes' *triggered* paths (one code per yellow point) with cross-checked variable values. |
| `09-03-26-2` | Clean run, all green — the negative control: no code may fire. |
| `09-03-26-4` | U2P1/U2P2/U2P3 yellows (incl. the exactly-6-reminders U2P3 case) plus a truncated Unit 5: production yellow **without** a window → no code, no pop-up. |
| `08-31-26` | Previous build; U1P3 yellow only. |

All four pass 26/26 as of 2026-09-13. The 9 code paths no fixture triggers
(EXCESS_ATTEMPTS at U2P1/U2P4/U3P4/U4P2/U5P1, SOLVED_WITH_ASSIST at U3P4, and
the U2P3/U2P6 salinity/both-options branches) are verified only by line-level
transcription — add a fixture when a playthrough reaches them.

### Adding a fixture for a new build

1. Drop the dump under `playthrough-logs-and-results/<build-id>/` (shared with
   the other features; nothing is copied here).
2. Run ad-hoc: `python run_all.py --log ../playthrough-logs-and-results/<build-id>/<dump>.json --all-codes`.
   The structural checks already tell you whether the scripts are internally
   consistent with the colors.
3. Establish expected codes and variables **independently** — the tester's
   declared intent ("I took DANI's assist after 4 wrong tries") and/or raw
   event-key counts inside the window — and add the entry to
   `config/expectations.yaml` with a `provenance` note. Do not paste the ad-hoc
   output back in as the expectation.

## Updating for a grading-logic change

When a `## Reason Codes` section changes (new code, new key list, new
threshold, reworded message with new `{variables}`), edit the matching
`rc_uXpY.py` to mirror the Corresponding Script, then re-run. Several scripts
deliberately mirror color-rule quirks that are **flagged for review** in the
markdown (U3P3 counts success node 84:36 in the color sum, U4P4 lists 107:4 as a
success key, U5P2 ignores DualChamber_* interactions, U3P5 uses the production
`< 2.5` rather than the rule table's `>= 3`); when a sign-off lands, change the
markdown script and the transcription together, and expect fixture variables to
move accordingly.

If a color script's window changes, its reason scripts (and these
transcriptions) must follow — the `color-consistency` check is what catches a
pop-up that no longer agrees with its cell.
