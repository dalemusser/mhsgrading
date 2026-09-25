# Plant the Superfruit Seeds in the Correct Locations

The score measures whether the player plants each of the four superfruit seeds in a garden plot that receives the dissolved super-nutrient carried downstream by the river.

* **+1 point:** The player selects a correct garden location.
* **−0.5 point:** The player selects an incorrect garden location.

```text
Final Score =
(Number of correct location selections × 1)
− (Number of incorrect location selections × 0.5)
```

The player selects 4 garden boxes, so the maximum score for this progress point is **4 points**.

## Implementation Note

The rubric’s on-track band for this point is 3 to 4 points (at most one wrong planting, with no penalty carried past the four boxes). The dashboard script (grading-logic/mhs-unit3-point5-grading.md) turns green at 2.5 points or more. With four seeds the two say the same thing: one wrong planting scores 3 − 0.5 = 2.5 and stays green, two wrong plantings score 2 − 1 = 1 and turn yellow. The 2.5 threshold was confirmed with the grading team on 2026-09-21 (decision A5), and the grading file's rule table, Analytics Script, Production Script and reason code all use it as of 2026-09-24.
