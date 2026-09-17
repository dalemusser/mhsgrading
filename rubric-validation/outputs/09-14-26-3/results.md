# Rubric validation results — 09-14-26-3

Log: `wenyi091426-3.stratalog.logdata.json`

**26 / 26 points match the expected dashboard color.**

| Point | Activity | Expected | Production | Result |
|---|---|---|---|---|
| U1P1 | Getting Your Space Legs | green | green | PASS |
| U1P2 | Info and Intros | green | green | PASS |
| U1P3 | Defend the Expedition | yellow | yellow | PASS |
| U1P4 | What Was That? | green | green | PASS |
| U2P1 | Escape the Ruin | yellow | yellow | PASS |
| U2P2 | Foraged Forging | yellow | yellow | PASS |
| U2P3 | Getting the Band Back Together Part II | yellow | yellow | PASS |
| U2P4 | Investigate the Temple | yellow | yellow | PASS |
| U2P5 | Classified Information | yellow | yellow | PASS |
| U2P6 | Which Watershed? Part I | yellow | yellow | PASS |
| U2P7 | Which Watershed? Part II | yellow | yellow | PASS |
| U3P1 | Good Morning Cadet + Establishing a Foothold | yellow | yellow | PASS |
| U3P2 | Pollution Solution | yellow | yellow | PASS |
| U3P3 | Pollution Argument | yellow | yellow | PASS |
| U3P4 | Forsaken Facility | yellow | yellow | PASS |
| U3P5 | Plant the Superfruit Seeds | yellow | yellow | PASS |
| U4P1 | Well What Have We Here?: Water Table Basics | yellow | yellow | PASS |
| U4P2 | Infiltration Glyph + Alien Well Floors 1 & 2 | yellow | yellow | PASS |
| U4P3 | Alien Well Floor 3 & 4 | yellow | yellow | PASS |
| U4P4 | Alien Well Floor 5 + You Know the Drill | yellow | yellow | PASS |
| U4P5 | Saving Cadet Anderson | yellow | yellow | PASS |
| U4P6 | Desert Delicacies | yellow | yellow | PASS |
| U5P1 | If I Had a Nickel- Floors 1 & 2 | yellow | yellow | PASS |
| U5P2 | If I Had a Nickel- Floors 3 & 4 | yellow | yellow | PASS |
| U5P3 | What Happened Here? | yellow | yellow | PASS |
| U5P4 | Water Problems Require Water Solutions | yellow | yellow | PASS |

## Diagnostics

```
[PASS] U1P3 — Defend the Expedition
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - WRONG_ARG_SELECTED: attempt_number=2 (yellow nodes hit 1x in window) — student needed multiple tries to build the correct argument
```

```
[PASS] U2P1 — Escape the Ruin
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - MISSING_SUCCESS_NODE: success node DialogueNodeEvent:68:29 absent in window — did not complete map-profile matching independently
         - TOO_MANY_NEGATIVES: attempts_number=5 (>4) — too many incorrect map-terrain matches
```

```
[PASS] U2P2 — Foraged Forging
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - BAD_FEEDBACK: triggering_number=4 (threshold <= 1) — repeated wrong-direction prompts while searching for Toppo
```

```
[PASS] U2P3 — Getting the Band Back Together Part II
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - BAD_FEEDBACK: triggering_number=14 (threshold < 6) — repeated wrong-direction prompts while searching for Tera/Aryn
```

```
[PASS] U2P4 — Investigate the Temple
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - MISSING_SUCCESS_NODE: success node DialogueNodeEvent:74:21 absent in window — did not complete watershed-flow matching independently
         - TOO_MANY_NEGATIVES: attempts_number=6 (> 5) — too many attempts on the watershed-flow glyph puzzle
```

```
[PASS] U2P5 — Classified Information
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - TOO_MANY_NEGATIVES: wrong_number=8 (score=3.33 < 4) — too many incorrect attempts identifying argument parts
```

```
[PASS] U2P6 — Which Watershed? Part I
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - MISSING_SUCCESS_NODE: pass node DialogueNodeEvent:20:43 absent in window — correct criterion never selected
         - HIT_YELLOW_NODE: chose an incorrect criterion for watershed size on first try: waterfall height
```

```
[PASS] U2P7 — Which Watershed? Part II
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - WRONG_ARG_SELECTED: attempt_number=9 (neg_count=8 > 3) — too many attempts to select evidence to support the claim
```

```
[PASS] U3P1 — Good Morning Cadet + Establishing a Foothold
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: cnt=0 wrong_count=3
         - TOO_MANY_NEGATIVES: attempt_number=3 (>= 2) — selected the wrong river too many times while identifying the direction of water flow
```

```
[PASS] U3P2 — Pollution Solution
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: c27=5 c29=4 c230=4 cSum=8 score=1 reminding_count=13
         - BAD_FEEDBACK: attempt_number=13 (> 6) — repeated reminding dialogues regarding redundant sensor usage
```

```
[PASS] U3P3 — Pollution Argument
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: sum_count=7 base_score=0 bonus=1 total_score=1
         - WRONG_ARG_SELECTED: attempts_number=7 (>4) — too many attempts to select correct reasoning
```

```
[PASS] U3P4 — Forsaken Facility
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: has_gate=1 total_count=5 score=0
         - TOO_MANY_NEGATIVES: attempts_number=5 (> 3) — too many attempts to make the correct matches
```

```
[PASS] U3P5 — Plant the Superfruit Seeds
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: pos_count=0 neg_count=4 sum_score=-2.0
         - TOO_MANY_NEGATIVES: attempts_number=4 (> 1) — planted super-fruit seeds into too many wrong spots
```

```
[PASS] U4P1 — Well What Have We Here?: Water Table Basics
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: score=0.0 has_correct=0 duration_seconds=168.454
         - WRONG_CHOISE_SELECTED: correct choice DialogueNodeEvent:88:5 absent in window — did not select the water-table boundary answer on first attempt
         - TOO_LONG_TO_SOLVE_PROBLEM: soil key puzzle duration=168.454s (> 30s or unmeasured) — spent too long solving the soil key puzzle
```

```
[PASS] U4P2 — Infiltration Glyph + Alien Well Floors 1 & 2
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - TOO_MANY_NEGATIVES: negative feedback node present in window — needed more than 2 attempts to figure out the correct matches
```

```
[PASS] U4P3 — Alien Well Floor 3 & 4
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: score=0 floor3_attempts=10 floor4_attempts=15
         - TOO_MANY_ATTEMPTS_3: floor3_attempts=10 (> 1) — interacted with the third-floor soil machine more than the optimal one attempt
         - TOO_MANY_ATTEMPTS_4: floor4_attempts=15 (> 1) — interacted with the fourth-floor soil machine more than the optimal one attempt
```

```
[PASS] U4P4 — Alien Well Floor 5 + You Know the Drill
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: score=0 attempt_time=18 negative_feedback_number=3
         - SCORE_BELOW_THRESHOLD: score=0 (<= 2) — combined soil-machine and dialogue score too low
         - TOO_MANY_ATTEMPTS: attempt_time=18 (> 3) — too many fifth-floor soil machine interactions
         - BAD_FEEDBACK: negative_feedback_number=3 (> 0) — wrong water-table choices before the correct layer
```

```
[PASS] U4P5 — Saving Cadet Anderson
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: has_success=1 negativeCount=10
         - WRONG_ARG_SELECTED: negativeCount=10 (>= 3) — too many negative feedback events before submitting the correct argument
```

```
[PASS] U4P6 — Desert Delicacies
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: box_score=0 dialogue_score=0 final=0 wrongTime=3
         - WRONG_CHOISE_SELECTED: wrongTime=3 (correct boxes < 2, correct-soil feedback dialogues = 0) — box 0: expected Gravel, got Clay, box 1: expected Sand, got Gravel, box 2: expected Clay, got Sand
```

```
[PASS] U5P1 — If I Had a Nickel- Floors 1 & 2
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - BAD_FEEDBACK: negative_feedback_number=1 (>0) — received negative feedback before solving the puzzle
```

```
[PASS] U5P2 — If I Had a Nickel- Floors 3 & 4
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - _score: floor3_attempts=8 floor4_attempts=10 score=1
         - TOO_MANY_ATTEMPTS_3: floor3_attempts=8 (>6) — too many condenser/evaporator interactions on the 3rd floor
         - TOO_MANY_ATTEMPTS_4: floor4_attempts=10 (>5) — too many condenser/evaporator interactions on the 4th floor
```

```
[PASS] U5P3 — What Happened Here?
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - WRONG_ARG_SELECTED: negativeCount=4 (>=4) — too many wrong arguments before submitting the correct one
```

```
[PASS] U5P4 — Water Problems Require Water Solutions
       expected=yellow actual=yellow
       reason(s) for yellow (expected):
         - MISSING_SUCCESS_NODE: success node DialogueNodeEvent:106:35 absent in window — did not correctly identify the water solution plan
```
