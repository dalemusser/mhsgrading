# Unit 2 Point 1 Grading

**Activity:** Escape the Ruin

**Trigger(Start) Event:** `DialogueNodeEvent:18:1`
**Trigger(End) Event:** `questFinishEvent:21`

---

## Grading Rule

Student must complete the map-profile matching independently and without excessive incorrect attempts.

| Outcome | Condition |
|---------|-----------|
| **Green** | Success node present AND no yellow nodes in attempt window |
| **Yellow** | Success node missing OR any yellow node present |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:21` (exclusive)
- **End:** Latest `questFinishEvent:21` (inclusive)
- The Production Script below bounds the window this way. The Trigger(Start) event in the header marks when the activity begins and drives the dashboard's in-progress state and the duration metrics.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:21` |
| Success | `DialogueNodeEvent:68:29` |
| Yellow | `DialogueNodeEvent:68:22` |
| Yellow | `DialogueNodeEvent:68:23` |
| Yellow | `DialogueNodeEvent:68:27` |
| Yellow | `DialogueNodeEvent:68:28` |
| Yellow | `DialogueNodeEvent:68:31` |

---

## Analytics Script

```js
// Unit 2, Point 1 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:21"

const playerId = "<playerId>";

const successKey = "DialogueNodeEvent:68:29";

const yellowNodes = [
  "DialogueNodeEvent:68:22",
  "DialogueNodeEvent:68:23",
  "DialogueNodeEvent:68:27",
  "DialogueNodeEvent:68:28",
  "DialogueNodeEvent:68:31"
];

const hasSuccess =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: successKey
  }) !== null;

const hasAnyYellow =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: yellowNodes }
  }) !== null;

const color =
  hasSuccess && !hasAnyYellow
    ? "green"
    : "yellow";

color;
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 1 — Attempt-based standalone production grading script
// Trigger eventKey: "questFinishEvent:21"

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:21";

const successKey = "DialogueNodeEvent:68:29";

const yellowNodes = [
  "DialogueNodeEvent:68:22",
  "DialogueNodeEvent:68:23",
  "DialogueNodeEvent:68:27",
  "DialogueNodeEvent:68:28",
  "DialogueNodeEvent:68:31"
];

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

  const hasSuccess =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: successKey,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  const hasAnyYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: yellowNodes },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  hasSuccess && !hasAnyYellow ? "green" : "yellow";
}
```

---

## Reason Codes

> This point has multiple possible reasons for a yellow grade. Scripts are needed to determine which reason(s) apply.

### SOLVED_WITH_ASSIST

**Instructor Message:** In Escape the Ruin, the student did not complete the topographic-map matching independently. After {attempt_number} incorrect arrangements, the in-game guide DANI placed the remaining pieces. This point earns green only when the student submits the correct solution on their own within 4 attempts. Needing this level of support may indicate the student would benefit from direct instruction on how contour lines represent elevation and slope before matching maps to terrain shapes.

#### Corresponding Script

```js
// U2P1: SOLVED_WITH_ASSIST - determine trigger and attempt_number
// Triggers when DANI completed the puzzle in the attempt window, on either path:
//   forced   - 68:28 (5th attempt, >3 wrong) or 68:31 (6th attempt, any wrong);
//   accepted - the player answered DANI's offer (68:23 / 68:27) with
//              "Sure. I'm stuck" (68:24 / 68:32) and DANI then placed the
//              pieces (68:26 / 68:34). Verified in log 09-14-26-3:
//              68:23 -> 68:24 -> 68:26, and the solved-on-own node 68:29
//              never fires on that path.
// attempt_number = incorrect submissions before DANI completed the puzzle
// (each wrong submission fires exactly one negative-feedback node, once per window)

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:21";

const ASSIST_KEYS = [
  "DialogueNodeEvent:68:24",  // accepted offer after 4th attempt ("Sure. I'm stuck")
  "DialogueNodeEvent:68:26",  // DANI places the pieces (accepted after 4th attempt)
  "DialogueNodeEvent:68:28",  // forced assist, 5th attempt, >3 wrong
  "DialogueNodeEvent:68:31",  // forced assist, 6th attempt, any wrong
  "DialogueNodeEvent:68:32",  // accepted offer after 5th attempt ("Sure. I'm stuck")
  "DialogueNodeEvent:68:34"   // DANI places the pieces (accepted after 5th attempt)
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:68:4",   // 1st attempt, 2-3 wrong
  "DialogueNodeEvent:68:5",   // 1st attempt, >3 wrong
  "DialogueNodeEvent:68:6",   // 2nd attempt, 2-3 wrong
  "DialogueNodeEvent:68:7",   // 2nd attempt, >3 wrong
  "DialogueNodeEvent:68:17",  // 3rd attempt, 2-3 wrong
  "DialogueNodeEvent:68:18",  // 3rd attempt, >3 wrong
  "DialogueNodeEvent:68:22",  // 4th attempt, 2-3 wrong
  "DialogueNodeEvent:68:23",  // 4th attempt, >3 wrong (assist offered)
  "DialogueNodeEvent:68:27",  // 5th attempt, 2-3 wrong (assist offered)
  "DialogueNodeEvent:68:28",  // 5th attempt, >3 wrong (DANI assists)
  "DialogueNodeEvent:68:31"   // 6th attempt, any wrong (DANI assists)
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, attempt_number: 0 });
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

  // 3) Reason code triggers if any assist node (forced or accepted) fired in the window
  const assisted =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: ASSIST_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 4) attempt_number: count negative-feedback nodes in the window
  const attemptNumber = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  ({ triggered: assisted, attempt_number: attemptNumber });
}
```

### EXCESS_ATTEMPTS

**Instructor Message:** In Escape the Ruin, the student matched all six topographic maps to their elevation profiles on their own, but needed {attempt_number} attempts. This point earns green only when the correct solution is submitted within 4 attempts. Repeated incorrect arrangements may indicate difficulty connecting the top-down contour-line view of a landscape to its side-view profile.

#### Corresponding Script

```js
// U2P1: EXCESS_ATTEMPTS — determine trigger and attempt_number
// Triggers when the student solved the puzzle independently (68:29 in window and
// no assist node, forced or accepted) but needed 5+ attempts (4+ negative-feedback nodes).
// attempt_number = incorrect submissions + 1 (the final correct submission)

const playerId = "<playerId>";

const TRIGGER_KEY = "questFinishEvent:21";
const SUCCESS_KEY = "DialogueNodeEvent:68:29"; // solved-on-their-own completion

const ASSIST_KEYS = [
  "DialogueNodeEvent:68:24",  // accepted offer after 4th attempt ("Sure. I'm stuck")
  "DialogueNodeEvent:68:26",  // DANI places the pieces (accepted after 4th attempt)
  "DialogueNodeEvent:68:28",  // forced assist, 5th attempt, >3 wrong
  "DialogueNodeEvent:68:31",  // forced assist, 6th attempt, any wrong
  "DialogueNodeEvent:68:32",  // accepted offer after 5th attempt ("Sure. I'm stuck")
  "DialogueNodeEvent:68:34"   // DANI places the pieces (accepted after 5th attempt)
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:68:4",   // 1st attempt, 2-3 wrong
  "DialogueNodeEvent:68:5",   // 1st attempt, >3 wrong
  "DialogueNodeEvent:68:6",   // 2nd attempt, 2-3 wrong
  "DialogueNodeEvent:68:7",   // 2nd attempt, >3 wrong
  "DialogueNodeEvent:68:17",  // 3rd attempt, 2-3 wrong
  "DialogueNodeEvent:68:18",  // 3rd attempt, >3 wrong
  "DialogueNodeEvent:68:22",  // 4th attempt, 2-3 wrong
  "DialogueNodeEvent:68:23",  // 4th attempt, >3 wrong (assist offered)
  "DialogueNodeEvent:68:27",  // 5th attempt, 2-3 wrong (assist offered)
  "DialogueNodeEvent:68:28",  // 5th attempt, >3 wrong (DANI assists)
  "DialogueNodeEvent:68:31"   // 6th attempt, any wrong (DANI assists)
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, attempt_number: 0 });
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

  // 3) Student reached the solved-on-their-own completion
  const solvedSelf =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: SUCCESS_KEY,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 4) DANI did not take over, forced or accepted (otherwise SOLVED_WITH_ASSIST applies instead)
  const assisted =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: ASSIST_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 5) Count incorrect submissions (one negative-feedback node each)
  const negativeCount = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // 6) 4+ wrong submissions means success came on attempt 5 or later
  const triggered = solvedSelf && !assisted && negativeCount >= 4;

  ({ triggered: triggered, attempt_number: negativeCount + 1 });
}
```

### Teacher Guidance
1. How information about elevation can be gained from contour lines.
2. How to use the compass and contour indices to aid navigation.
