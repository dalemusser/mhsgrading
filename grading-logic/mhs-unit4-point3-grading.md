# Unit 4 Point 3 Grading

**Activity:** Alien Well Floor 3 & 4

**Trigger(Start) Event:** `questActiveEvent:48`
**Trigger(End) Event:** `questActiveEvent:50`

---

## Grading Rule

This progress point will check how many times the player interacts with the soil machines on the third and forth floors within the alien dungeon. Depending on the number of attempts, a score will calculated. Basically the score will increase one if the player just interacted with the machine on the third floor at the first attempt to figure out the right type, otherwise zero. For the forth floor, if the player interacts with the machine once to figure the correct type then further increase two; if the interaction time is two then further increase 1; otherwise no further score increased.

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

If the color truns out to be yellow then depending on which condition(s) described below was reached, we decided which reaon codes to show on the pup-up message.

### SCORE_BELOW_THRESHOLD

**Instructor Message:** In the Alien Well (floors 3 and 4), the student changed the soil-type canisters {floor3_attempts} times on the third-floor machine and {floor4_attempts} times on the fourth-floor machine. This point earns green only when the fourth-floor machine is set correctly on the first try, or on the second try with the third floor solved in one. Many canister changes may indicate the student was cycling through soil types rather than predicting which soil matches the floor's water-flow requirement - water passes fastest through gravel, more slowly through sand, slowest through clay, and not at all through bedrock.

#### Corresponding Script

```js
// U4P3: SCORE_BELOW_THRESHOLD — determine trigger and per-floor counts
// Window mirrors the production color script: trigger-to-trigger on
// questActiveEvent:50 (previous occurrence exclusive, latest inclusive).
// Score: floor3==1 -> +1; floor4==1 -> +2, floor4==2 -> +1; yellow when <= 1.
// Counts are soilMachine ChangeCanister interactions on machine "1"
// (data.floor/machine are strings; floor 5 has a machine "2", excluded).

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:50";

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestTrigger) {
  ({ triggered: false, floor3_attempts: 0, floor4_attempts: 0 });
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

  const windowStartId = prevTrigger ? prevTrigger._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  // 3) Per-floor interaction counts inside the window
  const floor3 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventType: "soilMachine",
    "data.machine": "1",
    "data.floor": "3",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const floor4 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventType: "soilMachine",
    "data.machine": "1",
    "data.floor": "4",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // 4) Mirror the color formula exactly
  let score = 0;
  if (floor3 === 1) score += 1;
  if (floor4 === 1) score += 2;
  else if (floor4 === 2) score += 1;

  ({ triggered: score <= 1, floor3_attempts: floor3, floor4_attempts: floor4 });
}
```

### Teacher Guidance 
Remind students that water moves through different soils at different rates. Water will move fastest through sand, and slowest through clay. Water moves through sand at a slower rate than gravel and a faster rate than clay.

