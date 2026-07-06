# mhsgrading — Context for Claude Code

## What This Repo Does

This repository documents the grading rules and rubrics for the Mission HydroSci (MHS) game/curriculum—a 5-unit game-based Earth science program. Each unit contains multiple progress points, and this repo defines the grading logic for each point: trigger events, scoring rules, reason codes, and instructor messages. The grading implementations are executed by the mhsgrader Go application (in the stratahub repo), and this documentation serves as the authoritative specification for those implementations.

## Technology Stack

- **Language(s):** Markdown documentation
- **Framework(s):** None (pure documentation repo)
- **Database:** References MongoDB logdata collection (used by stratahub/mhsgrader)
- **Deployment:** Source of truth for grading logic; output consumed by mhsgrader (Go) and stratahub Dashboard

## Folder Structure

```
mhsgrading/
├── README.md                              # Overview and unit structure index
├── mhs-unit1-grading.md                   # Unit 1 summary
├── mhs-unit1-point1-grading.md            # Unit 1 Progress Point 1 grading rules
├── mhs-unit1-point2-grading.md            # Unit 1 Progress Point 2 grading rules
├── ... [similar structure for Units 2-5]
├── mhs-unit-start.md                      # Quest start event keys for each unit
├── Reason-codes-and-instructor-messages.md # Centralized reference for reason codes
├── docs/
│   └── issues_and_updates.md              # Critical issues, fixes, and discrepancies
├── LICENSE                                # MIT License
└── .gitignore                             # Standard Go/IDE ignore patterns
```

Each progress point grading file contains:
- **Trigger Events:** Start/end event keys that activate the grading check
- **Grading Rule:** Logic for scoring (green = pass, yellow = needs improvement)
- **Event Keys:** All event types referenced in the grading logic
- **Analytics Script:** JavaScript logic matching the analytics team's model
- **Production Script:** JavaScript implementation for the live game
- **Reason Codes:** When yellow, the specific reason why the student didn't fully succeed (e.g., `WRONG_ARG_SELECTED`, `TOO_MANY_NEGATIVES`, `MISSING_SUCCESS_NODE`)

## Code Patterns & Conventions

- **Naming:** Event keys use `EventType:dialogueNodeId:optionId` format (e.g., `DialogueNodeEvent:31:29`). Progress points use `UnitXPointY` format. Reason codes use UPPER_SNAKE_CASE.
- **Organization:** Files grouped by unit (1-5) and then by progress point within each unit. Unit-level files summarize; point-level files contain detailed grading logic.
- **Script Format:** Both analytics and production scripts are written in JavaScript pseudocode showing step-by-step scoring logic.
- **Reason Codes:** Follow a consistent structure with short code, short description, long description with {placeholder} interpolation, and teacher guidance.

## Key Dependencies & Gotchas

1. **Script-Code Alignment:** The production scripts in the documentation may diverge from the actual Go implementation in mhsgrader. See `docs/issues_and_updates.md` for known discrepancies (e.g., U4P6 Box ID mismatch, U4P4 production script bugs). Always verify critical grading logic against the Go code.

2. **Event Key Accuracy:** Grading depends on exact event keys from the game logdata collection. A single typo (e.g., `DialogueNodeEvent:31:30` instead of `DialogueNodeEvent:31:29`) breaks the grading check. Keys are extracted from game telemetry; cross-check with actual game logs before trusting new keys.

3. **Threshold Sensitivity:** Some reason codes use off-by-one boundaries (e.g., `negCount < 4` vs `negCount <= 4`). The docs at `docs/issues_and_updates.md` note where these were fixed. When updating thresholds, verify both the documentation and the Go code are aligned.

4. **Missing Reason Codes:** Ten progress points (U4P1 through U5P4) historically had placeholder "still figuring out" reason codes. These have been fixed in the code but documentation should be kept in sync. Always cross-check the Go code in stratahub/mhsgrader for the authoritative reason code list.

## How to Run Locally

This is a documentation repository; there is no "run" step. To integrate changes:

1. Update the relevant `.md` file(s) in this repo (e.g., `mhs-unit3-point2-grading.md`)
2. Verify changes against the Go implementation in `/stratahub/internal/app/rules/u{unit}p{point}.go`
3. Run the grader test suite in stratahub to confirm the documentation reflects actual behavior
4. Update the stratahub Dashboard reason code mappings in `stratahub/internal/app/features/mhsdashboard/dashboard.go` if new reason codes are introduced

## Related Repos

- **stratahub** — The main Go web app that runs mhsgrader (in `internal/app/rules/`) to score student work. Dashboard displays grading outcomes and reason codes.
- **mhscurriculum** — Source curriculum documents for MHS units and learning objectives; informs grading rubric design.
- **mhsgrader** — The Go grading engine (part of stratahub) that implements these rules; authoritative for boundary conditions.

## Notes for Claude

1. **Cross-Repo Verification:** When updating grading logic, check both this repo and the Go code in stratahub simultaneously. The Go code is the runtime truth; documentation may lag.

2. **Reason Code Consistency:** Each reason code must be defined in three places: (a) the unit/point grading file, (b) `Reason-codes-and-instructor-messages.md` for reference, and (c) the stratahub Dashboard mappings for display.

3. **Event Key Extraction:** Event keys come from the game's event telemetry. If adding new grading criteria, coordinate with the game team to identify the exact event keys and test with real game logs before finalizing.

4. **Version Control:** The `docs/issues_and_updates.md` file is a living log of discrepancies found during implementation. Update it when discovering mismatches between docs and code, and reference it when making fixes to avoid re-introducing old bugs.

5. **Testing:** Each grading rule should have corresponding unit tests in mhsgrader (`stratahub/internal/app/rules/`). Before committing documentation changes that affect grading thresholds or logic, ensure the test cases cover edge cases (e.g., boundary conditions for attempt counts).
