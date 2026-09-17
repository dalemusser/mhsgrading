# Teacher-Facing Feedback — Yellow Progress Points (Units 1–5)

**Player:** `wenyi091426-3` (test playthrough of build `20260914-`, played 2026-09-16 in two sittings; log dump `playthrough-logs-and-results/09-14-26-3/wenyi091426-3.stratalog.logdata.json`, 12,318 records, player id `6aa8589346b3c45b562092f8`)
**Expected dashboard colors (in order U1P1–U1P4, U2P1–U2P7, U3P1–U3P5, U4P1–U4P6, U5P1–U5P4):**
Green, Green, **Yellow**, Green, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**, **Yellow**

The expected colors are the `09-14-26-3` fixture in `rubric-validation/config/fixtures.yaml` (grading-readiness audit run 2026-09-16, 18 points with an independent doc-window check). Both validation suites reproduce them: `rubric-validation` (26/26 colors) and `reason-code-validation` (26/26, exactly one reason code triggered for each yellow point). This was a deliberately imperfect test run, so 23 of the 26 points are yellow. Timestamps below are the log's client timestamps (UTC). Unit 1 was started twice — the first run (from 00:23) was abandoned and the unit restarted at 00:45, so every Unit 1 window covers the second run — and the playthrough was split into two sittings with a break of about 13 hours between finding Aryn (01:47) and the temple glyph puzzle (14:51).

| Dashboard position | Point | Activity | Reason code (variables) |
|---|---|---|---|
| 3 | U1P3 | Defend the Expedition | `WRONG_ARG_SELECTED` (attempt_number 2) |
| 5 | U2P1 | Escape the Ruin (topographic-map matching) | `SOLVED_WITH_ASSIST` (4 wrong arrangements, accepted assist) |
| 6 | U2P2 | Foraged Forging (graded segment: finding Captain Toppo) | `EXCESS_NAV_REMINDERS` (4 reminders) |
| 7 | U2P3 | Getting the Band Back Together Part II (finding Tera and Aryn) | `EXCESS_NAV_REMINDERS` (14 reminders: 9 Tera, 5 Aryn) |
| 8 | U2P4 | Investigate the Temple | `SOLVED_WITH_ASSIST` (5 wrong arrangements) |
| 9 | U2P5 | Classified Information | `EXCESS_MISCLASSIFICATIONS` (8 wrong: 2 claim, 5 reasoning, 1 evidence) |
| 10 | U2P6 | Which Watershed? Part I | `WRONG_EVIDENCE_SELECTED` (waterfall height) |
| 11 | U2P7 | Which Watershed? Part II | `EXCESS_ATTEMPTS` (9 submissions: 2 claim, 6 irrelevant evidence) |
| 12 | U3P1 | Supply Run (Establishing a Foothold) | `EXCESS_WRONG_RIVERS` (3 wrong crates) |
| 13 | U3P2 | Pollution Solution Part I | `EXCESS_SENSOR_REMINDERS` (5 downstream, 8 redundant) |
| 14 | U3P3 | Pollution Solution Part II (Pollution Argument) | `EXCESS_ATTEMPTS` (6 wrong: 2 claim, 4 reasoning; reference panel opened) |
| 15 | U3P4 | Forsaken Facility (dissolved-particles glyph) | `SOLVED_WITH_ASSIST` (4 wrong arrangements, forced assist) |
| 16 | U3P5 | Part of a Balanced Ecosystem (Plant the Superfruit Seeds) | `EXCESS_WRONG_PLANTINGS` (4 wrong plots) |
| 17 | U4P1 | Well What Have We Here? | `SCORE_BELOW_THRESHOLD` (wrong water-table answer; 168 s puzzle) |
| 18 | U4P2 | Power Play – Floors 1 & 2 (Infiltration Glyph) | `SOLVED_WITH_ASSIST` (4 wrong arrangements, accepted assist) |
| 19 | U4P3 | Power Play – Floors 3 & 4 | `SCORE_BELOW_THRESHOLD` (10 and 15 canister changes) |
| 20 | U4P4 | Power Play – Floor 5 (+ drill task) | `SCORE_BELOW_THRESHOLD` (18 canister changes; 3 wrong depths) |
| 21 | U4P5 | Saving Cadet Anderson | `EXCESS_ATTEMPTS` (11 submissions: 6 claim, 1 reasoning, 3 evidence) |
| 22 | U4P6 | Desert Delicacies | `WRONG_SOIL_SELECTED` (all three boxes wrong) |
| 23 | U5P1 | If I Had a Nickel – Floors 1 & 2 | `SOLVED_WITH_ASSIST` (4 wrong arrangements, accepted assist) |
| 24 | U5P2 | If I Had a Nickel – Floors 3 & 4 | `SCORE_BELOW_THRESHOLD` (8 and 10 interactions) |
| 25 | U5P3 | What Happened Here? | `EXCESS_ATTEMPTS` (6 flagged: 4 claim, 1 reasoning, 1 evidence) |
| 26 | U5P4 | Water Problems Require Water Solutions | `WRONG_SETTINGS_SELECTED` (1 failed run, sunlight blocked) |

For every point, re-running the production grading logic and the reason-code scripts against the log reproduces the expected yellow and the variables shown above.

---

## Unit 1, Progress Point 3: Defend the Expedition

**Yellow-result trigger:**
Green requires that no wrong-argument node (`DialogueNodeEvent:70:25`) appears inside the attempt window (previous `questActiveEvent:34` → latest `questActiveEvent:34`, 01:08:29; no earlier occurrence exists, so the window reaches back to the start of the log — the abandoned first Unit 1 run never reached this activity). The node fired once. Reason code `WRONG_ARG_SELECTED`, `attempt_number = 2` (green requires a correct first submission).

**Performance summary:**
In the first graded use of the argumentation engine (the WAT-247 freshwater argument), the player submitted twice within 24 seconds. The first submission used the claim Europa Corp made; after Dr. Toppo's feedback the player replaced that claim with Toppo's and the second submission was correct.

**Gameplay evidence:**
- The argumentation tutorial session (01:05:55–01:06:40) was completed with a single submission.
- The freshwater session opened at 01:07:16; the Backing Info panel was opened at 01:07:19 (its close is not logged), and the player hovered over nodes `II` and `I` for 0.2 and 1.6 seconds before adding `II`, `1` and `A`.
- Submission 1 `A,1,II` at 01:07:27, 11 seconds after the session opened → wrong-argument feedback (`70:25`): "You have chosen the claim that Europa Corp made. Toppo is trying to make a different point so she will need a different claim."
- The player hovered `II` and `A` again, removed `II` (01:07:46), hovered `I` for 0.8 seconds and added it (01:07:48), opened the Backing Info panel for 0.7 seconds (01:07:49–01:07:50), then submitted `A,1,I` at 01:07:50 → success (`70:7`: "Great! You chose the main idea that Toppo is trying to support, also known as the claim."). The session closed 34 seconds after it opened.

**Possible learning need:**
This point targets identifying the claim that the given evidence and reasoning support. The first submission took the competing Europa Corp claim, and the component the player then changed (`II` → `I`) resolved it, so the player may need support distinguishing Toppo's claim from Europa Corp's by checking which conclusion the freshwater evidence actually supports before submitting. The 11-second first submission is consistent with the two claims not being compared beforehand. Both are interpretations — the logs cannot show what the player read.

**Potentially underused support:**
The Backing Info panel was opened twice, both times briefly (the second for under a second), and the node hover-overs that reveal each option's text lasted at most two seconds. Dr. Toppo's feedback after the first submission identified the wrong claim, and the second submission changed exactly that component, so the feedback was used. The logs cannot show whether the player used the optional dialogue choices to ask Dr. Toppo about claims, evidence and reasoning, or watched the argumentation video.

**Suggested instructor intervention:**
Ask the student to state, in their own words, what Toppo is trying to prove about WAT-247 and what Europa Corp claimed, then to explain which of the two the freshwater evidence supports and why. Encourage reading both claim options in full and deciding which one the evidence backs before the first submission.

**Dashboard pop-up text:**
The player completed the Unit 1 freshwater argument on the second submission, so the point is yellow (green requires a correct first submission). The first argument, submitted 11 seconds after the session opened, used the claim Europa Corp made; after Dr. Toppo's feedback named the claim as the problem, the player swapped in Toppo's claim and succeeded 24 seconds later. The Backing Info panel was opened twice, briefly, and option descriptions were hovered for under two seconds each. The quick first submission may indicate the two claims were not compared before submitting, while the immediate correction shows the feedback was used. Consider asking the student to state what Toppo wants to prove and what Europa Corp claimed, and to check which claim the freshwater evidence supports before submitting.

---

## Unit 2, Progress Point 1: Escape the Ruin (Topographic-Map Matching)

**Yellow-result trigger:**
Green requires the solved-on-own node (`DialogueNodeEvent:68:29`) and none of the yellow nodes (`68:22`, `68:23`, `68:27`, `68:28`, `68:31`) in the window (previous `questFinishEvent:21` → latest, 01:24:30; no earlier occurrence). `68:23` (fourth wrong arrangement, assist offered) fired and `68:29` did not. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 4` (green requires an independent solution within four attempts). The code recognises the accepted-assist nodes `68:24`/`68:26`, which were added to its key list on 2026-09-16 after this log exposed that path.

**Performance summary:**
In the alien-ruin puzzle that matches six topographic-map tiles to six terrain sockets, the player submitted four arrangements over about 4.5 minutes, each with more than three of the six tiles misplaced, accepted DANI's offer of help after the fourth, and DANI placed the pieces. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- All six tiles were placed between 01:16:07 and 01:16:44 → first-attempt feedback for more than three wrong tiles (`68:5`, 01:16:50: "My optical sensors detect patterns on these pieces that resemble topographic maps.").
- All six re-placed 01:16:59–01:17:37 → second-attempt feedback, again more than three wrong (`68:7`, 01:17:43: "Try matching the topographic map image to the corresponding landscape shape.").
- All six re-placed 01:17:49–01:18:28 → third-attempt feedback, more than three wrong (`68:18`, 01:18:44: "may we watch Toppo's lesson again?"); the player accepted ("Sure. That might help.", 01:18:53) and the lesson streamed (01:18:55–01:20:27).
- All six re-placed 01:20:32–01:20:57 → fourth-attempt feedback, more than three wrong (`68:23`, 01:21:13: "Would you like me to assist, TK?"); the player accepted ("Sure. I'm stuck.", 01:21:20). DANI's explanation while placing the pieces (`68:26`, 01:22:52: where contour lines are close together the terrain is steep, where they are spread out it is less sloped) followed the lesson link, and the room was completed at 01:23:30 ("We have finally solved this intractable puzzle.").
- Each arrangement took 30–40 seconds of placements; no follow-up question node (the optional "Topographic map?" or "Match them?" choices) was logged after the first two hints.

**Possible learning need:**
This point targets connecting the top-down contour-line view of a landscape with its side-view profile. Every arrangement had at least four of the six tiles wrong, including the one made after the lesson replay, which may indicate difficulty reading contour spacing as slope (close lines steep, wide lines gentle) and using that to pick the matching silhouette. This is an interpretation; the logs record placements, not what the player compared.

**Potentially underused support:**
The lesson replay after the third miss and DANI's assist after the fourth were both accepted (logged dialogue choices). The optional follow-up explanations offered after the first two hints were not logged as chosen, so the player may not have used DANI's contour-line explanation before re-arranging. The logs show the lesson link at 01:18:58 and the next placement at 01:20:32, consistent with the lesson running, but cannot show how much of it was watched.

**Suggested instructor intervention:**
Show the student two or three topographic-map tiles and their elevation profiles and ask them to point out where contour lines are close together (steep) or far apart (gentle) and where the peaks and valleys are, then to match each tile to a profile while explaining the choice. A short map-to-profile matching exercise with feedback targets the skill directly.

**Dashboard pop-up text:**
The player did not solve the topographic-map matching puzzle independently: four arrangements were submitted with more than three of the six tiles misplaced, and after the fourth the player accepted DANI's offer and DANI placed the pieces, which makes the point yellow (green requires an independent solution within four attempts). The player accepted the replay of Dr. Toppo's topography lesson after the third miss, yet the next arrangement still had most tiles wrong. This may indicate difficulty connecting contour-line spacing on the map tiles with the steepness and shape of the terrain silhouettes. Consider asking the student to explain what closely and widely spaced contour lines mean, then to match two or three map-and-profile pairs while saying where each landscape is steep.

---

## Unit 2, Progress Point 2: Foraged Forging (Finding Captain Toppo)

**Yellow-result trigger:**
The script counts wrong-direction reminder dialogues (six conversation-28/59 keys) between the activity start (`questFinishEvent:21`, 01:24:30) and end (`DialogueNodeEvent:20:26`, 01:35:31). Green allows at most one; four fired. Reason code `EXCESS_NAV_REMINDERS`, `triggering_number = 4`.

**Performance summary:**
After the hoverboard segment, the player had to turn Anderson's clue about Captain Toppo's location into a waypoint and travel there. The player checked the 90-foot legend entry, placed and moved the waypoint in two short map sessions, set off, and triggered the same clue reminder four times within 66 seconds; the player then reopened the map, moved the waypoint to a different area, and reached Toppo 12 seconds later, about three minutes after the segment began.

**Gameplay evidence:**
- Anderson offered to replay the mission-control video on topographic maps ("Do you want to watch it again?", 01:26:07); the player declined ("No, I'm good.", 01:26:15). Anderson's clue (`18:79`, 01:26:25): Captain Toppo is "just northwest of here on a hill at an elevation of approximately 90 feet."
- After the waypoint tutorial (01:30:57), the player unselected the 0-ft legend entry and selected "90 ft" (01:31:13), set the waypoint (01:31:17) and moved it six times across two map sessions ending 01:31:35, then opened the map again (01:31:52–01:31:59) and moved the waypoint three times to a different area.
- Reminder `28:179` fired at 01:32:02, 01:32:18, 01:32:45 and 01:33:08: "Anderson said that Toppo's pod was near our original location. We should look for two rock formations with contour lines close together nearer to where we started. Remember you can move the waypoint on your map at any time."
- The map was reopened at 01:33:27 and the waypoint moved three times to a third area (closed 01:33:32); Toppo was reached at 01:33:44 (`20:1`).

**Possible learning need:**
This point targets integrating clue information (direction, elevation, terrain features) with the topographic map. The reminders show the player first travelled through an area inconsistent with the clue, and the two waypoint relocations before travel suggest the clue's target — a hill at about 90 feet, northwest of the meeting point, with closely spaced contour lines — was not located on the first reading of the map. The successful relocation after the reminders shows the player could act on the hint. This is an interpretation; the logs cannot distinguish a misread map from an indirect route.

**Potentially underused support:**
Map, legend and waypoint use are logged (four short sessions), and the reminder was acted on. The replay of the topographic-map video was offered and declined (logged). The logs do not show whether the player revisited Anderson's clue in the chat history.

**Suggested instructor intervention:**
Give the student the clue text and a topographic map and ask them to find a hill at the stated elevation using the legend and the contour lines, explain how they know it is a hill (closed contour loops) and which direction is northwest, and place a waypoint there. Then discuss what to do when an in-game reminder says the route is inconsistent with the clue.

**Dashboard pop-up text:**
The player found Captain Toppo, but the wrong-direction reminder fired four times during the search, above the threshold of one, so the point is yellow. The logs show the player checked the 90-foot legend entry, placed and moved the waypoint in two map sessions, then triggered four reminders within 66 seconds after setting off; the player then reopened the map, moved the waypoint to a different area and reached Toppo 12 seconds later. Earlier, the player declined Anderson's offer to replay the topographic-map video. The initial off-course travel may indicate difficulty turning the clue (northwest, on a hill at about 90 feet) into a map location, though the reminder was clearly used. Consider asking the student to locate a hill at a given elevation from the legend and contour lines before travelling.

---

## Unit 2, Progress Point 3: Getting the Band Back Together Part II (Finding Tera and Aryn)

**Yellow-result trigger:**
The script counts the location-reminder dialogues (33 conversation-18/28/59 keys) between the Tera waypoint prompt (`DialogueNodeEvent:20:33`, 01:36:02) and the end of the Aryn search (`DialogueNodeEvent:22:18`, 01:47:38); green requires fewer than six. Fourteen fired — nine before Tera was found (`21:1`, 01:40:40) and five after the Aryn waypoint prompt (`18:231`, 01:42:15). Reason code `EXCESS_NAV_REMINDERS`, `triggering_number = 14`, `tera_count = 9`, `aryn_count = 5`.

**Performance summary:**
Two navigation tasks: Tera (a nearby river's eastern shore at about 0 feet, northwest of Toppo) was found after 4 minutes 38 seconds with nine reminders; Aryn (the north end of a mountain range, inside a passage that cuts through it) was found after 3 minutes 58 seconds with five reminders. Under the rubric the Tera search earns the navigation point (found within five minutes) and the Aryn search only the half point for map use (found after the three-minute limit); the waypoint-placement points cannot be judged from the logs.

**Gameplay evidence:**
- Tera: the player selected the 0-ft legend entry and moved the waypoint twice (01:36:06–01:36:08); an attempt to place it in the unmapped area was refused ("I don't have map data for that area yet", 01:36:10); the map closed at 01:36:12.
- Reminder `28:188` ("You found an area of low elevation on this river's eastern shore, but I don't see Tera's pod anywhere. Check your map to see if there's another area of low elevation along this same shoreline.") fired five times (01:36:38, 01:37:04, 01:38:12, 01:38:35, 01:39:53); reminder `28:187` ("Looks like you found an island, Tera's pod is not on an island. Check your map to see if you can find an area of around 0 feet elevation north of Toppo's location along a river.") fired four times (01:37:27, 01:37:41, 01:39:07, 01:39:27).
- The map was reopened twice during the Tera search, each time with waypoint moves (01:36:57–01:37:03, three moves; 01:38:00–01:38:05, one move); Tera was reached at 01:40:40.
- Aryn: Anderson's clue at 01:41:36; the map was opened at 01:42:07 and closed at 01:42:20, and again 01:42:23–01:42:26; no waypoint set or move event was logged after the Aryn clue. Reminder `28:194` ("Looks like you found a small mountain, but Aryn crashed in a passage that runs through a mountain range. Look for a path that passes through several mountains joined together.") fired five times (01:43:11, 01:43:29, 01:44:38, 01:44:59, 01:45:32); no map opening was logged after 01:42:26; Aryn was reached at 01:46:13.

**Possible learning need:**
This point targets connecting narrative clues (direction, elevation, landforms, water features) to the topographic map. In the Tera search the player reached the right kind of place — a low-elevation eastern shore — but the wrong stretch of it, and twice an island, which may indicate difficulty scanning the whole shoreline for candidate locations north of Toppo. In the Aryn search the same reminder fired five times, which may indicate difficulty distinguishing a single small mountain from a mountain range (several joined peaks with closely spaced contour lines) and spotting a passage through it. These are interpretations.

**Potentially underused support:**
During the Tera search the map was reopened and the waypoint moved after some reminders (logged), so the hints were partly used. During the Aryn search no waypoint placement or move and no map opening after 01:42:26 were logged, even though each reminder asked the player to look for the passage on the map; the waypoint from the Tera search may have been left in place. Chat-history review of Anderson's clues is not observable in the logs.

**Suggested instructor intervention:**
On the Unit 2 map, ask the student to point out a single hill, a mountain range (a cluster of joined high-elevation areas) and a passage through it, and to trace a river's eastern shore and mark the stretches at about 0 feet. Then give each clue in turn and have the student place a waypoint and explain the choice before moving.

**Dashboard pop-up text:**
The player located Tera and Aryn, but 14 location reminders fired across the two searches (9 while looking for Tera, 5 for Aryn), far above the limit of six, so the point is yellow. During the Tera search the player twice reached a low-elevation eastern shore without the pod and twice an island, reopening the map and moving the waypoint after some reminders; Tera was found after about 4.5 minutes. For Aryn the reminder about finding a small mountain rather than a range with a passage fired five times, no waypoint or map use was logged after the clue, and Aryn was found after about four minutes. This may indicate difficulty telling a single hill from a mountain range on the contour map and scanning a shoreline for candidate locations. Consider practising both on a map with the student.

---

## Unit 2, Progress Point 4: Investigate the Temple

**Yellow-result trigger:**
Green requires the solved-on-own node (`74:21`) and none of the yellow nodes (`74:16`, `74:17`, `74:20`, `74:22`) in the window (previous `DialogueNodeEvent:23:17` → latest, ending 14:56:04; no earlier occurrence). Nodes `74:17` (fifth wrong arrangement, assist offered) and `74:22` (DANI-helped completion) fired. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 5` (green requires an independent solution within five attempts).

**Performance summary:**
In the watershed glyph puzzle (ordering terrain pieces by watershed size and flow rate), the first graded activity after the 13-hour break, the player submitted five incorrect arrangements over about four minutes, accepted DANI's offer of help after the fifth, and DANI placed the pieces. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- Wrong-arrangement feedback at 14:51:03 (`74:4`), 14:51:48 (`74:6`: "These pieces resemble watersheds of varying size. Perhaps that is a clue to the correct order."), 14:52:38 (`74:10`: several pieces wrong; DANI offered Toppo's watershed lesson), 14:54:21 (`74:15`: "You should try ordering the watershed pieces by size."), 14:54:55 (`74:17`: "Would you like me to assist, TK?").
- The player accepted the assist ("Sure. I'm stuck", `74:18`, 14:55:00); the helped completion `74:22` followed at 14:55:02 ("The larger a watershed, the more...").
- Logged use of support: after the second miss the player chose the follow-up question "Sizes of watersheds?" (`74:11`, 14:52:01) and received DANI's definition (`74:23`); after the third miss the player accepted the video replay ("Sure. Let's watch it.", `74:13`, 14:52:50; the follow-on node fired 60 seconds later).
- Submissions were 34–103 seconds apart; a glyph-dock insertion was logged at 14:52:25 between the second and third attempts.

**Possible learning need:**
This point targets connecting drainage-area size to relative flow rate and using that pattern to order the pieces. Five wrong orders, two of them after the explicit hint to order by size, may indicate difficulty judging relative watershed size from the terrain pieces — comparing drainage areas rather than elevation or slope. This is an interpretation.

**Potentially underused support:**
The player demonstrably used two supports (the watershed-definition question and the video replay are logged as dialogue choices), and DANI's hint sequence escalated as designed. The logs cannot show how much of the replayed video was watched or whether the pieces were compared with one another before each submission.

**Suggested instructor intervention:**
Show the student two or three watershed diagrams of different sizes and ask them to rank them and predict which main river carries more water and why. Then ask what features of a terrain piece indicate drainage area (the extent of land draining to the river) versus features that do not (height alone). A short ordering exercise with feedback would target the skill directly.

**Dashboard pop-up text:**
The player completed the watershed glyph puzzle only with DANI's help: five arrangements were submitted incorrectly over about four minutes, and after the fifth the player accepted DANI's offer to place the pieces, which makes the point yellow (green requires an independent solution within five attempts). The logs show the supports were used — the player asked DANI about watershed sizes after the second miss and accepted the replay of Dr. Toppo's watershed lesson after the third — yet the fourth and fifth arrangements were still wrong after the hint to order the pieces by size. This may indicate difficulty judging relative drainage-area size from the terrain pieces. Consider asking the student to rank several watershed diagrams by size and explain which river would carry the most water.

---

## Unit 2, Progress Point 5: Classified Information

**Yellow-result trigger:**
Score = correct classifications − (incorrect classifications ÷ 3) inside the window (previous `DialogueNodeEvent:23:42` → latest, ending 15:21:37); green requires a score of at least 4. The player made 6 correct and 8 incorrect selections: 6 − 2.67 = 3.33. Reason code `EXCESS_MISCLASSIFICATIONS`, `wrong_number = 8` (2 claim, 5 reasoning, 1 evidence); green allows at most six incorrect selections.

**Performance summary:**
Repairing DANI required classifying six highlighted passages of an argument as claim, evidence or reasoning. The player made 14 selections in 7 minutes 32 seconds (15:06:27–15:13:59): the first five were incorrect, then correct and incorrect selections alternated until all six passages were classified.

**Gameplay evidence:**
- Feedback sequence: wrong ×5 (15:06:27–15:07:50), correct, correct, wrong, correct, correct, correct, wrong, wrong, correct (15:08:01–15:13:59).
- Misclassified passages by their actual role: five were reasoning (for example "Water moving through more soil makes it cleaner is reasoning because it is an accurate statement that explains why the evidence..." and the statements about dissolved pollutants, dissolved salt, the heavier ball and ice formation), one was evidence ("The depth of the wells... was collected from the environment"), two were claims ("salt is not destroyed when it is added to a glass of water" and "steam is gaseous water").
- Selections came 4–80 seconds apart; DANI closed the activity with "Now making arguments should be a breeze!"

**Possible learning need:**
This point targets recognising a passage's role from its function in the whole argument. Five of the eight errors were on reasoning passages — the first four selections all misclassified reasoning — so the player may have difficulty recognising the statement that explains why the evidence supports the claim, as distinct from the evidence itself or the conclusion. This is an interpretation.

**Potentially underused support:**
Dr. Toppo's feedback after each wrong selection states the passage's actual role and why. Errors continued after that feedback (three incorrect selections after the first correct one), so the player may not have fully applied it. The logs cannot confirm whether the player re-read the whole argument before each selection.

**Suggested instructor intervention:**
Give the student a short argument and ask them to mark each sentence as observed data (evidence), the conclusion (claim), or the explanation of why the data supports the conclusion (reasoning). Emphasise the test "Was this collected, is it the answer, or does it explain?" and practise with two or three fresh passages, focusing on the reasoning sentences.

**Dashboard pop-up text:**
The player completed the argument-component classification task but made 8 incorrect selections (6 correct), above the six allowed, so the point is yellow. The first five selections were all wrong, and five of the eight errors were on reasoning passages, for example the statement that water moving through more soil makes it cleaner; two were on claims and one on evidence. Errors continued after Dr. Toppo's feedback named each passage's actual role. This may indicate difficulty recognising reasoning as the statement that explains why the evidence supports the claim, as distinct from the evidence itself or the conclusion. Consider giving the student a short argument and asking them to mark each sentence as observed data, conclusion, or explanation of the link between them.

---

## Unit 2, Progress Point 6: Which Watershed? Part I

**Yellow-result trigger:**
Green requires the flow-rate choice (`DialogueNodeEvent:20:43`); the point is yellow when `20:44` (waterfall height) or `20:45` (salinity) fires in the window (latest `23:42` → latest `20:46`, 15:21:37–15:31:41). `20:44` fired. Reason code `WRONG_EVIDENCE_SELECTED`, `wrong_choice = waterfall height`.

**Performance summary:**
Using the drone, the player scanned all readings at the eastern and western waterfalls in about six minutes. When Dr. Toppo asked which data point would best identify the larger watershed, the player answered "Waterfall height" 18 seconds after the two claims were presented. Under the rubric this earns 0 of 0.5 points.

**Gameplay evidence:**
- Scans logged: eastern ocean salinity (drone test, 15:21:59), eastern river distance (15:24:46), eastern salinity, flow and height (15:25:22–15:25:31); western distance (15:26:42), western salinity, height and flow (15:27:55–15:28:04); DANI's data table at 15:28:04.
- Early in the task the player chose the dialogue line "Can't we just pick a watershed at random and call it good?" (`18:138`, 15:22:33); DANI replied that more evidence was needed.
- Dr. Toppo's framing at 15:28:47 ("Keep in mind that not all of the evidence is useful when building your argument"); the two candidate claims at 15:30:16–15:30:26; choice `20:44` "Waterfall height." at 15:30:44; the activity closed with `20:46` at 15:31:41.
- No chat-history or map events were logged in the window.

**Possible learning need:**
This point targets identifying flow rate as the observation that reflects drainage-area size. Choosing waterfall height may indicate the player associated the most visible difference between the falls with watershed size rather than reasoning about how much land drains to each river. This is an interpretation.

**Potentially underused support:**
The investigation dialogues explain the relevance of each observation, and the in-game chat log can be used to review them; the logs show no chat use in this window. The comparison table appeared about 2.5 minutes before the question; the logs cannot show how it was used.

**Suggested instructor intervention:**
Ask the student to explain what a watershed is and why a larger drainage area produces more water in the river. Then go through the four observations (flow rate, waterfall height, salinity, distance to the ocean) and ask, for each, whether it tells us anything about how much land drains to the river.

**Dashboard pop-up text:**
After collecting all the waterfall readings, the player answered Dr. Toppo's question about the most relevant evidence with "waterfall height" instead of water flow rate, which makes the point yellow (this single-choice point earns credit only for flow rate). The answer came 18 seconds after the two claims were presented, and no use of the chat history to review the investigation dialogues was logged; earlier the player had asked DANI whether they could just pick a watershed at random. The choice may indicate the player linked the most visible difference between the falls to watershed size rather than reasoning that a larger drainage area delivers more water. Consider asking the student to say, for each observation, whether it tells anything about how much land drains to the river.

---

## Unit 2, Progress Point 7: Which Watershed? Part II

**Yellow-result trigger:**
Green requires the success node (`27:7`) and at most three incorrect-argument nodes in the window (previous `questFinishEvent:54` → latest, ending 15:40:55; no earlier occurrence). Success fired, but eight incorrect nodes fired. Reason code `EXCESS_ATTEMPTS`, `attempt_number = 9`, `wrong_claim_number = 2`, `irrelevant_evidence_number = 6`.

**Performance summary:**
The player built the argument about which watershed is larger in 3 minutes 4 seconds (15:32:56–15:36:00), submitting nine times; the first eight were incorrect. Under the rubric a correct argument on the ninth attempt earns 0 of 3 points.

**Gameplay evidence:**
- Before starting, the player declined Dr. Toppo's review ("Do you have any questions about arguments, Deputy?" → "Nope.", 15:32:17; "I'm ready to argue.", 15:32:25). No reference panel was opened during the session (no tool events).
- Submissions with claim `I`: `B,C,1,I` 15:32:56 (multiple evidence pieces), `C,1,I` 15:33:18 ("while salinity may be an important factor, it does not help predict the size of watershed"), `D,1,I` 15:33:42 (longer river downstream), `B,1,I` 15:34:00 ("Both your claim and evidence does not link to your reasoning. Try using another piece of evidence and a different claim."), `A,1,I` 15:34:15 ("Your evidence does not fit with your claim. Try using a more appropriate claim.").
- Submissions with claim `II`: `D,1,II` 15:34:31 (downstream river), `C,1,II` 15:35:09 (salinity; node `C` had been hovered for 15 seconds beforehand), `B,1,II` 15:35:30 ("Your claim makes sense however the waterfall height might not be the best piece of evidence"), and `A,1,II` 15:36:00 → "Well done! You have made the best argument possible."
- The feedback identified `B` as waterfall height, `C` as salinity and `D` as the downstream river; `A`, the evidence in the winning argument, is therefore the flow-rate observation. Submissions were 15–38 seconds apart.

**Possible learning need:**
Two skills are involved: choosing the claim the data supports and selecting relevant evidence. The player tried every evidence option under the first claim before changing it, then cycled the same irrelevant options again under the right claim. The player may need support both in reading the comparison table to decide which watershed is larger and in recognising that only flow rate indicates watershed size — consistent with the "waterfall height" choice on the previous point. This is an interpretation.

**Potentially underused support:**
Neither reference panel (Watershed Graph, Waterfall Data) was opened during the session (a logged absence), and the pre-argument review was declined (logged). Dr. Toppo's per-attempt feedback named the problem each time, and the claim was changed only after the fifth attempt.

**Suggested instructor intervention:**
Walk through the waterfall comparison table: which river has the higher flow rate, and what does that imply about the land draining to it? Then ask the student to sort the four observations into "tells us about watershed size" and "does not". Finally, have them state the claim and the one piece of evidence that supports it, in their own words.

**Dashboard pop-up text:**
The player completed the watershed argument but needed nine submissions — eight incorrect — against a limit of four attempts, so the point is yellow. The logs show the player kept the first claim while trying every evidence option, changed the claim only after Dr. Toppo's fifth feedback said to, and then cycled the irrelevant options again under the new claim before landing on flow rate; submissions were 15–38 seconds apart. The reference panels were not opened during the session, and the pre-argument review was declined. The pattern may indicate difficulty using the comparison table to decide which watershed is larger and recognising flow rate as the only size-related evidence. Consider working through the table together and having the student sort the observations into relevant and irrelevant.

---

## Unit 3, Progress Point 1: Supply Run (Establishing a Foothold)

**Yellow-result trigger:**
Green requires more than one correct-river confirmation (`DialogueNodeEvent:10:30`) in the window (previous `DialogueNodeEvent:11:22` → latest, ending 16:42:06; no earlier occurrence). None fired; wrong-river nodes fired three times (`10:31` twice, `10:32` once). Reason code `EXCESS_WRONG_RIVERS`, `wrong_river_number = 3` (green allows at most one wrong crate).

**Performance summary:**
The player had to float Tera's three crates down the river that flows past her camp. All three crates were released into the wrong river within about two minutes, so none was delivered. Under the rubric this earns 0 of 3 points.

**Gameplay evidence:**
- Tera's instruction at 16:35:45: the crates landed "upstream of our current location, so check your map"; DANI opened the map at 16:37:10 with the hint "Both of these rivers start at the south, and their currents run north." The player selected the "Water" legend entry (16:37:17) and closed the map at 16:37:21 (11 seconds).
- Crate 1 placed on the hoverboard 16:37:22 and grabbed 16:37:26; map opened 16:37:28–16:37:32 (4 seconds); lost at 16:38:02 (`10:31`: "The locator on the crate seems to be moving away from my location... I'd suggest checking the map to see which river flows by my camp before sending the next one").
- Crate 2 grabbed 16:38:45; map opened 16:38:51–16:38:54 (3 seconds); lost at 16:39:07 (`10:31` again).
- Crate 3 grabbed 16:39:36 with no map check; lost at 16:40:08 (`10:32`: "You picked the wrong river... water flows from high elevations to lower elevations. This means that rivers and streams flow into the ocean...").

**Possible learning need:**
This point targets using the map to decide which river is hydrologically connected to Tera's camp. The map was checked for only three to four seconds before the first two crates and not at all before the third, and all three went into the wrong river, which may indicate the player chose a river by its general northward direction rather than by tracing its course to the camp. This is an interpretation; the logs do not record which river was chosen.

**Potentially underused support:**
Map use is logged (three sessions totalling about 18 seconds), and Tera's first feedback explicitly suggested checking which river flows by her camp before the next crate; the second crate was released 13 seconds after a three-second check. The logs cannot show whether the player watched Dr. Toppo's water-flow video or reviewed the chat history for Tera's clue that the crates landed upstream of her location.

**Suggested instructor intervention:**
On the watershed map, ask the student to find Tera's camp, trace each river from its source to the ocean, and explain which one passes the camp and why an object dropped upstream ends up there. Then ask what a useful map check looks like before releasing a crate — following the river's line to the camp, not just noting its direction.

**Dashboard pop-up text:**
All three of Tera's supply crates were released into the wrong river, so none reached her camp and the point is yellow (green requires at least two correct deliveries). The logs show short map checks of three to four seconds before the first and second crates, none before the third, and the three losses came within about two minutes; Tera's feedback after the first loss suggested checking which river flows past her camp. This may indicate the player identified a river by its general northward direction rather than by tracing its course to the camp. Consider having the student trace both rivers on the map from source to ocean, identify which one passes Tera's camp, and explain why a crate floats to the camp only from that river.

---

## Unit 3, Progress Point 2: Pollution Solution Part I

**Yellow-result trigger:**
Score = 5 − penalty(downstream reminders) − penalty(redundant-test reminders), where each penalty is 0 for at most one reminder, 1 for two or three, and 2 for four or more; green requires at least 3. Window: previous `DialogueNodeEvent:11:34` → latest, ending 16:50:37 (no earlier occurrence). Counts: 5 downstream reminders (`11:27`) and 8 redundant-test reminders (`11:29` ×4, `11:230` ×4), so 5 − 2 − 2 = 1. Reason code `EXCESS_SENSOR_REMINDERS`, `downstream_reminder_number = 5`, `redundant_reminder_number = 8`.

**Performance summary:**
Over six minutes (16:44:30–16:50:37) the player dropped sensors along the river to find the pollution source — 23 readings were logged (16 polluted, 7 clean) and the source was identified — but DANI's reminders about sampling direction fired 13 times. Under the rubric this earns 1 of 5 points.

**Gameplay evidence:**
- "Pollution will only flow downstream, so we need to test further upstream." (`11:27`) fired five times: 16:46:22, three times within 12 seconds (16:47:03–16:47:15), and 16:49:30.
- "Green checkmark means clean. You won't need to check upstream of a clean sensor." (`11:29`) fired four times (16:46:37, 16:48:39, 16:48:53, 16:49:01).
- "You are as far upstream as you can go in this branch. Please proceed downstream." (`11:230`) fired four times (16:46:44, 16:46:52, 16:48:45, 16:49:56).
- Readings came 3–10 seconds apart in runs (for example seven polluted readings in 68 seconds at 16:47:22–16:48:30); no map-open or chat-history events were logged during the task.

**Possible learning need:**
This point targets reasoning about upstream and downstream from sensor results. Repeated runs of the same reminder — continuing in the wrong direction after a polluted reading, continuing upstream past a clean sensor, and pushing past the top of a branch — may indicate difficulty translating a red or green result into "the source must be upstream of red and cannot be upstream of green". This is an interpretation; the placement decisions themselves are not logged.

**Potentially underused support:**
DANI's reminders state the rule each time and fired 13 times, so the player may not have adjusted the sampling strategy after them. No map opening was logged during the task, so the player may have benefited from checking the sensor-result overlay on the map to plan the next drop. No chat-history use was logged.

**Suggested instructor intervention:**
Draw a branching river with a few red and green sensor marks and ask the student where the source could and could not be, and where the next sensor should go. Emphasise the two rules: a polluted reading means test upstream; a clean reading rules out everything upstream of it.

**Dashboard pop-up text:**
The player traced the pollution source with the drone sensors but triggered 13 reminder dialogues — 5 for testing in the wrong direction and 8 for unnecessary tests (checking upstream of a clean sensor, or pushing past the top of a branch) — which drops the score to 1 of 5 and makes the point yellow. Three wrong-direction reminders fired within 12 seconds, 23 readings were taken in six minutes, and no map check was logged during the task. This may indicate difficulty converting a red or green reading into where the source can and cannot be. Consider sketching a branching river with sample results and asking the student to mark where the source could be and where the next sensor should go.

---

## Unit 3, Progress Point 3: Pollution Solution Part II (Pollution Argument)

**Yellow-result trigger:**
A base score comes from the count of graded conversation-84 nodes in the window (previous `questFinishEvent:18` → latest, ending 17:08:52; no earlier occurrence): at most 3 → 3 points, 4 → 2, 5 → 1, 6 or more → 0; one bonus point is added for opening the Pollution Site Data panel; green requires at least 3. The count was 7 (six incorrect submissions plus the success node, which the current script also counts), so the score is 0 + 1 = 1. Reason code `EXCESS_ATTEMPTS`, `wrong_argument_number = 6` (2 claim, 4 reasoning, 0 evidence), `backing_info_phrase = opened`.

**Performance summary:**
The player built the argument about where the pollutant enters the river in seven submissions over 2 minutes 14 seconds (16:53:40–16:55:54); the first six were incorrect and the seventh was correct. Both reference panels were opened after the second miss and again before the final submission. Under the rubric a correct argument on the seventh attempt earns 0 points, plus the 1-point reference bonus, so 1 of 4.

**Gameplay evidence:**
- The player declined the pre-argument review ("I think I'm good", 16:52:52; "I'm ready for argumentation", 16:53:02); the session opened at 16:53:16.
- Submissions and feedback: `B,1,II` 16:53:40 → claim "does not take into consideration that water can carry pollution"; `B,4,II` 16:54:01 → "Your argument is logical. But it does not accurately describe how water moves." followed by the nudge to click the Backing Information orbs; the Watershed Image and Pollution Site Data panels were opened at 16:54:14–16:54:15 (closes not logged); `A,2,II` 16:54:34 → claim feedback again; `A,2,I` 16:54:45 → "Your reasoning does not explain how water behaves. Pollutants travel downstream with water flow"; `A,3,I` 16:55:21 → "You reasoned that water must flow from north to south. This is not always true in nature."; `A,2,I` 16:55:34 — the same argument as the fourth submission → "Your claim and evidence makes sense. But, your reasoning does not explain how water behaves"; both panels reopened 16:55:52; `A,5,I` 16:55:54 → "Great Job! You made the best argument possible."
- Submissions were 11–36 seconds apart; reasoning node `5`, used in the winning argument, had been hovered for about five seconds at 16:54:25 and one second at 16:55:13.

**Possible learning need:**
This point targets selecting reasoning that links the sensor pattern (clean upstream, polluted downstream) to the claim. Four of the six errors were reasoning problems, including a submission reasoning that water must flow from north to south, and the sixth submission repeated an argument already rejected, so the player may need support articulating that dissolved pollution travels downstream with the flow regardless of compass direction, and support keeping track of which reasoning statements the feedback has already ruled out. This is an interpretation.

**Potentially underused support:**
Both reference panels were opened twice (logged), the second time two seconds before the winning submission. Dr. Toppo's feedback named the faulty component each time, and the player changed that component in most cases (claim after claim feedback, reasoning after reasoning feedback) — except for the identical resubmission. The sensor results and DANI's marked source from the previous task were available; the logs cannot show whether they were re-checked.

**Suggested instructor intervention:**
Ask the student to explain how the sensor pattern shows where the pollution enters the river, then to state the reasoning as a general rule ("dissolved pollution moves downstream with the water, so..."). Contrast that with the "water flows north to south" statement they chose and ask why map direction is not the rule; then have them read each reasoning option aloud and say which one states the rule before choosing.

**Dashboard pop-up text:**
The player built the pollution-source argument and opened the reference panels, but needed seven submissions — six incorrect — against a limit of three, so the point is yellow (1 of 4 rubric points, the 1 being the reference-panel bonus). Feedback flagged the claim twice and the reasoning four times, including a submission reasoning that water must flow north to south, and the sixth submission repeated the fourth argument unchanged. This may indicate difficulty stating the general rule that pollutants move downstream with the flow, independent of map direction, and difficulty telling which reasoning statement the feedback referred to. Consider asking the student to explain the sensor pattern and phrase the reasoning as a rule before choosing a reasoning statement.

---

## Unit 3, Progress Point 4: Forsaken Facility (Dissolved-Particles Glyph)

**Yellow-result trigger:**
Green requires the completion gate (`DialogueNodeEvent:78:24`) and fewer than three of the eight graded conversation-78 nodes (one per wrong submission, plus DANI's assist node `78:23`) in the window (latest `questActiveEvent:18`, 16:59:08 → latest `DialogueNodeEvent:73:200`, 17:10:29). Five graded nodes fired (`78:3`, `78:7`, `78:9`, `78:12`, `78:23`), so the score is 0. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 4` (green requires an independent solution within three attempts).

**Performance summary:**
At the entrance of the alien facility the player had to order three glyph pieces showing the stages of a material dissolving in water. Four arrangements were wrong within about 55 seconds; the fifth submission triggered DANI's assist, and DANI showed the correct order. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- Pieces placed in docks C, B and D at 16:59:11–16:59:16 → first-attempt feedback for three or more wrong (`78:3`, 16:59:20: "I believe the pieces are intended to be ordered in a specific way.").
- Re-placed in C, D, B at 16:59:34–16:59:40 → second-attempt hint (`78:7`, 16:59:43: "The circular images appear to represent a closer view of the water and particles in it. I believe this is how the water might appear under a microscope.").
- Docks D and B re-placed at 16:59:55–16:59:57 → third attempt, one or two wrong (`78:9`, 16:59:59: "close to the correct order"); D and B re-placed at 17:00:09–17:00:11 → fourth attempt, one or two wrong (`78:12`, 17:00:13: "That is very close, TK. I believe you can solve it."); D and B re-placed at 17:00:24–17:00:26 → fifth submission → DANI's assist (`78:23`, 17:00:29: "I believe I have calculated the correct order for the puzzle. Allow me to assist, TK. Activating holid projector.").
- The player then placed B and D (17:00:42–17:00:44) and the completion gate fired at 17:00:47. Submissions were 12–14 seconds apart; from the third attempt on only the same two docks were re-placed before each submission.

**Possible learning need:**
This point targets understanding how a soluble material behaves as it dissolves — particles added, still visible, then mixed and spread out so they can no longer be seen — and matching pictures of those stages. The two-piece swapping on the last three attempts, with "close" feedback each time, may indicate uncertainty about the order of two adjacent stages rather than of the whole sequence. This is an interpretation.

**Potentially underused support:**
DANI's hints (the microscope view, then "close" and "very close") were delivered; the chat tool for reviewing earlier explanations was not used in the window (no chat events), and the logs cannot show whether the player related the pieces to the pollution-tracing experience from the previous quest. DANI's post-puzzle explanation of the dissolving process was delivered after the assist.

**Suggested instructor intervention:**
Ask the student to describe what happens to salt or sugar stirred into water over time — visible grains, then smaller and fewer, then none visible although the material is still there — and to put three pictures of that process in order, explaining why the dissolved material is still present even when it cannot be seen.

**Dashboard pop-up text:**
The player did not solve the dissolved-particles glyph puzzle independently: four arrangements were wrong within about a minute, and on the fifth submission DANI ordered the pieces, which makes the point yellow (green requires an independent solution within three attempts). From the third attempt on the player swapped the same two pieces before each submission, and DANI's hints that the images show water and particles as seen under a microscope, and that the order was close, did not lead to the correct sequence. This may indicate difficulty sequencing the stages of dissolving — particles added, still visible, then spread out and no longer visible. Consider asking the student to describe what happens to salt or sugar stirred into water over time and to order three pictures of that process.

---

## Unit 3, Progress Point 5: Part of a Balanced Ecosystem (Plant the Superfruit Seeds)

**Yellow-result trigger:**
Score = correct plantings − 0.5 × wrong plantings in the window (previous `DialogueNodeEvent:10:194` → latest, ending 17:16:30; no earlier occurrence); the dashboard turns green at 2.5 or more. Four wrong plantings and none correct give −2. Reason code `EXCESS_WRONG_PLANTINGS`, `wrong_planting_number = 4` (green allows at most one wrong plot).

**Performance summary:**
Asked to plant four superfruit seeds in garden plots that receive the nutrient released at the temple, the player planted all four in plots that do not receive it, in 2 minutes 36 seconds (17:11:45–17:14:21). Tera ended the activity after the fourth wrong plot. Under the rubric this is 0 − 4 × 0.5 = −2 of 4 points.

**Gameplay evidence:**
- DANI marked the garden plots and opened the map at 17:11:03; the player set the waypoint and moved it twice, closing the map at 17:11:08.
- Planting 1 at 17:11:45 → `73:164` ("DANI is telling me that you picked the wrong spot. Is the water flowing downstream from the temple to here?") with hints to check the map, that water flows from high to low elevation, and to use the ocean in the north to pick the next plot; map 17:12:17–17:12:20 (waypoint moved twice).
- Planting 2 at 17:12:25 → `73:168` ("another wrong spot. You need to find a planting spot that is downstream from the temple") with the reminder that all watersheds flow toward the ocean; map 17:12:53–17:13:01 (waypoint moved five times to another region).
- Planting 3 at 17:13:29 → `73:168` again; map 17:13:57–17:14:02 (waypoint moved three times to a third region); planting 4 at 17:14:21 → `73:171` (activity ends: "We're losing daylight").
- Each planting was preceded by a map check of three to eight seconds with waypoint moves; the waypoint was moved to a different part of the map before each planting; all plots are logged with the same object name, so the chosen plots cannot be identified.

**Possible learning need:**
This point targets predicting which plots lie downstream of the nutrient source. Four wrong plots in different parts of the map, despite Tera's hints restating the downstream rule after each miss, may indicate difficulty tracing flow direction on the map from the temple toward the ocean and therefore which plots the nutrient can reach. This is an interpretation.

**Potentially underused support:**
Map and waypoint use are logged (five short sessions), and Tera's feedback after each planting restated the rule. The map checks lasted three to eight seconds each, which leaves little time to trace a river from the temple to a plot; the logs cannot show whether the chat history was used to revisit the hints.

**Suggested instructor intervention:**
Using the Unit 3 watershed map, ask the student to mark the temple release point and the ocean, draw arrows for the direction of flow along each river, and then circle the plots the nutrient can reach. Ask them to explain why a plot upstream of the temple or on a different branch cannot receive it.

**Dashboard pop-up text:**
The player planted all four superfruit seeds in plots that do not receive the temple's nutrient, so the score is −2 of 4 and the point is yellow (green allows at most one wrong plot). The logs show a map check of three to eight seconds with waypoint moves before each planting, and Tera's hints after each miss — water flows from high to low elevation toward the ocean in the north, so the plot must be downstream of the temple — yet each new plot, in a different part of the map, was still wrong. This may indicate difficulty tracing flow direction on the map from the temple toward the ocean. Consider having the student draw flow arrows on the map and circle the plots the nutrient can reach.

---

## Unit 4, Progress Point 1: Well What Have We Here?

**Yellow-result trigger:**
Score = 0.5 if the correct water-table answer (`DialogueNodeEvent:88:5`) appears in the window, plus 1.0 if the Unit 4 soil key puzzle took 30 seconds or less (0.5 if 30–90 seconds); green requires at least 1. Window: latest `DialogueNodeEvent:88:0` (17:22:00) → the Unit 4 soil-key close (17:29:33). The player chose the wrong answer (`88:7`) and the puzzle took 168 seconds, so the score is 0. Reason code `SCORE_BELOW_THRESHOLD`, `choice_phrase` = chose "it's any water found underground", `duration_phrase` = took 168 seconds.

**Performance summary:**
Anderson asked what the water table is; the player answered "It's any water found underground" 16 seconds later. The soil key puzzle that followed took 2 minutes 48 seconds. Under the rubric this earns 0 of 1.5 points.

**Gameplay evidence:**
- Anderson's question (`88:4`, 17:25:52: "What on Earth is the 'water table'...?") → answer `88:7` "It's any water found underground." at 17:26:08; the correct option (the boundary between saturated and unsaturated soil layers) was not selected, and the question is not repeated.
- Soil key puzzle 17:26:44–17:29:33: 48 drag steps; the selector swept the full soil range (bedrock to gravel) about eleven times; the correct soil (clay-sand, logged as `isCorrectSelection = true`) was passed eight times while the water level was too low or too high (17:26:58, 17:27:15, 17:27:41, 17:28:16, 17:28:31, 17:28:45, 17:29:05, 17:29:20) until clay-sand coincided with a proper level at 17:29:32; the level read "Proper" only during the final 25 seconds.

**Possible learning need:**
Two ideas are involved: the definition of the water table (the top of the saturated zone, not any underground water), and controlling the water level through soil choice in the puzzle. The wrong answer is the common misconception named in the grading notes; the repeated end-to-end sweeping may indicate the player was cycling through materials rather than predicting how each affects retention. Both are interpretations.

**Potentially underused support:**
Dr. Toppo's groundwater tutorial precedes Anderson's question; the logs cannot show whether it was watched. No chat-history use was logged. In the puzzle the level indicator gives immediate feedback, and the sweeps show it was being watched, but the target combination was passed eight times before it was recognised.

**Suggested instructor intervention:**
Ask the student to define the water table and draw a cross-section with unsaturated soil above and saturated soil below, labelling the boundary. Then ask how choosing clay versus gravel would change how much water is held and where the level ends up, and have them predict the effect of each soil before moving the selector.

**Dashboard pop-up text:**
The player answered Anderson's water-table question with "any water found underground" instead of the boundary between saturated and unsaturated soil, and took 168 seconds to complete the soil key puzzle (30 seconds earns full credit, 90 seconds half), so the score is 0 and the point is yellow. During the puzzle the selector swept end to end about eleven times and passed the correct clay-sand setting eight times before the water level was also in range. The wrong definition is the common misconception that the water table is simply underground water, and the sweeping may indicate trial and error rather than predicting each soil's effect on the water level. Consider having the student draw and label a cross-section of the water table.

---

## Unit 4, Progress Point 2: Power Play – Floors 1 & 2 (Infiltration Glyph)

**Yellow-result trigger:**
Green requires the post-puzzle explanation node (`DialogueNodeEvent:88:11`) and none of the yellow nodes (`102:9`, `102:10`, `102:12`, `102:18`, `102:23`) in the window (latest Unit 4 soil-key close, 17:29:33 → latest `questActiveEvent:48`, 17:38:56). `102:10` and `102:18` fired. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 4` (green requires an independent solution within three attempts). The code recognises the accepted-assist nodes `102:20`/`102:21`, which were added to its key list on 2026-09-16 after this log exposed that path.

**Performance summary:**
In the infiltration glyph puzzle (ordering gravel, sand, clay and the water-table piece by how water passes through them) the player submitted four incorrect orders in about two minutes, accepted DANI's offer of help after the fourth, and DANI ordered the pieces. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- A piece was placed at 17:30:04; wrong-order feedback at 17:30:10 (`102:3`, three or four of the four pieces wrong), 17:30:52 (`102:7`: "The images appear to represent the size of the particles of different types of soil."), 17:31:35 (`102:10`, three or four wrong: "a graph that shows the rate at which water passes through soils of different types."), 17:32:03 (`102:18`, three or four wrong: "Would you like me to assist, TK?").
- The player accepted (`102:20`, 17:32:08) and DANI ordered the pieces (`102:21`, 17:32:09); the explanation `88:11` followed at 17:32:13 and `88:12` at 17:32:20 ("soils with larger particles like sand allow water to move through them more quickly...").
- Submissions were 26–44 seconds apart. Between the offer and the completion the log contains no piece pick-up or placement inputs, only camera and visibility events, which is how the accepted-assist path was identified.

**Possible learning need:**
This point targets the link between particle size and infiltration rate (fastest through gravel, then sand, slowest through clay) and the meaning of the water-table piece. Three of the four arrangements had three or four of the four pieces misplaced, including the one made after DANI named the infiltration-rate graph, which may indicate the player had not yet connected particle size to how fast water passes through. This is an interpretation.

**Potentially underused support:**
DANI's hints named the concept (particle size, then the infiltration-rate graph) and the assist was accepted at the first offer. The logs cannot show whether the player consulted the chat history to revisit Dr. Toppo's groundwater tutorial or the soil descriptions from the previous point; no chat use was logged.

**Suggested instructor intervention:**
Ask the student to order gravel, sand and clay by particle size and then by how quickly water passes through, explaining the link (larger particles → larger spaces → faster infiltration). A quick sketch of particles with the spaces between them makes the relationship concrete.

**Dashboard pop-up text:**
The player did not solve the infiltration glyph puzzle independently: four arrangements were wrong within about two minutes, and after the fourth the player accepted DANI's offer and DANI ordered the pieces, which makes the point yellow (green requires an independent solution within three attempts). Three of the four submissions had three or four of the four pieces out of order, even after DANI's hints about particle size and the infiltration-rate graph. This may indicate the player had not yet linked soil particle size to infiltration rate — water passes fastest through gravel, more slowly through sand, and slowest through clay. Consider asking the student to order the three soils by particle size and by infiltration rate and to explain why the two orders match.

---

## Unit 4, Progress Point 3: Power Play – Floors 3 & 4

**Yellow-result trigger:**
Score = 1 if the third-floor machine was changed exactly once, plus 2 if the fourth-floor machine was changed exactly once (1 if twice); green requires more than 1. Window: previous `questActiveEvent:50` → latest, ending 17:45:04 (no earlier occurrence; the activity starts at `questActiveEvent:48`, 17:38:56). Floor 3 had 10 canister changes and floor 4 had 15, so the score is 0. Reason code `SCORE_BELOW_THRESHOLD`, `floor3_attempts = 10`, `floor4_attempts = 15`.

**Performance summary:**
On both floors the player cycled rapidly through the soil canisters rather than setting the pipe's soil once: ten changes in 11 seconds on floor 3 and fifteen changes in 32 seconds on floor 4. Both floors were completed. Under the rubric this earns 0 of 3 points.

**Gameplay evidence:**
- Floor 3: the "Soil View" panel was inspected at 17:39:04 (DANI: a gravel layer with even more space between the particles); canister changes 17:40:17–17:40:28: Bedrock, Clay, Sand, Bedrock, Clay, Sand, Bedrock, Clay, Sand, Gravel — the same three options cycled three times before Gravel; the floor was completed with Gravel.
- Floor 4: Soil View inspected at 17:42:39 (DANI: "another sand layer. The space between these particles is fully saturated with clean water — we are in the water table."); canister changes 17:43:01–17:43:33: Bedrock and Clay alternated five times, then Gravel, Clay, Bedrock, Gravel, Sand; the floor was completed with Sand.
- Changes were about one second apart on floor 3 and 1–7 seconds apart on floor 4.

**Possible learning need:**
This point targets predicting which soil produces the water level and flow the pipe needs. Cycling through the same options repeatedly, including bedrock three times on floor 3 and five times on floor 4, may indicate the player was scanning the options rather than predicting from soil properties. This is an interpretation.

**Potentially underused support:**
The Soil View panels describing the surrounding layer were inspected on both floors (logged), and each machine change gives immediate visual feedback. The one-second spacing on floor 3 leaves little time to observe the effect of a change before the next. No chat-history use was logged.

**Suggested instructor intervention:**
Before touching the machine, have the student predict aloud which soil will let the right amount of water through and why (permeability), test it, and only then change it. A predict-observe-explain routine with the three soils and bedrock targets the cycling pattern directly.

**Dashboard pop-up text:**
The player completed floors 3 and 4 of the alien well, but changed the soil canister ten times on the third floor (within 11 seconds) and fifteen times on the fourth, where the rubric expects one change on each floor, so the score is 0 and the point is yellow. On floor 3 the same three options were cycled three times before gravel was set; on floor 4 bedrock and clay were alternated five times before the other soils were tried. This may indicate scanning the options rather than predicting which soil produces the required water flow from its permeability. Consider asking the student to predict which soil should work before each change and to explain the prediction in terms of how fast water moves through gravel, sand, clay and bedrock.

---

## Unit 4, Progress Point 4: Power Play – Floor 5 and the Drill Task

**Yellow-result trigger:**
Score = 1 if the two-layer machine had exactly one change per layer, plus 1 if the single-layer machine had exactly one change, plus 2 for a correct drill depth with no wrong depths (1 with one wrong depth); green requires more than 2. Window: latest `questActiveEvent:50` (17:45:04) → latest `questActiveEvent:36` (17:59:14; the quest event re-fired on a scene change, which extends the window by six minutes of dialogue only). Machine 1 had 9 + 7 changes, machine 2 had 2, and three wrong drill choices were logged, so the score is 0. Reason code `SCORE_BELOW_THRESHOLD`, `machine_attempt_number = 18`, `wrong_choice_number = 3`.

**Performance summary:**
On floor 5 the player made 18 canister changes across the two machines (three is optimal), then in the drill task chose three wrong depths — each once — before choosing the fourth floor, which produced clean water. Under the rubric this earns 0 of 4 points.

**Gameplay evidence:**
- Soil View inspected at 17:45:14 (DANI: bedrock, tightly packed particles with no space for water).
- Machine 1 (17:45:47–17:46:18): the top row alternated Clay and Bedrock nine times and the bottom row seven times, mostly 1–3 seconds apart (final setting Clay / Clay).
- Machine 2 (17:46:46–17:46:54): Sand placed, then switched to Gravel.
- Drill: DANI's prompt at 17:48:01; the first choice came 90 seconds later — "Drill ALLLL the way down" (17:49:56) → "the drill has struck bedrock... there is no space for water"; first floor (17:50:23) → "I am not observing any water"; second floor (17:50:45) → the same; fourth floor (17:51:06) → "You drilled the well to the perfect depth resulting in clean water." Choices were 22–27 seconds apart and no depth was repeated.

**Possible learning need:**
This point targets where groundwater sits (the saturated zone above bedrock) and how layered soils control flow. The drill choices moved from the deepest option to the two shallowest and then to the correct depth without repeats, which suggests the outcome messages were used to eliminate options rather than to predict the water table's depth from the floors visited; the clay/bedrock toggling on both rows of machine 1 may indicate uncertainty about which layer combination lets water through. Both are interpretations.

**Potentially underused support:**
DANI's floor-by-floor descriptions in this well (sand, clay, gravel, "we are in the water table", bedrock) were delivered on the way down, and each drill outcome message explains why that depth failed; the 90-second pause before the first choice and the absence of repeats are consistent with the messages being read, but the logs cannot show what the player related them to. No chat-history use was logged.

**Suggested instructor intervention:**
Draw the well's layers with the water table marked and ask the student where a drill must stop to reach clean water, and why shallower depths find no water and the deepest hits bedrock. Then ask them to use DANI's floor descriptions (which floor was "in the water table") to predict the depth before drilling.

**Dashboard pop-up text:**
On the fifth floor the player changed soil canisters 18 times across the two machines (three changes is optimal), alternating clay and bedrock on both rows of the first machine, and then chose three wrong drilling depths before reaching clean water on the fourth floor, so the score is 0 and the point is yellow. The drill choices moved from the deepest option to the two shallowest, each tried once, which suggests the outcome messages were used to eliminate depths rather than to predict the right one. The canister toggling may indicate uncertainty about which layer combination lets water through to the well. Consider having the student sketch the layers with the water table marked and explain why only the fourth-floor depth yields clean water.

---

## Unit 4, Progress Point 5: Saving Cadet Anderson

**Yellow-result trigger:**
Green requires a success node (`90:50` or `90:57`) and fewer than three negative-feedback nodes in the window (previous `questActiveEvent:41` → latest, ending 18:14:39; no earlier occurrence, so the activity segment from `questActiveEvent:36`, 17:59:14, is used). Success fired (`90:57`), but 10 negative nodes fired. Reason code `EXCESS_ATTEMPTS`, `attempt_number = 11`, `claim_wrong_number = 6`, `reasoning_wrong_number = 1`, `evidence_wrong_number = 3`.

**Performance summary:**
The player built the argument about why Anderson's bunker keeps flooding in 11 submissions over 3 minutes 3 seconds (18:07:07–18:10:10): 10 incorrect, then a correct argument combining three pieces of evidence. Under the rubric a correct argument after more than five attempts earns 0 of 3 points, and the backing-information bonus was not earned, so 0 of 4.

**Gameplay evidence:**
- Evidence collected before arguing: the missing ceiling (18:00:30), the drones, and the soil composition on three floors — sand above and clay below the first floor with slight flooding; clay above and gravel below the second, no flooding; sand above and bedrock below the third, large-scale flooding with water entering through holes in the ceiling (18:01:29–18:04:41).
- The player declined the pre-argument review ("I think I'm good", 18:06:37; "I'm ready for argumentation", 18:06:44). No backing-information panel was opened in the session (no tool events).
- Seven submissions with claim `I` (18:07:07–18:08:27): `A,1,I`, `B,1,I`, `C,1,I`, `D,1,I` each drew "Are you sure the flooding will resolve by turning off the fountain? Is there a better way to explain how water got into the warehouse?"; `2,I` was flagged as incomplete (no evidence); `D,3,I` drew the claim feedback again; `D,4,I` drew it with "You should consider changing your claim."
- The player switched to claim `II` on the next submission: `D,4,II` 18:08:49 ("Water does not infiltrate upward"), `D,2,II` 18:09:09 and `D,A,2,II` 18:09:24 ("your argument may be missing important evidence"), then `A,D,C,2,II` at 18:10:10 → "Great job! You have made an argument that strongly combines claims, reasoning and evidence." Submissions were 10–46 seconds apart; node `II` was hovered for four seconds before the switch.

**Possible learning need:**
This point targets explaining that the bunker floods because it sits within the saturated zone, permeable sand surrounds it, and the ceiling is open — several pieces of evidence combined. Keeping Anderson's claim (that the flooding will resolve) for seven submissions while cycling the evidence and reasoning may indicate the player did not connect DANI's observation that the fountain pipes cannot account for the water with the need for a different claim; the "infiltrate upward" reasoning names a misconception about groundwater movement. These are interpretations.

**Potentially underused support:**
The argumentation reference panel was not opened (the logs show no tool events in this session), and the pre-argument review was declined. Dr. Toppo's feedback said to change the claim on the seventh submission and the claim was changed on the eighth, so that hint was used immediately. DANI's explanations while collecting evidence were delivered; the logs cannot show how they were used.

**Suggested instructor intervention:**
Ask the student to state what the evidence shows (bunker below the water table, sand around it, holes in the ceiling) and what claim those facts support; then discuss why water cannot infiltrate upward. Have them assemble the argument on paper — claim first, then all the evidence that supports it — before entering the tool.

**Dashboard pop-up text:**
The player eventually built the correct argument about the flooding bunker, but needed 11 submissions — 10 incorrect — where green allows at most two, so the point is yellow. For seven submissions the player kept the claim that the flooding would stop once the fountain was off, cycling the evidence and reasoning while six feedback messages questioned the claim; the claim was changed as soon as the feedback said to, after which one reasoning error (water infiltrating upward) and two missing-evidence flags preceded success. The in-tool reference panel was not opened. This may indicate difficulty connecting the collected evidence (an open ceiling, sand around the bunker, a location in the saturated zone) to a claim. Consider having the student state what each piece of evidence shows before choosing a claim.

---

## Unit 4, Progress Point 6: Desert Delicacies

**Yellow-result trigger:**
Score = the number of garden boxes whose latest camera placement matches the soil suited to the seedling (box 0 gravel, box 1 sand, box 2 clay), or, if higher, the number of "best soil" feedback lines in Tera's review; green requires at least 2. Window: latest `questActiveEvent:41` (18:14:39) → latest `questFinishEvent:56` (18:25:56). No box was correct and no "best soil" line fired. Reason code `WRONG_SOIL_SELECTED`, `wrong_box_number = 3`, `wrong_box_summary` = "the first box (chose Clay, needs Gravel) and the second box (chose Gravel, needs Sand) and the third box (chose Sand, needs Clay)".

**Performance summary:**
Tera asked the player to point a camera at the soil that would grow each seedling best given its water needs. The player put the peas (very little water) on clay, the potatoes (moderate water) on gravel, and the broccoli (a lot of water) on sand; none was right. Under the rubric this earns 0 of 3 points.

**Gameplay evidence:**
- Tera's prompts: peas "only need a very small amount of water" (18:15:16); potatoes "need a moderate amount of water" (18:16:01); broccoli "need a TON of water" (18:16:20). DANI's hint at 18:15:25: "Each of the soils Tera is testing has a different particle size. The seedling planted in the soil that holds the right amount of water will likely grow best."
- Placements: box 0 Clay at 18:15:51, box 1 Gravel at 18:16:14, box 2 Sand at 18:16:56 — 13 to 36 seconds after each prompt.
- Review (18:17:04, "I'm all set. Let's see the results."): peas → "This plant got more water than it required. The small soil particles will trap water and hold too much of it near its roots."; potatoes → "This plant did not get enough water. The water is expected to pass through the soil particles too easily..."; broccoli → the same "did not get enough water" line; then "You placed cameras to record seedlings in soil that did not suit their water needs."

**Possible learning need:**
This point targets matching plant water needs to soil retention and drainage. The least-thirsty plant went to the most water-retaining soil and the thirstiest plant to a fast-draining soil — the exact reverse of the intended matching — and the moderate plant to the fastest-draining soil, which may indicate the player reversed the link between particle size and water retention. This is an interpretation.

**Potentially underused support:**
DANI's particle-size hint was delivered before the first placement; the logs cannot show whether the player revisited it or the earlier soil descriptions through the chat history (none logged). When Tera asked "Do you need to move any cameras?", the player answered "I'm all set" without adjusting; the review comes only after all three placements, and no re-placement was logged.

**Suggested instructor intervention:**
Ask the student to order gravel, sand and clay by how much water they hold and why (particle size and pore space), then to match the three seedlings to soils, explaining each match. Compare with their in-game choices and the feedback Tera gave.

**Dashboard pop-up text:**
The player placed none of the three cameras on a suitable soil, so the score is 0 of 3 and the point is yellow (green requires at least two). The peas, which need very little water, were placed on clay; the potatoes, which need a moderate amount, on gravel; and the broccoli, which needs a lot, on sand; Tera's review reported too much water for the peas and too little for the other two. The two extreme cases are exact reversals of the intended matching, which may indicate the link between soil particle size and water retention was reversed. Consider asking the student to rank the three soils by how much water they hold and to explain why, then re-match the seedlings.

---

## Unit 5, Progress Point 1: If I Had a Nickel – Floors 1 & 2

**Yellow-result trigger:**
Green requires the success node (`100:44`) with none of `100:38`, `100:39` or `100:43` in the window (latest `questActiveEvent:43`, 18:29:20 → latest `questFinishEvent:43`, 18:36:44). `100:39` fired. Reason code `SOLVED_WITH_ASSIST`, `attempt_number = 4` (green requires an independent solution within four attempts).

**Performance summary:**
In the evaporation glyph puzzle (matching tablets that show evaporation rates to wall images of temperatures at different times of day) the player submitted four incorrect arrangements in 1 minute 43 seconds, accepted DANI's offer of help seven seconds after it appeared, and DANI ordered the tablets. Under the rubric this earns 0 of 2 points.

**Gameplay evidence:**
- The player accepted Dr. Toppo's Unit 5 lesson at the start of the floor ("Start Toppo Lesson?" → "Yes", 18:29:55–18:30:00); the follow-on node fired at 18:31:57, about two minutes later, consistent with the lesson running.
- Tablets picked up at 18:32:16–18:32:18; wrong-order feedback at 18:32:23 (`100:34`), 18:32:44 (`100:35`: "The tablets you can move appear to have something to do with evaporation rate."), 18:33:31 (`100:37`: "The images on the wall appear to depict temperatures at different times of day. Try matching them with the evaporation rate you might expect to see in those conditions."), 18:34:06 (`100:39`: "Would you like me to assist, TK?").
- 18:34:13 "Sure, I'm stuck." → 18:34:14 "I believe I have calculated the correct order for the puzzle. Activating holid projector."; completion lines at 18:34:20 and 18:34:34.
- Submissions were 21–46 seconds apart.

**Possible learning need:**
This point targets the relationship between temperature and evaporation rate (higher temperature, faster evaporation). A further wrong order after DANI's hint that named the relationship may indicate difficulty reading the temperature cues in the wall images or ordering the evaporation rates shown on the tablets. This is an interpretation.

**Potentially underused support:**
The Toppo lesson was started (logged); whether it was watched to the end is not logged, though the two-minute gap before the next node is consistent with it. DANI's hints escalated as designed, and the assist was accepted at the first offer; the logs cannot show whether the player compared the tablets with one another before each submission.

**Suggested instructor intervention:**
Show three temperature conditions (a cool morning, a warm afternoon, a hot midday) and ask the student to rank the expected evaporation rate and explain why in terms of the energy given to water molecules. Follow with a short image-matching exercise.

**Dashboard pop-up text:**
The player did not solve the evaporation glyph puzzle independently: four arrangements were wrong within about 100 seconds, and after the fourth the player accepted DANI's offer to order the tablets, so the point is yellow (green requires an independent solution within four attempts). The player had started Dr. Toppo's Unit 5 lesson two minutes earlier, and DANI's third hint spelled out the relationship — wall images show temperatures at different times of day, tablets show evaporation rates — yet the next arrangement was still wrong. This may indicate difficulty connecting higher temperature with faster evaporation when reading the images. Consider asking the student to rank a few temperature conditions by expected evaporation rate and to explain the reasoning.

---

## Unit 5, Progress Point 2: If I Had a Nickel – Floors 3 & 4

**Yellow-result trigger:**
Score: floor 3 with at most 6 condenser/evaporator interactions earns 2 (7–10 earns 1); floor 4 with at most 5 earns 2 (6–9 earns 1); green requires at least 3. Window: latest `questFinishEvent:43` (18:36:44) → latest `DialogueNodeEvent:96:1` (18:46:07). Floor 3 had 8 counted interactions and floor 4 had 10, so the score is 1 + 0 = 1. Reason code `SCORE_BELOW_THRESHOLD`, `floor3_attempts = 8`, `floor4_attempts = 10`.

**Performance summary:**
On floor 3 the player used eight counted condenser/evaporator interactions (plus thirteen dual-chamber toggles in room 2 that the current script does not count) and on floor 4 ten interactions, against optimal counts of six and five. Both floors were completed. Under the rubric this earns 1 of 4 points.

**Gameplay evidence:**
- Floor 3 (18:39:17–18:42:47): vent switch and condenser on in room 1 (18:39:40–18:39:51); in room 2 the paired dual-chamber evaporator and condenser were switched on and off thirteen times in 41 seconds (18:40:11–18:40:52) before the room's condenser was switched on (18:40:55); in room 4 condenser one was turned off, condenser two on, then condenser one on, off, on, off (six interactions in 56 seconds, 18:41:40–18:42:36).
- Floor 4 (18:42:47–18:45:25): room 1 condenser on (18:43:36); room 2 condenser on, evaporator on, condenser off, evaporator off, condenser on, evaporator on (six interactions in 14 seconds, 18:44:12–18:44:26); room 3 evaporator on, condenser on, vent switch, evaporator off (18:44:34–18:44:57).
- A chat-history close was logged at 18:45:51, after floor 4 was completed (the open is not logged). No debug menu was used.

**Possible learning need:**
This point targets evaporation and condensation as complementary processes and predicting each machine's effect. Rapid on/off toggling of paired machines, and of a condenser and evaporator together in room 2 of floor 4, may indicate trial and error rather than predicting which phase change a chamber needs. This is an interpretation.

**Potentially underused support:**
Floors 1 and 2 provided practice with the machines; a chat-history window was closed after floor 4, which suggests the player looked back at earlier instructions at some point, though the timing of the open is unknown. Each machine change gives immediate visual feedback, and the one- to three-second toggles leave little time to observe the effect.

**Suggested instructor intervention:**
Ask the student to explain what an evaporator and a condenser each do to water (liquid to vapor; vapor to liquid) and, for a given chamber goal, to predict which machine to turn on before testing. A predict-then-test routine targets the toggling pattern directly.

**Dashboard pop-up text:**
The player completed floors 3 and 4 of the water-chamber puzzles, but with eight counted condenser/evaporator interactions on floor 3 (optimal six) and ten on floor 4 (optimal five), so the score is 1 of 4 and the point is yellow. On floor 3 the paired dual-chamber machines were switched on and off 13 times in 41 seconds, and on floor 4 a condenser and an evaporator were toggled six times in 14 seconds, which may indicate trial-and-error switching rather than predicting whether a chamber needs evaporation or condensation. Consider asking the student to explain what each machine does to water and to predict the needed machine before testing.

---

## Unit 5, Progress Point 3: What Happened Here?

**Yellow-result trigger:**
The point is yellow when four or more flagged-submission nodes (39 conversation-108 keys since the 2026-09-17 key-list review, 33 before it) fire in the window (latest `DialogueNodeEvent:96:1`, 18:46:07 → latest `questFinishEvent:44`, 18:53:30); no success node is required. Six fired. Reason code `EXCESS_ATTEMPTS`, `wrong_argument_number = 6`, `claim_wrong_number = 4`, `reasoning_wrong_number = 1`, `evidence_wrong_number = 1`.

**Performance summary:**
After examining the evidence in Aryn's water factory (animal tracks, hygrometer, thermometer and storage pool, 18:48:40–18:50:16), the player submitted seven arguments in 1 minute 50 seconds (18:51:24–18:53:14); six were flagged — four for the claim, one for the reasoning, one for incomplete evidence — and the seventh (evidence `C,D`, reasoning `3`, claim `II`) was accepted. Under the rubric a correct argument after more than five attempts earns 0 of 3 points.

**Gameplay evidence:**
- The player declined the pre-argument review ("I think I'm good", 18:50:52); the session opened at 18:51:12.
- Four submissions with claim `I` in 50 seconds (18:51:24–18:52:14): `A,B,1,I`, `A,B,2,I`, `A,B,3,I`, `A,B,4,I` — each flagged "You are restating Aryn's claim. Since we collected evidence that water disappeared for natural reasons, try building an argument that doesn't align with what Aryn says"; only the reasoning changed between them.
- Both backing-information panels (Evaporation Flow Diagram, Heat Added/Released Chart) were opened at 18:51:35–18:51:36, after the first flag (closes not logged).
- With claim `II`: `C,4,II` 18:52:48 → "Your argument is very close to ideal, but your reasoning should connect all of your pieces of evidence with your claim" (node `108:65`, a reasoning flag); `C,3,II` 18:52:59 → "Your reasoning and claim make sense. But your argument could use another piece of evidence" (node `108:64`, an evidence flag); `C,D,3,II` at 18:53:14 was accepted (Aryn: "Did anyone ever tell you you're pretty persuasive, TK?"). Nodes `1` and `3` were hovered for 2–4 seconds before the switch. The "best argument possible" node did not fire; the quest completed.
- The two post-switch flags sit on the "one correct piece of evidence" branch of conversation 108, which was outside the color rule's key list until the 2026-09-17 review added that branch; this run is what exposed the gap.

**Possible learning need:**
This point targets arguing that the water evaporated, supported by the temperature and humidity evidence together. Four submissions restating Aryn's claim while only the reasoning changed may indicate the player did not recognise which claim was Aryn's and which was the natural-cause claim DANI proposed; once the claim was switched, two refinements (reasoning, then a second piece of evidence) reached the accepted argument, so the evidence selection appears to be the smaller difficulty. These are interpretations.

**Potentially underused support:**
Both backing-information panels were opened after the first flag (logged), unlike the previous run. DANI's explanations while collecting evidence (humidity rising from 10%, temperature rising all week) were delivered; the logs cannot show whether the player linked them to the argument. The pre-argument review with DANI was declined.

**Suggested instructor intervention:**
Ask the student to state the two competing claims in their own words — Aryn's (the Hegonians took the water) and DANI's (it disappeared naturally) — and what happened to the water; then have them pick, from the collected observations, the two measurements that show the water turned into vapor (temperature up, humidity up) and explain why the tracks and the salt do not.

**Dashboard pop-up text:**
The player completed the argument about Aryn's disappearing water, but six submissions were flagged (green allows fewer than four), so the point is yellow. The first four submissions, made in 50 seconds, all restated Aryn's claim while only the reasoning was changed; after switching claims, one submission was flagged for reasoning that did not connect the evidence and one for a missing second piece of evidence, and the argument was accepted on the seventh submission. Both backing-information panels were opened after the first flag. This may indicate difficulty recognising which claim was Aryn's and which was the natural explanation DANI proposed. Consider asking the student to state the two competing claims in their own words and to pick, from the collected observations, the two that show the water turned into vapor.

---

## Unit 5, Progress Point 4: Water Problems Require Water Solutions

**Yellow-result trigger:**
Green requires the maximum-water outcome (`DialogueNodeEvent:106:35`) and no failure outcome in the window (previous `questFinishEvent:44`, 18:53:30 → latest `questFinishEvent:45`, 18:59:25). The only run produced the sunlight-blocked failure (`106:25`). Reason code `WRONG_SETTINGS_SELECTED`, `wrong_run_number = 1`, `failure_phrase` = "the settings blocked sunlight, so the salt water could not heat up and evaporate".

**Performance summary:**
In the solar desalinator design task the player selected a tilted roof, an extra covering and a hot glass roof — the covering and the hot glass differ from the working design (tilted roof, no extra covering, cold glass) — within three seconds and submitted once. Under the rubric this earns 0 of 1.5 points.

**Gameplay evidence:**
- DANI started Dr. Toppo's desalinator video at 18:55:42 ("I have found a video on desalinators in Captain Toppo's survival series archive... Playing it for you now."); the design panel was opened at 18:58:12, two and a half minutes later.
- Selections: RoofStyle "Tilted In" 18:58:15, ExtraCovering "Covered" 18:58:16, GlassRoofTemperature "Hot" 18:58:17; submitted 18:58:18.
- Outcome `106:25`: "Looks like we didn't collect any water. Unfortunately, your settings did not allow for sunlight to enter the solar desalinator. Without sunlight, the salt water..." No second run was made; the quest closed at 18:59:25.

**Possible learning need:**
This point targets applying evaporation and condensation to a design: sunlight must reach the water (no covering), the glass must stay cool for condensation, and a sloped roof directs condensed water to the collector. The roof choice was right, but the covering and the hot glass contradict the first two steps, which may indicate the player had not linked those two features to evaporation and condensation. This is an interpretation; the three-second selection time is consistent with, but does not prove, choices made without weighing them.

**Potentially underused support:**
The video played for about two and a half minutes before the design panel was opened, so it may have been watched; the logs cannot confirm this. Conversations with Aryn, Toppo and Anderson and the chat history were available (no chat use was logged in the window). Dr. Toppo's outcome feedback explains the failure; only one run was made.

**Suggested instructor intervention:**
Ask the student to narrate the water's path in the still: sunlight heats the salt water, vapor rises, vapor condenses on a cool surface, droplets run down a slope into the collector. Then ask which setting supports each step and why a covered still with a hot roof produced no water even though the roof was tilted correctly.

**Dashboard pop-up text:**
The player's solar desalinator design produced no water: a tilted roof, an extra covering and a hot glass roof were selected within three seconds and submitted once, and Dr. Toppo's feedback explained that the covering blocked the sunlight needed for evaporation, so the point is yellow (green requires the maximum-water design with no failed runs). Two of the three choices differ from the working design — no covering and a cold glass roof. Dr. Toppo's desalinator video had been playing for about two and a half minutes before the design panel was opened, so it may have been watched. This may indicate the player had not linked the covering and glass temperature to evaporation and condensation. Consider asking the student to trace the water's path through the still and name the setting that supports each step.

---

## Verification and Documentation Notes

1. **Colors and reason codes verified.** `rubric-validation/run_all.py --fixture 09-14-26-3` reproduces all 26 expected colors, and `reason-code-validation/run_all.py --fixture 09-14-26-3` reproduces the 23 triggered codes and every variable quoted above. This log was the first to take the *accepted*-assist path in the U2P1 and U4P2 glyph puzzles; the reason-code scripts previously recognised only DANI's forced assist, so on 2026-09-16 the accepted-path nodes (`68:24`/`68:26`/`68:32`/`68:34` and `102:20`/`102:21`) were added to both markdown scripts and their transcriptions, after which the fixture passes 26/26.
2. **Evidence extraction.** Attempt windows were reproduced with the `attempt_window()` functions of the reason-code modules; for points whose grading window has no earlier trigger and therefore starts at the beginning of the log (U1P3, U2P1, U2P4, U2P5, U2P7, U3P1, U3P2, U3P3, U3P5, U4P3, U4P5), the narrative evidence was taken from the activity segment bounded by the documented start marker or the first node of the graded conversation. Records were ordered by client timestamp. Dialogue wording is quoted from `grading-logic/original-score-rubric-table-and-dialogue-database/Dialogue-ID-Texts.xlsx` (export of 2026-06-10; the accepted-assist nodes `102:20`/`102:21` have no text in that export).
3. **Rubric versus dashboard thresholds (reported, not resolved).** Where a rubric-point statement is made above it follows the files in `assessment-score-rubric-for-each-pp/`; the yellow trigger follows the grading code. The two differ in several places relevant to this player: the U2P3 rubric scores waypoint accuracy and time-to-find (Tera within 5 minutes, Aryn within 3) while the dashboard counts reminders; the U3P4 rubric gives 0 points from the third attempt while the dashboard stays green through three attempts; the U4P2 and U5P1 rubrics give 0 points from the third and fourth attempt respectively while the dashboard stays green one attempt longer; the U3P5 rubric's on-track band is 3–4 points while the dashboard turns green at 2.5; the U4P5 backing-information bonus in the rubric is not applied by the dashboard; the U5P4 rubric maximum is 1.5 points while the progress-point specification lists on-track as 2; the U3P3 color script counts the success node in its total, which makes its bands equal to total attempts and matches the rubric's attempt bands; and the U4P4 rubric describes the fifth-floor canister solutions inconsistently while the dashboard counts canister changes.
4. **Argument node labels are not documented in the repository.** Submissions are quoted by their logged labels. Where a role is stated (for example that `B` was waterfall height in U2P7, or that claim `I` was Aryn's claim in U5P3), it is inferred from the feedback node that fired for that submission and is labelled as such.
5. **Resource-use statements are log-grounded.** Panel openings (`argumentationToolEvent`), map openings and waypoints (`TopographicMapEvent`), dialogue choices such as declining the topographic-map video (U2P2), accepting the lesson replays (U2P1, U2P4) and the Toppo lesson (U5P1), and puzzle interactions come directly from the log. Absences stated definitively are also log-grounded: no tool events in the U2P7 and U4P5 sessions, no map events in the U3P2 sensor task, no map opening after 01:42:26 and no waypoint event in the Aryn search (U2P3), no map check before the third crate (U3P1). Chat-history use is only partly observable: the log records one `chatEvent` "Close" at 18:45:51 but no open events. Panel close events are logged for the U1P3 session only, so panel durations are not stated elsewhere.
6. **Tester artifacts.** The debug menu was never opened (the 13 `DEBUGMenu` records are `isOpened = false` emissions on scene loads); no `crash` records exist. `questActiveEvent:18` and `questActiveEvent:36` were re-emitted on scene changes, extending the U3P4 and U4P4 windows by dialogue-only stretches, and `questFinishEvent:45` was logged twice back-to-back; none affects a graded count. The `version` field reads `20260914-` on every record (build number missing).
7. **Known grading-logic items visible in this log.** U5P2's thirteen dual-chamber interactions on floor 3 are not counted by the current script (flagged in the grading file); U5P3's two "close" feedback nodes (`108:64`, `108:65`) were outside the color rule's key list when this run was first audited and were added, with their four sibling nodes, on 2026-09-17 (the count for this run rose from 4 to 6, color unchanged); the U2P2 grading file is titled "Foraged Forging" but grades the Finding-Toppo navigation, and its rubric file describes waypoint placement while the code counts reminders (carried over from the earlier examples); the U3P4 rubric file's implementation note about the two-versus-three-attempt threshold remains open.
