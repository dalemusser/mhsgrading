# Unit 4 Point 1 Grading

**Activity:** Well Wishes

**Trigger(Start) Event:** `DialogueNodeEvent:88:0`
**Trigger(End) Event:** `questActiveEvent:39`

---

## Grading Rule

This progress point is a score-based assessment rubric. First, it will check whether the correct choice (`DialogueNodeEvent:88:5`) was selected, if so then the score will increase 0.5;
Then, it will calculate the time duration (seconds) between the end and start event of soil key puzzle. If the time duration is less than or equal to 30 seconds, then the score will add 1;
If the time duration less than 90 seconds and larger than 30 seconds then the score will increase 0.5, other situation will not increase any value.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 1 |
| **Yellow** | score < 1 |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:39` (exclusive)
- **End:** Latest `questActiveEvent:39` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:39` |
| Target | `DialogueNodeEvent:88:5` |
| Target | soil key puzzle |

---

## Analytics Script

```js
// Unit 4, Point 1 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:39"

const playerId = "<playerId>";

const CORRECT_KEY = "DialogueNodeEvent:88:5";

const EVENT_TYPE = "Soil Key Puzzle";
const START_STATUS = "Started";
const END_STATUS = "Finished";

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
      "data.Soil Key Puzzle Status": START_STATUS
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
        "data.Soil Key Puzzle Status": END_STATUS
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
// Trigger eventKey: "questActiveEvent:39"

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:39";
const CORRECT_KEY = "DialogueNodeEvent:88:5";

const EVENT_TYPE = "Soil Key Puzzle";
const START_STATUS = "Started";
const END_STATUS = "Finished";

// 1) Latest trigger (end anchor)
const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestTrigger) {
  "yellow";
} else {
  // 2) Previous trigger (attempt boundary)
  const prevTrigger = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: TRIGGER_KEY,
      _id: { $lt: latestTrigger._id }
    },
    { sort: { _id: -1 }}
  );

  const windowStartId = prevTrigger ? prevTrigger._id : ObjectId("000000000000000000000000");
  const windowEndId = latestTrigger._id;

  let score = 0.0;

  // +0.5 if correct choice selected inside window
  const has8805 =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: CORRECT_KEY,
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (has8805) score += 0.5;

  // Find Started inside window (earliest)
  const startDoc = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: EVENT_TYPE,
      "data.Soil Key Puzzle Status": START_STATUS,
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    { sort: { _id: 1 }, projection: { serverTimestamp: 1, _id: 1 } }
  );

  let durationSeconds = null;

  if (startDoc && startDoc.serverTimestamp) {
    // Find Finished AFTER startDoc, still within window
    const endDoc = db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventType: EVENT_TYPE,
        "data.Soil Key Puzzle Status": END_STATUS,
        _id: { $gt: startDoc._id, $lte: windowEndId }
      },
      { sort: { _id: 1 }, projection: { serverTimestamp: 1 } }
    );

    if (endDoc && endDoc.serverTimestamp) {
      const startMs = new Date(startDoc.serverTimestamp).getTime();
      const endMs = new Date(endDoc.serverTimestamp).getTime();
      if (!Number.isNaN(startMs) && !Number.isNaN(endMs)) {
        durationSeconds = (endMs - startMs) / 1000.0;
      }
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

> Still figuring out the reason codes
