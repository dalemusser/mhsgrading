# Unit 5 Point 1 Grading

**Activity:** If I Had a Nickel- Floors 1 & 2

**Trigger(Start) Event:** `questActiveEvent:43`
**Trigger(End) Event:** `questFinishEvent:43`

---

## Grading Rule

This progress point is an attempt-based progress. If the player solved the puzzle (triggered `DialogueNodeEvent:100:44`) without triggering any of the following bad feedbacks (`DialogueNodeEvent:100:38`, `DialogueNodeEvent:100:39`, `DialogueNodeEvent:100:43`), the color is green; if the success dialogue never fired, or any of the bad feedbacks fired, the color is yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 1 |
| **Yellow** | score < 1 |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:43` (exclusive)
- **End:** Latest `questFinishEvent:43` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:43` |
| Target | `DialogueNodeEvent:100:44` |
| Target | `DialogueNodeEvent:100:38` |
| Target | `DialogueNodeEvent:100:39` |
| Target | `DialogueNodeEvent:100:43` |

---

## Analytics Script

```js
// Unit 5, Point 1 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:43"

const playerId = "<playerId>";

const POS_KEYS = ["DialogueNodeEvent:100:44"];
const NEG_KEYS = [
  "DialogueNodeEvent:100:38",
  "DialogueNodeEvent:100:39",
  "DialogueNodeEvent:100:43"
];

const has_trigger =
  db.logdata.findOne(
    {
      playerId: playerId,
      eventKey: { $in: POS_KEYS }
    }
  ) !== null;

let color;

if (!has_trigger) {
  color = "yellow";
} else {
  const cnt = db.logdata.countDocuments({
    playerId: playerId,
    eventKey: { $in: NEG_KEYS }
  });

  color = (cnt > 0) ? "yellow" : "green";
}

color;
```

## Production Script (Attempt-Based)

```js
// Unit 5, Point 1 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "questActiveEvent:39"

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:43";
const WINDOW_END_KEY = "questFinishEvent:43";

const POS_KEY = "DialogueNodeEvent:100:44";
const NEG_KEYS = [
  "DialogueNodeEvent:100:38",
  "DialogueNodeEvent:100:39",
  "DialogueNodeEvent:100:43"
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

  // 3) Check success inside window
  const hasTrigger =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: POS_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (!hasTrigger) {
    "yellow";
  } else {
    // 4) Count negative feedback inside window
    const cnt = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: NEG_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    });

    cnt > 0 ? "yellow" : "green";
  }
}
```

---

## Reason Codes

### Conversation-100 Feedback Nodes by Attempt

All keys are `DialogueNodeEvent:100:<n>`. Each wrong submission fires one
attempt-indexed feedback node (evaporation-rate tablet ordering, floors 1 & 2;
same structure as the U3P4/U4P2 glyph puzzles). Yellow keys are the
attempt-4-and-later nodes, so green = solved independently within 4 attempts.

| Attempt | 1–2 wrong | 3+ wrong |
|---------|-----------|----------|
| 1st | `100:33` "close to the solution" | `100:34` "ordered in a specific way" |
| 2nd | `100:35` evaporation-rate hint (single branch, any wrong) | — |
| 3rd | `100:36` "close to the correct order" | `100:37` temperature / time-of-day hint |
| 4th | `100:38` "very close" ★ | `100:39` assist offer ★ |
| 5th | `100:43` forced assist — DANI orders the tablets ★ (single branch, any wrong) | — |

★ = yellow key in the color rule.

Assist-path markers (all four verified logging in run 09-03-26-3, which walked
the accepted-offer path end to end):

| Node | Meaning |
|------|---------|
| `100:40` | "Sure, I'm stuck." — assist offer accepted |
| `100:41` | Accepted-assist execution — "Activating holid projector" |
| `100:43` | Forced-assist execution (5th attempt) |
| `100:46` | DANI-helped completion — "We have finally solved this puzzle" |

Other nodes: `100:44` ("Well done, TK") fires on BOTH the independent and the
DANI-assisted paths — it is NOT an independence signal; `100:45` is the
curricular explanation (higher temperature → higher evaporation rate);
`100:30/31/32` are idle nudges before the first placement; `100:42` is empty.

### SOLVED_WITH_ASSIST

**Instructor Message:** In If I Had a Nickel (floors 1 and 2), the student did not complete the evaporation glyph puzzle independently — after {attempt_number} incorrect arrangements, the in-game guide DANI ordered the tablets. This point earns green only when the student solves the puzzle on their own within 4 attempts. Needing this level of support may indicate the student would benefit from reviewing how temperature drives evaporation — the higher the temperature, the higher the evaporation rate.

#### Corresponding Scripts

```js
// U5P1: SOLVED_WITH_ASSIST — determine trigger and attempt_number
// Window mirrors the production color script: latest questActiveEvent:43 (start)
// to latest questFinishEvent:43 (end), end must not precede start.
// Triggers when any assist-path marker fired: 100:40 (offer accepted),
// 100:41 (accepted execution), 100:43 (forced execution), 100:46 (helped
// completion) — all four verified logging in run 09-03-26-3. Do NOT infer
// assistance from 100:44's absence — it fires on the assisted path too.
// attempt_number = incorrect arrangements before DANI ordered the tablets.

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:43";
const WINDOW_END_KEY = "questFinishEvent:43";

const ASSIST_KEYS = [
  "DialogueNodeEvent:100:40",  // "Sure, I'm stuck" — offer accepted
  "DialogueNodeEvent:100:41",  // accepted-assist execution
  "DialogueNodeEvent:100:43",  // forced assist (5th attempt)
  "DialogueNodeEvent:100:46"   // DANI-helped completion
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:100:33",  // 1st attempt, close
  "DialogueNodeEvent:100:34",  // 1st attempt, far
  "DialogueNodeEvent:100:35",  // 2nd attempt (evaporation-rate hint)
  "DialogueNodeEvent:100:36",  // 3rd attempt, close
  "DialogueNodeEvent:100:37",  // 3rd attempt, far (temperature hint)
  "DialogueNodeEvent:100:38",  // 4th attempt, close ("very close")
  "DialogueNodeEvent:100:39"   // 4th attempt, far (assist offered)
];

// 1) Window anchors
const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  // Missing/invalid window (incl. the started-but-unfinished pencil case)
  ({ triggered: false, attempt_number: 0 });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  // 2) Any assist-path marker in the window?
  const assisted =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: { $in: ASSIST_KEYS }, ...windowFilter
    }) !== null;

  // 3) Count incorrect arrangements
  const attemptNumber = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS }, ...windowFilter
  });

  ({ triggered: assisted, attempt_number: attemptNumber });
}
```

### EXCESS_ATTEMPTS

**Instructor Message:** In If I Had a Nickel (floors 1 and 2), the student solved the evaporation glyph puzzle on their own, but needed {attempt_number} attempts. This point earns green only when the puzzle is solved within 4 attempts. Repeated incorrect arrangements may indicate difficulty matching the wall images — temperatures at different times of day — to the evaporation rates they would produce.

#### Corresponding Scripts

```js
// U5P1: EXCESS_ATTEMPTS — determine trigger and attempt_number
// Same window as the color script. Triggers when the student solved the
// puzzle without DANI's assist but a color negative fired (100:38 / 100:39 /
// 100:43 — the 4th-attempt-and-later feedback), i.e. success took 5+ attempts
// or came right after a 4th-attempt miss. Mirrors the color rule's yellow set
// verbatim so the code can never disagree with the cell.
// attempt_number = incorrect arrangements + 1 (the final correct submission).

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:43";
const WINDOW_END_KEY = "questFinishEvent:43";

const ASSIST_KEYS = [
  "DialogueNodeEvent:100:40",
  "DialogueNodeEvent:100:41",
  "DialogueNodeEvent:100:43",
  "DialogueNodeEvent:100:46"
];

const COLOR_NEG_KEYS = [
  "DialogueNodeEvent:100:38",  // 4th attempt, close
  "DialogueNodeEvent:100:39",  // 4th attempt, far (assist offered)
  "DialogueNodeEvent:100:43"   // 5th attempt, forced assist
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:100:33",  // 1st attempt, close
  "DialogueNodeEvent:100:34",  // 1st attempt, far
  "DialogueNodeEvent:100:35",  // 2nd attempt (evaporation-rate hint)
  "DialogueNodeEvent:100:36",  // 3rd attempt, close
  "DialogueNodeEvent:100:37",  // 3rd attempt, far (temperature hint)
  "DialogueNodeEvent:100:38",  // 4th attempt, close ("very close")
  "DialogueNodeEvent:100:39"   // 4th attempt, far (assist offered)
];

// 1) Window anchors
const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  ({ triggered: false, attempt_number: 0 });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  // 2) DANI's assist did not run (otherwise SOLVED_WITH_ASSIST applies)
  const assisted =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: { $in: ASSIST_KEYS }, ...windowFilter
    }) !== null;

  // 3) A color negative fired — 4th-or-later submission was wrong
  const hasColorNeg =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: { $in: COLOR_NEG_KEYS }, ...windowFilter
    }) !== null;

  // 4) Count incorrect arrangements
  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS }, ...windowFilter
  });

  ({ triggered: !assisted && hasColorNeg, attempt_number: negCount + 1 });
}
```

### Teacher Guidance
Remind students that evaporation  is the phase change that occurs when energy is added to liquid to turn it into a gas Have students work through Unit 5 followup activity.
