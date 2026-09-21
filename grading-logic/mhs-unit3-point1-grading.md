# Unit 3 Point 1 Grading

**Activity:** Good Morning Cadet + Establishing a Foothold

**Trigger(Start) Event:** `DialogueNodeEvent:10:1`
**Trigger(End) Event:** `DialogueNodeEvent:11:22`

---

## Grading Rule

Count-based rule. The student must have more than one occurrence of the target event to demonstrate understanding of water flow direction.

| Outcome | Condition |
|---------|-----------|
| **Green** | Count of target event > 1 within the attempt window |
| **Yellow** | Count of target event <= 1, or no trigger exists |

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:11:22` (exclusive)
- **End:** Latest `DialogueNodeEvent:11:22` (inclusive)
- The Production Script below bounds the window this way. The Trigger(Start) event in the header marks when the activity begins and drives the dashboard's in-progress state and the duration metrics.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:11:22` |
| Target | `DialogueNodeEvent:10:30` |

---

## Analytics Script

```js
// Unit 3, Point 1 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:11:22"

const playerId = "<playerId>";

const cnt = db.logdata.countDocuments({
  game: "mhs",
  playerId: playerId,
  eventKey: "DialogueNodeEvent:10:30"
});

const color = cnt > 1 ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 1 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:11:22"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:11:22";
const TARGET_KEY = "DialogueNodeEvent:10:30";

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

  // 3) Count target occurrences within attempt window
  const cnt = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: TARGET_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  cnt > 1 ? "green" : "yellow";
}
```

---

## Reason Codes

### EXCESS_WRONG_RIVERS

**Instructor Message:** In Establishing a Foothold, while sending Tera's three supply crates back to her camp by floating them down a river, the student dropped {wrong_river_number} crates into the wrong river. This point earns green only when at most 1 crate goes into the wrong river. Wrong-river choices may indicate difficulty using the watershed map to determine flow direction - water flows from higher to lower elevation toward the ocean, so the correct river is the one that flows past Tera's camp.

#### Corresponding Script

```js
// U3P1: EXCESS_WRONG_RIVERS - determine trigger and wrong_river_number
// Triggers when the color rule goes yellow: fewer than 2 correct-river
// confirmations (10:30) in the attempt window. wrong_river_number counts the
// wrong-river feedback nodes directly (10:31 mid-task, 10:32 last crate).
// Audit invariant: correct + wrong = 3 (three crates, each thrown once).
// The wrong-river keys ALSO fire during the ungraded Morris-Galactic
// bonus-crate segment after this window - never count them unwindowed.

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:11:22";
const CORRECT_KEY = "DialogueNodeEvent:10:30";  // "you picked the right river"

const WRONG_RIVER_KEYS = [
  "DialogueNodeEvent:10:31",  // wrong river, crate lost (crates 1-2)
  "DialogueNodeEvent:10:32"   // wrong river, last crate
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, wrong_river_number: 0 });
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

  // 3) Correct-river confirmations (the color rule's target)
  const correctCount = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: CORRECT_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // 4) Wrong-river selections, counted directly
  const wrongCount = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: WRONG_RIVER_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // 5) Mirror the color rule exactly (green requires correctCount > 1)
  ({ triggered: correctCount <= 1, wrong_river_number: wrongCount });
}
```

### Teacher Guidance
Review watershed maps with students, and ask them to predict flow of water. Remind students that rivers empty into the ocean.
