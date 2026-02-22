# Unit 2 Point 5 Grading

**Activity:** Classified Information

**Trigger Event:** `DialogueNodeEvent:23:42`

---

## Grading Rule

Score-based rule. Count positive (correct) and negative (incorrect) argument component selections, then compute a weighted score.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 4 |
| **Yellow** | score < 4, or no trigger exists |

### Score Formula

```
score = pos_count - (neg_count / 3.0)
```

- `pos_count` = count of correct identification events (POS_KEYS)
- `neg_count` = count of incorrect identification events (NEG_KEYS)

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:23:42` (exclusive)
- **End:** Latest `DialogueNodeEvent:23:42` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:23:42` |

**Positive Keys (correct identifications):**

`DialogueNodeEvent:26:165` through `DialogueNodeEvent:26:186` (22 keys)

<details>
<summary>Full list</summary>

- `DialogueNodeEvent:26:165`
- `DialogueNodeEvent:26:166`
- `DialogueNodeEvent:26:167`
- `DialogueNodeEvent:26:168`
- `DialogueNodeEvent:26:169`
- `DialogueNodeEvent:26:170`
- `DialogueNodeEvent:26:171`
- `DialogueNodeEvent:26:172`
- `DialogueNodeEvent:26:173`
- `DialogueNodeEvent:26:174`
- `DialogueNodeEvent:26:175`
- `DialogueNodeEvent:26:176`
- `DialogueNodeEvent:26:177`
- `DialogueNodeEvent:26:178`
- `DialogueNodeEvent:26:179`
- `DialogueNodeEvent:26:180`
- `DialogueNodeEvent:26:181`
- `DialogueNodeEvent:26:182`
- `DialogueNodeEvent:26:183`
- `DialogueNodeEvent:26:184`
- `DialogueNodeEvent:26:185`
- `DialogueNodeEvent:26:186`

</details>

**Negative Keys (incorrect identifications):**

`DialogueNodeEvent:26:187` through `DialogueNodeEvent:26:211` (25 keys)

<details>
<summary>Full list</summary>

- `DialogueNodeEvent:26:187`
- `DialogueNodeEvent:26:188`
- `DialogueNodeEvent:26:189`
- `DialogueNodeEvent:26:190`
- `DialogueNodeEvent:26:191`
- `DialogueNodeEvent:26:192`
- `DialogueNodeEvent:26:193`
- `DialogueNodeEvent:26:194`
- `DialogueNodeEvent:26:195`
- `DialogueNodeEvent:26:196`
- `DialogueNodeEvent:26:197`
- `DialogueNodeEvent:26:198`
- `DialogueNodeEvent:26:199`
- `DialogueNodeEvent:26:200`
- `DialogueNodeEvent:26:201`
- `DialogueNodeEvent:26:202`
- `DialogueNodeEvent:26:203`
- `DialogueNodeEvent:26:204`
- `DialogueNodeEvent:26:205`
- `DialogueNodeEvent:26:206`
- `DialogueNodeEvent:26:207`
- `DialogueNodeEvent:26:208`
- `DialogueNodeEvent:26:209`
- `DialogueNodeEvent:26:210`
- `DialogueNodeEvent:26:211`

</details>

---

## Reason Codes

| Code | Short Description | Teacher Guidance |
|------|-------------------|------------------|
| TOO_MANY_NEGATIVES | Too many incorrect attempts identifying argument parts (claim, evidence, reasoning) | Review the three parts of an argument with student: 1. Claim: statement that answers the driving question. 2. Evidence: scientific data and facts that support your claim. 3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim. |

---

## Analytics Script

```js
// Unit 2, Point 5 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:23:42"

const playerId = "<playerId>";

const POS_KEYS = [
  "DialogueNodeEvent:26:165", "DialogueNodeEvent:26:166", "DialogueNodeEvent:26:167",
  "DialogueNodeEvent:26:168", "DialogueNodeEvent:26:169", "DialogueNodeEvent:26:170",
  "DialogueNodeEvent:26:171", "DialogueNodeEvent:26:172", "DialogueNodeEvent:26:173",
  "DialogueNodeEvent:26:174", "DialogueNodeEvent:26:175", "DialogueNodeEvent:26:176",
  "DialogueNodeEvent:26:177", "DialogueNodeEvent:26:178", "DialogueNodeEvent:26:179",
  "DialogueNodeEvent:26:180", "DialogueNodeEvent:26:181", "DialogueNodeEvent:26:182",
  "DialogueNodeEvent:26:183", "DialogueNodeEvent:26:184", "DialogueNodeEvent:26:185",
  "DialogueNodeEvent:26:186"
];

const NEG_KEYS = [
  "DialogueNodeEvent:26:187", "DialogueNodeEvent:26:188", "DialogueNodeEvent:26:189",
  "DialogueNodeEvent:26:190", "DialogueNodeEvent:26:191", "DialogueNodeEvent:26:192",
  "DialogueNodeEvent:26:193", "DialogueNodeEvent:26:194", "DialogueNodeEvent:26:195",
  "DialogueNodeEvent:26:196", "DialogueNodeEvent:26:197", "DialogueNodeEvent:26:198",
  "DialogueNodeEvent:26:199", "DialogueNodeEvent:26:200", "DialogueNodeEvent:26:201",
  "DialogueNodeEvent:26:202", "DialogueNodeEvent:26:203", "DialogueNodeEvent:26:204",
  "DialogueNodeEvent:26:205", "DialogueNodeEvent:26:206", "DialogueNodeEvent:26:207",
  "DialogueNodeEvent:26:208", "DialogueNodeEvent:26:209", "DialogueNodeEvent:26:210",
  "DialogueNodeEvent:26:211"
];

const posCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: POS_KEYS }
});

const negCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: NEG_KEYS }
});

const score = posCount - (negCount / 3.0);
const color = score >= 4 ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 5 — Attempt-based standalone production grading script
// Trigger eventKey: "DialogueNodeEvent:23:42"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:42";

const POS_KEYS = [
  "DialogueNodeEvent:26:165", "DialogueNodeEvent:26:166", "DialogueNodeEvent:26:167",
  "DialogueNodeEvent:26:168", "DialogueNodeEvent:26:169", "DialogueNodeEvent:26:170",
  "DialogueNodeEvent:26:171", "DialogueNodeEvent:26:172", "DialogueNodeEvent:26:173",
  "DialogueNodeEvent:26:174", "DialogueNodeEvent:26:175", "DialogueNodeEvent:26:176",
  "DialogueNodeEvent:26:177", "DialogueNodeEvent:26:178", "DialogueNodeEvent:26:179",
  "DialogueNodeEvent:26:180", "DialogueNodeEvent:26:181", "DialogueNodeEvent:26:182",
  "DialogueNodeEvent:26:183", "DialogueNodeEvent:26:184", "DialogueNodeEvent:26:185",
  "DialogueNodeEvent:26:186"
];

const NEG_KEYS = [
  "DialogueNodeEvent:26:187", "DialogueNodeEvent:26:188", "DialogueNodeEvent:26:189",
  "DialogueNodeEvent:26:190", "DialogueNodeEvent:26:191", "DialogueNodeEvent:26:192",
  "DialogueNodeEvent:26:193", "DialogueNodeEvent:26:194", "DialogueNodeEvent:26:195",
  "DialogueNodeEvent:26:196", "DialogueNodeEvent:26:197", "DialogueNodeEvent:26:198",
  "DialogueNodeEvent:26:199", "DialogueNodeEvent:26:200", "DialogueNodeEvent:26:201",
  "DialogueNodeEvent:26:202", "DialogueNodeEvent:26:203", "DialogueNodeEvent:26:204",
  "DialogueNodeEvent:26:205", "DialogueNodeEvent:26:206", "DialogueNodeEvent:26:207",
  "DialogueNodeEvent:26:208", "DialogueNodeEvent:26:209", "DialogueNodeEvent:26:210",
  "DialogueNodeEvent:26:211"
];

// 1) Latest trigger (end anchor) by arrival order
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  "yellow";
} else {
  // 2) Previous trigger (defines attempt start boundary)
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

  // 3) Count POS/NEG inside window
  const posCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: POS_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const score = posCount - (negCount / 3.0);
  score >= 4 ? "green" : "yellow";
}
```
