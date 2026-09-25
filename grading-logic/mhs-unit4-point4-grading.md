# Unit 4 Point 4 Grading

**Activity:** Alien Well Floor 5 + You Know the Drill

**Trigger(Start) Event:** `questActiveEvent:50`
**Trigger(End) Event:** `questActiveEvent:36`

---

## Grading Rule

This progress point is score based. There are two tasks under this progress point. The first task is to check how many times the player interact with the two-layer machine and another one-layer machine on the fifth floor.
if they changed the two-layer machine exactly once on the top canister and exactly once on the bottom canister (one change per layer; the game requires both canisters to be set, decision A6) then the score gains one, otherwise zero;
if they interacted with the one-layer machine only once to figure out the correct answer, then the score further gains one; otherwise gain zero;
The next task is to select the correct drilling depth. Only the fourth floor (`DialogueNodeEvent:107:5`) yields clean water; every other depth, including the middle choice (`107:4`, contaminated water), counts as a wrong choice (decision B3, 2026-09-21: follow the game, not the rubric's "layer 3 or 4"). If the player selects the correct depth at the first attempt then the score gains two; if within two attempts then the score gains one; otherwise no further score gain.
Finally, if the aggregated score is larger than 2 then the color is green; otherwise the color is yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | score > 2 |
| **Yellow** | score <= 2 |

### Attempt Window (Production)

- **Start:** Latest `questActiveEvent:50` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `questActiveEvent:36` (inclusive; this quest event logs twice back-to-back in every playthrough — the latest-anchor windowing absorbs the duplicate)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24: (1) previously the script took the latest start and the latest end and returned yellow unless the end came after the start; per the start-and-end window decision (A1) it now anchors on the end first. (2) `DialogueNodeEvent:107:4` (middle depth, contaminated water) moved from SUCCESS_KEYS to NEG_KEYS in the Analytics, Production and reason-code scripts (decision B3); `107:5` is now the only success key. Conversation 107 re-verified the same day against the 2026-09-21 dialogue database (11 nodes, unchanged; only `107:5` → `107:9` "clean water" ends the task, the other outcomes loop back to the prompt). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `questActiveEvent:50` |
| Trigger (End) | `questActiveEvent:36` |
| Target | `soilMachine` records with `data.floor` = `"5"` (machine `"1"` TopRow / BottomRow, machine `"2"`; eventType + data match, not an eventKey) |
| Success (drill) | `DialogueNodeEvent:107:5` |
| Negative (drill) | `DialogueNodeEvent:107:2` |
| Negative (drill) | `DialogueNodeEvent:107:3` |
| Negative (drill) | `DialogueNodeEvent:107:4` |
| Negative (drill) | `DialogueNodeEvent:107:6` |


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

const SUCCESS_KEYS = ["DialogueNodeEvent:107:5"];  // 107:4 moved to NEG_KEYS 2026-09-24 (decision B3)
const NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:4", "DialogueNodeEvent:107:6"];

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
// Window start: latest questActiveEvent:50 before the end event (exclusive)
// Window end:   latest questActiveEvent:36 (inclusive)

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:50";
const END_KEY = "questActiveEvent:36";

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
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
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

  const SUCCESS_KEYS = ["DialogueNodeEvent:107:5"];  // 107:4 moved to NEG_KEYS 2026-09-24 (decision B3)
  const NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:4", "DialogueNodeEvent:107:6"];

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
count(107:7) + count(107:8) + count(107:10). **Decision B3 (2026-09-21, applied
2026-09-24):** `107:4` is a negative key. Its outcome is contaminated water and the
task continues until `107:5` is chosen, so the game treats it as a wrong depth even
though the rubric's wording says "layer 3 or 4"; a middle-then-fourth player now
earns second-try credit (+1) instead of first-try credit (+2). Conversation 107
re-verified against the 2026-09-21 dialogue database (11 nodes, unchanged).

### SCORE_BELOW_THRESHOLD

**Instructor Message:** In the Alien Well's fifth floor and the drill task, the student changed soil canisters {machine_attempt_number} times across the floor's two machines (three changes - one per layer - is optimal) and chose a wrong drilling depth {wrong_choice_number} times before reaching clean water. This point earns green only when the drill hits the right depth on the first choice with at least one machine set optimally, or on the second choice with both machines set optimally. Wrong depths may indicate difficulty locating the water table: drilling too shallow finds no water, too deep hits bedrock, and water that has filtered through too few soil layers stays contaminated - the clean water lies just above the bedrock.

#### Corresponding Script

```js
// U4P4: SCORE_BELOW_THRESHOLD — determine trigger and quantities
// Window mirrors the production color script: latest questActiveEvent:36 (end),
// latest questActiveEvent:50 before it (start, exclusive; zero ObjectId when none).
// triggered mirrors the color formula verbatim: +1 if machine 1 has exactly one
// TopRow and one BottomRow change, +1 if machine 2 has exactly one change,
// +2 / +1 for the correct depth (107:5, the only clean-water outcome) with
// 0 / 1 wrong depths before it; yellow when score <= 2. Since 2026-09-24
// (decision B3) 107:4 "middle" is a wrong depth like 2, 3 and 6, so
// wrong_choice_number equals the color rule's negative count.
// machine_attempt_number = all fifth-floor canister changes.

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:50";
const END_KEY = "questActiveEvent:36";

const SUCCESS_KEYS = ["DialogueNodeEvent:107:5"];   // fourth floor — clean water
const NEG_KEYS = [
  "DialogueNodeEvent:107:2",  // first floor — no water
  "DialogueNodeEvent:107:3",  // second floor — no water
  "DialogueNodeEvent:107:4",  // middle — contaminated water (negative since 2026-09-24)
  "DialogueNodeEvent:107:6"   // all the way down — bedrock
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  ({ triggered: false, machine_attempt_number: 0, wrong_choice_number: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

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
    eventKey: { $in: SUCCESS_KEYS }, ...windowFilter
  });
  const negTotal = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEG_KEYS }, ...windowFilter
  });

  // Mirror the color formula exactly
  let score = 0;
  if (m1Top === 1 && m1Bottom === 1) score += 1;
  if (m2 === 1) score += 1;
  if (successTotal > 0 && negTotal === 0) score += 2;
  else if (successTotal > 0 && negTotal === 1) score += 1;

  ({
    triggered: score <= 2,
    machine_attempt_number: m1Top + m1Bottom + m2,
    wrong_choice_number: negTotal
  });
}
```

### Teacher Guidance
1. Water moves through soils at different rates depending on particle size: fastest through gravel, more slowly through sand, slowest through clay - and not at all through bedrock.
2. The water table forms where water collects above an impermeable layer: drilling too shallow finds no water, too deep hits bedrock, and water that has filtered through too few soil layers remains contaminated.
3. Ask the student to predict, for each machine layer and for the drill depth, what the water should do there and why - before trying an answer.