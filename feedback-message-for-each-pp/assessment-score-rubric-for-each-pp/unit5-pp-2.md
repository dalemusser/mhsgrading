# Water Chamber Puzzles: Third and Fourth Floors

This progress point combines the water chamber puzzles on the third and fourth floors of the dungeon. For each floor, the score measures how many times the player interacts with the condenser and evaporator panels while completing the floor — fewer interactions indicate that the player predicted the phase change each chamber needed rather than switching by trial and error.

## A. Third Floor

A minimum of 5 panel interactions is needed to complete this floor: the four single-chamber machines and the dual-chamber machine, whose condenser and evaporator switches each count as an interaction.

* **2 points:** The player completes the floor with 6 or fewer condenser/evaporator interactions.
* **1 point:** The player completes the floor with 7 to 10 interactions.
* **0 points:** Anything else (11 or more interactions, or the floor not completed).

## B. Fourth Floor

A minimum of 4 panel interactions is needed to complete this floor.

* **2 points:** The player completes the floor with 5 or fewer condenser/evaporator interactions.
* **1 point:** The player completes the floor with 6 to 9 interactions.
* **0 points:** Anything else (10 or more interactions, or the floor not completed).

## Overall Score

The maximum combined score for this progress point is **4 points**.

## Implementation Note

The dashboard grading for this point (grading-logic/mhs-unit5-point2-grading.md) counts every condenser and evaporator toggle logged on the floor, including the third floor's dual-chamber machine (added on 2026-09-24; before that only the single-chamber machines were counted, which under-counted the third floor). One difference from this rubric remains: a floor with no logged interactions scores 2 points in the dashboard, whereas the rubric gives 0 for a floor that was not completed. A student cannot reach the end of the dungeon without playing both floors, so this only shows up when a floor is skipped with the debug menu or its records are lost.
