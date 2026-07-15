# MHS Dashboard Grading — Test Suite

Python tests for the color-determination logic behind each progress point on the
dashboard. There is **one test file per `mhs-unitX-pointY-grading.md`**, plus a
shared harness and an aggregate runner.

Each test transcribes that point's **"Production Script (Attempt-Based)"**
(MongoDB/JS, the code that decides green/yellow) into Python, runs it against a
captured gameplay log, and:

1. checks whether the production code returns the **expected dashboard color**;
2. when a point is yellow (or when production disagrees with the expected
   color), runs the point's **reason-code logic** to report *why* — e.g. a count
   over threshold, a missing success node, or a mis-anchored attempt window.

## Layout

| File | Purpose |
|------|---------|
| `mhs_harness.py` | In-memory, MongoDB-like query layer over the log dump (`find_one`/`find`/`count_documents`, `_id`/`timestamp` ranges, `$in`, sorting, dotted paths). Loads the JSON and normalizes `_id` to its hex string. |
| `mhs_report.py` | Shared assertion/printing helpers used by every test. |
| `test_uXpY.py` | One per grading point (26 total). Defines `META`, `grade(coll, pid)` (production color logic) and `diagnose(coll, pid)` (reason codes). |
| `run_all.py` | Runs all 26 in dashboard order, prints a table + diagnostics, and compares the full color sequence to the expected list. |
| `05-01-26/…json` | Example gameplay log this suite is validated against. |

## Running

```bash
cd tests
python run_all.py                 # full table + diagnostics
python run_all.py --quiet         # table only
python run_all.py --log PATH.json # validate a new weekly build's log dump
python test_u3p3.py               # run a single point (exit code 0=pass, 1=fail)
```

`run_all.py` exits non-zero if any point's production color differs from the
expected color.

## How the attempt window works

Most production scripts grade only the **latest attempt**: they find the latest
*trigger* event, the previous trigger (the attempt boundary), and count/inspect
the relevant event keys whose `_id` falls in `(prevTrigger, latestTrigger]`.
`mhs_harness.latest_trigger_window()` implements this shared pattern; points with
distinct start/end keys (e.g. U2P2, U4P1, U5P1) inline their own window.

ObjectId ordering is reproduced via lexicographic comparison of the 24-char hex
`_id` strings, which matches both MongoDB's byte ordering and generation/arrival
time — so the windowing matches production exactly.

## Current results (against `05-01-26`)

24 / 26 points match the expected dashboard colors. **Two mismatches**, both the
same class of defect — the production attempt-window is anchored on an event key
that does **not** bracket the graded activity, so the relevant log records fall
outside the window:

- **U2P6 — Which Watershed? Part I** (expected **green**, production **yellow**).
  The window ends on `DialogueNodeEvent:20:35`, which fires *before* the pass
  node `DialogueNodeEvent:20:43`. The pass node is excluded, so the script can't
  see the correct choice. The documented Trigger(End) is `DialogueNodeEvent:20:46`
  (which occurs after the pass node). **Fix:** anchor the window end on `20:46`.

- **U3P3 — Pollution Argument** (expected **yellow**, production **green**).
  The window is anchored on `questActiveEvent:18`, which fires *after* the whole
  argumentation activity. All 7 wrong-argument selections and the BackingInfoPanel
  use occur before it, so the windowed count is 0 → score 3 → green. The file's
  own documented window (`DialogueNodeEvent:11:34` → `questFinishEvent:18`)
  contains the activity and yields yellow. **Fix:** anchor the window on
  `11:34` / `questFinishEvent:18`, not `questActiveEvent:18`.

Run `python run_all.py` to see the full per-point diagnostics.

## Updating for a new build

When a new weekly build changes the color logic for a point, edit that point's
`grade()`/`diagnose()` to match the new "Production Script (Attempt-Based)" in
its grading markdown, update `META["expected"]` / the `POINTS` list in
`run_all.py` if the expected color changed, and re-run with the new log dump via
`--log`.
