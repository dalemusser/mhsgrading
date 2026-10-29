# MHS Classroom Gameplay Bug Investigation

## Purpose

This folder converts the classroom issue records from `Classroom Issue Tracker 2026.xlsx` into Markdown context files for AI-assisted gameplay-log investigation.

The files are designed to help an analyst reconstruct what happened before a reported gameplay problem, compare affected playthroughs with successful playthroughs, and generate testable hypotheses for QA and development.

## Important interpretation rule

The classroom tracker describes **reported symptoms and context**, not confirmed root causes.

When using these files with gameplay logs:

1. Treat the tracker wording as the starting observation.
2. Do not assume that the activity named in the tracker caused the bug.
3. Distinguish clearly among:
   - **Observed**: directly supported by the tracker or log records.
   - **Inferred**: strongly suggested by the available evidence.
   - **Speculative**: a plausible explanation that still requires verification.
4. Prefer comparisons with students who successfully completed the same activity in the same game collection/build.
5. Look backward far enough in the event sequence to detect an earlier state or transition problem, rather than examining only the final action where the student became stuck.

## Files

- `classroom-issue-tracker.md` — concise index of all issues in the uploaded tracker.
- `issues/QA-1693-u2-classifier.md` — Unit 2 Classifier progression issue.
- `issues/QA-1694-u3-supply-run-crate1.md` — Unit 3 Supply Run / Crate 1 issue following earlier Unit 2 difficulties.
- `issues/QA-1697-u2-argumentation.md` — Unit 2 Argumentation progression issue.
- `issues/U4-saving-cadet-anderson.md` — Unit 4 Saving Cadet Anderson case resolved/worked around by refreshing.

## Source and limitations

Source workbook: `Classroom Issue Tracker 2026.xlsx`, Sheet1, rows 2–5.

The workbook's `Notes` cells for QA 1693, QA 1694, and QA 1697 evaluated as `#VALUE!` when the uploaded workbook was read. Therefore, these Markdown files do **not** attempt to reconstruct or guess any missing note content.

The `Students` field is retained verbatim from the source tracker in the individual issue files so that records can be matched to gameplay logs. If these files will be uploaded to an external AI service, follow your institution's data-handling requirements and anonymize student-identifying information when required.
