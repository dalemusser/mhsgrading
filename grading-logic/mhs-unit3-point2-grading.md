# Unit 3 Point 2 Grading

**Activity:** Pollution Solution

**Trigger(Start) Event:** `questActiveEvent:17`
**Trigger(End) Event:** `DialogueNodeEvent:11:34`

---

## Grading Rule

Score-based rule with capped penalties. The student starts with 5 points and loses points based on incorrect attempts, capped per category.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 3 |
| **Yellow** | score < 3, or no trigger exists |

### Score Formula

```
score = 5 - capped_penalty(c27) - capped_penalty(c29 + c230)
```

Where `capped_penalty(cnt)`:
| Count | Penalty |
|-------|---------|
| <= 1  | 0       |
| 2-3   | 1       |
| >= 4  | 2       |

### Count Targets

- `c27` = count of `DialogueNodeEvent:11:27`
- `c29` = count of `DialogueNodeEvent:11:29`
- `c230` = count of `DialogueNodeEvent:11:230`
- `cSum` = c29 + c230

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:11:34` (exclusive)
- **End:** Latest `DialogueNodeEvent:11:34` (inclusive)
- The Production Script below bounds the window this way. The Trigger(Start) event in the header marks when the activity begins and drives the dashboard's in-progress state and the duration metrics.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:11:34` |
| Penalty group 1 | `DialogueNodeEvent:11:27` |
| Penalty group 2 | `DialogueNodeEvent:11:29` |
| Penalty group 2 | `DialogueNodeEvent:11:230` |

---

## Analytics Script

```js
// Unit 3, Point 2 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:11:34"

const playerId = "<playerId>";

function cappedPenalty(cnt) {
  if (cnt <= 1) return 0;
  if (cnt <= 3) return 1;
  return 2;
}

const c27 = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:11:27"
});

const c29 = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:11:29"
});

const c230 = db.logdata.countDocuments({
  game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:11:230"
});

const cSum = c29 + c230;

let score = 5;
score -= cappedPenalty(c27);
score -= cappedPenalty(cSum);

const color = score < 3 ? "yellow" : "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 2 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:11:34"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:11:34";

function cappedPenalty(cnt) {
  if (cnt <= 1) return 0;
  if (cnt <= 3) return 1;
  return 2;
}

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

  const c27 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: "DialogueNodeEvent:11:27",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const c29 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: "DialogueNodeEvent:11:29",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const c230 = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: "DialogueNodeEvent:11:230",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const cSum = c29 + c230;

  let score = 5;
  score -= cappedPenalty(c27);
  score -= cappedPenalty(cSum);

  score < 3 ? "yellow" : "green";
}
```

---

## Reason Codes

### EXCESS_SENSOR_REMINDERS

**Instructor Message:** In Pollution Solution, while using drone-dropped sensors to trace the source of the river pollution, the student triggered {downstream_reminder_number} reminders that pollution flows only downstream (testing in the wrong direction) and {redundant_reminder_number} reminders about unnecessary tests (checking upstream of a clean sensor, or pushing past the top of a branch). This point stays green unless reminders accumulate in both categories: one occurring 4 or more times and the other at least twice. Repeated reminders of both kinds may indicate difficulty using sensor readings to reason about how dissolved material spreads through a watershed: pollution can appear only downstream of its source, so a polluted reading means the source is upstream, and a clean reading clears everything upstream of it.

#### Corresponding Script

```js
// U3P2: EXCESS_SENSOR_REMINDERS — determine trigger and reminder counts
// Triggers when the color formula goes yellow: score = 5 - pen(c27) - pen(c29+c230) < 3,
// where pen caps each category (<=1: 0, 2-3: 1, >=4: 2). Yellow therefore requires
// reminders in BOTH categories — never gate this on a lump-sum reminder count.
// downstream_reminder_number = wrong-direction reminders (11:27);
// redundant_reminder_number = unnecessary-test reminders (11:29 clean-upstream,
// 11:230 top-of-branch). Related nodes 11:28 and 11:30 are ungraded by design.

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:11:34";

const DOWNSTREAM_KEY = "DialogueNodeEvent:11:27";   // test further upstream
const REDUNDANT_KEYS = [
  "DialogueNodeEvent:11:29",   // no need to check upstream of a clean sensor
  "DialogueNodeEvent:11:230"   // top of branch reached, proceed downstream
];

function cappedPenalty(cnt) {
  if (cnt <= 1) return 0;
  if (cnt <= 3) return 1;
  return 2;
}

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, downstream_reminder_number: 0, redundant_reminder_number: 0 });
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

  // 3) Category counts inside the window
  const downstreamCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: DOWNSTREAM_KEY,
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const redundantCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: REDUNDANT_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // 4) Mirror the color formula exactly
  const score = 5 - cappedPenalty(downstreamCount) - cappedPenalty(redundantCount);

  ({
    triggered: score < 3,
    downstream_reminder_number: downstreamCount,
    redundant_reminder_number: redundantCount
  });
}
```

### Teacher Guidance
Review watershed maps with students, and ask them to predict flow of water. Remind students that rivers empty into the ocean.