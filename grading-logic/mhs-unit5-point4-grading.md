# Unit 5 Point 4 Grading

**Activity:** Water Problems Require Water Solutions

**Trigger(Start) Event:** `questFinishEvent:44`
**Trigger(End) Event:** `questFinishEvent:45`

---

## Grading Rule

This progress point is a number-based progress. Firstly, it will check whether the plan is correctly figured out - (`DialogueNodeEvent:106:35`) - if we don't find the record within the players' event, then the color will return yellow; then it will check if the total number of following dialogues (`DialogueNodeEvent:106:4`,`DialogueNodeEvent:106:25`,`DialogueNodeEvent:106:26`,`DialogueNodeEvent:106:27`,`DialogueNodeEvent:106:28`,`DialogueNodeEvent:106:29`,`DialogueNodeEvent:106:30`,`DialogueNodeEvent:106:31`,`DialogueNodeEvent:106:32`,`DialogueNodeEvent:106:33`,`DialogueNodeEvent:106:34`) happened is euqal to 0 then the color returns green, otherwise it will return yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | have `DialogueNodeEvent:106:35` and number = 0 |
| **Yellow** | no `DialogueNodeEvent:106:35` or number > 0 or both |

### Attempt Window (Production)

- **Start:** Previous `questFinishEvent:44` (exclusive)
- **End:** Latest `questFinishEvent:45` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:44` |
| Target | `DialogueNodeEvent:106:35` |
| Target | `DialogueNodeEvent:106:4` |
| Target | `DialogueNodeEvent:106:25` |
| Target | `DialogueNodeEvent:106:26` |
| Target | `DialogueNodeEvent:106:27` |
| Target | `DialogueNodeEvent:106:28` |
| Target | `DialogueNodeEvent:106:29` |
| Target | `DialogueNodeEvent:106:30` |
| Target | `DialogueNodeEvent:106:31` |
| Target | `DialogueNodeEvent:106:32` |
| Target | `DialogueNodeEvent:106:33` |
| Target | `DialogueNodeEvent:106:34` |

---

## Analytics Script

```js
// Unit 5, Point 4 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:45"

const playerId = "<playerId>";

const SUCCESS_KEY = "DialogueNodeEvent:106:35";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:106:4",
  "DialogueNodeEvent:106:25",
  "DialogueNodeEvent:106:26",
  "DialogueNodeEvent:106:27",
  "DialogueNodeEvent:106:28",
  "DialogueNodeEvent:106:29",
  "DialogueNodeEvent:106:30",
  "DialogueNodeEvent:106:31",
  "DialogueNodeEvent:106:32",
  "DialogueNodeEvent:106:33",
  "DialogueNodeEvent:106:34"
];

const has_success =
  db.logdata.findOne(
    {
      playerId: playerId,
      eventKey: SUCCESS_KEY
    }
  ) !== null;

let color;

if (!has_success) {
  color = "yellow";
} else {
  const cnt = db.logdata.countDocuments({
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS }
  });

  color = (cnt === 0) ? "green" : "yellow";
}

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe color script
// Window start: previous questFinishEvent:44 (exclusive)
// Window end:   latest questFinishEvent:45 (inclusive)

const playerId = "<playerId>";

const START_KEY = "questFinishEvent:44";
const END_KEY = "questFinishEvent:45";
const SUCCESS_KEY = "DialogueNodeEvent:106:35";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:106:4",
  "DialogueNodeEvent:106:25",
  "DialogueNodeEvent:106:26",
  "DialogueNodeEvent:106:27",
  "DialogueNodeEvent:106:28",
  "DialogueNodeEvent:106:29",
  "DialogueNodeEvent:106:30",
  "DialogueNodeEvent:106:31",
  "DialogueNodeEvent:106:32",
  "DialogueNodeEvent:106:33",
  "DialogueNodeEvent:106:34"
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: END_KEY
  },
  { sort: { _id: -1 }}
);

if (!latestEnd) {
  "yellow";
} else {
  // 2) Previous start anchor before latest end
  const prevStart = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: START_KEY,
      _id: { $lt: latestEnd._id }
    },
    { sort: { _id: -1 }}
  );

  const windowStartId = prevStart
    ? prevStart._id
    : ObjectId("000000000000000000000000");

  const windowEndId = latestEnd._id;

  // 3) Check success node inside window
  const has_success =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: SUCCESS_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (!has_success) {
    "yellow";
  } else {
    // 4) Count negative nodes inside window
    const cnt = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: NEGATIVE_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    });

    cnt === 0 ? "green" : "yellow";
  }
}
```

---

## Reason Codes

### Conversation-106 Desalinator Outcome Nodes by Failure Mode

All keys are `DialogueNodeEvent:106:<n>`. Each solar desalinator run produces
exactly one outcome node, so on single-run paths a missing success node and a
present failure node are the same event. The color rule (zero tolerance)
requires the success node with no failure nodes in the window.

| Outcome | Nodes | Meaning |
|---------|-------|---------|
| Success — maximum water | `106:35` | "You set the solar desalinator to its best settings. As a result, you gathered the maximum amount of water." |
| No water — sunlight blocked | `106:4`, `106:25`, `106:26`, `106:27`, `106:28`, `106:29` | Settings blocked sunlight, so the salt water could not heat up and evaporate (6 variants) |
| No water — glass too hot | `106:30`, `106:31`, `106:32` | The glass surface was too hot, so condensation could not form (3 variants) |
| Small amount — roof angle | `106:33`, `106:34` | Evaporation and condensation worked, but the roof's angle let most of the condensed water escape (2 variants) |

Nodes that are **not** graded: `106:37` fires after either outcome (structural
continuation); `106:36` is the engine's "No matching response found" line;
`106:0` is empty. Window note: `questFinishEvent:45` (the end trigger) logs
twice back-to-back — the latest-anchor windowing absorbs the duplicate.

### WRONG_SETTINGS_SELECTED

**Instructor Message:** In Water Problems Require Water Solutions, the student ran the solar desalinator with settings that did not produce the maximum amount of water: {failure_phrase}. This point earns green only when the desalinator collects the maximum water with no failed runs. Each failure mode maps directly to the water cycle - the salt water needs sunlight to heat it for evaporation, the glass surface must stay cool for condensation to form, and the roof angle determines whether the condensed water is collected.

#### Corresponding Script

```js
// U5P4: WRONG_SETTINGS_SELECTED — determine trigger and failure summary
// Window mirrors the production color script: latest questFinishEvent:45 (end),
// previous questFinishEvent:44 before it (start, exclusive; note 45 logs twice
// back-to-back — latest-anchor windowing absorbs the duplicate).
// Color rule (zero tolerance): green only when 106:35 fired AND no failure
// outcome fired. Each desalinator run produces exactly one outcome node, so
// success-missing and failure-present coincide on single-run paths.
// failure_phrase names the observed failure mode(s) for the instructor.

const playerId = "<playerId>";

const START_KEY = "questFinishEvent:44";
const END_KEY = "questFinishEvent:45";
const SUCCESS_KEY = "DialogueNodeEvent:106:35";

const SUNLIGHT_KEYS = [   // no water: sunlight blocked, no evaporation
  "DialogueNodeEvent:106:4", "DialogueNodeEvent:106:25", "DialogueNodeEvent:106:26",
  "DialogueNodeEvent:106:27", "DialogueNodeEvent:106:28", "DialogueNodeEvent:106:29"
];
const GLASS_KEYS = [      // no water: glass too hot, no condensation
  "DialogueNodeEvent:106:30", "DialogueNodeEvent:106:31", "DialogueNodeEvent:106:32"
];
const ROOF_KEYS = [       // small amount: roof angle didn't collect the water
  "DialogueNodeEvent:106:33", "DialogueNodeEvent:106:34"
];

const NEGATIVE_KEYS = [...SUNLIGHT_KEYS, ...GLASS_KEYS, ...ROOF_KEYS];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  ({ triggered: false, wrong_run_number: 0, failure_phrase: "" });
} else {
  // 2) Previous start anchor before the latest end
  const prevStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = prevStart ? prevStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  const countIn = (keys) => db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventKey: { $in: keys }, ...windowFilter
  });

  const hasSuccess = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: SUCCESS_KEY, ...windowFilter
  }, { projection: { _id: 1 } }) !== null;

  const sunlightCount = countIn(SUNLIGHT_KEYS);
  const glassCount = countIn(GLASS_KEYS);
  const roofCount = countIn(ROOF_KEYS);
  const negCount = sunlightCount + glassCount + roofCount;

  const parts = [];
  if (sunlightCount > 0) parts.push(
    "the settings blocked sunlight, so the salt water could not heat up and evaporate"
    + (sunlightCount > 1 ? " (" + sunlightCount + " runs)" : ""));
  if (glassCount > 0) parts.push(
    "the glass surface was too hot for condensation to form"
    + (glassCount > 1 ? " (" + glassCount + " runs)" : ""));
  if (roofCount > 0) parts.push(
    "the roof angle let most of the condensed water escape, collecting only a small amount"
    + (roofCount > 1 ? " (" + roofCount + " runs)" : ""));

  const failurePhrase = parts.length > 0
    ? parts.join("; and ")
    : "no successful desalinator run was recorded";

  // Mirror the color rule exactly: green requires success AND zero failures
  ({
    triggered: !hasSuccess || negCount > 0,
    wrong_run_number: negCount,
    failure_phrase: failurePhrase
  });
}
```

### Teacher Guidance 
Review the water cycle concepts covered in Unit 5 with the student. Discuss how the evidence gathered throughout the unit should inform the final solution plan.