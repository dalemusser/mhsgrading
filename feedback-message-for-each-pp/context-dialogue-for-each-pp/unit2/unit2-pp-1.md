Beginning of UNIT 2

[Cutscene] Player Exits Pod:
INT. ESCAPE POD
Cadet’s vision slowly fades in on the DESTROYED interior of the escape pod. Virtually everything is now broken, including the main view screen. Wires and instrument clusters hang loose and sparking. A small fire burns behind a dislodged panel.
{Animation (Dev): The camera fades in blurry, then slowly clears up}
{Animation (Dev): Ambient sparks occasionally fly from broken wires}
{Animation (Art): A small fire flickers behind a broken panel}

##### AUTOMATED SYSTEM [conversation, automatic]
###### Warning! Fire detected.
###### Fire suppression systems–offline.
###### For your safety, please exit the escape pod immediately.

{Animation (Art): The Player exits the pod}

[/Cutscene]
# Part 1: Welcome to WAT247
## Task 1.1 - Rise from the Wreckage
EXT. ALIEN RUINS
{Audio: Crash Site (Ruin) BGM plays. Ambient sparking SFX play from the crashed pod}
The Player steps foot into a dark, nearly pitch-black room. The only light is coming from the door of the pod.

[Note: The player can move around the area normally. Monologues are time-triggered events.]

(Hard cut from Cutscene to gameplay beginning.)

When the player exits the pod…
#####
##### PLAYER [choices, automatic, roaming]
| Where am I? | Hey, who turned out the lights? |
| :---- | :---- |

15 seconds after the prior conversation ends…
##### PLAYER [choices, automatic, roaming]
| All right, focus, let’s see what we can find. | Great, now I’m talking to myself. |
| :---- | :---- |

15 seconds after the prior conversation ends…

##### PLAYER [choices, automatic, roaming]
| Okay, I’m going to investigate that panel. | Mysterious green dust? Count me in! |
| :---- | :---- |

{Waypoint: Nanomachine panel}

When the player approaches the panel...
##### PLAYER [choices, automatic]
| Let’s figure out how this works. | Let’s break this thing! |
| :---- | :---- |
######
#####
{Input: Press [E/Action button] to activate the panel}

{Mini Game: Nanomachine Puzzle 1}

[Cutscene begins immediately following the mini game]

##### [Cutscene] Nanos Swirling Player

Even more green dust issues from the panel and begins to swirl around the Player’s holo-watch, which begins to glow in kind,
{Animation (Art): Green, dust-like nanomachine particles swirl around the holo-watch, which glows green to match}

The bizarre architecture lights up with pulsing alien glyphs and illuminates the room. The Player looks around quickly, lingering briefly on some key elements the player will need to explore in a moment, including an open 6-sided door.
{Animation (Art): Alien glyphs light up in pulses, illuminating the room}

As the Player turns back, the dust around the watch begins to spiral, as if spinning down a drain, into the holo-watch.The dust vanishes, entirely swallowed into the holo-watch, with a rush. The watch SPARKS, shakes violently, and a green band is added to the upper band of the watch.
{Animation (Art): The nanomachine particles drain into the holo-watch}
{Animation (Art): Player holds their arm to stabilize it as the watch shakes and sparks}
{Animation (Art): A band on the upper section of the watch lights up green}

The watch finally appears to settle down and reboot. The familiar bootup screen returns and resolves to home.

DANI glitches and pops in and out of existence, then finally reappears in a degraded, 8-bit form.

[/Cutscene]
#####

##### PLAYER [choices]
| What, is my watch glowing? | Ugh, that’s kinda gross. |
| :---- | :---- |



{Animation (Dev): Door unlocks and opens. Door emissive texture should change color to reflect the unlocked state}

{Audio: Rumbling SFX accompany the opening door}

##### DANI [Dialogue, conversation, automatic]
###### C-c-c-communication sys-systems are re-restoring. I am… active. Thank you, TK.

##### PLAYER [choices]
| I’m glad you’re back, DANI! | What just happened? |
| :---- | :---- |

##### DANI [conversation]
###### The dust that entered the holo-watch appears to have been a swarm of nanomachines. They have partially reconstructed my neural matrix.

##### PLAYER [choices]
| Whoa, were they experimental tech from the ship? | Those were alien nanomachines, right? |
| :---- | :---- |

##### DANI [conversation]
###### The nanomachines were not Earth technology. Conjecture: whoever created this structure was most probably also the creator of the swarm.
#####
##### PLAYER [choices]
| What is this structure? | Can we find out who those creators were? |
| :---- | :---- |

##### DANI [End dialogue, conversation]
###### I do not have additional information at this time. Perhaps if we continue exploring we may locate both the answers to your questions and the exit.
#####

{Mission: Escape the Ruin assigned}
{Quest Tracker: “Escape the Ruin: Check the next room.”}
{Waypoint: Open door to the next room}

Player walks through door.

INT. POWERCUBE ROOM
The small square room, approximately 5 meters each side, is hushed and dark. The otherwise smooth walls are etched with a thick, circuit-board like pattern that travels up the walls and continues across the ceiling. A geometric mass (waist height pedestal with the power cube, though that’s not currently clear in the player’s view in the darkness), stands in the center of the room.

#####
{Animation (Dev): Door closes and locks behind the player after they enter. Door emissive texture reverts to its locked color.}
{Audio: Rumbling SFX accompany the door closing}
{Mission: Escape the Ruin updated}

##### PLAYER [choices, automatic]
| DANI, what’s going on? | Great, now we’re trapped! |
| :---- | :---- |
#####
##### [Cutscene]
##### DANI [conversation]
###### One moment, TK. Allow me to test a hypothesis.
#####



{Animation (Art): DANI appears to strain, fuzzing out to static, before popping back to 8-bit normal.}
##### [/Cutscene]

{Animation (Art): The powercube in the center of the room is illuminated by a gentle, green glow. It rotates gently, ethereal green light pulsating through circuit-like lines running across and through it.}


#####
##### PLAYER [choices]
| I didn’t know you could do that! | So, now you’re infected by aliens? |
| :---- | :---- |

##### DANI [conversation]
###### I only know I am now able to interact with these devices in a limited capacity. They appear to be miniaturized power sources–similar to powerful batteries. They may prove useful.

##### PLAYER [End dialogue, choices]
| Got it. We can figure this out. | Whatever, let’s grab that glowing alien thing. |
| :---- | :---- |

[Note: All feedback dialogue happens automatically when its conditions are met]
| FEEDBACK |  |
| :---- | :---- |
| (If P doesn’t pick up powercube for 30 seconds) DANI [gameplay, roaming] What do you believe this cube is for? | (If P doesn’t pick up powercube for 60 seconds) DANI [gameplay, roaming] We should examine the cube. {Quest Tracker: “Escape the Ruin: Examine the cube.”} {Waypoint: Powercube} |
#####
{Input: Press [E/Action button] to pick up the powercube}

{Animation (Art): Player bends down to pick up the cube.}

{Animation (Dev): Two small circles on the nearby power pad begin to glow green, matching the glow of the cube}

| FEEDBACK |  |
| :---- | :---- |
| (If P doesn’t set the cube on the pad for 30 seconds) DANI [gameplay, roaming] Perhaps this cube is intended to be placed in a specific location. | (If P doesn’t set the cube on the pad for 60 seconds) DANI [gameplay, roaming] Those glowing spots on the floor seem to align with the cube. {Quest Tracker: “Escape the Ruin: Perhaps the cube should go on the pad?”} {Waypoint: Power pad} |

{Input: Press [E/Action button] to put down the powercube]


{Animation (Art): The player sets down the powercube and their hands drop to their sides.}
{Audio: Powercube landing SFX play whenever the player drops the cube.}


When the player places the cube on the pad…
{Audio: Congratulatory powering on SFX play}
{Animation (Dev): The hexagonal door on the back wall opens. Its emissive texture changes color to its unlocked state}
{Audio: Rumbling SFX plays to match the door opening}
##### DANI [Sequence, gameplay, automatic]
###### Placing the power cube onto the pad powered the door control mechanism and opened the door.

##### PLAYER [End sequence, choices]
| Let’s keep moving. | Yeah, yeah, let’s get to more alien stuff! |
| :---- | :---- |

Player moves into the next room.

INT. THIRD ROOM
The third room contains another nanomachine panel.

When the player approaches it…

##### DANI [Sequence, conversation, automatic]
###### This device likely contains another nanomachine swarm.

##### PLAYER [sequence, choices]
| Let’s approach with caution. | Sweet! MORE ALIENS! |
| :---- | :---- |

{Input: Press [E/Action button] to activate the panel}
{Mini Game: Nanomachine Panel 2}

[Cutscene] Nanos Changing DANI  (begins immediately after the mini game)

Green dust again pours from the panel.
{Animation (Art): Nanomachine particles pour from the panel}

DANI flickers to static.
{Animation (Art): DANI’s avatar glitches and fizzles out}

The holo-watch sparks, pulses, adds a new color band! After it settles, it reboots with a familiar sound, and DANI reappears with a plain, chunky, low-res 3D model (think Nintendo 64 graphics).
{Animation (Art): The player watches, more at ease than before, as the watch pulses and another band lights up}

[/Cutscene]

##### DANI [Dialogue, gameplay]
###### TK, I am back. The nanomachines appear to have performed further repairs, and my map functionality has returned. Please help me verify its integrity.

DANI menu opens automatically.

[Map tutorial]

{Animation (Dev): A highlight blinks on and off at the map button until player clicks it}
{Input: [Press E/Action button or Click] to open the map}
[Note: Use the fog of war map depicted on slide 5 of this slideshow]

##### DANI [gameplay]
###### This is the map. Our location is highlighted here.

{Animation (Dev): A highlight blinks on and off at the player map icon}

##### DANI [curricular]
###### As this is a topographic map, the legend indicates elevation.

{Animation (Dev): A highlight blinks on and off at the map legend}
#####
##### DANI [gameplay]
###### I will continue to update the map as more information becomes available.
#####
##### DANI [gameplay]
###### Thank you, TK. My map functionality appears fully operational.

{Animation (Dev): A highlight blinks on and off at the close map button until the player closes the map}

[End map tutorial]
######
##### DANI [conversation, automatic]
###### TK, these nanomachine swarms seem to be both repairing me and upgrading my abilities in unexpected ways. If we want to survive what challenges WAT247 poses, we should try to find and open more of them.

##### PLAYER [choices]
| Agreed. We’ll look out for more nanomachines. | I’ll help repair you, but I’m on the fence about these upgrades. |
| :---- | :---- |
#####
##### DANI [conversation]
| Thank you, TK. | I understand. Please know that whatever upgrades the nanomachines add to the holo-watch will be used to help the crew through this crisis. |
| :---- | :---- |

{Request: The Measure of a Mutt assigned}
[Note: Requests do not track on assignment, but become visible in the Objectives menu. DANI and Jasper’s requests, The Measure of a Mutt and Secrets of the Lost Society, respectively, are required as part of the main gameplay path. Thus, they have no objectives off of this main path.]
######
##### DANI [End dialogue, conversation, automatic]
###### Let’s continue to the next room.

INT. FOURTH ROOM
A locked door rests imposingly in the far wall. Six incomplete symbols, three set into each side wall, connect to it by dark trails running across the walls and floor. In the center of the floor, there is a hexagonal depression. Scattered about the room are six tiles with more incomplete symbols engraved on them.

##### DANI [conversation, automatic]
###### I do not seem to have access to the door controls in this room—I recommend investigating to find a way forward.

{Input: Press [E/Action button] to pick up a glyph tile}
{Animation (Art): Player bends down to pick up the tile (general animation)}
At any of the incomplete wall symbols…
{Input: Press [E/Action button] to place tile into wall}
{Animation (Art): Player reaches out and sets the tile into the wall}

| FEEDBACK |  |  |  |
| :---- | :---- | :---- | :---- |
| (If P doesn’t interact with the pieces around the room for 15 seconds) DANI [gameplay, roaming] I believe the stone pieces on the floor may fit into the wall panels. | (If P doesn’t interact with the pieces around the room for 30 seconds) DANI [gameplay, roaming] Perhaps you could attempt to place one of those pieces on the floor into a wall panel. | (If P doesn’t interact with the pieces around the room for 60 seconds) DANI [gameplay, roaming] Hey TK, place one of the pieces on the floor into a wall panel. We will observe what follows. |  |
| Once all six tiles are placed, they are checked simultaneously: |  |  |  |
| (If the tile is in the correct place) {Audio: Congratulatory jingle plays} {Animation (Dev): Panel glows green} | (If the tile is in an incorrect place) {Audio: Negative jingle plays} {Animation (Dev): Tile falls to the floor} |  |  |
| Feedback - First Attempt |  |  |  |
| (If P placed 2-3 incorrect tiles) DANI [gameplay] It appears that some pieces are in the correct location, but several still need to be rearranged. TK, I recommend continuing to work out the correct pattern. | (If P placed > 3 incorrect tiles) DANI [curricular] I believe we may need to reevaluate our approach. My optical sensors detect patterns on these pieces that resemble topographic maps. TK, what do you think? |  |  |
|  | Choice: Topographic map? DANI [curricular] Topographic maps have contour lines that show elevation changes across terrain. Contour lines that are close together on a topographic map show steep slopes, and contour lines that are far apart show gentle slopes. | Choice: Yeah, they actually do. |  |
| Feedback - Second Attempt |  |  |  |
| (If P placed 2-3 incorrect tiles) DANI [curricular] Several pieces are still not in the correct location. TK, have you tried matching the topographic map image to the corresponding landscape shape? | (If P placed > 3 incorrect tiles) DANI [curricular] I believe the aliens may have been attempting to demonstrate the connection between landscape features and topographic maps with this room. Try matching the topographic map image to the corresponding landscape shape. |  |  |
| Choice: Match them? DANI [curricular] I believe the pieces that have silhouettes of landscapes correspond with the topographic map images. Match them by using what you know about reading topographic maps. The closer the contour lines, the steeper the slope. | Choice: Got it. Thanks! | Choice: Match them? DANI [curricular] The pieces that have silhouettes of landscapes correspond with the topographic map images. Match them by using what you know about reading topographic maps.  Where you see lines close together there are steep slopes in the landscape. Where you see lines far apart there are gentler slopes. | Choice: Got it. Thanks! |
| Feedback - Third Attempt |  |  |  |
| (If P placed 2-3 incorrect tiles) DANI [gameplay] Your logic is working. I believe you are getting closer to the solution, TK. Keep trying. | (If P placed > 3 incorrect tiles) DANI [curricular] Several pieces appear to be in the incorrect location. TK, may we watch Toppo’s lesson again? |  |  |
|  | Choice: Sure. That might help. DANI [curricular] Streaming the video to your holo-watch. Topography lesson from U1 plays | Choice: Nah, I don’t need to. |  |
| Feedback - Fourth Attempt |  |  |  |
| (If P placed 2-3 incorrect tiles) DANI [gameplay] That is very close, TK. I believe you can solve it. | (If P placed > 3 incorrect tiles) DANI [gameplay] Would you like me to assist, TK? |  |  |
|  | Choice: Sure. I’m stuck. DANI [gameplay] Moving the pieces now. {Animation: Pieces fly to the correct locations} [Note: Jump to puzzle solved - DANI helped] | Choice: No, I’m okay. |  |
| Feedback - Fifth Attempt |  |  |  |
| (If P placed 2-3 incorrect tiles) DANI [gameplay] Would you like me to assist, TK? | (If P placed > 3 incorrect tiles) DANI [gameplay] I believe I have ascertained the key to this puzzle. Allow me to assist, TK… there. {Animation (Dev): Pieces fly to the correct locations} [Note: Jump to puzzle solved - DANI helped] |  |  |
| Choice: Sure. I’m stuck. DANI [gameplay] Moving the pieces now. {Animation (Dev): Pieces fly to the correct locations} [Note: Jump to puzzle solved - DANI helped] | Choice: No, I’m okay. |  |  |
| Feedback - Sixth Attempt |  |  |  |
| (If P placed any incorrect tiles) DANI [gameplay] I believe I have ascertained the key to this puzzle. Allow me to assist, TK… there. {Animation: (Dev) Pieces fly to the correct locations} [Note: Jump to puzzle solved - DANI helped] |  |  |  |

After the glyph is solved…
{Audio: Congratulatory jingle plays. A quiet click SFX plays underneath it}
| (If P solved it on their own) DANI [gameplay] Well done, TK. Not everyone is capable of solving a puzzle left by an ancient alien civilization. It appears the designers have rewarded you for your efforts. | (If DANI helped) DANI [curricular] Whoever designed this ensured the contour lines on each map piece matched the corresponding terrain. Where contour lines are close together you can see the terrain is steep, but where the contour lines are spread out the terrain is less drastically sloped. This information will be vital as we navigate the unexplored surface of this planet. If you ever want to review this info you can watch Toppo’s video in the reference menu here. Topography lesson from U1 plays DANI [gameplay] We have finally solved this puzzle. TK, do you see what was left behind over there? |
| :---- | :---- |

A wedge-shaped tile is now present in the depression in the center of the room.

{Input: Press [E/Action button] to pick up the tile}
{Audio: Collectible acquired SFX plays}
{Animation (Dev): Door opens on the far wall. As before, its emissive texture changes color to its unlocked state}
{Audio: Rumbling SFX play along with the animation}

INT. FIFTH ROOM

{Animation (Art) In the center of the room, the Soil Key floats, gently spinning, over a pedestal.}

If the player doesn’t pick up the soil key for 30 seconds…
| DANI [gameplay] TK, what is that object in the center of the room? A key? Animation (Dev): Camera zooms to the soil key, lingers for a few seconds, then returns to the normal perspective |
| :---- |

When the player approaches the soil key…

##### DANI [conversation]
###### This key is ancient–centuries, possibly millennia old. Please handle it carefully.

{Input: Press [E/Action button] to pick up the key}

[Cutscene]

{Animation (Art): The Player slowly, gingerly reaches out to touch the soil key. The moment their finger grazes it, it immediately crumbles to dust.}

##### DANI [conversation]
###### I may have a solution.

{Animation (Art): DANI strains again, fuzzing to static, then popping back in. A small beam of light projects from the holo-watch, focusing and resolving into a hazy replica of the soil key, floating in the air. After a moment, it flickers out.}

[/Cutscene]

##### DANI [roaming]
###### This may take a moment… I am testing a new function provided by the alien technology we encountered. Please do not wait on my account.

When the player approaches the soil key panel beside the door…

##### DANI
###### The slot in this panel is a perfect fit for the key. Let me attempt another projection.

{Animation (Art): DANI projects the soil key hologram in the interface. The camera shifts to the usual angle for the soil key minigame. The puzzle is solved at the default position, so it automatically completes after a few seconds}
{Audio: Confirmation beep SFX plays}
{Animation (Art): The outer door of the temple slowly slides open}
{Audio: Grinding stone and crumbling dust SFX play}

##### DANI [conversation]
###### Interesting. I will hold onto this key projection for later. Future locks may not be so cooperative.

##### PLAYER [choices]
| Can we just go already? | Thanks. Let’s get out of here. |
| :---- | :---- |

Player exits the temple.

{Mission: Escape the Ruin completed}
