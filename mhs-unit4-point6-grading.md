# Unit 4 Point 6 Grading

**Activity:** Desert Delicacies

**Trigger(Start) Event:** `questActiveEvent:41`
**Trigger(End) Event:** `questFinishEvent:56`

---

## Grading Rule

This is a score-based progress point. There are three garden boxes, each time when the player places the camera on the correct soil type then the score will add one. In box 0, if the latest camera placement is gravel, then the score adds one; in box 1, if the latest camera placement is sand, then the score adds another one; in box 2, if the latest camera placement is clay, then the score further adds one. If the score is equal to or larger than 2, then the color turns to green; otherwise the color returns yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | The score >= 2 |
| **Yellow** | The score < 2 |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:41` (exclusive)
- **End:** Latest `questFinishEvent:56` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:56` |
| Target | TerasGardenBox |

---

## Analytics Script

```js
// Unit 4, Point 6 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:56"

const playerId = "<playerId>";

let score = 0;

// Latest placement for Box 0
const latestBox0 = db.logdata.findOne(
  {
    playerId: playerId,
    eventType: "TerasGardenBox",
    "data.actionType": "cameraPlaced",
    "data.boxId": "0"
  },
  {
    sort: { _id: -1 }
  }
);

if (latestBox0 && latestBox0.data && latestBox0.data.soilType === "Gravel") {
  score += 1;
}

// Latest placement for Box 1
const latestBox1 = db.logdata.findOne(
  {
    playerId: playerId,
    eventType: "TerasGardenBox",
    "data.actionType": "cameraPlaced",
    "data.boxId": "1"
  },
  {
    sort: { _id: -1 }
  }
);

if (latestBox1 && latestBox1.data && latestBox1.data.soilType === "Sand") {
  score += 1;
}

// Latest placement for Box 2
const latestBox2 = db.logdata.findOne(
  {
    playerId: playerId,
    eventType: "TerasGardenBox",
    "data.actionType": "cameraPlaced",
    "data.boxId": "2"
  },
  {
    sort: { _id: -1 }
  }
);

if (latestBox2 && latestBox2.data && latestBox2.data.soilType === "Clay") {
  score += 1;
}

const color = (score >= 2) ? "green" : "yellow";

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe TerasGardenBox scoring
// Window start: "questActiveEvent:41"
// Window end:   "questFinishEvent:56"

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:41";
const WINDOW_END_KEY = "questFinishEvent:56";

// 1) Most recent window start
const latestStart = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_START_KEY
  },
  { sort: { _id: -1 }}
);

// 2) Most recent window end
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 }}
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  "yellow";
} else {
  const windowStartId = latestStart._id;
  const windowEndId = latestEnd._id;

  let score = 0;

  // Latest placement for Box 1 within window
  const latestBox1 = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "TerasGardenBox",
      "data.actionType": "cameraPlaced",
      "data.boxId": "0",
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    {
      sort: { _id: -1 }
    }
  );

  if (latestBox1 && latestBox1.data && latestBox1.data.soilType === "Gravel") {
    score += 1;
  }

  // Latest placement for Box 1 within window
  const latestBox2 = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "TerasGardenBox",
      "data.actionType": "cameraPlaced",
      "data.boxId": "1",
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    {
      sort: { _id: -1 }
    }
  );

  if (latestBox2 && latestBox2.data && latestBox2.data.soilType === "Sand") {
    score += 1;
  }

  // Latest placement for Box 2 within window
  const latestBox3 = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "TerasGardenBox",
      "data.actionType": "cameraPlaced",
      "data.boxId": "2",
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    {
      sort: { _id: -1 }
    }
  );

  if (latestBox3 && latestBox3.data && latestBox3.data.soilType === "Clay") {
    score += 1;
  }

  score >= 2 ? "green" : "yellow";
}
```

---

## Reason Codes

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questFinishEvent:56` has not been logged.

### SCORE_BELOW_THRESHOLD

**Short Description:** Student placed incorrect soil types in the garden boxes.

**Instructor Message:** The student placed the correct soil type in {score} out of 3 garden boxes. The threshold for success is at least 2 out of 3 correct placements.

**Quantities:** `score`, `details` (e.g., "1/3 correct")

**Determination:** The count of garden boxes with the correct latest soil placement is less than 2. Expected placements: Box 0 = Gravel, Box 1 = Sand, Box 2 = Clay.

**Teacher Guidance:** Review soil types and their water-holding properties with the student. Discuss which soil types are best suited for different plants based on water retention characteristics.
