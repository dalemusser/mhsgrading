# Evaporation Rate Glyph Puzzle

The score is determined by the number of attempts the player requires to submit the correct order of the tablets ranking evaporation rates.

* **2 points:** The player submits the correct order on the first attempt.
* **1 point:** The player submits the correct order on the second or third attempt.
* **0 points:** The player requires 4 or more attempts, does not submit a correct order, or does not attempt the puzzle.

The maximum score for this progress point is **2 points**.

## Implementation Note

The current dashboard grading for this point (grading-logic/mhs-unit5-point1-grading.md) stays green as long as the player solves the puzzle independently within 4 attempts (the yellow feedback nodes fire from the 4th incorrect submission on), one attempt more lenient than this rubric’s 0-point band. Confirm which threshold the rubric intends.

DANI's assist (offered after the 4th incorrect submission, forced after the 5th) does not currently place the tablets in the game: assisted players still have to submit the correct order themselves before the game moves on (observed on builds 20260902 and 20260914). This does not change the rubric's outcome, because assistance is only reached at the 4th attempt or later, which is already the 0-point band; the dashboard likewise grades every assisted run yellow and labels it as solved with assistance.
