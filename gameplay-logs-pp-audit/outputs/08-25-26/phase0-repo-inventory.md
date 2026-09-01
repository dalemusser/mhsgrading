# Phase 0 — Repository Inventory (pre-pipeline inspection)

Date: 2026-08-30. Target build: `08-25-26` (game version `20260819-12237`).

## Inputs located

| Asset | Path | Notes |
|---|---|---|
| Grading logic (production) | `grading-logic/mhs-unit{1-5}-point{Y}-grading.md` | 26 files (U1:4, U2:7, U3:5, U4:6, U5:4). Every file has a `## Production Script` fence, an `## Event Keys` table (`Role | Event Key`), header `Trigger(Start)/Trigger(End)` lines, and (for 22/26) an `### Attempt Window (Production)` block. |
| Assessment intent | `.../MHS-2.0-Embedded-Assessment-Working-Doc.docx` | One table: Checkpoint/Unit/Topic/Task/Dashboard/Student Action/Log Tag/Score formula. Uses `U<u>.C<p>` IDs and `conv-node` dialogue tags. NOTE: file is a OneDrive cloud placeholder — direct read fails with PermissionError; copy first to hydrate. |
| PP specification | `.../Progress-Points.docx` | Per-unit tables: Name/Description/Checkpoint/Color Determination/Progress Log Mark/EA-Color Log Mark/Arg Attempt No. Log Mark. Uses `U<u>.C<p>` IDs. |
| Dialogue map (historical) | `.../Dialogue-ID-Texts.xlsx` | Sheet1, 2575 rows: ConversationID / NodeID / DialogueText (text truncated ~40 chars in some cells — verify). |
| Dialogue DB export (2026-06-10) | `.../2026-06-10-MHSDialogueExport.csv` | Unity Dialogue System export. Sections: Database(0) / Global User Script(3) / Conversations(5) / DialogueEntries(84, header row 85) / OutgoingLinks(2661). DialogueEntries: entrytag, ConvID, ID, Actor, Conversant, Title, MenuText, DialogueText, ... |
| Newest logs | `playthrough-logs-and-results/08-25-26/wenyi082526-1.stratalog.logdata.json` | 6,124 records, single player, all 5 units completed (per coverage manifest + EndOfUnit events). |
| Coverage manifest | `gameplay-logs-test/config/coverage/08-25-26.yaml` | Units 1–5 all `complete`. |
| Prior grading test suite | `tests/` | 26 `test_uXpY.py` modules transcribing each Production Script 1:1 over `mhs_harness.py` (in-memory Mongo-like layer). `run_all.py --log PATH`. Reused for Stage 2 execution. |
| Prior weekly log QA | `gameplay-logs-test/` | Event-level inventory + expectations audit; 08-25-26 report already generated (`reports/08-25-26/`). Cross-referenced, not re-run. |
| Prior known issues | `docs/issues_and_updates.md` | 2026-03-18 doc-vs-Go-grader discrepancies (U4P6 boxId schemes, U3P3 target-key list, etc.). |

## Immediately observed schema facts (verified against raw dumps)

1. **Top-level player field changed**: 05-01-26 dump has `playerId` (`"wenyi050126-1"`); 08-13-26 and 08-25-26 dumps have `user_id` (hex) and **no `playerId`**. Every production script filters `playerId: <id>` — this is a Stage-1 finding affecting all 26 points (at least for exported-log replays; live-DB schema unverifiable from this repo).
2. `eventKey` exists only on DialogueEvent node records (`DialogueNodeEvent:<conv>:<node>`) and questEvent records (`questActiveEvent:<qid>` / `questFinishEvent:<qid>`). 1,192 of 6,124 records have `eventKey` in 08-25.
3. All quest trigger IDs referenced by grading (16,17,18,21,28,34,36,39,41,43,44,45,48,50,54,56) were observed in 08-25 as questActive and/or questFinish keys.
4. 23 eventTypes observed in 08-25 (incl. new `SolarStillDesignEvent`); event-level schema summaries already exist under `gameplay-logs-test/reports/08-25-26/csv/`.
5. Dialogue conversations referenced by grading but **not observed at all** in 08-25 eventKeys: 28, 59, 102, 108 (and others sparsely observed: 68, 70, 74, 84, 90, 100, 106, 107). Reconciliation phase determines which of these are behavioral (player made no errors) vs structural (dialogue flow changed).

## Grading-dependency shape (from `## Event Keys` tables + production fences)

- Roles seen: Trigger, Trigger (Start/End), Trigger / End, Start, End (analytics), Gate (required), Success, Pass (correct choice), Positive, Yellow, Yellow (wrong choice), Negative, Target, Target (wrong direction), Penalty group 1/2, Field, eventType, data.toolName.
- Non-eventKey dependencies: `argumentationToolEvent` + `data.toolName` (U3P3), `soilMachine` + floor/machine/row (U4P3, U4P4), `TerasGardenBox` + actionType/boxId/soilType (U4P6), `WaterChamberEvent` + floor/machineType (U5P2), `Soil Key Puzzle` (U4P1).
- Attempt windows: 22 points use a `(previous-anchor, latest-anchor]` `_id` window; U1P1/U1P2/U1P4 are completion-only; U2P2/U2P3 use lifetime counting (no window block).

## Naming convention map

`U<u>.C<p>` (docs) == `U<u>P<p>` (dashboard/tests) == `mhs-unit<u>-point<p>-grading.md` (grading file). "U<u> Finish" rows in Progress-Points.docx are unit-completion markers, not PPs.

## Ambiguities recorded for the audit outputs

- The dialogue export CSV is dated 2026-06-10; the audited build is 2026-08-19. The export is the *freshest available* dialogue DB but may itself lag the build. Text-level reconciliation treats it as "current-ish" with MEDIUM confidence.
- Expected colors in `tests/run_all.py` / `META["expected"]` belong to the 05-01-26 playthrough round; they are NOT expected values for 08-25-26 (colors depend on player performance). Stage 2 derives expectations from rubric + observed behavior instead.
