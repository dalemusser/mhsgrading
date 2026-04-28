# Unit 5 Point 3 Grading

**Activity:** What Happened Here?

**Trigger(Start) Event:** `DialogueNodeEvent:96:1`
**Trigger(End) Event:** `questFinishEvent:44`

---

## Grading Rule

This progress point is an attempt-based, if the total number of following dialogues (`DialogueNodeEvent:108:25`,`DialogueNodeEvent:108:32`,`DialogueNodeEvent:108:33`,`DialogueNodeEvent:108:37`,`DialogueNodeEvent:108:39`,`DialogueNodeEvent:108:41`,`DialogueNodeEvent:108:47`,`DialogueNodeEvent:108:53`,`DialogueNodeEvent:108:54`,`DialogueNodeEvent:108:55`,`DialogueNodeEvent:108:59`,`DialogueNodeEvent:108:60`,`DialogueNodeEvent:108:61`,`DialogueNodeEvent:108:62`,`DialogueNodeEvent:108:70`,`DialogueNodeEvent:108:72`,`DialogueNodeEvent:108:73`,`DialogueNodeEvent:108:74`,`DialogueNodeEvent:108:75`,`DialogueNodeEvent:108:76`,`DialogueNodeEvent:108:78`,`DialogueNodeEvent:108:79`,`DialogueNodeEvent:108:80`,`DialogueNodeEvent:108:82`,`DialogueNodeEvent:108:83`,`DialogueNodeEvent:108:84`,`DialogueNodeEvent:108:85`,`DialogueNodeEvent:108:86`,`DialogueNodeEvent:108:87`,`DialogueNodeEvent:108:88`,`DialogueNodeEvent:108:89`,`DialogueNodeEvent:108:90`,`DialogueNodeEvent:108:91`) happened is euqal to or larger than 4 then the color returns yellow, otherwise it will return green.

| Outcome | Condition |
|---------|-----------|
| **Green** | attempt <= 4 |
| **Yellow** | attempt > 4 |

### Attempt Window (Production)

- **Start:** Previous `DialogueNodeEvent:96:1` (exclusive)
- **End:** Latest `questFinishEvent:44` (inclusive)

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:44` |
| Target | `DialogueNodeEvent:108:25` |
| Target | `DialogueNodeEvent:108:32` |
| Target | `DialogueNodeEvent:108:33` |
| Target | `DialogueNodeEvent:108:37` |
| Target | `DialogueNodeEvent:108:39` |
| Target | `DialogueNodeEvent:108:41` |
| Target | `DialogueNodeEvent:108:47` |
| Target | `DialogueNodeEvent:108:53` |
| Target | `DialogueNodeEvent:108:54` |
| Target | `DialogueNodeEvent:108:55` |
| Target | `DialogueNodeEvent:108:59` |
| Target | `DialogueNodeEvent:108:60` |
| Target | `DialogueNodeEvent:108:61` |
| Target | `DialogueNodeEvent:108:62` |
| Target | `DialogueNodeEvent:108:70` |
| Target | `DialogueNodeEvent:108:72` |
| Target | `DialogueNodeEvent:108:73` |
| Target | `DialogueNodeEvent:108:74` |
| Target | `DialogueNodeEvent:108:75` |
| Target | `DialogueNodeEvent:108:76` |
| Target | `DialogueNodeEvent:108:78` |
| Target | `DialogueNodeEvent:108:79` |
| Target | `DialogueNodeEvent:108:80` |
| Target | `DialogueNodeEvent:108:82` |
| Target | `DialogueNodeEvent:108:83` |
| Target | `DialogueNodeEvent:108:84` |
| Target | `DialogueNodeEvent:108:85` |
| Target | `DialogueNodeEvent:108:86` |
| Target | `DialogueNodeEvent:108:87` |
| Target | `DialogueNodeEvent:108:88` |
| Target | `DialogueNodeEvent:108:89` |
| Target | `DialogueNodeEvent:108:90` |
| Target | `DialogueNodeEvent:108:91` |

---

## Analytics Script

```js
// Unit 5, Point 3 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:44"

const playerId = "<playerId>";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
  "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
  "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
  "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
  "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:70",
  "DialogueNodeEvent:108:72", "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74",
  "DialogueNodeEvent:108:75", "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78",
  "DialogueNodeEvent:108:79", "DialogueNodeEvent:108:80", "DialogueNodeEvent:108:82",
  "DialogueNodeEvent:108:83", "DialogueNodeEvent:108:84", "DialogueNodeEvent:108:85",
  "DialogueNodeEvent:108:86", "DialogueNodeEvent:108:87", "DialogueNodeEvent:108:88",
  "DialogueNodeEvent:108:89", "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91"
];

const cnt = db.logdata.countDocuments({
  playerId: playerId,
  eventKey: { $in: NEGATIVE_KEYS }
});

const color = (cnt >= 4) ? "yellow" : "green";

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe attempt-based color script
// Window start: "DialogueNodeEvent:96:1"
// Window end:   "questFinishEvent:44"

const playerId = "<playerId>";

const WINDOW_START_KEY = "DialogueNodeEvent:96:1";
const WINDOW_END_KEY = "questFinishEvent:44";

const NEGATIVE_KEYS = [
  "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
  "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
  "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
  "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
  "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:70",
  "DialogueNodeEvent:108:72", "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74",
  "DialogueNodeEvent:108:75", "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78",
  "DialogueNodeEvent:108:79", "DialogueNodeEvent:108:80", "DialogueNodeEvent:108:82",
  "DialogueNodeEvent:108:83", "DialogueNodeEvent:108:84", "DialogueNodeEvent:108:85",
  "DialogueNodeEvent:108:86", "DialogueNodeEvent:108:87", "DialogueNodeEvent:108:88",
  "DialogueNodeEvent:108:89", "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91"
];

// 1) Most recent window start
const latestStart = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_START_KEY
  },
  { sort: { _id: -1 }}
);

// 2) Most recent window end
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 }}
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  "yellow";
} else {
  const windowStartId = latestStart._id;
  const windowEndId = latestEnd._id;

  const cnt = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: { $in: NEGATIVE_KEYS },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  cnt >= 4 ? "yellow" : "green";
}
```

---

## Reason Codes

### NO_TRIGGER

**Short Description:** Student has not yet completed the trigger event for this activity.

**Instructor Message:** The student has not yet reached the point in the game where this progress point is evaluated.

**Determination:** The trigger event `questFinishEvent:44` has not been logged.

### WRONG_ARG_SELECTED

**Short Description:** The students submitted too many wrong arguments before submitting the correct one.

**Instructor Message:** Before submitting the correct argument, the student triggered {negativeCount} negative feedback before submitting the correct argument.

**Quantities:** `negativeCount` — count of negative dialogue events

**Determination:** The count of negative dialogue nodes (33 target events across `DialogueNodeEvent:108:*`) is 4 or more in the attempt window.

**Teacher Guidance:** Review parts of an argument with students. Have students work through argumentation review followup activity.

#### Analytics-Matching Script (MongoDB/JS)