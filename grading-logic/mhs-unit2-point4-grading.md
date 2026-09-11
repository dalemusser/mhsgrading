# Unit 2 Point 4 Grading

**Activity:** Investigate the Temple

**Trigger(Start) Event:** `DialogueNodeEvent:22:18`
**Trigger(End) Event:** `DialogueNodeEvent:23:17`

---

## Grading Rule

Student must complete the watershed-flow matching independently and solve the glyph puzzle without excessive attempts.

| Outcome | Condition |
|---------|-----------|
| **Green** | Success node present AND no bad feedback nodes in attempt window |
| **Yellow** | Success node missing OR any bad feedback node present |

### Attempt Window (Production)

- **Start:** `DialogueNodeEvent:22:18` (exclusive)
- **End:** `DialogueNodeEvent:23:17` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:23:17` |
| Success | `DialogueNodeEvent:74:21` |
---

## Analytics Script

```js
// Unit 2, Point 4 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:23:17"

const playerId = "<playerId>";
| Bad Feedback | `DialogueNodeEvent:74:16` |
| Bad Feedback | `DialogueNodeEvent:74:17` |
| Bad Feedback | `DialogueNodeEvent:74:20` |
| Bad Feedback | `DialogueNodeEvent:74:22` |


const successKey = "DialogueNodeEvent:74:21";

const badKeys = [
  "DialogueNodeEvent:74:16",
  "DialogueNodeEvent:74:17",
  "DialogueNodeEvent:74:20",
  "DialogueNodeEvent:74:22"
];

const hasSuccess =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: successKey
  }) !== null;

const hasBadFeedback =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: badKeys }
  }) !== null;

const color =
  hasSuccess && !hasBadFeedback
    ? "green"
    : "yellow";

color;
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 4 — Standalone replay-aware grading (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:23:17"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:17";

const successKey = "DialogueNodeEvent:74:21";
const badKeys = [
  "DialogueNodeEvent:74:16",
  "DialogueNodeEvent:74:17",
  "DialogueNodeEvent:74:20",
  "DialogueNodeEvent:74:22"
];

// 1) Latest trigger
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  "yellow";
} else {
  // 2) Previous trigger (defines prior attempt boundary)
  const prevTrigger = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY, _id: { $lt: latestTrigger._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = prevTrigger ? prevTrigger._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  // 3) Check success/bad within this attempt window
  const hasSuccess =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: successKey,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  const hasBad =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: badKeys },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  hasSuccess && !hasBad ? "green" : "yellow";
}
```

---

## Reason Codes

> This point has multiple possible reasons for a yellow grade. Scripts are needed to determine which reason(s) apply.

### SOLVED_WITH_ASSIST

**Instructor Message:** In Investigate the Temple, the student did not complete the watershed glyph puzzle independently - after {attempt_number} incorrect arrangements, the in-game guide DANI stepped in to order the watershed pieces. This point earns green only when the student submits the correct arrangement on their own within 5 attempts. Needing this level of support may indicate the student would benefit from reviewing how a larger drainage area collects and delivers more water to the main river, producing a greater flow rate.

#### Correspoinding Script

```js
// U2P4: SOLVED_WITH_ASSIST — determine trigger and attempt_number
// Triggers when an assist marker fired in the attempt window: 74:18 (player
// accepted DANI's offer — the node that reliably logs on this build), or
// 74:20 / 74:25 (DANI orders the pieces) / 74:22 (helped completion).
// attempt_number = incorrect submissions before DANI completed the puzzle
// (each wrong submission fires exactly one feedback node, once per window)

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:17";

const ASSIST_KEYS = [
  "DialogueNodeEvent:74:18",  // "Sure. I'm stuck" — accepted assist offer
  "DialogueNodeEvent:74:20",  // DANI orders the pieces
  "DialogueNodeEvent:74:22",  // DANI-helped completion
  "DialogueNodeEvent:74:25"   // DANI orders the pieces (video-link variant)
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:74:4",   // 1st attempt, any wrong
  "DialogueNodeEvent:74:5",   // 2nd attempt, 2-3 wrong
  "DialogueNodeEvent:74:6",   // 2nd attempt, >3 wrong
  "DialogueNodeEvent:74:9",   // 3rd attempt, 2-3 wrong
  "DialogueNodeEvent:74:10",  // 3rd attempt, >3 wrong (video offered)
  "DialogueNodeEvent:74:15",  // 4th attempt, any wrong
  "DialogueNodeEvent:74:16",  // 5th attempt, 2-3 wrong
  "DialogueNodeEvent:74:17"   // 5th attempt, >3 wrong (assist offered)
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

  // 3) Reason code triggers if any assist marker fired in the window
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

**Instructor Message:** In Investigate the Temple, the student arranged the watershed terrain pieces correctly on their own, but needed {attempt_number} attempts. This point earns green only when the correct arrangement is submitted within 5 attempts. Repeated incorrect arrangements may indicate difficulty connecting drainage-area size with relative flow rate — the pattern that a larger watershed collects and delivers more water to its main river.

#### Correspoinding Script

```js
// U2P4: EXCESS_ATTEMPTS — determine trigger and attempt_number
// Triggers when the student solved the puzzle independently (74:21 in window,
// no assist marker) but the 5th submission was wrong (74:16 or 74:17 fired),
// meaning success took 6+ attempts. Mirrors the color rule's yellow keys.
// attempt_number = incorrect submissions + 1 (the final correct submission)

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:23:17";
const SUCCESS_KEY = "DialogueNodeEvent:74:21"; // solved-on-their-own completion

const FIFTH_ATTEMPT_KEYS = [
  "DialogueNodeEvent:74:16",  // 5th attempt, 2-3 wrong
  "DialogueNodeEvent:74:17"   // 5th attempt, >3 wrong (assist offered)
];

const ASSIST_KEYS = [
  "DialogueNodeEvent:74:18",
  "DialogueNodeEvent:74:20",
  "DialogueNodeEvent:74:22",
  "DialogueNodeEvent:74:25"
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:74:4",   // 1st attempt, any wrong
  "DialogueNodeEvent:74:5",   // 2nd attempt, 2-3 wrong
  "DialogueNodeEvent:74:6",   // 2nd attempt, >3 wrong
  "DialogueNodeEvent:74:9",   // 3rd attempt, 2-3 wrong
  "DialogueNodeEvent:74:10",  // 3rd attempt, >3 wrong (video offered)
  "DialogueNodeEvent:74:15",  // 4th attempt, any wrong
  "DialogueNodeEvent:74:16",  // 5th attempt, 2-3 wrong
  "DialogueNodeEvent:74:17"   // 5th attempt, >3 wrong (assist offered)
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

  // 4) DANI did not step in (otherwise SOLVED_WITH_ASSIST applies instead)
  const assisted =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: ASSIST_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 5) The 5th submission was wrong — success required 6+ attempts
  const fifthWrong =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: FIFTH_ATTEMPT_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 6) Count incorrect submissions (one feedback node each)
  const negativeCount = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const triggered = solvedSelf && !assisted && fifthWrong;

  ({ triggered: triggered, attempt_number: negativeCount + 1 });
}
```

### Teacher Guidance
Review the relationship between watershed size and flow rate.
