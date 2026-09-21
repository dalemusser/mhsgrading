# Unit 4 Point 6 Grading

**Activity:** Desert Delicacies

**Trigger(Start) Event:** `questActiveEvent:41`
**Trigger(End) Event:** `questFinishEvent:56`

---

## Grading Rule

This is a score-based progress point. There are three garden boxes, each time when the player places the camera on the correct soil type then the score will add one. In box 0, if the latest camera placement is gravel, then the score adds one; in box 1, if the latest camera placement is sand, then the score adds another one; in box 2, if the latest camera placement is clay, then the score further adds one. If the score is equal to or larger than 2, then the color turns to green; otherwise the color returns yellow.

**Dialogue-feedback fallback (OR logic):** the box-id → soil-type mapping above is the primary check, but box ids have shifted between builds before, so the score is additionally secured by Dani's review feedback dialogues. When the player asks for the results (`DialogueNodeEvent:92:33`, "I'm all set. Let's see the results."), each garden box produces exactly one feedback dialogue: `DialogueNodeEvent:92:61` ("You chose the best soil for this plant") when the soil is correct, or `DialogueNodeEvent:92:62` ("Too Little") / `DialogueNodeEvent:92:63` ("Too Much") when it is wrong. A box therefore gains its point only when it shows `92:61` and not `92:62`/`92:63`, so the count of `92:61` events in the latest review round equals the number of correctly filled boxes — with no dependence on box ids. The final score is the **maximum** of the box-id score and this dialogue score (per box: the point is gained if either method shows it correct), so the grading survives a box-id change as long as the feedback dialogue still fires. Caveat: the feedback nodes carry no box id, so a re-inspected plant could in principle re-fire its feedback; anchoring the count to the latest `92:33` and capping it at 3 keeps this secondary evidence conservative.

| Outcome | Condition |
|---------|-----------|
| **Green** | The score >= 2 |
| **Yellow** | The score < 2 |

### Attempt Window (Production)

- **Start:** Latest `questActiveEvent:41` (exclusive; the window is valid only when the end event comes after it)
- **End:** Latest `questFinishEvent:56` (inclusive)
- The Production Script below bounds the window this way. The Trigger(Start) event in the header marks when the activity begins and drives the dashboard's in-progress state and the duration metrics.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `questFinishEvent:56` |
| Target | TerasGardenBox |
| Target | `DialogueNodeEvent:92:33` |
| Target | `DialogueNodeEvent:92:61` |
| Target | `DialogueNodeEvent:92:62` |
| Target | `DialogueNodeEvent:92:63` |

---

## Analytics Script

```js
// Unit 4, Point 6 — Analytics-matching script
// Trigger eventKey: "questFinishEvent:56"

const playerId = "<playerId>";

let score = 0;

// Latest placement for Box 0
const latestBox0 = db.logdata.findOne(
  {
    playerId: playerId,
    eventType: "TerasGardenBox",
    "data.actionType": "cameraPlaced",
    "data.boxId": "0"
  },
  {
    sort: { _id: -1 }
  }
);

if (latestBox0 && latestBox0.data && latestBox0.data.soilType === "Gravel") {
  score += 1;
}

// Latest placement for Box 1
const latestBox1 = db.logdata.findOne(
  {
    playerId: playerId,
    eventType: "TerasGardenBox",
    "data.actionType": "cameraPlaced",
    "data.boxId": "1"
  },
  {
    sort: { _id: -1 }
  }
);

if (latestBox1 && latestBox1.data && latestBox1.data.soilType === "Sand") {
  score += 1;
}

// Latest placement for Box 2
const latestBox2 = db.logdata.findOne(
  {
    playerId: playerId,
    eventType: "TerasGardenBox",
    "data.actionType": "cameraPlaced",
    "data.boxId": "2"
  },
  {
    sort: { _id: -1 }
  }
);

if (latestBox2 && latestBox2.data && latestBox2.data.soilType === "Clay") {
  score += 1;
}

// Dialogue-feedback fallback (box-id independent): in each results review,
// one feedback node fires per garden box — 92:61 = correct soil,
// 92:62 ("Too Little") / 92:63 ("Too Much") = wrong soil.
// Count 92:61 in the latest review round (after the latest 92:33).
const REVIEW_START_KEY = "DialogueNodeEvent:92:33";
const CORRECT_FEEDBACK_KEY = "DialogueNodeEvent:92:61";

const latestReview = db.logdata.findOne(
  {
    playerId: playerId,
    eventKey: REVIEW_START_KEY
  },
  {
    sort: { _id: -1 },
    projection: { _id: 1 }
  }
);

const feedbackFilter = {
  playerId: playerId,
  eventKey: CORRECT_FEEDBACK_KEY
};

if (latestReview) {
  feedbackFilter._id = { $gt: latestReview._id };
}

const dialogueScore = Math.min(3, db.logdata.countDocuments(feedbackFilter));

// OR logic: a box counts if either the box-id check or the feedback dialogue
// shows it correct — take the better of the two scores.
const finalScore = Math.max(score, dialogueScore);

const color = (finalScore >= 2) ? "green" : "yellow";

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe TerasGardenBox scoring
// Window start: "questActiveEvent:41"
// Window end:   "questFinishEvent:56"

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:41";
const WINDOW_END_KEY = "questFinishEvent:56";

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

  let score = 0;

  // Latest placement for Box 1 within window
  const latestBox1 = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "TerasGardenBox",
      "data.actionType": "cameraPlaced",
      "data.boxId": "0",
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    {
      sort: { _id: -1 }
    }
  );

  if (latestBox1 && latestBox1.data && latestBox1.data.soilType === "Gravel") {
    score += 1;
  }

  // Latest placement for Box 1 within window
  const latestBox2 = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "TerasGardenBox",
      "data.actionType": "cameraPlaced",
      "data.boxId": "1",
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    {
      sort: { _id: -1 }
    }
  );

  if (latestBox2 && latestBox2.data && latestBox2.data.soilType === "Sand") {
    score += 1;
  }

  // Latest placement for Box 2 within window
  const latestBox3 = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventType: "TerasGardenBox",
      "data.actionType": "cameraPlaced",
      "data.boxId": "2",
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    {
      sort: { _id: -1 }
    }
  );

  if (latestBox3 && latestBox3.data && latestBox3.data.soilType === "Clay") {
    score += 1;
  }

  // Dialogue-feedback fallback (box-id independent): in each results review,
  // one feedback node fires per garden box — 92:61 = correct soil,
  // 92:62 ("Too Little") / 92:63 ("Too Much") = wrong soil.
  const REVIEW_START_KEY = "DialogueNodeEvent:92:33";
  const CORRECT_FEEDBACK_KEY = "DialogueNodeEvent:92:61";

  const latestReview = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: REVIEW_START_KEY,
      _id: { $gt: windowStartId, $lte: windowEndId }
    },
    {
      sort: { _id: -1 },
      projection: { _id: 1 }
    }
  );

  // Count 92:61 in the latest review round; if the review-start node is
  // missing from the logs, fall back to the whole attempt window.
  const feedbackStartId = latestReview ? latestReview._id : windowStartId;

  const dialogueScore = Math.min(3, db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventKey: CORRECT_FEEDBACK_KEY,
    _id: { $gt: feedbackStartId, $lte: windowEndId }
  }));

  // OR logic: a box counts if either the box-id check or the feedback dialogue
  // shows it correct — take the better of the two scores.
  const finalScore = Math.max(score, dialogueScore);

  finalScore >= 2 ? "green" : "yellow";
}
```

---

## Reason Codes

### WRONG_SOIL_SELECTED

**Instructor Message:** In Desert Delicacies, the student placed recording cameras on the soil they predicted would grow each seedling best, but chose a soil that does not match the seedling's water needs in {wrong_box_summary}. This point earns green only when at least 2 of the 3 garden boxes have the correct soil. Wrong choices may indicate difficulty connecting soil particle size to water retention: coarse soils like gravel let water drain past the roots, while fine-particle soils like clay trap too much of it, so each seedling needs the soil whose drainage matches its water requirement.

#### Corresponding Script
```js
// U4P6: WRONG_SOIL_SELECTED — determine trigger and wrong-box summary
// Mirrors the production color rule verbatim: per-box latest cameraPlaced
// (Box 0=Gravel, 1=Sand, 2=Clay) with the dialogue-feedback fallback
// (92:61 count in the latest review round, anchored on 92:33), final score =
// max of both, yellow when < 2. Note: the review can also start at 92:36
// (second-round "see the results") — flagged as a color-script improvement;
// this script stays mirror-exact until that is applied to the color scripts.

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:41";
const WINDOW_END_KEY = "questFinishEvent:56";

const EXPECTED_SOIL_BY_BOX = { "0": "Gravel", "1": "Sand", "2": "Clay" };
const BOX_LABELS = { "0": "the first box", "1": "the second box", "2": "the third box" };

const latestStart = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestStart || !latestEnd || latestEnd._id < latestStart._id) {
  ({ triggered: false, wrong_box_number: 0, wrong_box_summary: "" });
} else {
  const windowFilter = { _id: { $gt: latestStart._id, $lte: latestEnd._id } };

  let boxScore = 0;
  const wrongParts = [];

  Object.keys(EXPECTED_SOIL_BY_BOX).forEach(function (boxId) {
    const expected = EXPECTED_SOIL_BY_BOX[boxId];
    const latestPlacement = db.logdata.findOne(
      {
        game: "mhs", playerId: playerId,
        eventType: "TerasGardenBox",
        "data.actionType": "cameraPlaced",
        "data.boxId": boxId,
        ...windowFilter
      },
      { sort: { _id: -1 }, projection: { "data.soilType": 1 } }
    );

    const actual = latestPlacement && latestPlacement.data
      ? latestPlacement.data.soilType : null;

    if (actual === expected) {
      boxScore += 1;
    } else if (actual) {
      wrongParts.push(BOX_LABELS[boxId] + " (chose " + actual + ", needs " + expected + ")");
    } else {
      wrongParts.push(BOX_LABELS[boxId] + " (no camera placement recorded, needs " + expected + ")");
    }
  });

  // Dialogue-feedback fallback, mirror of the color script
  const latestReview = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: "DialogueNodeEvent:92:33", ...windowFilter },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );
  const feedbackStartId = latestReview ? latestReview._id : latestStart._id;

  const dialogueScore = Math.min(3, db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventKey: "DialogueNodeEvent:92:61",
    _id: { $gt: feedbackStartId, $lte: latestEnd._id }
  }));

  const finalScore = Math.max(boxScore, dialogueScore);

  ({
    triggered: finalScore < 2,
    wrong_box_number: wrongParts.length,
    wrong_box_summary: wrongParts.join(" and ")
  });
}
```

### Teacher Guidance
Remind students that water moves through different soils at different rates. Water will move fastest through sand, and slowest through clay. Water moves through sand at a slower rate than gravel and a faster rate than clay.