# Unit 2 Point 6 Grading

**Activity:** Which Watershed? Part I

**Trigger(Start) Event:** `DialogueNodeEvent:23:42`
**Trigger(End) Event:** `DialogueNodeEvent:20:46`

---

## Grading Rule

Student must select the correct criterion for determining watershed size on the first try.

| Outcome | Condition |
|---------|-----------|
| **Green** | Pass node present AND no yellow nodes in attempt window |
| **Yellow** | Pass node missing OR any yellow node present |

### Attempt Window (Production)

- **Start:** Latest `DialogueNodeEvent:23:42` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `DialogueNodeEvent:20:46` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24: previously the script took the latest start and the latest end and returned yellow unless the end came after the start (a re-entered activity with no new end lost its grade); per the start-and-end window decision (A1) it now anchors on the end first. Keys re-verified the same day against the 2026-09-21 dialogue database (conversation 20 unchanged; `20:42` offers exactly `20:43` / `20:44` / `20:45`, each leading straight to `20:46`). Both Python transcriptions follow; the Go rule must be updated in step.

> Note: `DialogueNodeEvent:20:35` opens the question mid-attempt and must not anchor the window, since the pass/yellow nodes fire after it.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `DialogueNodeEvent:23:42` |
| Trigger (End) | `DialogueNodeEvent:20:46` |
| Pass (correct choice) | `DialogueNodeEvent:20:43` |
| Yellow (wrong choice) | `DialogueNodeEvent:20:44` |
| Yellow (wrong choice) | `DialogueNodeEvent:20:45` |

---

## Analytics Script

```js
// Unit 2, Point 6 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:20:46"

const playerId = "<playerId>";

const passKey = "DialogueNodeEvent:20:43";

const yellowKeys = [
  "DialogueNodeEvent:20:44",
  "DialogueNodeEvent:20:45"
];

const hasPass =
  db.logdata.findOne({
    game: "mhs",
    playerId: playerId,
    eventKey: passKey
  }) !== null;

if (!hasPass) {
  "yellow";
} else {
  const hasYellow =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: yellowKeys }
    }) !== null;

  const color = hasYellow ? "yellow" : "green";
  color;
}
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 6 — Attempt-based standalone production grading script
// Window start: latest DialogueNodeEvent:23:42 before the end event (exclusive)
// Window end:   latest DialogueNodeEvent:20:46 (inclusive)

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:23:42"; // opens the activity
const END_KEY   = "DialogueNodeEvent:20:46"; // closes the attempt
const PASS_KEY  = "DialogueNodeEvent:20:43";
const YELLOW_KEYS = ["DialogueNodeEvent:20:44", "DialogueNodeEvent:20:45"];

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

  // 3) Must have PASS_KEY within attempt window
  const hasPass =
    db.logdata.findOne({
      game: "mhs",
      playerId: playerId,
      eventKey: PASS_KEY,
      _id: { $gt: windowStartId, $lte: windowEndId }
    }) !== null;

  if (!hasPass) {
    "yellow";
  } else {
    // 4) Must have none of YELLOW_KEYS within attempt window
    const hasYellow =
      db.logdata.findOne({
        game: "mhs",
        playerId: playerId,
        eventKey: { $in: YELLOW_KEYS },
        _id: { $gt: windowStartId, $lte: windowEndId }
      }) !== null;

    hasYellow ? "yellow" : "green";
  }
}
```

---

## Reason Codes

### WRONG_EVIDENCE_SELECTED

**Instructor Message:** In Which Watershed? Part I, when Dr. Toppo asked which observation provides the strongest evidence for identifying the larger watershed, the student selected {wrong_choice} instead of the correct answer, water flow rate. This point earns green only when water flow rate is selected. This may indicate difficulty distinguishing evidence that directly relates to watershed size - a larger drainage area collects and delivers more water, producing a greater flow rate - from observations such as waterfall height or salinity that do not indicate how much land drains to the river.

#### Corresponding Script

```js
// U2P6: WRONG_EVIDENCE_SELECTED — determine trigger and wrong_choice
// Window mirrors the production color script: latest DialogueNodeEvent:20:46 (end),
// latest DialogueNodeEvent:23:42 before it (start, exclusive; zero ObjectId when none).
// Triggers when a wrong-option node (20:44 waterfall height, 20:45 salinity)
// fired in the attempt window. The question is single-select with no retry
// (20:42 -> 43 | 44 | 45 -> 46 in the 2026-09-21 dialogue database), so exactly
// one choice node fires per window; the both-options fallback below is defensive only.

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:23:42"; // opens the activity (exclusive)
const END_KEY   = "DialogueNodeEvent:20:46"; // closes the attempt (inclusive)
const HEIGHT_KEY   = "DialogueNodeEvent:20:44"; // chose waterfall height
const SALINITY_KEY = "DialogueNodeEvent:20:45"; // chose salinity

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  ({ triggered: false, wrong_choice: null });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  const hasHeight =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: HEIGHT_KEY, ...windowFilter
    }) !== null;

  const hasSalinity =
    db.logdata.findOne({
      game: "mhs", playerId: playerId,
      eventKey: SALINITY_KEY, ...windowFilter
    }) !== null;

  let wrongChoice = null;
  if (hasHeight && hasSalinity) wrongChoice = "waterfall height and salinity";
  else if (hasHeight) wrongChoice = "waterfall height";
  else if (hasSalinity) wrongChoice = "salinity";

  ({ triggered: wrongChoice !== null, wrong_choice: wrongChoice });
}
```

### Teacher Guidance
1. Claim: statement that answers the driving question.
2. Evidence: scientific data and facts that support your claim.