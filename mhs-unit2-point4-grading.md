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
---

## Analytics Script

```js
// Unit 2, Point 4 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:23:17"

const playerId = "<playerId>";
| Bad Feedback | `DialogueNodeEvent:74:16` |
| Bad Feedback | `DialogueNodeEvent:74:17` |
| Bad Feedback | `DialogueNodeEvent:74:20` |
| Bad Feedback | `DialogueNodeEvent:74:22` |


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

has_not_success_node = coll.find_one(
        {
            "playerId": playerId,
            "eventKey": "DialogueNodeEvent:74:21"
        }
    ) is None

has_not_success_node
```

```python
# TOO_MANY_NEGATIVES: count attempts_number from bad feedback node occurrences

FIVE_ATTEMPT_KEYS = [
        "DialogueNodeEvent:74:16",
        "DialogueNodeEvent:74:17"
    ]

SIX_ATTEMPT_KEYS = [
        "DialogueNodeEvent:74:22",
        "DialogueNodeEvent:74:20"
    ]

relevant_keys = FIVE_ATTEMPT_KEYS + SIX_ATTEMPT_KEYS

events = list(coll.find(
        {"playerId": pid, "eventKey": {"$in": relevant_keys}}
    ))

triggered_keys = {e["eventKey"] for e in events}

attempt = 0

if any(k in triggered_keys for k in SIX_ATTEMPT_KEYS):
  attempt = 6

if any(k in triggered_keys for k in FIVE_ATTEMPT_KEYS):
  attempt = 5
  
attempt
```

#### Analytics-Matching Script (MongoDB/JS)

```js
// U2P4: Determine which reason code(s) apply and compute quantities
// MISSING_SUCCESS_NODE: check if success node (74:21) is absent

const has_not_success_node =
  db.logdata.findOne(
    {
      playerId: playerId,
      eventKey: "DialogueNodeEvent:74:21"
    }
    ) !== null;
    
has_not_success_node
```

```js
// TOO_MANY_NEGATIVES: count attempts_number from bad feedback node occurrences
// Exact match to data analytics script

const playerId = "<playerId>";

const FIVE_ATTEMPT_KEYS = [
  "DialogueNodeEvent:74:16",
  "DialogueNodeEvent:74:17"
];

const SIX_ATTEMPT_KEYS = [
  "DialogueNodeEvent:74:22",
  "DialogueNodeEvent:74:20"
];

const relevantKeys = [
  ...FIVE_ATTEMPT_KEYS,
  ...SIX_ATTEMPT_KEYS
];

const events = db.logdata.find(
  {
    playerId: playerId,
    eventKey: { $in: relevantKeys }
  }
).toArray();

const triggeredKeys = new Set(events.map(e => e.eventKey));

let attempt = 0;

if (SIX_ATTEMPT_KEYS.some(k => triggeredKeys.has(k))) {
  attempt = 6;
}

if (FIVE_ATTEMPT_KEYS.some(k => triggeredKeys.has(k))) {
  attempt = 5;
}

attempt;
```

#### Production Script (Attempt-Based, MongoDB/JS)

```js
// U2P4: Determine which reason code(s) apply and compute quantities
// MISSING_SUCCESS_NODE: check if success node (74:21) is absent within attempt window

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:17";
const SUCCESS_KEY = "DialogueNodeEvent:74:21";

// 1) Latest trigger
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let hasNotSuccessNode = true;

if (!latestTrigger) {
  hasNotSuccessNode = true;
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

  hasNotSuccessNode =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: SUCCESS_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) == null;
}

hasNotSuccessNode;
```

```js
// TOO_MANY_NEGATIVES: count attempts_number from bad feedback node occurrences within attempt window
// With windowing for replay support

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:17";

const FIVE_ATTEMPT_KEYS = [
  "DialogueNodeEvent:74:16",
  "DialogueNodeEvent:74:17"
];

const SIX_ATTEMPT_KEYS = [
  "DialogueNodeEvent:74:22",
  "DialogueNodeEvent:74:20"
];

const relevantKeys = [
  ...FIVE_ATTEMPT_KEYS,
  ...SIX_ATTEMPT_KEYS
];

// 1) Latest trigger
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let attempt = 0;

if (!latestTrigger) {
  attempt = 0;
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

  const events = db.logdata.find(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: relevantKeys },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }
  ).toArray();

  const triggeredKeys = new Set(events.map(e => e.eventKey));

  if (SIX_ATTEMPT_KEYS.some(k => triggeredKeys.has(k))) attempt = 6;
  else if (FIVE_ATTEMPT_KEYS.some(k => triggeredKeys.has(k))) attempt = 5;
}

attempt;
```
