# Unit 4 Point 2 Grading

**Activity:** Infiltration Glyph + Alien Well Floors 1 & 2

**Trigger(Start) Event:** The close of the soil key puzzle in Unit 4 — the `Soil Key Puzzle` event with `Soil Key Puzzle Status` = `Finished` and `Unit` matching Unit 4 (currently `"Unit 4 Dev"`; an eventType + data match, not an eventKey)
**Trigger(End) Event:** `questActiveEvent:48`

---

## Grading Rule

This progress point will check how many attempts the player used to figure out the correct matches of the puzzle by checking what feedback they received after competing the matches.
Any feedback received represented by the following dialogues (`DialogueNodeEvent:102:9`, `DialogueNodeEvent:102:10`, `DialogueNodeEvent:102:12`, `DialogueNodeEvent:102:18`, `DialogueNodeEvent:102:23`) means the player tried more than 2 attempts, which will make the block as yellow.
Another check is to see whether the player figured out the correct matches by themselves, which is marked by the event of `DialogueNodeEvent:88:11`.

| Outcome | Condition |
|---------|-----------|
| **Green** | has `DialogueNodeEvent:88:11` and no yellow feedbacks |
| **Yellow** | either no `DialogueNodeEvent:88:11` or has any yellow feedback or both |

### Attempt Window (Production)

- **Start:** Latest Unit 4 `Soil Key Puzzle` event with `Soil Key Puzzle Status` = `Finished` before the trigger (exclusive)
- **End:** Latest `questActiveEvent:48` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:48` |
| Window Start | `Soil Key Puzzle` event with `Soil Key Puzzle Status` = `Finished` and `Unit` matching Unit 4 (eventType + data match, not an eventKey) |
| Target | `DialogueNodeEvent:88:11` |
| Target | `DialogueNodeEvent:102:9` |
| Target | `DialogueNodeEvent:102:10` |
| Target | `DialogueNodeEvent:102:12` |
| Target | `DialogueNodeEvent:102:18` |
| Target | `DialogueNodeEvent:102:23` |

---

## Analytics Script

```js
// Unit 4, Point 2 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:48"

const playerId = "<playerId>";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:102:9",
  "DialogueNodeEvent:102:10",
  "DialogueNodeEvent:102:12",
  "DialogueNodeEvent:102:18",
  "DialogueNodeEvent:102:23"
];

const has_8811 =
  db.logdata.findOne(
    { playerId: playerId, eventKey: "DialogueNodeEvent:88:11" },
    { projection: { _id: 1 } }
  ) !== null;

let color;

if (!has_8811) {
  color = 2; // yellow
} else {
  const has_any_102 =
    db.logdata.findOne(
      { playerId: playerId, eventKey: { $in: NEGATIVE_KEYS } },
      { projection: { _id: 1 } }
    ) !== null;

  color = has_any_102 ? 2 : 1; // yellow if any negative else green
}

color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 2 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "questActiveEvent:48"
// Window start: close of the Unit 4 soil key puzzle
// ("Soil Key Puzzle" event, "Soil Key Puzzle Status" = "Finished", Unit matching "Unit 4")

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:48";

const SOIL_KEY_EVENT_TYPE = "Soil Key Puzzle";
const SOIL_KEY_END_STATUS = "Finished";
// data.Unit holds the scene name (currently "Unit 4 Dev"); match by prefix
// because the soil key puzzle also fires in Units 2 and 3.
const UNIT_4 = /^Unit 4/;

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:102:9",
  "DialogueNodeEvent:102:10",
  "DialogueNodeEvent:102:12",
  "DialogueNodeEvent:102:18",
  "DialogueNodeEvent:102:23"
];

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

if (!latestTrigger) {
  "yellow";
} else {
  // Window start: latest Unit 4 soil key puzzle close before the trigger
  const soilKeyClose = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: SOIL_KEY_EVENT_TYPE,
      "data.Soil Key Puzzle Status": SOIL_KEY_END_STATUS,
      "data.Unit": UNIT_4,
      _id: { $lt: latestTrigger._id }
    },
    { sort: { _id: -1 }}
  );

  const windowStartId = soilKeyClose ? soilKeyClose._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  const has_8811 =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: "DialogueNodeEvent:88:11",
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (!has_8811) {
    "yellow";
  } else {
    const has_any_102 =
      db.logdata.findOne(
        {
          game: "mhs",
          playerId: playerId,
          eventKey: { $in: NEGATIVE_KEYS },
          _id: { $gt: windowStartId, $lte: windowEndId }
        }
      ) !== null;

    has_any_102 ? "yellow" : "green";
  }
}
```

---

## Reason Codes

### Conversation-102 Feedback Nodes by Attempt

All keys are `DialogueNodeEvent:102:<n>`. Each wrong submission fires exactly one
attempt-indexed feedback node (4-piece ordering puzzle; text-identical to the
U3P4 conversation-78 set). Yellow keys are the attempt-3-and-later nodes, so
green = correct order within 3 attempts.

| Attempt | 1–2 pieces wrong | 3–4 pieces wrong |
|---------|------------------|-------------------|
| 1st | `102:4` "close to the solution" | `102:3` "ordered in a specific way" |
| 2nd | `102:7` particle-size hint (single branch, any wrong) | — |
| 3rd | `102:9` "close to the correct order" ★ | `102:10` infiltration-rate graph hint ★ |
| 4th | `102:12` "very close" ★ | `102:18` assist offer ★ |
| 5th | `102:23` forced assist — DANI orders the pieces ★ (single branch, any wrong) | — |

★ = yellow key in the color rule.

Other nodes: `88:11` is the post-puzzle explanation and fires on BOTH the
independent and DANI-assisted paths (verified in run 09-03-26-3) — it is NOT an
independence signal. `102:0` is structural; `102:14/15/16` are the player's
empty-text response choices to feedback (they DO log); `102:19/20/21/24` are
empty and unobserved. If the player accepts the assist offer at `102:18`, the
node the execution logs as is unconfirmed (only the forced 5th-attempt path,
which logs `102:23`, has been observed).

### SOLVED_WITH_ASSIST

**Instructor Message:** In the Infiltration Glyph puzzle, the student did not complete the soil-infiltration ordering independently. After {attempt_number} incorrect arrangements, the in-game guide DANI ordered the pieces. This point earns green only when the student submits the correct order on their own within 3 attempts. Needing this level of support may indicate the student would benefit from reviewing how water infiltrates different soils: the larger the soil particles, the faster water passes through.

#### Corresponding Script

```js
// U4P2: SOLVED_WITH_ASSIST — determine trigger and attempt_number
// Window mirrors the production color script: latest questActiveEvent:48 (end),
// latest Unit 4 soil-key-puzzle close before it (start, exclusive).
// Triggers when DANI completed the puzzle in the window, on either path:
//   forced   - 102:23 (5th attempt, any wrong; verified in run 09-03-26-3);
//   accepted - the player accepted the offer at 102:18 and DANI ordered the
//              pieces: 102:20 then 102:21 fire (empty-text nodes in the
//              2026-06-10 dialogue export). Verified in run 09-14-26-3: the
//              puzzle completed 10 s after the offer with no player inputs.
// Do NOT infer assistance from 88:11's absence — 88:11 fires on the assisted
// path too. attempt_number = incorrect arrangements before DANI completed
// the puzzle.

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:48";

const ASSIST_KEYS = [
  "DialogueNodeEvent:102:20",  // accepted DANI's offer (after 102:18)
  "DialogueNodeEvent:102:21",  // DANI orders the pieces (accepted path)
  "DialogueNodeEvent:102:23"   // DANI orders the pieces (forced, 5th attempt)
];

const SOIL_KEY_EVENT_TYPE = "Soil Key Puzzle";
const SOIL_KEY_END_STATUS = "Finished";
const UNIT_4 = /^Unit 4/;  // data.Unit is the scene name (currently "Unit 4 Dev")

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:102:4",   // 1st attempt, 1-2 wrong
  "DialogueNodeEvent:102:3",   // 1st attempt, 3-4 wrong
  "DialogueNodeEvent:102:7",   // 2nd attempt, any wrong (particle-size hint)
  "DialogueNodeEvent:102:9",   // 3rd attempt, 1-2 wrong
  "DialogueNodeEvent:102:10",  // 3rd attempt, 3-4 wrong (rate-graph hint)
  "DialogueNodeEvent:102:12",  // 4th attempt, 1-2 wrong
  "DialogueNodeEvent:102:18"   // 4th attempt, 3-4 wrong (assist offered)
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, attempt_number: 0 });
} else {
  // 2) Window start: latest Unit 4 soil key puzzle close before the trigger
  const soilKeyClose = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: SOIL_KEY_EVENT_TYPE,
      "data.Soil Key Puzzle Status": SOIL_KEY_END_STATUS,
      "data.Unit": UNIT_4,
      _id: { $lt: latestTrigger._id }
    },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = soilKeyClose ? soilKeyClose._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  // 3) Assist executed (forced or accepted)?
  const assisted =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: ASSIST_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 4) Count incorrect arrangements
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

**Instructor Message:** In the Infiltration Glyph puzzle, the student arranged the pieces showing how water passes through different soils, but needed {attempt_number} attempts. This point earns green only when the correct order is submitted within 3 attempts. Repeated incorrect arrangements may indicate difficulty connecting soil particle size to infiltration rate: water moves quickly through gravel, more slowly through sand, and slowest through clay.

#### Corresponding Scripts

```js
// U4P2: EXCESS_ATTEMPTS — determine trigger and attempt_number
// Same window as the color script. Triggers when the student completed the
// puzzle without DANI's assist (neither the forced 102:23 nor the accepted
// 102:20/102:21 path) but a yellow key fired — i.e., the 3rd submission (or
// later) was wrong, so success took 4+ attempts.
// attempt_number = incorrect arrangements + 1 (the final correct submission).

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:48";

const ASSIST_KEYS = [
  "DialogueNodeEvent:102:20",  // accepted DANI's offer (after 102:18)
  "DialogueNodeEvent:102:21",  // DANI orders the pieces (accepted path)
  "DialogueNodeEvent:102:23"   // DANI orders the pieces (forced, 5th attempt)
];

const SOIL_KEY_EVENT_TYPE = "Soil Key Puzzle";
const SOIL_KEY_END_STATUS = "Finished";
const UNIT_4 = /^Unit 4/;

const YELLOW_KEYS = [
  "DialogueNodeEvent:102:9",   // 3rd attempt, 1-2 wrong
  "DialogueNodeEvent:102:10",  // 3rd attempt, 3-4 wrong
  "DialogueNodeEvent:102:12",  // 4th attempt, 1-2 wrong
  "DialogueNodeEvent:102:18"   // 4th attempt, 3-4 wrong (assist offered)
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:102:4",   // 1st attempt, 1-2 wrong
  "DialogueNodeEvent:102:3",   // 1st attempt, 3-4 wrong
  "DialogueNodeEvent:102:7",   // 2nd attempt, any wrong (particle-size hint)
  "DialogueNodeEvent:102:9",   // 3rd attempt, 1-2 wrong
  "DialogueNodeEvent:102:10",  // 3rd attempt, 3-4 wrong (rate-graph hint)
  "DialogueNodeEvent:102:12",  // 4th attempt, 1-2 wrong
  "DialogueNodeEvent:102:18"   // 4th attempt, 3-4 wrong (assist offered)
];

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!latestTrigger) {
  ({ triggered: false, attempt_number: 0 });
} else {
  // 2) Window start: latest Unit 4 soil key puzzle close before the trigger
  const soilKeyClose = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: SOIL_KEY_EVENT_TYPE,
      "data.Soil Key Puzzle Status": SOIL_KEY_END_STATUS,
      "data.Unit": UNIT_4,
      _id: { $lt: latestTrigger._id }
    },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = soilKeyClose ? soilKeyClose._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  // 3) DANI's assist did not execute, forced or accepted (otherwise SOLVED_WITH_ASSIST applies)
  const assisted =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: ASSIST_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 4) A yellow key fired — 3rd-or-later submission was wrong
  const hasYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: YELLOW_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  // 5) Count incorrect arrangements
  const negCount = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  ({ triggered: !assisted && hasYellow, attempt_number: negCount + 1 });
}
```


### Teacher Guidance
Remind students that infiltration is the process by which water on the ground surface enters the soil. Water moves through sand at a slower rate than gravel and a faster rate than clay.
