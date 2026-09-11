# Unit 4 Point 5 Grading

**Activity:** Saving Cadet Anderson

**Trigger(Start) Event:** `questActiveEvent:36`
**Trigger(End) Event:** `questActiveEvent:41`

---

## Grading Rule

This progress point recording how players perform within the argumentation task. This will first check whether the player successfully construct the correct argumentation (whether their log record contains (`DialogueNodeEvent:90:50`, `DialogueNodeEvent:90:57`)).
Then it will check how many negative feedback got from the argumentation construction.
If there is no correct feedback then the color is yellow, or the negative feedback number surpass 4, or both then the color is yellow, otherwise green.

| Outcome | Condition |
|---------|-----------|
| **Green** | Have correct feedback and the negative feedback number is less than 4 |
| **Yellow** | Either no correct feedback or the negative feedback number is equal to or larger than 4 or both |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:36` (exclusive)
- **End:** Latest `questActiveEvent:41` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:41` |
| Target | `DialogueNodeEvent:90:50` |
| Target | `DialogueNodeEvent:90:57` |
| Target | `DialogueNodeEvent:90:25` |
| Target | `DialogueNodeEvent:90:37` |
| Target | `DialogueNodeEvent:90:39` |
| Target | `DialogueNodeEvent:90:45` |
| Target | `DialogueNodeEvent:90:47` |
| Target | `DialogueNodeEvent:90:52` |
| Target | `DialogueNodeEvent:90:54` |
| Target | `DialogueNodeEvent:90:55` |
| Target | `DialogueNodeEvent:90:56` |
| Target | `DialogueNodeEvent:90:58` |
| Target | `DialogueNodeEvent:90:59` |
| Target | `DialogueNodeEvent:90:60` |
| Target | `DialogueNodeEvent:90:61` |


---

## Analytics Script

```js
// Unit 4, Point 5 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:41"

const playerId = "<playerId>";

const POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"];

const NEG_KEYS = [
  "DialogueNodeEvent:90:25","DialogueNodeEvent:90:37","DialogueNodeEvent:90:39",
  "DialogueNodeEvent:90:45","DialogueNodeEvent:90:47","DialogueNodeEvent:90:52",
  "DialogueNodeEvent:90:54","DialogueNodeEvent:90:55","DialogueNodeEvent:90:56",
  "DialogueNodeEvent:90:58","DialogueNodeEvent:90:59","DialogueNodeEvent:90:60",
  "DialogueNodeEvent:90:61"
];

const has_trigger =
  db.logdata.findOne(
    { playerId: playerId, eventKey: { $in: POS_KEYS } }
  ) !== null;

let color;

if (!has_trigger) {
  color = 2; 
} else {
  const cnt = db.logdata.countDocuments({
    playerId: playerId,
    eventKey: { $in: NEG_KEYS }
  });

  color = (cnt >= 3) ? "yellow" : "green";
}

color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 5 — Production (replay-safe, latest attempt window)
// Trigger eventKey: "questActiveEvent:41"

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:41";

const POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"];

const NEG_KEYS = [
  "DialogueNodeEvent:90:25","DialogueNodeEvent:90:37","DialogueNodeEvent:90:39",
  "DialogueNodeEvent:90:45","DialogueNodeEvent:90:47","DialogueNodeEvent:90:52",
  "DialogueNodeEvent:90:54","DialogueNodeEvent:90:55","DialogueNodeEvent:90:56",
  "DialogueNodeEvent:90:58","DialogueNodeEvent:90:59","DialogueNodeEvent:90:60",
  "DialogueNodeEvent:90:61"
];

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

if (!latestTrigger) {
  "yellow";
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

  const windowStartId = prevTrigger
    ? prevTrigger._id
    : ObjectId("000000000000000000000000");

  const windowEndId = latestTrigger._id;

  const has_trigger =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: { $in: POS_KEYS },
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (!has_trigger) {
    "yellow";
  } else {
    const cnt = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: NEG_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    });

    cnt >= 3 ? "yellow" : "green";
  }
}
```

---

## Reason Codes

### Conversation-90 Feedback Nodes by Argument Component

All keys are `DialogueNodeEvent:90:<n>`. Each incorrect submission fires one
component-specific feedback node; several exist as base + stronger-hint pairs
that name the same problem.

| Category | Nodes | Feedback gist |
|----------|-------|---------------|
| Success — optimal | `90:50` | "Great job! You have made the best argument possible." |
| Success — after revisions | `90:57` | "Great job! You have made an argument that strongly combines claims, reasoning and evidence." |
| Claim | `90:37`, `90:55` | "Are you sure the flooding will resolve by turning off the fountain? Is there a better way to explain how water got into the warehouse?" (55 adds "consider changing your claim") |
| Reasoning | `90:25`, `90:56` | Reasoning does not connect the claim to the evidence in a scientifically accurate way (56 adds "rethink your reasoning") |
| Reasoning — misconception | `90:52`, `90:60` | "Water does not flow easily through bedrock" (60 adds "review the reasoning statements") |
| Reasoning — misconception | `90:54`, `90:61` | "Water does not infiltrate upward" (61 adds "review the reasoning statements") |
| Evidence | `90:39`, `90:58` | Argument may be missing important evidence (58 adds "try adding additional evidence") |
| Evidence | `90:45`, `90:59` | Evidence does not support the claim (59 notes claim and reasoning are correct — "reassess which evidence best supports your claim") |
| Completeness | `90:47` | "Your argument is incomplete. Make sure you have included all three parts." |

Nodes that are **not** graded: `90:48`, `90:49` — "click the Backing Information
orbs" hint nudges; `90:0`, `90:38`, `90:51`, `90:53` — empty structural nodes.
The script's three component key lists group these rows as: claim = {37, 55};
reasoning = {25, 56, 52, 60, 54, 61}; evidence/completeness = {39, 58, 45, 59, 47}.

### EXCESS_ATTEMPTS

**Instructor Message:** In Saving Cadet Anderson, the student built the argument explaining how water flooded the warehouse, but needed {attempt_number} submissions - {claim_wrong_number} flagged for the claim, {reasoning_wrong_number} for the reasoning, and {evidence_wrong_number} for evidence or completeness. This point earns green only when the correct argument is submitted with at most 2 incorrect submissions. Reasoning errors here reflect misconceptions the feedback names directly - water does not flow easily through bedrock, and water does not infiltrate upward - while claim errors suggest difficulty identifying the actual source of the flooding.

#### Corresponding Script

```js
// U4P5: EXCESS_ATTEMPTS - determine trigger and component quantities
// Window mirrors the production color script: trigger-to-trigger on questActiveEvent:41.
// triggered mirrors the color rule verbatim: no success node (90:50 first-try /
// 90:57 after revisions) OR 3+ negative submissions. Note: the color scripts use
// >= 3 (green = at most 2 negatives); the older prose saying ">= 4" is wrong.
// attempt_number = incorrect submissions + 1 when success is present.

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:41";

const POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"];

const CLAIM_NEG_KEYS = [
  "DialogueNodeEvent:90:37", "DialogueNodeEvent:90:55"
];
const REASONING_NEG_KEYS = [
  "DialogueNodeEvent:90:25", "DialogueNodeEvent:90:56",
  "DialogueNodeEvent:90:52", "DialogueNodeEvent:90:60",  // bedrock misconception
  "DialogueNodeEvent:90:54", "DialogueNodeEvent:90:61"   // infiltrate-upward misconception
];
const EVIDENCE_NEG_KEYS = [
  "DialogueNodeEvent:90:39", "DialogueNodeEvent:90:58",  // missing evidence
  "DialogueNodeEvent:90:45", "DialogueNodeEvent:90:59",  // unsupportive evidence
  "DialogueNodeEvent:90:47"                              // incomplete argument
];

const NEG_KEYS = [...CLAIM_NEG_KEYS, ...REASONING_NEG_KEYS, ...EVIDENCE_NEG_KEYS];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, attempt_number: 0, claim_wrong_number: 0,
     reasoning_wrong_number: 0, evidence_wrong_number: 0 });
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

  const hasSuccess = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: { $in: POS_KEYS }, ...windowFilter
  }) !== null;

  const negCount = countIn(NEG_KEYS);

  ({
    triggered: !hasSuccess || negCount >= 3,
    attempt_number: negCount + (hasSuccess ? 1 : 0),
    claim_wrong_number: countIn(CLAIM_NEG_KEYS),
    reasoning_wrong_number: countIn(REASONING_NEG_KEYS),
    evidence_wrong_number: countIn(EVIDENCE_NEG_KEYS)
  });
}
```

### Teacher Guidance
Review the components of a scientific argument with the student:
1. Claim: a statement that answers the driving question
2. Evidence: scientific data and facts that support the claim
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.