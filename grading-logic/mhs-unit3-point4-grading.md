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

- **Start:** Latest `questActiveEvent:18` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `DialogueNodeEvent:73:200` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics. `questActiveEvent:18` fires two or three times per playthrough (quest stages); the latest one before the end is the glyph-room entry, and every conversation-78 node follows it.
- Changed 2026-09-24: previously the script took the latest start and the latest end and returned yellow unless the end came after the start (a re-entered activity with no new end lost its grade); per the start-and-end window decision (A1) it now anchors on the end first. Same-day review against the 2026-09-21 dialogue database: conversations 73 and 78 unchanged (all keys present; the export carries explicit attempt gates), and the accepted-assist nodes `78:20` / `78:21` were added to the reason-code assist keys (colour keys unchanged). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `questActiveEvent:18` |
| Trigger (End) | `DialogueNodeEvent:73:200` |
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
// Window start: latest questActiveEvent:18 before the end event (exclusive)
// Window end:   latest DialogueNodeEvent:73:200 (inclusive)

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:18";
const END_KEY = "DialogueNodeEvent:73:200";
const GATE_KEY = "DialogueNodeEvent:78:24";

const TARGET_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

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

  // 3) Gate: must have 78:24 within (start, end]
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
    // 4) Count target events within the window
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
```

---

## Reason Codes

Conversation 78 ("U3/Glyph Games/Dissolving Particles", 16 nodes; gates re-verified against the 2026-09-21 dialogue database on 2026-09-24): each wrong submission fires exactly one attempt-indexed node — attempt 1 `78:4` (1–2 wrong) / `78:3` (3 wrong), attempt 2 `78:7`, attempt 3 `78:9` / `78:10`, attempt 4 `78:12` / `78:18` (offer: `78:19` decline, `78:20` accept → `78:21` "Activating holid projector"), attempt 5 `78:23` (forced assist). `78:24` ("OnSolve") fires whenever the puzzle is solved, on every path; `78:14`–`78:16` are idle hints. Game behaviour to note (build 20260914-, log 09-14-26-3): after the forced assist `78:23` the pieces did NOT move — the student placed two more pieces before `78:24` fired — so the "solved by yourself" completion cannot be inferred from `78:24`; assistance is detected positively from the offer/accept/execution/forced nodes instead, as at U2P1 and U2P4. `attempt_number` counts every attempt-indexed node, `78:23` included, so the fifth wrong order that forces the assist is counted like the forced nodes at U2P1 and U2P4 (aligned across U3P4, U4P2 and U5P1 on 2026-09-24; until then the glyph puzzles reported 4 on the forced path). If the game team does not restore the auto-solve, the SOLVED_WITH_ASSIST wording "DANI ordered the pieces" should become "DANI showed the correct order".

### SOLVED_WITH_ASSIST

**Instructor Message:** In Forsaken Facility, the student did not complete the ordering puzzle showing how materials dissolve into water independently. After {attempt_number} incorrect arrangements, the in-game guide DANI ordered the pieces. This point earns green only when the student submits the correct order on their own within 3 attempts. Needing this level of support may indicate the student would benefit from reviewing how the particles of a dissolved material spread through water, even once they can no longer be seen.

#### Corresponding Script

```js
// U3P4: SOLVED_WITH_ASSIST — determine trigger and attempt_number
// Window mirrors the production color script: latest DialogueNodeEvent:73:200 (end),
// latest questActiveEvent:18 before it (start, exclusive; zero ObjectId when none).
// Triggers when an assist marker fired in the window — forced (78:23, 5th attempt)
// or accepted (78:20 "Sure. I'm stuck" after the 4th-attempt offer 78:18, then
// 78:21 "Activating holid projector") — or when the completion gate 78:24 is
// absent. The accepted nodes were added 2026-09-24 (gates verified in the
// 2026-09-21 export; the path is not yet observed in a log). On the current
// build the projector does not move the pieces, so 78:24 also fires after an
// assisted solve; assistance is therefore detected from these nodes, never
// from the completion marker. attempt_number = attempt-indexed feedback nodes,
// one per wrong submission, 78:23 included (the 5th wrong order that forces the
// assist is counted, as at U2P1/U2P4; aligned 2026-09-24).

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:18";
const END_KEY   = "DialogueNodeEvent:73:200";
const GATE_KEY  = "DialogueNodeEvent:78:24";  // "OnSolve" completion marker

const ASSIST_KEYS = [
  "DialogueNodeEvent:78:20",  // accepted offer after the 4th attempt ("Sure. I'm stuck")
  "DialogueNodeEvent:78:21",  // DANI: "I have calculated the correct order... Activating holid projector."
  "DialogueNodeEvent:78:23"   // forced assist, 5th attempt
];

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:78:4",   // 1st attempt, 1-2 wrong
  "DialogueNodeEvent:78:3",   // 1st attempt, 3 wrong
  "DialogueNodeEvent:78:7",   // 2nd attempt, any wrong (microscope hint)
  "DialogueNodeEvent:78:9",   // 3rd attempt, 1-2 wrong
  "DialogueNodeEvent:78:10",  // 3rd attempt, 3 wrong
  "DialogueNodeEvent:78:12",  // 4th attempt, 1-2 wrong
  "DialogueNodeEvent:78:18",  // 4th attempt, 3 wrong (assist offered)
  "DialogueNodeEvent:78:23"   // 5th attempt, any wrong — forces the assist (counted since 2026-09-24, as at U2P1/U2P4)
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  ({ triggered: false, attempt_number: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  // 3) Any assist marker (accepted or forced) inside the window
  const assisted = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: { $in: ASSIST_KEYS }, ...windowFilter
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
// Window mirrors the production color script: latest DialogueNodeEvent:73:200 (end),
// latest questActiveEvent:18 before it (start, exclusive; zero ObjectId when none).
// Triggers when the student completed the puzzle (gate 78:24 present, no assist
// marker of either kind) but the color count — all 8 target keys, one per wrong
// submission — reached 3+, i.e. success took 4+ attempts. Without an assist the
// count can only be 3 (solved on attempt 4) or 4 (declined the offer, solved on
// attempt 5); a 5th wrong submission forces the assist.
// attempt_number = incorrect submissions + 1 (the final correct submission).

const playerId = "<playerId>";

const START_KEY = "questActiveEvent:18";
const END_KEY   = "DialogueNodeEvent:73:200";
const GATE_KEY  = "DialogueNodeEvent:78:24";

const ASSIST_KEYS = [
  "DialogueNodeEvent:78:20",  // accepted offer ("Sure. I'm stuck")
  "DialogueNodeEvent:78:21",  // DANI: "Activating holid projector."
  "DialogueNodeEvent:78:23"   // forced assist, 5th attempt
];

const COLOR_TARGET_KEYS = [
  "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
  "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
  "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23"
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  ({ triggered: false, attempt_number: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  // 3) Any assist marker (accepted or forced) inside the window
  const assisted = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: { $in: ASSIST_KEYS }, ...windowFilter
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