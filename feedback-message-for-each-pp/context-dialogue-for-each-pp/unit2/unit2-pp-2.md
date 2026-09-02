## Task 1.2 - Back on Board
EXT. TEMPLE ENTRANCE - MID-DAY

[Cutscene] Player Exits the Temple

Player exits temple–the door emerges from the base of a mountain–and finds themself looking across the truly alien world of WAT247. The alien sounds of a distant world are carried on a hollow wind.
{Audio: Crash Site (Exploration) BGM begins, Ruins BGM ends}
{Audio: Alien nature ambience SFX plays. After a brief delay, a dull roaring SFX grows steadily louder}

##### DANI [conversation]
###### I am detecting a rapidly approaching bio-signature.

{Animation (Art): Bruised and self-bandaged, Anderson comes SPEEDING in on a rickety, shaking hoverboard, drifting in way too fast and letting out an enormous backfire as she stops.}
#####
##### ANDERSON [conversation]
###### TK! TK!

{Animation (Art): Anderson hops off the hoverboard.}

[/Cutscene]



PLAYER [Dialogue, choices, automatic]
| Glad to see you’re safe. | Am I about to get some sort of lecture? |
| :---- | :---- |

ANDERSON [conversation]
| Pfft, I can survive anything with a canteen and a multitool. | Nah, I’m too busy getting us all out of this mess. |
| :---- | :---- |

##### DANI [conversation]
###### Cadet Anderson, how did you locate us?

##### ANDERSON [curricular]
###### I used my scanner to pull the last moments of footage from your pod before it crashed. I could tell that you were headed straight into the west side of a mountain range. All I had to do was cross-reference that information with my topographic map of the area to determine where you were.

##### PLAYER [choices]
| Could you show me how to do that? | Sounds easy–I’ll bet I could do it. |
| :---- | :---- |

##### ANDERSON [conversation]
###### Sure. Let's check the map.

######
[Map tutorial 2: U2 Map Tutorials]
Map opens automatically
[Note: Use the fog of war map depicted on slide 5 of this slideshow]
{Animation (Dev): Highlight increasingly narrow sections of the map and UI elements as Anderson speaks}

##### ANDERSON [curricular]
###### I could tell that your pod was going to crash into the west side of a large mountain range, close to the middle. I used the map to find a big area of high elevation with contour lines close together on both sides–the large steep mountain. From there, I used the map compass to find out which side was the west side and headed towards the center of that region.

##### PLAYER [choices]
| Got it. Super easy. | I’m still lost. |
| :---- | :---- |

##### ANDERSON [conversation]
###### You should have a mission control video on topographic maps. Do you want to watch it again?

##### PLAYER [choices]
| Sure. {Popup: Topography Toppo Lesson plays - U1 Toppo Lessons} | No, I’m good. |
| :---- | :---- |

Map closes automatically

[End map tutorial #2]

##### DANI [conversation]
###### Cadet Anderson, have you located any of the other cadets from the pod footage yet?

##### ANDERSON [conversation]
###### Let’s see what we’ve got.


######

[Cutscene]
(Animation (Art): Anderson pulls out a cobbled together walkie-talkie-like device with a huge radar scanning screen. She looks down at the device meaningfully for a moment. It lets out a sad beep of failure. She shakes it vigorously in frustration.}

##### ANDERSON [conversation]
###### Much better.

{Animation (Art): The device begins to glow}
{Audio: Happy, low-res beep SFX plays}
[/Cutscene]



##### ANDERSON [conversation]
###### I’ve got another pod located. Captain Toppo is located just northwest of here on a hill at an elevation of approximately 90 feet.

##### PLAYER [choices]
| I think I’d better go rescue the Captain. | I’ll find her when I’ve got some time. |
| :---- | :---- |

##### ANDERSON [curricular]
###### Perfect. That gives me more time to get this tracker working better. I’ll let you know when I get location data on the others.

##### PLAYER [End dialogue, choices]
| You know, a hoverboard would make this search go faster. | That hoverboard is a sweet ride, Anderson. I want it. |
| :---- | :---- |



[Cutscene]Anderson and Hoverboard
{Animation (Art): Anderson looks at her hoverboard and shrugs}

##### ANDERSON [conversation]
###### Guess I don’t need it for now. Go for it.

{Animation (Art): Anderson tosses Player the hoverboard}
{Animation (Art): Player gets on the hoverboard, which shudders worryingly}
(Audio: Grinding and sparking SFX play}
{Animation (Art): Player steps down off the board}
[/Cutscene]



##### DANI [Dialogue, conversation]
###### This hoverboard is not up to regulation. I calculate a 43.7% probability of a catastrophic failure.

##### ANDERSON [conversation]
###### It works fine. I just took some “non-essential” parts off it to fix up this scanner.

##### PLAYER [choices]
| Still seems a bit sketchy. | This thing is going to explode. |
| :---- | :---- |

##### DANI [conversation]
###### Anderson, this hoverboard must be repaired before we can depart.

##### ANDERSON [conversation]
###### Fine, fine. I found some kind of alien forge–at least, I think it’s a forge–over on that hill. I’m sure I can figure out how to use it to fix the hoverboard with some of the debris that fell off the Copernicus. Bring over five pieces of scrap, and I’ll get it fixed up for you.

##### DANI [conversation, in ear]
###### Cadet Anderson clearly does not suffer a lack of self-confidence.


{Mission: Foraged Forging assigned}
{Quest Tracker: “Foraged Forging: Collect 5 piles of scrap metal. X/5 collected}
##### DANI [End dialogue, gameplay]
###### TK, this is the first time we have had more than one mission at a time. If you would like to turn mission tracking on or off, open the objectives interface and [UI/control indication needed].

When the player is in range of a pile of scrap…
{Input: Press [E/Action button] to pick up scrap}
{Animation (Art): Player leans down and picks up scrap (general animation)}

After the player collects at least 5 piles of scrap metal…
{Mission: Foraged Forging updated}
{Quest Tracker: “Foraged Forging: Return to Anderson”}
{Waypoint: Anderson}

Anderson stands next to the alien forge.

{Input: Press [E/Action button] to talk to Anderson}

##### ANDERSON [Dialogue, conversation]
###### Looks like you found all the scrap we need. Meanwhile, I’ve mastered using this alien forge.

{Animation (Art): Anderson presses a button on the forge. Nothing happens. She presses a second button. Nothing happens. She presses a third, angrily, and dangerous sparks burst out of the top with a terrible mechanical grinding sound}

##### ANDERSON [Dialogue, conversation]
###### (trying to convince TK) It’s supposed to do that!

{Animation (Art): Anderson kicks the forge, and with the sound of a motor turning over and starting, it begins thrumming along smoothly, lights happily flashing as it waits to forge new items.}

##### ANDERSON [End dialogue, conversation]
###### See? Running like clockwork. TK, follow my lead and don’t get in the way.

{Mini Game: Scrap Forge}

After completing the mini game…

{Animation (Art): Anderson looks happily at the hoverboard.}
{Tutorial Popup: Hoverboard toggle}
[Note: For the on-screen, touch interface, the hoverboard toggle button should now be available]
##### [Cutscene]
#####
##### ANDERSON [Dialogue, conversation, automatic]
###### All done. DANI, does this meet your specifications now?
######
##### DANI [conversation]
###### Scanning.


A green scan emits from the holo-watch that washes back and forth over the hoverboard–and then the board disintegrates!

##### ANDERSON [conversation]
###### DANI, I JUST BUILT THAT.

A green scan from the holo-watch re-extends and the board rematerializes.
[/Cutscene]

##### DANI [conversation]
###### It appears the nanomachines have granted me the ability to project solid, tangible holograms of objects. “Holids,” if you will. TK, I can now store your hoverboard as a holid and recall it for you any time you need it.

##### PLAYER [choices]
| That’s awesome, DANI. | That’s really weird. |
| :---- | :---- |

##### DANI [conversation]
| Agreed. It is an ability capable of inspiring awe. I am curious what else I may be able to project as a holid. | I apologize for any concern this may cause you. It is, however, highly efficient. |
| :---- | :---- |

##### Anderson [conversation]
###### DANI, you and I are going to have a long conversation later about how we can use that alien ability. For now, TK, I could use more scrap from the Copernicus for some of my other projects, too. If you collect scrap and bring it back to me, I’ll let you be the beta tester for whatever I invent next. Deal?

##### PLAYER [choices]
| Sounds good. | I’ll think about it. |
| :---- | :---- |

{Animation (Art): Anderson nods}

{Request: Reduce, Reuse, Recycle assigned}
{Mission: Getting the Band Back Together assigned}
{Quest Tracker: “Getting the Band Back Together: Find Captain Toppo”}

## Task 1.3 - Finding Toppo

##### ANDERSON [curricular]
###### Well, what are you waiting for? You’ve got a working hoverboard…apparently… and Captain Toppo is located just northwest of here on a hill at an elevation of approximately 90 feet.
#####
##### DANI [curricular]
###### Opening your map, TK.

Map opens automatically
[Note: Fog of War obscures the shaded areas on slide 5 of U2 Topographic Character Hunt (July 2023 Version)]
[Map tutorial 3 U2 Map Tutorials]

##### DANI [End dialogue, gameplay]
###### You may now place your own waypoints on the map. These may assist you in navigating the world. Drag and move a waypoint from the glowing box to the map.Try placing a waypoint where you think Captain Toppo may be, based on Anderson’s readings.

[Note: A text box should display Anderson’s hint until the map closes]
{Animation (Dev): A highlight blinks on and off at the marker box until the player places a marker. When they tap or mouse over the box, a transparent “ghost” marker moves from the box to the map, then drops. This animation loops as long as the player is interacting with the box or actively dragging the marker.}
{Input: [Click/Tap] the waypoint and drag it to where Toppo could be}

If the player tries to place a waypoint on a foggy part of the map…

##### DANI [gameplay]
###### I do not have data for this region yet. For now, focus on the area I have information on.
{Audio: Congratulatory SFX plays when the player places a waypoint}

After the player places a waypoint…



##### DANI [Sequence, curricular, automatic]
###### TK, this is an opportune moment to check on the recovery of your short-term memory: what is indicated by the contour lines being close together on a topographic map?
######
##### PLAYER [choices]
| There are steep elevation changes. | There is flat land. | I honestly don’t know. |
| :---- | :---- | :---- |

##### DANI [End sequence, curricular]
| Excellent, your short-term memory appears to be recovering well. | Where contour lines are close together, there are steep elevation changes. Let’s review the mission video on topographic maps. {Popup: Topography Toppo Lesson plays - U1 Toppo Lessons} | That is okay. Let’s review the mission video on topographic maps. {Popup: Topography Toppo Lesson plays - U1 Toppo Lessons} |
| :---- | :---- | :---- |

| FEEDBACK |  |  |
| :---- | :---- | :---- |
| If P wanders off-course (see pink areas on slide 4) U2 Topographic Character Hunt (8/10/23 Version) DANI [curricular] Anderson said that Toppo’s pod was northwest of our original location. We should look for a location on a hill at an elevation of approximately 90 feet. Remember you can move the waypoint on your map at any time. | If P hasn’t found Toppo, checked the map, or received other feedback for 2 minutes DANI [gameplay, roaming] Remember to use your map. To open it, [press M/tap the Map button].. | If P hasn’t found Toppo in 5 minutes and hasn’t received other feedback for 2 minutes DANI [gameplay, roaming] We need to find Toppo soon, TK. Use your map to find an area on a hill at an elevation of approximately 90 feet. |

[End map tutorial 3]


Player travels to Toppo’s location

EXT. - TOPPO’S RIDGE

[Cutscene] Finding Toppo

Player proceeds forward to find Toppo at her crashed, still smoking escape pod. She has two crates kicked open haphazardly, with various survival gear, maps, and more spilling out of them. She has a topographic map, compass, canteen, and markers spilled across a fold out table that she’s nervously watching.
{Animation (Art): Toppo pores over the map, nervous and agitated}

{Animation (Art): Toppo looks up}

##### TOPPO [conversation]
###### (elated) TK, you’re all right!

Toppo embraces the Player in a bear hug. Then, seemingly realizing she’s broken her mask of composure, she quickly releases the player and slides back into a more authoritative stance, coughing and composing herself.
{Animation (Art): Toppo wraps the player in a bear hug. After a moment, she sheepishly steps back and returns to her usual, authoritative composure}
[/Cutscene]

##### TOPPO [Dialogue, conversation, automatic]
###### (officious) Status report?

##### PLAYER [choices]
| Ready for duty. | I could use a sick day. |
| :---- | :---- |

##### DANI [conversation, in ear]
| Are you certain you are feeling prepared? This was a traumatic event. I may be able to persuade Captain Toppo to give you some time. | Noted. Adjusting health output parameters. |
| :---- | :---- |

##### PLAYER [choices]
| I’m okay, I promise. | Actually, I could use a break. | Thanks, DANI. |
| :---- | :---- | :---- |

##### DANI [conversation]
| Captain, I can verify the Cadet is in prime physical condition and ready to report. | Captain, the Cadet has experienced multiple traumatic events in succession. Without a full psychological evaluation, I cannot recommend the Cadet for active duty. |
| :---- | :---- |

##### TOPPO [conversation]
| Excellent. And DANI, I’m glad to see you made it down in one piece. | (sighing) Noted. I wish I could give you a break, but I still need your help before we can rest. DANI, I’m glad you made it down and can provide support to Cadet TK. |
| :---- | :---- |

##### TOPPO [conversation]
###### Now, do either of you have any idea of the whereabouts of the other cadets?

##### DANI [conversation]
###### Captain, we met with Anderson at the base of the mountain and are coordinating with her to locate all mission crew members.

{Animation (Art): Toppo salutes}

##### TOPPO [conversation]
###### Cadet TK, that is exemplary work, and I want you to keep up your search for the others. To that end, I’m officially deputizing you, which raises your mission rank by one level and grants you more authority in how you operate.
######
##### PLAYER [choices]
| Thank you, Captain! | Sweet, power! |
| :---- | :---- |

##### TOPPO [conversation]
###### I’m going to go meet up with Anderson to begin coordinating our next steps. Keep me updated on your progress, Deputy TK.

[Note: From this point forward, Toppo will use a dialogue variable for the majority of her references to the player. This variable will hold the player’s current rank within the team, which will increase as they complete arguments and critiques.]
