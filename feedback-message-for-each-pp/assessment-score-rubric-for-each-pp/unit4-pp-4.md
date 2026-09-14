# Alien Well: Fifth Floor and the Drill Task

This progress point combines the two soil-machine puzzles on the fifth floor of the alien well with the drilling task that follows.

## A. Fifth-Floor Soil Machines

One point is available for each of the two rooms; a point is earned when the player sets the room’s machine to the correct solution on the first attempt.

* **1 point (Room 5-1):** The player selects **clay** for the top canister on the first attempt **and** does not change the bottom canister.
* **1 point (Room 5-2):** The player selects **clay** for the bottom canister on the first attempt, **or** selects **sand** for the top canister and does not change the bottom canister.
* **0 points** for a room whose machine is changed repeatedly before reaching the correct setting, or that is not attempted.

The maximum score for the soil machines is **2 points**.

## B. Drill Task

The score measures how many attempts the player needs to choose a drilling depth that reaches usable groundwater.

* **2 points:** The player selects layer 3 or layer 4 on the first attempt.
* **1 point:** The player selects layer 3 or layer 4 on the second attempt.
* **0 points:** Anything else (a correct layer only after two attempts, or the task not attempted).

The maximum score for the drill task is **2 points**.

## Overall Score

The maximum combined score for this progress point is **4 points**.

## Scoring Clarification

The rubric describes the fifth-floor machine solutions inconsistently: the student-action column lists clay/sand combinations per room, the log-tag column lists **sand** for both machines, and the score formula simply awards 1 point per room for a correct first-attempt solution. The current dashboard script (grading-logic/mhs-unit4-point4-grading.md) implements the formula by counting canister changes — exactly one change per layer on the two-layer machine and exactly one change on the single-layer machine. The intended correct settings for each canister should be confirmed before this rubric is quoted to teachers.
