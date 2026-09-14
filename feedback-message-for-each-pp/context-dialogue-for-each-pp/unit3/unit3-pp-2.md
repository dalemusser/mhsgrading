## Task 1.2 \- The Source of the Pollution

**{Audio: Alarm siren SFX plays}**

##### TERA **\[conversation\]**

###### *Oh no\!*

**{Animation: Tera checks the readout on a device.}**

##### 

##### TERA **\[curricular\]**

###### *The analysis of the river water just finished–it has some sort of toxic material in it\! That’s the same water I’ve been using on the crops… which means they’re all dead\!*

**{Audio: Dark musical sting plays}**

##### PLAYER **\[choices\]**

| What happened to the crops? | What about the livestream? | Are there any seeds left? | How long can we go without food? | Give me the last few seeds. I’ll find some way to get us more food. |
| :---- | :---- | :---- | :---- | :---- |

##### TERA **\[conversation\]**

| *The polluted water… it killed everything I planted in the field. We have no food.* | *You think I can stream this? I built a campsite right next to a river full of toxic chemicals and killed all of our crops. My viewers would think I’m a fraud.* | *We only have a handful of seeds now. I don’t know if they’ll be enough.* | DANI \[conversation\] With rationing, I estimate the team will be able to survive for an additional 19 days, 6 hours, 53 minutes, and 12 seconds. Approximately. TERA \[conversation\] I think you forgot a \<joke\> tag, DANI. | \<CLOSES CONVERSATION\> |
| :---- | :---- | :---- | ----- | :---- |

##### TERA **\[curricular\]**

###### *I may have made a mistake, but I’m still responsible for safeguarding this mission’s food supply. You’re not planting ANYTHING until you convince me you’ve found the source of the pollution. You’re going to need to provide a rock-solid claim, reasoning, and evidence that you’ve found the source before I let you have the seeds.*

**{Animation (Dev): Argumentation Orb (Driving Question) flies into the holo-watch}**

##### DANI **\[conversation\]**

###### *Logging this information into the argumentation engine.*

Argumentation interface opens automatically.

**{Popup: “Driving Question Collected."}**

**{Animation (Dev): The driving question fades into its respective slot.}**

Argumentation interface closes automatically.

##### DANI **\[conversation\]**

###### *TK, there are several pollution sensor modules in that crate. Since the sensors detect contamination, we could utilize the drone to test along the river and pinpoint the source of the contamination. Launching now.*

**{Animation (Art): DANI projects the holid drone for the player to use}**  
**{Audio: Drone flight SFX}**  
**(Player control automatically shifts to the drone)**  
**{Popup: “Mission: Pollution Solution assigned”}**  
**{Quest Tracker: “Pick up a pollution sensor module”}**

##### DANI **\[gameplay, *automatic*\]**

###### *Pick up a sensor module from the open crate.*

Player flies the drone to the crate  
**{Input: Press \[E/Action button\] to pick up the module}**  
**{Popup: “Mission: Pollution Solution updated”}**  
**{Quest Tracker: “Test the sensor module”}**

##### DANI **\[gameplay\]**

###### *We can test the water most effectively by dropping a sensor into the river. Place one now to test it.*

Player drops sensor into the river.  
**{Input: Press \[E/Action button\] to drop a sensor}**

##### DANI **\[gameplay\]**

###### *Excellent, this sensor is able to detect the pollution in the river. I will mark sensor results for you on your map–a red X means that the river is polluted. A green checkmark means that it is clean. With these, we should be able to pinpoint exactly where the source of the pollution is located.*

**{Popup: “Mission: Pollution Solution updated”}**  
**{Quest Tracker: “Use the sensors to track pollution”}**  
Player flies up the river and drops sensors.  
**{Input: Press \[E/Action button\] to drop sensors}**  
***\[Note: Input prompt for pollution sensors will be displayed at any point while the drone is above the river\]***

| FEEDBACK |  |  |
| ----- | ----- | ----- |
| **(If P throws sensor and it’s polluted)**  DANI **\[curricular\]** *Red X for polluted. I’ll mark it for you.* **{Animation (Dev): Argumentation Orb (Evidence) flies into the drone} *\[Note: A red X mark appears on the map at the sensor’s location\]*** | **(If P throws sensor and it’s clean)**  DANI **\[curricular\]** *The water is clean.* **{Animation (Dev): Argumentation Orb (Evidence) flies into the drone} *\[Note: A green checkmark appears on the map at the sensor’s location\]*** | **(If P throws a sensor downstream of any sensor)**   DANI **\[curricular\]** *Pollution will only flow downstream, so we need to test upstream of the pollution.* |
| **(If P throws near most upstream polluted sensor)**  DANI **\[curricular\]** *We previously tested close to this area. Consider heading further upstream.*  | **(If P throws a sensor upstream of a clean sensor)**  DANI **\[curricular\]** *Green checkmark means clean. You won’t need to check upstream of a clean sensor.* | **(If P throws a sensor into the ocean at the river's mouth)**  DANI **\[curricular\]** *We are at the ocean downstream of Tera’s base–logically, there will be pollution here. I recommended proceeding upstream.* |
| Location-Based Feedback |  |  |
| DANI **\[curricular\]** *Excellent work. It appears we have passed the first river branch. Let us continue upstream.* | DANI **\[curricular\]** *We are making excellent progress–our location is approximately halfway to the waterfall.* | DANI **\[curricular\]** *We have nearly reached the waterfall. There is only one more river branch to test. The source of the pollution is most likely there.* |

**\[Cutscene\] Drone Flying Back to Camp:**   
**\[As the Drone automatically flies back to Tera’s Camp\]**

**{Popup: “Mission: Pollution Solution updated”}**  
**{Quest Tracker: “Present your case to Tera”}**  
**{Audio: Tera’s Garden (Argumentation) BGM begins, Exploration BGM ends, Ringtone SFX plays}**  
**\[/Cutscene\]**

**{Popup: DANI Map (To be updated for 2.0) [Backing Info](https://docs.google.com/presentation/d/17FvX1uFWxikRjxbby2ntLkWXR_haE483jjmVyi2ofTQ/edit?slide=id.g2bb6a59d4c5_0_71#slide=id.g2bb6a59d4c5_0_71)}**

##### DANI **\[curricular, *automatic*\]**

###### *I have overlaid the collected sensor data on the map. By observing the clean versus polluted areas of the river, you have determined the source of the pollution. This information should help convince Tera we know exactly where the source is located.*