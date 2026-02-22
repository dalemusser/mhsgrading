# Unit 2 Point 3 Grading

**Activity:** Getting the Band Back Together Part II

**Trigger Event:** `DialogueNodeEvent:22:18`

---

## Grading Rule

Windowed rule using client timestamps. Count wrong-direction prompts between the start and end of the activity. The student should trigger at most 6 wrong-direction dialogues.

| Outcome | Condition |
|---------|-----------|
| **Green** | Target count <= 6 within the activity window |
| **Yellow** | Target count > 6, or start/end events missing |

### Activity Window

- **Start Key:** `DialogueNodeEvent:20:33`
- **End Key:** `DialogueNodeEvent:22:1`

### Attempt Window (Production)

Uses the latest trigger `DialogueNodeEvent:22:18` and the most recent start key before it, fenced by `_id` range.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:22:18` |
| Start | `DialogueNodeEvent:20:33` |
| End (analytics) | `DialogueNodeEvent:22:1` |
| Target (wrong direction) | `DialogueNodeEvent:18:225` |
| Target (wrong direction) | `DialogueNodeEvent:28:185` |
| Target (wrong direction) | `DialogueNodeEvent:59:185` |
| Target (wrong direction) | `DialogueNodeEvent:28:184` |
| Target (wrong direction) | `DialogueNodeEvent:28:191` |
| Target (wrong direction) | `DialogueNodeEvent:59:184` |
| Target (wrong direction) | `DialogueNodeEvent:59:191` |
| Target (wrong direction) | `DialogueNodeEvent:18:226` |
| Target (wrong direction) | `DialogueNodeEvent:18:227` |
| Target (wrong direction) | `DialogueNodeEvent:28:186` |
| Target (wrong direction) | `DialogueNodeEvent:59:186` |
| Target (wrong direction) | `DialogueNodeEvent:18:228` |
| Target (wrong direction) | `DialogueNodeEvent:28:187` |
| Target (wrong direction) | `DialogueNodeEvent:59:187` |
| Target (wrong direction) | `DialogueNodeEvent:18:229` |
| Target (wrong direction) | `DialogueNodeEvent:28:188` |
| Target (wrong direction) | `DialogueNodeEvent:59:188` |
| Target (wrong direction) | `DialogueNodeEvent:18:230` |
| Target (wrong direction) | `DialogueNodeEvent:28:180` |
| Target (wrong direction) | `DialogueNodeEvent:59:180` |
| Target (wrong direction) | `DialogueNodeEvent:18:233` |
| Target (wrong direction) | `DialogueNodeEvent:28:192` |
| Target (wrong direction) | `DialogueNodeEvent:59:192` |
| Target (wrong direction) | `DialogueNodeEvent:18:234` |
| Target (wrong direction) | `DialogueNodeEvent:28:193` |
| Target (wrong direction) | `DialogueNodeEvent:59:193` |
| Target (wrong direction) | `DialogueNodeEvent:18:235` |
| Target (wrong direction) | `DialogueNodeEvent:28:194` |
| Target (wrong direction) | `DialogueNodeEvent:59:194` |
| Target (wrong direction) | `DialogueNodeEvent:18:236` |
| Target (wrong direction) | `DialogueNodeEvent:18:237` |
| Target (wrong direction) | `DialogueNodeEvent:28:190` |
| Target (wrong direction) | `DialogueNodeEvent:59:190` |

---

## Reason Codes

| Code | Short Description | Teacher Guidance |
|------|-------------------|------------------|
| BAD_FEEDBACK | Repeated wrong-direction prompts while searching for Tera/Aryn | Review how to read a topographic map with the student including: 1. How information about elevation can be gained from contour lines. 2. How to use the compass and contour indices to aid navigation. |

---

## Analytics Script

```js
// Unit 2, Point 3 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:22:18"

const playerId = "<playerId>";

const START_KEY = "DialogueNodeEvent:20:33";
const END_KEY   = "DialogueNodeEvent:22:1";

const TARGET_KEYS = [
  "DialogueNodeEvent:18:225", "DialogueNodeEvent:28:185", "DialogueNodeEvent:59:185",
  "DialogueNodeEvent:28:184", "DialogueNodeEvent:28:191", "DialogueNodeEvent:59:184", "DialogueNodeEvent:59:191",
  "DialogueNodeEvent:18:226", "DialogueNodeEvent:18:227", "DialogueNodeEvent:28:186", "DialogueNodeEvent:59:186",
  "DialogueNodeEvent:18:228", "DialogueNodeEvent:28:187", "DialogueNodeEvent:59:187",
  "DialogueNodeEvent:18:229", "DialogueNodeEvent:28:188", "DialogueNodeEvent:59:188",
  "DialogueNodeEvent:18:230", "DialogueNodeEvent:28:180", "DialogueNodeEvent:59:180",
  "DialogueNodeEvent:18:233", "DialogueNodeEvent:28:192", "DialogueNodeEvent:59:192",
  "DialogueNodeEvent:18:234", "DialogueNodeEvent:28:193", "DialogueNodeEvent:59:193",
  "DialogueNodeEvent:18:235", "DialogueNodeEvent:28:194", "DialogueNodeEvent:59:194",
  "DialogueNodeEvent:18:236", "DialogueNodeEvent:18:237", "DialogueNodeEvent:28:190", "DialogueNodeEvent:59:190"
];

// 1) Earliest start by timestamp
const startDoc = db.logdata
  .find({ game: "mhs", playerId: playerId, eventKey: START_KEY, timestamp: { $type: "string" } })
  .sort({ timestamp: 1 }).limit(1).next();

if (startDoc) {
  const startIso = startDoc.timestamp;

  // 2) Earliest end at/after start by timestamp
  const endDoc = db.logdata
    .find({ game: "mhs", playerId: playerId, eventKey: END_KEY, timestamp: { $gte: startIso, $type: "string" } })
    .sort({ timestamp: 1 }).limit(1).next();

  if (endDoc) {
    const endIso = endDoc.timestamp;

    // 3) Count targets in window
    const countTargets = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: TARGET_KEYS },
      timestamp: { $gte: startIso, $lte: endIso }
    });

    countTargets <= 6 ? "green" : "yellow";
  }
}
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 3 — Standalone production grading script
// Trigger eventKey: "DialogueNodeEvent:22:18"

const playerId = "<playerId>";

const TRIGGER_KEY = "DialogueNodeEvent:22:18";
const START_KEY = "DialogueNodeEvent:20:33";

const TARGET_KEYS = [
  "DialogueNodeEvent:18:225", "DialogueNodeEvent:28:185", "DialogueNodeEvent:59:185",
  "DialogueNodeEvent:28:184", "DialogueNodeEvent:28:191", "DialogueNodeEvent:59:184", "DialogueNodeEvent:59:191",
  "DialogueNodeEvent:18:226", "DialogueNodeEvent:18:227", "DialogueNodeEvent:28:186", "DialogueNodeEvent:59:186",
  "DialogueNodeEvent:18:228", "DialogueNodeEvent:28:187", "DialogueNodeEvent:59:187",
  "DialogueNodeEvent:18:229", "DialogueNodeEvent:28:188", "DialogueNodeEvent:59:188",
  "DialogueNodeEvent:18:230", "DialogueNodeEvent:28:180", "DialogueNodeEvent:59:180",
  "DialogueNodeEvent:18:233", "DialogueNodeEvent:28:192", "DialogueNodeEvent:59:192",
  "DialogueNodeEvent:18:234", "DialogueNodeEvent:28:193", "DialogueNodeEvent:59:193",
  "DialogueNodeEvent:18:235", "DialogueNodeEvent:28:194", "DialogueNodeEvent:59:194",
  "DialogueNodeEvent:18:236", "DialogueNodeEvent:18:237", "DialogueNodeEvent:28:190", "DialogueNodeEvent:59:190"
];

// 1) Latest trigger (end anchor) by arrival order
const endDoc = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: TRIGGER_KEY },
  { sort: { _id: -1 } }
);

if (!endDoc || !endDoc.timestamp) {
  "yellow";
} else {
  // 2) Latest start before that end (same attempt) by arrival order
  const startDoc = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: START_KEY,
      _id: { $lte: endDoc._id }
    },
    { sort: { _id: -1 } }
  );

  if (!startDoc || !startDoc.timestamp) {
    "yellow";
  } else {
    const startIso = startDoc.timestamp;
    const endIso = endDoc.timestamp;

    // 3) Count targets within the bounded attempt window
    const countTargets = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: TARGET_KEYS },
      timestamp: { $gte: startIso, $lte: endIso },
      _id: { $gte: startDoc._id, $lte: endDoc._id }
    });

    countTargets <= 6 ? "green" : "yellow";
  }
}
```
