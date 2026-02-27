# Unit 3 Point 2 Grading

**Activity:** Pollution Solution

**Trigger Event:** `DialogueNodeEvent:11:34`

---

## Grading Rule

Score-based rule with capped penalties. The student starts with 5 points and loses points based on incorrect attempts, capped per category.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 3 |
| **Yellow** | score < 3, or no trigger exists |

### Score Formula

```
score = 5 - capped_penalty(c27) - capped_penalty(c29 + c230)
```

Where `capped_penalty(cnt)`:
| Count | Penalty |
|-------|---------|
| <= 1  | 0       |
| 2-3   | 1       |
| >= 4  | 2       |

### Count Targets

- `c27` = count of `DialogueNodeEvent:11:27`
- `c29` = count of `DialogueNodeEvent:11:29`
- `c230` = count of `DialogueNodeEvent:11:230`
- `cSum` = c29 + c230

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:11:34` (exclusive)
- **End:** Latest `DialogueNodeEvent:11:34` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:11:34` |
| Penalty group 1 | `DialogueNodeEvent:11:27` |
| Penalty group 2 | `DialogueNodeEvent:11:29` |
| Penalty group 2 | `DialogueNodeEvent:11:230` |

---

## Analytics Script

```js
// Unit 3, Point 2 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:11:34"

const playerId = "<playerId>";

function cappedPenalty(cnt) {
  if (cnt <= 1) return 0;
  if (cnt <= 3) return 1;
  return 2;
}

const c27 = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:11:27"
});

const c29 = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:11:29"
});

const c230 = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:11:230"
});

const cSum = c29 + c230;

let score = 5;
score -= cappedPenalty(c27);
score -= cappedPenalty(cSum);

const color = score < 3 ? "yellow" : "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 2 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:11:34"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:11:34";

function cappedPenalty(cnt) {
  if (cnt <= 1) return 0;
  if (cnt <= 3) return 1;
  return 2;
}

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

  const c27 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: "DialogueNodeEvent:11:27",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const c29 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: "DialogueNodeEvent:11:29",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const c230 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: "DialogueNodeEvent:11:230",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const cSum = c29 + c230;

  let score = 5;
  score -= cappedPenalty(c27);
  score -= cappedPenalty(cSum);

  score < 3 ? "yellow" : "green";
}
```

---

## Reason Codes

### BAD_FEEDBACK

**Short Description:** Repeated reminding dialogues triggered regarding redundant sensor usage.

**Instructor Message:** The student triggered {attempt_number} times of the reminding dialogues regarding the redundant sensor usage during the activity of finding the source of a pollutant by predicting the spread of dissolved materials through a watershed. The threshold for success is not to trigger such reminding dialogues more than 6 times.

**Quantities:** `attempt_number` — count of negative feedback triggered.

**Teacher Guidance:**
Review watershed maps with students, and ask them to predict flow of water. Remind students that rivers empty into the ocean.

### Reason Determination Scripts

#### Data Analytics Script (Python)
```python
# U3P2: Determine attempt_number for BAD_FEEDBACK
# Count the number of dialogues triggered to remind redundant sensors used

REMINDING_KEYS = [
    "DialogueNodeEvent:11:27",
    "DialogueNodeEvent:11:29",
    "DialogueNodeEvent:11:230"
]

reminding_count = coll.count_documents({
    "playerId": pid,
    "eventKey": {"$in": REMINDING_KEYS}
})

reminding_count
```

#### Analytics-Matching Script (MongoDB/JS)
```js
// U3P2: Determine attempt_number for BAD_FEEDBACK
// Count the number of dialogues triggered to remind redundant sensors used

const playerId = "<playerId>";

const REMINDING_KEYS = [
  "DialogueNodeEvent:11:27",
  "DialogueNodeEvent:11:29",
  "DialogueNodeEvent:11:230"
];

const reminding_count = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: REMINDING_KEYS }
});

reminding_count;
```

#### Production Script (Attempt-Based, MongoDB/JS)
```js
// U3P2: Determine attempt_number for BAD_FEEDBACK
// Count the number of dialogues triggered to remind redundant sensors used

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:11:34";

const REMINDING_KEYS = [
  "DialogueNodeEvent:11:27",
  "DialogueNodeEvent:11:29",
  "DialogueNodeEvent:11:230"
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let reminding_count = 0;

if (!latestTrigger) {
  reminding_count = 0;
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

  reminding_count = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: REMINDING_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });
}

reminding_count;
```

