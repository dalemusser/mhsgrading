# Unit 3 Point 1 Grading

**Activity:** Good Morning Cadet + Establishing a Foothold

**Trigger Event:** `questFinishEvent:17`

---

## Grading Rule

Count-based rule. The student must have more than one occurrence of the target event to demonstrate understanding of water flow direction.

| Outcome | Condition |
|---------|-----------|
| **Green** | Count of target event > 1 within the attempt window |
| **Yellow** | Count of target event <= 1, or no trigger exists |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:17` (exclusive)
- **End:** Latest `questFinishEvent:17` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:17` |
| Target | `DialogueNodeEvent:10:30` |

---

## Analytics Script

```js
// Unit 3, Point 1 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:17"

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
// Trigger eventKey: "questFinishEvent:17"

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:17";
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

### TOO_MANY_NEGATIVES

**Short Description:** Too many wrong river selections.

**Instructor Message:** The student selected {attempt_number} times of the wrong river during the activity of sending Tera’s crates back to her by identifying the direction of water flow based on a map of the watershed. The threshold for success is not to select the wrong river equal to 2 or more than 2 times.

**Quantities:** `attempt_number` — count of wrong river selected.

**Teacher Guidance:**
Review watershed maps with students, and ask them to predict flow of water. Remind students that rivers empty into the ocean.

### Reason Quantity Scripts

#### Data Analytics Script (Python)
```python
# U3P1: Determine attempt_number for TOO_MANY_NEGATIVES
# Count the number of wrong-reiver selection dialogues triggered

count  = 3 - coll.count_documents({"playerId": pid, "eventKey": "DialogueNodeEvent:10:30"})

count
```

#### Analytics-Matching Script (MongoDB/JS)
```js
// U3P1: Determine attempt_number for TOO_MANY_NEGATIVES
// Exact match to data analytics script

const playerId = "<playerId>";

const count =
  3 - db.logdata.countDocuments({
        playerId: playerId,
        eventKey: "DialogueNodeEvent:10:30"
      });

count;
```

#### Production Script (Attempt-Based, MongoDB/JS)
```js
// U2P3: Determine triggering_number for BAD_FEEDBACK
// With windowing for replay support

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:17";
const TARGET_KEY = "DialogueNodeEvent:10:30";

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let wrongCount = null;

if (!latestTrigger) {
  wrongCount = null;
} else {
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

  const cnt = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: TARGET_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  wrongCount = Math.max(0, 3 - cnt);
}

wrongCount;
```


