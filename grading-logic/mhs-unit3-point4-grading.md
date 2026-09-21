# Unit 3 Point 4 Grading

**Activity:** Forsaken Facility

**Trigger(Start) Event:** `questActiveEvent:18`
**Trigger(End) Event:** `DialogueNodeEvent:73:200`

---

## Grading Rule

Gate + score-based rule. First, the student must have the gate event (78:24). Then, count target events and compute a score.

| Outcome | Condition |
|---------|-----------|
| **Green** | Gate present AND score > 0 (i.e. target count <= 2) |
| **Yellow** | Gate missing OR score == 0 (i.e. target count >= 3), or no trigger exists |

### Score from Target Count

| total_count | score |
|-------------|-------|
| 0           | 2     |
| 1-2         | 1     |
| >= 3        | 0     |

### Attempt Window (Production)

- **Start:** Latest `questActiveEvent:18` (exclusive; the window is valid only when the end event comes after it)
- **End:** Latest `DialogueNodeEvent:73:200` (inclusive)
- The Production Script below bounds the window this way. The Trigger(Start) event in the header marks when the activity begins and drives the dashboard's in-progress state and the duration metrics.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:73:200` |
| Gate (required) | `DialogueNodeEvent:78:24` |
| Target | `DialogueNodeEvent:78:3` |
| Target | `DialogueNodeEvent:78:4` |
| Target | `DialogueNodeEvent:78:7` |
| Target | `DialogueNodeEvent:78:9` |
| Target | `DialogueNodeEvent:78:10` |
| Target | `DialogueNodeEvent:78:12` |
| Target | `DialogueNodeEvent:78:18` |
| Target | `DialogueNodeEvent:78:23` |

---

## Analytics Script

```js
// Unit 3, Point 4 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:73:200"

const playerId = "<playerId>";

const TARGET_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

// Gate: must have 78:24
const has7824 =
  db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:78:24" },
    { projection: { _id: 1 } }
  ) !== null;

if (!has7824) {
  "yellow";
} else {
  const totalCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: TARGET_KEYS }
  });

  let score;
  if (totalCount === 0) score = 2;
  else if (totalCount <= 2) score = 1;
  else score = 0;

  score === 0 ? "yellow" : "green";
}
```

## Production Script (Attempt-Based)

```js
// Unit 3, Point 4 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:73:200"

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:18";
const END_KEY = "DialogueNodeEvent:73:200";
const GATE_KEY = "DialogueNodeEvent:78:24";

const TARGET_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

// 1) Latest start anchor
const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: START_KEY },
  { sort: { _id: -1 } }
);

// 2) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

// Must have both anchors
if (!latestStart || !latestEnd) {
  "yellow";
} else {
  // End must happen after start
  if (latestEnd._id <= latestStart._id) {
    "yellow";
  } else {
    const windowStartId = latestStart._id;
    const windowEndId = latestEnd._id;

    // Gate: must have 78:24 within (start, end]
    const has7824 =
      db.logdata.findOne(
        {
          game: "mhs",
          playerId: playerId,
          eventKey: GATE_KEY,
          _id: { $gt: windowStartId, $lte: windowEndId }
        },
        { projection: { _id: 1 } }
      ) !== null;

    if (!has7824) {
      "yellow";
    } else {
      const totalCount = db.logdata.countDocuments({
        game: "mhs",
        playerId: playerId,
        eventKey: { $in: TARGET_KEYS },
        _id: { $gt: windowStartId, $lte: windowEndId }
      });

      let score;
      if (totalCount === 0) score = 2;
      else if (totalCount <= 2) score = 1;
      else score = 0;

      score === 0 ? "yellow" : "green";
    }
  }
}
```

---

## Reason Codes

### SOLVED_WITH_ASSIST

**Instructor Message:** In Forsaken Facility, the student did not complete the ordering puzzle showing how materials dissolve into water independently. After {attempt_number} incorrect arrangements, the in-game guide DANI ordered the pieces. This point earns green only when the student submits the correct order on their own within 3 attempts. Needing this level of support may indicate the student would benefit from reviewing how the particles of a dissolved material spread through water, even once they can no longer be seen.

#### Corresponding Script

```js
// U3P4: SOLVED_WITH_ASSIST — determine trigger and attempt_number
// Window mirrors the production color script: latest questActiveEvent:18 (start)
// to latest 73:200 (end), end must follow start. Triggers when DANI's assist
// executed (78:23) or the completion gate (78:24) is absent from a valid window
// (the accepted-assist path's execution node is unconfirmed — the gate check
// covers it either way). attempt_number = attempt-indexed feedback nodes fired
// before DANI completed the puzzle.

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:18";
const END_KEY   = "DialogueNodeEvent:73:200";
const GATE_KEY  = "DialogueNodeEvent:78:24";  // completion marker (empty text)
const ASSIST_KEY = "DialogueNodeEvent:78:23"; // DANI orders the pieces

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:78:4",   // 1st attempt, 1-2 wrong
  "DialogueNodeEvent:78:3",   // 1st attempt, 3-4 wrong
  "DialogueNodeEvent:78:7",   // 2nd attempt, any wrong (microscope hint)
  "DialogueNodeEvent:78:9",   // 3rd attempt, 1-2 wrong
  "DialogueNodeEvent:78:10",  // 3rd attempt, 3-4 wrong
  "DialogueNodeEvent:78:12",  // 4th attempt, 1-2 wrong
  "DialogueNodeEvent:78:18"   // 4th attempt, 3-4 wrong (assist offered)
];

const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: START_KEY },
  { sort: { _id: -1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestStart || !latestEnd || latestEnd._id <= latestStart._id) {
  ({ triggered: false, attempt_number: 0 });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  const assisted = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: ASSIST_KEY, ...windowFilter
  }) !== null;

  const hasGate = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: GATE_KEY, ...windowFilter
  }, { projection: { _id: 1 } }) !== null;

  const attemptNumber = db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: NEGATIVE_KEYS }, ...windowFilter
  });

  ({ triggered: assisted || !hasGate, attempt_number: attemptNumber });
}
```

### EXCESS_ATTEMPTS

**Instructor Message:** In Forsaken Facility, the student ordered the puzzle pieces showing how materials dissolve into water on their own, but needed {attempt_number} attempts. This point earns green only when the correct order is submitted within 3 attempts. Repeated incorrect arrangements may indicate difficulty sequencing how particles of a dissolved material spread through water over time.

#### Corresponding Script

```js
// U3P4: EXCESS_ATTEMPTS — determine trigger and attempt_number
// Same window as the color script. Triggers when the student completed the
// puzzle (gate 78:24 present, no assist) but the color count — all 8 target
// keys, one per wrong submission — reached 3+, i.e. success took 4+ attempts.
// attempt_number = incorrect submissions + 1 (the final correct submission).

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:18";
const END_KEY   = "DialogueNodeEvent:73:200";
const GATE_KEY  = "DialogueNodeEvent:78:24";
const ASSIST_KEY = "DialogueNodeEvent:78:23";

const COLOR_TARGET_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: START_KEY },
  { sort: { _id: -1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestStart || !latestEnd || latestEnd._id <= latestStart._id) {
  ({ triggered: false, attempt_number: 0 });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  const assisted = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: ASSIST_KEY, ...windowFilter
  }) !== null;

  const hasGate = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: GATE_KEY, ...windowFilter
  }, { projection: { _id: 1 } }) !== null;

  const colorCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: COLOR_TARGET_KEYS }, ...windowFilter
  });

  ({ triggered: hasGate && !assisted && colorCount >= 3, attempt_number: colorCount + 1 });
}
```

### Teacher Guidance 
Review dissolved materials. Remind students that dissolved materials in water are present even if they cannot be seen.