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

- **Start:** Latest `questActiveEvent:48` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `questActiveEvent:50` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the previous-and-latest end window (previous `questActiveEvent:50` exclusive .. latest `questActiveEvent:50` inclusive), per the start-and-end window decision (A1). This point has no dialogue keys; re-verified the same day on the logs: every floor-3 / floor-4 `soilMachine` record (machine `"1"`, all `ChangeCanister`, string `floor` / `machine`) lies between the two quest events, so the counts are unchanged. Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `questActiveEvent:48` |
| Trigger (End) | `questActiveEvent:50` |
| Target | `soilMachine` records with `data.machine` = `"1"` and `data.floor` = `"3"` / `"4"` (eventType + data match, not an eventKey) |


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
// Window start: latest questActiveEvent:48 before the end event (exclusive)
// Window end:   latest questActiveEvent:50 (inclusive)

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:48";
const END_KEY = "questActiveEvent:50";

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  "yellow";
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: START_KEY,
      _id: { $lt: latestEnd._id }
    },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowEndId = latestEnd._id;

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

If the color turns out to be yellow then depending on which condition(s) described below was reached, we decide which reason codes to show in the pop-up message.

### SCORE_BELOW_THRESHOLD

**Instructor Message:** In the Alien Well (floors 3 and 4), the student changed the soil-type canisters {floor3_attempts} times on the third-floor machine and {floor4_attempts} times on the fourth-floor machine. This point earns green only when the fourth-floor machine is set correctly on the first try, or on the second try with the third floor solved in one. Many canister changes may indicate the student was cycling through soil types rather than predicting which soil matches the floor's water-flow requirement - water passes fastest through gravel, more slowly through sand, slowest through clay, and not at all through bedrock.

#### Corresponding Script

```js
// U4P3: SCORE_BELOW_THRESHOLD — determine trigger and per-floor counts
// Window mirrors the production color script: latest questActiveEvent:50 (end),
// latest questActiveEvent:48 before it (start, exclusive; zero ObjectId when none).
// Score: floor3==1 -> +1; floor4==1 -> +2, floor4==2 -> +1; yellow when <= 1.
// Counts are soilMachine ChangeCanister interactions on machine "1"
// (data.floor/machine are strings; floor 5 has a machine "2", excluded).

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:48";
const END_KEY = "questActiveEvent:50";

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  ({ triggered: false, floor3_attempts: 0, floor4_attempts: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: START_KEY,
      _id: { $lt: latestEnd._id }
    },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowEndId = latestEnd._id;

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

