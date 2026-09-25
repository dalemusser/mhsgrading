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

- **Start:** Latest `DialogueNodeEvent:11:34` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `questFinishEvent:18` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the previous-and-latest end window (previous `questFinishEvent:18` exclusive .. latest `questFinishEvent:18` inclusive), per the start-and-end window decision (A1). Keys re-verified the same day against the 2026-09-21 dialogue database (conversation 84 unchanged: 24 nodes, same gates). The bonus lookup now also starts at `11:34`, so Unit 2's backing-info panel events can no longer fall inside the window. Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role            | Event Key                   |
|-----------------|-----------------------------|
| Trigger (Start) | `DialogueNodeEvent:11:34`   |
| Trigger (End)   | `questFinishEvent:18`       |

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
// Window start: latest DialogueNodeEvent:11:34 before the end event (exclusive)
// Window end:   latest questFinishEvent:18 (inclusive)

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:11:34";
const END_KEY = "questFinishEvent:18";

const TARGET_KEYS = [
  "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
  "DialogueNodeEvent:84:36", "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:38",
  "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40", "DialogueNodeEvent:84:41",
  "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43", "DialogueNodeEvent:84:44",
  "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46", "DialogueNodeEvent:84:47"
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  "yellow";
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: START_KEY,
      _id: { $lt: latestEnd._id }
    },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowEndId = latestEnd._id;

  // 3) Target count and bonus inside the window
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

**Instructor Message:** In Pollution Argument, while constructing the argument about where the pollutant enters the river, the student made {wrong_argument_number} incorrect submissions ({claim_wrong_number} with a claim problem, {reasoning_wrong_number} with a reasoning problem, and {evidence_wrong_number} with an evidence or structure problem), and {backing_info_phrase} the Pollution Site Data reference panel. This point earns green only when incorrect submissions stay within the limit (at most 3, or one more when the reference panel has been consulted, which earns a bonus point). Errors concentrated on reasoning may indicate difficulty explaining how pollution travels downstream with the water flow, which is the link between the sensor evidence and the claim.

#### Conversation-84 Feedback Nodes by Argument Component

All keys are `DialogueNodeEvent:84:<n>`. The conversation branches on the argument
state through player gate nodes (claim I + evidence A is the correct pair, reasoning
5 the correct reasoning); each incorrect submission fires exactly one Dr. Toppo
feedback node. Most feedback exists as a generic/specific pair chosen by the game's
`argSpecificFeedback` flag; both members of a pair describe the same mistake, so the
categories below follow the argument state (the gate), not the wording. Reviewed
against the 2026-06-10 Unity dialogue export on 2026-09-17; re-verified unchanged
against the 2026-09-21 export on 2026-09-24.

| Category | Branch (player gate) | Nodes | Feedback gist |
|----------|----------------------|-------|---------------|
| Claim | claim II, evidence A — only the claim is wrong (gate 38) | 39, 45 | "Your claim does not take into consideration that water can carry pollution" |
| Claim | claim II, evidence B — claim and evidence both wrong; the feedback addresses the claim (gate 8) | 25, 46 (reasoning 1, 2, 3 or 5); 40 (reasoning 4: "Your argument is logical. But it does not accurately describe how water moves.") | Same claim problem; 40 is the reasoning-4 variant at the same gate |
| Reasoning | claim I, evidence A — only the reasoning is wrong (gate 31) | 32, 41 (reasoning 1); 33, 42 (reasoning 2); 34, 43 (reasoning 3); 35, 44 (reasoning 4) | Reasoning does not explain the location of the pollution / how water behaves; "water must flow north to south" is not always true; reasoning does not match the evidence |
| Evidence / structure | claim I, evidence B — wrong evidence, any reasoning (gate 4) | 37 | "Your evidence does not match up with the rest of your argument" |
| Evidence / structure | several pieces of evidence at once, any claim | 20 | Multiple evidence pieces used (the node text still says "size of a watershed" — Unit 2 wording; report to the design team) |
| Evidence / structure | any component missing | 47 | "Your argument is incomplete" |

Nodes that are **not** incorrect submissions:

| Node | Meaning |
|------|---------|
| `84:36` | Success — "Great Job! You made the best argument possible." Counted in the color scripts' TARGET_KEYS on purpose: it makes the count equal the number of attempts, so the base-score bands (≤ 3 / 4 / 5 / ≥ 6) equal the working document's attempt bands |
| `84:38` | Branch gate for claim II + evidence A (a player node that never logs); listed in TARGET_KEYS but inert |
| `84:48`, `84:49` | Hint nudges — "click the Backing Information orbs" (ungraded by design) |
| `84:0`, `84:4`, `84:8`, `84:31` | Start node and branch gates, never logged |

Unobserved state (report to the dev team): at gate 8 the reasoning-4 feedback exists
only in its generic variant (`84:40`); once the specific-wording flag is on, a claim II +
evidence B + reasoning 4 submission has no matching node and would go uncounted.

#### Corresponding Script

```js
// U3P3: EXCESS_ATTEMPTS — determine trigger and quantities
// Window mirrors the production color script: latest questFinishEvent:18 (end),
// latest DialogueNodeEvent:11:34 before it (start, exclusive; zero ObjectId when none).
// triggered mirrors the color formula verbatim: base score from the color
// script's TARGET_KEYS count (which includes success node 84:36 by design —
// the count then equals the number of attempts — and the inert gate 84:38),
// plus 1 bonus for opening the Pollution Site Data panel; yellow when total < 3.
// The quantities report honest counts: wrong_argument_number excludes 84:36/38,
// and the three component counts split it by ARGUMENT STATE (the conversation-84
// branch gate), so a generic/specific pair and the gate's reasoning variants
// always land in the same bucket (reviewed against the Unity export 2026-09-17).

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:11:34";
const END_KEY = "questFinishEvent:18";

const CLAIM_NEG_KEYS = [
  "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:45",  // claim II + evidence A: only the claim is wrong
  "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:46",  // claim II + evidence B, reasoning 1/2/3/5: claim problem named
  "DialogueNodeEvent:84:40"                              // claim II + evidence B, reasoning 4: same gate
];
const REASONING_NEG_KEYS = [                             // claim I + evidence A: only the reasoning is wrong
  "DialogueNodeEvent:84:32", "DialogueNodeEvent:84:41",  // reasoning 1: does not explain the pollution's location
  "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:42",  // reasoning 2: does not explain how water behaves
  "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:43",  // reasoning 3: "water must flow north to south"
  "DialogueNodeEvent:84:35", "DialogueNodeEvent:84:44"   // reasoning 4: does not match the evidence
];
const EVIDENCE_STRUCT_NEG_KEYS = [
  "DialogueNodeEvent:84:37",  // claim I + evidence B: evidence doesn't match the argument
  "DialogueNodeEvent:84:20",  // multiple evidence pieces used
  "DialogueNodeEvent:84:47"   // incomplete argument
];

const WRONG_KEYS = [...CLAIM_NEG_KEYS, ...REASONING_NEG_KEYS, ...EVIDENCE_STRUCT_NEG_KEYS];

// Color-rule key list, kept verbatim so triggered matches the cell (incl. 36/38)
const COLOR_TARGET_KEYS = [...WRONG_KEYS, "DialogueNodeEvent:84:36", "DialogueNodeEvent:84:38"];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  ({ triggered: false, wrong_argument_number: 0, claim_wrong_number: 0,
     reasoning_wrong_number: 0, evidence_wrong_number: 0, backing_info_phrase: "did not open" });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowEndId = latestEnd._id;
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
