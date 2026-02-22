# Unit 3 Point 3 Grading

**Activity:** Pollution Argument

**Trigger Event:** `questFinishEvent:18`

---

## Grading Rule

Score-based rule with a bonus. Count incorrect argument selections, compute a base score, then add a bonus point if the student used the backing info panel.

| Outcome | Condition |
|---------|-----------|
| **Green** | total_score >= 3 |
| **Yellow** | total_score < 3, or no trigger exists |

### Score Formula

```
base_score = (see table below based on sum_count)
bonus      = 1 if player used "BackingInfoPanel - Pollution Site Data", else 0
total_score = base_score + bonus
```

### Base Score from Target Count

| sum_count | base_score |
|-----------|------------|
| <= 3      | 3          |
| 4         | 2          |
| 5         | 1          |
| >= 6      | 0          |

### Bonus Condition

Player must have a log entry with:
- `eventType` = `"argumentationToolEvent"`
- `data.toolName` = `"BackingInfoPanel - Pollution Site Data"`

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:18` (exclusive)
- **End:** Latest `questFinishEvent:18` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:18` |

**Target Keys (incorrect argument selections):**

<details>
<summary>Full list (16 keys)</summary>

- `DialogueNodeEvent:84:20`
- `DialogueNodeEvent:84:25`
- `DialogueNodeEvent:84:32`
- `DialogueNodeEvent:84:33`
- `DialogueNodeEvent:84:34`
- `DialogueNodeEvent:84:35`
- `DialogueNodeEvent:84:37`
- `DialogueNodeEvent:84:39`
- `DialogueNodeEvent:84:40`
- `DialogueNodeEvent:84:41`
- `DialogueNodeEvent:84:42`
- `DialogueNodeEvent:84:43`
- `DialogueNodeEvent:84:44`
- `DialogueNodeEvent:84:45`
- `DialogueNodeEvent:84:46`
- `DialogueNodeEvent:84:47`

</details>

**Bonus Event:**

| Field | Value |
|-------|-------|
| eventType | `argumentationToolEvent` |
| data.toolName | `BackingInfoPanel - Pollution Site Data` |

---

## Reason Codes

> No reason codes defined for this point.

---

## Analytics Script

```js
// Unit 3, Point 3 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:18"

const playerId = "<playerId>";

const TARGET_KEYS = [
  "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
  "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40",
  "DialogueNodeEvent:84:41", "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43",
  "DialogueNodeEvent:84:44", "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46",
  "DialogueNodeEvent:84:47"
];

const sumCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: TARGET_KEYS }
});

let baseScore;
if (sumCount <= 3) baseScore = 3;
else if (sumCount === 4) baseScore = 2;
else if (sumCount === 5) baseScore = 1;
else baseScore = 0;

const hasBonus =
  db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "argumentationToolEvent",
      "data.toolName": "BackingInfoPanel - Pollution Site Data"
    },
    { projection: { _id: 1 } }
  ) !== null;

const totalScore = baseScore + (hasBonus ? 1 : 0);
const color = totalScore >= 3 ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 3 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "questFinishEvent:18"

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:18";

const TARGET_KEYS = [
  "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
  "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40",
  "DialogueNodeEvent:84:41", "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43",
  "DialogueNodeEvent:84:44", "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46",
  "DialogueNodeEvent:84:47"
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

  const sumCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: TARGET_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  let baseScore;
  if (sumCount <= 3) baseScore = 3;
  else if (sumCount === 4) baseScore = 2;
  else if (sumCount === 5) baseScore = 1;
  else baseScore = 0;

  const hasBonus =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventType: "argumentationToolEvent",
        "data.toolName": "BackingInfoPanel - Pollution Site Data",
        _id: { $gt: windowStartId, $lte: windowEndId }
      },
      { projection: { _id: 1 } }
    ) !== null;

  const totalScore = baseScore + (hasBonus ? 1 : 0);
  totalScore >= 3 ? "green" : "yellow";
}
```
