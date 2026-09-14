# Teacher-Facing Feedback — Yellow Progress Points (Units 1–5)

**Player:** `wenyi090326-3` (test playthrough of build 20260902-12353, played 2026-09-05; log dump `playthrough-logs-and-results/09-03-26-3/wenyi090326-3.stratalog.logdata.json`, 11,537 records, player id `6a9a0779e2ada9cb13ea75c0`)
**Expected dashboard colors (in order U1P1–U1P4, U2P1–U2P7, U3P1–U3P5, U4P1–U4P6, U5P1–U5P4):**
Green, Green, **Yellow**, Green, Green, **Yellow**, Green, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, Green, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**

The expected colors are the `09-03-26-3` fixture in `rubric-validation/config/fixtures.yaml` (grading-readiness audit re-run 2026-09-06, cross-checked against the tester's declared intent). Both validation suites reproduce them: `rubric-validation` (26/26 colors) and `reason-code-validation` (26/26, exactly one reason code triggered for each yellow point). This was a deliberately imperfect test run, so 20 of the 26 points are yellow. Timestamps below are the log's client timestamps (UTC). The first ten minutes of the dump (21:10–21:20) are an abandoned Unit-1 restart on an older build and fall outside every graded window.

| Dashboard position | Point | Activity | Reason code (variables) |
|---|---|---|---|
| 3 | U1P3 | Defend the Expedition | `WRONG_ARG_SELECTED` (attempt_number 3) |
| 6 | U2P2 | Foraged Forging (graded segment: finding Captain Toppo) | `EXCESS_NAV_REMINDERS` (19 reminders) |
| 8 | U2P4 | Investigate the Temple | `SOLVED_WITH_ASSIST` (5 wrong arrangements) |
| 9 | U2P5 | Classified Information | `EXCESS_MISCLASSIFICATIONS` (10 wrong: 1 claim, 3 reasoning, 6 evidence) |
| 10 | U2P6 | Which Watershed? Part I | `WRONG_EVIDENCE_SELECTED` (waterfall height) |
| 11 | U2P7 | Which Watershed? Part II | `EXCESS_ATTEMPTS` (9 submissions: 2 claim, 6 irrelevant evidence) |
| 12 | U3P1 | Supply Run (Establishing a Foothold) | `EXCESS_WRONG_RIVERS` (3 wrong crates) |
| 13 | U3P2 | Pollution Solution Part I | `EXCESS_SENSOR_REMINDERS` (13 downstream, 22 redundant) |
| 14 | U3P3 | Pollution Solution Part II (Pollution Argument) | `EXCESS_ATTEMPTS` (5 wrong: 2 claim, 3 reasoning; reference panel opened) |
| 16 | U3P5 | Part of a Balanced Ecosystem (Plant the Superfruit Seeds) | `EXCESS_WRONG_PLANTINGS` (4 wrong plots) |
| 17 | U4P1 | Well What Have We Here? | `SCORE_BELOW_THRESHOLD` (wrong water-table answer; 136 s puzzle) |
| 18 | U4P2 | Power Play – Floors 1 & 2 (Infiltration Glyph) | `SOLVED_WITH_ASSIST` (4 wrong arrangements) |
| 19 | U4P3 | Power Play – Floors 3 & 4 | `SCORE_BELOW_THRESHOLD` (7 and 6 canister changes) |
| 20 | U4P4 | Power Play – Floor 5 (+ drill task) | `SCORE_BELOW_THRESHOLD` (16 canister changes; 7 wrong depths) |
| 21 | U4P5 | Saving Cadet Anderson | `EXCESS_ATTEMPTS` (15 submissions: 8 claim, 3 reasoning, 3 evidence) |
| 22 | U4P6 | Desert Delicacies | `WRONG_SOIL_SELECTED` (boxes 1 and 2 wrong) |
| 23 | U5P1 | If I Had a Nickel – Floors 1 & 2 | `SOLVED_WITH_ASSIST` (4 wrong arrangements) |
| 24 | U5P2 | If I Had a Nickel – Floors 3 & 4 | `SCORE_BELOW_THRESHOLD` (8 and 10 interactions) |
| 25 | U5P3 | What Happened Here? | `EXCESS_ATTEMPTS` (11 flagged: 7 claim, 2 reasoning, 2 evidence) |
| 26 | U5P4 | Water Problems Require Water Solutions | `WRONG_SETTINGS_SELECTED` (1 failed run, sunlight blocked) |

For every point, re-running the production grading logic and the reason-code scripts against the log reproduces the expected yellow and the variables shown above.

---

## Unit 1, Progress Point 3: Defend the Expedition

**Yellow-result trigger:**
Green requires that no wrong-argument node (`DialogueNodeEvent:70:25`) appears inside the attempt window (previous `questActiveEvent:34` → latest `questActiveEvent:34`, 21:19:30–21:32:52). The node fired twice. Reason code `WRONG_ARG_SELECTED`, `attempt_number = 3` (green requires a correct first submission).

**Performance summary:**
In the first graded use of the argumentation engine (the WAT-247 freshwater argument), the player submitted three times within 11 seconds. The first submission was incorrect, the second was the identical argument resubmitted after removing and re-adding one node, and the third, with one component swapped, was correct.

**Gameplay evidence:**
- The argumentation tutorial session (21:31:30–21:32:01) was completed with a single submission (`A,1,I`).
- The freshwater session opened at 21:32:10; the in-tool Backing Info panel was opened at 21:32:11 (its close is not logged), and the player hovered over nodes `1`, `A`, `I` and `II` for 0–2 seconds each before the first submission.
- Submission 1 `A,1,II` at 21:32:21 → wrong-argument feedback (`70:25`): "You have chosen the claim that Europa Corp made. Toppo is trying to make a different point so she will need a different claim."
- Submission 2 `A,1,II` at 21:32:29 — the same argument again (node `II` was removed and re-added) → the same feedback.
- Submission 3 `A,1,I` at 21:32:32 → success (`70:7`: "Great! You chose the main idea that Toppo is trying to support, also known as the claim."). The session closed 22 seconds after it opened.

**Possible learning need:**
This point targets identifying the claim that the given evidence and reasoning support. The feedback twice named the claim as the problem, and the component the player finally changed (`II` → `I`) resolved it, so the player may need support distinguishing Toppo's claim from the competing Europa Corp claim by checking which conclusion the evidence actually supports. Resubmitting an unchanged argument may also indicate that the feedback was not used before the second attempt. Both are interpretations — the logs cannot show what the player read.

**Potentially underused support:**
The Backing Info panel was opened once at the start of the session (logged), and the node hover-overs that reveal each option's text lasted at most two seconds each. Dr. Toppo's feedback after the first submission explicitly identified the wrong claim, but the second submission changed nothing. The logs cannot show whether the player used the optional dialogue choices to ask Dr. Toppo about claims, evidence and reasoning, or watched the argumentation video.

**Suggested instructor intervention:**
Ask the student to state, in their own words, what Toppo is trying to prove about WAT-247 and what Europa Corp claimed, then to explain which of the two the freshwater evidence supports and why. Having the student read the feedback aloud after an incorrect attempt and say what they will change before resubmitting targets the resubmit-unchanged pattern directly.

**Dashboard pop-up text:**
The player completed the Unit 1 freshwater argument, but the first submission chose the wrong claim and the correct argument came only on the third attempt, so the point is yellow (green requires a correct first submission). All three submissions were made within 11 seconds; the second repeated the first argument unchanged even though Dr. Toppo's feedback had already identified the claim as the problem. The Backing Info panel was opened once at the start, and node descriptions were hovered for at most two seconds. The pattern may indicate difficulty distinguishing Toppo's claim from Europa Corp's, or feedback not being used between attempts. Consider asking the student to explain which conclusion the evidence supports and to say what they will change before each resubmission.

---

## Unit 2, Progress Point 2: Foraged Forging (Finding Captain Toppo)

**Yellow-result trigger:**
The script counts wrong-direction reminder dialogues (six conversation-28/59 keys) between the activity start (`questFinishEvent:21`, 21:40:44) and end (`DialogueNodeEvent:20:26`, 21:46:05). Green allows at most one; 19 fired. Reason code `EXCESS_NAV_REMINDERS`, `triggering_number = 19`.

**Performance summary:**
After the hoverboard segment, the player had to turn Anderson's clue about Captain Toppo's location into a waypoint and travel there. The player opened the map, checked the 90-ft legend entry, placed and adjusted a waypoint within 15 seconds, and reached Toppo about 5.5 minutes after the segment began — but the same clue reminder fired 19 times on the way.

**Gameplay evidence:**
- Map opened 21:43:01; legend entry "90 ft" selected 21:43:11; waypoint set 21:43:13 and moved once (21:43:14); map closed 21:43:16 — the only map use in the window.
- Reminder `28:179` fired 19 times: 16 times between 21:43:38 and 21:43:58 (a 20-second span starting 22 seconds after the map closed), then three more at 21:44:55–21:45:01. Its text: "Anderson said that Toppo's pod was near our original location. We should look for two rock formations with contour lines close together nearer to where we started. Remember you can move the waypoint on your map at any time."
- The map was not reopened after any reminder; Toppo was reached at 21:45:27 (`20:1`), 26 seconds after the last reminder.

**Possible learning need:**
This point targets integrating clue information (direction, elevation, terrain features) with the topographic map. The reminders indicate the player traveled through an area inconsistent with the clue immediately after placing the waypoint. The reminder names two closely spaced rock formations (tight contour lines) near the starting point as the target, so the player may have difficulty matching that terrain description to the map, or may have placed the waypoint elsewhere. The logs cannot distinguish a misread map from an indirect route.

**Potentially underused support:**
Map, legend and waypoint use are logged (one 15-second session). The reminder itself invites the player to move the waypoint, but no map opening followed any of the 19 reminders, so the player may not have used the reminder to re-check the waypoint. The logs do not show whether the player revisited Anderson's clue in the chat history or used DANI's guidance on contour spacing.

**Suggested instructor intervention:**
Give the student the clue text and a topographic map and ask them to point out where contour lines are close together (steep rock formations) and to place a waypoint there, explaining why. Then ask what they would do when an in-game reminder says the route is inconsistent with the clue — reopen the map and compare — to build the habit of checking the map mid-route.

**Dashboard pop-up text:**
The player found Captain Toppo, but the wrong-direction reminder fired 19 times during the search, far above the threshold of one, so the point is yellow. The logs show one 15-second map session (legend "90 ft" checked, waypoint placed and adjusted) right before travel; 16 reminders then fired within 20 seconds, and the map was not reopened afterward. The reminder text points to two rock formations with closely spaced contour lines near the start, so the off-course travel may indicate difficulty matching that terrain description to the map, or a waypoint placed elsewhere. Consider asking the student to locate closely spaced contour lines on a map and explain what they show, and to re-check the map whenever a reminder appears.

---

## Unit 2, Progress Point 4: Investigate the Temple

**Yellow-result trigger:**
Green requires the solved-on-own node (`74:21`) and none of the yellow nodes (`74:16`, `74:17`, `74:20`, `74:22`) in the window (previous `DialogueNodeEvent:23:17` → latest, ending 21:59:02). Node `74:17` (fifth wrong arrangement, assist offered) fired. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 5` (green requires an independent solution within five attempts).

**Performance summary:**
In the watershed glyph puzzle (ordering terrain pieces by watershed size and flow rate), the player submitted five incorrect arrangements over about three minutes, accepted DANI's offer of help after the fifth, and DANI placed the pieces. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- Glyph pieces were docked from 21:55:19; wrong-arrangement feedback at 21:55:31 (`74:4`), 21:55:55 (`74:6`: "These pieces resemble watersheds of varying size. Perhaps that is a clue to the correct order."), 21:56:22 (`74:10`: several pieces wrong; DANI offered Toppo's watershed lesson), 21:57:58 (`74:15`: "You should try ordering the watershed pieces by size."), 21:58:30 (`74:17`: "Would you like me to assist, TK?").
- The player accepted the assist ("Sure. I'm stuck", `74:18`, 21:58:34); the completion line `74:21` followed at 21:58:39.
- Logged use of support: after the second miss the player chose the follow-up question "Sizes of watersheds?" (`74:11`) and received DANI's watershed definition (`74:23`); after the third miss the player accepted the video replay ("Sure. Let's watch it.", `74:13`; "Streaming the video to your holo-watch", `74:24`).
- Between the fourth feedback (21:57:58) and the fifth submission, two docking actions were logged (21:58:10, 21:58:13), so pieces were being rearranged between attempts.

**Possible learning need:**
This point targets connecting drainage-area size to relative flow rate and using that pattern to order the pieces. Five wrong orders despite the explicit hint to order by size may indicate difficulty judging relative watershed size from the terrain pieces — comparing drainage areas rather than elevation or slope. This is an interpretation.

**Potentially underused support:**
The player demonstrably used two supports (the watershed-definition question and the video replay are logged as dialogue choices), and DANI's hint sequence escalated as designed. The logs cannot show how much of the replayed video was watched (no duration is logged) or whether the player compared the pieces with one another before each submission.

**Suggested instructor intervention:**
Show the student two or three watershed diagrams of different sizes and ask them to rank them and predict which main river carries more water and why. Then ask what features of a terrain piece indicate drainage area (the extent of land draining to the river) versus features that do not (height alone). A short ordering exercise with feedback would target the skill directly.

**Dashboard pop-up text:**
The player completed the watershed glyph puzzle only with DANI's help: five arrangements were submitted incorrectly over about three minutes, and after the fifth the player accepted DANI's offer to place the pieces, which makes the point yellow (green requires an independent solution within five attempts). The logs show the player used the available supports — asking DANI about watershed sizes after the second miss and accepting the replay of Dr. Toppo's watershed lesson after the third — yet the next two arrangements were still wrong even after the hint to order the pieces by size. This may indicate difficulty judging relative drainage-area size from the terrain pieces. Consider asking the student to rank a few watershed diagrams by size and explain which river would carry more water.

---

## Unit 2, Progress Point 5: Classified Information

**Yellow-result trigger:**
Score = correct classifications − (incorrect classifications ÷ 3) inside the window (previous `DialogueNodeEvent:23:42` → latest, ending 22:06:31); green requires a score of at least 4. The player made 6 correct and 10 incorrect selections: 6 − 3.33 = 2.67. Reason code `EXCESS_MISCLASSIFICATIONS`, `wrong_number = 10` (1 claim, 3 reasoning, 6 evidence); green allows at most six incorrect selections.

**Performance summary:**
Repairing DANI required classifying six highlighted passages of an argument as claim, evidence or reasoning. The player made 16 selections in 2 minutes 37 seconds (22:02:48–22:05:25): the first six were all incorrect, after which correct and incorrect selections alternated until all six passages were classified.

**Gameplay evidence:**
- Feedback sequence: wrong ×6 (22:02:48–22:03:49), then correct, correct, wrong, correct, correct, wrong, correct, wrong, wrong, correct (22:04:16–22:05:17).
- Misclassified passages by their actual role: six were evidence (e.g., "Oh no! That was evidence. The pollution sensor data was collected from the environment."), three were reasoning (e.g., "...is reasoning because it is an accurate statement that explains why the evidence supports the claim."), one was the claim ("Too bad! That was the claim. Stating that steam is gaseous water is the claim because it answers the driving question...").
- Selections came 4–27 seconds apart; DANI closed the activity with "Now making arguments should be a breeze!"

**Possible learning need:**
This point targets recognising a passage's role from its function in the whole argument. Six of the ten errors were on evidence passages and three on reasoning passages, so the player may have difficulty separating information collected from the environment (evidence) from statements that explain why that information supports the claim (reasoning). This is an interpretation.

**Potentially underused support:**
Dr. Toppo's feedback after each wrong selection states the passage's actual role and why. Errors continued after that feedback (four incorrect selections after the first correct one), so the player may not have fully applied it. The logs cannot confirm whether the player re-read the whole argument before each selection.

**Suggested instructor intervention:**
Give the student a short argument and ask them to underline the sentences that report observations or data (evidence) and the sentences that explain why the data supports the conclusion (reasoning), then compare. Emphasise the test "Was this collected from the environment, or does it explain?" and practise with two or three fresh passages.

**Dashboard pop-up text:**
The player completed the argument-component classification task but made 10 incorrect selections (6 correct), well above the six allowed, so the point is yellow. The first six selections were all wrong, and errors continued after Dr. Toppo's corrective feedback. Of the ten errors, six were on evidence passages and three on reasoning passages, which may indicate difficulty separating information collected from the environment (evidence) from statements that explain how the evidence supports the claim (reasoning). Consider giving the student a short argument and asking them to mark evidence versus reasoning sentences and to justify each using "was it observed, or does it explain?"

---

## Unit 2, Progress Point 6: Which Watershed? Part I

**Yellow-result trigger:**
Green requires the flow-rate choice (`DialogueNodeEvent:20:43`); the point is yellow when `20:44` (waterfall height) or `20:45` (salinity) fires in the window (latest `23:42` → latest `20:46`, 22:06:31–22:09:02). `20:44` fired. Reason code `WRONG_EVIDENCE_SELECTED`, `wrong_choice = waterfall height`.

**Performance summary:**
Using the drone, the player scanned all readings at the Eastern and Western Falls in about two minutes. When Dr. Toppo asked which data point would best identify the larger watershed, the player answered "Waterfall height" two seconds after the question appeared. Under the rubric this earns 0 of 0.5 points.

**Gameplay evidence:**
- Scans logged: Eastern ocean, distance, salinity, flow and height (22:06:52–22:07:32); Western distance, salinity, height and flow (22:08:20–22:08:45).
- Dr. Toppo's framing at 22:08:57–22:08:58 ("Keep in mind that not all of the evidence is useful when building your argument"; the two candidate claims); choice `20:44` "Waterfall height." at 22:09:00; the activity closed with `20:46` at 22:09:02.
- No chat-history or map events were logged in the window.

**Possible learning need:**
This point targets identifying flow rate as the observation that reflects drainage-area size. Choosing waterfall height may indicate the player associated the most visible difference between the falls with watershed size rather than reasoning about how much land drains to each river. This is an interpretation.

**Potentially underused support:**
The investigation dialogues explain the relevance of each observation, and the in-game chat log can be used to review them; the logs show no chat use in this window, and the answer was given two seconds after the question, which leaves little time for review. The comparison table appears after collection; the logs cannot show how it was used.

**Suggested instructor intervention:**
Ask the student to explain what a watershed is and why a larger drainage area produces more water in the river. Then go through the four observations (flow rate, waterfall height, salinity, distance to the ocean) and ask, for each, whether it tells us anything about how much land drains to the river.

**Dashboard pop-up text:**
After collecting all the waterfall readings, the player answered Dr. Toppo's question about the most relevant evidence with "waterfall height" instead of water flow rate, which makes the point yellow (this single-choice point earns credit only for flow rate). The answer came two seconds after the question appeared, and no use of the chat history to review the investigation dialogues was logged. The choice may indicate the player linked the most striking difference between the two falls to watershed size rather than reasoning that a larger drainage area delivers more water, so flow rate is the indicator. Consider asking the student to explain, for each observation, whether it says anything about how much land drains to the river.

---

## Unit 2, Progress Point 7: Which Watershed? Part II

**Yellow-result trigger:**
Green requires the success node (`27:7`) and at most three incorrect-argument nodes in the window (previous `questFinishEvent:54` → latest, ending 22:14:17). Success fired, but eight incorrect nodes fired. Reason code `EXCESS_ATTEMPTS`, `attempt_number = 9`, `wrong_claim_number = 2`, `irrelevant_evidence_number = 6`.

**Performance summary:**
The player built the argument about which watershed is larger over four minutes (22:09:30–22:13:32), submitting nine times; the first eight were incorrect. Under the rubric a correct argument on the ninth attempt earns 0 of 3 points.

**Gameplay evidence:**
- Before starting, the player used the optional review choices "What is reasoning?" and "What is a watershed?" with Dr. Toppo (logged dialogue nodes `20:48`–`20:61`).
- Both reference panels were opened at 22:10:07 (Watershed Graph) and 22:10:08 (Waterfall Data), one second before the first submission; their closes are not logged, and neither was reopened.
- Submissions with claim `I`: `B,C,1,I` 22:10:09 (multiple evidence pieces), `B,1,I` 22:10:25 ("While the waterfall may be the taller of the two, how does that help predict the size of the watershed?"), `D,1,I` 22:10:47 (longer river downstream), `C,1,I` 22:11:03 (claim and evidence do not link to the reasoning), `A,1,I` 22:11:14 ("Your evidence does not fit with your claim. Try using a more appropriate claim.").
- After a pause of 1 minute 43 seconds (22:11:14–22:12:57), submissions with claim `II`: `D,1,II` 22:13:11 (downstream river), `C,1,II` 22:13:21 (salinity), `B,1,II` 22:13:27 ("Your claim makes sense however the waterfall height might not be the best piece of evidence"), and `A,1,II` 22:13:31 → "Well done! You have made the best argument possible."
- The feedback identified `B` as waterfall height, `C` as salinity and `D` as the downstream river; `A`, the evidence in the winning argument, is therefore the flow-rate observation. Apart from the one pause, submissions were 4–22 seconds apart.

**Possible learning need:**
Two skills are involved: choosing the claim the data supports and selecting relevant evidence. The player tried every evidence option under the wrong claim before changing it, then cycled three irrelevant options again under the right claim. The player may need support both in reading the comparison table to decide which watershed is larger and in recognising that only flow rate indicates watershed size — consistent with the "waterfall height" choice on the previous point. This is an interpretation; the cycling is observed, its reasons are not.

**Potentially underused support:**
Both reference tools were opened once, immediately before the first attempt, and not reopened during the eight incorrect attempts. Dr. Toppo's per-attempt feedback named the problem each time (irrelevant evidence, then "try another claim"), and the claim was changed only after the fifth attempt. The pre-task review dialogues were used (logged).

**Suggested instructor intervention:**
Walk through the waterfall comparison table: which river has the higher flow rate, and what does that imply about the land draining to it? Then ask the student to sort the four observations into "tells us about watershed size" and "does not". Finally, have them state the claim and the one piece of evidence that supports it, in their own words.

**Dashboard pop-up text:**
The player completed the watershed argument but needed nine submissions — eight incorrect — against a limit of four attempts, so the point is yellow. The logs show the player kept the first claim while trying every evidence option, changed the claim only after Dr. Toppo's fifth feedback said to, and then cycled the irrelevant options again before landing on flow rate; submissions were 4–22 seconds apart. Both reference panels were opened once just before the first attempt and not reopened. The pattern may indicate difficulty using the comparison table to decide which watershed is larger and recognising flow rate as the only size-related evidence. Consider working through the table together and having the student sort the observations into relevant and irrelevant.

---

## Unit 3, Progress Point 1: Supply Run (Establishing a Foothold)

**Yellow-result trigger:**
Green requires more than one correct-river confirmation (`DialogueNodeEvent:10:30`) in the window (previous `DialogueNodeEvent:11:22` → latest, ending 22:19:16). None fired; wrong-river nodes fired three times (`10:31` twice, `10:32` once). Reason code `EXCESS_WRONG_RIVERS`, `wrong_river_number = 3` (green allows at most one wrong crate).

**Performance summary:**
The player had to float Tera's three crates down the river that flows past her camp. All three crates were released into the wrong river within about two minutes, so none was delivered. Under the rubric this earns 0 of 3 points.

**Gameplay evidence:**
- DANI opened the map at 22:17:06 with the hint "Both of these rivers start at the south, and their currents run north."; the player reopened it for three seconds (22:17:17–22:17:20).
- Crate 1 lost at 22:17:46 (`10:31`: "The locator on the crate seems to be moving away from my location... I'd suggest checking the map to see which river flows by my camp before sending the next one"); crate 2 grabbed 22:17:57 and lost 22:18:13 (`10:31` again); crate 3 grabbed 22:18:30 and lost 22:18:59 (`10:32`: "You picked the wrong river... water flows from high elevations to lower elevations. This means that rivers and streams flow into the ocean...").
- No map opening was logged after 22:17:20 — none between the three releases.

**Possible learning need:**
This point targets using the map to decide which river is hydrologically connected to Tera's camp. Releasing three crates without reopening the map, after feedback that suggested checking it, may indicate the player identified a river by proximity or general direction rather than by tracing its course to the camp. This is an interpretation; the logs do not record which river was chosen.

**Potentially underused support:**
The map was used once, briefly; Tera's first feedback explicitly suggested checking the map before the next crate, and the logs show no map use afterwards. The logs cannot show whether the player watched Dr. Toppo's water-flow video or reviewed the chat history for Tera's clue that the crates landed upstream of her location.

**Suggested instructor intervention:**
On the watershed map, ask the student to find Tera's camp, trace each river from its source to the ocean, and explain which one passes the camp and why an object dropped upstream ends up there. Then ask what they would do differently after a failed delivery — check the map before the next crate.

**Dashboard pop-up text:**
All three of Tera's supply crates were released into the wrong river, so none reached her camp and the point is yellow (green requires at least two correct deliveries). The logs show one three-second map check before the first crate and none afterwards, even though Tera's feedback after the first loss suggested checking the map to see which river flows past her camp; the three losses came within about 75 seconds of each other. This may indicate the player chose a river by proximity rather than by tracing its flow to the camp. Consider having the student trace both rivers on the map from source to ocean, identify which one passes Tera's camp, and explain why a crate floats to the camp only from that river.

---

## Unit 3, Progress Point 2: Pollution Solution Part I

**Yellow-result trigger:**
Score = 5 − penalty(downstream reminders) − penalty(redundant-test reminders), where each penalty is 0 for at most one reminder, 1 for two or three, and 2 for four or more; green requires at least 3. Window: previous `DialogueNodeEvent:11:34` → latest, ending 22:27:40. Counts: 13 downstream reminders (`11:27`) and 22 redundant-test reminders (`11:29` ×16, `11:230` ×6), so 5 − 2 − 2 = 1. Reason code `EXCESS_SENSOR_REMINDERS`, `downstream_reminder_number = 13`, `redundant_reminder_number = 22`.

**Performance summary:**
Over seven minutes (22:20:21–22:27:40) the player dropped sensors along the river to find the pollution source — 21 readings were logged (13 polluted, 8 clean) and the source was identified — but DANI's reminders about sampling direction fired 35 times. Under the rubric this earns 1 of 5 points.

**Gameplay evidence:**
- "Pollution will only flow downstream, so we need to test further upstream." (`11:27`) fired 13 times, in runs of six (22:22:08–22:22:46, right after the first clean reading), five (22:25:10–22:25:48) and two.
- "Green checkmark means clean. You won't need to check upstream of a clean sensor." (`11:29`) fired 16 times, including nine in 40 seconds (22:23:33–22:24:13) and four more at 22:24:30–22:24:48.
- "You are as far upstream as you can go in this branch. Please proceed downstream." (`11:230`) fired six times; the ungraded "We previously tested close to this area" (`11:28`) twice.
- Reminders came 3–10 seconds apart within each run; no map-open or chat-history events were logged during the task.

**Possible learning need:**
This point targets reasoning about upstream and downstream from sensor results. Repeated runs of the same reminder — continuing in the wrong direction after a polluted reading and continuing upstream past a clean sensor — may indicate difficulty translating a red or green result into "the source must be upstream of red and cannot be upstream of green". This is an interpretation; the placement decisions themselves are not logged.

**Potentially underused support:**
DANI's reminders state the rule each time and fired 35 times, so the player may not have adjusted the sampling strategy after them. No map opening was logged during the task, so the player may have benefited from checking the sensor-result overlay on the map to plan the next drop. No chat-history use was logged.

**Suggested instructor intervention:**
Draw a branching river with a few red and green sensor marks and ask the student where the source could and could not be, and where the next sensor should go. Emphasise the two rules: a polluted reading means test upstream; a clean reading rules out everything upstream of it.

**Dashboard pop-up text:**
The player traced the pollution source with the drone sensors but triggered 35 reminder dialogues — 13 for testing in the wrong direction and 22 for unnecessary tests (checking upstream of a clean sensor or pushing past the top of a branch) — which drops the score to 1 of 5 and makes the point yellow. The reminders came in rapid runs (for example, nine clean-sensor reminders in 40 seconds), and no map check was logged during the task. This may indicate difficulty converting a red or green reading into where the source can be. Consider sketching a branching river with sample results and asking the student to mark where the source could be and where to test next.

---

## Unit 3, Progress Point 3: Pollution Solution Part II (Pollution Argument)

**Yellow-result trigger:**
A base score comes from the count of graded conversation-84 nodes in the window (previous `questFinishEvent:18` → latest, ending 22:42:54): at most 3 → 3 points, 4 → 2, 5 → 1, 6 or more → 0; one bonus point is added for opening the Pollution Site Data panel; green requires at least 3. The count was 6 (five incorrect submissions plus the success node, which the current script also counts), so the score is 0 + 1 = 1. Reason code `EXCESS_ATTEMPTS`, `wrong_argument_number = 5` (2 claim, 3 reasoning, 0 evidence), `backing_info_phrase = opened`.

**Performance summary:**
The player built the argument about where the pollutant enters the river in six submissions over three minutes (22:29:28–22:31:32); the first five were incorrect and the sixth was correct. Both reference panels were opened at the start. Under the rubric a correct argument on the sixth attempt earns 0 points, plus the 1-point reference bonus, so 1 of 4.

**Gameplay evidence:**
- Session opened 22:28:26; the Pollution Site Data and Watershed Image panels were opened at 22:28:29 (closes not logged); the player hovered over reasoning node `5` for 39 seconds (22:28:35–22:29:14) before the first submission.
- Submissions and feedback: `B,1,II` 22:29:28 → claim "does not take into consideration that water can carry pollution"; `B,4,II` 22:29:55 → "Your argument is logical. But it does not accurately describe how water moves."; `A,1,II` 22:30:37 → claim feedback again; `A,3,I` 22:30:59 → "You reasoned that water must flow from north to south. This is not always true in nature."; `A,2,I` 22:31:21 → "Your reasoning does not explain how water behaves. Pollutants travel downstream with water flow."; `A,5,I` 22:31:32 → "Great Job! You made the best argument possible."
- Submissions were 11–42 seconds apart; the reasoning node used in the winning argument (`5`) is the one the player studied longest at the start.

**Possible learning need:**
This point targets selecting reasoning that links the sensor pattern (clean upstream, polluted downstream) to the claim. Three of the five errors were reasoning problems, including a submission reasoning that water must flow from north to south, so the player may need support articulating that dissolved pollution travels downstream with the flow regardless of compass direction. This is an interpretation.

**Potentially underused support:**
Both reference panels were opened at the start (logged). Dr. Toppo's feedback named the faulty component each time, and the player changed that component in most cases (claim after claim feedback, reasoning after reasoning feedback), which is evidence the feedback was used. The sensor results and DANI's marked source from the previous task were available; the logs cannot show whether they were re-checked.

**Suggested instructor intervention:**
Ask the student to explain how the sensor pattern shows where the pollution enters the river, then to state the reasoning as a general rule ("dissolved pollution moves downstream with the water, so..."). Contrast that with the "water flows north to south" statement they chose and ask why map direction is not the rule.

**Dashboard pop-up text:**
The player built the pollution-source argument and opened the reference panels, but needed six submissions — five incorrect — against a limit of three, so the point is yellow (1 of 4 rubric points, the 1 being the reference-panel bonus). Feedback flagged the claim twice and the reasoning three times, including a submission reasoning that water must flow north to south; the player changed the flagged component each time and succeeded with the reasoning node they had studied longest at the start. This may indicate difficulty stating the general rule that pollutants move downstream with the flow, independent of map direction. Consider asking the student to explain the sensor pattern and phrase the reasoning as a rule.

---

## Unit 3, Progress Point 5: Part of a Balanced Ecosystem (Plant the Superfruit Seeds)

**Yellow-result trigger:**
Score = correct plantings − 0.5 × wrong plantings in the window (previous `DialogueNodeEvent:10:194` → latest, ending 22:50:14); the dashboard turns green at 2.5 or more. Four wrong plantings and none correct give −2. Reason code `EXCESS_WRONG_PLANTINGS`, `wrong_planting_number = 4` (green allows at most one wrong plot).

**Performance summary:**
Asked to plant four superfruit seeds in garden plots that receive the nutrient released at the temple, the player planted all four in plots that do not receive it, over 3 minutes 20 seconds (22:47:16–22:49:38). Tera ended the activity after the fourth wrong plot. Under the rubric this is 0 − 4 × 0.5 = −2 of 4 points.

**Gameplay evidence:**
- DANI marked the garden plots on the map (`73:210`) and opened it (22:46:23–22:46:34); the player then opened the map ten times, mostly for 2–7 seconds (for example 22:46:56–22:47:01, 22:47:23–22:47:29, 22:49:02–22:49:09).
- Plantings and feedback: 22:47:16 → `73:164` ("DANI is telling me that you picked the wrong spot. Is the water flowing downstream from the temple to here?") with hints to check the map, that water flows from high to low elevation, and to use the location of the ocean in the north of the map; 22:48:12 and 22:48:28 → `73:168` ("another wrong spot. You need to find a planting spot that is downstream from the temple.") with the reminder that all watersheds flow toward the ocean; 22:49:38 → `73:171` (activity ends).
- Two to four map checks preceded each of the first, second and fourth plantings; the second and third plantings were 16 seconds apart with no map check between them.

**Possible learning need:**
This point targets predicting which plots lie downstream of the nutrient source. Four wrong plots despite repeated map use and three explicit hints about downstream flow may indicate difficulty determining flow direction on the map (from the temple toward the ocean in the north) and therefore which plots the nutrient can reach. This is an interpretation.

**Potentially underused support:**
Map use is well documented (ten openings), and Tera's feedback after each planting restated the rule. The logs show no waypoint placement in this window, so the player may have benefited from marking a candidate plot before travelling to it; the logs cannot show whether the chat history was used to revisit the hints, and all plots are logged with the same object name, so the chosen plots cannot be identified.

**Suggested instructor intervention:**
Using the Unit 3 watershed map, ask the student to mark the temple release point and the ocean, draw arrows for the direction of flow along each river, and then circle the plots the nutrient can reach. Ask them to explain why a plot upstream of the temple or on a different branch cannot receive it.

**Dashboard pop-up text:**
The player planted all four superfruit seeds in plots that do not receive the temple's nutrient, so the score is −2 of 4 and the point is yellow (green allows at most one wrong plot). The logs show the player opened the map ten times during the task and received Tera's hints after each miss — water flows from high to low elevation toward the ocean in the north, so the plot must be downstream of the temple — yet each new plot was still wrong; two plantings came 16 seconds apart with no map check between them. This may indicate difficulty reading flow direction on the map and identifying which plots lie downstream of the release point. Consider having the student draw flow arrows on the map and circle the plots the nutrient can reach.

---

## Unit 4, Progress Point 1: Well What Have We Here?

**Yellow-result trigger:**
Score = 0.5 if the correct water-table answer (`DialogueNodeEvent:88:5`) appears in the window, plus 1.0 if the Unit 4 soil key puzzle took 30 seconds or less (0.5 if 30–90 seconds); green requires at least 1. Window: latest `DialogueNodeEvent:88:0` (22:52:00) → the Unit 4 soil-key close (22:59:13). The player chose the wrong answer (`88:7`) and the puzzle took 136 seconds, so the score is 0. Reason code `SCORE_BELOW_THRESHOLD`, `choice_phrase` = chose "it's any water found underground", `duration_phrase` = took 136 seconds.

**Performance summary:**
Anderson asked what the water table is; the player answered "It's any water found underground" four seconds later. The soil key puzzle that followed took 2 minutes 16 seconds. Under the rubric this earns 0 of 1.5 points.

**Gameplay evidence:**
- Anderson's question (`88:4`, 22:56:27: "What on Earth is the 'water table'...?") → answer `88:7` "It's any water found underground." at 22:56:31; the correct option (the boundary between saturated and unsaturated soil layers) was not selected, and the question is not repeated.
- Soil key puzzle 22:56:57–22:59:13: 50 drag steps; the selector swept across the full soil range (bedrock to gravel) about six times; the correct soil (clay-sand, logged as `isCorrectSelection = true`) was passed seven times while the water level was too low or too high, until clay-sand coincided with a proper level at 22:59:12.

**Possible learning need:**
Two ideas are involved: the definition of the water table (the top of the saturated zone, not any underground water), and controlling the water level through soil choice in the puzzle. The wrong answer is the common misconception named in the grading notes; the sweeping pattern may indicate the player was cycling through materials rather than predicting how each affects retention. Both are interpretations.

**Potentially underused support:**
Dr. Toppo's groundwater tutorial precedes Anderson's question; the logs cannot show whether it was watched. No chat-history use was logged. In the puzzle the level indicator gives immediate feedback, and the sweeps show it was being used, but the target combination was passed several times before it was recognised.

**Suggested instructor intervention:**
Ask the student to define the water table and draw a cross-section with unsaturated soil above and saturated soil below, labelling the boundary. Then ask how choosing clay versus gravel would change how much water is held and where the level ends up.

**Dashboard pop-up text:**
The player answered Anderson's water-table question with "any water found underground" instead of the boundary between saturated and unsaturated soil, and took 136 seconds to complete the soil key puzzle (30 seconds earns full credit, 90 seconds half), so the score is 0 and the point is yellow. During the puzzle the selector swept across all soil types about six times and passed the correct clay-sand setting seven times before the water level was also in range. The wrong definition is the common misconception that the water table is simply underground water, and the sweeping may indicate trial and error rather than predicting each soil's effect. Consider having the student draw and label a cross-section of the water table.

---

## Unit 4, Progress Point 2: Power Play – Floors 1 & 2 (Infiltration Glyph)

**Yellow-result trigger:**
Green requires the post-puzzle explanation node (`DialogueNodeEvent:88:11`) and none of the yellow nodes (`102:9`, `102:10`, `102:12`, `102:18`, `102:23`) in the window (latest Unit 4 soil-key close, 22:59:13 → latest `questActiveEvent:48`, 23:11:25). `102:10`, `102:12` and `102:23` fired. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 4` (green requires an independent solution within three attempts).

**Performance summary:**
In the infiltration glyph puzzle (matching gravel, sand, clay and the water-table piece to water-movement rates) the player submitted four incorrect orders in about 80 seconds; on the fifth submission DANI placed the pieces. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- Pieces were placed from 22:59:48; wrong-order feedback at 22:59:59 (`102:3`, three or four pieces wrong), 23:00:27 (`102:7`: "The images appear to represent the size of the particles of different types of soil."), 23:00:54 (`102:10`, three or four wrong: "a graph that shows the rate at which water passes through soils of different types."), 23:01:17 (`102:12`, one or two wrong: "That is very close, TK. I believe you can solve it.").
- 23:01:31 → `102:23` "I believe I have calculated the correct order for the puzzle. Allow me to assist, TK." (DANI's assist after the fifth submission); the explanation `88:11` followed at 23:02:10.
- Submissions were 14–28 seconds apart; the placement after the "very close" hint (23:01:26) still did not produce the correct order.
- On floor 2 immediately afterwards, the player changed the soil canister seven times (23:10:32–23:10:52) before the correct soil was set — not graded here, but consistent with the same difficulty.

**Possible learning need:**
This point targets the link between particle size and infiltration rate (fastest through gravel, then sand, slowest through clay) and the meaning of the water-table piece. Four wrong orders, two of them with three or four of the four pieces misplaced, may indicate the player had not yet connected particle size to how fast water passes through. This is an interpretation.

**Potentially underused support:**
DANI's hints named the concept (particle size, then the infiltration-rate graph). The logs cannot show whether the player consulted the chat history to revisit Dr. Toppo's groundwater tutorial or the soil descriptions from the previous point; no chat use was logged.

**Suggested instructor intervention:**
Ask the student to order gravel, sand and clay by particle size and then by how quickly water passes through, explaining the link (larger particles → larger spaces → faster infiltration). A quick sketch of particles with the spaces between them makes the relationship concrete.

**Dashboard pop-up text:**
The player did not solve the infiltration glyph puzzle independently: four arrangements were wrong within about 80 seconds, and after the fifth submission DANI placed the pieces, which makes the point yellow (green requires an independent solution within three attempts). Two submissions had three or four of the four pieces out of order, and the arrangement after DANI's "very close" hint was still wrong. This may indicate the player had not yet linked soil particle size to infiltration rate — water passes fastest through gravel, more slowly through sand, and slowest through clay. Consider asking the student to order the three soils by particle size and by infiltration rate and to explain why the two orders match.

---

## Unit 4, Progress Point 3: Power Play – Floors 3 & 4

**Yellow-result trigger:**
Score = 1 if the third-floor machine was changed exactly once, plus 2 if the fourth-floor machine was changed exactly once (1 if twice); green requires more than 1. Window: previous `questActiveEvent:50` → latest, ending 23:18:13. Floor 3 had 7 canister changes and floor 4 had 6, so the score is 0. Reason code `SCORE_BELOW_THRESHOLD`, `floor3_attempts = 7`, `floor4_attempts = 6`.

**Performance summary:**
On both floors the player cycled rapidly through the soil canisters rather than setting the pipe's soil once: seven changes in seven seconds on floor 3 and six changes in 18 seconds on floor 4. Both floors were completed. Under the rubric this earns 0 of 3 points.

**Gameplay evidence:**
- Floor 3 (23:12:16–23:12:23): Bedrock, Clay, Sand, Bedrock, Clay, Sand, Gravel — the floor was completed with Gravel; the "Soil View" panel was inspected at 23:11:29 before the machine was touched.
- Floor 4 (23:15:13–23:15:31): Bedrock, Clay, Gravel, Clay, Bedrock, Gravel — completed with Gravel; Soil View inspected at 23:14:55.
- Changes were about one second apart on floor 3 and 1–7 seconds apart on floor 4.

**Possible learning need:**
This point targets predicting which soil produces the water level and flow the pipe needs. Sub-second cycling through every canister, including bedrock more than once, may indicate the player was scanning the options rather than predicting from soil properties. This is an interpretation.

**Potentially underused support:**
The Soil View panels describing the surrounding layer were inspected on both floors (logged), and each machine change gives immediate visual feedback. The one-second spacing on floor 3 leaves little time to observe the effect of a change before the next. Practice floors 1 and 2 preceded this; no chat-history use was logged.

**Suggested instructor intervention:**
Before touching the machine, have the student predict aloud which soil will let the right amount of water through and why (permeability), test it, and only then change it. A predict-observe-explain routine with the three soils and bedrock targets the cycling pattern directly.

**Dashboard pop-up text:**
The player completed floors 3 and 4 of the alien well, but changed the soil canister seven times on the third floor (within seven seconds) and six times on the fourth, where the rubric expects one change on each floor, so the score is 0 and the point is yellow. The changes cycled through every option, including bedrock more than once, at roughly one-second intervals, which may indicate scanning the options rather than predicting which soil produces the required water flow from its permeability. Consider asking the student to predict which soil should work before each change and to explain the prediction in terms of how fast water moves through gravel, sand, clay and bedrock.

---

## Unit 4, Progress Point 4: Power Play – Floor 5 and the Drill Task

**Yellow-result trigger:**
Score = 1 if the two-layer machine had exactly one change per layer, plus 1 if the single-layer machine had exactly one change, plus 2 for a correct drill depth with no wrong depths (1 with one wrong depth); green requires more than 2. Window: latest `questActiveEvent:50` (23:18:13) → latest `questActiveEvent:36` (23:23:55). Machine 1 had 5 + 5 changes, machine 2 had 6, and six wrong drill choices were logged, so the score is 0. Reason code `SCORE_BELOW_THRESHOLD`, `machine_attempt_number = 16`, `wrong_choice_number = 7` (the reason script also counts the "middle" depth, which produced contaminated water).

**Performance summary:**
On floor 5 the player made 16 canister changes across the two machines (three is optimal), then in the drill task chose seven wrong depths in 22 seconds before choosing the fourth floor, which produced clean water. Under the rubric this earns 0 of 4 points.

**Gameplay evidence:**
- Machine 1 (23:18:32–23:19:27): top row Clay → Bedrock → Clay → Bedrock → Clay; bottom row Clay → Bedrock → Clay → Bedrock → Clay (final Clay / Clay).
- Machine 2 (23:19:48–23:20:07): Sand placed, re-selected four times within two seconds, then switched to Gravel.
- Drill (23:21:11–23:21:33): first floor → "I am not observing any water"; second floor → the same; all the way down → "the drill has struck bedrock... there is no space for water"; then the same three choices again in the same order; then "Middle" → "water, but it appears to be contaminated. The water may not be filtering through enough soil layers"; then the fourth floor → "You drilled the well to the perfect depth resulting in clean water." Choices were 1–4 seconds apart.

**Possible learning need:**
This point targets where groundwater sits (the saturated zone above bedrock) and how layered soils control flow. Repeating the same three wrong depths in the same order may indicate the outcome messages were not used to eliminate options, and the clay/bedrock toggling on both layers of machine 1 may indicate uncertainty about which layer combination lets water through. Both are interpretations.

**Potentially underused support:**
DANI's outcome message after each drill choice explains why that depth failed (no water, bedrock, contaminated); the repeated sequence suggests those messages may not have been used. DANI's floor-by-floor descriptions in this well (sand, clay, gravel, "we are in the water table", bedrock) were delivered; the logs cannot show whether the player related them to the drill panel. No chat-history use was logged.

**Suggested instructor intervention:**
Draw the well's layers with the water table marked and ask the student where a drill must stop to reach clean water, and why shallower depths find no water, the deepest hits bedrock, and a shallow saturated layer gives water that has not filtered through enough soil. Then ask them to restate what each drill message told them.

**Dashboard pop-up text:**
On the fifth floor the player changed soil canisters 16 times across the two machines (three changes is optimal) and then chose seven wrong drilling depths before reaching clean water on the fourth floor, so the score is 0 and the point is yellow. The drill choices repeated the same wrong sequence (first floor, second floor, all the way down) twice within 22 seconds even though DANI's messages explained each failure — no water, bedrock, then contaminated water — which may indicate the feedback was not used to narrow the depth, and uncertainty about where the saturated zone lies above bedrock. Consider having the student sketch the layers with the water table and explain why only the fourth-floor depth yields clean water.

---

## Unit 4, Progress Point 5: Saving Cadet Anderson

**Yellow-result trigger:**
Green requires a success node (`90:50` or `90:57`) and fewer than three negative-feedback nodes in the window (previous `questActiveEvent:41` → latest, ending 23:31:59). Success fired (`90:57`), but 14 negative nodes fired. Reason code `EXCESS_ATTEMPTS`, `attempt_number = 15`, `claim_wrong_number = 8`, `reasoning_wrong_number = 3`, `evidence_wrong_number = 3`.

**Performance summary:**
The player built the argument about why Anderson's bunker keeps flooding in 15 submissions over five minutes (23:27:47–23:30:38): 14 incorrect, then a correct argument combining three pieces of evidence. Under the rubric a correct argument after more than five attempts earns 0 of 3 points, and the backing-information bonus was not earned, so 0 of 4.

**Gameplay evidence:**
- Evidence collected before arguing: soil composition on three floors, the missing ceiling, and the drones (scans logged 23:24:21–23:25:21).
- Nine submissions with claim `I` (23:27:47–23:28:46), eight of which drew "Are you sure the flooding will resolve by turning off the fountain? Is there a better way to explain how water got into the warehouse?" (the last three adding "You should consider changing your claim."); one (`4,I`, 23:28:15) was flagged as incomplete because it had no claim or evidence.
- After a pause of 1 minute 21 seconds (23:28:46–23:30:07) the player switched to claim `II`: three reasoning errors ("Water does not infiltrate upward", "Water does not flow easily through bedrock", "not scientifically accurate"), two evidence errors ("Your claim and reasoning are correct, but your argument contains evidence that does not support your claim"), then success at 23:30:38 with evidence `A,C,D`, reasoning `2` and claim `II`.
- No backing-information panel was opened in this session (no tool events are logged); node `A` was hovered for 19 seconds at 23:29:09 before the second run.

**Possible learning need:**
This point targets explaining that the bunker floods because it sits within the saturated zone, permeable sand surrounds it, and the ceiling is open — several pieces of evidence combined. Keeping Anderson's claim (that the flooding will resolve) through eight rounds of feedback may indicate the player did not connect DANI's observation that the fountain pipes cannot account for the water with the need for a different claim; the reasoning errors (water infiltrating upward, flowing through bedrock) name misconceptions about groundwater movement. These are interpretations.

**Potentially underused support:**
The argumentation reference panel was not opened (the logs show no tool events in this session). Dr. Toppo's feedback said to change the claim from the seventh submission onward; the claim was changed on the tenth. DANI's explanations while collecting evidence (for example "sand above this floor, and bedrock below this floor. Large-scale flooding detected") were delivered; the logs cannot show how they were used.

**Suggested instructor intervention:**
Ask the student to state what the evidence shows (bunker below the water table, sand around it, holes in the ceiling) and what claim those facts support; then discuss why water cannot infiltrate upward or pass easily through bedrock. Have them assemble the argument on paper before entering the tool.

**Dashboard pop-up text:**
The player eventually built the correct argument about the flooding bunker, but needed 15 submissions — 14 incorrect — where green allows at most two, so the point is yellow. For nine submissions the player kept the claim that the flooding would stop once the fountain was off, despite eight feedback messages questioning it; after switching claims, the feedback flagged reasoning that water infiltrates upward or flows through bedrock, then unsupported evidence. The in-tool reference panel was not opened. This may indicate difficulty connecting the collected evidence (sand around the bunker, an open ceiling, a location within the saturated zone) to a claim, and misconceptions about how groundwater moves. Consider having the student state what each piece of evidence shows before choosing a claim.

---

## Unit 4, Progress Point 6: Desert Delicacies

**Yellow-result trigger:**
Score = the number of garden boxes whose latest camera placement matches the soil suited to the seedling (box 0 gravel, box 1 sand, box 2 clay), or, if higher, the number of "best soil" feedback lines in Tera's review; green requires at least 2. Window: latest `questActiveEvent:41` (23:31:59) → latest `questFinishEvent:56` (23:35:42). One box was correct. Reason code `WRONG_SOIL_SELECTED`, `wrong_box_summary` = "the first box (chose Clay, needs Gravel) and the second box (chose Gravel, needs Sand)".

**Performance summary:**
Tera asked the player to point a camera at the soil that would grow each seedling best given its water needs. The player put the peas (very little water) on clay, the potatoes (moderate water) on gravel, and the broccoli (a lot of water) on clay; only the broccoli choice was right. Under the rubric this earns 1 of 3 points.

**Gameplay evidence:**
- Tera's prompts: peas "only need a very small amount of water" (23:32:16); potatoes "need a moderate amount of water" (23:32:33); broccoli "need a TON of water" (23:32:46). DANI's hint at 23:32:17: "Each of the soils Tera is testing has a different particle size. The seedling planted in the soil that holds the right amount of water will likely grow best."
- Placements: box 0 Clay at 23:32:26, box 1 Gravel at 23:32:40, box 2 Clay at 23:32:58 — each 7–12 seconds after its prompt.
- Review (23:33:04, "I'm all set. Let's see the results."): peas → "This plant got more water than it required. The small soil particles will trap water..."; potatoes → "This plant did not get enough water. The water is expected to pass through the soil particles too easily..."; broccoli → "You chose the best soil for this plant."; then "You placed cameras to record seedlings in soil that did not suit their water needs."

**Possible learning need:**
This point targets matching plant water needs to soil retention and drainage. The two errors run opposite to the intended relationship (the least-thirsty plant on the most water-retaining soil, the moderately thirsty plant on the fastest-draining soil), which may indicate the player reversed the link between particle size and water retention, or matched on another cue. This is an interpretation.

**Potentially underused support:**
DANI's particle-size hint was delivered before the first placement; the logs cannot show whether the player revisited it or the earlier soil descriptions through the chat history (none logged). When Tera asked "Do you need to move any cameras?", the player answered "I'm all set" without adjusting; the review comes only after all three placements, and no re-placement was logged.

**Suggested instructor intervention:**
Ask the student to order gravel, sand and clay by how much water they hold and why (particle size and pore space), then to match the three seedlings to soils, explaining each match. Compare with their in-game choices and the feedback Tera gave.

**Dashboard pop-up text:**
The player placed only one of three cameras on a suitable soil, so the score is 1 of 3 and the point is yellow (green requires at least two). The peas, which need very little water, were placed on clay, and the potatoes, which need a moderate amount, on gravel; Tera's review reported that the peas got too much water and the potatoes too little. Only the broccoli, on clay, was right. The two errors run opposite to the intended relationship, which may indicate that the link between soil particle size and water retention was reversed. Consider asking the student to rank the three soils by how much water they hold and to explain why, then re-match the seedlings.

---

## Unit 5, Progress Point 1: If I Had a Nickel – Floors 1 & 2

**Yellow-result trigger:**
Green requires the success node (`100:44`) with none of `100:38`, `100:39` or `100:43` in the window (latest `questActiveEvent:43`, 23:36:27 → latest `questFinishEvent:43`, 23:44:46). `100:39` and `100:43` fired. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 4` (green requires an independent solution within four attempts).

**Performance summary:**
In the evaporation glyph puzzle (matching tablets that show evaporation rates to wall images of temperatures at different times of day) the player submitted four incorrect arrangements in 75 seconds, accepted DANI's offer of help after the fourth, and DANI ordered the tablets. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- The player accepted Dr. Toppo's Unit 5 lesson at the start of the unit ("Start Toppo Lesson?" → "Yes", 23:36:50–23:36:53), about 4.5 minutes before the puzzle.
- Placements from 23:41:24; wrong-order feedback at 23:41:31 (`100:34`, three or more wrong), 23:41:56 (`100:35`: "The tablets you can move appear to have something to do with evaporation rate."), 23:42:18 (`100:37`: "The images on the wall appear to depict temperatures at different times of day. Try matching them with the evaporation rate you might expect to see in those conditions."), 23:42:39 (`100:39`: "Would you like me to assist, TK?").
- 23:42:43 "Sure, I'm stuck." → 23:42:44 "Activating holid projector."; a further placement at 23:42:53 triggered DANI's assist line again (`100:43`) at 23:43:04; completion (`100:44`) at 23:43:23.
- Submissions were 21–25 seconds apart.

**Possible learning need:**
This point targets the relationship between temperature and evaporation rate (higher temperature, faster evaporation). Three further wrong orders after DANI's hint that named the relationship may indicate difficulty reading the temperature cues in the wall images or ordering the evaporation rates shown on the tablets. This is an interpretation.

**Potentially underused support:**
The Toppo lesson was started (logged); whether it was watched to the end is not logged. DANI's hints escalated as designed; the logs cannot show whether the player compared the tablets with one another before each submission. No chat-history use was logged inside the window.

**Suggested instructor intervention:**
Show three temperature conditions (a cool morning, a warm afternoon, a hot midday) and ask the student to rank the expected evaporation rate and explain why in terms of the energy given to water molecules. Follow with a short image-matching exercise.

**Dashboard pop-up text:**
The player did not solve the evaporation glyph puzzle independently: four arrangements were wrong within 75 seconds, and after the fourth the player accepted DANI's offer to order the tablets, so the point is yellow (green requires an independent solution within four attempts). The player had started Dr. Toppo's Unit 5 lesson a few minutes earlier, and DANI's third hint spelled out the relationship — wall images show temperatures at different times of day, tablets show evaporation rates — yet the next arrangement was still wrong. This may indicate difficulty connecting higher temperature with faster evaporation when reading the images. Consider asking the student to rank a few temperature conditions by expected evaporation rate and to explain the reasoning.

---

## Unit 5, Progress Point 2: If I Had a Nickel – Floors 3 & 4

**Yellow-result trigger:**
Score: floor 3 with at most 6 condenser/evaporator interactions earns 2 (7–10 earns 1); floor 4 with at most 5 earns 2 (6–9 earns 1); green requires at least 3. Window: latest `questFinishEvent:43` (23:44:46) → latest `DialogueNodeEvent:96:1` (23:53:24). Floor 3 had 8 counted interactions and floor 4 had 10, so the score is 1 + 0 = 1. Reason code `SCORE_BELOW_THRESHOLD`, `floor3_attempts = 8`, `floor4_attempts = 10`.

**Performance summary:**
On floor 3 the player used eight counted condenser/evaporator interactions (plus twelve dual-chamber toggles in room 2 that the current script does not count) and on floor 4 ten interactions, against optimal counts of six and five. Both floors were completed. Under the rubric this earns 1 of 4 points.

**Gameplay evidence:**
- Floor 3 (23:47:18–23:49:58): condenser on in room 1; in room 2 the paired dual-chamber condenser and evaporator were switched on and off twelve times in 45 seconds (23:47:51–23:48:36) before the room's condenser was switched on; in room 4 the first condenser was toggled off, on, off, on, the second condenser turned on, and the first turned off (six interactions in 40 seconds).
- Floor 4 (23:51:01–23:52:20): room 2 evaporator on, off, condenser on, evaporator on; room 3 evaporator on, condenser on, condenser off, evaporator off, condenser on.
- A chat-history close was logged at 23:53:07 (the open is not logged). The tester's debug menu was opened briefly on floor 2 (23:46:50–23:46:55), before the graded floors.

**Possible learning need:**
This point targets evaporation and condensation as complementary processes and predicting each machine's effect. Rapid on/off toggling of paired machines may indicate trial and error rather than predicting which phase change a chamber needs. This is an interpretation.

**Potentially underused support:**
Floors 1 and 2 provided practice with the machines; a chat-history window was closed near the end of floor 4, which suggests the player looked back at earlier instructions at some point, though the timing of the open is unknown. Each machine change gives immediate visual feedback, and the one- to two-second toggles in room 2 leave little time to observe the effect.

**Suggested instructor intervention:**
Ask the student to explain what an evaporator and a condenser each do to water (liquid to vapor; vapor to liquid) and, for a given chamber goal, to predict which machine to turn on before testing. A predict-then-test routine targets the toggling pattern directly.

**Dashboard pop-up text:**
The player completed floors 3 and 4 of the water-chamber puzzles, but with eight counted condenser/evaporator interactions on floor 3 (optimal six) and ten on floor 4 (optimal five), so the score is 1 of 4 and the point is yellow. On floor 3 the paired dual-chamber machines were switched on and off twelve times in 45 seconds, and on floor 4 machines were toggled on and off within seconds of each other, which may indicate trial-and-error switching rather than predicting whether a chamber needs evaporation or condensation. A chat-history window was closed near the end of floor 4. Consider asking the student to explain what each machine does to water and to predict the needed machine before testing.

---

## Unit 5, Progress Point 3: What Happened Here?

**Yellow-result trigger:**
The point is yellow when four or more flagged-submission nodes (33 conversation-108 keys) fire in the window (latest `DialogueNodeEvent:96:1`, 23:53:24 → latest `questFinishEvent:44`, 23:56:51); no success node is required. Eleven fired. Reason code `EXCESS_ATTEMPTS`, `wrong_argument_number = 11`, `claim_wrong_number = 7`, `reasoning_wrong_number = 2`, `evidence_wrong_number = 2`.

**Performance summary:**
After examining the evidence in Aryn's water factory (animal tracks, hygrometer, thermometer and storage pool, 23:54:04–23:54:24), the player submitted twelve arguments in 1 minute 45 seconds (23:55:00–23:56:45); eleven were flagged, and the quest completed after the twelfth (evidence `C,D`, reasoning `3`, claim `II`). Under the rubric a correct argument after more than five attempts earns 0 of 3 points.

**Gameplay evidence:**
- Seven submissions with claim `I` in 37 seconds (23:55:00–23:55:37), each flagged as "You are restating Aryn's claim. We are pretty sure this is incorrect." — the reasoning was cycled `1` to `4`, then the evidence `A` to `D`, while the claim stayed the same.
- With claim `II`: "Your claim sounds good. Try using a different piece of evidence." (`A`), "The amount of salt in the collector does not explain what happens to the water." (`B`), "your reasoning does not match the rest of your argument" twice (`C`, `D` with reasoning `1`), then `C,D,3,II` was accepted at 23:56:45.
- The nudge "Remember, you can click on the 'Backing Information' orbs..." fired after ten of the eleven flagged submissions; no backing-information panel was opened during the session (no tool events logged). Submissions were 4–31 seconds apart.

**Possible learning need:**
This point targets arguing that the water evaporated, supported by the temperature and humidity evidence together. Seven submissions restating Aryn's claim while changing other components may indicate the player did not recognise which claim was Aryn's and which was the natural-cause claim DANI proposed; the later evidence cycling may indicate difficulty selecting the two observations (rising temperature, rising humidity) that jointly support evaporation. These are interpretations.

**Potentially underused support:**
The backing-information panels were not opened despite ten prompts (a logged absence). DANI's explanations while collecting evidence (humidity rising from 10% to almost 60%; temperature rising all week) were delivered; the logs cannot show whether the player linked them to the argument. The pre-argument review with DANI was declined ("I think I'm good").

**Suggested instructor intervention:**
Ask the student what happened to the water and which two measurements show it (temperature up, humidity up), then to state a claim that opposes Aryn's. Practise identifying, from a list, which observations support "the water evaporated" and which do not (the salt amount, the tracks).

**Dashboard pop-up text:**
The player completed the argument about Aryn's disappearing water, but 11 of 12 submissions were flagged (green allows fewer than four), so the point is yellow. For the first seven submissions, made in 37 seconds, the player kept restating Aryn's claim while changing the reasoning and evidence; after switching claims, the evidence and reasoning were cycled until a two-evidence argument was accepted. The backing-information panels were not opened despite ten reminders. This may indicate difficulty recognising which claim was Aryn's, and difficulty selecting the temperature and humidity evidence that together support evaporation. Consider asking the student to state the opposing claim and to pick, from the collected observations, the two that show the water turned into vapor.

---

## Unit 5, Progress Point 4: Water Problems Require Water Solutions

**Yellow-result trigger:**
Green requires the maximum-water outcome (`DialogueNodeEvent:106:35`) and no failure outcome in the window (previous `questFinishEvent:44`, 23:56:51 → latest `questFinishEvent:45`, 23:59:25). The only run produced the sunlight-blocked failure (`106:27`). Reason code `WRONG_SETTINGS_SELECTED`, `wrong_run_number = 1`, `failure_phrase` = "the settings blocked sunlight, so the salt water could not heat up and evaporate".

**Performance summary:**
In the solar desalinator design task the player selected a flat roof, an extra covering and a hot glass roof — all three settings differ from the working design (tilted roof, no extra covering, cold glass) — within five seconds and submitted once. Under the rubric this earns 0 of 1.5 points.

**Gameplay evidence:**
- DANI played Dr. Toppo's desalinator video at 23:57:59–23:58:00 ("I have found a video on desalinators in Captain Toppo's survival series archive... Playing it for you now."); the design panel was opened at 23:58:06.
- Selections: RoofStyle "Flat" 23:58:08, ExtraCovering "Covered" 23:58:10, GlassRoofTemperature "Hot" 23:58:12; submitted 23:58:13.
- Outcome `106:27`: "Looks like we didn't collect any water. Unfortunately, your settings did not allow for sunlight to enter the solar desalinator. Without sunlight, the salt water can't get enough heat to evaporate..." No second run was made; the quest closed at 23:59:25.

**Possible learning need:**
This point targets applying evaporation and condensation to a design: sunlight must reach the water (no covering), the glass must stay cool for condensation, and a sloped roof directs condensed water to the collector. All three choices contradict these, which may indicate the player had not yet linked each design feature to a step of the water cycle. This is an interpretation; the five-second selection time is consistent with, but does not prove, choices made without weighing them.

**Potentially underused support:**
The video began eight seconds before the first selection, so it may not have been watched before designing. Conversations with Aryn, Toppo and Anderson and the chat history were available (no chat use was logged in the window). The blueprint view and Dr. Toppo's outcome feedback explain the failure; only one run was made.

**Suggested instructor intervention:**
Ask the student to narrate the water's path in the still: sunlight heats the salt water, vapor rises, vapor condenses on a cool surface, droplets run down a slope into the collector. Then ask which setting supports each step and why the flat, covered, hot design produced no water.

**Dashboard pop-up text:**
The player's solar desalinator design produced no water: a flat roof, an extra covering and a hot glass roof were selected within five seconds and submitted once, and Dr. Toppo's feedback explained that the covering blocked the sunlight needed for evaporation, so the point is yellow (green requires the maximum-water design with no failed runs). All three choices differ from the working design — sloped roof, no covering, cold glass. Dr. Toppo's desalinator video started only eight seconds before the first selection, so it may not have been used. This may indicate the player had not linked each design feature to a step of the water cycle. Consider asking the student to trace the water's path through the still and name the setting that supports each step.

---

## Verification and Documentation Notes

1. **Colors and reason codes verified.** `rubric-validation/run_all.py --fixture 09-03-26-3` reproduces all 26 expected colors, and `reason-code-validation/run_all.py --fixture 09-03-26-3` reproduces the 20 triggered codes and every variable quoted above. The fixture's `description` in `rubric-validation/config/fixtures.yaml` says "17 yellow points" but its expected list contains 20 yellows; the list is correct and the description should be updated.
2. **Evidence extraction.** Attempt windows were reproduced with the `attempt_window()` functions of the reason-code modules; for points whose grading window has no earlier trigger and therefore starts at the beginning of the log (U2P4, U2P5, U2P7, U3P1, U3P2, U3P3, U3P5, U4P3, U4P5), the narrative evidence was taken from the activity segment bounded by the documented start marker. Records were ordered by client timestamp. Dialogue wording is quoted from `grading-logic/original-score-rubric-table-and-dialogue-database/Dialogue-ID-Texts.xlsx`.
3. **Rubric versus dashboard thresholds (reported, not resolved).** Where a rubric-point statement is made above it follows the files in `assessment-score-rubric-for-each-pp/`; the yellow trigger follows the grading code. The two differ in several places relevant to this player: the U4P2 and U5P1 rubrics give 0 points from the third and fourth attempt respectively while the dashboard stays green one attempt longer; the U3P5 rubric's on-track band is 3–4 points while the dashboard turns green at 2.5; the U4P5 backing-information bonus in the rubric is not applied by the dashboard; the U5P4 rubric maximum is 1.5 points while the progress-point specification lists on-track as 2; the U3P3 color script counts the success node in its total, which makes its bands equal to total attempts and matches the rubric's attempt bands; the U4P3 rubric names sand as the fourth-floor solution but this player completed the floor with gravel; and the U4P4 rubric describes the fifth-floor canister solutions inconsistently while the dashboard counts canister changes.
4. **Argument node labels are not documented in the repository.** Submissions are quoted by their logged labels. Where a role is stated (for example that `B` was waterfall height in U2P7, or that claim `I` was Anderson's claim in U4P5), it is inferred from the feedback node that fired for that submission and is labelled as such.
5. **Resource-use statements are log-grounded.** Panel openings (`argumentationToolEvent`), map openings and waypoints (`TopographicMapEvent`), dialogue choices such as accepting the video replay or the Toppo lesson, and puzzle interactions come directly from the log. Absences stated definitively are also log-grounded: no tool events in the U4P5 and U5P3 sessions, no map opening after 22:17:20 in U3P1, no map events in the U3P2 sensor task. Chat-history use is only partly observable: the log records `chatEvent` "Close" at 23:36:27 and 23:53:07 but no open events, so durations cannot be given. Panel close events were not logged for most sessions, so panel durations are not stated (unlike the 05-01-26 example, where they were).
6. **Tester artifacts.** The debug menu was opened at 22:36:53 (Unit 3, after the pollution argument) and 23:46:50 (Unit 5, floor 2); neither falls inside a graded count. The `crash` telemetry records (pointer-lock and WASM errors) do not affect any graded window.
7. **Known grading-logic items visible in this log.** U5P2's twelve dual-chamber interactions on floor 3 are not counted by the current script (flagged in the grading file); U4P4's script counts the "middle" drill depth as a success even though DANI reports contaminated water (flagged); the U2P2 grading file is titled "Foraged Forging" but grades the Finding-Toppo navigation, and its rubric file describes waypoint placement while the code counts reminders (carried over from the Units 1–2 example).
