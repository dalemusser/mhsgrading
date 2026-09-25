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

- **Start:** Latest `questActiveEvent:41` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `questFinishEvent:56` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the latest-start / latest-end form (yellow whenever the latest `questFinishEvent:56` preceded the latest `questActiveEvent:41`), per the start-and-end window decision (A1). Keys re-verified the same day against the 2026-09-21 dialogue database (conversation 92: two empty structural nodes added, review and feedback nodes unchanged). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `questActiveEvent:41` |
| Trigger (End) | `questFinishEvent:56` |
| Target | TerasGardenBox |
| Target | `DialogueNodeEvent:92:33` |
| Target | `DialogueNodeEvent:92:61` |
| Target | `DialogueNodeEvent:92:62` |
| Target | `DialogueNodeEvent:92:63` |

Notes on conversation 92 ("U4/DesertDelicacies"), re-verified against the 2026-09-21 dialogue database on 2026-09-24:

- `92:33` and `92:36` carry the same text ("I'm all set. Let's see the results."). `92:33` answers Tera's first check (`92:32`, quest entry 9); `92:36` answers her second check (`92:35`, quest entry 10), which the player only reaches by first choosing `92:34` ("Actually, let me move some cameras and I'll come back."; `92:37` repeats that loop). Exactly one of the two fires per attempt, and the feedback round (`92:61` / `92:62` / `92:63`, one per box, then `92:64` once all three cameras are checked) follows it. Playthrough 09-03-26-2 took the second route (moved the second box's camera from Clay to Sand, then `92:36` → 63, 61, 61); `92:33` never fired there, so the scripts' whole-attempt-window fallback counted the round, with the same result as anchoring on `92:36` would give. Adding `92:36` as a second review anchor is agreed in principle (grading-team questions, B list) and waits for a release-build playthrough of that route (imperfect-playthrough checklist, item 11).
- `92:39` ("Excellent performance…", `Cameras_Placed_Correctly >= 2`) and `92:40` ("…soil that did not suit their water needs", `< 2`) are the game's own verdict on the same "at least 2 of 3" rule. In every log they agree with the dashboard colour (39 in the green runs, 40 in the yellow runs). They are not graded, but they are a ready cross-check if the camera records or the feedback nodes ever change.
- `92:66` and `92:67` are new in the 2026-09-21 database: empty structural nodes under the second- and third-seedling prompts (`92:27` / `92:28` and `92:30` / `92:31`), matching `92:65` under the first; the stage directions were also stripped from `92:9`–`92:16` and `92:59`. None of that touches the graded keys.
- The game's Box 0 / 1 / 2 → Gravel / Sand / Clay mapping has held on every build in the logs (05-01 through 09-14), and the feedback nodes agree with it box by box. `TerasGardenBox` records other than `cameraPlaced` log an empty `actionType` since the 20260902 builds (it was `soilSelected` before); the scripts only read `cameraPlaced`, so that is a logging note for the game team, not a grading issue.

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
// Window start: latest questActiveEvent:41 before the end event (exclusive)
// Window end:   latest questFinishEvent:56 (inclusive)

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:41";
const WINDOW_END_KEY = "questFinishEvent:56";

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 } }
);

if (!latestEnd) {
  "yellow";
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    {
      game: "mhs",
      playerId: playerId,
      eventKey: WINDOW_START_KEY,
      _id: { $lt: latestEnd._id }
    },
    { sort: { _id: -1 } }
  );

  const windowStartId = latestStart
    ? latestStart._id
    : ObjectId("000000000000000000000000");
  const windowEndId = latestEnd._id;

  let score = 0;

  // Latest placement for Box 0 within window
  const latestBox0 = db.logdata.findOne(
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

  if (latestBox0 && latestBox0.data && latestBox0.data.soilType === "Gravel") {
    score += 1;
  }

  // Latest placement for Box 1 within window
  const latestBox1 = db.logdata.findOne(
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

  if (latestBox1 && latestBox1.data && latestBox1.data.soilType === "Sand") {
    score += 1;
  }

  // Latest placement for Box 2 within window
  const latestBox2 = db.logdata.findOne(
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

  if (latestBox2 && latestBox2.data && latestBox2.data.soilType === "Clay") {
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
// Window mirrors the production color script: latest questFinishEvent:56 (end),
// latest questActiveEvent:41 before it (start, exclusive; zero ObjectId when none).
// Mirrors the production color rule verbatim: per-box latest cameraPlaced
// (Box 0=Gravel, 1=Sand, 2=Clay) with the dialogue-feedback fallback
// (92:61 count in the latest review round, anchored on 92:33), final score =
// max of both, yellow when < 2. Note: when the player first answers "let me
// move some cameras" (92:34) the results are requested through 92:36 instead
// of 92:33 (seen in 09-03-26-2, where 92:33 never fired); the 92:33-missing
// fallback then counts the whole attempt window, which holds exactly one
// results round, so the count is the same. Adding 92:36 as a second review
// anchor is agreed in principle and waits for a release-build check; this
// script stays mirror-exact until that is applied to the color scripts.

const playerId = "<playerId>";

const WINDOW_START_KEY = "questActiveEvent:41";
const WINDOW_END_KEY = "questFinishEvent:56";

const EXPECTED_SOIL_BY_BOX = { "0": "Gravel", "1": "Sand", "2": "Clay" };
const BOX_LABELS = { "0": "the first box", "1": "the second box", "2": "the third box" };

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  ({ triggered: false, wrong_box_number: 0, wrong_box_summary: "" });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

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
  const feedbackStartId = latestReview ? latestReview._id : windowStartId;

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