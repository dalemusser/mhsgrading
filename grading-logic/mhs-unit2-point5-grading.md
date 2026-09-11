# Unit 2 Point 5 Grading

**Activity:** Classified Information

**Trigger(Start) Event:** `DialogueNodeEvent:23:17`
**Trigger(End) Event:** `DialogueNodeEvent:23:42`

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

All keys are `DialogueNodeEvent:26:<n>`. ✓ = correct classification ("Nice Job!"/"Great!");
✗ = incorrect classification ("Too bad!"/"Oh no!" — the node names the component the passage actually was).

| Argument item | Claim ✓ | Reasoning ✓ | Evidence ✓ | Claim ✗ | Reasoning ✗ | Evidence ✗ |
|---------------|---------|-------------|------------|---------|-------------|------------|
| East/West well cleanliness | 140 | 142 | 143 | 137 | 144 | 145 |
| Ocean evaporation          | 146 | 147 | 148 | 187 | 188 | 189 |
| Pool water from air        | 165 | 166 | 167 | 191 | 192 | 193 |
| Water pollution            | 168 | 169 | 170 | 194 | 195 | 196 |
| Salt dissolving            | 172 | 173 | 174 | 197 | 198 | 199 |
| Ice is frozen water        | 175 | 176 | 177 | 200 | 201 | 202 |
| Steam is gaseous water     | 178 | 179 | 180 | 203 | 204 | 205 |
| Burning match molecules    | 181 | 182 | 183 | 206 | 207 | 208 |
| Ball mass and speed        | 184 | 185 | 186 | 209 | 210 | 211 |

Structural nodes (no component semantics): `26:141` fires once after every correct
selection, `26:138` once after every incorrect selection (audit cross-check:
count(138) = total negatives), `26:136` = activity completion. `26:171` does not
exist in the dialogue database; `26:190` is an empty, unused node — neither
belongs in any key list.

---

## Analytics Script

```js
// Unit 2, Point 5 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:23:42"

const playerId = "<playerId>";

const POS_KEYS = [
  "DialogueNodeEvent:26:140", "DialogueNodeEvent:26:142",
  "DialogueNodeEvent:26:143", "DialogueNodeEvent:26:146",
  "DialogueNodeEvent:26:147", "DialogueNodeEvent:26:148",
  "DialogueNodeEvent:26:165", "DialogueNodeEvent:26:166", "DialogueNodeEvent:26:167",
  "DialogueNodeEvent:26:168", "DialogueNodeEvent:26:169", "DialogueNodeEvent:26:170", "DialogueNodeEvent:26:172", "DialogueNodeEvent:26:173",
  "DialogueNodeEvent:26:174", "DialogueNodeEvent:26:175", "DialogueNodeEvent:26:176",
  "DialogueNodeEvent:26:177", "DialogueNodeEvent:26:178", "DialogueNodeEvent:26:179",
  "DialogueNodeEvent:26:180", "DialogueNodeEvent:26:181", "DialogueNodeEvent:26:182",
  "DialogueNodeEvent:26:183", "DialogueNodeEvent:26:184", "DialogueNodeEvent:26:185",
  "DialogueNodeEvent:26:186"
];

const NEG_KEYS = [
  "DialogueNodeEvent:26:137", "DialogueNodeEvent:26:144",
  "DialogueNodeEvent:26:145",
  "DialogueNodeEvent:26:187", "DialogueNodeEvent:26:188", "DialogueNodeEvent:26:189", "DialogueNodeEvent:26:191", "DialogueNodeEvent:26:192",
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
  "DialogueNodeEvent:26:140", "DialogueNodeEvent:26:142",
  "DialogueNodeEvent:26:143", "DialogueNodeEvent:26:146",
  "DialogueNodeEvent:26:147", "DialogueNodeEvent:26:148",
  "DialogueNodeEvent:26:165", "DialogueNodeEvent:26:166", "DialogueNodeEvent:26:167",
  "DialogueNodeEvent:26:168", "DialogueNodeEvent:26:169", "DialogueNodeEvent:26:170", "DialogueNodeEvent:26:172", "DialogueNodeEvent:26:173",
  "DialogueNodeEvent:26:174", "DialogueNodeEvent:26:175", "DialogueNodeEvent:26:176",
  "DialogueNodeEvent:26:177", "DialogueNodeEvent:26:178", "DialogueNodeEvent:26:179",
  "DialogueNodeEvent:26:180", "DialogueNodeEvent:26:181", "DialogueNodeEvent:26:182",
  "DialogueNodeEvent:26:183", "DialogueNodeEvent:26:184", "DialogueNodeEvent:26:185",
  "DialogueNodeEvent:26:186"
];

const NEG_KEYS = [
  "DialogueNodeEvent:26:137", "DialogueNodeEvent:26:144",
  "DialogueNodeEvent:26:145",
  "DialogueNodeEvent:26:187", "DialogueNodeEvent:26:188", "DialogueNodeEvent:26:189", "DialogueNodeEvent:26:191", "DialogueNodeEvent:26:192",
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

---

## Reason Codes

### EXCESS_MISCLASSIFICATIONS

**Instructor Message:** In Classified Information, while repairing DANI by classifying highlighted passages of a scientific argument, the student made {wrong_number} incorrect classifications - {claim_wrong} on passages that were claims, {reasoning_wrong} on reasoning, and {evidence_wrong} on evidence. This point earns green only when the student completes all six classifications with at most 6 incorrect selections. Errors concentrated on one component may indicate difficulty recognizing that component's role: a claim states the conclusion, evidence provides information collected from the environment, and reasoning explains how the evidence supports the claim.

#### Correspoinding Script

```js
// U2P5: EXCESS_MISCLASSIFICATIONS — determine trigger and quantities
// Triggers when the color formula goes yellow: score = posCount - negCount/3 < 4
// (with the activity completed, this is equivalent to 7+ incorrect selections).
// wrong_number = total incorrect classifications; the three component counts
// break it down by what the misclassified passage actually was (claim /
// reasoning / evidence) — the logs do not record which wrong label the
// student chose, only which component they failed to recognize.
// Audit invariants: claim + reasoning + evidence = wrong_number, and
// count of structural node 26:138 in the window = wrong_number.

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:42";

const POS_KEYS = [
  // claim correct
  "DialogueNodeEvent:26:140", "DialogueNodeEvent:26:146", "DialogueNodeEvent:26:165",
  "DialogueNodeEvent:26:168", "DialogueNodeEvent:26:172", "DialogueNodeEvent:26:175",
  "DialogueNodeEvent:26:178", "DialogueNodeEvent:26:181", "DialogueNodeEvent:26:184",
  // reasoning correct
  "DialogueNodeEvent:26:142", "DialogueNodeEvent:26:147", "DialogueNodeEvent:26:166",
  "DialogueNodeEvent:26:169", "DialogueNodeEvent:26:173", "DialogueNodeEvent:26:176",
  "DialogueNodeEvent:26:179", "DialogueNodeEvent:26:182", "DialogueNodeEvent:26:185",
  // evidence correct
  "DialogueNodeEvent:26:143", "DialogueNodeEvent:26:148", "DialogueNodeEvent:26:167",
  "DialogueNodeEvent:26:170", "DialogueNodeEvent:26:174", "DialogueNodeEvent:26:177",
  "DialogueNodeEvent:26:180", "DialogueNodeEvent:26:183", "DialogueNodeEvent:26:186"
];

const CLAIM_NEG_KEYS = [        // passage was a claim
  "DialogueNodeEvent:26:137", "DialogueNodeEvent:26:187", "DialogueNodeEvent:26:191",
  "DialogueNodeEvent:26:194", "DialogueNodeEvent:26:197", "DialogueNodeEvent:26:200",
  "DialogueNodeEvent:26:203", "DialogueNodeEvent:26:206", "DialogueNodeEvent:26:209"
];

const REASONING_NEG_KEYS = [    // passage was reasoning
  "DialogueNodeEvent:26:144", "DialogueNodeEvent:26:188", "DialogueNodeEvent:26:192",
  "DialogueNodeEvent:26:195", "DialogueNodeEvent:26:198", "DialogueNodeEvent:26:201",
  "DialogueNodeEvent:26:204", "DialogueNodeEvent:26:207", "DialogueNodeEvent:26:210"
];

const EVIDENCE_NEG_KEYS = [     // passage was evidence
  "DialogueNodeEvent:26:145", "DialogueNodeEvent:26:189", "DialogueNodeEvent:26:193",
  "DialogueNodeEvent:26:196", "DialogueNodeEvent:26:199", "DialogueNodeEvent:26:202",
  "DialogueNodeEvent:26:205", "DialogueNodeEvent:26:208", "DialogueNodeEvent:26:211"
];

const NEG_KEYS = [
  ...CLAIM_NEG_KEYS,
  ...REASONING_NEG_KEYS,
  ...EVIDENCE_NEG_KEYS
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, wrong_number: 0, claim_wrong: 0, reasoning_wrong: 0, evidence_wrong: 0 });
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

  // 3) Counts inside the window
  const posCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: POS_KEYS }, ...windowFilter
  });

  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS }, ...windowFilter
  });

  const claimWrong = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: CLAIM_NEG_KEYS }, ...windowFilter
  });

  const reasoningWrong = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: REASONING_NEG_KEYS }, ...windowFilter
  });

  const evidenceWrong = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: EVIDENCE_NEG_KEYS }, ...windowFilter
  });

  // 4) Mirror the color rule exactly
  const score = posCount - (negCount / 3.0);

  ({
    triggered: score < 4,
    wrong_number: negCount,
    claim_wrong: claimWrong,
    reasoning_wrong: reasoningWrong,
    evidence_wrong: evidenceWrong
  });
}
```

### Teacher Guidance
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.