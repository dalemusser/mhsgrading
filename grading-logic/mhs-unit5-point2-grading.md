# Unit 5 Point 2 Grading

**Activity:** If I Had a Nickel- Floors 3 & 4

**Trigger(Start) Event:** `questFinishEvent:43`
**Trigger(End) Event:** `DialogueNodeEvent:96:1`

---

## Grading Rule

This progress point is a score-based progress, at the beggining the score euquals to 0, if the player solved the puzzle on the third floor by interactig with condenser or evaporator machines within equal to or less than 6, attempts, then the score will add 2; If the interaction attempts on the third floor are larger than 6 but less than 11 attempts, then the score will add 1; interaction attempts larger than 10 times, will let the score add 0; Then the players will continue the puzzle solving on the forth floor, if they solved the puzzle on this floor by interacting with condenser or evaporator machines within equal to or less than 5 attempts, then the score will further add 2; if they solved the puzzle on the forth floor by interacting with condenser or evaporator machines larger than 5 and less than 10 times, then the score will fruther add 1; No further score will be added if the interaction attempts on the forth floor surpass 9 times. If the score is euqal to or larger than 3 then the block color turns to green, otherwise if the score is less than 3 then the block color turns to yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 3 |
| **Yellow** | score < 3 |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:43` (exclusive)
- **End:** Latest `DialogueNodeEvent:96:1` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:96:1` |
| Target | WaterChamberEvent |

---

## Analytics Script

```js
// Unit 5, Point 2 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:96:1"

let score = 0;

const playerId = "<playerId>";
const VALID_TYPES = ["Condenser", "Evaporator"];

// Count relevant interactions on Floor 3
const floor3_attempts = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "WaterChamberEvent",
  "data.floor": "3",
  "data.machineType": { $in: VALID_TYPES }
});

// Count relevant interactions on Floor 4
const floor4_attempts = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "WaterChamberEvent",
  "data.floor": "4",
  "data.machineType": { $in: VALID_TYPES }
});

// Scoring for Floor 3
if (floor3_attempts <= 6) {
  score += 2;
} else if (floor3_attempts < 11) {
  score += 1;
}

// Scoring for Floor 4
if (floor4_attempts <= 5) {
  score += 2;
} else if (floor4_attempts < 10) {
  score += 1;
}

color = (score < 3) ? "yellow" : "green";

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe score calculation for Unit 5 water chamber puzzle
// Window start: "questFinishEvent:43"
// Window end:   "DialogueNodeEvent:96:1"

const playerId = "<playerId>";

const WINDOW_START_KEY = "questFinishEvent:43";
const WINDOW_END_KEY = "DialogueNodeEvent:96:1";
const VALID_TYPES = ["Condenser", "Evaporator"];

// 1) Most recent window start
const latestStart = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_START_KEY
  },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

// 2) Most recent window end
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  "yellow";
} else {
  const windowStartId = latestStart._id;
  const windowEndId = latestEnd._id;

  let score = 0;

  // Count relevant interactions on Floor 3
  const floor3_attempts = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "WaterChamberEvent",
    "data.floor": "3",
    "data.machineType": { $in: VALID_TYPES },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // Count relevant interactions on Floor 4
  const floor4_attempts = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "WaterChamberEvent",
    "data.floor": "4",
    "data.machineType": { $in: VALID_TYPES },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // Scoring for Floor 3
  if (floor3_attempts <= 6) {
    score += 2;
  } else if (floor3_attempts < 11) {
    score += 1;
  }

  // Scoring for Floor 4
  if (floor4_attempts <= 5) {
    score += 2;
  } else if (floor4_attempts < 10) {
    score += 1;
  }

  score < 3 ? "yellow" : "green";
}
```

---

## Reason Codes

### SCORE_BELOW_THRESHOLD

**Instructor Message:** In If I Had a Nickel (floors 3 and 4), the student used {floor3_attempts} condenser and evaporator interactions to solve the third-floor water chamber puzzle and {floor4_attempts} on the fourth floor. This point earns green only when at least one floor is solved within its optimal count (6 interactions on the third floor, 5 on the fourth) and the other stays within its partial range (at most 10 and 9, respectively). Many interactions may indicate trial-and-error switching rather than predicting the phase change each chamber needs — condensation removes energy to turn water vapor into liquid, and evaporation adds energy to turn liquid back into vapor.

#### Corresponding Script

```js
// U5P2: SCORE_BELOW_THRESHOLD — determine trigger and per-floor counts
// Window mirrors the production color script: latest questFinishEvent:43 (start)
// to latest DialogueNodeEvent:96:1 (end). Score: floor3 <=6 -> +2, 7-10 -> +1;
// floor4 <=5 -> +2, 6-9 -> +1; yellow when total < 3.
// VALID_TYPES stays mirror-exact with the color script — note the flagged gap:
// floor 3 also logs DualChamber_Condenser / DualChamber_Evaporator, which are
// currently not counted (add to both scripts once approved). VentSwitch and
// the floors-1/2 events inside this window are excluded by design.

const playerId = "<playerId>";

const WINDOW_START_KEY = "questFinishEvent:43";
const WINDOW_END_KEY = "DialogueNodeEvent:96:1";
const VALID_TYPES = ["Condenser", "Evaporator"];

const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  ({ triggered: false, floor3_attempts: 0, floor4_attempts: 0 });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  const floorCount = (floor) => db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventType: "WaterChamberEvent",
    "data.floor": floor,
    "data.machineType": { $in: VALID_TYPES },
    ...windowFilter
  });

  const floor3 = floorCount("3");
  const floor4 = floorCount("4");

  // Mirror the color formula exactly
  let score = 0;
  if (floor3 <= 6) score += 2;
  else if (floor3 < 11) score += 1;
  if (floor4 <= 5) score += 2;
  else if (floor4 < 10) score += 1;

  ({ triggered: score < 3, floor3_attempts: floor3, floor4_attempts: floor4 });
}
```

### Teacher Guidance 
Remind students that condensation is the phase change that occurs when energy is removed from a gas to turn it into a liquid. Have students work through Unit 5 followup activity.