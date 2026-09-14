# Reason-code validation results — 09-03-26-2

Log: `wenyi090326-2.stratalog.logdata.json`

**26 / 26 points pass every check (expected codes + variables, pop-up/cell consistency, message placeholders).**

| Point | Activity | Color | Window | Triggered code(s) | Expected | Result |
|---|---|---|---|---|---|---|
| U1P1 | Getting Your Space Legs | green | yes | - | - | PASS |
| U1P2 | Info and Intros | green | yes | - | - | PASS |
| U1P3 | Defend the Expedition | green | yes | - | - | PASS |
| U1P4 | What Was That? | green | yes | - | - | PASS |
| U2P1 | Escape the Ruin | green | yes | - | - | PASS |
| U2P2 | Foraged Forging | green | yes | - | - | PASS |
| U2P3 | Getting the Band Back Together Part II | green | yes | - | - | PASS |
| U2P4 | Investigate the Temple | green | yes | - | - | PASS |
| U2P5 | Classified Information | green | yes | - | - | PASS |
| U2P6 | Which Watershed? Part I | green | yes | - | - | PASS |
| U2P7 | Which Watershed? Part II | green | yes | - | - | PASS |
| U3P1 | Establishing a Foothold | green | yes | - | - | PASS |
| U3P2 | Pollution Solution | green | yes | - | - | PASS |
| U3P3 | Pollution Argument | green | yes | - | - | PASS |
| U3P4 | Forsaken Facility | green | yes | - | - | PASS |
| U3P5 | Plant the Superfruit Seeds | green | yes | - | - | PASS |
| U4P1 | Well What Have We Here? | green | yes | - | - | PASS |
| U4P2 | Infiltration Glyph + Alien Well Floors 1 & 2 | green | yes | - | - | PASS |
| U4P3 | Alien Well Floor 3 & 4 | green | yes | - | - | PASS |
| U4P4 | Alien Well Floor 5 + You Know the Drill | green | yes | - | - | PASS |
| U4P5 | Saving Cadet Anderson | green | yes | - | - | PASS |
| U4P6 | Desert Delicacies | green | yes | - | - | PASS |
| U5P1 | If I Had a Nickel- Floors 1 & 2 | green | yes | - | - | PASS |
| U5P2 | If I Had a Nickel- Floors 3 & 4 | green | yes | - | - | PASS |
| U5P3 | What Happened Here? | green | yes | - | - | PASS |
| U5P4 | Water Problems Require Water Solutions | green | yes | - | - | PASS |

## Instructor messages (triggered codes)

_No reason code triggered on this log._

## All code evaluations

| Point | Code | Triggered | Variables |
|---|---|---|---|
| U1P1 | _(no reason codes)_ | - | - |
| U1P2 | _(no reason codes)_ | - | - |
| U1P3 | WRONG_ARG_SELECTED | no | attempt_number=1 |
| U1P4 | _(no reason codes)_ | - | - |
| U2P1 | SOLVED_WITH_ASSIST | no | attempt_number=1 |
| U2P1 | EXCESS_ATTEMPTS | no | attempt_number=2 |
| U2P2 | EXCESS_NAV_REMINDERS | no | triggering_number=0 |
| U2P3 | EXCESS_NAV_REMINDERS | no | triggering_number=0, tera_count=0, aryn_count=0 |
| U2P4 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U2P4 | EXCESS_ATTEMPTS | no | attempt_number=1 |
| U2P5 | EXCESS_MISCLASSIFICATIONS | no | wrong_number=0, claim_wrong=0, reasoning_wrong=0, evidence_wrong=0 |
| U2P6 | WRONG_EVIDENCE_SELECTED | no | wrong_choice=None |
| U2P7 | EXCESS_ATTEMPTS | no | attempt_number=1, wrong_claim_number=0, irrelevant_evidence_number=0 |
| U3P1 | EXCESS_WRONG_RIVERS | no | wrong_river_number=0 |
| U3P2 | EXCESS_SENSOR_REMINDERS | no | downstream_reminder_number=0, redundant_reminder_number=0 |
| U3P3 | EXCESS_ATTEMPTS | no | wrong_argument_number=0, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0, backing_info_phrase='opened' |
| U3P4 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U3P4 | EXCESS_ATTEMPTS | no | attempt_number=1 |
| U3P5 | EXCESS_WRONG_PLANTINGS | no | wrong_planting_number=0 |
| U4P1 | SCORE_BELOW_THRESHOLD | no | choice_phrase='answered correctly', duration_phrase='took 17 seconds to solve' |
| U4P2 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U4P2 | EXCESS_ATTEMPTS | no | attempt_number=1 |
| U4P3 | SCORE_BELOW_THRESHOLD | no | floor3_attempts=1, floor4_attempts=1 |
| U4P4 | SCORE_BELOW_THRESHOLD | no | machine_attempt_number=3, wrong_choice_number=0 |
| U4P5 | EXCESS_ATTEMPTS | no | attempt_number=1, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0 |
| U4P6 | WRONG_SOIL_SELECTED | no | wrong_box_number=1, wrong_box_summary='the first box (chose Sand, needs Gravel)' |
| U5P1 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U5P1 | EXCESS_ATTEMPTS | no | attempt_number=1 |
| U5P2 | SCORE_BELOW_THRESHOLD | no | floor3_attempts=0, floor4_attempts=6 |
| U5P3 | EXCESS_ATTEMPTS | no | wrong_argument_number=0, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0 |
| U5P4 | WRONG_SETTINGS_SELECTED | no | wrong_run_number=0, failure_phrase='no successful desalinator run was recorded' |
