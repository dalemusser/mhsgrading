# Unit 3 Point 5 Grading

**Activity:** Plant the Superfruit Seeds

**Trigger Event:** `DialogueNodeEvent:10:194`

---

## Grading Rule

Score-based rule using weighted positive and negative counts.

| Outcome | Condition |
|---------|-----------|
| **Green** | sum_score >= 3 |
| **Yellow** | sum_score < 3, or no trigger exists |

### Score Formula

```
pos_score = pos_count * 1.0
neg_score = neg_count * 0.5
sum_score = pos_score - neg_score
```

- `pos_count` = count of `DialogueNodeEvent:73:163`
- `neg_count` = count of events in NEG_KEYS

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:10:194` (exclusive)
- **End:** Latest `DialogueNodeEvent:10:194` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:10:194` |
| Positive | `DialogueNodeEvent:73:163` |
| Negative | `DialogueNodeEvent:73:164` |
| Negative | `DialogueNodeEvent:73:168` |
| Negative | `DialogueNodeEvent:73:171` |

---

## Analytics Script

```js
// Unit 3, Point 5 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:10:194"

const playerId = "<playerId>";

const POS_KEY = "DialogueNodeEvent:73:163";
const NEG_KEYS = ["DialogueNodeEvent:73:164", "DialogueNodeEvent:73:168", "DialogueNodeEvent:73:171"];

const posCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: POS_KEY
});

const negCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: NEG_KEYS }
});

const posScore = posCount * 1.0;
const negScore = negCount * 0.5;
const sumScore = posScore - negScore;

const color = sumScore < 3 ? "yellow" : "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 5 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:10:194"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:10:194";
const POS_KEY = "DialogueNodeEvent:73:163";
const NEG_KEYS = ["DialogueNodeEvent:73:164", "DialogueNodeEvent:73:168", "DialogueNodeEvent:73:171"];

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

  const posCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: POS_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const sumScore = (posCount * 1.0) - (negCount * 0.5);
  sumScore < 3 ? "yellow" : "green";
}
```

---

## Reason Codes

> No reason codes defined for this point.
