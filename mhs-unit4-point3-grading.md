# Unit 4 Point 3 Grading

**Activity:** Alien Well Floor 3 & 4

**Trigger(Start) Event:** `questActiveEvent:48`
**Trigger(End) Event:** `questActiveEvent:50`

---

## Grading Rule

This progress point will check how many times the player interacts with the soil machines on the third and forth floors within the alien dungeon. Depending on the number of attempts, a score will calculated.
Basically the score will increase one if the player just interacted with the machine on the third floor at the first attempt to figure out the right type, otherwise zero.
For the forth floor, if the player interacts with the machine once to figure the correct type then further increase two; if the interaction time is two then further increase 1; otherwise no further score increased.

| Outcome | Condition |
|---------|-----------|
| **Green** | score > 1 |
| **Yellow** | score <= 1 |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:48` (exclusive)
- **End:** Latest `questActiveEvent:50` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:50` |
| Target | soil machine logs related to dungeon floor 3 and 4 |


---

## Analytics Script

```js
// Unit 4, Point 3 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:50"

const playerId = "<playerId>";

const c_floor3 = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.machine": "1",
  "data.floor": "3"
});

const c_floor4 = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.machine": "1",
  "data.floor": "4"
});

let score = 0;

if (c_floor3 === 1) {
  score += 1;
}

if (c_floor4 === 1) {
  score += 2;
} else if (c_floor4 === 2) {
  score += 1;
}

const color = (score > 1) ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 3 — Production (replay-safe, latest attempt window)
// Trigger eventKey: "questActiveEvent:50"

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:50";

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestTrigger) {
  "yellow";
} else {

  // 2) Previous trigger (attempt boundary)
  const prevTrigger = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: TRIGGER_KEY,
      _id: { $lt: latestTrigger._id }
    },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = prevTrigger
    ? prevTrigger._id
    : ObjectId("000000000000000000000000");

  const windowEndId = latestTrigger._id;

  // 3) Count soilMachine interactions inside attempt window

  const c_floor3 = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.machine": "1",
    "data.floor": "3",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const c_floor4 = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.machine": "1",
    "data.floor": "4",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  let score = 0;

  if (c_floor3 === 1) {
    score += 1;
  }

  if (c_floor4 === 1) {
    score += 2;
  } else if (c_floor4 === 2) {
    score += 1;
  }

  score > 1 ? "green" : "yellow";
}
```

---

## Reason Codes

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questActiveEvent:50` has not been logged.

### SCORE_BELOW_THRESHOLD

**Quantities:** `score`, `floor3_attempts`, `floor4_attempts`

**Determination:** The combined score from floor 3 and floor 4 soil machine interactions is 1 or less.

#### TOO_MANY_ATTEMPTS_3

**Short Description:** The student interacted with the soil-type machines within the dungeon on the third floor too many times.

**Instructor Message:** The optimal interaction number is only one interaction. So, if the student interacted only one time for the machine the score will gain 1; If the student interacted with the machine more than once, then the score will not gain. Since the student interacted with the soil-type machines for {attempt_number}, which is more than the optimal attempt, they cannot gain the full score for this floor.

**Determination:** Wether the machine interaction time on the third floor, `floor3_attempts`, is more than once.

**Teacher Guidance:** Remind students that water moves through different soils at different rates. Water will move fastest through sand, and slowest through clay. Water moves through sand at a slower rate than gravel and a faster rate than clay.

#### TOO_MANY_ATTEMPTS_4

**Short Description:** The student interacted with the soil-type machines within the dungeon on the fourth floor too many times.

**Instructor Message:** The optimal interaction number is only one interaction. So, if the student interacted only one time for the machine the score will further gain 2; If the student interacted with the machine twice, then the score will further gain 1; otherwise the score for this floor is 0. Since the student interacted with the soil-type machines for {attempt_number}, which is more than the optimal attempt, they cannot gain the full score for this floor.

**Determination:** Wether the machine interaction time on the fourth floor, `floor4_attempts`, is more than once.

**Teacher Guidance:** Remind students that water moves through different soils at different rates. Water will move fastest through sand, and slowest through clay. Water moves through sand at a slower rate than gravel and a faster rate than clay.

#### Analytics-Matching Script (MongoDB/JS)




