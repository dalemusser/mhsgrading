# Unit 3 Point 3 Grading

**Activity:** Pollution Argument

**Trigger Event:** `questFinishEvent:18`

---

## Grading Rule

Score-based rule with a bonus. Count incorrect argument selections, compute a base score, then add a bonus point if the student used the backing info panel.

| Outcome | Condition |
|---------|-----------|
| **Green** | total_score >= 3 |
| **Yellow** | total_score < 3, or no trigger exists |

### Score Formula

```
base_score = (see table below based on sum_count)
bonus      = 1 if player used "BackingInfoPanel - Pollution Site Data", else 0
total_score = base_score + bonus
```

### Base Score from Target Count

| sum_count | base_score |
|-----------|------------|
| <= 3      | 3          |
| 4         | 2          |
| 5         | 1          |
| >= 6      | 0          |

### Bonus Condition

Player must have a log entry with:
- `eventType` = `"argumentationToolEvent"`
- `data.toolName` = `"BackingInfoPanel - Pollution Site Data"`

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:18` (exclusive)
- **End:** Latest `questFinishEvent:18` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:18` |

**Target Keys (incorrect argument selections):**

<details>
<summary>Full list (16 keys)</summary>

- `DialogueNodeEvent:84:20`
- `DialogueNodeEvent:84:25`
- `DialogueNodeEvent:84:32`
- `DialogueNodeEvent:84:33`
- `DialogueNodeEvent:84:34`
- `DialogueNodeEvent:84:35`
- `DialogueNodeEvent:84:37`
- `DialogueNodeEvent:84:39`
- `DialogueNodeEvent:84:40`
- `DialogueNodeEvent:84:41`
- `DialogueNodeEvent:84:42`
- `DialogueNodeEvent:84:43`
- `DialogueNodeEvent:84:44`
- `DialogueNodeEvent:84:45`
- `DialogueNodeEvent:84:46`
- `DialogueNodeEvent:84:47`

</details>

**Bonus Event:**

| Field | Value |
|-------|-------|
| eventType | `argumentationToolEvent` |
| data.toolName | `BackingInfoPanel - Pollution Site Data` |

---

## Analytics Script

```js
// Unit 3, Point 3 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:18"

const playerId = "<playerId>";

const TARGET_KEYS = [
  "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
  "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40",
  "DialogueNodeEvent:84:41", "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43",
  "DialogueNodeEvent:84:44", "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46",
  "DialogueNodeEvent:84:47"
];

const sumCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: TARGET_KEYS }
});

let baseScore;
if (sumCount <= 3) baseScore = 3;
else if (sumCount === 4) baseScore = 2;
else if (sumCount === 5) baseScore = 1;
else baseScore = 0;

const hasBonus =
  db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "argumentationToolEvent",
      "data.toolName": "BackingInfoPanel - Pollution Site Data"
    },
    { projection: { _id: 1 } }
  ) !== null;

const totalScore = baseScore + (hasBonus ? 1 : 0);
const color = totalScore >= 3 ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 3 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "questFinishEvent:18"

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:18";

const TARGET_KEYS = [
  "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
  "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40",
  "DialogueNodeEvent:84:41", "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43",
  "DialogueNodeEvent:84:44", "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46",
  "DialogueNodeEvent:84:47"
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

  const sumCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: TARGET_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  let baseScore;
  if (sumCount <= 3) baseScore = 3;
  else if (sumCount === 4) baseScore = 2;
  else if (sumCount === 5) baseScore = 1;
  else baseScore = 0;

  const hasBonus =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventType: "argumentationToolEvent",
        "data.toolName": "BackingInfoPanel - Pollution Site Data",
        _id: { $gt: windowStartId, $lte: windowEndId }
      },
      { projection: { _id: 1 } }
    ) !== null;

  const totalScore = baseScore + (hasBonus ? 1 : 0);
  totalScore >= 3 ? "green" : "yellow";
}
```

---

## Reason Codes

### MISSING_SUCCESS_NODE

**Short Description:** Did not check backing information for key knowledge.

**Instructor Message:** The student didn’t open the backing information regarding the pollution site data during the activity of constructing an argument about the location of the pollutant that includes reasoning and links a claim with evidence. The threshold for success is to check the information at least once during the activity.

**Determination:** Check whether the argumentationToolEvent event (`BackingInfoPanel - Pollution Site Data`) is absent.

**Teacher Guidance:** Review the three parts of an argument with student:
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.

### WRONG_ARG_SELECTED

**Short Description:** Too many attempts to select correct reasoning to connect the claim with evidence.

**Instructor Message:** The student used {attempt_number} to construct the correct argument during the activity of constructing an argument about the location of the pollutant that includes reasoning and links a claim with evidence. The threshold for success is to construct the correct argument within 4 attempts.

**Determination:** Count yellow node occurrences; yellow if count > 4.

**Quantities:** `attempts_number` — count of yellow node occurrences.

**Teacher Guidance:** Review the three parts of an argument with student: 
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.

### Reason Determination Scripts

#### Data Analytics Script (Python)

```python
# U3P3: The performnace of the student's argumentation performance in Unit 3
# MISSING_SUCCESS_NODE: Check if the player look at the backing informaiton regarding the the pollution site data. 

has_backing_info = coll.find_one({
    "playerId": pid,
    "eventType": "argumentationToolEvent",
    "data.toolName": "BackingInfoPanel - Pollution Site Data"
}) is not None

has_backing_info
```

```python
# WRONG_ARG_SELECTED: How many times students construct the wrong arguments. 

WRONG_ARGUMENT_KEYS = [
    "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
    "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
    "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40",
    "DialogueNodeEvent:84:41", "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43",
    "DialogueNodeEvent:84:44", "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46",
    "DialogueNodeEvent:84:47"
]

wrong_argument_count = coll.count_documents({
    "playerId": pid,
    "eventKey": {"$in": WRONG_ARGUMENT_KEYS}
})

wrong_argument_count
```

#### Analytics-Matching Script (MongoDB/JS)

```js
// U3P3: The performnace of the student's argumentation performance in Unit 3
// MISSING_SUCCESS_NODE: Exact match to data analytics script

const playerId = "<playerId>";

const has_backing_info =
  db.logdata.findOne({
    playerId: playerId,
    eventType: "argumentationToolEvent",
    "data.toolName": "BackingInfoPanel - Pollution Site Data"
  }) !== null;

has_backing_info;
```

```js
// U3P3: The performnace of the student's argumentation performance in Unit 3.
// WRONG_ARG_SELECTED: How many times students construct the wrong arguments. 

const playerId = "<playerId>";

const WRONG_ARGUMENT_KEYS = [
  "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
  "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40",
  "DialogueNodeEvent:84:41", "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43",
  "DialogueNodeEvent:84:44", "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46",
  "DialogueNodeEvent:84:47"
];

const wrong_argument_count = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: WRONG_ARGUMENT_KEYS }
});

wrong_argument_count;
```

#### Production Script (Attempt-Based, MongoDB/JS)

```js
// U3P3: Determine whether the student triggered the success node.
// Exact match to data analytics script

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:18";

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let has_backing_info = false;

if (!latestTrigger) {
  has_backing_info = false;
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

  has_backing_info =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventType: "argumentationToolEvent",
        "data.toolName": "BackingInfoPanel - Pollution Site Data",
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;
}

has_backing_info;
```

```js
// U3P3: Determine whether the student triggered the success node.
// WRONG_ARG_SELECTED: How many times students construct the wrong arguments.

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:18";

const WRONG_ARGUMENT_KEYS = [
  "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
  "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40",
  "DialogueNodeEvent:84:41", "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43",
  "DialogueNodeEvent:84:44", "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46",
  "DialogueNodeEvent:84:47"
];

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

let wrong_argument_count = 0;

if (!latestTrigger) {
  wrong_argument_count = 0;
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

  wrong_argument_count = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: WRONG_ARGUMENT_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });
}

wrong_argument_count;
```

