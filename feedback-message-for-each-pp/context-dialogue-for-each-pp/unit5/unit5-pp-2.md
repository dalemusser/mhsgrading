**{Mission: “If I Had a Nickel” updated}**  
**{Quest Tracker: “There’s another locked door in this room”}**  
**{Waypoint: None}**

**{IF PLAYER INTERACTS WITH MURAL}**

The mural symbolically depicts a Hegonian with liquid super-nutrient pouring from its right-hand to a healthy growing tree, and a swarm of nanomachines pouring from its left hand to a thriving biomechanical crocodile.

**\<Dialogue\>**

##### DANI

###### *We have found another Hegonian mural. There is an inscription.*

##### PLAYER

| What does the inscription say? | Let’s move on. |
| :---- | :---- |

##### DANI

| \[Translation\] Though we could not reverse time, we found a different path. We created the super-nutrient to help the plants of Praxis grow larger, better suited to the heat. For the animals, we developed nanomachines that would live symbiotically within their bodies, adapting them to survive with less water. | Understood. \<CLOSES TREE\> |
| :---- | :---- |

**\<End Dialogue\>**

##### 

| Timed Feedback |  |
| ----- | ----- |
| *If P doesn’t interact with the vent switch for 15 seconds…* DANI **\[automatic, gameplay\]** *This room appears different from the others.* | *If P doesn’t interact with the vent switch for 30 more seconds…* DANI **\[automatic, gameplay\]** *What is the function of that lever?* **{Mission: “If I Had a Nickel” updated} {Quest Tracker: “What does that lever do?”} {Waypoint: Vent switch}** |

**{Input: Press \[E/Action button\] to operate the switch}**  
**{Animation: The vent opens, allowing water vapor into the basin}**

##### 

| Timed Feedback |  |
| ----- | ----- |
| *If P doesn’t interact with the control panel for 15 seconds…* DANI **\[automatic, gameplay\]** *Opening the vent filled the basin with water vapor.* | *If P doesn’t interact with the control panel for 30 more seconds…* DANI **\[automatic, gameplay\]** *Now that there is water inside the basin, the control panel might do what we need.* **{Mission: “If I Had a Nickel” updated} {Quest Tracker: “Activate the device.”} {Waypoint: Control panel}** |

**{Input: Press \[E/Action button\] to activate the condenser control panel}**  
**{Animation (Art): Water droplets form on the inside walls of the basin, then trickle down into the rising water}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): The water level in the basin rises slightly, and the power cube floats out into the canal, within reach}**  
**{Input: Press \[E/Action button\] to pick up the cube}**  
**{Input: Press \[E/Action button\] to place the cube on the pedestal}**  
**{Animation (Dev): The door opens}**  
**{Audio: Rumbling SFX play along with the animation}**

**{Mission: “If I Had a Nickel” updated}**  
**{Quest Tracker: “Let’s keep moving.”}**  
**{Waypoint: Newly opened door}**

**INT. ISLAND RUINS \- FLOOR 3, ROOM 2**  
This room is larger than the others, with two condenser basins in the center connected by a pipe. The basin on the right is already active, about half full of water, and contains an inactive evaporator apparatus. The other has a power cube inside and a canal leading out from it. There are control panels next to each of the basins. The wall adjacent to the entry door contains a locked door with a power cube pedestal nearby.  
***\[Note: This room’s right control panel will need to support two separate interaction zones: one to turn on/off the condenser, one to do the same for the evaporator.\]***  
**{Animation (Art): Extremely slow condensation in the right basin}**

##### 

| Timed Feedback |  |
| ----- | ----- |
| *If P doesn’t interact with the control panels for 15 seconds…* DANI **\[automatic, gameplay\]** *We need to get that power cube out of the basin to move forward.* | *If P doesn’t interact with the control panel for 30 more seconds…* DANI **\[automatic, gameplay\]** *Based on our experience so far, how can we get water into that basin to carry the power cube out?* **{Mission: “If I Had a Nickel” updated} {Quest Tracker: “We need to get water into the basin with the power cube.”} {Waypoint: None}** |
| ***\[Note: 30 seconds after the second set of feedback, the quest state should silently advance to one with the same tracker text and a waypoint on the next step. This repeats as follows when they complete each step.\]*** **{Waypoint: Right condenser controls} {Waypoint: None (for 30 seconds)} {Waypoint: Evaporator controls} {Waypoint: None (for 30 seconds)} {Waypoint: Left condenser controls}** |  |

**{Input: Press \[E/Action button\] to turn off the right condenser}**  
**{Animation (Art): Condensation animation stops}**  
**{Audio: Quiet, mechanical humming SFX fade out}**

**{Input: Press \[E/Action button\] to turn on the evaporator}**  
**{Animation (Art): The evaporator glows and water vapor fills up the basin}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): The water level in the basin decreases}**

**{Input: Press \[E/Action button\] to turn on the left condenser}**  
**{Animation (Art): Water droplets form on the inside walls of the basin, then trickle down into the rising water}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): The water level in the basin rises slightly, and the power cube floats out into the canal, within reach}**

**{Input: Press \[E/Action button\] to pick up the power cube}**  
**{Input: Press \[E/Action button\] to place the power cube on the pedestal}**  
**{Animation (Dev): The door opens}**  
**{Audio: Rumbling SFX play along with the animation}**

**{Mission: “If I Had a Nickel” updated}**  
**{Quest Tracker: “At least you’re getting your steps in.”}**  
**{Waypoint: Newly opened door}**

**INT. ISLAND RUINS \- FLOOR 3, ROOM 3**  
This room contains a larger-than-usual evaporator basin about half full of water. There are two vents around the top of the basin, one in the ceiling and one on the far side leading into the rooms beyond. Another, smaller pipe goes the same direction, connected to the side just above the water level. The evaporator is active and sending water vapor through the upper pipe to the next room, but it is just as quickly replaced with liquid water flowing from the smaller pipe. The door across the room is open, revealing stairs leading upward. This room contains no control panel.

**INT. ISLAND RUINS \- FLOOR 3, ROOM 4**  
The closer of two basins connects to the two pipes from the previous room. The lower pipe connects near the base, while the upper pipe connects about halfway up. Its condenser is already running, and all condensed water is flowing right back into the lower pipe to the previous room. Another ventilation pipe connects to the further basin. Both of these contain condenser units, neither contains substantial water, and the further basin has a power cube and a canal leading outward. The two basins have separate control panels at their bases. A locked elevator is set into a side wall with a pedestal nearby.

##### 

| Timed Feedback |  |
| ----- | ----- |
| *If P doesn’t interact with the control panels for 15 seconds…* DANI **\[automatic, gameplay\]** *We need to get a power cube from an empty basin again. However, all of the water in this room is coming from the one we just left.* | *If P doesn’t interact with the control panel for 30 more seconds…* DANI **\[automatic, gameplay\]** *Water is condensing in the first basin before it can reach the second. We will need to address that first.* **{Mission: “If I Had a Nickel” updated} {Quest Tracker: “We need water to reach the second basin.”} {Waypoint: First condenser controls}** |

**{Input: Press \[E/Action button\] to turn off the condenser connected to the previous room}**  
**{Animation (Art): Condensation animation slows to a stop}**  
**{Audio: Quiet, mechanical humming SFX fade out}**  
**{Animation (Dev): Water vapor drifting into this basin now drifts through to the other instead of condensing immediately}**

**{Input: Press \[E/Action button\] to turn on the other condenser}**  
**{Animation (Art): Water droplets form on the inside walls of the basin, then trickle down into the rising water}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): The water level in the basin rises slightly, and the power cube floats out into the canal, within reach}**

**{Input: Press \[E/Action button\] to pick up the cube}**  
**{Input: Press \[E/Action button\] to place the cube on the pedestal}**  
**{Animation (Dev): The door opens}**  
**{Audio: Rumbling SFX play along with the animation}**

**{Mission: “If I Had a Nickel” updated}**  
**{Quest Tracker: “Surely we must be approaching the way out.”}**  
**{Waypoint: Elevator}**

Player proceeds to the elevator

**\<Cutscene\>**  
**{Audio: Elevator ding SFX plays, followed by rumbling elevator ascent SFX}**  
**{Animation (Dev): Elevator doors close, camera vibrates}**  
**{Audio: Elevator ding SFX play again as ascent SFX fade into silence}**  
**{Animation (Dev): Elevator doors open}**  
**\</Cutscene\>**

**INT. ISLAND RUINS \- FLOOR 4, ROOM 1**  
There are two basins in this room: a half full one with an evaporator and an empty one with a condenser. There is a power cube in the condenser basin and a canal connecting to the next room. The door forward is already open. Another Hegonian mural covers a side wall.

**{Mission: “If I Had a Nickel” updated}**  
**{Quest Tracker: “Investigate the raised section of the room.”}**  
**{Waypoint: None}**

**{IF PLAYER INTERACTS WITH MURAL}**

**\<Dialogue\>**

The mural depicts animals and plants thriving in the environment, and a group of Hegonians looking at one another appraisingly.

##### DANI

###### *We have found another Hegonian mural. There is an inscription.*

##### PLAYER

| What does the inscription say? | Let’s move on. |
| :---- | :---- |

##### DANI

| \[Translation\] Though we had staved off extinction for the remaining life of Praxis, we had not fixed the root cause of our planet’s suffering. Yet, there was still hope. There was still one thing we Hegonians had not yet changed to suit our needs. Ourselves.  | Understood. \<CLOSES TREE\> |
| :---- | :---- |

**\<End Dialogue\>**

##### 

| Timed Feedback |  |
| ----- | ----- |
| *If P doesn’t interact with the control panels for 30 seconds or tries to move to room 2 immediately…* DANI **\[automatic, gameplay\]** *While the door is open, there is a power cube in this room and a canal leading to the next. I recommend getting the cube to the next room before moving on.* | *If P doesn’t interact with the control panel for 60 more seconds…* DANI **\[automatic, gameplay\]** *The layout of this room is similar to some we encountered previously. Try evaporating the water first.* **{Mission: “If I Had a Nickel” updated} {Quest Tracker: “Try evaporating the water first.”} {Waypoint: Evaporator controls}** |

**{Input: Press \[E/Action button\] to turn on the evaporator}**  
**{Animation (Art): The evaporator glows and water vapor fills up the basin}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): Water vapor drifts from the evaporator basin to the condenser}**

**{Input: Press \[E/Action button\] to turn on the condenser}**  
**{Animation (Art): Water droplets form on the inside walls of the basin, then trickle down into the rising water}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): The water level in the basin rises slightly, and the power cube floats through the canal and into the next room}**

**{Mission: “If I Had a Nickel” updated}**  
**{Quest Tracker: “Follow that cube\!”}**  
**{Waypoint: Open door to room 2}**

**INT. ISLAND RUINS \- FLOOR 4, ROOM 2**  
The canal from the previous room connects to one of two wider basins in this room, and the power cube has floated into it. Another canal spans from the first to the second basin, which in turn leads into the next room. This door is also open. Both basins contain evaporators and condenser units, but only the far basin contains water.

##### 

| Timed Feedback |  |
| ----- | ----- |
| *If P doesn’t interact with the control panels for 30 seconds…* DANI **\[automatic, gameplay\]** *Another room to move the power cube through, and no way for us to pick it up yet. Hm.* | *If P doesn’t interact with the control panel for 60 more seconds…* DANI **\[automatic, gameplay\]** *If we cannot pick it up, we must use water. TK, I leave the controls to you.* **{Mission: “If I Had a Nickel” updated} {Quest Tracker: “Let’s keep that power cube moving.”} {Waypoint: None}** |
| ***\[Note: 30 seconds after the second set of feedback, the quest state should silently advance to one with the same tracker text and a waypoint on the next step. This repeats as follows when they complete each step.\]*** **{Waypoint: Second evaporator controls} {Waypoint: None (for 30 seconds)} {Waypoint: First condenser controls} {Waypoint: None (for 30 seconds)} {Waypoint: First condenser controls} {Waypoint: None (for 30 seconds)} {Waypoint: First evaporator controls} {Waypoint: None (for 30 seconds)} {Waypoint: Second evaporator controls} {Waypoint: None (for 30 seconds)} {Waypoint: Second condenser controls}** |  |

**{Input: Press \[E/Action button\] to turn on the second evaporator}**  
**{Animation (Art): The evaporator glows and water vapor fills up the basin}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Input: Press \[E/Action button\] to turn on the first condenser}**  
**{Animation (Art): Water droplets form on the inside walls of the basin, then trickle down into the rising water}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): Water fills the first basin as the second empties, carrying the cube through the canal and into the second}**

**{Input: Press \[E/Action button\] to turn off the first condenser}**  
**{Animation (Art): Condensation animation slows to a stop}**  
**{Audio: Quiet, mechanical humming SFX stop}**  
**{Input: Press \[E/Action button\] to turn on the first evaporator}**  
**{Animation (Art): The evaporator glows and water vapor fills up the basin}**  
**{Audio: Quiet, mechanical humming SFX play}**

**{Input: Press \[E/Action button\] to turn off the second evaporator}**  
**{Animation (Art): Evaporator light and visible water vapor fade}**  
**{Audio: Quiet, mechanical humming SFX stop}**  
**{Input: Press \[E/Action button\] to turn on the second condenser}**  
**{Animation (Art): Water droplets form on the inside walls of the basin, then trickle down into the rising water}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Animation (Dev): The first basin empties and the second refills, carrying the cube into the next room}**

**{Mission: “If I Had a Nickel” updated}**  
**{Quest Tracker: “Look at that cube go\!”}**  
**{Waypoint: Door to room 3}**

**INT. ISLAND RUINS \- FLOOR 4, ROOM 3**  
A large, floor-to-ceiling basin takes up the center of the room, with the power cube from the previous room inside. A pipe leads into the top of the basin from the floor outside, blocked by a closed vent. The corresponding switch is beside the pipe, near the locked door to the next room. A power cube pedestal is attached to the large, already running condenser unit at the top of the basin. Though there is some water in the basin, it is not enough to lift the cube to the pedestal.

##### 

| Timed Feedback |  |
| ----- | ----- |
| *If P doesn’t interact with the vent switch for 45 seconds…* DANI **\[automatic, gameplay\]** *Look at that pipe. The vent is closed, but it must connect to the floor below.*  **{Mission: “If I Had a Nickel” updated} {Quest Tracker: “Open the vent.”} {Waypoint: Vent switch}** |  |

**{Animation (Art): Scant water droplets form on the inside walls of the basin, then trickle down and out of sight}**  
**{Audio: Quiet, mechanical humming SFX play}**  
**{Input: Press \[E/Action button\] to use the vent switch}**  
**{Animation (Dev): Water vapor flows into the basin from room 3-3 below and condenses into liquid, lifting the power cube until it snaps onto the pedestal and the door opens}**  
**{Audio: Door opening SFX play with the animation}**

**INT. ISLAND RUINS \- FLOOR 4, ROOM 4**  
The door opens to reveal a darkened cavern tunnel. Hegonian lights provide gentle illumination to the tunnel that arches up and away, toward the island.

**{Mission: “If I Had a Nickel…” updated}**  
**{Quest Tracker: “How curious… where does this tunnel lead?”}**  
**{Waypoint \- End of Cavern}**

{PLAYER PROCEEDS TO CAVERN}

**INT. ISLAND TUNNEL**

The tunnel winds its way back upward at a gentle incline. The rocky walls of the tunnel look almost unfinished, though the lights and smooth floor clearly indicate it was Hegonian-made.

{PLAYER REACHES END}

**\<Cutscene\>**

At the end of the tunnel is a sealed door. The Player approaches, and the door rumbles and begins to open, then SEIZES up with a grinding sound. 

**{Audio: mechanical grinding sound}**

The gap in the door is tiny–only a single crack of sunlight streams through it.

The Player runs to the door and tries to force it open with their hands, but nothing happens.

**\<End Cutscene\>**

**\<Dialogue\>**

##### DANI

###### *This door is made of Hegonian alloy. I do not believe we have the tools to open it.*

##### PLAYER

| Can you contact anyone on the radio? | I’ll MAKE it open with my FISTS. {Animation: Player bangs on the door with their fists.} {Audio: hollow banging on steel door} {Animation: Having clearly hurt themself, the Player shakes and holds their hands} |
| :---- | :---- |

##### DANI

| Our transmitting range is severely limited by magnetic interference. Sending SOS now. | While you recover from your injuries, I will broadcast a local SOS. However, our transmitting range is severely limited by magnetic interference.  |
| :---- | :---- |

**{Audio: gentle electronic morse code beeping}**

The Player slumps down to the ground and leans back against the wall of the cavern.

**\<End Dialogue\>**

FADE TO BLACK