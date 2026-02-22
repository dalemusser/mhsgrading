# Unit 2 Point 6 Grading

**Activity:** Which Watershed? Part I

**Trigger Event:** `DialogueNodeEvent:20:46`

---

## Grading Rule

Student must select the correct criterion for determining watershed size on the first try.

| Outcome | Condition |
|---------|-----------|
| **Green** | Pass node present AND no yellow nodes in attempt window |
| **Yellow** | Pass node missing OR any yellow node present |

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:20:35` (exclusive)
- **End:** Latest `DialogueNodeEvent:20:35` (inclusive)

> Note: The production script uses `DialogueNodeEvent:20:35` as the trigger key for windowing.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:20:46` |
| Production Trigger | `DialogueNodeEvent:20:35` |
| Pass (correct choice) | `DialogueNodeEvent:20:43` |
| Yellow (wrong choice) | `DialogueNodeEvent:20:44` |
| Yellow (wrong choice) | `DialogueNodeEvent:20:45` |

---

## Reason Codes

| Code | Short Description | Teacher Guidance |
|------|-------------------|------------------|
| HIT_YELLOW_NODE | Chose an incorrect criterion for watershed size on first try | Review parts of claim and evidence with student: 1. Claim: statement that answers the driving question. 2. Evidence: scientific data and facts that support your claim. |

---

## Analytics Script

```js
// Unit 2, Point 6 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:20:46"

const playerId = "<playerId>";

const passKey = "DialogueNodeEvent:20:43";

const yellowKeys = [
  "DialogueNodeEvent:20:44",
  "DialogueNodeEvent:20:45"
];

const hasPass =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: passKey
  }) !== null;

if (!hasPass) {
  "yellow";
} else {
  const hasYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: yellowKeys }
    }) !== null;

  const color = hasYellow ? "yellow" : "green";
  color;
}
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 6 — Attempt-based standalone production grading script
// Trigger eventKey: "DialogueNodeEvent:20:35"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:20:35";
const PASS_KEY = "DialogueNodeEvent:20:43";
const YELLOW_KEYS = ["DialogueNodeEvent:20:44", "DialogueNodeEvent:20:45"];

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

  // 3) Must have PASS_KEY within attempt window
  const hasPass =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: PASS_KEY,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  if (!hasPass) {
    "yellow";
  } else {
    // 4) Must have none of YELLOW_KEYS within attempt window
    const hasYellow =
      db.logdata.findOne({
        game: "mhs",
        playerId: playerId,
        eventKey: { $in: YELLOW_KEYS },
        _id: { $gt: windowStartId, $lte: windowEndId }
      }) !== null;

    hasYellow ? "yellow" : "green";
  }
}
```
