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

`DialogueNodeEvent:27:11` through `DialogueNodeEvent:27:30` (15 keys; `27:19` and `27:21`–`27:24` do not exist in the dialogue database)

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

**Instructor Message:** In Which Watershed? Part II, the student built the argument about which watershed is larger, but needed {attempt_number} submissions - {wrong_claim_number} where only the claim was wrong, {both_wrong_number} where both the claim and the evidence were wrong, and {irrelevant_evidence_number} where the claim was right but the evidence does not indicate watershed size (waterfall height, salinity, the downstream river, or several pieces at once). This point earns green only when the correct argument is submitted within 4 attempts. Repeated incorrect submissions may indicate difficulty selecting the claim the data supports and distinguishing relevant evidence - flow rate reflects how much land drains to each river - from irrelevant observations.

#### Correspoinding Script

```js
// U2P7: EXCESS_ATTEMPTS - determine trigger and quantities
// Triggers when the color rule goes yellow in the attempt window:
// success (27:7) missing OR more than 3 incorrect submissions.
// (questFinishEvent:54 only fires after the argument completes, so in
// practice success is present and the trigger means 4+ wrong submissions.)
// attempt_number = incorrect submissions + 1 (the final correct submission).
// The three sub-counts split the incorrect submissions by ARGUMENT STATE (the
// conversation-27 branch gate that fired), not by wording: every feedback is a
// generic/specific pair selected by argSpecificFeedback, and both members of a
// pair describe the same mistake (reviewed against the 2026-06-10 Unity
// dialogue export on 2026-09-17).
//   gate 27:31       claim I + evidence A (flow rate)   -> 27:11 / 27:12   only the claim is wrong
//   gates 27:4/5/6   claim I + evidence B / C / D       -> 27:13 - 27:18   claim AND evidence wrong
//   gates 27:8/9/10  claim II + evidence B / C / D      -> 27:25 - 27:30   only the evidence is wrong
//   (any claim)      several pieces of evidence at once -> 27:20           evidence-selection problem
// Audit invariants: wrong_claim_number + both_wrong_number +
// irrelevant_evidence_number = negCount, and count of structural node 27:0 in
// the window = total submissions.

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:54";
const SUCCESS_KEY = "DialogueNodeEvent:27:7"; // "Well done! You have made the best argument possible."

const WRONG_CLAIM_KEYS = [           // claim I with the flow-rate evidence (A): only the claim is wrong
  "DialogueNodeEvent:27:11",  // generic: evidence doesn't fit the claim (backing-info pointer)
  "DialogueNodeEvent:27:12"   // specific: try a more appropriate claim
];

const BOTH_WRONG_KEYS = [            // claim I with irrelevant evidence: claim AND evidence wrong
  "DialogueNodeEvent:27:13", "DialogueNodeEvent:27:14",  // waterfall height (B)
  "DialogueNodeEvent:27:15", "DialogueNodeEvent:27:16",  // salinity (C)
  "DialogueNodeEvent:27:17", "DialogueNodeEvent:27:18"   // downstream river (D)
];

const IRRELEVANT_EVIDENCE_KEYS = [   // claim II (correct) with evidence that does not indicate watershed size
  "DialogueNodeEvent:27:25", "DialogueNodeEvent:27:26",  // waterfall height (B)
  "DialogueNodeEvent:27:27", "DialogueNodeEvent:27:28",  // salinity (C)
  "DialogueNodeEvent:27:29", "DialogueNodeEvent:27:30",  // downstream river (D)
  "DialogueNodeEvent:27:20"                              // several pieces of evidence at once (any claim)
];

const NEG_KEYS = [
  ...WRONG_CLAIM_KEYS,
  ...BOTH_WRONG_KEYS,
  ...IRRELEVANT_EVIDENCE_KEYS
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, attempt_number: 0, wrong_claim_number: 0, both_wrong_number: 0, irrelevant_evidence_number: 0 });
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

  const countIn = (keys) => db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: keys }, ...windowFilter
  });

  // 3) Student reached the correct-argument completion
  const hasSuccess =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: SUCCESS_KEY, ...windowFilter
    }) !== null;

  // 4) Counts inside the window
  const negCount = countIn(NEG_KEYS);
  const claimCount = countIn(WRONG_CLAIM_KEYS);
  const bothCount = countIn(BOTH_WRONG_KEYS);
  const evidenceCount = countIn(IRRELEVANT_EVIDENCE_KEYS);

  // 5) Mirror the color rule exactly
  const triggered = !(hasSuccess && negCount <= 3);

  ({
    triggered: triggered,
    attempt_number: hasSuccess ? negCount + 1 : negCount,
    wrong_claim_number: claimCount,
    both_wrong_number: bothCount,
    irrelevant_evidence_number: evidenceCount
  });
}
```

### Teacher Guidance
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.