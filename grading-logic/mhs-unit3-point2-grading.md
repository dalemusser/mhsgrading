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

- **Start:** Latest `questActiveEvent:17` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `DialogueNodeEvent:11:34` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the previous-and-latest end window (previous `DialogueNodeEvent:11:34` exclusive .. latest `DialogueNodeEvent:11:34` inclusive), per the start-and-end window decision (A1). Keys re-verified the same day against the 2026-09-21 dialogue database (`11:27`, `11:29`, `11:230`, `11:34` unchanged and unique; the ungraded `11:28` / `11:30` unchanged; conversation 11 lost only the Aryn crate-chat nodes 18–20). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `questActiveEvent:17` |
| Trigger (End) | `DialogueNodeEvent:11:34` |
| Penalty group 1 | `DialogueNodeEvent:11:27` |
| Penalty group 2 | `DialogueNodeEvent:11:29` |
| Penalty group 2 | `DialogueNodeEvent:11:230` |

**Known, deliberately ungraded reminders (decision 2026-09-24):**

- `DialogueNodeEvent:11:30` — "We are at the ocean downstream of Tera's base—logically, there will be pollution here. I recommend proceeding upstream." (the design's ocean-throw reminder). Present and unchanged in the 2026-09-21 dialogue database, but it has never fired in any playthrough log (eight runs, builds 20260501 through 20260914-), and the logs carry no sensor-drop or drone-position event, so whether the game still plays it cannot be determined. It is kept OUT of every script on purpose: the Progress-Points row grades only `11:27` / `11:29` / `11:230`, while the rubric file scores the ocean throw as its own 1-point category, and its placement (penalty group 1, group 2, or a third category) would change the capped-penalty formula the moment it fires. Decision deferred until the deliberately imperfect release-build playthrough includes one sensor thrown into the ocean at the river mouth, which will show whether `11:30` fires at all and whether `11:27` fires with it. If it is then added, the change must reach both colour scripts, the reason-code script, both Python transcriptions and the Go rule; no fixture outcome would move.
- `DialogueNodeEvent:11:28` — "We previously tested close to this area. Consider heading further upstream." Ungraded by design (a proximity hint, not a flow-logic error); fired twice in 09-03-26-3.

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
// Window start: latest questActiveEvent:17 before the end event (exclusive)
// Window end:   latest DialogueNodeEvent:11:34 (inclusive)

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:17";
const END_KEY = "DialogueNodeEvent:11:34";

function cappedPenalty(cnt) {
  if (cnt <= 1) return 0;
  if (cnt <= 3) return 1;
  return 2;
}

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

  // 3) Category counts inside the window
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
// Window mirrors the production color script: latest DialogueNodeEvent:11:34 (end),
// latest questActiveEvent:17 before it (start, exclusive; zero ObjectId when none).
// Triggers when the color formula goes yellow: score = 5 - pen(c27) - pen(c29+c230) < 3,
// where pen caps each category (<=1: 0, 2-3: 1, >=4: 2). Yellow therefore requires
// reminders in BOTH categories — never gate this on a lump-sum reminder count.
// downstream_reminder_number = wrong-direction reminders (11:27);
// redundant_reminder_number = unnecessary-test reminders (11:29 clean-upstream,
// 11:230 top-of-branch). Related nodes 11:28 and 11:30 are ungraded by design.

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:17";
const END_KEY = "DialogueNodeEvent:11:34";

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

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  ({ triggered: false, downstream_reminder_number: 0, redundant_reminder_number: 0 });
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