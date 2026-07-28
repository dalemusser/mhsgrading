# Teacher-Facing Feedback — Yellow Progress Points (Units 1–2)

**Player:** `wenyi050126-1` (test playthrough, log dump `tests/05-01-26/wenyi050126-1.stratalog.logdata.json`)
**Expected dashboard colors (Units 1–2, in order U1P1–U1P4, U2P1–U2P7):**
Green, Green, **Yellow**, Green, Green, **Yellow**, Green, Green, Green, Green, **Yellow**

Per `tests/TEST_RESULTS.md`, the three expected-yellow progress points are:

| Dashboard position | Point | Activity |
|---|---|---|
| 3 | U1P3 | Defend the Expedition |
| 6 | U2P2 | Foraged Forging (graded segment: navigating to find Captain Toppo) |
| 11 | U2P7 | Which Watershed? Part II |

For this player, the production grading scripts and the expected colors agree on all three points (verified by re-running each production script's logic against the log).

---

## Unit 1, Progress Point 3: Defend the Expedition

**Yellow-result trigger:**
The grading script marks this point yellow when any wrong-argument dialogue node (`DialogueNodeEvent:70:25` or `DialogueNodeEvent:70:33`) appears in the attempt window. The log contains `DialogueNodeEvent:70:25` — the player's first argument submission was incorrect. The reason code is `WRONG_ARG_SELECTED` with `attempt_number = 2` (threshold: correct on the first attempt).

**Performance summary:**
In the first real use of the argumentation engine, the player assembled and submitted an argument about whether planet WAT-247 has freshwater. The first submission was incorrect; the player then revised two of the three argument components and submitted a correct argument on the second attempt, about one minute later.

**Gameplay evidence:**
- First submission `A,1,II` at 17:52:37 (`submitAnswerEvent`), immediately followed by wrong-argument node `DialogueNodeEvent:70:25`.
- The player then removed node `A` and added node `B`, and removed node `II` and added node `I`, before submitting `B,1,I` at 17:53:40 — the success node `DialogueNodeEvent:70:7` fired, and the session closed.
- The player opened the Backing Info panel at 17:52:02 (before the first submission) and opened it twice more between the two attempts (17:53:20–17:53:22); each of the later openings lasted under one second.
- Total attempts in the graded window: 2 (green requires a correct first submission).

**Possible learning need:**
This progress point targets identifying the claim that is logically supported by the provided evidence and reasoning (claim–evidence–reasoning structure). Because the first submission was wrong on two components, the player may need additional support connecting a claim to the evidence and reasoning that support it. This is an interpretation — the logs cannot determine whether the error reflected a conceptual gap or an accidental selection.

**Potentially underused support:**
The player demonstrably used the Backing Info panel and revised after Dr. Toppo's feedback (both are logged). However, the between-attempt Backing Info openings each lasted less than one second, so the player may not have fully read that reference material. The logs cannot confirm whether the player used the hover-over node definitions or the optional dialogue choices for asking Dr. Toppo about claims, evidence, and reasoning.

**Suggested instructor intervention:**
Ask the student to explain, in their own words, what a claim, evidence, and reasoning each do in an argument, and then to explain why the correct claim about WAT-247's freshwater is supported by the evidence. Comparing their first (incorrect) and second (correct) submissions and articulating what changed would directly target the skill this point measures.

**Dashboard pop-up text:**
The player completed the freshwater argument for Unit 1, but the first submission was incorrect, and the correct argument was submitted only on the second attempt — which produced the yellow classification (green requires a correct first submission). After the incorrect attempt, the player revised two of the three argument components and succeeded about a minute later. The logs show the player briefly opened the Backing Info panel between attempts, but each opening lasted under a second, so the reference material may not have been fully used. The first incorrect attempt may indicate difficulty identifying which claim is supported by the given evidence and reasoning. Consider asking the student to explain the roles of claim, evidence, and reasoning, and to describe what they changed between their two submissions and why.

---

## Unit 2, Progress Point 2: Foraged Forging (Finding Captain Toppo)

**Yellow-result trigger:**
The grading script counts wrong-direction reminder dialogues (nine possible `DialogueNodeEvent` keys) between the activity start (`questFinishEvent:21`) and end (`DialogueNodeEvent:20:26`). Green requires at most 1; this player triggered 7, so the point is yellow. The reason code is `BAD_FEEDBACK` with `triggering_number = 7` (threshold ≤ 1).

**Performance summary:**
After repairing the hoverboard, the player had to interpret Anderson's clue — Captain Toppo is "northwest of here on a hill at an elevation of approximately 90 feet" — place a waypoint on the topographic map, and navigate there. The player did place a waypoint and ultimately reached Toppo about six and a half minutes after the segment began, but while traveling, wrong-direction reminder dialogues fired seven times.

**Gameplay evidence:**
- Activity window: 18:08:42 (`questFinishEvent:21`) to 18:15:11 (`DialogueNodeEvent:20:26`), about 6.5 minutes.
- The player opened the map at 18:12:53 and placed a waypoint (drag ended at 18:12:58) — direct evidence the map and waypoint tools were used.
- The same wrong-direction reminder node (`DialogueNodeEvent:28:179`) was logged seven times between 18:13:20 and 18:13:32 — a roughly 12-second span shortly after the waypoint was placed.
- The player reached Toppo about two minutes after the last reminder; no further wrong-direction dialogues were logged.

**Possible learning need:**
This progress point targets applying topographic-map knowledge to navigation: connecting narrative clues (direction, elevation, terrain) to map features and testing a route. The wrong-direction reminders indicate the player traveled through an off-course area; this may reflect difficulty translating "northwest" and "a hill at about 90 feet of elevation" into a map location using the compass and contour lines. The current logs cannot determine whether the player misread the map, placed the waypoint at an unintended location, or simply took an indirect route; note that all seven reminders occurred within a single 12-second span rather than being spread across the segment.

**Potentially underused support:**
The map and waypoint tools were used (logged). However, the available logs do not show evidence that the player replayed the optional Topography video that Anderson offers, or used DANI's map guidance connecting Anderson's clues to contour lines and the compass. The player may have benefited from re-checking the map against the clue before or during travel — the map was opened once within the graded window.

**Suggested instructor intervention:**
Ask the student to open a topographic map and point to northwest using the compass, then identify a hill whose contour lines indicate roughly 90 feet of elevation. Reviewing how closely spaced contour lines show steepness, and how contour indices give elevation, directly addresses the navigation skill this point measures. A short exercise — "given this clue, where would you place the waypoint, and why?" — would let the student verbalize their route-planning reasoning.

**Dashboard pop-up text:**
The player successfully found Captain Toppo, but wrong-direction reminder dialogues fired seven times during the search, well above the success threshold of at most one, producing the yellow classification. The logs show the player opened the topographic map and placed a waypoint; all seven reminders then occurred within about 12 seconds while traveling, and the player reached Toppo roughly two minutes later. The off-course travel may indicate difficulty translating Anderson's clue — northwest, on a hill at about 90 feet of elevation — into a map location using the compass and contour lines. The player may not have fully used DANI's map guidance or the optional topography video review. Consider asking the student to locate northwest on the map compass and to find a hill of about 90 feet using contour lines, explaining their reasoning aloud.

---

## Unit 2, Progress Point 7: Which Watershed? Part II

**Yellow-result trigger:**
Green requires the success node (`DialogueNodeEvent:27:7`) **and** at most 3 incorrect evidence selections in the attempt window. The player did reach the success node, but four incorrect-argument nodes fired (`27:11`, `27:13`, `27:15`, `27:18`), so `neg_count = 4 > 3` → yellow. The reason code is `WRONG_ARG_SELECTED` with `attempt_number = 5` (threshold ≤ 4 attempts).

**Performance summary:**
The player built the argument about whether the Eastern or Western watershed is larger. The first four submissions were incorrect; the correct argument was submitted on the fifth attempt, about two and a half minutes after the first. Under the rubric, a correct argument on the fifth attempt earns 1 of 3 points.

**Gameplay evidence:**
- Five `submitAnswerEvent` records: `A,1,I` (18:33:36), `B,1,I` (18:33:46), `C,1,I` (18:34:10), `D,1,I` (18:34:31) — each followed by an incorrect-argument node — and the correct `A,1,II` at 18:35:06, followed by the success node `DialogueNodeEvent:27:7`.
- Across the four incorrect attempts, the player changed only one component per submission, cycling it through options `A`, `B`, `C`, `D` in order; the successful fifth attempt returned to `A` and swapped component `I` for `II`.
- Consecutive submissions came 10–25 seconds apart.
- Both in-tool reference panels were opened just before the first submission — "BackingInfoPanel – Watershed Graph" (18:33:33) and "BackingInfoPanel – Waterfall Data" (18:33:34) — but each stayed open for under one second, and neither was reopened during the four incorrect attempts.

**Possible learning need:**
This point targets selecting scientifically relevant evidence: flow rate indicates relative watershed size, while waterfall height, salinity, and distance to the ocean do not. The in-order cycling of one component with short gaps between submissions may indicate the player was iterating through options rather than using the collected observations to identify the relevant evidence — though the logs cannot confirm the player's reasoning. The player may need additional support connecting flow rate with relative watershed size and distinguishing relevant evidence from other collected observations.

**Potentially underused support:**
The logs show the player opened both reference tools — the watershed–flow-rate explanation and the waterfall-data comparison table — but each for less than one second, so the player may not have fully used them. Dr. Toppo's per-attempt feedback, which identifies the specific problem with an incorrect argument, was available after each of the four incorrect submissions; the logs cannot show how thoroughly it was read. The optional pre-task review dialogues with Dr. Toppo (claims, evidence, reasoning, watershed definition) are also available but their use cannot be verified from these logs.

**Suggested instructor intervention:**
Guide the student through the waterfall comparison table and ask which of the four measurements (flow rate, waterfall height, salinity, distance to the ocean) could indicate how much land drains to each river — and why the others cannot. Then ask the student to restate the winning argument in their own words: which watershed is larger, what evidence shows it, and how the evidence supports the claim. A short practice item asking the student to sort evidence into "relevant" and "not relevant" for a given question would directly target this skill.

**Dashboard pop-up text:**
The player completed the watershed argument, but needed five attempts — four incorrect submissions before the correct one — exceeding the threshold of four attempts and producing the yellow classification. The logs show the player changed one argument component at a time, cycling through the options in order, with 10–25 seconds between submissions. Both reference tools — the watershed flow-rate explanation and the waterfall comparison table — were opened only briefly (under one second each) before the first attempt and not reopened afterward. This pattern may indicate the player was iterating through choices rather than using the collected waterfall data to identify the relevant evidence. Consider walking through the comparison table together, asking the student why flow rate — rather than waterfall height, salinity, or distance to the ocean — indicates which watershed is larger.

---

## Verification and Documentation Notes

1. **Colors verified.** For all three points, re-running the production grading logic against the log reproduces the expected yellow (U1P3: yellow node in window; U2P2: 7 wrong-direction dialogues > 1; U2P7: success present but `neg_count` 4 > 3). No expected-vs-actual conflict exists for Units 1–2, so no expected-color override was needed.
2. **U2P2 naming/rubric inconsistency (reported, not silently resolved).** The grading file is titled "Foraged Forging," but its graded window (`questFinishEvent:21` → `DialogueNodeEvent:20:26`) and reason code cover the subsequent "Finding Toppo" navigation segment (Task 1.3 in the Unit 2 combo doc). Additionally, the rubric for this point scores *waypoint placement accuracy*, while the grading code counts *wrong-direction reminder dialogues* — related but not identical measures. The feedback above follows the grading code, as instructed.
3. **Argument node labels are not documented in the repo.** The U1/U2 "Arg Details" documents referenced by the combo docs are not present, so submissions are described by their logged node labels (`A,1,II`, etc.) without asserting which label corresponds to which claim/evidence/reasoning option.
4. **Resource-use statements are log-grounded.** Backing-info panel openings (with durations), map opens, and waypoint placements are taken directly from `argumentationToolEvent` and `Topographic Map Event`/`TopographicMapEvent` records; where usage could not be verified (videos, optional review dialogues, hover definitions), cautious wording is used.
