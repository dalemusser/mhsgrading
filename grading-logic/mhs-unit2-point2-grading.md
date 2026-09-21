# Unit 2 Point 2 Grading

**Activity:** Foraged Forging

**Trigger(Start) Event:** `questFinishEvent:21`
**Trigger(End) Event:** `DialogueNodeEvent:20:26`

---

## Grading Rule

Windowed rule using client timestamps. Count wrong-direction prompts between the start and end of the activity. The student should trigger at most 1 wrong-direction dialogue.

| Outcome | Condition |
|---------|-----------|
| **Green** | Target count <= 1 within the activity window |
| **Yellow** | Target count > 1, or start/end events missing |

### Activity Window

- **Start Key:** `questFinishEvent:21`
- **End Key:** `DialogueNodeEvent:20:26` (trigger)

### Attempt Window (Production)

Uses the latest end trigger and the most recent start key before it, fenced by `_id` range.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger / End | `DialogueNodeEvent:20:26` |
| Start | `questFinishEvent:21` |
| Target (wrong direction) | `DialogueNodeEvent:28:179` |
| Target (wrong direction) | `DialogueNodeEvent:59:179` |
| Target (wrong direction) | `DialogueNodeEvent:28:182` |
| Target (wrong direction) | `DialogueNodeEvent:59:182` |
| Target (wrong direction) | `DialogueNodeEvent:28:183` |
| Target (wrong direction) | `DialogueNodeEvent:59:183` |

---

## Analytics Script

```js
// Unit 2, Point 2 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:20:26"

const playerId = "<playerId>";

const START_KEY = "questFinishEvent:21";
const END_KEY = "DialogueNodeEvent:20:26";

const TARGET_KEYS = [
  "DialogueNodeEvent:28:179",
  "DialogueNodeEvent:59:179",
  "DialogueNodeEvent:28:182",
  "DialogueNodeEvent:59:182",
  "DialogueNodeEvent:28:183",
  "DialogueNodeEvent:59:183"
];

// 1) Earliest start by timestamp
const startDoc = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: START_KEY },
  { sort: { timestamp: 1 } }
);

if (!startDoc || !startDoc.timestamp) {
  "yellow";
} else {
  const startIso = startDoc.timestamp;

  // 2) Earliest end after start by timestamp
  const endDoc = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: END_KEY,
      timestamp: { $gte: startIso }
    },
    { sort: { timestamp: 1 } }
  );

  if (!endDoc || !endDoc.timestamp) {
    "yellow";
  } else {
    const endIso = endDoc.timestamp;

    // 3) Count targets in [startIso, endIso]
    const countTargets = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: TARGET_KEYS },
      timestamp: { $gte: startIso, $lte: endIso }
    });

    countTargets <= 1 ? "green" : "yellow";
  }
}
```

## Production Script (Attempt-Based)

```js
// Unit 2, Point 2 — Attempt-based standalone production grading script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:20:26"

const playerId = "<playerId>";

const END_KEY = "DialogueNodeEvent:20:26";     // trigger
const START_KEY = "questFinishEvent:21";

const TARGET_KEYS = [
  "DialogueNodeEvent:28:179",
  "DialogueNodeEvent:59:179",
  "DialogueNodeEvent:28:182",
  "DialogueNodeEvent:59:182",
  "DialogueNodeEvent:28:183",
  "DialogueNodeEvent:59:183"
];

// 1) Latest end trigger by arrival order
const endDoc = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!endDoc || !endDoc.timestamp) {
  "yellow";
} else {
  const endIso = endDoc.timestamp;

  // 2) Latest start before this end (same attempt) by arrival order
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

    // 3) Count targets within [startIso, endIso] fenced by _id window
    const countTargets = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: TARGET_KEYS },
      timestamp: { $gte: startIso, $lte: endIso },
      _id: { $gte: startDoc._id, $lte: endDoc._id }
    });

    countTargets <= 1 ? "green" : "yellow";
  }
}
```

---

## Reason Codes

### EXCESS_NAV_REMINDERS

**Instructor Message:** In Foraged Forging, while navigating to find Captain Toppo, the student triggered {triggering_number} adaptive reminders, dialogues that fire when the player travels somewhere inconsistent with Anderson's clues or has not been consulting the map. This point earns green only when at most 1 such reminder fires during the search. Repeated reminders may indicate difficulty translating the clues about direction, elevation, and terrain features into a location on the topographic map using contour lines and the compass.

#### Correspoinding Script

```js
// U2P2: EXCESS_NAV_REMINDERS — determine trigger and triggering_number
// Window mirrors the production color script exactly: latest end trigger
// (DialogueNodeEvent:20:26), then the latest start (questFinishEvent:21)
// at or before it, fenced by both timestamp and _id.
// triggering_number = adaptive navigation reminders fired during the search.

const playerId = "<playerId>";

const END_KEY = "DialogueNodeEvent:20:26";     // trigger
const START_KEY = "questFinishEvent:21";

const BAD_FEEDBACK_KEYS = [
  "DialogueNodeEvent:28:179",  // clue reminder: near original location, rock formations
  "DialogueNodeEvent:59:179",
  "DialogueNodeEvent:28:182",  // map-usage reminder: open the map with M
  "DialogueNodeEvent:59:182",
  "DialogueNodeEvent:28:183",  // clue reminder: hill at ~90 feet elevation
  "DialogueNodeEvent:59:183"
];

// 1) Latest end trigger by arrival order
const endDoc = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: END_KEY },
  { sort: { _id: -1 } }
);

if (!endDoc || !endDoc.timestamp) {
  ({ triggered: false, triggering_number: 0 });
} else {
  // 2) Latest start at or before this end (same attempt)
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
    ({ triggered: false, triggering_number: 0 });
  } else {
    // 3) Count reminders within the window, fenced by timestamp and _id
    const count = db.logdata.countDocuments({
      game: "mhs",
      playerId: playerId,
      eventKey: { $in: BAD_FEEDBACK_KEYS },
      timestamp: { $gte: startDoc.timestamp, $lte: endDoc.timestamp },
      _id: { $gte: startDoc._id, $lte: endDoc._id }
    });

    // 4) Green allows at most 1 reminder; more than 1 triggers the reason code
    ({ triggered: count > 1, triggering_number: count });
  }
}
```

### Teacher Guidance
1. How information about elevation can be gained from contour lines.
2. How to use the compass and contour indices to aid navigation.