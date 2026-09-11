# Unit 4 Point 4 Grading

**Activity:** Alien Well Floor 5 + You Know the Drill

**Trigger(Start) Event:** `questActiveEvent:50`
**Trigger(End) Event:** `questActiveEvent:36`

---

## Grading Rule

This progress point is score based. There are two tasks under this progress point. The first task is to check how many times the player interact with the two-layer machine and another one-layer machine on the fifth floor.
if they interacted with the top machine with one time and the bottom machine with zero time then the score gain once, otherwise zero;
if they interacted with the one-layer machine only once to figure out the correct answer, then the score further gains one; otherwise gain zero;
The next task is to select the correct dialogue choice. If the player select correct choice at the first attempt individually then the score gains two; if the player figures out the correct answer by themselves within two attemts individually then the score further gains one; otherwise no further score gain.
Finally, if the aggregated score is larger than 2 then the color is green; otherwise the color is yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | score > 2 |
| **Yellow** | score <= 2 |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:50` (exclusive)
- **End:** Latest `questActiveEvent:36` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:36` |
| Target | soil machine logs related to dungeon floor 5 |
| Target | `DialogueNodeEvent:107:4` |
| Target | `DialogueNodeEvent:107:5` |
| Target | `DialogueNodeEvent:107:2` |
| Target | `DialogueNodeEvent:107:3` |
| Target | `DialogueNodeEvent:107:6` |


---

## Analytics Script

```js
// Unit 4, Point 4 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:36"

const playerId = "<playerId>";

let score = 0;

const c_m1_top = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.floor": "5",
  "data.machine": "1",
  "data.row": "TopRow"
});

const c_m1_bottom = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.floor": "5",
  "data.machine": "1",
  "data.row": "BottomRow"
});

if (c_m1_top === 1 && c_m1_bottom === 1) {
  score += 1;
}

const c_m2_floor5 = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "soilMachine",
  "data.floor": "5",
  "data.machine": "2"
});

if (c_m2_floor5 === 1) {
  score += 1;
}

const SUCCESS_KEYS = ["DialogueNodeEvent:107:4", "DialogueNodeEvent:107:5"];
const NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:6"];

const success_total = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: SUCCESS_KEYS }
});

const neg_total = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: NEG_KEYS }
});

if (success_total > 0 && neg_total === 0) {
  score += 2;
} else if (success_total > 0 && neg_total === 1) {
  score += 1;
}

const color = (score > 2) ? "green" : "yellow";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 4 — Production (replay-safe, latest attempt window)
// Window start: latest "questActiveEvent:50"
// Window end:   latest "questActiveEvent:36"

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:50";
const WINDOW_END_KEY = "questActiveEvent:36";

// 1) Find latest window start
const latestStart = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_START_KEY
  },
  { sort: { _id: -1 } }
);

// 2) Find latest window end
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 } }
);

if (!latestStart || !latestEnd || latestEnd._id <= latestStart._id) {
  "yellow";
} else {
  const windowStartId = latestStart._id;
  const windowEndId = latestEnd._id;

  let score = 0;

  const c_m1_top = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.floor": "5",
    "data.machine": "1",
    "data.row": "TopRow",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const c_m1_bottom = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.floor": "5",
    "data.machine": "1",
    "data.row": "BottomRow",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  if (c_m1_top === 1 && c_m1_bottom === 1) {
    score += 1;
  }

  const c_m2_floor5 = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "soilMachine",
    "data.floor": "5",
    "data.machine": "2",
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  if (c_m2_floor5 === 1) {
    score += 1;
  }

  const SUCCESS_KEYS = ["DialogueNodeEvent:107:4", "DialogueNodeEvent:107:5"];
  const NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:6"];

  const success_total = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: SUCCESS_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  const neg_total = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEG_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  if (success_total > 0 && neg_total === 0) {
    score += 2;
  } else if (success_total > 0 && neg_total === 1) {
    score += 1;
  }

  score > 2 ? "green" : "yellow";
}
```

---

## Reason Codes

### Conversation-107 Drill-Depth Choices and Outcomes

All keys are `DialogueNodeEvent:107:<n>`. DANI's prompt (`107:1`) asks which floor
the drill should be sent to; each choice fires one choice node and one outcome
node. Only the fourth floor yields clean water.

| Choice | Depth | Outcome node | Result |
|--------|-------|--------------|--------|
| `107:2` | First floor | `107:7` | No water — too shallow |
| `107:3` | Second floor | `107:7` | No water — too shallow |
| `107:4` | Middle | `107:8` | Water found but **contaminated** — not filtered through enough soil layers |
| `107:5` | Fourth floor | `107:9` | **Clean water — correct answer** ("drilled to the perfect depth") |
| `107:6` | All the way down | `107:10` | Bedrock — no space for water, drill nearly destroyed |

Notes: `107:1` re-fires before every retry, and the outcome nodes (`107:7/8/9/10`)
log alongside the choices — wrong drills can be cross-checked as
count(107:7) + count(107:8) + count(107:10). **Flagged for review:** the color
scripts currently list `107:4` in SUCCESS_KEYS, but its outcome is contaminated
water and the task continues until `107:5` is chosen — it should move to the
negative set (this changes the dialogue scoring for middle-then-fourth players
from first-try credit +2 to second-try credit +1).

### SCORE_BELOW_THRESHOLD

**Instructor Message:** In the Alien Well's fifth floor and the drill task, the student changed soil canisters {machine_attempt_number} times across the floor's two machines (three changes - one per layer - is optimal) and chose a wrong drilling depth {wrong_choice_number} times before reaching clean water. This point earns green only when the drill hits the right depth on the first choice with at least one machine set optimally, or on the second choice with both machines set optimally. Wrong depths may indicate difficulty locating the water table: drilling too shallow finds no water, too deep hits bedrock, and water that has filtered through too few soil layers stays contaminated - the clean water lies just above the bedrock.

#### Corresponding Script

```js
// U4P4: SCORE_BELOW_THRESHOLD — determine trigger and quantities
// Window mirrors the production color script: latest questActiveEvent:50 (start)
// to latest questActiveEvent:36 (end), end after start.
// triggered mirrors the CURRENT color formula verbatim — including 107:4 in
// SUCCESS_KEYS, which is flagged for review (107:4 = "middle" yields
// contaminated water per outcome node 107:8; only 107:5 reaches clean water).
// wrong_choice_number reports the honest count of wrong drill depths
// (107:2/3/4/6); machine_attempt_number = all fifth-floor canister changes.

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:50";
const WINDOW_END_KEY = "questActiveEvent:36";

const COLOR_SUCCESS_KEYS = ["DialogueNodeEvent:107:4", "DialogueNodeEvent:107:5"];
const COLOR_NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:6"];
const WRONG_DEPTH_KEYS = [
  "DialogueNodeEvent:107:2",  // first floor — no water
  "DialogueNodeEvent:107:3",  // second floor — no water
  "DialogueNodeEvent:107:4",  // middle — contaminated water
  "DialogueNodeEvent:107:6"   // all the way down — bedrock
];

const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id <= latestStart._id) {
  ({ triggered: false, machine_attempt_number: 0, wrong_choice_number: 0 });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  const machineCount = (row, machine) => db.logdata.countDocuments({
    game: "mhs", playerId: playerId, eventType: "soilMachine",
    "data.floor": "5", "data.machine": machine,
    ...(row ? { "data.row": row } : {}),
    ...windowFilter
  });

  const m1Top = machineCount("TopRow", "1");
  const m1Bottom = machineCount("BottomRow", "1");
  const m2 = machineCount(null, "2");

  const successTotal = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: COLOR_SUCCESS_KEYS }, ...windowFilter
  });
  const colorNegTotal = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: COLOR_NEG_KEYS }, ...windowFilter
  });
  const wrongDepths = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: WRONG_DEPTH_KEYS }, ...windowFilter
  });

  // Mirror the color formula exactly
  let score = 0;
  if (m1Top === 1 && m1Bottom === 1) score += 1;
  if (m2 === 1) score += 1;
  if (successTotal > 0 && colorNegTotal === 0) score += 2;
  else if (successTotal > 0 && colorNegTotal === 1) score += 1;

  ({
    triggered: score <= 2,
    machine_attempt_number: m1Top + m1Bottom + m2,
    wrong_choice_number: wrongDepths
  });
}
```

### Teacher Guidance:
1. Water moves through soils at different rates depending on particle size: fastest through gravel, more slowly through sand, slowest through clay - and not at all through bedrock.
2. The water table forms where water collects above an impermeable layer: drilling too shallow finds no water, too deep hits bedrock, and water that has filtered through too few soil layers remains contaminated.
3. Ask the student to predict, for each machine layer and for the drill depth, what the water should do there and why - before trying an answer.