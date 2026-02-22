# Unit 2 Point 4 Grading

**Activity:** Investigate the Temple

**Trigger Event:** `DialogueNodeEvent:23:17`

---

## Grading Rule

Student must complete the watershed-flow matching independently and solve the glyph puzzle without excessive attempts.

| Outcome | Condition |
|---------|-----------|
| **Green** | Success node present AND no bad feedback nodes in attempt window |
| **Yellow** | Success node missing OR any bad feedback node present |

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:23:17` (exclusive)
- **End:** Latest `DialogueNodeEvent:23:17` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:23:17` |
| Success | `DialogueNodeEvent:74:21` |
| Bad Feedback | `DialogueNodeEvent:74:16` |
| Bad Feedback | `DialogueNodeEvent:74:17` |
| Bad Feedback | `DialogueNodeEvent:74:20` |
| Bad Feedback | `DialogueNodeEvent:74:22` |

---

## Reason Codes

| Code | Short Description | Teacher Guidance |
|------|-------------------|------------------|
| MISSING_SUCCESS_NODE | Did not complete watershed-flow matching independently | Review the relationship between watershed size and flow rate. |
| TOO_MANY_NEGATIVES | Too many attempts on watershed-flow glyph puzzle | Review the relationship between watershed size and flow rate. |

---

## Analytics Script

```js
// Unit 2, Point 4 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:23:17"

const playerId = "<playerId>";

const successKey = "DialogueNodeEvent:74:21";

const badKeys = [
  "DialogueNodeEvent:74:16",
  "DialogueNodeEvent:74:17",
  "DialogueNodeEvent:74:20",
  "DialogueNodeEvent:74:22"
];

const hasSuccess =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: successKey
  }) !== null;

const hasBadFeedback =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: badKeys }
  }) !== null;

const color =
  hasSuccess && !hasBadFeedback
    ? "green"
    : "yellow";

color;
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 4 — Standalone replay-aware grading (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:23:17"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:17";

const successKey = "DialogueNodeEvent:74:21";
const badKeys = [
  "DialogueNodeEvent:74:16",
  "DialogueNodeEvent:74:17",
  "DialogueNodeEvent:74:20",
  "DialogueNodeEvent:74:22"
];

// 1) Latest trigger
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  "yellow";
} else {
  // 2) Previous trigger (defines prior attempt boundary)
  const prevTrigger = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY, _id: { $lt: latestTrigger._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = prevTrigger ? prevTrigger._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  // 3) Check success/bad within this attempt window
  const hasSuccess =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: successKey,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  const hasBad =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: badKeys },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  hasSuccess && !hasBad ? "green" : "yellow";
}
```
