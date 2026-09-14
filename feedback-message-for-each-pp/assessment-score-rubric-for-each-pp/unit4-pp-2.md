# Infiltration Glyph Puzzle

The score is determined by the number of attempts the player requires to submit the correct order of the glyph pieces showing how water infiltrates different soil types.

* **2 points:** The player submits the correct order on the first attempt.
* **1 point:** The player submits the correct order on the second attempt.
* **0 points:** The player requires more than 2 attempts, does not submit a correct order, or does not attempt the puzzle.

The maximum score for this progress point is **2 points**.

## Implementation Note

The current dashboard grading for this point (grading-logic/mhs-unit4-point2-grading.md) stays green as long as the player solves the puzzle independently within 3 attempts (the yellow feedback nodes fire from the 3rd incorrect submission on), one attempt more lenient than this rubric’s 0-point band. Confirm which threshold the rubric intends.
