# Unit 2 Point 1 Grading

**Activity:** Escape the Ruin

**Trigger Event:** `questFinishEvent:21`

---

## Grading Rule

Student must complete the map-profile matching independently and without excessive incorrect attempts.

| Outcome | Condition |
|---------|-----------|
| **Green** | Success node present AND no yellow nodes in attempt window |
| **Yellow** | Success node missing OR any yellow node present |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:21` (exclusive)
- **End:** Latest `questFinishEvent:21` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:21` |
| Success | `DialogueNodeEvent:68:29` |
| Yellow | `DialogueNodeEvent:68:22` |
| Yellow | `DialogueNodeEvent:68:23` |
| Yellow | `DialogueNodeEvent:68:27` |
| Yellow | `DialogueNodeEvent:68:28` |
| Yellow | `DialogueNodeEvent:68:31` |

---

## Analytics Script

```js
// Unit 2, Point 1 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:21"

const playerId = "<playerId>";

const successKey = "DialogueNodeEvent:68:29";

const yellowNodes = [
  "DialogueNodeEvent:68:22",
  "DialogueNodeEvent:68:23",
  "DialogueNodeEvent:68:27",
  "DialogueNodeEvent:68:28",
  "DialogueNodeEvent:68:31"
];

const hasSuccess =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: successKey
  }) !== null;

const hasAnyYellow =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: yellowNodes }
  }) !== null;

const color =
  hasSuccess && !hasAnyYellow
    ? "green"
    : "yellow";

color;
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 1 — Attempt-based standalone production grading script
// Trigger eventKey: "questFinishEvent:21"

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:21";

const successKey = "DialogueNodeEvent:68:29";

const yellowNodes = [
  "DialogueNodeEvent:68:22",
  "DialogueNodeEvent:68:23",
  "DialogueNodeEvent:68:27",
  "DialogueNodeEvent:68:28",
  "DialogueNodeEvent:68:31"
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
      game: "mhs",
      playerId: playerId,
      eventKey: successKey,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  const hasAnyYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: yellowNodes },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  hasSuccess && !hasAnyYellow ? "green" : "yellow";
}
```

---

## Reason Codes

> This point has multiple possible reasons for a yellow grade. Scripts are needed to determine which reason(s) apply.

### MISSING_SUCCESS_NODE

**Short Description:** Did not complete map-profile matching independently

**Instructor Message:** Students didn't make the correct matches by themselves during the activity of matching topographic maps to elevation profiles. One of the successful conditions for this activity is to make correct matches.

**Determination:** Check whether the success node (`DialogueNodeEvent:68:29`) is absent.

**Teacher Guidance:**
1. How information about elevation can be gained from contour lines.
2. How to use the compass and contour indices to aid navigation.

### TOO_MANY_NEGATIVES

**Short Description:** Too many incorrect map-terrain matches

**Instructor Message:** Students made wrong matches of topographic maps and real-world terrains using {attempts_number} attempts. The other successful condition for this activity is to make the correct matches within 4 attempts.

**Determination:** Count yellow node occurrences; yellow if count > 4.

**Quantities:** `attempts_number` — count of incorrect match attempts

**Teacher Guidance:**
1. How information about elevation can be gained from contour lines.
2. How to use the compass and contour indices to aid navigation.

### Reason Determination Scripts

#### Data Analytics Script (Python)

```python
# U2P1: Determine which reason code(s) apply and compute quantities
# MISSING_SUCCESS_NODE: check if success node (68:29) is absent

has_success_node = coll.find_one(
        {
            "playerId": playerId,
            "eventKey": "DialogueNodeEvent:68:29"
        }
    ) is not None

has_success_node
```

```python
# TOO_MANY_NEGATIVES: count attempts_number from yellow node occurrences

FIVE_ATTEMPT_KEYS = [
        "DialogueNodeEvent:68:22",
        "DialogueNodeEvent:68:23"
    ]

SIX_ATTEMPT_KEYS = [
        "DialogueNodeEvent:68:27",
        "DialogueNodeEvent:68:31"
    ]
    
NPC_HELP_KEY = "DialogueNodeEvent:68:28"

relevant_keys = FIVE_ATTEMPT_KEYS + SIX_ATTEMPT_KEYS + [NPC_HELP_KEY]

events = list(coll.find(
        {"playerId": pid, "eventKey": {"$in": relevant_keys}}
    ))

triggered_keys = {e["eventKey"] for e in events}

attempt = 0

if NPC_HELP_KEY in triggered_keys:
  attempt = 7

if any(k in triggered_keys for k in SIX_ATTEMPT_KEYS):
  attempt = 6

if any(k in triggered_keys for k in FIVE_ATTEMPT_KEYS):
  attempt = 5
  
attempt
```

#### Analytics-Matching Script (MongoDB/JS)

```js
// U2P1: Determine which reason code(s) apply and compute quantities
// MISSING_SUCCESS_NODE: check if success node (68:29) is absent

const has_success_node =
  db.logdata.findOne(
    {
      playerId: playerId,
      eventKey: "DialogueNodeEvent:68:29"
    }
    ) !== null;
    
has_success_node
```

```js
// TOO_MANY_NEGATIVES: count attempts_number from yellow node occurrences
// Exact match to data analytics script

const playerId = "<playerId>";

const FIVE_ATTEMPT_KEYS = [
  "DialogueNodeEvent:68:22",
  "DialogueNodeEvent:68:23"
];

const SIX_ATTEMPT_KEYS = [
  "DialogueNodeEvent:68:27",
  "DialogueNodeEvent:68:31"
];

const NPC_HELP_KEY = "DialogueNodeEvent:68:28";

const relevantKeys = [
  ...FIVE_ATTEMPT_KEYS,
  ...SIX_ATTEMPT_KEYS,
  NPC_HELP_KEY
];

const events = db.logdata.find(
  {
    playerId: playerId,
    eventKey: { $in: relevantKeys }
  }
).toArray();

const triggeredKeys = new Set(events.map(e => e.eventKey));

let attempt = 0;

if (triggeredKeys.has(NPC_HELP_KEY)) {
  attempt = 7;
}

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
// U2P1: Determine which reason code(s) apply and compute quantities
// MISSING_SUCCESS_NODE: check if success node (68:29) is absent within attempt window

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:21";
const SUCCESS_KEY = "DialogueNodeEvent:68:29";

// 1) Latest trigger
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let hasSuccessNode = false;

if (!latestTrigger) {
  hasSuccessNode = false;
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

  hasSuccessNode =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: SUCCESS_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;
}

const MISSING_SUCCESS_NODE = !hasSuccessNode;

MISSING_SUCCESS_NODE;
```

```js
// TOO_MANY_NEGATIVES: count attempts_number from yellow node occurrences within attempt window
// With windowing for replay support

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:21";

const FIVE_ATTEMPT_KEYS = [
  "DialogueNodeEvent:68:22",
  "DialogueNodeEvent:68:23"
];

const SIX_ATTEMPT_KEYS = [
  "DialogueNodeEvent:68:27",
  "DialogueNodeEvent:68:31"
];

const NPC_HELP_KEY = "DialogueNodeEvent:68:28";

const relevantKeys = [
  ...FIVE_ATTEMPT_KEYS,
  ...SIX_ATTEMPT_KEYS,
  NPC_HELP_KEY
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

  if (triggeredKeys.has(NPC_HELP_KEY)) attempt = 7;
  else if (SIX_ATTEMPT_KEYS.some(k => triggeredKeys.has(k))) attempt = 6;
  else if (FIVE_ATTEMPT_KEYS.some(k => triggeredKeys.has(k))) attempt = 5;
}

attempt;
```
