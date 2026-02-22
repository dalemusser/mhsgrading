# Unit 3 Point 4 Grading

**Activity:** Forsaken Facility

**Trigger Event:** `DialogueNodeEvent:73:200`

---

## Grading Rule

Gate + score-based rule. First, the student must have the gate event (78:24). Then, count target events and compute a score.

| Outcome | Condition |
|---------|-----------|
| **Green** | Gate present AND score > 0 (i.e. target count <= 2) |
| **Yellow** | Gate missing OR score == 0 (i.e. target count >= 3), or no trigger exists |

### Score from Target Count

| total_count | score |
|-------------|-------|
| 0           | 2     |
| 1-2         | 1     |
| >= 3        | 0     |

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:73:200` (exclusive)
- **End:** Latest `DialogueNodeEvent:73:200` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:73:200` |
| Gate (required) | `DialogueNodeEvent:78:24` |
| Target | `DialogueNodeEvent:78:3` |
| Target | `DialogueNodeEvent:78:4` |
| Target | `DialogueNodeEvent:78:7` |
| Target | `DialogueNodeEvent:78:9` |
| Target | `DialogueNodeEvent:78:10` |
| Target | `DialogueNodeEvent:78:12` |
| Target | `DialogueNodeEvent:78:18` |
| Target | `DialogueNodeEvent:78:23` |

---

## Analytics Script

```js
// Unit 3, Point 4 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:73:200"

const playerId = "<playerId>";

const TARGET_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

// Gate: must have 78:24
const has7824 =
  db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:78:24" },
    { projection: { _id: 1 } }
  ) !== null;

if (!has7824) {
  "yellow";
} else {
  const totalCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: TARGET_KEYS }
  });

  let score;
  if (totalCount === 0) score = 2;
  else if (totalCount <= 2) score = 1;
  else score = 0;

  score === 0 ? "yellow" : "green";
}
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 4 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:73:200"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:73:200";

const TARGET_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
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

  // Gate: must have 78:24 within attempt window
  const has7824 =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: "DialogueNodeEvent:78:24",
        _id: { $gt: windowStartId, $lte: windowEndId }
      },
      { projection: { _id: 1 } }
    ) !== null;

  if (!has7824) {
    "yellow";
  } else {
    const totalCount = db.logdata.countDocuments({
      game: "mhs", playerId: playerId,
      eventKey: { $in: TARGET_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    });

    let score;
    if (totalCount === 0) score = 2;
    else if (totalCount <= 2) score = 1;
    else score = 0;

    score === 0 ? "yellow" : "green";
  }
}
```

---

## Reason Codes

> No reason codes defined for this point.
