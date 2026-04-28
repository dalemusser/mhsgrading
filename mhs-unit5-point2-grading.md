# Unit 5 Point 1 Grading

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

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `DialogueNodeEvent:96:1` has not been logged.

### SCORE_BELOW_THRESHOLD

**Determination:** The combined score from floor 3 and floor 4 water chamber interactions is less than 3.

**Quantities:** `score`, `floor3_attempts`, `floor4_attempts`

#### TOO_MANY_ATTEMPTS_3

**Short Description:** The students interacted with the condenser and evaporator machines  too many times on the 3rd floor to solve the puzzle.

**Instructor Message:** When interacting with the condenser and evaporator machines on the third floor, the student conducted {floor3_attempts} interactions, which surpasses the optimal interaction times, which is 6.

#### TOO_MANY_ATTEMPTS_4

**Short Description:** The students interacted with the condenser and evaporator machines too many times on the 4th floor to solve the puzzle.

**Instructor Message:** When interacting with the condenser and evaporator machines on the fourth floor, the student conducted {floor4_attempts} interactions, which surpasses the optimal interaction times, which is 5.

**Teacher Guidance:** Remind students that condensation is the phase change that occurs when energy is removed from a gas to turn it into a liquid. Have students work through Unit 5 followup activity.

#### Analytics-Matching Script (MongoDB/JS)