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

---

## Reason Codes

> This point has multiple possible reasons for a yellow grade. Scripts are needed to determine which reason(s) apply.

### MISSING_SUCCESS_NODE

**Short Description:** Did not complete watershed-flow matching independently

**Instructor Message:** Students didn't figure out the correct match of the watershed size and the flow rate by themselves during the activity of finding Jasper and relating watershed size to flow rate through its main river. One of the successful conditions for this activity is to make correct matches by students themselves.

**Determination:** Check whether the success node (`DialogueNodeEvent:74:21`) is absent.

**Teacher Guidance:** Review the relationship between watershed size and flow rate.

### TOO_MANY_NEGATIVES

**Short Description:** Too many attempts on watershed-flow glyph puzzle

**Instructor Message:** Students tried {attempts_number} attempts to solve the glyph puzzle. The other successful condition is to solve the puzzle within 5 attempts.

**Determination:** Count bad feedback node occurrences; yellow if count > 5.

**Quantities:** `attempts_number` — count of glyph puzzle attempts

**Teacher Guidance:** Review the relationship between watershed size and flow rate.

### Reason Determination Scripts

#### Data Analytics Script (Python)

```python
# U2P4: Determine which reason code(s) apply and compute quantities
# MISSING_SUCCESS_NODE: check if success node (74:21) is absent
# TOO_MANY_NEGATIVES: count attempts_number from bad feedback node occurrences
```

#### Analytics-Matching Script (MongoDB/JS)

```js
// U2P4: Determine which reason code(s) apply and compute quantities
// MISSING_SUCCESS_NODE: check if success node (74:21) is absent
// TOO_MANY_NEGATIVES: count attempts_number from bad feedback node occurrences
// Exact match to data analytics script
```

#### Production Script (Attempt-Based, MongoDB/JS)

```js
// U2P4: Determine which reason code(s) apply and compute quantities
// MISSING_SUCCESS_NODE: check if success node (74:21) is absent within attempt window
// TOO_MANY_NEGATIVES: count attempts_number from bad feedback node occurrences within attempt window
// With windowing for replay support
```
