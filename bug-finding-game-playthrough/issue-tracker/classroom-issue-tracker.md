# Classroom Issue Tracker — Claude Reference

This document summarizes the four gameplay issues recorded in the uploaded classroom issue tracker. It is intended as orientation for gameplay-log investigation, not as a statement of confirmed causes.

| Issue | Email date | Collection | Reporting org. | Unit / activity | Tracker description of affected case | Status |
|---|---|---|---|---|---|---|
| QA 1693 | 2026-09-23 | MHS-Release_V1.0.0 | Maryville | U2 / Classifier | Players who stop after U2 Classifier, but before finishing U2 | Tested |
| QA 1694 | 2026-09-29 | MHS-Release_V1.0.0 | Maryville | U3 / Supply Run / Crate 1 | Players that were skipped ahead from Unit 2 after experiencing the above classifier or argumentation bug | Identified |
| QA 1697 | 2026-09-23 | MHS-Release_V1.0.0 | Goodhue | U2 / Argumentation | Same idea as the Classifier bug | Tested |
| No Hansoft ID listed | 2026-10-05 | MHS-Release_V1.0.0 | Goodhue | U4 / Saving Cadet Anderson | Unsure, got around by refreshing | New |

## How to interpret the four cases

### QA 1693 — U2 Classifier

The tracker explicitly identifies a progression boundary: the affected players made it to/through the Unit 2 Classifier activity but did not finish Unit 2. The log analysis should determine exactly where their event sequence stops matching successful Unit 2 playthroughs.

### QA 1697 — U2 Argumentation

The tracker describes this as the "same idea as the Classifier bug." Treat that wording as an indication of a similar reported progression problem, **not** proof that QA 1693 and QA 1697 share the same underlying defect. Compare their event/state transitions to determine whether a common mechanism exists.

### QA 1694 — U3 Supply Run / Crate 1

The tracker specifically identifies affected players who had previously experienced the Unit 2 Classifier or Argumentation problem and were skipped ahead into Unit 3. This creates an important dependency question: did the Unit 3 problem arise independently, or did those players enter Unit 3 without some state that is normally initialized through Unit 2? Test both explanations.

### U4 — Saving Cadet Anderson

The tracker contains very limited diagnostic information. It states that the situation was "unsure" and that the player got around it by refreshing. The refresh behavior is valuable evidence, but the exact failure mechanism is unknown. Compare events/state immediately before the refresh with events/state immediately after the resumed session.

## Cross-case questions worth testing

- Do QA 1693 and QA 1697 fail at a similar type of post-activity quest transition?
- Are expected completion/transition events present in successful controls but absent in affected U2 cases?
- Do the QA 1694 students enter Unit 3 with different prerequisite state from normally progressing students?
- Does refresh/reload reconstruct or reset a missing state in the U4 case?
- Are there repeated, missing, or out-of-order events immediately before progression stops?
- Are suspicious patterns truly specific to affected students, or do they also occur in successful playthroughs?

See the individual issue files for exact tracker records and investigation targets.
