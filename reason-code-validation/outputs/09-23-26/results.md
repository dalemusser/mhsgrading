# Reason-code validation results — 09-23-26

Log: `wenyi09232026.stratalog.logdata.json`

**26 / 26 points pass every check (expected codes + variables, pop-up/cell consistency, message placeholders).**

| Point | Activity | Color | Window | Triggered code(s) | Expected | Result |
|---|---|---|---|---|---|---|
| U1P1 | Getting Your Space Legs | green | yes | - | - | PASS |
| U1P2 | Info and Intros | green | yes | - | - | PASS |
| U1P3 | Defend the Expedition | green | yes | - | - | PASS |
| U1P4 | What Was That? | green | yes | - | - | PASS |
| U2P1 | Escape the Ruin | yellow | yes | EXCESS_ATTEMPTS | EXCESS_ATTEMPTS | PASS |
| U2P2 | Foraged Forging | green | yes | - | - | PASS |
| U2P3 | Getting the Band Back Together Part II | green | yes | - | - | PASS |
| U2P4 | Investigate the Temple | yellow | yes | EXCESS_ATTEMPTS | EXCESS_ATTEMPTS | PASS |
| U2P5 | Classified Information | green | yes | - | - | PASS |
| U2P6 | Which Watershed? Part I | green | yes | - | - | PASS |
| U2P7 | Which Watershed? Part II | green | yes | - | - | PASS |
| U3P1 | Establishing a Foothold | green | yes | - | - | PASS |
| U3P2 | Pollution Solution | green | yes | - | - | PASS |
| U3P3 | Pollution Argument | green | yes | - | - | PASS |
| U3P4 | Forsaken Facility | yellow | yes | SOLVED_WITH_ASSIST | SOLVED_WITH_ASSIST | PASS |
| U3P5 | Plant the Superfruit Seeds | green | yes | - | - | PASS |
| U4P1 | Well What Have We Here? | green | yes | - | - | PASS |
| U4P2 | Infiltration Glyph + Alien Well Floors 1 & 2 | yellow | yes | SOLVED_WITH_ASSIST | SOLVED_WITH_ASSIST | PASS |
| U4P3 | Alien Well Floor 3 & 4 | green | yes | - | - | PASS |
| U4P4 | Alien Well Floor 5 + You Know the Drill | green | yes | - | - | PASS |
| U4P5 | Saving Cadet Anderson | green | yes | - | - | PASS |
| U4P6 | Desert Delicacies | green | yes | - | - | PASS |
| U5P1 | If I Had a Nickel- Floors 1 & 2 | yellow | yes | EXCESS_ATTEMPTS | EXCESS_ATTEMPTS | PASS |
| U5P2 | If I Had a Nickel- Floors 3 & 4 | green | yes | - | - | PASS |
| U5P3 | What Happened Here? | green | yes | - | - | PASS |
| U5P4 | Water Problems Require Water Solutions | green | yes | - | - | PASS |

## Instructor messages (triggered codes)

### U2P1 — Escape the Ruin (yellow)

**EXCESS_ATTEMPTS** — `attempt_number=6`

> In Escape the Ruin, the student matched all six topographic maps to their elevation profiles on their own, but needed 6 attempts. This point earns green only when the correct solution is submitted within 4 attempts. Repeated incorrect arrangements may indicate difficulty connecting the top-down contour-line view of a landscape to its side-view profile.

### U2P4 — Investigate the Temple (yellow)

**EXCESS_ATTEMPTS** — `attempt_number=6`

> In Investigate the Temple, the student arranged the watershed terrain pieces correctly on their own, but needed 6 attempts. This point earns green only when the correct arrangement is submitted within 5 attempts. Repeated incorrect arrangements may indicate difficulty connecting drainage-area size with relative flow rate, the pattern that a larger watershed collects and delivers more water to its main river.

### U3P4 — Forsaken Facility (yellow)

**SOLVED_WITH_ASSIST** — `attempt_number=5`

> In Forsaken Facility, the student did not complete the ordering puzzle showing how materials dissolve into water independently. After 5 incorrect arrangements, the in-game guide DANI ordered the pieces. This point earns green only when the student submits the correct order on their own within 3 attempts. Needing this level of support may indicate the student would benefit from reviewing how the particles of a dissolved material spread through water, even once they can no longer be seen.

### U4P2 — Infiltration Glyph + Alien Well Floors 1 & 2 (yellow)

**SOLVED_WITH_ASSIST** — `attempt_number=5`

> In the Infiltration Glyph puzzle, the student did not complete the soil-infiltration ordering independently. After 5 incorrect arrangements, the in-game guide DANI ordered the pieces. This point earns green only when the student submits the correct order on their own within 3 attempts. Needing this level of support may indicate the student would benefit from reviewing how water infiltrates different soils: the larger the soil particles, the faster water passes through.

### U5P1 — If I Had a Nickel- Floors 1 & 2 (yellow)

**EXCESS_ATTEMPTS** — `attempt_number=5`

> In If I Had a Nickel (floors 1 and 2), the student solved the evaporation glyph puzzle on their own, but needed 5 attempts. This point earns green only when the puzzle is solved within 4 attempts. Repeated incorrect arrangements may indicate difficulty matching the wall images (temperatures at different times of day) to the evaporation rates they would produce.

## All code evaluations

| Point | Code | Triggered | Variables |
|---|---|---|---|
| U1P1 | _(no reason codes)_ | - | - |
| U1P2 | _(no reason codes)_ | - | - |
| U1P3 | WRONG_ARG_SELECTED | no | attempt_number=1 |
| U1P4 | _(no reason codes)_ | - | - |
| U2P1 | SOLVED_WITH_ASSIST | no | attempt_number=5 |
| U2P1 | EXCESS_ATTEMPTS | yes | attempt_number=6 |
| U2P2 | EXCESS_NAV_REMINDERS | no | triggering_number=0 |
| U2P3 | EXCESS_NAV_REMINDERS | no | triggering_number=0, tera_count=0, aryn_count=0 |
| U2P4 | SOLVED_WITH_ASSIST | no | attempt_number=5 |
| U2P4 | EXCESS_ATTEMPTS | yes | attempt_number=6 |
| U2P5 | EXCESS_MISCLASSIFICATIONS | no | wrong_number=0, claim_wrong=0, reasoning_wrong=0, evidence_wrong=0 |
| U2P6 | WRONG_EVIDENCE_SELECTED | no | wrong_choice=None |
| U2P7 | EXCESS_ATTEMPTS | no | attempt_number=1, wrong_claim_number=0, both_wrong_number=0, irrelevant_evidence_number=0 |
| U3P1 | EXCESS_WRONG_RIVERS | no | wrong_river_number=0 |
| U3P2 | EXCESS_SENSOR_REMINDERS | no | downstream_reminder_number=3, redundant_reminder_number=0 |
| U3P3 | EXCESS_ATTEMPTS | no | wrong_argument_number=0, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0, backing_info_phrase='opened' |
| U3P4 | SOLVED_WITH_ASSIST | yes | attempt_number=5 |
| U3P4 | EXCESS_ATTEMPTS | no | attempt_number=6 |
| U3P5 | EXCESS_WRONG_PLANTINGS | no | wrong_planting_number=0 |
| U4P1 | SCORE_BELOW_THRESHOLD | no | choice_phrase='answered correctly', duration_phrase='took 15 seconds to solve' |
| U4P2 | SOLVED_WITH_ASSIST | yes | attempt_number=5 |
| U4P2 | EXCESS_ATTEMPTS | no | attempt_number=6 |
| U4P3 | SCORE_BELOW_THRESHOLD | no | floor3_attempts=1, floor4_attempts=1 |
| U4P4 | SCORE_BELOW_THRESHOLD | no | machine_attempt_number=3, wrong_choice_number=0 |
| U4P5 | EXCESS_ATTEMPTS | no | attempt_number=1, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0 |
| U4P6 | WRONG_SOIL_SELECTED | no | wrong_box_number=0, wrong_box_summary='' |
| U5P1 | SOLVED_WITH_ASSIST | no | attempt_number=4 |
| U5P1 | EXCESS_ATTEMPTS | yes | attempt_number=5 |
| U5P2 | SCORE_BELOW_THRESHOLD | no | floor3_attempts=9, floor4_attempts=4 |
| U5P3 | EXCESS_ATTEMPTS | no | wrong_argument_number=0, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0 |
| U5P4 | WRONG_SETTINGS_SELECTED | no | wrong_run_number=0, failure_phrase='no successful desalinator run was recorded' |
