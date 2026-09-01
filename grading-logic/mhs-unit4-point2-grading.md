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

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questActiveEvent:48` has not been logged.

### MISSING_SUCCESS_NODE

**Short Description:** Student did not complete the infiltration glyph puzzle independently.

**Instructor Message:** The student did not reach the expected success outcome (`DialogueNodeEvent:88:11`) for the infiltration glyph matching puzzle. This indicates the student may not have completed the puzzle on their own.

**Determination:** The success node `DialogueNodeEvent:88:11` is absent from the attempt window.

**Teacher Guidance:** Remind students that infiltration is the process by which water on the ground surface enters the soil. Water moves through sand at a slower rate than gravel and a faster rate than clay.

### TOO_MANY_NEGATIVES

**Short Description:** Student received negative feedback indicating too many puzzle attempts.

**Instructor Message:** The student received corrective feedback during the infiltration glyph puzzle, indicating they needed more than 2 attempts to figure out the correct matches.

**Determination:** Any of the negative feedback nodes (`DialogueNodeEvent:102:9`, `DialogueNodeEvent:102:10`, `DialogueNodeEvent:102:12`, `DialogueNodeEvent:102:18`, `DialogueNodeEvent:102:23`) are present in the attempt window.

**Teacher Guidance:** Remind students that infiltration is the process by which water on the ground surface enters the soil. Water moves through sand at a slower rate than gravel and a faster rate than clay.
