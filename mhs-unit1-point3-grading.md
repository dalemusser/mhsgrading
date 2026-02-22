# Unit 1 Point 3 Grading

**Activity:** Defend the Expedition

**Trigger Event:** `questActiveEvent:34`

---

## Grading Rule

Check whether the student needed multiple attempts to build the correct argument.

| Outcome | Condition |
|---------|-----------|
| **Green** | No yellow nodes found within the attempt window |
| **Yellow** | Any yellow node found within the attempt window, or no trigger exists |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:34` (exclusive)
- **End:** Latest `questActiveEvent:34` (inclusive)

> Without windowing, one early mistake permanently results in yellow. With windowing, a student can replay and earn green on a later attempt.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:34` |
| Yellow | `DialogueNodeEvent:70:25` |
| Yellow | `DialogueNodeEvent:70:33` |

---

## Reason Codes

### WRONG_ARG_SELECTED

**Short Description:** Needed multiple tries to build the correct argument

**Instructor Message:** The student used {attempt_number} to construct the correct argument during the activity of learning to use the argumentation engine and identifying a claim in an argument. The threshold for success is to construct the correct argument at the first attempt.

**Quantities:** `attempt_number` — count of attempts

**Teacher Guidance:**
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.

### Reason Quantity Scripts

#### Data Analytics Script (Python)

```python
# U1P3: Determine attempt_number for WRONG_ARG_SELECTED
# Count the number of attempts to construct the correct argument
```

#### Analytics-Matching Script (MongoDB/JS)

```js
// U1P3: Determine attempt_number for WRONG_ARG_SELECTED
// Exact match to data analytics script
```

#### Production Script (Attempt-Based, MongoDB/JS)

```js
// U1P3: Determine attempt_number for WRONG_ARG_SELECTED
// With windowing for replay support
```

---

## Analytics Script

```js
// Unit 1, Point 3 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:34"

const playerId = "<playerId>";

const YELLOW_KEYS = [
  "DialogueNodeEvent:70:25",
  "DialogueNodeEvent:70:33"
];

const hasYellow =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: YELLOW_KEYS }
  }) !== null;

const color = hasYellow ? "yellow" : "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 1, Point 3 — Attempt-based standalone production script
// Trigger eventKey: "questActiveEvent:34"

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:34";

const YELLOW_KEYS = [
  "DialogueNodeEvent:70:25",
  "DialogueNodeEvent:70:33"
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

  const hasYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: YELLOW_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  hasYellow ? "yellow" : "green";
}
```
