# Unit 2 Point 7 Grading

**Activity:** Which Watershed? Part II

**Trigger(Start) Event:** `DialogueNodeEvent:20:46`
**Trigger(End) Event:** `questFinishEvent:54`

---

## Grading Rule

Student must successfully build the watershed argument with limited incorrect evidence selections.

| Outcome | Condition |
|---------|-----------|
| **Green** | Success key present AND neg_count <= 3 in attempt window |
| **Yellow** | Success key missing OR neg_count > 3, or no trigger exists |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:54` (exclusive)
- **End:** Latest `questFinishEvent:54` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:54` |
| Success | `DialogueNodeEvent:27:7` |

**Negative Keys (incorrect evidence selections):**

`DialogueNodeEvent:27:11` through `DialogueNodeEvent:27:30` (20 keys)

<details>
<summary>Full list</summary>

- `DialogueNodeEvent:27:11`
- `DialogueNodeEvent:27:12`
- `DialogueNodeEvent:27:13`
- `DialogueNodeEvent:27:14`
- `DialogueNodeEvent:27:15`
- `DialogueNodeEvent:27:16`
- `DialogueNodeEvent:27:17`
- `DialogueNodeEvent:27:18`
- `DialogueNodeEvent:27:20`
- `DialogueNodeEvent:27:25`
- `DialogueNodeEvent:27:26`
- `DialogueNodeEvent:27:27`
- `DialogueNodeEvent:27:28`
- `DialogueNodeEvent:27:29`
- `DialogueNodeEvent:27:30`

</details>

---

## Analytics Script

```js
// Unit 2, Point 7 — Analytics-matching script (lifetime)
// Trigger eventKey: "questFinishEvent:54"

const playerId = "<playerId>";

const SUCCESS_KEY = "DialogueNodeEvent:27:7";

const NEG_KEYS = [
  "DialogueNodeEvent:27:11", "DialogueNodeEvent:27:12", "DialogueNodeEvent:27:13", "DialogueNodeEvent:27:14",
  "DialogueNodeEvent:27:15", "DialogueNodeEvent:27:16", "DialogueNodeEvent:27:17", "DialogueNodeEvent:27:18", "DialogueNodeEvent:27:20", "DialogueNodeEvent:27:25", "DialogueNodeEvent:27:26",
  "DialogueNodeEvent:27:27", "DialogueNodeEvent:27:28", "DialogueNodeEvent:27:29", "DialogueNodeEvent:27:30"
];

const hasSuccess =
  db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: SUCCESS_KEY
  }) !== null;

const negCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: NEG_KEYS }
});

const color = hasSuccess && negCount <= 3 ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 7 — Attempt-based standalone production grading script
// Trigger eventKey: "questFinishEvent:54"

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:54";
const SUCCESS_KEY = "DialogueNodeEvent:27:7";

const NEG_KEYS = [
  "DialogueNodeEvent:27:11", "DialogueNodeEvent:27:12", "DialogueNodeEvent:27:13", "DialogueNodeEvent:27:14",
  "DialogueNodeEvent:27:15", "DialogueNodeEvent:27:16", "DialogueNodeEvent:27:17", "DialogueNodeEvent:27:18", "DialogueNodeEvent:27:20", "DialogueNodeEvent:27:25", "DialogueNodeEvent:27:26",
  "DialogueNodeEvent:27:27", "DialogueNodeEvent:27:28", "DialogueNodeEvent:27:29", "DialogueNodeEvent:27:30"
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
      game: "mhs", playerId: playerId,
      eventKey: SUCCESS_KEY,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  (hasSuccess && negCount <= 3) ? "green" : "yellow";
}
```

---

## Reason Codes

### EXCESS_ATTEMPTS

**Instructor Message:** In Which Watershed? Part II, the student built the argument about which watershed is larger, but needed {attempt_number} submissions - {wrong_claim_number} where the claim did not match the evidence and reasoning, and {irrelevant_evidence_number} using evidence that does not indicate watershed size (waterfall height, salinity, or the downstream river). This point earns green only when the correct argument is submitted within 4 attempts. Repeated incorrect submissions may indicate difficulty selecting the claim the data supports and distinguishing relevant evidence - flow rate reflects how much land drains to each river - from irrelevant observations.

#### Correspoinding Script

```js
// U2P7: EXCESS_ATTEMPTS - determine trigger and quantities
// Triggers when the color rule goes yellow in the attempt window:
// success (27:7) missing OR more than 3 incorrect submissions.
// (questFinishEvent:54 only fires after the argument completes, so in
// practice success is present and the trigger means 4+ wrong submissions.)
// attempt_number = incorrect submissions + 1 (the final correct submission);
// the two sub-counts split the incorrect submissions by problem type -
// wrong/mismatched claim vs. irrelevant evidence.
// Audit invariants: wrong_claim_number + irrelevant_evidence_number = negCount,
// and count of structural node 27:0 in the window = total submissions.

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:54";
const SUCCESS_KEY = "DialogueNodeEvent:27:7"; // "Well done! You have made the best argument possible."

const WRONG_CLAIM_KEYS = [           // claim wrong or doesn't fit evidence & reasoning
  "DialogueNodeEvent:27:11",  // evidence doesn't fit claim (backing-info pointer)
  "DialogueNodeEvent:27:12",  // evidence doesn't fit claim — try another claim
  "DialogueNodeEvent:27:14",  // both claim and evidence don't link to reasoning
  "DialogueNodeEvent:27:16",  // both claim and evidence don't link to reasoning
  "DialogueNodeEvent:27:18"   // both claim and evidence don't link to reasoning
];

const IRRELEVANT_EVIDENCE_KEYS = [   // evidence doesn't indicate watershed size
  "DialogueNodeEvent:27:13",  // waterfall height
  "DialogueNodeEvent:27:25",  // waterfall height
  "DialogueNodeEvent:27:26",  // waterfall height (claim was correct)
  "DialogueNodeEvent:27:15",  // salinity
  "DialogueNodeEvent:27:27",  // salinity
  "DialogueNodeEvent:27:28",  // salinity
  "DialogueNodeEvent:27:17",  // downstream river
  "DialogueNodeEvent:27:29",  // downstream river
  "DialogueNodeEvent:27:30",  // downstream river
  "DialogueNodeEvent:27:20"   // multiple evidence pieces at once
];

const NEG_KEYS = [
  ...WRONG_CLAIM_KEYS,
  ...IRRELEVANT_EVIDENCE_KEYS
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, attempt_number: 0, wrong_claim_number: 0, irrelevant_evidence_number: 0 });
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

  const windowFilter = { _id: { $gt: windowStartId, $lte: windowEndId } };

  // 3) Student reached the correct-argument completion
  const hasSuccess =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: SUCCESS_KEY, ...windowFilter
    }) !== null;

  // 4) Counts inside the window
  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS }, ...windowFilter
  });

  const claimCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: WRONG_CLAIM_KEYS }, ...windowFilter
  });

  const evidenceCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: IRRELEVANT_EVIDENCE_KEYS }, ...windowFilter
  });

  // 5) Mirror the color rule exactly
  const triggered = !(hasSuccess && negCount <= 3);

  ({
    triggered: triggered,
    attempt_number: hasSuccess ? negCount + 1 : negCount,
    wrong_claim_number: claimCount,
    irrelevant_evidence_number: evidenceCount
  });
}
```

### Teacher Guidance
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.