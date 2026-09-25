# Reason-code validation results — 09-03-26-4

Log: `wenyi090326-4.stratalog.logdata.json`

**26 / 26 points pass every check (expected codes + variables, pop-up/cell consistency, message placeholders).**

| Point | Activity | Color | Window | Triggered code(s) | Expected | Result |
|---|---|---|---|---|---|---|
| U1P1 | Getting Your Space Legs | green | yes | - | - | PASS |
| U1P2 | Info and Intros | green | yes | - | - | PASS |
| U1P3 | Defend the Expedition | green | yes | - | - | PASS |
| U1P4 | What Was That? | green | yes | - | - | PASS |
| U2P1 | Escape the Ruin | yellow | yes | SOLVED_WITH_ASSIST | SOLVED_WITH_ASSIST | PASS |
| U2P2 | Foraged Forging | yellow | yes | EXCESS_NAV_REMINDERS | EXCESS_NAV_REMINDERS | PASS |
| U2P3 | Getting the Band Back Together Part II | yellow | yes | EXCESS_NAV_REMINDERS | EXCESS_NAV_REMINDERS | PASS |
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
| U5P1 | If I Had a Nickel- Floors 1 & 2 | yellow | no | - | - | PASS |
| U5P2 | If I Had a Nickel- Floors 3 & 4 | yellow | no | - | - | PASS |
| U5P3 | What Happened Here? | yellow | no | - | - | PASS |
| U5P4 | Water Problems Require Water Solutions | yellow | no | - | - | PASS |

## Instructor messages (triggered codes)

### U2P1 — Escape the Ruin (yellow)

**SOLVED_WITH_ASSIST** — `attempt_number=5`

> In Escape the Ruin, the student did not complete the topographic-map matching independently. After 5 incorrect arrangements, the in-game guide DANI placed the remaining pieces. This point earns green only when the student submits the correct solution on their own within 4 attempts. Needing this level of support may indicate the student would benefit from direct instruction on how contour lines represent elevation and slope before matching maps to terrain shapes.

### U2P2 — Foraged Forging (yellow)

**EXCESS_NAV_REMINDERS** — `triggering_number=11`

> In Foraged Forging, while navigating to find Captain Toppo, the student triggered 11 adaptive reminders, dialogues that fire when the player travels somewhere inconsistent with Anderson's clues or has not been consulting the map. This point earns green only when at most 1 such reminder fires during the search. Repeated reminders may indicate difficulty translating the clues about direction, elevation, and terrain features into a location on the topographic map using contour lines and the compass.

### U2P3 — Getting the Band Back Together Part II (yellow)

**EXCESS_NAV_REMINDERS** — `triggering_number=6`, `tera_count=6`, `aryn_count=0`

> In Getting the Band Back Together Part II, while navigating to find Tera and Aryn, the student triggered 6 adaptive reminders, dialogues that fire when the player travels somewhere inconsistent with the location clues (6 during the search for Tera, 0 during the search for Aryn). This point earns green only when fewer than 6 such reminders fire across the two searches. Repeated reminders may indicate difficulty connecting each set of clues (direction, elevation, landforms, and water features) to locations on the topographic map when planning and adjusting a route.

## All code evaluations

| Point | Code | Triggered | Variables |
|---|---|---|---|
| U1P1 | _(no reason codes)_ | - | - |
| U1P2 | _(no reason codes)_ | - | - |
| U1P3 | WRONG_ARG_SELECTED | no | attempt_number=1 |
| U1P4 | _(no reason codes)_ | - | - |
| U2P1 | SOLVED_WITH_ASSIST | yes | attempt_number=5 |
| U2P1 | EXCESS_ATTEMPTS | no | attempt_number=6 |
| U2P2 | EXCESS_NAV_REMINDERS | yes | triggering_number=11 |
| U2P3 | EXCESS_NAV_REMINDERS | yes | triggering_number=6, tera_count=6, aryn_count=0 |
| U2P4 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U2P4 | EXCESS_ATTEMPTS | no | attempt_number=1 |
| U2P5 | EXCESS_MISCLASSIFICATIONS | no | wrong_number=0, claim_wrong=0, reasoning_wrong=0, evidence_wrong=0 |
| U2P6 | WRONG_EVIDENCE_SELECTED | no | wrong_choice=None |
| U2P7 | EXCESS_ATTEMPTS | no | attempt_number=1, wrong_claim_number=0, both_wrong_number=0, irrelevant_evidence_number=0 |
| U3P1 | EXCESS_WRONG_RIVERS | no | wrong_river_number=0 |
| U3P2 | EXCESS_SENSOR_REMINDERS | no | downstream_reminder_number=0, redundant_reminder_number=0 |
| U3P3 | EXCESS_ATTEMPTS | no | wrong_argument_number=0, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0, backing_info_phrase='opened' |
| U3P4 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U3P4 | EXCESS_ATTEMPTS | no | attempt_number=1 |
| U3P5 | EXCESS_WRONG_PLANTINGS | no | wrong_planting_number=0 |
| U4P1 | SCORE_BELOW_THRESHOLD | no | choice_phrase='answered correctly', duration_phrase='took 13 seconds to solve' |
| U4P2 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U4P2 | EXCESS_ATTEMPTS | no | attempt_number=1 |
| U4P3 | SCORE_BELOW_THRESHOLD | no | floor3_attempts=1, floor4_attempts=1 |
| U4P4 | SCORE_BELOW_THRESHOLD | no | machine_attempt_number=3, wrong_choice_number=0 |
| U4P5 | EXCESS_ATTEMPTS | no | attempt_number=1, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0 |
| U4P6 | WRONG_SOIL_SELECTED | no | wrong_box_number=0, wrong_box_summary='' |
| U5P1 | SOLVED_WITH_ASSIST | no | attempt_number=0 |
| U5P1 | EXCESS_ATTEMPTS | no | attempt_number=0 |
| U5P2 | SCORE_BELOW_THRESHOLD | no | floor3_attempts=0, floor4_attempts=0 |
| U5P3 | EXCESS_ATTEMPTS | no | wrong_argument_number=0, claim_wrong_number=0, reasoning_wrong_number=0, evidence_wrong_number=0 |
| U5P4 | WRONG_SETTINGS_SELECTED | no | wrong_run_number=0, failure_phrase='' |
