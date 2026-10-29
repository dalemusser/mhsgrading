# Log sufficiency per student — fall 2026 analysis dataset (129 students)

**Audited:** 2026-10-23.
**Input:** `playthrough-logs-and-results/fall2026-bowling-green-wayne-county/stratalog_BowlingGreen_WayneCounty_fall2026_129users.jsonl` — 1,705,812 records, 129 user_ids. These are the fall students rated A or B in the 10-22 audit, with all their records across builds `20260914-`, `20261005-12466` and `20261016-`.
**Method:** the `build-log-qa` audit run once per student, against the newest internal baseline, [`reports/09-23-26`](../09-23-26/). New in this run is a per-unit view, [`csv/user_unit_summary.csv`](csv/user_unit_summary.csv).

Background on the data-quality issues (late uploads, stale payloads, the delivery envelope, build switching) is in the 10-22 report: [`../fall2026-bowling-green-wayne-county/README.md`](../fall2026-bowling-green-wayne-county/README.md).

---

## Answer

**Every one of the 129 students has logs sufficient for behaviour analysis.**
- There is no FAIL for any student.
- **72 students** are *ready*: analyse as is, after routine cleaning (sort by timestamp, drop resends and exact duplicates).
- **57 students** are *usable with handling*. 51 of them have 1–10% of their records uploaded late on the September build, so for those records keep `timestamp`, `eventType`, `eventKey` and `sceneName` and treat `data` as missing. 5 had a WASM crash, and 1 lost 278 records in transport.
- These per-student results are identical to the 10-22 audit (0 differences across 129 students), as expected for the same records.

"Sufficient" means the logging captured what the student did. It does not mean the student finished the game. Progress varies a lot and is shown per unit below.

## Per unit

Analyses will usually be per unit, and most students changed build partway through a unit, so each student × unit pair is rated on its own records.

Data quality labels, using the same thresholds as the student verdict:
- **ok** — under 1% late uploads in that unit;
- **rule** — 1–10%: apply the late-upload rule;
- **unreliable** — 10% or more: payload-based measures are weak for that unit; event, timing and progress measures are fine.

**All 129 students**

| unit | finished | played, not finished | not reached |
|---|---|---|---|
| 1 | 124 | 5 | 0 |
| 2 | 72 | 57 | 0 |
| 3 | 107 | 17 | 5 |
| 4 | 80 | 38 | 11 |
| 5 | 64 | 23 | 42 |

**Accounts created 2026-09-27 (75 students, mostly on the fixed October builds)**

| unit | finished | played, not finished | not reached |
|---|---|---|---|
| 1 | 74 (73 ok, 1 rule) | 1 | 0 |
| 2 | 69 (43 ok, **26 rule**) | 6 (1 rule) | 0 |
| 3 | 70 ok | 2 | 3 |
| 4 | 57 ok (1 with 278 records lost) | 13 | 5 |
| 5 | 40 ok | 15 | 20 |

**Accounts created 2026-09-11 (54 students, mostly on the September build)**

| unit | finished | played, not finished | not reached |
|---|---|---|---|
| 1 | 50 (46 ok, 2 rule, **2 unreliable**) | 4 (**1 unreliable**) | 0 |
| 2 | 3 (1 ok, 2 rule) | 51 (1 ok, **43 rule, 7 unreliable**) | 0 |
| 3 | 37 (35 ok, 1 rule, **1 unreliable**) | 15 (2 rule) | 2 |
| 4 | 23 (21 ok, 1 rule, **1 unreliable**) | 25 (4 rule) | 6 |
| 5 | 24 (22 ok, 2 rule) | 8 ok | 22 |

**What stands out:**
- **Unit 2 is where late uploads concentrate.** 72 of the 85 student-units that need the late-upload rule are in Unit 2, because both groups played Unit 2 on the September build. In the 09-27 group, Unit 2 is the *only* unit that needs the rule, apart from one Unit 1.
- **Unit 2 was rarely finished in the 09-11 group** (3 of 54), because of the Unit 2 freeze bug. Those students were moved on to Unit 3.
- **Unit 1 is the reliable common baseline:** 124 students finished it, almost all with clean payloads.

**Student-units needing care** (all on build `20260914-`):

| student | unit | issue |
|---|---|---|
| `6aa413b141b41dbac0c7f1ee` | 1 (finished) | 299 of 778 records late (38%) |
| `6aa4144c41b41dbac0c7f26d` | 1 (finished) | 544 of 1,427 late (38%) |
| `6aa4144c41b41dbac0c7f26d` | 4 (finished) | 688 of 3,858 late (18%) |
| `6aa4144c41b41dbac0c7f26f` | 1 (not finished) | 317 of 696 late (46%) |
| `6aa4142c41b41dbac0c7f252` | 3 (finished) | 1,055 of 8,140 late (13%) |
| `6aa413b141b41dbac0c7f1f0`, `…1f8`, `6aa4142c41b41dbac0c7f249`, `…24a`, `…251`, `6aa4144c41b41dbac0c7f262`, `…265` | 2 (not finished) | 11–28% late |

There is also one transport loss: `6ab9a9279a8420a1e6b56b7d`, Unit 4 (finished), 278 records (about 11 minutes) lost on 10-19.

## The export is a snapshot

- The last record is from 2026-10-19 16:57 UTC.
- **09-11 group:** they last played between 10-01 and 10-08, so their data looks final.
- **09-27 group:** 24 students were playing on 10-19 itself and 6 more on 10-18. 36 of their unfinished units (mostly Units 4 and 5) may simply have been in progress. A later export would extend them; re-run this audit on it with the same command.

## Files

| file | contents |
|---|---|
| `csv/user_unit_summary.csv` | **new:** one row per student × unit (129 × 5). Columns: status, data_quality label, records, active days and minutes, builds, % on the October delivery envelope, quests finished, late-upload (stale-payload) records and %, records lost in transport |
| `csv/user_summary.csv` | one row per student: verdict and reasons, progress, delay and stale-payload counts, transport loss, duplicates, crashes, finding counts vs the baseline |
| `cohort-report.md` | generated tables: verdicts, builds, finding prevalence vs baseline, per-student table, per-unit readiness, method |
| `users/<user_id>/audit-report.md` | the full standard audit for one student |
| `csv/finding_prevalence.csv`, `csv/build_summary.csv`, `csv/transport_sessions.csv` | the same roll-ups as the 10-22 audit, restricted to these students |

To re-run (about 30 s), from the repository root:

```bash
python build-log-qa/scripts/audit_per_user.py \
    --input playthrough-logs-and-results/fall2026-bowling-green-wayne-county/stratalog_BowlingGreen_WayneCounty_fall2026_129users.jsonl \
    --build-id fall2026-bowling-green-wayne-county-129users \
    --baseline build-log-qa/reports/09-23-26
```
