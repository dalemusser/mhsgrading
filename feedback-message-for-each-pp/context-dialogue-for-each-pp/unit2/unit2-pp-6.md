## Task 2.3: Drone on the Range
{Animation (Dev): Drone launches automatically}
[Note: View and controls change to drone movement]
{Quest Tracker: “Which Watershed?: Scan the ocean”}
{Waypoint: Ocean outlet at the eastern lake}

##### DANI [gameplay, automatic]
###### Please fly the drone to the marker.

{Popup: Drone control tutorial image(s)}
##### DANI [Sequence, conversation]
###### Excellent work, TK. You are growing proficient in your piloting of the drone.

##### PLAYER [choices]
| Thanks, DANI. I think I’m ready. | What can I say? I’m a natural. |
| :---- | :---- |

##### DANI [End sequence, gameplay]
###### Perhaps you should practice collecting evidence using the drone as well. I will offer an option for evidence collection.

{Popup: Required data screen displays that the player must collect:
1) The salinity of the ocean
}
{Quest Tracker: “Mission: Which Watershed?: Scan the ocean”}
{Waypoint: Ocean outlet at the edge of the lake}

While flying drone, player reaches the waypoint in the ocean…
{Input: Press [E/Action button] to scan the ocean}

{Animation (Dev): Drone send a long-range scanning pulse that sweeps across the surface of the ocean}
{Animation (Art): Celebratory animation plays as the data screen marks off salinity}

##### DANI [Sequence, conversation]
###### As expected, the ocean’s salinity registers as seven percent. The drone’s scan function appears to be working correctly.

##### PLAYER [choices]
| We should go collect real evidence now. | Can’t we just pick a watershed at random and call it good? |
| :---- | :---- |

##### DANI [curricular]
| Affirmative. | Negative. We need to collect additional evidence before we may determine whose claim is correct. |
| :---- | :---- |

##### DANI [End sequence, gameplay]
###### I recommend beginning with the eastern watershed. We can make a measurement at the river first, then proceed to the waterfall. Placing a marker on the river.



{Quest Tracker: “Mission: Which Watershed?: Evaluate the eastern river”}
{Waypoint: Midpoint (roughly) of the eastern river}

EXT. EASTERN RIVER

As the drone comes within [20 units] of the waypoint…

##### DANI [Sequence, conversation, automatic]
###### We are now in a good location to measure the river.

##### PLAYER [choices]
| Roger. | Chill, DANI, I know that. |
| :---- | :---- |

##### DANI [End sequence, gameplay]
###### There is one primary piece of information to collect.

{Popup: Required data screen appears, displaying that the player must collect:
1) The distance from the eastern waterfall to the ocean}

When the drone reaches the waypoint…
{Input: Press [E/Action button] to scan the eastern river]
{Animation (Dev): Drone sends a long-range scanning pulse that sweeps up the length of the river}
{Animation (Art): Celebratory animation plays as the data screen marks off distance}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}



##### DANI [Sequence, curricular]
###### <color="green">The waterfall is approximately 85km from the ocean.</color>

##### PLAYER [choices]
| I think we have everything we need here. | That’s a wrap! |
| :---- | :---- |

##### DANI [End sequence, gameplay]
###### Agreed. Let us proceed to the eastern waterfall. Placing the waypoint now.


{Quest Tracker: “Mission: Which Watershed?: Investigate the eastern waterfall. 0/3 points investigated}
{Waypoints: Basin, midpoint, and top of waterfall}

EXT. EASTERN WATERFALL

When the drone comes within [20 units] of the waypoints…

##### DANI [Sequence, conversation, automatic]
###### We are now in an ideal location to measure the waterfall.

##### PLAYER [choices]
| Let’s do it! | Time for some serious stunt flying! |
| :---- | :---- |

##### DANI [End sequence, gameplay]
###### There are three primary pieces of information to collect.

{Popup: Required data screen appears, displaying that the player must collect:
1) water salinity
2) waterfall height
3) flow rate}

[Note: The three data points can be collected in any order]

When the drone reaches the waterfall basin waypoint…
{Input: Press [E/Action button] to assess salinity}
{Animation (Dev): Arm mechanism with dropper emerges from bottom of drone and takes a sample from the water. Corresponding data appears on screen}
{Animation (Art): Celebratory animation plays as the data screen marks off salinity}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}
{Quest Tracker: “Mission: Which Watershed?: Investigate the eastern waterfall. 1/3 points investigated”}
{Waypoint: Waterfall basin waypoint disabled}

When the drone reaches the middle waypoint…
{Input: Press [E/Action button] to assess flow rate}
{Animation (Dev): Water wheel appears from drone arm. When it touches water, wheel spins and corresponding data appears on screen}
{Animation (Art): Celebratory animation plays as the data screen marks off flow rate}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}
{Quest Tracker: “Mission: Which Watershed?: Investigate the eastern waterfall. 2/3 points investigated”}
{Waypoint: Middle waypoint disabled}

When the drone reaches the upper waypoint…
{Input: Press [E/Action button] to measure height}
{Animation (Dev): Drone uses laser to draw a line from the bottom of the waterfall to the top. Corresponding data appears on screen}
{Animation (Art): Celebratory animation plays as the data screen marks off height}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}
{Quest Tracker: “Mission: Which Watershed?: Investigate the eastern waterfall. 3/3 points investigated”}
{Waypoint: Upper waypoint disabled}

When the player collects all three data points…

##### DANI [Sequence, curricular, automatic]
###### <color="green">This waterfall is pouring 30 liters of water per second, about 35 meters tall, and the salinity level seems to be 0.2%.</color>

##### DANI [conversation]
###### I have logged all relevant pieces of evidence from the drone.
######
##### PLAYER [choices]
| Time for the western watershed. | All right, let’s get the western side done with. |
| :---- | :---- |
######
##### DANI [End sequence, gameplay]
###### Marking the western river on your map.


{Quest Tracker: “Mission: Which Watershed?: Assess the western river”}
{Waypoint: Midpoint (roughly) of the western river}

EXT. WEST RIVER

When the drone comes within [20 units] of the waypoint…

##### DANI [Sequence, conversation, automatic]
###### We have reached the river and may begin measurements.

##### PLAYER [choices]
| Can do. | Yep, I still know that, DANI. |
| :---- | :---- |

##### DANI [End sequence, gameplay]
###### There is one primary piece of information to collect.

{Popup: Required data screen appears, displaying that the player must collect:
1) distance from waterfall to ocean}

When the drone reaches the waypoint…
{Input: Press [E/Action button] to measure the river}
{Animation (Dev): Drone sends a long-range scanning pulse that sweeps up the length of the river}
{Animation (Art): Celebratory animation plays as the data screen marks off distance}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}



##### DANI [Sequence, curricular]
###### <color="green">The waterfall is approximately 95km from the ocean.</color>

##### PLAYER [choices]
| Let’s get to the waterfall. | Let’s blow this popsicle stand. |
| :---- | :---- |

##### DANI [End sequence, gameplay]
###### Placing the waypoint for the western waterfall now.


{Quest Tracker: “Mission: Which Watershed?: Investigate the western waterfall. 0/3 points investigated}
{Waypoints: Basin, midpoint, and top of western waterfall}


EXT. WESTERN WATERFALL
When the drone comes within [30 units] of the waypoints…
#####
##### DANI [conversation, automatic]
###### We need to collect the same three pieces of evidence about this waterfall.

{Popup: Required data screen appears, displaying that the player must collect:
1) water salinity
2) waterfall height
3) flow rate}

[Note: The three data points can be collected in any order]

When the drone reaches the waterfall basin waypoint…
{Input: Press [E/Action button] to assess salinity}
{Animation (Dev): Arm mechanism with dropper emerges from bottom of drone and takes a sample from the water. Corresponding data appears on screen}
{Animation (Art): Celebratory animation plays as the data screen marks off salinity}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}
{Quest Tracker: “Mission: Which Watershed?: Investigate the western waterfall. 1/3 points investigated”}
{Waypoint: Waterfall basin waypoint disabled}

When the drone reaches the middle waypoint…
{Input: Press [E/Action button] to assess flow rate}
{Animation (Dev): Water wheel appears from drone arm. When it touches water, wheel spins and corresponding data appears on screen}
{Animation (Art): Celebratory animation plays as the data screen marks off flow rate}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}
{Quest Tracker: “Mission: Which Watershed?: Investigate the western waterfall. 2/3 points investigated”}
{Waypoint: Middle waypoint disabled}

When the drone reaches the upper waypoint…
{Input: Press [E/Action button] to measure height}
{Animation (Dev): Drone uses laser to draw a line from the bottom of the waterfall to the top. Corresponding data appears on screen}
{Animation (Art): Celebratory animation plays as the data screen marks off height}
{Animation (Dev): Argumentation Orb (Evidence) flies into the drone}
{Quest Tracker: “Mission: Which Watershed?: Investigate the western waterfall. 3/3 points investigated”}
{Waypoint: Upper waypoint disabled}


When the player collects all three data points…

##### DANI [Sequence, curricular, automatic]
###### <color="green">This waterfall is: pouring 100 Liters of water per second, is 20 meters tall and the salinity is 0.35%.</color>

##### DANI [End sequence, curricular]
###### I have generated a table of the data you have collected from both waterfalls in the area. Please take note.

{Animation (Dev): Argumentation Orb (Backing Info) flies into the drone}

{Popup: ARF Chart 1 U2 DANI Charts}

After the player closes the table…
{Audio: Ringtone SFX plays through DANI’s dialogue}
#####
##### DANI [Sequence, conversation, automatic]
###### Excellent timing–Captain Toppo is calling

##### TOPPO [gameplay, call]
###### Deputy, I hope you’ve been collecting good evidence out there. I want you to get the drone back here and meet up with us, on the double.

##### PLAYER [choices]
| Yes, Captain. | I’ll get around to it. |
| :---- | :---- |

##### TOPPO [End sequence, conversation, call]
| Toppo, out. | You’d better. Toppo, out. |
| :---- | :---- |

{Quest Tracker: “Mission: Which Watershed?: Make your case!”}
{Waypoint: The player’s location (cadet, not drone)}

The player pilots the drone back to the group.
