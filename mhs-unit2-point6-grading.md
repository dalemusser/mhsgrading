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

---

## Reason Codes

### HIT_YELLOW_NODE

**Short Description:** Chose an incorrect criterion for watershed size on first try

**Instructor Message:** Students chose the wrong standards to determine which watershed is larger, {dialogue_node_1} or/and {dialogue_node_2} at the first attempt during the activity of collecting evidence to construct an argument about watershed size. The success threshold is to select the correct standard, {dialogue_node_3}, at the first attempt.

**Quantities:**
- `dialogue_node_1` — first incorrect standard chosen
- `dialogue_node_2` — second incorrect standard chosen (if applicable)
- `dialogue_node_3` — the correct standard

**Teacher Guidance:**
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.

### Reason Quantity Scripts

#### Data Analytics Script (Python)

```python
# U2P6: Determine dialogue_node_1, dialogue_node_2, dialogue_node_3 for HIT_YELLOW_NODE
# Identify which incorrect standards were chosen and which is the correct standard

KEY_44 = "DialogueNodeEvent:20:44"
KEY_45 = "DialogueNodeEvent:20:45"

events = list(coll.find(
        {
            "playerId": pid,
            "eventKey": {"$in": [KEY_44, KEY_45]}
        }
    ))

triggered = {e["eventKey"] for e in events}

has_44 = KEY_44 in triggered
has_45 = KEY_45 in triggered

if has_44 and has_45:
  result = "guessing through the correct answer"
elif has_44:
  result = "waterfall height"
elif has_45:
  result = "salinity"
  
result
```

#### Analytics-Matching Script (MongoDB/JS)

```js
// U2P6: Determine dialogue_node_1, dialogue_node_2, dialogue_node_3 for HIT_YELLOW_NODE
// Exact match to data analytics script

const playerId = "<playerId>";

const KEY_44 = "DialogueNodeEvent:20:44";
const KEY_45 = "DialogueNodeEvent:20:45";

const events = db.logdata.find(
  {
    playerId: playerId,
    eventKey: { $in: [KEY_44, KEY_45] }
  }
).toArray();

const triggered = new Set(events.map(e => e.eventKey));

const has_44 = triggered.has(KEY_44);
const has_45 = triggered.has(KEY_45);

let result;

if (has_44 && has_45) {
  result = "guessing through the correct answer";
} else if (has_44) {
  result = "waterfall height";
} else if (has_45) {
  result = "salinity";
}

result;
```

#### Production Script (Attempt-Based, MongoDB/JS)

```js
// U2P6: Determine dialogue_node_1, dialogue_node_2, dialogue_node_3 for HIT_YELLOW_NODE
// With windowing for replay support

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:20:46";
const KEY_44 = "DialogueNodeEvent:20:44";
const KEY_45 = "DialogueNodeEvent:20:45";

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let result = null;

if (!latestTrigger) {
  result = null;
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
      eventKey: { $in: [KEY_44, KEY_45] },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }
  ).toArray();

  const triggered = new Set(events.map(e => e.eventKey));

  const has_44 = triggered.has(KEY_44);
  const has_45 = triggered.has(KEY_45);

  if (has_44 && has_45) {
    result = "guessing through the correct answer";
  } else if (has_44) {
    result = "waterfall height";
  } else if (has_45) {
    result = "salinity";
  }

}
result;
```
