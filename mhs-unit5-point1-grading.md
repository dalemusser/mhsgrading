# Unit 5 Point 1 Grading

**Activity:** If I Had a Nickel- Floors 1 & 2

**Trigger(Start) Event:** `questActiveEvent:43`
**Trigger(End) Event:** `questFinishEvent:43`

---

## Grading Rule

This progress point is a attempt-based progress, if the player solved the puzzle (triggered `DialogueNodeEvent:100:44`) at the first attempt, then they will gain all 2 points; If the player solved the puzzle within 3 attempts, triggered `DialogueNodeEvent:100:44` without triggering any of the following bad feedbacks (`DialogueNodeEvent:100:38`, `DialogueNodeEvent:100:39`, `DialogueNodeEvent:100:43`); Either of the above behavior will return green; Anything else will return yellow. 

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 1 |
| **Yellow** | score < 1 |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:43` (exclusive)
- **End:** Latest `questFinishEvent:43` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:43` |
| Target | `DialogueNodeEvent:100:44` |
| Target | `DialogueNodeEvent:100:38` |
| Target | `DialogueNodeEvent:100:39` |
| Target | `DialogueNodeEvent:100:43` |

---

## Analytics Script

```js
// Unit 5, Point 1 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:43"

const playerId = "<playerId>";

const POS_KEYS = ["DialogueNodeEvent:100:44"];
const NEG_KEYS = [
  "DialogueNodeEvent:100:38",
  "DialogueNodeEvent:100:39",
  "DialogueNodeEvent:100:43"
];

const has_trigger =
  db.logdata.findOne(
    {
      playerId: playerId,
      eventKey: { $in: POS_KEYS }
    }
  ) !== null;

let color;

if (!has_trigger) {
  color = "yellow";
} else {
  const cnt = db.logdata.countDocuments({
    playerId: playerId,
    eventKey: { $in: NEG_KEYS }
  });

  color = (cnt > 2) ? "yellow" : "green";
}

color;
```

## Production Script (Attempt-Based)

```js
// Unit 5, Point 1 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "questActiveEvent:39"

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:43";
const WINDOW_END_KEY = "questFinishEvent:43";

const POS_KEY = "DialogueNodeEvent:100:44";
const NEG_KEYS = [
  "DialogueNodeEvent:100:38",
  "DialogueNodeEvent:100:39",
  "DialogueNodeEvent:100:43"
];

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

  // 3) Check success inside window
  const hasTrigger =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: POS_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (!hasTrigger) {
    "yellow";
  } else {
    // 4) Count negative feedback inside window
    const cnt = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: NEG_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    });

    cnt > 2 ? "yellow" : "green";
  }
}
```

---

## Reason Codes

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questFinishEvent:43` has not been logged.

### MISSING_SUCCESS_NODE

**Short Description:** Student did not solve the water chamber puzzle on floors 1 and 2.

**Instructor Message:** The student did not reach the expected success outcome (`DialogueNodeEvent:100:44`) for the water chamber puzzle on floors 1 and 2.

**Determination:** The success node `DialogueNodeEvent:100:44` is absent from the attempt window.

**Teacher Guidance:** Review the water chamber puzzle mechanics with the student. Discuss how condensation and evaporation processes work and how to apply that understanding to solve the puzzle.

### BAD_FEEDBACK

**Short Description:** The student received too much negative feedback before solving the glyph puzzle.

**Instructor Message:** Students received totally {negative_feedback_number} negative feedback, which surpasses the threshold of two times, before solving the puzzle.

**Quantities:** `negative_feedback_number` — count of negative feedback events

**Determination:** The count of negative feedback nodes (`DialogueNodeEvent:100:38`, `DialogueNodeEvent:100:39`, `DialogueNodeEvent:100:43`) exceeds 2 in the attempt window.

**Teacher Guidance:** Remind students that evaporation  is the phase change that occurs when energy is added to liquid to turn it into a gas Have students work through Unit 5 followup activity.

#### Analytics-Matching Script (MongoDB/JS)