## Task 2.4: Just Like the Simulations
EXT. GROUP LOCATION

When the player reaches the waypoint…
[Note: View and control returns to the cadet]
{Animation : The drone flies into TK’s backpack}
The Player walks over to the team, who are still standing around bickering.
{Animation (Dev): Toppo walks over to the player}


##### TOPPO [Sequence, conversation, automatic]
###### Deputy, I trust you’ve made good progress and been able to keep DANI on track now that he’s fixed.
######
##### DANI [conversation]
###### Feeling much better, Captain.

##### TOPPO [curricular]
###### Good. Deputy, let’s look at the data you’ve collected to help us determine which river is created by the largest watershed. Keep in mind that not all of the evidence is useful when building your argument.
######
##### TOPPO [curricular]
###### We have two claims for this argument. The first is that <color=#35F>the watershed upstream of the Eastern waterfall is larger than the watershed upstream of the Western waterfall.</color> The second is that  <color=#35F>the watershed upstream of the Western waterfall is larger than the watershed upstream of the Eastern waterfall.</color> Which data point do you think will be most important for identifying the largest watershed?

##### PLAYER [choices, saved]
| Flow rate. | Waterfall height. | Salinity. |
| :---- | :---- | :---- |

##### TOPPO [gameplay]
###### Okay, let’s put your thinking to the test using DANI’s argumentation system. You’ll use the claims and evidence you’ve collected to make an argument.
######
##### TOPPO [conversation]
###### Do you have any questions about arguments, Deputy?

[Note: The following choices loop back to the above question until the player moves on]
| Choice: What is a claim? TOPPO [curricular] A <color=#57F>claim</color> is the main idea that you are trying to support in an argument. | Choice: What is evidence? TOPPO [curricular] <color=#3F5>Evidence</color> is information collected from the environment that supports your claim. | Choice: What is reasoning? TOPPO [curricular] <color=#F53>Reasoning</color> is a scientifically accurate idea that logically connects your claim and evidence. |
| :---- | :---- | :---- |
| Choice: Nope. TOPPO [conversation] Do you have any other questions? [Note: The following choices loop back to this question until the player moves on] |  |  |
| Choice: Why is this important? TOPPO [curricular] Since the Copernicus was destroyed, we’re stranded here. If we’re going to survive on this planet, we’re going to need as much water as possible. By determining which watershed is larger, we will be able to establish our base in the best possible location. | Choice: What is a watershed? TOPPO [curricular] A watershed is a way of thinking about where water that falls on land goes. A watershed describes an area of land that includes all the streams and rivers that flow together and eventually flow out to sea. Larger watersheds have more water flowing through their rivers. | Choice: Wait, I forgot something. TOPPO [conversation] Do you need a reminder on any other parts of an argument? [Note: Loops back to the choices above] |
| Choice: I’m ready to argue. TOPPO [End sequence, conversation] Okay, let’s begin. |  |  |




Argumentation interface opens automatically.

Player makes passing argument.
[Note: Details in this document U2 Arg Details (Updated for 2.0)]

When the player presents a completed argument…


#####
##### TOPPO [conversation, automatic]
###### That’s it–Deputy TK has proven the western waterfall belongs to the largest watershed.

##### TERA [conversation]
###### I knew I was right! Looks like you all need to trust your survival expert a little bit more. BOOM! Haha!

##### JASPER [conversation]
###### I strongly disagree with this outcome. The eastern watershed is superior for our purposes. In time, I will convince you to relocate.

##### ARYN [conversation]
###### Let’s pump the brakes, Jasper. TK gave 110%, nailed that argument, and took it to the next level. Easy shoe-in for a promotion.

##### ANDERSON [conversation]
###### Aryn, would you just… nevermind. Let’s just get moving so I can start getting things set up at basecamp.
######
{Animation (Art): Toppo turns to address the group}
######
##### TOPPO [conversation]
###### Everyone, pick up as much of your gear as you can carry. Let’s head up beyond that waterfall and get started on our base camp!


{Animation (Dev): Toppo walks up to the player}
{Animation (Art): The team moves to gather their things in the background}



##### TOPPO [Sequence, conversation]
###### Deputy, I want to congratulate you on how well you’ve done. You’ve handled every problem thrown at you today and just solved a major issue for the team by successfully completing that scientific argument.
######
##### PLAYER [choices]
| You’re welcome! | Eh, it was no big deal. |
| :---- | :---- |

##### TOPPO [conversation]
###### TK, you’ve more than proven to me that you’re ready and willing to take on responsibility for the integrity of this mission. As of today, you’re  officially my second in command. We’ll all be relying on you to help us survive this mess. Best of luck, Deputy TK. I’ll see you at basecamp.

##### PLAYER [End sequence, choices]
| Thank you, Captain! | I’ll be waiting for the next promotion! |
| :---- | :---- |

{Request: Claim of Command assigned}

FADE TO BLACK

FADE IN
