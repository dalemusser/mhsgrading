# Unit 1 Point 3 Grading

**Activity:** Defend the Expedition

**Trigger(Start) Event:** `DialogueNodeEvent:30:98`
**Trigger(End) Event:** `questActiveEvent:34`

---

## Grading Rule

Check whether the student needed multiple attempts to build the correct argument.

| Outcome | Condition |
|---------|-----------|
| **Green** | No yellow nodes found within the attempt window |
| **Yellow** | Any yellow node found within the attempt window, or no trigger exists |

### Attempt Window (Production)

- **Start:** `DialogueNodeEvent:30:98` (exclusive)
- **End:** `questActiveEvent:34` (inclusive)

> Without windowing, one early mistake permanently results in yellow. With windowing, a student can replay and earn green on a later attempt.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:34` |
| Yellow | `DialogueNodeEvent:70:25` |

---

## Analytics Script

```js
// Unit 1, Point 3 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:34"
// Success eventKey: "DialogueNodeEvent:70:7"

const playerId = "<playerId>";

const YELLOW_KEYS = [
  "DialogueNodeEvent:70:25"
];

const hasYellow =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: YELLOW_KEYS }
  }) !== null;

const color = hasYellow ? "yellow" : "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 1, Point 3 — Attempt-based standalone production script
// Trigger eventKey: "questActiveEvent:34"

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:34";

const YELLOW_KEYS = [
  "DialogueNodeEvent:70:25"
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
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
    { sort: { _id: -1 } }
  );

  const windowStartId = prevTrigger ? prevTrigger._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  const hasYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: YELLOW_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  hasYellow ? "yellow" : "green";
}
```

---

## Reason Codes

### WRONG_ARG_SELECTED

**Instructor Message:** In Defend the Expedition, the student's first argument submission was incorrect; they built the correct argument on attempt {attempt_number}. This point earns green only when the first submission is correct. The early miss may indicate difficulty identifying which claim is supported by the given evidence and reasoning.

#### Quantitative script

```js
// U1P3: Determine attempt_number for WRONG_ARG_SELECTED
// With windowing for replay support

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:34";

const ATTEMPT_KEYS = [
  "DialogueNodeEvent:70:25",
  "DialogueNodeEvent:70:7"
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  0;
} else {
  // 2) Previous trigger (attempt boundary)
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

  // 3) Count attempt dialogue triggers only inside the window
  const attempts = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: ATTEMPT_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  attempts;
}
```

### Teacher Guidance:
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.
