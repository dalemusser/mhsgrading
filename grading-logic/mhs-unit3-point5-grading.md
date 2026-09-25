# Unit 3 Point 5 Grading

**Activity:** Plant the Superfruit Seeds

**Trigger(Start) Event:** `DialogueNodeEvent:73:200`
**Trigger(End) Event:** `DialogueNodeEvent:10:194`

---

## Grading Rule

Score-based rule using weighted positive and negative counts.

| Outcome | Condition |
|---------|-----------|
| **Green** | sum_score >= 2.5 |
| **Yellow** | sum_score < 2.5, or no trigger exists |

### Score Formula

```
pos_score = pos_count * 1.0
neg_score = neg_count * 0.5
sum_score = pos_score - neg_score
```

- `pos_count` = count of `DialogueNodeEvent:73:163`
- `neg_count` = count of events in NEG_KEYS
- Four seeds are planted, so `pos_count + neg_count = 4` and green (>= 2.5) means at most one wrong planting, matching the rubric's on-track band of 3–4 points. Threshold confirmed as 2.5 in the grading-team replies of 2026-09-21 (decision A5); the rule table and the Analytics Script were aligned to it on 2026-09-24.

### Attempt Window (Production)

- **Start:** Latest `DialogueNodeEvent:73:200` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `DialogueNodeEvent:10:194` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the previous-and-latest end window (previous `DialogueNodeEvent:10:194` exclusive .. latest `DialogueNodeEvent:10:194` inclusive), per the start-and-end window decision (A1). Keys re-verified the same day against the 2026-09-21 dialogue database (conversation 73 unchanged; `73:164` fires on the first wrong planting, `73:168` on the second and third, `73:171` when a third or later wrong planting is the last seed — the export gates on `seedsIncorrectlyPlanted` / `seedsPlanted`). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `DialogueNodeEvent:73:200` |
| Trigger (End) | `DialogueNodeEvent:10:194` |
| Positive | `DialogueNodeEvent:73:163` |
| Negative | `DialogueNodeEvent:73:164` |
| Negative | `DialogueNodeEvent:73:168` |
| Negative | `DialogueNodeEvent:73:171` |

---

## Analytics Script

```js
// Unit 3, Point 5 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:10:194"

const playerId = "<playerId>";

const POS_KEY = "DialogueNodeEvent:73:163";
const NEG_KEYS = ["DialogueNodeEvent:73:164", "DialogueNodeEvent:73:168", "DialogueNodeEvent:73:171"];

const posCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: POS_KEY
});

const negCount = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: { $in: NEG_KEYS }
});

const posScore = posCount * 1.0;
const negScore = negCount * 0.5;
const sumScore = posScore - negScore;

const color = sumScore < 2.5 ? "yellow" : "green";  // 2.5 per decision A5 (was 3)
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 5 — Attempt-based standalone production script (latest attempt)
// Window start: latest DialogueNodeEvent:73:200 before the end event (exclusive)
// Window end:   latest DialogueNodeEvent:10:194 (inclusive)

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:73:200";
const END_KEY = "DialogueNodeEvent:10:194";
const POS_KEY = "DialogueNodeEvent:73:163";
const NEG_KEYS = ["DialogueNodeEvent:73:164", "DialogueNodeEvent:73:168", "DialogueNodeEvent:73:171"];

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

  // 3) Counts inside the window
  const posCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: POS_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const sumScore = (posCount * 1.0) - (negCount * 0.5);
  sumScore < 2.5 ? "yellow" : "green";
}
```

---

## Reason Codes

### EXCESS_WRONG_PLANTINGS

**Instructor Message:** In Plant the Superfruit Seeds, while helping Tera plant four superfruit seeds in garden plots along the river, the student planted {wrong_planting_number} seeds into wrong spots - locations that do not receive the super-nutrient. This point earns green only when at most 1 seed is planted in a wrong spot. Repeated wrong plantings may indicate difficulty predicting how a dissolved material spreads through a watershed: the nutrient travels downstream with the water flow, so only plots downstream of the temple source can receive it.

#### Corresponding Script

```js
// U3P5: EXCESS_WRONG_PLANTINGS — determine trigger and wrong_planting_number
// Window mirrors the production color script: latest DialogueNodeEvent:10:194 (end),
// latest DialogueNodeEvent:73:200 before it (start, exclusive; zero ObjectId when none).
// Triggers when the color formula goes yellow:
// sum_score = posCount*1.0 - negCount*0.5 < 2.5 (i.e., 2+ wrong plantings;
// threshold 2.5 confirmed as decision A5, 2026-09-21).
// wrong_planting_number counts wrong-spot feedback directly (164 first wrong,
// 168 second and third wrong, 171 when a third or later wrong planting is the
// last seed — gates verified in the 2026-09-21 dialogue export).
// Invariant: posCount + negCount = 4 seeds when the segment completed.

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:73:200";
const END_KEY = "DialogueNodeEvent:10:194";
const POS_KEY = "DialogueNodeEvent:73:163";

const NEG_KEYS = [
  "DialogueNodeEvent:73:164",  // 1st wrong spot
  "DialogueNodeEvent:73:168",  // intermediate wrong spot (repeats)
  "DialogueNodeEvent:73:171"   // 3rd+ wrong spot on the last seed, activity terminates
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  ({ triggered: false, wrong_planting_number: 0 });
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

  // 3) Counts inside the window
  const posCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: POS_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const sumScore = (posCount * 1.0) - (negCount * 0.5);

  ({ triggered: sumScore < 2.5, wrong_planting_number: negCount });
}
```

### Teacher Guidance
Review watershed maps with students, and ask them to predict flow of water. Remind students that dissolved material in water moves with the flow of water.
