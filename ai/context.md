# mhsgrading — Context for Claude Code

## What This Repo Does

Documents and validates the grading rules for Mission HydroSci (MHS), a
five-unit game-based Earth science program with 26 progress points. For each
point it defines the events that start and end the activity, the colour rule
(green/yellow) and the reason codes shown to teachers when a point is yellow,
each with an Instructor Message template and a script that computes the
message's variables. The Go grader (`mhsgrader`, its own repository) transcribes
these documents; the StrataHub MHS Dashboard renders the messages.

## Technology Stack

- Markdown specifications (`grading-logic/`)
- Python 3.10+ validation pipelines (`pip install -r requirements.txt`; only `pyyaml`)
- Gameplay log dumps (MongoDB extended JSON) as fixtures

## Folder Structure

```
mhsgrading/
├── README.md                      # Index and the four log-analysis features
├── grading-logic/                 # THE SPEC: mhs-unitN-pointM-grading.md per point (26),
│   │                              #   unit summaries, mhs-unit-start.md,
│   │                              #   Reason-codes-and-instructor-messages.md (generated index)
│   └── original-score-rubric-table-and-dialogue-database/  # EA working doc, Progress-Points, dialogue exports
├── rubric-validation/             # test_uXpY.py = Production Script transcriptions; config/fixtures.yaml
├── reason-code-validation/        # rc_uXpY.py = Corresponding Script transcriptions; config/expectations.yaml
├── grading-readiness-audit/       # Does a new build's logging still support each rule?
├── build-log-qa/                  # Event-level logging QA per weekly build
├── playthrough-logs-and-results/  # Log dumps by build (the fixtures) + log-format investigations
├── feedback-message-for-each-pp/  # Context for teacher-facing feedback (rubric, goals, strategies, dialogue)
├── prompts/                       # Task prompts that produced the major work products
└── docs/                          # issues_and_updates.md, grading-team-questions-2026-09.md,
                                   #   grading-doc-changes-2026-09-21.md
```

Each point document has: header (Activity, Trigger(Start), Trigger(End)),
Grading Rule table, "Attempt Window (Production)" block, Event Keys table,
Analytics Script (historical), **Production Script (Attempt-Based)** (the colour),
and **Reason Codes**: one `### CODE` per code with `**Instructor Message:**`
(template with `{placeholders}`), a "Corresponding Script" returning
`{triggered, <variables>}`, and a "Teacher Guidance" section.

## Conventions

- Event keys: `EventType:conversation:node` (e.g. `DialogueNodeEvent:68:29`),
  or an eventType + data match where the game logs no key (the Unit 4 soil-key
  puzzle close).
- Windows are `_id`-based: most scripts grade (previous END trigger, latest
  END]; some use latest START / latest END; U2P2/U2P3 also fence by the client
  `timestamp`. The Attempt Window block states the script's window; the header's
  Trigger(Start) marks when the activity begins.
- Reason code names are UPPER_SNAKE_CASE; variables are the message's
  placeholders verbatim (`attempt_number`, `wrong_box_summary`, …).
- Player field in logs is `user_id` (24-hex StrataHub id) since 2026-05;
  the scripts say `playerId` and the harness maps it.

## Keeping the three copies in sync

A rule lives in three places that must agree: the markdown script, its Python
transcription (`test_uXpY.py` / `rc_uXpY.py`), and the Go rule in
`mhsgrader/internal/app/rules/uXpY.go`. After changing a script:

1. Update the transcription and run `python run_all.py` in both suites (all
   fixtures must stay 26/26; expected colours/codes live in the `config/*.yaml`).
2. Update the Go rule and run `go test ./internal/app/grader/ -run TestFixtureReplay`
   in `mhsgrader` (replays the same fixtures through the real grader).
3. If a message or guidance changed: regenerate the dashboard catalog
   (`go run ./cmd/mhsreasoncodes` in `mhsgrader`) and the section-B index table.

## Notes for Claude

- The per-point documents are authoritative; `Reason-codes-and-instructor-messages.md`
  section B is generated from them.
- Fixture expectations are established independently of the scripts (audit +
  tester intent); never paste a script's output back in as the expectation.
- Open decisions for the grading team and the corrections already made are in
  `docs/`; check them before "fixing" something that is deliberately as it is
  (e.g. U3P3 counting the success node, U3P5's 2.5 threshold).
