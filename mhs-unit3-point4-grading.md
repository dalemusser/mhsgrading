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

### MISSING_SUCCESS_NODE

**Short Description:** Did not make the correct matches independently.

**Instructor Message:** The student didn’t successfully solve the puzzle of matching the pieces showing how materials move through waterways independently during the activity of navigating alien ruins and solving puzzles. The threshold for success is to solve the puzzle by the students themselves.

**Determination:** Check whether there is an eventKey of (`DialogueNodeEvent:78:24`).

**Teacher Guidance:** Review dissolved materials. Remind students that dissolved materials in water are present even if they cannot be seen.

### TOO_MANY_NEGATIVES

**Short Description:** Too many attempts to make the correct matches.

**Instructor Message:** The student used {attempt_number} to make the correct matches during the activity of navigating alien ruins and solving puzzles of how materials move through waterways. The threshold for success is to solve the puzzle within 3 attempts.

**Determination:** Count yellow node occurrences; yellow if the attempt > 3.

**Quantities:** `attempts_number` — count of yellow node occurrences.

**Teacher Guidance:** Review dissolved materials. Remind students that dissolved materials in water are present even if they cannot be seen.

### Reason Determination Scripts

#### Data Analytics Script (Python)

```python
# U3P4: The performnace of the student's puzzle solving regarding how materials move through waterways.
# MISSING_SUCCESS_NODE: Check if the player solve the puzzle independently. 

has_7824 = coll.find_one({
    "playerId": pid,
    "eventKey": "DialogueNodeEvent:78:24"
}) is not None

has_7824
```

```python
# TOO_MANY_NEGATIVES: Check how many negative feedbacks the student received. 

DIALOGUE_KEYS = [
    "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
    "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
    "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
]

total_count = coll.count_documents({
    "playerId": pid,
    "eventKey": {"$in": DIALOGUE_KEYS}
})

total_count
```

#### Analytics-Matching Script (MongoDB/JS)

```js
// U3P4: The performnace of the student's puzzle solving regarding how materials move through waterways.
// MISSING_SUCCESS_NODE: Check if the player solve the puzzle independently.

const playerId = "<playerId>";

const has_7824 =
  db.logdata.findOne({
    playerId: playerId,
    eventKey: "DialogueNodeEvent:78:24"
  }) !== null;

has_7824;
```

```js
// TOO_MANY_NEGATIVES: Check how many negative feedbacks the student received.

const playerId = "<playerId>";

const DIALOGUE_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

const total_count = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: DIALOGUE_KEYS }
});

total_count;
```

#### Production Script (Attempt-Based, MongoDB/JS)

```js
// U3P4: The performnace of the student's puzzle solving regarding how materials move through waterways.
// MISSING_SUCCESS_NODE: Check if the player solve the puzzle independently.

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:73:200";
const TARGET_KEY  = "DialogueNodeEvent:78:24";

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

let has7824 = false;

if (!latestTrigger) {
  // Not reached => false (or null if you prefer)
  has7824 = false;
} else {
  // 2) Previous trigger (attempt boundary)
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

  // 3) Existence check within the window
  has7824 =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: TARGET_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      },
      { projection: { _id: 1 } }
    ) !== null;
}

has7824;
```

```js
// TOO_MANY_NEGATIVES: Check how many negative feedbacks the student received.

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:73:200";

const DIALOGUE_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let total_count = 0;

if (!latestTrigger) {
  total_count = 0;
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

  total_count = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: DIALOGUE_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });
}

total_count;
```
