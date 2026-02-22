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
