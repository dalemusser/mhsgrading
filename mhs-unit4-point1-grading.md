# Unit 4 Point 1 Grading

**Activity:** Well What Have We Here?: Water Table Basics

**Trigger(Start) Event:** `DialogueNodeEvent:88:0`
**Trigger(End) Event:** `DialogueNodeEvent:88:10`

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

- **Start:** Previous `DialogueNodeEvent:88:0` (exclusive)
- **End:** Latest `DialogueNodeEvent:88:10` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:88:10` |
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

const START_KEY = "DialogueNodeEvent:88:0";
const END_KEY = "DialogueNodeEvent:88:10";
const CORRECT_KEY = "DialogueNodeEvent:88:5";

const EVENT_TYPE = "Soil Key Puzzle";
const START_STATUS = "Started";
const END_STATUS = "Finished";

// 1) Most recent start anchor
const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

// 2) Most recent end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
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
      { sort: { _id: 1 }, projection: { serverTimestamp: 1, _id: 1 } }
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

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questActiveEvent:39` has not been logged.

### SCORE_BELOW_THRESHOLD

The reason for turning yellow in this progress point is becuase the aggregated score is less than 1, if there is no eventkey of `DialogueNodeEvent:88:5`, then the reason code WRONG_CHOISE_SELECTED will be triggered; if the duration is larger than 30 seconds then the reason code TOO_LONG_TO_SOLVE_PROBLEM will be triggured; if both conditions exist, then both reason codes triggered.

#### WRONG_CHOISE_SELECTED

**Short Description:** Missing the correct answer to the question.

**Instructor Message:** The student didn’t select the answer of “It’s the boundary between saturated and unsaturated soil layers” to a question from Anderson. One success condition is to select this answer at the first attempt.

**Determination:** Whether the eventkey of (`DialogueNodeEvent:88:5`) existed within the game log.

**Teacher Guidance:** Remind students the definition of water table: underground boundary between the soil surface and the area where groundwater saturates spaces between soil particles.

#### TOO_LONG_TO_SOLVE_PROBLEM

**Short Description:** Spent too much time on solving the soil key puzzle.

**Instructor Message:** The student spent too much time, {time duration} seconds, on solving the soil key puzzle. Depending on the time duration, there are two levels of the score the students can gain, if the students can solve the puzzle within 30 seconds, then the score could gain 1 point; if the students can solve the puzzle surpass 30 seconds but within 90 seconds, then the score could gain 0.5 point; if else there is no score could gain.

**Determination:** Calculate the time duration between `START_STATUS` and `END_STATUS` of `Soil Key Puzzle Status`.

**Teacher Guidance:** Remind students the definition of water table: underground boundary between the soil surface and the area where groundwater saturates spaces between soil particles.

#### Analytics-Matching Script (MongoDB/JS)








