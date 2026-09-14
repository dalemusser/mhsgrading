# Place Pollution Sensors to Trace the Source

The player drops sensors along the river to locate where the pollution enters the watershed. The score starts from 5 possible points and is reduced when the player repeatedly triggers DANI’s reminder dialogues, which fire when a sensor placement does not follow the logic of downstream flow. Three reminders are scored, each in its own category.

## A. Testing in the Wrong Direction

Reminder: “Pollution will only flow downstream, so we need to test further upstream.”

* **2 points:** The reminder is triggered 0 or 1 time.
* **1 point:** The reminder is triggered 2 or 3 times.
* **0 points:** The reminder is triggered 4 or more times.

## B. Unnecessary Tests Upstream of a Clean Sensor

Reminder: “Green checkmark means clean. You won’t need to check upstream of a clean sensor.”

* **2 points:** The reminder is triggered 0 or 1 time.
* **1 point:** The reminder is triggered 2 or 3 times.
* **0 points:** The reminder is triggered 4 or more times.

## C. Starting Point at the Ocean

Reminder: “We are at the ocean downstream of Tera’s base — logically, there will be pollution here. I recommend proceeding upstream.”

* **1 point:** The reminder is never triggered.
* **0 points:** The reminder is triggered.

## Overall Score

```text
Final Score = A + B + C
```

The maximum combined score for this progress point is **5 points**.
