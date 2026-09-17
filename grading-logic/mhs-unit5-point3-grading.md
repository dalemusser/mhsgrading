# Unit 5 Point 3 Grading

**Activity:** What Happened Here?

**Trigger(Start) Event:** `DialogueNodeEvent:96:1`
**Trigger(End) Event:** `questFinishEvent:44`

---

## Grading Rule

This progress point is attempt-based: it counts Dr. Toppo's wrong-answer feedback dialogues in the latest attempt window. Every incorrect submission fires exactly one of the 39 conversation-108 feedback nodes listed under Event Keys (each feedback exists as a generic/specific pair, selected by the game's `argSpecificFeedback` flag, and both members of every pair are counted). If the count is 4 or more the color is yellow, otherwise green. The success nodes (`DialogueNodeEvent:108:51`, `DialogueNodeEvent:108:52`) and the backing-information nudges (`DialogueNodeEvent:108:48`, `DialogueNodeEvent:108:49`) are not counted, and no success node is required.

| Outcome | Condition |
|---------|-----------|
| **Green** | fewer than 4 counted feedback dialogues in the window (0–3 incorrect submissions) |
| **Yellow** | 4 or more counted feedback dialogues in the window |

### Attempt Window (Production)

- **Start:** Latest `DialogueNodeEvent:96:1` (exclusive)
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
| Target | `DialogueNodeEvent:108:63` |
| Target | `DialogueNodeEvent:108:64` |
| Target | `DialogueNodeEvent:108:65` |
| Target | `DialogueNodeEvent:108:66` |
| Target | `DialogueNodeEvent:108:68` |
| Target | `DialogueNodeEvent:108:69` |
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
// NEGATIVE_KEYS = all 39 conversation-108 wrong-answer feedback nodes
// (extended 2026-09-17 with 63/64, 65/66, 68/69 — the "one correct evidence"
// and "wrong evidence pair" branches for the correct claim).

const playerId = "<playerId>";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
  "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
  "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
  "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
  "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:63",
  "DialogueNodeEvent:108:64", "DialogueNodeEvent:108:65", "DialogueNodeEvent:108:66",
  "DialogueNodeEvent:108:68", "DialogueNodeEvent:108:69", "DialogueNodeEvent:108:70",
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
// NEGATIVE_KEYS = all 39 conversation-108 wrong-answer feedback nodes
// (extended 2026-09-17 with 63/64, 65/66, 68/69 — the "one correct evidence"
// and "wrong evidence pair" branches for the correct claim).

const playerId = "<playerId>";

const WINDOW_START_KEY = "DialogueNodeEvent:96:1";
const WINDOW_END_KEY = "questFinishEvent:44";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
  "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
  "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
  "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
  "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:63",
  "DialogueNodeEvent:108:64", "DialogueNodeEvent:108:65", "DialogueNodeEvent:108:66",
  "DialogueNodeEvent:108:68", "DialogueNodeEvent:108:69", "DialogueNodeEvent:108:70",
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

All keys are `DialogueNodeEvent:108:<n>`. The conversation branches on the argument
state (claim, evidence combination, reasoning) through player gate nodes, and each
flagged submission fires exactly one Dr. Toppo feedback node. Every feedback exists
as a generic/specific pair (the game's `argSpecificFeedback` flag picks the wording),
and both members of each pair are counted. The color rule counts all 39 nodes below
(reviewed against the 2026-06-10 Unity dialogue export on 2026-09-17; the six nodes
marked ★ were added that day).

| Category | Branch (player gate) | Nodes | Feedback gist |
|----------|----------------------|-------|---------------|
| Claim — restating Aryn's claim | claim I, several pieces of evidence (gate 4) | 37, 70 | "You are restating Aryn's claim" |
| Claim — restating Aryn's claim | claim I, several pieces of evidence or several reasoning statements (gates 4, 71) | 72, 73, 74, 75 | Same, multiple-reasoning variants |
| Claim — restating Aryn's claim | claim I, evidence A alone (gate 31) | 32, 41 (reasoning 1); 33, 76 (reasoning 2, 3 or 4) | "Your claim and evidence are (not) aligned with your reasoning... you are restating Aryn's claim" |
| Claim — restating Aryn's claim | claim I, evidence B, C or D alone (gate 77) | 78, 79 | "Your claim and evidence are not aligned. You are restating Aryn's claim" |
| Reasoning — too many / redundant | claim II, one piece of evidence, several reasoning statements (gate 38) | 39, 53 | "Too many reasoning statements" |
| Reasoning — too many / redundant | claim II, evidence C and D (gate 50) | 54, 55 (reasoning 3+4); 90, 91 (three or more) | "Redundant" / "too many reasoning statements" |
| Reasoning — misconceptions | claim II, evidence C and D (gate 50) | 84, 85 (reasoning 1); 86 (reasoning 2) | "Are you sure the water is being filtered / transformed into salt?" |
| Reasoning — misconceptions | claim II, C or D alone (gate 56) | 59 (reasoning 1); 61 (reasoning 2) | Same misconception feedback |
| Reasoning — mismatch | claim II, evidence C and D (gate 50) | 87 (reasoning 2) | "Your reasoning does not match the rest of your argument" |
| Reasoning — mismatch | claim II, C or D alone (gate 56) | 60 (reasoning 1); 62 (reasoning 2) | Same |
| Reasoning — doesn't connect all evidence | claim II, evidence C and D (gate 50) | 88, 89 (reasoning 4) | "Your reasoning should connect all of your pieces of evidence with your claim" |
| Reasoning — doesn't connect all evidence | claim II, C or D alone (gate 56) | 65 ★, 66 ★ (reasoning 4) | Identical text to 88/89 |
| Evidence | claim II, evidence B alone (gate 8) | 25, 80 | "The amount of salt in the collector does not explain what happens to the water" |
| Evidence | claim II, evidence A alone (gate 81) | 82, 83 | "Scientifically your evidence does not support your claim" / "claim sounds good — try different evidence" |
| Evidence | claim II, two or more pieces of evidence other than C+D (gate 67) | 68 ★, 69 ★ | "Your argument contains evidence that does not support your claim" |
| Evidence — incomplete set | claim II, C or D alone, reasoning 3 (gate 56) | 63 ★, 64 ★ | "Your reasoning and claim make sense, but your argument could use another piece of evidence" |
| Completeness | any component missing | 47 | "Your argument is incomplete. Make sure you have included all three parts." |

Nodes that are **not** counted:

| Node | Meaning |
|------|---------|
| `108:48`, `108:49` | "Click the Backing Information orbs" nudges — fire after a failed attempt when the panel has not been opened; ungraded by design |
| `108:51`, `108:52` | "Great Job Cadet!!! You have made the best argument possible." — success (claim II, evidence C and D, reasoning 3); NOT required by the color rule, and the quest can complete without it firing |
| `108:0, 4, 8, 31, 38, 50, 56, 67, 71, 77, 81, 92` | Structural nodes (start, argument-state gates, end) |

Script bucket lists derived from these rows: claim = {32, 33, 37, 41, 70, 72, 73,
74, 75, 76, 78, 79}; reasoning = {39, 53, 54, 55, 59, 60, 61, 62, 65, 66, 84, 85,
86, 87, 88, 89, 90, 91}; evidence/completeness = {25, 47, 63, 64, 68, 69, 80, 82, 83}.

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
// split it by the problem the feedback named. The key lists cover all 39
// conversation-108 wrong-answer feedback nodes (reviewed against the Unity
// dialogue export 2026-09-17; 63/64, 65/66, 68/69 added then).
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
  "DialogueNodeEvent:108:88", "DialogueNodeEvent:108:89",  // reasoning doesn't connect all evidence (C and D)
  "DialogueNodeEvent:108:65", "DialogueNodeEvent:108:66"   // reasoning doesn't connect all evidence (C or D alone)
];

const EVIDENCE_NEG_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:80",  // salt amount doesn't explain the water
  "DialogueNodeEvent:108:82", "DialogueNodeEvent:108:83",  // evidence doesn't support the claim (A alone)
  "DialogueNodeEvent:108:68", "DialogueNodeEvent:108:69",  // evidence doesn't support the claim (pair other than C+D)
  "DialogueNodeEvent:108:63", "DialogueNodeEvent:108:64",  // one piece of evidence missing (C or D alone, reasoning 3)
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