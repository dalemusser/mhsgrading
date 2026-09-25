# Unit 5 Point 2 Grading

**Activity:** If I Had a Nickel- Floors 3 & 4

**Trigger(Start) Event:** `questFinishEvent:43`
**Trigger(End) Event:** `DialogueNodeEvent:96:1`

---

## Grading Rule

This is a score-based progress point. The score starts at 0. On the third floor, count the player's interactions with the condenser and evaporator panels — the four single-chamber machines and the dual-chamber machine, i.e. `WaterChamberEvent` records whose `data.machineType` is `Condenser`, `Evaporator`, `DualChamber_Condenser` or `DualChamber_Evaporator`, each On/Off toggle being one interaction: 6 or fewer adds 2, 7 to 10 adds 1, 11 or more adds 0. On the fourth floor, count the same interactions: 5 or fewer adds 2, 6 to 9 adds 1, 10 or more adds 0. A score of 3 or more is green; less than 3 is yellow. The vent switches (`VentSwitch`) and the floor-1 / floor-2 chamber events that fall inside the window are not counted. The two dual-chamber types were added on 2026-09-24 (grading-team review item approved 2026-09-21); until then only `Condenser` and `Evaporator` were counted.

| Outcome | Condition |
|---------|-----------|
| **Green** | score >= 3 |
| **Yellow** | score < 3 |

### Attempt Window (Production)

- **Start:** Latest `questFinishEvent:43` before the end event (exclusive; zero ObjectId when there is none)
- **End:** Latest `DialogueNodeEvent:96:1` (inclusive)
- The Production Script below bounds the window this way: it anchors on the latest end event and takes the latest start event before it, so a completed attempt keeps its grade if the student re-enters the activity afterwards. The Trigger(Start) event in the header is that same start event; it also drives the dashboard's in-progress state and the duration metrics.
- Changed 2026-09-24 from the latest-start / latest-end form (yellow whenever the latest `DialogueNodeEvent:96:1` preceded the latest `questFinishEvent:43`), per the start-and-end window decision (A1). The end key was re-verified the same day against the 2026-09-21 dialogue database (conversation 96 unchanged). Both Python transcriptions follow; the Go rule must be updated in step.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger (Start) | `questFinishEvent:43` |
| Trigger (End) | `DialogueNodeEvent:96:1` |
| Target | `eventType: "WaterChamberEvent"` with `data.floor` `"3"` or `"4"` and `data.machineType` in `Condenser`, `Evaporator`, `DualChamber_Condenser`, `DualChamber_Evaporator` (one record per On/Off toggle; `VentSwitch` records and other floors are not counted) |

Notes (re-verified 2026-09-24):

- The end anchor `96:1` (Aryn: "What a week. Stuck on this island without a teleporter…", conversation 96 "U5/PostDungeon") is unchanged and unique in the 2026-09-21 dialogue database; conversation 96 is identical to the 2026-06-10 export. It fires once per playthrough (twice, 13 s apart, in the non-fixture log 08-13-26; the latest is taken). The start anchor `questFinishEvent:43` is U5P1's end and fires once.
- Quest sequence inside the window: `questActiveEvent:51` (with the start) → `questFinishEvent:51` / `questActiveEvent:52` (floor 3) → `questFinishEvent:52` / `questActiveEvent:53` (floor 4) → `96:1`. The floor-2 chamber events fall inside the window, before quest 51 finishes, and are excluded by the floor filter.
- Dual-chamber machine: floor 3 has four single-chamber machines and one dual-chamber machine whose two switches log as `DualChamber_Condenser` / `DualChamber_Evaporator`. The rubric's "minimum of 5 panel interactions" on floor 3 is 4 single + 1 dual, so the rubric always assumed the dual chamber counts; the scripts count it since 2026-09-24. Effect on the logs: fixtures 08-31-26 4 → 5 (green unchanged), 09-03-26-3 8 → 24 and 09-14-26-3 8 → 21 (yellow unchanged, score 1 → 0); the older log 05-01-26 moves 4 → 7 (two extra dual-chamber toggles) and its colour from green to yellow, which is what the rubric intends.
- Known weakness (not changed): a floor with zero counted interactions scores +2, whereas the rubric gives 0 for a floor that was not completed. It has only been observed in 09-03-26-2, where the tester skipped floor 3 with the debug menu (quests 51 and 52 finished in the same second while the menu was open), so that fixture's U5P2 green rests on the skip. A student cannot reach `96:1` without playing floor 3, so this only matters for QA runs or lost logging; if the team wants it closed, require at least the rubric minimum (5 on floor 3, 4 on floor 4) before a floor earns any points.

---

## Analytics Script

```js
// Unit 5, Point 2 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:96:1"

let score = 0;

const playerId = "<playerId>";
// Single-chamber and dual-chamber condenser/evaporator panels (DualChamber_* added 2026-09-24)
const VALID_TYPES = ["Condenser", "Evaporator", "DualChamber_Condenser", "DualChamber_Evaporator"];

// Count relevant interactions on Floor 3
const floor3_attempts = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "WaterChamberEvent",
  "data.floor": "3",
  "data.machineType": { $in: VALID_TYPES }
});

// Count relevant interactions on Floor 4
const floor4_attempts = db.logdata.countDocuments({
  playerId: playerId,
  eventType: "WaterChamberEvent",
  "data.floor": "4",
  "data.machineType": { $in: VALID_TYPES }
});

// Scoring for Floor 3
if (floor3_attempts <= 6) {
  score += 2;
} else if (floor3_attempts < 11) {
  score += 1;
}

// Scoring for Floor 4
if (floor4_attempts <= 5) {
  score += 2;
} else if (floor4_attempts < 10) {
  score += 1;
}

color = (score < 3) ? "yellow" : "green";

color;
```

## Production Script (Attempt-Based)

```js
// Production — replay-safe score calculation for Unit 5 water chamber puzzle
// Window start: latest questFinishEvent:43 before the end event (exclusive)
// Window end:   latest DialogueNodeEvent:96:1 (inclusive)

const playerId = "<playerId>";

const WINDOW_START_KEY = "questFinishEvent:43";
const WINDOW_END_KEY = "DialogueNodeEvent:96:1";
// Single-chamber and dual-chamber condenser/evaporator panels (DualChamber_* added 2026-09-24)
const VALID_TYPES = ["Condenser", "Evaporator", "DualChamber_Condenser", "DualChamber_Evaporator"];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  {
    game: "mhs",
    playerId: playerId,
    eventKey: WINDOW_END_KEY
  },
  { sort: { _id: -1 }, projection: { _id: 1 } }
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
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );

  const windowStartId = latestStart
    ? latestStart._id
    : ObjectId("000000000000000000000000");
  const windowEndId = latestEnd._id;

  let score = 0;

  // Count relevant interactions on Floor 3
  const floor3_attempts = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "WaterChamberEvent",
    "data.floor": "3",
    "data.machineType": { $in: VALID_TYPES },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // Count relevant interactions on Floor 4
  const floor4_attempts = db.logdata.countDocuments({
    game: "mhs",
    playerId: playerId,
    eventType: "WaterChamberEvent",
    "data.floor": "4",
    "data.machineType": { $in: VALID_TYPES },
    _id: { $gt: windowStartId, $lte: windowEndId }
  });

  // Scoring for Floor 3
  if (floor3_attempts <= 6) {
    score += 2;
  } else if (floor3_attempts < 11) {
    score += 1;
  }

  // Scoring for Floor 4
  if (floor4_attempts <= 5) {
    score += 2;
  } else if (floor4_attempts < 10) {
    score += 1;
  }

  score < 3 ? "yellow" : "green";
}
```

---

## Reason Codes

### SCORE_BELOW_THRESHOLD

**Instructor Message:** In If I Had a Nickel (floors 3 and 4), the student used {floor3_attempts} condenser and evaporator interactions to solve the third-floor water chamber puzzle and {floor4_attempts} on the fourth floor. This point earns green only when at least one floor is solved within its optimal count (6 interactions on the third floor, 5 on the fourth) and the other stays within its partial range (at most 10 and 9, respectively). Many interactions may indicate trial-and-error switching rather than predicting the phase change each chamber needs: condensation removes energy to turn water vapor into liquid, and evaporation adds energy to turn liquid back into vapor.

#### Corresponding Script

```js
// U5P2: SCORE_BELOW_THRESHOLD — determine trigger and per-floor counts
// Window mirrors the production color script: latest DialogueNodeEvent:96:1 (end),
// latest questFinishEvent:43 before it (start, exclusive; zero ObjectId when none).
// Score: floor3 <=6 -> +2, 7-10 -> +1; floor4 <=5 -> +2, 6-9 -> +1; yellow when
// total < 3. VALID_TYPES is mirror-exact with the color script and, since
// 2026-09-24, includes the floor-3 dual-chamber machine (DualChamber_Condenser /
// DualChamber_Evaporator). VentSwitch and the floors-1/2 events inside this
// window are excluded by design.

const playerId = "<playerId>";

const WINDOW_START_KEY = "questFinishEvent:43";
const WINDOW_END_KEY = "DialogueNodeEvent:96:1";
const VALID_TYPES = ["Condenser", "Evaporator", "DualChamber_Condenser", "DualChamber_Evaporator"];

// 1) Latest end anchor
const latestEnd = db.logdata.findOne(
  { game: "mhs", playerId: playerId, eventKey: WINDOW_END_KEY },
  { sort: { _id: -1 }, projection: { _id: 1 } }
);

if (!latestEnd) {
  ({ triggered: false, floor3_attempts: 0, floor4_attempts: 0 });
} else {
  // 2) Latest start anchor before the latest end
  const latestStart = db.logdata.findOne(
    { game: "mhs", playerId: playerId, eventKey: WINDOW_START_KEY, _id: { $lt: latestEnd._id } },
    { sort: { _id: -1 }, projection: { _id: 1 } }
  );
  const windowStartId = latestStart ? latestStart._id : ObjectId("000000000000000000000000");
  const windowFilter = { _id: { $gt: windowStartId, $lte: latestEnd._id } };

  const floorCount = (floor) => db.logdata.countDocuments({
    game: "mhs", playerId: playerId,
    eventType: "WaterChamberEvent",
    "data.floor": floor,
    "data.machineType": { $in: VALID_TYPES },
    ...windowFilter
  });

  const floor3 = floorCount("3");
  const floor4 = floorCount("4");

  // Mirror the color formula exactly
  let score = 0;
  if (floor3 <= 6) score += 2;
  else if (floor3 < 11) score += 1;
  if (floor4 <= 5) score += 2;
  else if (floor4 < 10) score += 1;

  ({ triggered: score < 3, floor3_attempts: floor3, floor4_attempts: floor4 });
}
```

### Teacher Guidance 
Remind students that condensation is the phase change that occurs when energy is removed from a gas to turn it into a liquid. Have students work through Unit 5 followup activity.