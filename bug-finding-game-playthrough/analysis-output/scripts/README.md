# Analysis scripts (first-pass forensic investigation, 2026-10-06)

Read-only Python 3 scripts used to produce the findings in `../`. They never write to `players-logs-met-bugs/`; parsed logs are cached as pickles in `%TEMP%/mhs-bug-forensics-cache` (delete that folder to force a re-parse).

Run from this folder, e.g. `python q25steps.py` or `python q25steps.py meyer2.walton.gronrall`. On Windows set `PYTHONIOENCODING=utf-8` first, because some output contains non-ASCII dialogue text.

| Script | What it shows | Used in |
|---|---|---|
| `mhslog.py` | Shared loader: sorts by client `timestamp`, adds `lagged()` (server arrival > 60 s after client time) and `cn()`/`dlg()`. **Dialogue identity comes from `eventKey`, because `data.conversationId/nodeId` is stale in buffered uploads.** | all |
| `dlgdb.py` | Lookup into the 2026-09-21 Unity Dialogue System export (text, conditions, scripts). | all |
| `milestones.py` | Per-student timeline of sessions, scene changes, quest events, EndOfUnit, DEBUG-menu records and crash records. | mapping, all |
| `lag.py` | `data` vs `eventKey` mismatches and upload-lag statistics per file. | cross-issue (telemetry) |
| `q25steps.py` | "Which Watershed?" (quest 25) milestones per session. | QA-1693, QA-1697 |
| `frozen_q25.py` | Every reload that lands in quest 25: replayed nodes, conversation-21 finish, conversation 8 absent, input count. | QA-1693, QA-1697 |
| `drone.py` | Drone phase (after `23:42`) per launch. | QA-1693, QA-1697 |
| `reloads.py` / `restorecls.py` | Quest state emitted at every reload versus the state before it (regressions). | all |
| `q16steps.py` | Supply Run (quest 16) milestones per Unit-3 session. | QA-1694 |
| `crate1prox.py` | Closest approach to Supply Crate 1 and Interact presses near it, per session. | QA-1694 |
| `u3_blackout.py` | Unit-3 sessions loading with quest 16 active: dialogue events (0 = blackout). | QA-1694 |
| `q36_conv82.py` | Saving Cadet Anderson conversation-82 sequence per player. | U4 |
| `pausedlg.py` / `hungdlg.py` | Pause presses during dialogue; "hung conversation" scan (linked node, no continuation, player active ≥ 60 s). | U4, QA-1693, cross-issue |
| `window.py` | Narrative printer for an index range: `python window.py <student> <start_i> <end_i> [--pos] [--all]`. | ad hoc |

Controls come from `../../../playthrough-logs-and-results/09-14-26-3` and `09-23-26`: two complete internal playthroughs logged under the same `20260914-` version string.
