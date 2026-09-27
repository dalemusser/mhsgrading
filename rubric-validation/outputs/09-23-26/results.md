# Rubric validation results — 09-23-26

Log: `wenyi09232026.stratalog.logdata.json`

**26 / 26 points match the expected dashboard color.**

| Point | Activity | Expected | Production | Result |
|---|---|---|---|---|
| U1P1 | Getting Your Space Legs | green | green | PASS |
| U1P2 | Info and Intros | green | green | PASS |
| U1P3 | Defend the Expedition | green | green | PASS |
| U1P4 | What Was That? | green | green | PASS |
| U2P1 | Escape the Ruin | yellow | yellow | PASS |
| U2P2 | Foraged Forging | green | green | PASS |
| U2P3 | Getting the Band Back Together Part II | green | green | PASS |
| U2P4 | Investigate the Temple | yellow | yellow | PASS |
| U2P5 | Classified Information | green | green | PASS |
| U2P6 | Which Watershed? Part I | green | green | PASS |
| U2P7 | Which Watershed? Part II | green | green | PASS |
| U3P1 | Good Morning Cadet + Establishing a Foothold | green | green | PASS |
| U3P2 | Pollution Solution | green | green | PASS |
| U3P3 | Pollution Argument | green | green | PASS |
| U3P4 | Forsaken Facility | yellow | yellow | PASS |
| U3P5 | Plant the Superfruit Seeds | green | green | PASS |
| U4P1 | Well What Have We Here?: Water Table Basics | green | green | PASS |
| U4P2 | Infiltration Glyph + Alien Well Floors 1 & 2 | yellow | yellow | PASS |
| U4P3 | Alien Well Floor 3 & 4 | green | green | PASS |
| U4P4 | Alien Well Floor 5 + You Know the Drill | green | green | PASS |
| U4P5 | Saving Cadet Anderson | green | green | PASS |
| U4P6 | Desert Delicacies | green | green | PASS |
| U5P1 | If I Had a Nickel- Floors 1 & 2 | yellow | yellow | PASS |
| U5P2 | If I Had a Nickel- Floors 3 & 4 | green | green | PASS |
| U5P3 | What Happened Here? | green | green | PASS |
| U5P4 | Water Problems Require Water Solutions | green | green | PASS |

## Diagnostics

```
[PASS] U2P1 — Escape the Ruin
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - TOO_MANY_NEGATIVES: attempts_number=5 (>4) — too many incorrect map-terrain matches
```

```
[PASS] U3P4 — Forsaken Facility
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: has_gate=1 total_count=5 score=0
         - TOO_MANY_NEGATIVES: attempts_number=5 (>= 3) — too many attempts to make the correct matches
```

```
[PASS] U4P2 — Infiltration Glyph + Alien Well Floors 1 & 2
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - TOO_MANY_NEGATIVES: negative feedback node present in window — needed more than 2 attempts to figure out the correct matches
```

```
[PASS] U5P1 — If I Had a Nickel- Floors 1 & 2
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - BAD_FEEDBACK: negative_feedback_number=1 (>0) — received negative feedback before solving the puzzle
```
