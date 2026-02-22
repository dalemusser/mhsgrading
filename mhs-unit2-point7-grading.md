# Unit 2 Point 7 Grading

**Activity:** Which Watershed? Part II

**Trigger Event:** `questFinishEvent:54`

---

## Grading Rule

Student must successfully build the watershed argument with limited incorrect evidence selections.

| Outcome | Condition |
|---------|-----------|
| **Green** | Success key present AND neg_count <= 3 in attempt window |
| **Yellow** | Success key missing OR neg_count > 3, or no trigger exists |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:54` (exclusive)
- **End:** Latest `questFinishEvent:54` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:54` |
| Success | `DialogueNodeEvent:27:7` |

**Negative Keys (incorrect evidence selections):**

`DialogueNodeEvent:27:11` through `DialogueNodeEvent:27:30` (20 keys)

<details>
<summary>Full list</summary>

- `DialogueNodeEvent:27:11`
- `DialogueNodeEvent:27:12`
- `DialogueNodeEvent:27:13`
- `DialogueNodeEvent:27:14`
- `DialogueNodeEvent:27:15`
- `DialogueNodeEvent:27:16`
- `DialogueNodeEvent:27:17`
- `DialogueNodeEvent:27:18`
- `DialogueNodeEvent:27:19`
- `DialogueNodeEvent:27:20`
- `DialogueNodeEvent:27:21`
- `DialogueNodeEvent:27:22`
- `DialogueNodeEvent:27:23`
- `DialogueNodeEvent:27:24`
- `DialogueNodeEvent:27:25`
- `DialogueNodeEvent:27:26`
- `DialogueNodeEvent:27:27`
- `DialogueNodeEvent:27:28`
- `DialogueNodeEvent:27:29`
- `DialogueNodeEvent:27:30`

</details>

---

## Reason Codes

| Code | Short Description | Teacher Guidance |
|------|-------------------|------------------|
| WRONG_ARG_SELECTED | Too many attempts to select evidence to support the claim | Review parts of claim and evidence with student: 1. Claim: statement that answers the driving question. 2. Evidence: scientific data and facts that support your claim. |

---

## Analytics Script

```js
// Unit 2, Point 7 — Analytics-matching script (lifetime)
// Trigger eventKey: "questFinishEvent:54"

const playerId = "<playerId>";

const SUCCESS_KEY = "DialogueNodeEvent:27:7";

const NEG_KEYS = [
  "DialogueNodeEvent:27:11", "DialogueNodeEvent:27:12", "DialogueNodeEvent:27:13", "DialogueNodeEvent:27:14",
  "DialogueNodeEvent:27:15", "DialogueNodeEvent:27:16", "DialogueNodeEvent:27:17", "DialogueNodeEvent:27:18",
  "DialogueNodeEvent:27:19", "DialogueNodeEvent:27:20", "DialogueNodeEvent:27:21", "DialogueNodeEvent:27:22",
  "DialogueNodeEvent:27:23", "DialogueNodeEvent:27:24", "DialogueNodeEvent:27:25", "DialogueNodeEvent:27:26",
  "DialogueNodeEvent:27:27", "DialogueNodeEvent:27:28", "DialogueNodeEvent:27:29", "DialogueNodeEvent:27:30"
];

const hasSuccess =
  db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: SUCCESS_KEY
  }) !== null;

const negCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: NEG_KEYS }
});

const color = hasSuccess && negCount <= 3 ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 7 — Attempt-based standalone production grading script
// Trigger eventKey: "questFinishEvent:54"

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:54";
const SUCCESS_KEY = "DialogueNodeEvent:27:7";

const NEG_KEYS = [
  "DialogueNodeEvent:27:11", "DialogueNodeEvent:27:12", "DialogueNodeEvent:27:13", "DialogueNodeEvent:27:14",
  "DialogueNodeEvent:27:15", "DialogueNodeEvent:27:16", "DialogueNodeEvent:27:17", "DialogueNodeEvent:27:18",
  "DialogueNodeEvent:27:19", "DialogueNodeEvent:27:20", "DialogueNodeEvent:27:21", "DialogueNodeEvent:27:22",
  "DialogueNodeEvent:27:23", "DialogueNodeEvent:27:24", "DialogueNodeEvent:27:25", "DialogueNodeEvent:27:26",
  "DialogueNodeEvent:27:27", "DialogueNodeEvent:27:28", "DialogueNodeEvent:27:29", "DialogueNodeEvent:27:30"
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

  const hasSuccess =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: SUCCESS_KEY,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  (hasSuccess && negCount <= 3) ? "green" : "yellow";
}
```
