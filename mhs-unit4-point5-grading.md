# Unit 4 Point 5 Grading

**Activity:** Saving Cadet Anderson

**Trigger(Start) Event:** `questActiveEvent:36`
**Trigger(End) Event:** `questActiveEvent:41`

---

## Grading Rule

This progress point recording how players perform within the argumentation task. This will first check whether the player successfully construct the correct argumentation (whether their log record contains (`DialogueNodeEvent:90:50`, `DialogueNodeEvent:90:57`)).
Then it will check how many negative feedback got from the argumentation construction.
If there is no correct feedback then the color is yellow, or the negative feedback number surpass 4, or both then the color is yellow, otherwise green.

| Outcome | Condition |
|---------|-----------|
| **Green** | Have correct feedback and the negative feedback number is less than 4 |
| **Yellow** | Either no correct feedback or the negative feedback number is equal to or larger than 4 or both |

### Attempt Window (Production)

- **Start:** Previous `questActiveEvent:41` (exclusive)
- **End:** Latest `questActiveEvent:41` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:41` |
| Target | `DialogueNodeEvent:90:50` |
| Target | `DialogueNodeEvent:90:57` |
| Target | `DialogueNodeEvent:90:25` |
| Target | `DialogueNodeEvent:90:37` |
| Target | `DialogueNodeEvent:90:39` |
| Target | `DialogueNodeEvent:90:45` |
| Target | `DialogueNodeEvent:90:47` |
| Target | `DialogueNodeEvent:90:52` |
| Target | `DialogueNodeEvent:90:54` |
| Target | `DialogueNodeEvent:90:55` |
| Target | `DialogueNodeEvent:90:56` |
| Target | `DialogueNodeEvent:90:58` |
| Target | `DialogueNodeEvent:90:59` |
| Target | `DialogueNodeEvent:90:60` |
| Target | `DialogueNodeEvent:90:61` |


---

## Analytics Script

```js
// Unit 4, Point 5 — Analytics-matching script
// Trigger eventKey: "questActiveEvent:41"

const playerId = "<playerId>";

const POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"];

const NEG_KEYS = [
  "DialogueNodeEvent:90:25","DialogueNodeEvent:90:37","DialogueNodeEvent:90:39",
  "DialogueNodeEvent:90:45","DialogueNodeEvent:90:47","DialogueNodeEvent:90:52",
  "DialogueNodeEvent:90:54","DialogueNodeEvent:90:55","DialogueNodeEvent:90:56",
  "DialogueNodeEvent:90:58","DialogueNodeEvent:90:59","DialogueNodeEvent:90:60",
  "DialogueNodeEvent:90:61"
];

const has_trigger =
  db.logdata.findOne(
    { playerId: playerId, eventKey: { $in: POS_KEYS } }
  ) !== null;

let color;

if (!has_trigger) {
  color = 2; 
} else {
  const cnt = db.logdata.countDocuments({
    playerId: playerId,
    eventKey: { $in: NEG_KEYS }
  });

  color = (cnt >= 3) ? "yellow" : "green";
}

color;
```

## Production Script (Attempt-Based)

```js
// Unit 4, Point 5 — Production (replay-safe, latest attempt window)
// Trigger eventKey: "questActiveEvent:41"

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:41";

const POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"];

const NEG_KEYS = [
  "DialogueNodeEvent:90:25","DialogueNodeEvent:90:37","DialogueNodeEvent:90:39",
  "DialogueNodeEvent:90:45","DialogueNodeEvent:90:47","DialogueNodeEvent:90:52",
  "DialogueNodeEvent:90:54","DialogueNodeEvent:90:55","DialogueNodeEvent:90:56",
  "DialogueNodeEvent:90:58","DialogueNodeEvent:90:59","DialogueNodeEvent:90:60",
  "DialogueNodeEvent:90:61"
];

const latestTrigger = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 }}
);

if (!latestTrigger) {
  "yellow";
} else {
  const prevTrigger = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: TRIGGER_KEY,
      _id: { $lt: latestTrigger._id }
    },
    { sort: { _id: -1 }}
  );

  const windowStartId = prevTrigger
    ? prevTrigger._id
    : ObjectId("000000000000000000000000");

  const windowEndId = latestTrigger._id;

  const has_trigger =
    db.logdata.findOne(
      {
        game: "mhs",
        playerId: playerId,
        eventKey: { $in: POS_KEYS },
        _id: { $gt: windowStartId, $lte: windowEndId }
      }
    ) !== null;

  if (!has_trigger) {
    "yellow";
  } else {
    const cnt = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: NEG_KEYS },
      _id: { $gt: windowStartId, $lte: windowEndId }
    });

    cnt >= 3 ? "yellow" : "green";
  }
}
```

---

## Reason Codes

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questActiveEvent:41` has not been logged.

### MISSING_SUCCESS_NODE

**Short Description:** Student did not successfully construct the correct argumentation.

**Instructor Message:** The student did not reach the expected success outcome for the argumentation task. Neither `DialogueNodeEvent:90:50` nor `DialogueNodeEvent:90:57` were found, indicating the student did not successfully construct the correct argument about saving Cadet Anderson.

**Determination:** Neither positive feedback node (`DialogueNodeEvent:90:50`, `90:57`) is present in the attempt window.

**Teacher Guidance:** Review the argumentation task with the student. Discuss how to construct a complete scientific argument with claim, evidence, and reasoning in the context of the rescue scenario.

### TOO_MANY_NEGATIVES

**Short Description:** Student received too many negative feedback responses during the argumentation task.

**Instructor Message:** The student received {negativeCount} negative feedback responses while constructing the argument about saving Cadet Anderson. The threshold for success is fewer than 4 negative responses.

**Quantities:** `negativeCount` — count of negative feedback events

**Determination:** The count of negative feedback nodes (`DialogueNodeEvent:90:25`, `90:37`, `90:39`, `90:45`, `90:47`, `90:52`, `90:54`-`90:61`) is 4 or more in the attempt window.

**Teacher Guidance:** Review the components of a scientific argument with the student:
1. Claim: a statement that answers the driving question
2. Evidence: scientific data and facts that support the claim
3. Reasoning: explains how or why the evidence supports the claim
