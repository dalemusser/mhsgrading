# Unit 3 Point 3 Grading

**Activity:** Pollution Argument

**Trigger(Start) Event:** `DialogueNodeEvent:11:34`
**Trigger(End) Event:** `questFinishEvent:18`

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

- **Start:** Previous `DialogueNodeEvent:11:34` (exclusive)
- **End:** Latest `questFinishEvent:18` (inclusive)

---

## Event Keys

| Role          | Event Key             |
|---------------|-----------------------|
| Trigger (End) | `questFinishEvent:18` |

**Target Keys (incorrect argument selections):**

<details>
<summary>Full list (18 keys)</summary>

- `DialogueNodeEvent:84:20`
- `DialogueNodeEvent:84:25`
- `DialogueNodeEvent:84:32`
- `DialogueNodeEvent:84:33`
- `DialogueNodeEvent:84:34`
- `DialogueNodeEvent:84:35`
- `DialogueNodeEvent:84:36`
- `DialogueNodeEvent:84:37`
- `DialogueNodeEvent:84:38`
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
  "DialogueNodeEvent:84:36", "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:38",
  "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40", "DialogueNodeEvent:84:41",
  "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43", "DialogueNodeEvent:84:44",
  "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46", "DialogueNodeEvent:84:47"
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
  "DialogueNodeEvent:84:36", "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:38",
  "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40", "DialogueNodeEvent:84:41",
  "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43", "DialogueNodeEvent:84:44",
  "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46", "DialogueNodeEvent:84:47"
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

### EXCESS_ATTEMPTS

**Instructor Message:** In Pollution Argument, while constructing the argument about where the pollutant enters the river, the student made {wrong_argument_number} incorrect submissions — {claim_wrong_number} with a claim problem, {reasoning_wrong_number} with a reasoning problem, and {evidence_wrong_number} with an evidence or structure problem — and {backing_info_phrase} the Pollution Site Data reference panel. This point earns green only when incorrect submissions stay within the limit (at most 3, or one more when the reference panel has been consulted, which earns a bonus point). Errors concentrated on reasoning may indicate difficulty explaining how pollution travels downstream with the water flow, which is the link between the sensor evidence and the claim.

#### Conversation-84 Feedback Nodes by Argument Component

All keys are `DialogueNodeEvent:84:<n>`. Each incorrect-submission feedback node names
the component that caused the problem (color-tagged in the dialogue text).

| Problem category | Nodes | Feedback gist |
|------------------|-------|---------------|
| Claim            | 25, 39, 45, 46 | Claim does not take into consideration that water can carry pollution |
| Reasoning        | 32, 33, 34, 35, 40, 41, 42, 43, 44 | Reasoning does not explain how water behaves / where the pollution is; "water must flow north to south" is not always true; reasoning does not match the evidence |
| Evidence / structure | 37, 20, 47 | Evidence does not match the argument; multiple evidence pieces used; argument incomplete |

Nodes that are **not** incorrect submissions:

| Node | Meaning |
|------|---------|
| `84:36` | Success — "Great Job! You made the best argument possible." (currently still counted in the color scripts' TARGET_KEYS — flagged for review) |
| `84:38` | Empty node, no text (currently still counted in the color scripts' TARGET_KEYS — flagged for review) |
| `84:48`, `84:49` | Hint nudges — "click the Backing Information orbs" (ungraded by design) |
| `84:0`, `84:4`, `84:8`, `84:31` | Empty structural nodes, never graded |

#### Correspoinding Script

```js
// U3P3: EXCESS_ATTEMPTS — determine trigger and quantities
// triggered mirrors the color formula verbatim: base score from the color
// script's TARGET_KEYS count (which currently includes success node 84:36 and
// empty 84:38 — flagged for review), plus 1 bonus for opening the Pollution
// Site Data panel; yellow when total < 3.
// The quantities report honest counts: wrong_argument_number excludes 84:36/38,
// and the three component counts split it by the problem the feedback named.

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:18";

const CLAIM_NEG_KEYS = [
  "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:39",
  "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46"
];
const REASONING_NEG_KEYS = [
  "DialogueNodeEvent:84:32", "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34",
  "DialogueNodeEvent:84:35", "DialogueNodeEvent:84:40", "DialogueNodeEvent:84:41",
  "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43", "DialogueNodeEvent:84:44"
];
const EVIDENCE_STRUCT_NEG_KEYS = [
  "DialogueNodeEvent:84:37",  // evidence doesn't match the argument
  "DialogueNodeEvent:84:20",  // multiple evidence pieces used
  "DialogueNodeEvent:84:47"   // incomplete argument
];

const WRONG_KEYS = [...CLAIM_NEG_KEYS, ...REASONING_NEG_KEYS, ...EVIDENCE_STRUCT_NEG_KEYS];

// Color-rule key list, kept verbatim so triggered matches the cell (incl. 36/38)
const COLOR_TARGET_KEYS = [...WRONG_KEYS, "DialogueNodeEvent:84:36", "DialogueNodeEvent:84:38"];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, wrong_argument_number: 0, claim_wrong_number: 0,
     reasoning_wrong_number: 0, evidence_wrong_number: 0, backing_info_phrase: "did not open" });
} else {
  // 2) Previous trigger (attempt boundary)
  const prevTrigger = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY, _id: { $lt: latestTrigger._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = prevTrigger ? prevTrigger._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;
  const windowFilter = { _id: { $gt: windowStartId, $lte: windowEndId } };

  const countIn = (keys) => db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: keys }, ...windowFilter
  });

  const sumCount = countIn(COLOR_TARGET_KEYS);   // mirrors the color script
  const wrongCount = countIn(WRONG_KEYS);        // honest wrong-submission count
  const claimCount = countIn(CLAIM_NEG_KEYS);
  const reasoningCount = countIn(REASONING_NEG_KEYS);
  const evidenceCount = countIn(EVIDENCE_STRUCT_NEG_KEYS);

  let baseScore;
  if (sumCount <= 3) baseScore = 3;
  else if (sumCount === 4) baseScore = 2;
  else if (sumCount === 5) baseScore = 1;
  else baseScore = 0;

  const hasBonus =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventType: "argumentationToolEvent",
      "data.toolName": "BackingInfoPanel - Pollution Site Data",
      ...windowFilter
    }, { projection: { _id: 1 } }) !== null;

  ({
    triggered: (baseScore + (hasBonus ? 1 : 0)) < 3,
    wrong_argument_number: wrongCount,
    claim_wrong_number: claimCount,
    reasoning_wrong_number: reasoningCount,
    evidence_wrong_number: evidenceCount,
    backing_info_phrase: hasBonus ? "opened" : "did not open"
  });
}
```

### Teacher Guidance
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.
