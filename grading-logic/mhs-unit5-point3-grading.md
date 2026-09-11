# Unit 5 Point 3 Grading

**Activity:** What Happened Here?

**Trigger(Start) Event:** `DialogueNodeEvent:96:1`
**Trigger(End) Event:** `questFinishEvent:44`

---

## Grading Rule

This progress point is an attempt-based, if the total number of following dialogues (`DialogueNodeEvent:108:25`,`DialogueNodeEvent:108:32`,`DialogueNodeEvent:108:33`,`DialogueNodeEvent:108:37`,`DialogueNodeEvent:108:39`,`DialogueNodeEvent:108:41`,`DialogueNodeEvent:108:47`,`DialogueNodeEvent:108:53`,`DialogueNodeEvent:108:54`,`DialogueNodeEvent:108:55`,`DialogueNodeEvent:108:59`,`DialogueNodeEvent:108:60`,`DialogueNodeEvent:108:61`,`DialogueNodeEvent:108:62`,`DialogueNodeEvent:108:70`,`DialogueNodeEvent:108:72`,`DialogueNodeEvent:108:73`,`DialogueNodeEvent:108:74`,`DialogueNodeEvent:108:75`,`DialogueNodeEvent:108:76`,`DialogueNodeEvent:108:78`,`DialogueNodeEvent:108:79`,`DialogueNodeEvent:108:80`,`DialogueNodeEvent:108:82`,`DialogueNodeEvent:108:83`,`DialogueNodeEvent:108:84`,`DialogueNodeEvent:108:85`,`DialogueNodeEvent:108:86`,`DialogueNodeEvent:108:87`,`DialogueNodeEvent:108:88`,`DialogueNodeEvent:108:89`,`DialogueNodeEvent:108:90`,`DialogueNodeEvent:108:91`) happened is euqal to or larger than 4 then the color returns yellow, otherwise it will return green.

| Outcome | Condition |
|---------|-----------|
| **Green** | attempt <= 4 |
| **Yellow** | attempt > 4 |

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:96:1` (exclusive)
- **End:** Latest `questFinishEvent:44` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:44` |
| Target | `DialogueNodeEvent:108:25` |
| Target | `DialogueNodeEvent:108:32` |
| Target | `DialogueNodeEvent:108:33` |
| Target | `DialogueNodeEvent:108:37` |
| Target | `DialogueNodeEvent:108:39` |
| Target | `DialogueNodeEvent:108:41` |
| Target | `DialogueNodeEvent:108:47` |
| Target | `DialogueNodeEvent:108:53` |
| Target | `DialogueNodeEvent:108:54` |
| Target | `DialogueNodeEvent:108:55` |
| Target | `DialogueNodeEvent:108:59` |
| Target | `DialogueNodeEvent:108:60` |
| Target | `DialogueNodeEvent:108:61` |
| Target | `DialogueNodeEvent:108:62` |
| Target | `DialogueNodeEvent:108:70` |
| Target | `DialogueNodeEvent:108:72` |
| Target | `DialogueNodeEvent:108:73` |
| Target | `DialogueNodeEvent:108:74` |
| Target | `DialogueNodeEvent:108:75` |
| Target | `DialogueNodeEvent:108:76` |
| Target | `DialogueNodeEvent:108:78` |
| Target | `DialogueNodeEvent:108:79` |
| Target | `DialogueNodeEvent:108:80` |
| Target | `DialogueNodeEvent:108:82` |
| Target | `DialogueNodeEvent:108:83` |
| Target | `DialogueNodeEvent:108:84` |
| Target | `DialogueNodeEvent:108:85` |
| Target | `DialogueNodeEvent:108:86` |
| Target | `DialogueNodeEvent:108:87` |
| Target | `DialogueNodeEvent:108:88` |
| Target | `DialogueNodeEvent:108:89` |
| Target | `DialogueNodeEvent:108:90` |
| Target | `DialogueNodeEvent:108:91` |

---

## Analytics Script

```js
// Unit 5, Point 3 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:44"

const playerId = "<playerId>";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
  "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
  "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
  "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
  "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:70",
  "DialogueNodeEvent:108:72", "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74",
  "DialogueNodeEvent:108:75", "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78",
  "DialogueNodeEvent:108:79", "DialogueNodeEvent:108:80", "DialogueNodeEvent:108:82",
  "DialogueNodeEvent:108:83", "DialogueNodeEvent:108:84", "DialogueNodeEvent:108:85",
  "DialogueNodeEvent:108:86", "DialogueNodeEvent:108:87", "DialogueNodeEvent:108:88",
  "DialogueNodeEvent:108:89", "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91"
];

const cnt = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: NEGATIVE_KEYS }
});

const color = (cnt >= 4) ? "yellow" : "green";

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe attempt-based color script
// Window start: "DialogueNodeEvent:96:1"
// Window end:   "questFinishEvent:44"

const playerId = "<playerId>";

const WINDOW_START_KEY = "DialogueNodeEvent:96:1";
const WINDOW_END_KEY = "questFinishEvent:44";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
  "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
  "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
  "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
  "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:70",
  "DialogueNodeEvent:108:72", "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74",
  "DialogueNodeEvent:108:75", "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78",
  "DialogueNodeEvent:108:79", "DialogueNodeEvent:108:80", "DialogueNodeEvent:108:82",
  "DialogueNodeEvent:108:83", "DialogueNodeEvent:108:84", "DialogueNodeEvent:108:85",
  "DialogueNodeEvent:108:86", "DialogueNodeEvent:108:87", "DialogueNodeEvent:108:88",
  "DialogueNodeEvent:108:89", "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91"
];

// 1) Most recent window start
const latestStart = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_START_KEY
  },
  { sort: { _id: -1 }}
);

// 2) Most recent window end
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 }}
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  "yellow";
} else {
  const windowStartId = latestStart._id;
  const windowEndId = latestEnd._id;

  const cnt = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  cnt >= 4 ? "yellow" : "green";
}
```

---

## Reason Codes

### Conversation-108 Feedback Nodes by Argument Component

All keys are `DialogueNodeEvent:108:<n>`. Each flagged submission fires one
component-specific feedback node; many exist as multiple phrasing variants of
the same problem. The color rule counts all 33 nodes below.

| Category | Nodes | Feedback gist |
|----------|-------|---------------|
| Claim — restating Aryn's claim | 32, 33, 37, 41, 70, 72, 73, 74, 75, 76, 78, 79 | "You are restating Aryn's claim. We are pretty sure this is incorrect — try building an argument that doesn't align with what Aryn says" (12 alignment/phrasing variants) |
| Reasoning — too many / redundant | 39, 53, 54, 55, 90, 91 | "Too many reasoning statements" / "Your reasoning statements are redundant — select one that explains why your evidence supports your claim" |
| Reasoning — misconceptions | 59, 84, 85 | "Are you sure the water is being filtered?" — reasoning does not describe how water behaves in nature |
| Reasoning — misconceptions | 61, 86 | "Are you sure the water is being transformed into salt?" |
| Reasoning — mismatch | 60, 62, 87 | "Claim and evidence make sense, but your reasoning does not match the rest of your argument" |
| Reasoning — doesn't connect evidence | 88, 89 | "Your reasoning should connect all of your pieces of evidence with your claim" |
| Evidence | 25, 80, 82, 83 | Evidence does not support the claim ("the amount of salt in the collector does not explain what happens to the water"); "claim sounds good — try different evidence" |
| Completeness | 47 | "Your argument is incomplete. Make sure you have included all three parts." |

Nodes that are **not** in the color rule:

| Node | Meaning |
|------|---------|
| `108:48`, `108:49` | "Click the Backing Information orbs" nudges — fire after every negative; ungraded by design |
| `108:51`, `108:52` | "Great Job Cadet!!! You have made the best argument possible." — ideal-argument success; NOT required by the color rule, and run 09-03-26-3 completed the quest (yellow) without it firing |
| `108:63`, `108:64` | "Could use another piece of evidence — add one more to make your argument stronger" (softer improvement feedback) — **flagged for review**: near-identical twins of graded nodes are included (e.g. 65 vs 88), so confirm whether the 63–69 set is deliberately ungraded or an oversight |
| `108:65`, `108:66`, `108:68`, `108:69` | Same-text twins of graded nodes 88/89 and 82/83-family — **flagged for review**, as above |
| `108:0, 4, 8, 31, 38, 50, 56, 67, 71, 77, 81, 92` | Empty structural nodes |

Script bucket lists derived from these rows: claim = {32, 33, 37, 41, 70, 72, 73,
74, 75, 76, 78, 79}; reasoning = {39, 53, 54, 55, 59, 60, 61, 62, 84, 85, 86, 87,
88, 89, 90, 91}; evidence/completeness = {25, 80, 82, 83, 47}.

### EXCESS_ATTEMPTS

**Instructor Message:** In What Happened Here?, while building the argument about why the collected water disappeared, the student made {wrong_argument_number} flagged submissions - {claim_wrong_number} for restating Aryn's claim instead of arguing against it, {reasoning_wrong_number} for reasoning problems, and {evidence_wrong_number} for evidence or completeness problems. This point earns green only when fewer than 4 submissions are flagged. Claim errors suggest the student did not connect the evidence to the natural explanation - the water evaporated, leaving the salt behind - while the reasoning feedback names specific misconceptions to review, such as the water being filtered or transformed into salt.

#### Corresponding Script

```js
// U5P3: EXCESS_ATTEMPTS — determine trigger and component quantities
// Window mirrors the production color script: latest DialogueNodeEvent:96:1
// (start) to latest questFinishEvent:44 (end), end must not precede start.
// Triggers when the color rule goes yellow: 4+ flagged submissions (count-only —
// this point has NO success-node requirement; the ideal-argument nodes 108:51/52
// are not part of the color rule and may not fire even on completed runs).
// wrong_argument_number = total flagged submissions; the three component counts
// split it by the problem the feedback named. The softer twins 108:63-69 are
// currently NOT in the color rule (flagged for review) and are not counted here.
// Audit invariant: claim + reasoning + evidence counts = wrong_argument_number.

const playerId = "<playerId>";

const WINDOW_START_KEY = "DialogueNodeEvent:96:1";
const WINDOW_END_KEY = "questFinishEvent:44";

const CLAIM_NEG_KEYS = [            // restating Aryn's claim
  "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33", "DialogueNodeEvent:108:37",
  "DialogueNodeEvent:108:41", "DialogueNodeEvent:108:70", "DialogueNodeEvent:108:72",
  "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74", "DialogueNodeEvent:108:75",
  "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78", "DialogueNodeEvent:108:79"
];

const REASONING_NEG_KEYS = [
  "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:53",  // too many reasoning statements
  "DialogueNodeEvent:108:54", "DialogueNodeEvent:108:55",  // redundant reasoning
  "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91",  // too many reasoning statements
  "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:84",  // "water being filtered" misconception
  "DialogueNodeEvent:108:85",
  "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:86",  // "transformed into salt" misconception
  "DialogueNodeEvent:108:60", "DialogueNodeEvent:108:62",  // reasoning doesn't match the argument
  "DialogueNodeEvent:108:87",
  "DialogueNodeEvent:108:88", "DialogueNodeEvent:108:89"   // reasoning doesn't connect all evidence
];

const EVIDENCE_NEG_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:80",  // salt amount doesn't explain the water
  "DialogueNodeEvent:108:82", "DialogueNodeEvent:108:83",  // evidence doesn't support the claim
  "DialogueNodeEvent:108:47"                               // incomplete argument
];

const NEG_KEYS = [...CLAIM_NEG_KEYS, ...REASONING_NEG_KEYS, ...EVIDENCE_NEG_KEYS];

// 1) Window anchors (mirror of the color production script)
const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  // Missing/invalid window (incl. started-but-unfinished pencil case)
  ({ triggered: false, wrong_argument_number: 0, claim_wrong_number: 0,
     reasoning_wrong_number: 0, evidence_wrong_number: 0 });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  const countIn = (keys) => db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: keys }, ...windowFilter
  });

  const negCount = countIn(NEG_KEYS);

  ({
    triggered: negCount >= 4,
    wrong_argument_number: negCount,
    claim_wrong_number: countIn(CLAIM_NEG_KEYS),
    reasoning_wrong_number: countIn(REASONING_NEG_KEYS),
    evidence_wrong_number: countIn(EVIDENCE_NEG_KEYS)
  });
}
```

### Teacher Guidance
Review parts of an argument with students. Have students work through argumentation review followup activity.