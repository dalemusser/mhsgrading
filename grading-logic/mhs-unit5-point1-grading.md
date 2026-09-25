# Unit 5 Point 1 Grading

**Activity:** If I Had a Nickel- Floors 1 & 2

**Trigger(Start) Event:** `questActiveEvent:43`
**Trigger(End) Event:** `questFinishEvent:43`

---

## Grading Rule

This progress point is an attempt-based progress. If the player solved the puzzle (triggered `DialogueNodeEvent:100:44`) without triggering any of the following bad feedbacks (`DialogueNodeEvent:100:38`, `DialogueNodeEvent:100:39`, `DialogueNodeEvent:100:43`), the color is green; if the success dialogue never fired, or any of the bad feedbacks fired, the color is yellow.

| Outcome | Condition |
|---------|-----------|
| **Green** | `DialogueNodeEvent:100:44` present AND none of `100:38`, `100:39`, `100:43` in the window |
| **Yellow** | Success node missing OR any of those bad-feedback nodes present |

### Attempt Window (Production)

- **Start:** Latest `questActiveEvent:43` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `questFinishEvent:43` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the latest-start / latest-end form (yellow whenever the latest `questFinishEvent:43` preceded the latest `questActiveEvent:43`), per the start-and-end window decision (A1). Keys re-verified the same day against the 2026-09-21 dialogue database (conversation 100 unchanged: 18 nodes, same gates; only the texts of `100:42`, `100:44` and `100:46` changed). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `questActiveEvent:43` |
| Trigger (End) | `questFinishEvent:43` |
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
// Window start: latest questActiveEvent:43 before the end event (exclusive)
// Window end:   latest questFinishEvent:43 (inclusive)

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:43";
const WINDOW_END_KEY = "questFinishEvent:43";

const POS_KEY = "DialogueNodeEvent:100:44";
const NEG_KEYS = [
  "DialogueNodeEvent:100:38",
  "DialogueNodeEvent:100:39",
  "DialogueNodeEvent:100:43"
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
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
      eventKey: WINDOW_START_KEY,
      _id: { $lt: latestEnd._id }
    },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart
    ? latestStart._id
    : ObjectId("000000000000000000000000");
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

Assist-path markers (all four verified logging in runs 09-03-26-3 and
09-14-26-3, both of which walked the accepted-offer path end to end):

| Node | Meaning |
|------|---------|
| `100:40` | "Sure, I'm stuck." — assist offer accepted |
| `100:41` | Accepted-assist execution — "Activating holid projector" |
| `100:43` | Forced-assist execution (5th attempt) |
| `100:46` | DANI-helped completion — "We have finally solved this puzzle" |

Other nodes: `100:44` ("Well done, TK") fires on BOTH the independent and the
DANI-assisted paths — it is NOT an independence signal; `100:45` is the
curricular explanation (higher temperature → higher evaporation rate);
`100:30/31/32` are idle nudges before the first placement; `100:42` ("I'll take
another crack at it.", text added in the 2026-09-21 database) is the declined
offer — it returns the player to the puzzle and is deliberately not an assist
key.

**Assist does not solve the puzzle (game bug, open; re-checked 2026-09-24):**
in the Unity export `100:44` is titled `OnPlayerSolve` and `100:46`
`OnAutoSolve`, so by design only one of them should fire per attempt. In both
assisted runs the game fires `100:46` a few seconds after `100:41` but leaves
the tablets where they are: in 09-14-26-3 (build 20260914-) `100:46` came 6 s
after `100:41`, then seven interact inputs, then `100:44` 14 s later; in
09-03-26-3 (build 20260902) the tester placed a glyph after `100:46`, submitted
a fifth wrong order (`100:43` forced assist, `100:46` again) and only then
reached `100:44`. The grading holds regardless: the colour is yellow on every
assisted path because `100:39` (offer) or `100:43` (forced) is itself a colour
negative; SOLVED_WITH_ASSIST is detected from the assist nodes, never from
`100:44`'s absence; EXCESS_ATTEMPTS requires that no assist node fired, so an
assisted run can never be misfiled there; and `attempt_number` counts every wrong
arrangement, one feedback node each, `100:43` included, so the fifth wrong order
that forces the assist is counted like the forced nodes at U2P1 and U2P4
(aligned across U3P4, U4P2 and U5P1 on 2026-09-24): 4 in 09-14-26-3, 5 in
09-03-26-3, where the tester submitted a fifth wrong order after the accepted
assist failed to place the tablets. If the bug is not fixed before release, the instructor message's "DANI ordered the
tablets" should read "DANI showed the correct order", since the student still
had to place them.

### SOLVED_WITH_ASSIST

**Instructor Message:** In If I Had a Nickel (floors 1 and 2), the student did not complete the evaporation glyph puzzle independently. After {attempt_number} incorrect arrangements, the in-game guide DANI ordered the tablets. This point earns green only when the student solves the puzzle on their own within 4 attempts. Needing this level of support may indicate the student would benefit from reviewing how temperature drives evaporation: the higher the temperature, the higher the evaporation rate.

#### Corresponding Scripts

```js
// U5P1: SOLVED_WITH_ASSIST — determine trigger and attempt_number
// Window mirrors the production color script: latest questFinishEvent:43 (end),
// latest questActiveEvent:43 before it (start, exclusive; zero ObjectId when none).
// Triggers when any assist-path marker fired: 100:40 (offer accepted),
// 100:41 (accepted execution), 100:43 (forced execution), 100:46 (helped
// completion) — all four verified logging in runs 09-03-26-3 and 09-14-26-3.
// Do NOT infer assistance from 100:44's absence — it fires on the assisted
// path too (the projector does not move the tablets on the current build).
// attempt_number = incorrect arrangements, one feedback node each, 100:43
// included (the 5th wrong order that forces the assist is counted, as at
// U2P1/U2P4 and, since the 2026-09-24 alignment, U3P4/U4P2).

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
  "DialogueNodeEvent:100:39",  // 4th attempt, far (assist offered)
  "DialogueNodeEvent:100:43"   // 5th attempt, any wrong — forces the assist (counted since 2026-09-24, as at U2P1/U2P4)
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  // No finished attempt (incl. the started-but-unfinished pencil case)
  ({ triggered: false, attempt_number: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );
  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  // 3) Any assist-path marker in the window?
  const assisted =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: { $in: ASSIST_KEYS }, ...windowFilter
    }) !== null;

  // 4) Count incorrect arrangements
  const attemptNumber = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS }, ...windowFilter
  });

  ({ triggered: assisted, attempt_number: attemptNumber });
}
```

### EXCESS_ATTEMPTS

**Instructor Message:** In If I Had a Nickel (floors 1 and 2), the student solved the evaporation glyph puzzle on their own, but needed {attempt_number} attempts. This point earns green only when the puzzle is solved within 4 attempts. Repeated incorrect arrangements may indicate difficulty matching the wall images (temperatures at different times of day) to the evaporation rates they would produce.

#### Corresponding Scripts

```js
// U5P1: EXCESS_ATTEMPTS — determine trigger and attempt_number
// Same window as the color script (latest questFinishEvent:43, latest
// questActiveEvent:43 before it). Triggers when the student solved the
// puzzle without DANI's assist but a color negative fired (100:38 / 100:39 /
// 100:43 — the 4th-attempt-and-later feedback), i.e. success took 5+ attempts
// or came right after a 4th-attempt miss. Mirrors the color rule's yellow set
// verbatim so the code can never disagree with the cell. Because every assist
// node is excluded first, an assisted run can never land here even though
// 100:44 also fires on the assisted path (auto-solve bug).
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
  "DialogueNodeEvent:100:39",  // 4th attempt, far (assist offered)
  "DialogueNodeEvent:100:43"   // 5th attempt, any wrong — forces the assist (counted since 2026-09-24, as at U2P1/U2P4)
];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  ({ triggered: false, attempt_number: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );
  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  // 3) DANI's assist did not run (otherwise SOLVED_WITH_ASSIST applies)
  const assisted =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: { $in: ASSIST_KEYS }, ...windowFilter
    }) !== null;

  // 4) A color negative fired — 4th-or-later submission was wrong
  const hasColorNeg =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: { $in: COLOR_NEG_KEYS }, ...windowFilter
    }) !== null;

  // 5) Count incorrect arrangements
  const negCount = db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS }, ...windowFilter
  });

  ({ triggered: !assisted && hasColorNeg, attempt_number: negCount + 1 });
}
```

### Teacher Guidance
Remind students that evaporation  is the phase change that occurs when energy is added to liquid to turn it into a gas Have students work through Unit 5 followup activity.
