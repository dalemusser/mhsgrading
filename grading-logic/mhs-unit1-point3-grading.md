# Unit 1 Point 3 Grading

**Activity:** Defend the Expedition

**Trigger(Start) Event:** `DialogueNodeEvent:30:98`
**Trigger(End) Event:** `questActiveEvent:34`

---

## Grading Rule

Check whether the student needed multiple attempts to build the correct argument.

| Outcome | Condition |
|---------|-----------|
| **Green** | No yellow nodes found within the attempt window |
| **Yellow** | Any yellow node found within the attempt window, or no trigger exists |

### Attempt Window (Production)

- **Start:** Latest `DialogueNodeEvent:30:98` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `questActiveEvent:34` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-23 from the previous-and-latest end window (previous `questActiveEvent:34` exclusive .. latest `questActiveEvent:34` inclusive), per the start-and-end window decision (A1). Both Python transcriptions follow; the Go rule must be updated in step.

> Without windowing, one early mistake permanently results in yellow. With windowing, a student can replay and earn green on a later attempt.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `DialogueNodeEvent:30:98` |
| Trigger (End) | `questActiveEvent:34` |
| Yellow | `DialogueNodeEvent:70:25` |

---

## Analytics Script

```js
// Unit 1, Point 3 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:34"
// Success eventKey: "DialogueNodeEvent:70:7"

const playerId = "<playerId>";

const YELLOW_KEYS = [
  "DialogueNodeEvent:70:25"
];

const hasYellow =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: YELLOW_KEYS }
  }) !== null;

const color = hasYellow ? "yellow" : "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 1, Point 3 — Attempt-based standalone production script
// Window start: latest DialogueNodeEvent:30:98 before the end event (exclusive)
// Window end:   latest questActiveEvent:34 (inclusive)

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:30:98";
const END_KEY = "questActiveEvent:34";

const YELLOW_KEYS = [
  "DialogueNodeEvent:70:25"
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

  // 3) Any yellow node inside the window?
  const hasYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: YELLOW_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  hasYellow ? "yellow" : "green";
}
```

---

## Reason Codes

### WRONG_ARG_SELECTED

**Instructor Message:** In Defend the Expedition, the student's first argument submission was incorrect; they built the correct argument on attempt {attempt_number}. This point earns green only when the first submission is correct. The early miss may indicate difficulty identifying which claim is supported by the given evidence and reasoning.

#### Corresponding Script

```js
// U1P3: WRONG_ARG_SELECTED — determine trigger and attempt_number
// Window mirrors the production color script: latest questActiveEvent:34 (end),
// latest DialogueNodeEvent:30:98 before it (start, exclusive; zero ObjectId when none).
// `triggered` recomputes the color rule verbatim (any yellow node inside the
// window), so the pop-up can never disagree with the cell.
// attempt_number = argument submissions inside the window: every wrong submission
// fires 70:25 and the correct one fires 70:7, so wrong + correct = the attempt on
// which the correct argument was built.

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:30:98";
const END_KEY = "questActiveEvent:34";

const YELLOW_KEYS = [
  "DialogueNodeEvent:70:25"
];

const ATTEMPT_KEYS = [
  "DialogueNodeEvent:70:25",
  "DialogueNodeEvent:70:7"
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  ({ triggered: false, attempt_number: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  // 3) Color rule, mirrored: any yellow node inside the window
  const hasYellow = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: { $in: YELLOW_KEYS }, ...windowFilter
  }, { projection: { _id: 1 } }) !== null;

  // 4) Count argument submissions inside the window
  const attempts = db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: ATTEMPT_KEYS }, ...windowFilter
  });

  ({ triggered: hasYellow, attempt_number: attempts });
}
```

### Teacher Guidance
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.
3. Reasoning: links your claim to the evidence presented by explaining how or why the evidence supports the claim.
