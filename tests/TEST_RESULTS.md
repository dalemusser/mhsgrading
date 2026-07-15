# MHS Dashboard Grading — Test Results

**Date:** 2026-06-02
**Log dump tested:** `tests/05-01-26/wenyi050126-1.stratalog.logdata.json` (4,458 records, player `wenyi050126-1`)
**Suite:** one Python test per `mhs-unitX-pointY-grading.md`, run via `tests/run_all.py`

---

## Summary

**24 / 26 progress points match the expected dashboard color.**

Each test transcribes the point's **"Production Script (Attempt-Based)"** (the
MongoDB/JS code that decides green/yellow) 1:1 into Python, runs it against the
captured gameplay log through a faithful MongoDB-like query layer
(`mhs_harness.py`), and compares the result to the expected color. When a point
is yellow — or when production disagrees with the expected color — the point's
reason-code logic runs to report *why*.

```
Expected: Green, Green, Yellow, Green, Green, Yellow, Green, Green, Green, Green, Yellow,
          Green, Green, Yellow, Green, Green, Green, Green, Green, Green, Green, Green,
          Green, Green, Green, Green
Actual:   Green, Green, Yellow, Green, Green, Yellow, Green, Green, Green, Yellow, Yellow,
          Green, Green, Green, Green, Green, Green, Green, Green, Green, Green, Green,
          Green, Green, Green, Green
```

---

## Per-point table

| # | Point | Activity | Expected | Production | Result |
|---|-------|----------|----------|------------|--------|
| 1 | U1P1 | Getting Your Space Legs | Green | Green | ✅ PASS |
| 2 | U1P2 | Info and Intros | Green | Green | ✅ PASS |
| 3 | U1P3 | Defend the Expedition | Yellow | Yellow | ✅ PASS |
| 4 | U1P4 | What Was That? | Green | Green | ✅ PASS |
| 5 | U2P1 | Escape the Ruin | Green | Green | ✅ PASS |
| 6 | U2P2 | Foraged Forging | Yellow | Yellow | ✅ PASS |
| 7 | U2P3 | Getting the Band Back Together Part II | Green | Green | ✅ PASS |
| 8 | U2P4 | Investigate the Temple | Green | Green | ✅ PASS |
| 9 | U2P5 | Classified Information | Green | Green | ✅ PASS |
| 10 | U2P6 | Which Watershed? Part I | Green | **Yellow** | ❌ **FAIL** |
| 11 | U2P7 | Which Watershed? Part II | Yellow | Yellow | ✅ PASS |
| 12 | U3P1 | Good Morning Cadet + Establishing a Foothold | Green | Green | ✅ PASS |
| 13 | U3P2 | Pollution Solution | Green | Green | ✅ PASS |
| 14 | U3P3 | Pollution Argument | Yellow | **Green** | ❌ **FAIL** |
| 15 | U3P4 | Forsaken Facility | Green | Green | ✅ PASS |
| 16 | U3P5 | Plant the Superfruit Seeds | Green | Green | ✅ PASS |
| 17 | U4P1 | Well What Have We Here?: Water Table Basics | Green | Green | ✅ PASS |
| 18 | U4P2 | Infiltration Glyph + Alien Well Floors 1 & 2 | Green | Green | ✅ PASS |
| 19 | U4P3 | Alien Well Floor 3 & 4 | Green | Green | ✅ PASS |
| 20 | U4P4 | Alien Well Floor 5 + You Know the Drill | Green | Green | ✅ PASS |
| 21 | U4P5 | Saving Cadet Anderson | Green | Green | ✅ PASS |
| 22 | U4P6 | Desert Delicacies | Green | Green | ✅ PASS |
| 23 | U5P1 | If I Had a Nickel- Floors 1 & 2 | Green | Green | ✅ PASS |
| 24 | U5P2 | If I Had a Nickel- Floors 3 & 4 | Green | Green | ✅ PASS |
| 25 | U5P3 | What Happened Here? | Green | Green | ✅ PASS |
| 26 | U5P4 | Water Problems Require Water Solutions | Green | Green | ✅ PASS |

---

## The two mismatches — same root cause

Both failures are the **same class of defect**: the production attempt-window is
anchored on an event key that does **not** bracket the graded activity, so the
relevant log records fall *outside* the window and the windowed counts are wrong.
In each case the production script's window key also disagrees with the
"Attempt Window" the markdown itself documents.

### ❌ U2P6 — Which Watershed? Part I (expected Green, production Yellow)

The window's end anchor is `DialogueNodeEvent:20:35`. In the log there is only
**one** `20:35` event, and the pass node `DialogueNodeEvent:20:43` fires
**immediately after it** — i.e. just past `windowEndId` — so the windowed query
cannot see the correct choice and returns yellow.

| Event | `_id` (chronological) | Inside production window? |
|-------|----------------------|---------------------------|
| `DialogueNodeEvent:20:35` (window end anchor) | `…80c7` | — (window = `(MIN, …80c7]`) |
| `DialogueNodeEvent:20:43` (pass node) | `…80d1` | ❌ after window end |
| `DialogueNodeEvent:20:46` (documented Trigger-End) | `…80d5` | ❌ after window end |

No wrong-choice nodes (`20:44`/`20:45`) exist, so the true grade is **green**.
The lifetime/analytics script also yields green.

**Fix:** anchor the window **end on `DialogueNodeEvent:20:46`** (the documented
Trigger-End), not `DialogueNodeEvent:20:35`. The window then includes the pass
node.

### ❌ U3P3 — Pollution Argument (expected Yellow, production Green)

The window is anchored on `questActiveEvent:18` (both boundaries). That event
fires **after** the entire argumentation activity, so the windowed counts are 0:
`sum_count = 0 → base_score = 3 → total = 3 → green`.

| Events | `_id` range | vs. first `questActiveEvent:18` (`…8513`) |
|--------|-------------|-------------------------------------------|
| 7 wrong-argument nodes (`DialogueNodeEvent:84:20–47`) | `…8419` … `…84d5` | all **before** the trigger |
| 10 BackingInfoPanel uses | `…8401` … `…84c5` | all **before** the trigger |
| `questActiveEvent:18` (production window anchor) | `…8513`, `…8573` | window contains none of the above |

Lifetime/analytics: `sum_count = 7 → base_score = 0`, bonus `= 1` → `total = 1 < 3`
→ **yellow** (the expected color). The file's own documented window
(`DialogueNodeEvent:11:34` → `questFinishEvent:18`) **also** contains all 7 wrong
arguments and the backing-info use and yields yellow.

**Fix:** anchor the window on **`DialogueNodeEvent:11:34` (start) /
`questFinishEvent:18` (end)** — as the markdown documents — not
`questActiveEvent:18`.

---

## Reasons surfaced for the (correctly) yellow points

| Point | Reason code | Quantity / finding |
|-------|-------------|--------------------|
| U1P3 | `WRONG_ARG_SELECTED` | `attempt_number = 2` — needed multiple tries to build the correct argument |
| U2P2 | `BAD_FEEDBACK` | `triggering_number = 7` (threshold ≤ 1) — repeated wrong-direction prompts |
| U2P7 | `WRONG_ARG_SELECTED` | `attempt_number = 5` (`neg_count = 4` > 3) — too many evidence-selection attempts |

---

## How to reproduce

```bash
cd tests
python run_all.py                 # full table + diagnostics (exit 1 if any mismatch)
python run_all.py --quiet         # table only
python run_all.py --log PATH.json # validate a future weekly build's log dump
python test_u3p3.py               # run a single point (exit 0 = pass, 1 = fail)
```

See [README.md](README.md) for the suite layout and how to update tests when a
new build changes a point's color logic.

---

## Verification notes

- The harness reproduces MongoDB ObjectId ordering via lexicographic comparison
  of the 24-char hex `_id` strings, which matches both Mongo's byte ordering and
  generation/arrival time — so attempt-windowing matches production.
- All 26 production scripts were transcribed from the **Production Script
  (Attempt-Based)** section of each grading markdown (verbatim key lists,
  thresholds, operators, and default-to-yellow branches).
- The mismatch diagnoses were confirmed directly against the log data by
  comparing each event's `_id` position to the production window boundaries.
