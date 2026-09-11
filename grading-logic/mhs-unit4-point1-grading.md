# Unit 4 Point 1 Grading

**Activity:** Well What Have We Here?: Water Table Basics

**Trigger(Start) Event:** `DialogueNodeEvent:88:0`
**Trigger(End) Event:** The close of the soil key puzzle in Unit 4 — the `Soil Key Puzzle` event with `Soil Key Puzzle Status` = `Finished` and `Unit` matching Unit 4 (currently `"Unit 4 Dev"`; an eventType + data match, not an eventKey)

---

## Grading Rule

This progress point is a score-based assessment rubric. First, it will check whether the correct choice (`DialogueNodeEvent:88:5`) was selected, if so then the score will increase 0.5; Then, it will calculate the time duration (seconds) between the end and start event of soil key puzzle. If the time duration is less than or equal to 30 seconds, then the score will further add 1; If the time duration less than 90 seconds and larger than 30 seconds then the score will further increase 0.5, other situation will not increase any value.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 1 |
| **Yellow** | score < 1 |

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:88:0` (exclusive)
- **End:** Latest Unit 4 `Soil Key Puzzle` event with `Soil Key Puzzle Status` = `Finished` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `Soil Key Puzzle` event with `Soil Key Puzzle Status` = `Finished` and `Unit` matching Unit 4 (eventType + data match, not an eventKey) |
| Target | `DialogueNodeEvent:88:5` |
| Target | soil key puzzle |

---

## Analytics Script

```js
// Unit 4, Point 1 — Analytics-matching script
// Trigger: close of the Unit 4 soil key puzzle
// ("Soil Key Puzzle" event, "Soil Key Puzzle Status" = "Finished", Unit matching "Unit 4")

const playerId = "<playerId>";

const CORRECT_KEY = "DialogueNodeEvent:88:5";

const EVENT_TYPE = "Soil Key Puzzle";
const START_STATUS = "Started";
const END_STATUS = "Finished";
// data.Unit holds the scene name (currently "Unit 4 Dev"); match by prefix
// because the soil key puzzle also fires in Units 2 and 3.
const UNIT_4 = /^Unit 4/;

let score = 0.0;

const has8805 =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: CORRECT_KEY
      }
    ) !== null;

if (has8805) score += 0.5;

const startDoc = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: EVENT_TYPE,
      "data.Soil Key Puzzle Status": START_STATUS,
      "data.Unit": UNIT_4
    },
    { sort: { _id: 1 }}
  );

let durationSeconds = null;

if (startDoc && startDoc.serverTimestamp) {
    const endDoc = db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventType: EVENT_TYPE,
        "data.Soil Key Puzzle Status": END_STATUS,
        "data.Unit": UNIT_4
      },
      { sort: { _id: 1 }}
    );

    if (endDoc && endDoc.serverTimestamp) {
      const startMs = new Date(startDoc.serverTimestamp).getTime();
      const endMs = new Date(endDoc.serverTimestamp).getTime();
      if (!Number.isNaN(startMs) && !Number.isNaN(endMs)) {
        durationSeconds = (endMs - startMs) / 1000.0;
      }
    }
  }

if (durationSeconds !== null) {
    if (durationSeconds > 0 && durationSeconds <= 30) score += 1.0;
    else if (durationSeconds > 30 && durationSeconds <= 90) score += 0.5;
  }

const color = score >= 1 ? "green" : "yellow";

color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 1 — Attempt-based standalone production script (latest attempt)
// Start anchor: DialogueNodeEvent:88:0
// End anchor: close of the Unit 4 soil key puzzle
// ("Soil Key Puzzle" event, "Soil Key Puzzle Status" = "Finished", Unit matching "Unit 4")

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:88:0";
const CORRECT_KEY = "DialogueNodeEvent:88:5";

const EVENT_TYPE = "Soil Key Puzzle";
const START_STATUS = "Started";
const END_STATUS = "Finished";
// data.Unit holds the scene name (currently "Unit 4 Dev"); match by prefix
// because the soil key puzzle also fires in Units 2 and 3.
const UNIT_4 = /^Unit 4/;

// 1) Most recent start anchor
const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

// 2) Most recent end anchor: latest Unit 4 soil key puzzle close
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventType: EVENT_TYPE,
    "data.Soil Key Puzzle Status": END_STATUS,
    "data.Unit": UNIT_4
  },
  { sort: { _id: -1 }, projection: { _id: 1, serverTimestamp: 1 } }
);

// Must have both anchors
if (!latestStart || !latestEnd) {
  "yellow";
} else if (latestEnd._id <= latestStart._id) {
  // End must happen after start
  "yellow";
} else {
  const windowStartId = latestStart._id;
  const windowEndId = latestEnd._id;

  let score = 0.0;

  // +0.5 if correct choice selected inside window
  const has8805 =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: CORRECT_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      },
      { projection: { _id: 1 } }
    ) !== null;

  if (has8805) score += 0.5;

  // Find Started inside window (earliest, Unit 4 only)
  const startDoc = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: EVENT_TYPE,
      "data.Soil Key Puzzle Status": START_STATUS,
      "data.Unit": UNIT_4,
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    { sort: { _id: 1 }, projection: { serverTimestamp: 1, _id: 1 } }
  );

  let durationSeconds = null;

  // The end anchor itself is the puzzle close — its timestamp is the end time.
  if (startDoc && startDoc.serverTimestamp && latestEnd.serverTimestamp) {
    const startMs = new Date(startDoc.serverTimestamp).getTime();
    const endMs = new Date(latestEnd.serverTimestamp).getTime();

    if (!Number.isNaN(startMs) && !Number.isNaN(endMs)) {
      durationSeconds = (endMs - startMs) / 1000.0;
    }
  }

  // Duration scoring
  if (durationSeconds !== null) {
    if (durationSeconds > 0 && durationSeconds <= 30) score += 1.0;
    else if (durationSeconds > 30 && durationSeconds <= 90) score += 0.5;
  }

  score >= 1 ? "green" : "yellow";
}
```

---

## Reason Codes

### SCORE_BELOW_THRESHOLD

**Instructor Message:** In Well What Have We Here?, the student {choice_phrase} Anderson's question about what the water table is, and {duration_phrase} the soil key puzzle. This point earns green only when the puzzle is solved within 30 seconds, or within 90 seconds with the water-table question answered correctly. A missed question may reflect the common misconception that the water table is simply any underground water — it is specifically the boundary between the saturated and unsaturated soil layers — and a slow solve may indicate difficulty controlling the water level between the target lines.

#### Corresponding Script

```js
// U4P1: SCORE_BELOW_THRESHOLD — determine trigger and message phrases
// Mirrors the production color formula: +0.5 if 88:5 (correct water-table answer,
// single-shot question — 88:7 is the observable wrong choice), +1.0 if the Unit 4
// soil key puzzle took <= 30s, +0.5 if 30-90s; yellow when score < 1.

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:88:0";
const CORRECT_KEY = "DialogueNodeEvent:88:5";
const WRONG_KEY = "DialogueNodeEvent:88:7";   // "any water found underground"

const EVENT_TYPE = "Soil Key Puzzle";
const START_STATUS = "Started";
const END_STATUS = "Finished";
const UNIT_4 = /^Unit 4/;  // data.Unit is the scene name; puzzle also fires in U2/U3

const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

const latestEnd = db.logdata.findOne(
  {
    game: "mhs", playerId: playerId, eventType: EVENT_TYPE,
    "data.Soil Key Puzzle Status": END_STATUS, "data.Unit": UNIT_4
  },
  { sort: { _id: -1 }, projection: { _id: 1, serverTimestamp: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id <= latestStart._id) {
  ({ triggered: false, choice_phrase: "", duration_phrase: "" });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  const hasCorrect = db.logdata.findOne({
    game: "mhs", playerId: playerId, eventKey: CORRECT_KEY, ...windowFilter
  }, { projection: { _id: 1 } }) !== null;

  // Earliest Unit 4 puzzle start inside the window; the end anchor is the close.
  const startDoc = db.logdata.findOne(
    {
      game: "mhs", playerId: playerId, eventType: EVENT_TYPE,
      "data.Soil Key Puzzle Status": START_STATUS, "data.Unit": UNIT_4,
      ...windowFilter
    },
    { sort: { _id: 1 }, projection: { serverTimestamp: 1 } }
  );

  let durationSeconds = null;
  if (startDoc && startDoc.serverTimestamp && latestEnd.serverTimestamp) {
    const startMs = new Date(startDoc.serverTimestamp).getTime();
    const endMs = new Date(latestEnd.serverTimestamp).getTime();
    if (!Number.isNaN(startMs) && !Number.isNaN(endMs)) {
      durationSeconds = (endMs - startMs) / 1000.0;
    }
  }

  let score = 0.0;
  if (hasCorrect) score += 0.5;
  if (durationSeconds !== null) {
    if (durationSeconds > 0 && durationSeconds <= 30) score += 1.0;
    else if (durationSeconds > 30 && durationSeconds <= 90) score += 0.5;
  }

  const choicePhrase = hasCorrect
    ? "answered correctly"
    : "chose 'it's any water found underground' instead of the correct answer on";

  const durationPhrase = durationSeconds !== null
    ? "took " + Math.round(durationSeconds) + " seconds to solve"
    : "has no measured completion time for";

  ({ triggered: score < 1, choice_phrase: choicePhrase, duration_phrase: durationPhrase });
}
```

### Teacher Guidance 
Remind students the definition of water table: underground boundary between the soil surface and the area where groundwater saturates spaces between soil particles.




