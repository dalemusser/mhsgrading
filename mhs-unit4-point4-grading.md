# Unit 4 Point 4 Grading

**Activity:** Alien Well Floor 5 + You Know the Drill

**Trigger Event:** `questActiveEvent:36`

---

## Grading Rule

This progress point is score based. There are two tasks under this progress point. The first task is to check how many times the player interact with the two-layer machine and another one-layer machine on the fifth floor.
if they interacted with the top machine with one time and the bottom machine with zero time then the score gain once, otherwise zero;
if they interacted with the one-layer machine only once to figure out the correct answer, then the score further gains one; otherwise gain zero;
The next task is to select the correct dialogue choice. If the player select correct choice at the first attempt individually then the score gains two; if the player figures out the correct answer by themselves within two attemts individually then the score further gains one; otherwise no further score gain.
Finally, if the aggregated score is larger than 2 then the color is green; otherwise the color is yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | score > 2 |
| **Yellow** | score <= 2 |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:36` (exclusive)
- **End:** Latest `questActiveEvent:36` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:36` |
| Target | soil machine logs related to dungeon floor 5 |
| Target | `DialogueNodeEvent:107:4` |
| Target | `DialogueNodeEvent:107:5` |
| Target | `DialogueNodeEvent:107:2` |
| Target | `DialogueNodeEvent:107:3` |
| Target | `DialogueNodeEvent:107:6` |


---

## Analytics Script

```js
// Unit 4, Point 4 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:36"

const playerId = "<playerId>";

let score = 0;

const c_m1_top = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.floor": "5",
  "data.machine": "1",
  "data.row": "TopRow"
});

const c_m1_bottom = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.floor": "5",
  "data.machine": "1",
  "data.row": "BottomRow"
});

if (c_m1_top === 1 && c_m1_bottom === 0) {
  score += 1;
}

const c_m2_floor5 = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.floor": "5",
  "data.machine": "2"
});

if (c_m2_floor5 === 1) {
  score += 1;
}

const SUCCESS_KEYS = ["DialogueNodeEvent:107:4", "DialogueNodeEvent:107:5"];
const NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:6"];

const success_total = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: SUCCESS_KEYS }
});

const neg_total = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: NEG_KEYS }
});

if (success_total === 1 && neg_total === 0) {
  score += 2;
} else if (success_total === 1 && neg_total === 1) {
  score += 1;
}

const color = (score > 2) ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 4 — Production (replay-safe, latest attempt window)
// Trigger eventKey: "questActiveEvent:36"

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:36";

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

if (!latestTrigger) {
  "yellow";
} else {
  const prevTrigger = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: TRIGGER_KEY,
      _id: { $lt: latestTrigger._id }
    },
    { sort: { _id: -1 }}
  );

  const windowStartId = prevTrigger ? prevTrigger._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  let score = 0;

  const c_m1_top = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.floor": "5",
    "data.machine": "1",
    "data.row": "TopRow",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const c_m1_bottom = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.floor": "5",
    "data.machine": "1",
    "data.row": "BottomRow",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  if (c_m1_top === 1 && c_m1_bottom === 0) {
    score += 1;
  }

  const c_m2_floor5 = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.floor": "5",
    "data.machine": "2",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  if (c_m2_floor5 === 1) {
    score += 1;
  }

  const SUCCESS_KEYS = ["DialogueNodeEvent:107:4", "DialogueNodeEvent:107:5"];
  const NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:6"];

  const success_total = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: SUCCESS_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const neg_total = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  if (success_total === 1 && neg_total === 0) {
    score += 2;
  } else if (success_total === 1 && neg_total === 1) {
    score += 1;
  }

  score > 2 ? "green" : "yellow";
}
```

---

## Reason Codes

> Still figuring out the reason codes
