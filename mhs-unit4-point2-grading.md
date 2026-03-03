# Unit 4 Point 2 Grading

**Activity:** Infiltration Glyph + Alien Well Floors 1 & 2

**Trigger Event:** `questActiveEvent:48`

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

- **Start:** Previous `questActiveEvent:48` (exclusive)
- **End:** Latest `questActiveEvent:48` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questActiveEvent:48` |
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

const playerId = "<playerId>";

const TRIGGER_KEY = "questActiveEvent:48";

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

> Still figuring out the reason codes
