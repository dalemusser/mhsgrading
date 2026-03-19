# Unit 5 Point 4 Grading

**Activity:** Water Problems Require Water Solutions

**Trigger(Start) Event:** `questFinishEvent:44`
**Trigger(End) Event:** `questFinishEvent:45`

---

## Grading Rule

This progress point is a number-based progress. Firstly, it will check whether the plan is correctly figured out - (`DialogueNodeEvent:106:35`) - if we don't find the record within the players' event, then the color will return yellow; then it will check if the total number of following dialogues (`DialogueNodeEvent:106:4`,`DialogueNodeEvent:106:25`,`DialogueNodeEvent:106:26`,`DialogueNodeEvent:106:27`,`DialogueNodeEvent:106:28`,`DialogueNodeEvent:106:29`,`DialogueNodeEvent:106:30`,`DialogueNodeEvent:106:31`,`DialogueNodeEvent:106:32`,`DialogueNodeEvent:106:33`,`DialogueNodeEvent:106:34`) happened is euqal to 0 then the color returns green, otherwise it will return yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | have `DialogueNodeEvent:106:35` and number = 0 |
| **Yellow** | no `DialogueNodeEvent:106:35` or number > 0 or both |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:44` (exclusive)
- **End:** Latest `questFinishEvent:45` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:44` |
| Target | `DialogueNodeEvent:106:35` |
| Target | `DialogueNodeEvent:106:4` |
| Target | `DialogueNodeEvent:106:25` |
| Target | `DialogueNodeEvent:106:26` |
| Target | `DialogueNodeEvent:106:27` |
| Target | `DialogueNodeEvent:106:28` |
| Target | `DialogueNodeEvent:106:29` |
| Target | `DialogueNodeEvent:106:30` |
| Target | `DialogueNodeEvent:106:31` |
| Target | `DialogueNodeEvent:106:32` |
| Target | `DialogueNodeEvent:106:33` |
| Target | `DialogueNodeEvent:106:34` |

---

## Analytics Script

```js
// Unit 5, Point 4 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:45"

const playerId = "<playerId>";

const SUCCESS_KEY = "DialogueNodeEvent:106:35";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:106:4",
  "DialogueNodeEvent:106:25",
  "DialogueNodeEvent:106:26",
  "DialogueNodeEvent:106:27",
  "DialogueNodeEvent:106:28",
  "DialogueNodeEvent:106:29",
  "DialogueNodeEvent:106:30",
  "DialogueNodeEvent:106:31",
  "DialogueNodeEvent:106:32",
  "DialogueNodeEvent:106:33",
  "DialogueNodeEvent:106:34"
];

const has_success =
  db.logdata.findOne(
    {
      playerId: playerId,
      eventKey: SUCCESS_KEY
    }
  ) !== null;

let color;

if (!has_success) {
  color = "yellow";
} else {
  const cnt = db.logdata.countDocuments({
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS }
  });

  color = (cnt === 0) ? "green" : "yellow";
}

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe color script
// Window start: previous questFinishEvent:44 (exclusive)
// Window end:   latest questFinishEvent:45 (inclusive)

const playerId = "<playerId>";

const START_KEY = "questFinishEvent:44";
const END_KEY = "questFinishEvent:45";
const SUCCESS_KEY = "DialogueNodeEvent:106:35";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:106:4",
  "DialogueNodeEvent:106:25",
  "DialogueNodeEvent:106:26",
  "DialogueNodeEvent:106:27",
  "DialogueNodeEvent:106:28",
  "DialogueNodeEvent:106:29",
  "DialogueNodeEvent:106:30",
  "DialogueNodeEvent:106:31",
  "DialogueNodeEvent:106:32",
  "DialogueNodeEvent:106:33",
  "DialogueNodeEvent:106:34"
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: END_KEY
  },
  { sort: { _id: -1 }}
);

if (!latestEnd) {
  "yellow";
} else {
  // 2) Previous start anchor before latest end
  const prevStart = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: START_KEY,
      _id: { $lt: latestEnd._id }
    },
    { sort: { _id: -1 }}
  );

  const windowStartId = prevStart
    ? prevStart._id
    : ObjectId("000000000000000000000000");

  const windowEndId = latestEnd._id;

  // 3) Check success node inside window
  const has_success =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: SUCCESS_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (!has_success) {
    "yellow";
  } else {
    // 4) Count negative nodes inside window
    const cnt = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: NEGATIVE_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    });

    cnt === 0 ? "green" : "yellow";
  }
}
```

---

## Reason Codes

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questFinishEvent:45` has not been logged.

### MISSING_SUCCESS_NODE

**Short Description:** Student did not figure out the correct water solution plan.

**Instructor Message:** The student did not reach the expected success outcome (`DialogueNodeEvent:106:35`), indicating they did not correctly identify the water solution plan.

**Determination:** The success node `DialogueNodeEvent:106:35` is absent from the attempt window.

**Teacher Guidance:** Review atmospheric water and the water cycle with the student. Discuss how water problems in the game scenario connect to real-world water solutions.

### TOO_MANY_NEGATIVES

**Short Description:** Student made incorrect selections while constructing the water solution.

**Instructor Message:** The student made {negativeCount} incorrect selections during the water solution activity. The threshold for success is zero incorrect selections — the student must select the correct plan without errors.

**Quantities:** `negativeCount` — count of negative dialogue events

**Determination:** Any of the negative dialogue nodes (`DialogueNodeEvent:106:4`, `106:25`-`106:34`) are present in the attempt window. Zero tolerance — any incorrect selection results in yellow.

**Teacher Guidance:** Review the water cycle concepts covered in Unit 5 with the student. Discuss how the evidence gathered throughout the unit should inform the final solution plan.