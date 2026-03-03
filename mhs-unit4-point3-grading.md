# Unit 4 Point 3 Grading

**Activity:** Alien Well Floor 3 & 4

**Trigger Event:** `questActiveEvent:50`

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

- **Start:** Previous `questActiveEvent:50` (exclusive)
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

> Still figuring out the reason codes
