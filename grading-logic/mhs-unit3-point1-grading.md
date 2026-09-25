# Unit 3 Point 1 Grading

**Activity:** Good Morning Cadet + Establishing a Foothold

**Trigger(Start) Event:** `DialogueNodeEvent:10:1`
**Trigger(End) Event:** `DialogueNodeEvent:11:22`

---

## Grading Rule

Count-based rule. The student must have more than one occurrence of the target event to demonstrate understanding of water flow direction.

| Outcome | Condition |
|---------|-----------|
| **Green** | Count of target event > 1 within the attempt window |
| **Yellow** | Count of target event <= 1, or no trigger exists |

### Attempt Window (Production)

- **Start:** Latest `DialogueNodeEvent:10:1` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `DialogueNodeEvent:11:22` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the previous-and-latest end window (previous `DialogueNodeEvent:11:22` exclusive .. latest `DialogueNodeEvent:11:22` inclusive), per the start-and-end window decision (A1). Keys re-verified the same day against the 2026-09-21 dialogue database (`10:1`, `10:30`, `10:31`, `10:32`, `11:22` unchanged and unique; conversation 11 lost nodes 18–20, none graded here). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `DialogueNodeEvent:10:1` |
| Trigger (End) | `DialogueNodeEvent:11:22` |
| Target | `DialogueNodeEvent:10:30` |

---

## Analytics Script

```js
// Unit 3, Point 1 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:11:22"

const playerId = "<playerId>";

const cnt = db.logdata.countDocuments({
  game: "mhs",
  playerId: playerId,
  eventKey: "DialogueNodeEvent:10:30"
});

const color = cnt > 1 ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 1 — Attempt-based standalone production script (latest attempt)
// Window start: latest DialogueNodeEvent:10:1 before the end event (exclusive)
// Window end:   latest DialogueNodeEvent:11:22 (inclusive)

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:10:1";
const END_KEY = "DialogueNodeEvent:11:22";
const TARGET_KEY = "DialogueNodeEvent:10:30";

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

  // 3) Count target occurrences within attempt window
  const cnt = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: TARGET_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  cnt > 1 ? "green" : "yellow";
}
```

---

## Reason Codes

### EXCESS_WRONG_RIVERS

**Instructor Message:** In Establishing a Foothold, while sending Tera's three supply crates back to her camp by floating them down a river, the student dropped {wrong_river_number} crates into the wrong river. This point earns green only when at most 1 crate goes into the wrong river. Wrong-river choices may indicate difficulty using the watershed map to determine flow direction - water flows from higher to lower elevation toward the ocean, so the correct river is the one that flows past Tera's camp.

#### Corresponding Script

```js
// U3P1: EXCESS_WRONG_RIVERS - determine trigger and wrong_river_number
// Window mirrors the production color script: latest DialogueNodeEvent:11:22 (end),
// latest DialogueNodeEvent:10:1 before it (start, exclusive; zero ObjectId when none).
// Triggers when the color rule goes yellow: fewer than 2 correct-river
// confirmations (10:30) in the attempt window. wrong_river_number counts the
// wrong-river feedback nodes directly (10:31 mid-task, 10:32 last crate).
// Audit invariant: correct + wrong = 3 (three crates, each thrown once).
// The wrong-river keys ALSO fire during the ungraded Morris-Galactic
// bonus-crate segment after this window - never count them unwindowed.

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:10:1";
const END_KEY = "DialogueNodeEvent:11:22";
const CORRECT_KEY = "DialogueNodeEvent:10:30";  // "you picked the right river"

const WRONG_RIVER_KEYS = [
  "DialogueNodeEvent:10:31",  // wrong river, crate lost (crates 1-2)
  "DialogueNodeEvent:10:32"   // wrong river, last crate
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  ({ triggered: false, wrong_river_number: 0 });
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

  // 3) Correct-river confirmations (the color rule's target)
  const correctCount = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: CORRECT_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // 4) Wrong-river selections, counted directly
  const wrongCount = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: WRONG_RIVER_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // 5) Mirror the color rule exactly (green requires correctCount > 1)
  ({ triggered: correctCount <= 1, wrong_river_number: wrongCount });
}
```

### Teacher Guidance
Review watershed maps with students, and ask them to predict flow of water. Remind students that rivers empty into the ocean.
