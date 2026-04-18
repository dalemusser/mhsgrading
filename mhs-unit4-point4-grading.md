# Unit 4 Point 4 Grading

**Activity:** Alien Well Floor 5 + You Know the Drill

**Trigger(Start) Event:** `questActiveEvent:50`
**Trigger(End) Event:** `questActiveEvent:36`

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

- **Start:** Previous `questActiveEvent:50` (exclusive)
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

if (c_m1_top === 1 && c_m1_bottom === 1) {
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

if (success_total > 0 && neg_total === 0) {
  score += 2;
} else if (success_total > 0 && neg_total === 1) {
  score += 1;
}

const color = (score > 2) ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 4 — Production (replay-safe, latest attempt window)
// Window start: latest "questActiveEvent:50"
// Window end:   latest "questActiveEvent:36"

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:50";
const WINDOW_END_KEY = "questActiveEvent:36";

// 1) Find latest window start
const latestStart = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_START_KEY
  },
  { sort: { _id: -1 } }
);

// 2) Find latest window end
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 } }
);

if (!latestStart || !latestEnd || latestEnd._id <= latestStart._id) {
  "yellow";
} else {
  const windowStartId = latestStart._id;
  const windowEndId = latestEnd._id;

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

  if (c_m1_top === 1 && c_m1_bottom === 1) {
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

  if (success_total > 0 && neg_total === 0) {
    score += 2;
  } else if (success_total > 0 && neg_total === 1) {
    score += 1;
  }

  score > 2 ? "green" : "yellow";
}
```

---

## Reason Codes

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questActiveEvent:36` has not been logged.

### SCORE_BELOW_THRESHOLD

**Short Description:** Student needed too many attempts on the floor 5 soil machines and/or dialogue selections.

**Instructor Message:** The student's score was below the expected threshold. The score is based on three components: (1) efficient interaction with the two-layer machine on floor 5 (+1 if top row solved in one attempt with no bottom row interactions), (2) efficient interaction with the one-layer machine on floor 5 (+1 if solved in one attempt), and (3) correct dialogue choices (+2 if correct on first attempt, +1 if correct within two attempts). A score greater than 2 is required.

**Quantities:** `score`

**Determination:** The combined score from soil machine interactions and dialogue choices is 2 or less.

**Teacher Guidance:** Review groundwater concepts with the student, particularly how soil layers interact and how to apply that understanding to identify the correct soil type. Also review the dialogue choices related to drilling and well construction.
