# Classroom Bug Forensics — First-Pass Analysis Outputs

Produced 2026-10-06 following `prompts/gameplay-log-forensic-analysis-1.md`, from the ten affected-student logs in `../players-logs-met-bugs/` and the issue files in `../issue-tracker/`. The source logs were only read, never modified.

## Read in this order

1. **`cross-issue-summary.md`** — the one-page picture:
   - how the four tickets map onto two failure mechanisms;
   - the student outcome matrix;
   - telemetry caveats;
   - top reproduction experiments, code areas and telemetry asks.
2. **`student-log-mapping.md`** — which log belongs to which student, with confidence and the two filename typos (`read` → Reed, `gronrall` → Gronvall).
3. Per-issue reports (each follows the protocol's section list: Executive Finding → … → Confidence and Limitations):
   - `QA-1693-analysis.md` — Unit 2 Classifier.
   - `QA-1697-analysis.md` — Unit 2 "Argumentation" (largely the same defect as QA 1693).
   - `QA-1694-analysis.md` — Unit 3 Supply Run / Crate 1 (with the Hypothesis A vs B evaluation).
   - `U4-saving-cadet-anderson-analysis.md` — Unit 4 refresh case.
4. `scripts/` — the read-only Python used for every number in the reports (see `scripts/README.md`).

## Conventions

- **Evidence labels:** **[O]** observed directly in the logs · **[I]** inferred from the sequence and/or the dialogue-database export · **[S]** speculative.
- **Times:** client `timestamp` in UTC (2026). Sessions are split at `gameStartEvent`.
- **Node notation:** `conversation:node`, e.g. `21:51`. Node text, conditions and links come from `grading-logic/original-score-rubric-table-and-dialogue-database/2026-09-21-MHSDialogueExport.csv`.
- **Dialogue identity is taken from `eventKey`, not from `data.conversationId/nodeId`.** In offline-buffered uploads the `data` payload is stale. Details are in the cross-issue summary, under telemetry integrity.
- **Controls:**
  - Ella Preble (same build, completed Units 2–3);
  - the five Goodhue students (skipped from Unit 2 but not affected by QA 1694);
  - internal playthroughs `playthrough-logs-and-results/09-14-26-3` and `09-23-26` (same `20260914-` build string).

## Follow-ups that need people, not logs

- Re-export **Ella Preble's** records after 2026-10-05 18:51 UTC. The refresh the tracker mentions is not in this export.
- Confirm with Dale Musser's team / QA whether MHS-Release_V1.0.0 was re-deployed between 2026-09-24 and 2026-10-05, since the build string is truncated.
- Ask the Goodhue teacher what was on screen when students were "stuck at Argumentation". The analysis predicts DANI's retraining dialogue with the "Error: Argumentation Points Cannot Be Classified" alert.
