# Reason-code validation results — 09-03-26-3

Log: `wenyi090326-3.stratalog.logdata.json`

**26 / 26 points pass every check (expected codes + variables, pop-up/cell consistency, message placeholders).**

| Point | Activity | Color | Window | Triggered code(s) | Expected | Result |
|---|---|---|---|---|---|---|
| U1P1 | Getting Your Space Legs | green | yes | - | - | PASS |
| U1P2 | Info and Intros | green | yes | - | - | PASS |
| U1P3 | Defend the Expedition | yellow | yes | WRONG_ARG_SELECTED | WRONG_ARG_SELECTED | PASS |
| U1P4 | What Was That? | green | yes | - | - | PASS |
| U2P1 | Escape the Ruin | green | yes | - | - | PASS |
| U2P2 | Foraged Forging | yellow | yes | EXCESS_NAV_REMINDERS | EXCESS_NAV_REMINDERS | PASS |
| U2P3 | Getting the Band Back Together Part II | green | yes | - | - | PASS |
| U2P4 | Investigate the Temple | yellow | yes | SOLVED_WITH_ASSIST | SOLVED_WITH_ASSIST | PASS |
| U2P5 | Classified Information | yellow | yes | EXCESS_MISCLASSIFICATIONS | EXCESS_MISCLASSIFICATIONS | PASS |
| U2P6 | Which Watershed? Part I | yellow | yes | WRONG_EVIDENCE_SELECTED | WRONG_EVIDENCE_SELECTED | PASS |
| U2P7 | Which Watershed? Part II | yellow | yes | EXCESS_ATTEMPTS | EXCESS_ATTEMPTS | PASS |
| U3P1 | Establishing a Foothold | yellow | yes | EXCESS_WRONG_RIVERS | EXCESS_WRONG_RIVERS | PASS |
| U3P2 | Pollution Solution | yellow | yes | EXCESS_SENSOR_REMINDERS | EXCESS_SENSOR_REMINDERS | PASS |
| U3P3 | Pollution Argument | yellow | yes | EXCESS_ATTEMPTS | EXCESS_ATTEMPTS | PASS |
| U3P4 | Forsaken Facility | green | yes | - | - | PASS |
| U3P5 | Plant the Superfruit Seeds | yellow | yes | EXCESS_WRONG_PLANTINGS | EXCESS_WRONG_PLANTINGS | PASS |
| U4P1 | Well What Have We Here? | yellow | yes | SCORE_BELOW_THRESHOLD | SCORE_BELOW_THRESHOLD | PASS |
| U4P2 | Infiltration Glyph + Alien Well Floors 1 & 2 | yellow | yes | SOLVED_WITH_ASSIST | SOLVED_WITH_ASSIST | PASS |
| U4P3 | Alien Well Floor 3 & 4 | yellow | yes | SCORE_BELOW_THRESHOLD | SCORE_BELOW_THRESHOLD | PASS |
| U4P4 | Alien Well Floor 5 + You Know the Drill | yellow | yes | SCORE_BELOW_THRESHOLD | SCORE_BELOW_THRESHOLD | PASS |
| U4P5 | Saving Cadet Anderson | yellow | yes | EXCESS_ATTEMPTS | EXCESS_ATTEMPTS | PASS |
| U4P6 | Desert Delicacies | yellow | yes | WRONG_SOIL_SELECTED | WRONG_SOIL_SELECTED | PASS |
| U5P1 | If I Had a Nickel- Floors 1 & 2 | yellow | yes | SOLVED_WITH_ASSIST | SOLVED_WITH_ASSIST | PASS |
| U5P2 | If I Had a Nickel- Floors 3 & 4 | yellow | yes | SCORE_BELOW_THRESHOLD | SCORE_BELOW_THRESHOLD | PASS |
| U5P3 | What Happened Here? | yellow | yes | EXCESS_ATTEMPTS | EXCESS_ATTEMPTS | PASS |
| U5P4 | Water Problems Require Water Solutions | yellow | yes | WRONG_SETTINGS_SELECTED | WRONG_SETTINGS_SELECTED | PASS |

## Instructor messages (triggered codes)

### U1P3 — Defend the Expedition (yellow)

**WRONG_ARG_SELECTED** — `attempt_number=3`

> In Defend the Expedition, the student's first argument submission was incorrect; they built the correct argument on attempt 3. This point earns green only when the first submission is correct. The early miss may indicate difficulty identifying which claim is supported by the given evidence and reasoning.

### U2P2 — Foraged Forging (yellow)

**EXCESS_NAV_REMINDERS** — `triggering_number=19`

> In Foraged Forging, while navigating to find Captain Toppo, the student triggered 19 adaptive reminders, dialogues that fire when the player travels somewhere inconsistent with Anderson's clues or has not been consulting the map. This point earns green only when at most 1 such reminder fires during the search. Repeated reminders may indicate difficulty translating the clues about direction, elevation, and terrain features into a location on the topographic map using contour lines and the compass.

### U2P4 — Investigate the Temple (yellow)

**SOLVED_WITH_ASSIST** — `attempt_number=5`

> In Investigate the Temple, the student did not complete the watershed glyph puzzle independently - after 5 incorrect arrangements, the in-game guide DANI stepped in to order the watershed pieces. This point earns green only when the student submits the correct arrangement on their own within 5 attempts. Needing this level of support may indicate the student would benefit from reviewing how a larger drainage area collects and delivers more water to the main river, producing a greater flow rate.

### U2P5 — Classified Information (yellow)

**EXCESS_MISCLASSIFICATIONS** — `wrong_number=10`, `claim_wrong=1`, `reasoning_wrong=3`, `evidence_wrong=6`

> In Classified Information, while repairing DANI by classifying highlighted passages of a scientific argument, the student made 10 incorrect classifications - 1 on passages that were claims, 3 on reasoning, and 6 on evidence. This point earns green only when the student completes all six classifications with at most 6 incorrect selections. Errors concentrated on one component may indicate difficulty recognizing that component's role: a claim states the conclusion, evidence provides information collected from the environment, and reasoning explains how the evidence supports the claim.

### U2P6 — Which Watershed? Part I (yellow)

**WRONG_EVIDENCE_SELECTED** — `wrong_choice='waterfall height'`

> In Which Watershed? Part I, when Dr. Toppo asked which observation provides the strongest evidence for identifying the larger watershed, the student selected waterfall height instead of the correct answer, water flow rate. This point earns green only when water flow rate is selected. This may indicate difficulty distinguishing evidence that directly relates to watershed size - a larger drainage area collects and delivers more water, producing a greater flow rate - from observations such as waterfall height or salinity that do not indicate how much land drains to the river.

### U2P7 — Which Watershed? Part II (yellow)

**EXCESS_ATTEMPTS** — `attempt_number=9`, `wrong_claim_number=1`, `both_wrong_number=3`, `irrelevant_evidence_number=4`

> In Which Watershed? Part II, the student built the argument about which watershed is larger, but needed 9 submissions - 1 where only the claim was wrong, 3 where both the claim and the evidence were wrong, and 4 where the claim was right but the evidence does not indicate watershed size (waterfall height, salinity, the downstream river, or several pieces at once). This point earns green only when the correct argument is submitted within 4 attempts. Repeated incorrect submissions may indicate difficulty selecting the claim the data supports and distinguishing relevant evidence - flow rate reflects how much land drains to each river - from irrelevant observations.

### U3P1 — Establishing a Foothold (yellow)

**EXCESS_WRONG_RIVERS** — `wrong_river_number=3`

> In Establishing a Foothold, while sending Tera's three supply crates back to her camp by floating them down a river, the student dropped 3 crates into the wrong river. This point earns green only when at most 1 crate goes into the wrong river. Wrong-river choices may indicate difficulty using the watershed map to determine flow direction - water flows from higher to lower elevation toward the ocean, so the correct river is the one that flows past Tera's camp.

### U3P2 — Pollution Solution (yellow)

**EXCESS_SENSOR_REMINDERS** — `downstream_reminder_number=13`, `redundant_reminder_number=22`

> In Pollution Solution, while using drone-dropped sensors to trace the source of the river pollution, the student triggered 13 reminders that pollution flows only downstream (testing in the wrong direction) and 22 reminders about unnecessary tests (checking upstream of a clean sensor, or pushing past the top of a branch). This point stays green unless reminders accumulate in both categories: one occurring 4 or more times and the other at least twice. Repeated reminders of both kinds may indicate difficulty using sensor readings to reason about how dissolved material spreads through a watershed: pollution can appear only downstream of its source, so a polluted reading means the source is upstream, and a clean reading clears everything upstream of it.

### U3P3 — Pollution Argument (yellow)

**EXCESS_ATTEMPTS** — `wrong_argument_number=5`, `claim_wrong_number=3`, `reasoning_wrong_number=2`, `evidence_wrong_number=0`, `backing_info_phrase='opened'`

> In Pollution Argument, while constructing the argument about where the pollutant enters the river, the student made 5 incorrect submissions (3 with a claim problem, 2 with a reasoning problem, and 0 with an evidence or structure problem), and opened the Pollution Site Data reference panel. This point earns green only when incorrect submissions stay within the limit (at most 3, or one more when the reference panel has been consulted, which earns a bonus point). Errors concentrated on reasoning may indicate difficulty explaining how pollution travels downstream with the water flow, which is the link between the sensor evidence and the claim.

### U3P5 — Plant the Superfruit Seeds (yellow)

**EXCESS_WRONG_PLANTINGS** — `wrong_planting_number=4`

> In Plant the Superfruit Seeds, while helping Tera plant four superfruit seeds in garden plots along the river, the student planted 4 seeds into wrong spots - locations that do not receive the super-nutrient. This point earns green only when at most 1 seed is planted in a wrong spot. Repeated wrong plantings may indicate difficulty predicting how a dissolved material spreads through a watershed: the nutrient travels downstream with the water flow, so only plots downstream of the temple source can receive it.

### U4P1 — Well What Have We Here? (yellow)

**SCORE_BELOW_THRESHOLD** — `choice_phrase="chose 'it's any water found underground' instead of the correct answer on"`, `duration_phrase='took 136 seconds to solve'`

> In Well What Have We Here?, the student chose 'it's any water found underground' instead of the correct answer on Anderson's question about what the water table is, and took 136 seconds to solve the soil key puzzle. This point earns green only when the puzzle is solved within 30 seconds, or within 90 seconds with the water-table question answered correctly. A missed question may reflect the common misconception that the water table is simply any underground water (it is specifically the boundary between the saturated and unsaturated soil layers), and a slow solve may indicate difficulty controlling the water level between the target lines.

### U4P2 — Infiltration Glyph + Alien Well Floors 1 & 2 (yellow)

**SOLVED_WITH_ASSIST** — `attempt_number=5`

> In the Infiltration Glyph puzzle, the student did not complete the soil-infiltration ordering independently. After 5 incorrect arrangements, the in-game guide DANI ordered the pieces. This point earns green only when the student submits the correct order on their own within 3 attempts. Needing this level of support may indicate the student would benefit from reviewing how water infiltrates different soils: the larger the soil particles, the faster water passes through.

### U4P3 — Alien Well Floor 3 & 4 (yellow)

**SCORE_BELOW_THRESHOLD** — `floor3_attempts=7`, `floor4_attempts=6`

> In the Alien Well (floors 3 and 4), the student changed the soil-type canisters 7 times on the third-floor machine and 6 times on the fourth-floor machine. This point earns green only when the fourth-floor machine is set correctly on the first try, or on the second try with the third floor solved in one. Many canister changes may indicate the student was cycling through soil types rather than predicting which soil matches the floor's water-flow requirement - water passes fastest through gravel, more slowly through sand, slowest through clay, and not at all through bedrock.

### U4P4 — Alien Well Floor 5 + You Know the Drill (yellow)

**SCORE_BELOW_THRESHOLD** — `machine_attempt_number=16`, `wrong_choice_number=7`

> In the Alien Well's fifth floor and the drill task, the student changed soil canisters 16 times across the floor's two machines (three changes - one per layer - is optimal) and chose a wrong drilling depth 7 times before reaching clean water. This point earns green only when the drill hits the right depth on the first choice with at least one machine set optimally, or on the second choice with both machines set optimally. Wrong depths may indicate difficulty locating the water table: drilling too shallow finds no water, too deep hits bedrock, and water that has filtered through too few soil layers stays contaminated - the clean water lies just above the bedrock.

### U4P5 — Saving Cadet Anderson (yellow)

**EXCESS_ATTEMPTS** — `attempt_number=15`, `claim_wrong_number=8`, `reasoning_wrong_number=3`, `evidence_wrong_number=3`

> In Saving Cadet Anderson, the student built the argument explaining how water flooded the warehouse, but needed 15 submissions - 8 flagged for the claim, 3 for the reasoning, and 3 for evidence or completeness. This point earns green only when the correct argument is submitted with at most 2 incorrect submissions. Reasoning errors here reflect misconceptions the feedback names directly - water does not flow easily through bedrock, and water does not infiltrate upward - while claim errors suggest difficulty identifying the actual source of the flooding.

### U4P6 — Desert Delicacies (yellow)

**WRONG_SOIL_SELECTED** — `wrong_box_number=2`, `wrong_box_summary='the first box (chose Clay, needs Gravel) and the second box (chose Gravel, needs Sand)'`

> In Desert Delicacies, the student placed recording cameras on the soil they predicted would grow each seedling best, but chose a soil that does not match the seedling's water needs in the first box (chose Clay, needs Gravel) and the second box (chose Gravel, needs Sand). This point earns green only when at least 2 of the 3 garden boxes have the correct soil. Wrong choices may indicate difficulty connecting soil particle size to water retention: coarse soils like gravel let water drain past the roots, while fine-particle soils like clay trap too much of it, so each seedling needs the soil whose drainage matches its water requirement.

### U5P1 — If I Had a Nickel- Floors 1 & 2 (yellow)

**SOLVED_WITH_ASSIST** — `attempt_number=5`

> In If I Had a Nickel (floors 1 and 2), the student did not complete the evaporation glyph puzzle independently. After 5 incorrect arrangements, the in-game guide DANI ordered the tablets. This point earns green only when the student solves the puzzle on their own within 4 attempts. Needing this level of support may indicate the student would benefit from reviewing how temperature drives evaporation: the higher the temperature, the higher the evaporation rate.

### U5P2 — If I Had a Nickel- Floors 3 & 4 (yellow)

**SCORE_BELOW_THRESHOLD** — `floor3_attempts=24`, `floor4_attempts=10`

> In If I Had a Nickel (floors 3 and 4), the student used 24 condenser and evaporator interactions to solve the third-floor water chamber puzzle and 10 on the fourth floor. This point earns green only when at least one floor is solved within its optimal count (6 interactions on the third floor, 5 on the fourth) and the other stays within its partial range (at most 10 and 9, respectively). Many interactions may indicate trial-and-error switching rather than predicting the phase change each chamber needs: condensation removes energy to turn water vapor into liquid, and evaporation adds energy to turn liquid back into vapor.

### U5P3 — What Happened Here? (yellow)

**EXCESS_ATTEMPTS** — `wrong_argument_number=11`, `claim_wrong_number=7`, `reasoning_wrong_number=2`, `evidence_wrong_number=2`

> In What Happened Here?, while building the argument about why the collected water disappeared, the student made 11 flagged submissions - 7 for restating Aryn's claim instead of arguing against it, 2 for reasoning problems, and 2 for evidence or completeness problems. This point earns green only when fewer than 4 submissions are flagged. Claim errors suggest the student did not connect the evidence to the natural explanation - the water evaporated, leaving the salt behind - while the reasoning feedback names specific misconceptions to review, such as the water being filtered or transformed into salt.

### U5P4 — Water Problems Require Water Solutions (yellow)

**WRONG_SETTINGS_SELECTED** — `wrong_run_number=1`, `failure_phrase='the settings blocked sunlight, so the salt water could not heat up and evaporate'`

> In Water Problems Require Water Solutions, the student ran the solar desalinator with settings that did not produce the maximum amount of water: the settings blocked sunlight, so the salt water could not heat up and evaporate. This point earns green only when the desalinator collects the maximum water with no failed runs. Each failure mode maps directly to the water cycle - the salt water needs sunlight to heat it for evaporation, the glass surface must stay cool for condensation to form, and the roof angle determines whether the condensed water is collected.

## All code evaluations

| Point | Code | Triggered | Variables |
|---|---|---|---|
| U1P1 | _(no reason codes)_ | - | - |
| U1P2 | _(no reason codes)_ | - | - |
| U1P3 | WRONG_ARG_SELECTED | yes | attempt_number=3 |
| U1P4 | _(no reason codes)_ | - | - |
| U2P1 | SOLVED_WITH_ASSIST | no | attempt_number=1 |
| U2P1 | EXCESS_ATTEMPTS | no | attempt_number=2 |
| U2P2 | EXCESS_NAV_REMINDERS | yes | triggering_number=19 |
| U2P3 | EXCESS_NAV_REMINDERS | no | triggering_number=0, tera_count=0, aryn_count=0 |
| U2P4 | SOLVED_WITH_ASSIST | yes | attempt_number=5 |
| U2P4 | EXCESS_ATTEMPTS | no | attempt_number=6 |
| U2P5 | EXCESS_MISCLASSIFICATIONS | yes | wrong_number=10, claim_wrong=1, reasoning_wrong=3, evidence_wrong=6 |
| U2P6 | WRONG_EVIDENCE_SELECTED | yes | wrong_choice='waterfall height' |
| U2P7 | EXCESS_ATTEMPTS | yes | attempt_number=9, wrong_claim_number=1, both_wrong_number=3, irrelevant_evidence_number=4 |
| U3P1 | EXCESS_WRONG_RIVERS | yes | wrong_river_number=3 |
| U3P2 | EXCESS_SENSOR_REMINDERS | yes | downstream_reminder_number=13, redundant_reminder_number=22 |
| U3P3 | EXCESS_ATTEMPTS | yes | wrong_argument_number=5, claim_wrong_number=3, reasoning_wrong_number=2, evidence_wrong_number=0, backing_info_phrase='opened' |
| U3P4 | SOLVED_WITH_ASSIST | no | attempt_number=1 |
| U3P4 | EXCESS_ATTEMPTS | no | attempt_number=2 |
| U3P5 | EXCESS_WRONG_PLANTINGS | yes | wrong_planting_number=4 |
| U4P1 | SCORE_BELOW_THRESHOLD | yes | choice_phrase="chose 'it's any water found underground' instead of the correct answer on", duration_phrase='took 136 seconds to solve' |
| U4P2 | SOLVED_WITH_ASSIST | yes | attempt_number=5 |
| U4P2 | EXCESS_ATTEMPTS | no | attempt_number=6 |
| U4P3 | SCORE_BELOW_THRESHOLD | yes | floor3_attempts=7, floor4_attempts=6 |
| U4P4 | SCORE_BELOW_THRESHOLD | yes | machine_attempt_number=16, wrong_choice_number=7 |
| U4P5 | EXCESS_ATTEMPTS | yes | attempt_number=15, claim_wrong_number=8, reasoning_wrong_number=3, evidence_wrong_number=3 |
| U4P6 | WRONG_SOIL_SELECTED | yes | wrong_box_number=2, wrong_box_summary='the first box (chose Clay, needs Gravel) and the second box (chose Gravel, needs Sand)' |
| U5P1 | SOLVED_WITH_ASSIST | yes | attempt_number=5 |
| U5P1 | EXCESS_ATTEMPTS | no | attempt_number=6 |
| U5P2 | SCORE_BELOW_THRESHOLD | yes | floor3_attempts=24, floor4_attempts=10 |
| U5P3 | EXCESS_ATTEMPTS | yes | wrong_argument_number=11, claim_wrong_number=7, reasoning_wrong_number=2, evidence_wrong_number=2 |
| U5P4 | WRONG_SETTINGS_SELECTED | yes | wrong_run_number=1, failure_phrase='the settings blocked sunlight, so the salt water could not heat up and evaporate' |
