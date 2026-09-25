# Convince Anderson to Leave Her Base

The score measures how many attempts the player needs to submit a complete, scientifically correct argument explaining how water flooded the warehouse, plus a bonus for consulting the backing information.

## Scoring Criteria

* **3 points:** The player submits the correct argument within 1 to 3 attempts.
* **2 points:** The player submits the correct argument on the 4th attempt.
* **1 point:** The player submits the correct argument on the 5th attempt.
* **0 points:** The player requires more than 5 attempts, does not submit a correct argument, or does not attempt the task.

## Backing-Information Bonus

* **1 point:** The player opens the backing information that shows the warehouse layout at any time during the task.
* **0 points:** The player never opens it.

The maximum score for this progress point is **4 points** (3 points for the argument plus the 1-point bonus).

## Implementation Note

The current dashboard grading for this point (grading-logic/mhs-unit4-point5-grading.md) is based on the number of incorrect submissions before the correct argument only; the backing-information bonus is not applied in the dashboard color.

The dashboard's green band is also one attempt stricter than this rubric's color band. The dashboard grades green only when the correct argument is submitted with at most 2 incorrect submissions (correct on the 1st to 3rd attempt, the 3-point band above), and yellow from the 3rd incorrect submission on. Under this rubric a correct argument on the 4th attempt still earns 2 points, which falls inside the "Green: 2–4 points" band of the progress-point table, so a student with exactly 3 incorrect submissions is green by the rubric but yellow on the dashboard. The `>= 3` threshold is the settled value in the grading scripts and the Go grader (issues log item 5, 2026-09-17; re-confirmed 2026-09-24). Confirm which band the rubric intends before the rubric is quoted to teachers.
