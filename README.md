# mhsgrading

Grading in Mission HydroSci for use by mhsgrader.

## Repository layout

| Folder | Contents |
| ------ | -------- |
| [grading-logic/](grading-logic/) | The dashboard color-grading logic for every unit and progress point (see index below), plus [Reason-codes-and-instructor-messages.md](grading-logic/Reason-codes-and-instructor-messages.md) and [mhs-unit-start.md](grading-logic/mhs-unit-start.md). |
| [feedback-message-for-each-pp/](feedback-message-for-each-pp/) | Source material and outputs for per-progress-point pop-up feedback: assessment score rubrics, curriculum goals, potential strategies, context dialogue (docx), game narrative combo docs, and example pop-up feedback (e.g. [yellow-pp-teacher-feedback-units1-2.md](feedback-message-for-each-pp/example-pop-up-feedback/yellow-pp-teacher-feedback-units1-2.md)). |
| [tests/](tests/) | Python test suite validating the 26 point-grading scripts against captured gameplay logs — one `test_uXpY.py` per point, a MongoDB-like harness, and an aggregate runner. See [tests/README.md](tests/README.md). |
| [playthrough-logs-and-results/](playthrough-logs-and-results/) | Captured gameplay log dumps and their test results, organized by playthrough date (e.g. `05-01-26/`). |
| [prompts/](prompts/) | Prompts used to generate grading logic and adaptive feedback. |
| [docs/](docs/) | Project notes — [issues_and_updates.md](docs/issues_and_updates.md). |

## Grading logic by unit

- [Unit 1 - Get Your Space Legs](grading-logic/mhs-unit1-grading.md)
  - [Point 1 - Getting Your Space Legs](grading-logic/mhs-unit1-point1-grading.md)
  - [Point 2 - Info and Intros](grading-logic/mhs-unit1-point2-grading.md)
  - [Point 3 - Defend the Expedition](grading-logic/mhs-unit1-point3-grading.md)
  - [Point 4 - What Was That?](grading-logic/mhs-unit1-point4-grading.md)
- [Unit 2 - Find the Flow](grading-logic/mhs-unit2-grading.md)
  - [Point 1 - Escape the Ruin](grading-logic/mhs-unit2-point1-grading.md)
  - [Point 2 - Foraged Forging](grading-logic/mhs-unit2-point2-grading.md)
  - [Point 3 - Getting the Band Back Together Part II](grading-logic/mhs-unit2-point3-grading.md)
  - [Point 4 - Investigate the Temple](grading-logic/mhs-unit2-point4-grading.md)
  - [Point 5 - Classified Information](grading-logic/mhs-unit2-point5-grading.md)
  - [Point 6 - Which Watershed? Part I](grading-logic/mhs-unit2-point6-grading.md)
  - [Point 7 - Which Watershed? Part II](grading-logic/mhs-unit2-point7-grading.md)
- [Unit 3 - Clean the Stream](grading-logic/mhs-unit3-grading.md)
  - [Point 1 - Good Morning Cadet + Establishing a Foothold](grading-logic/mhs-unit3-point1-grading.md)
  - [Point 2 - Pollution Solution](grading-logic/mhs-unit3-point2-grading.md)
  - [Point 3 - Pollution Argument](grading-logic/mhs-unit3-point3-grading.md)
  - [Point 4 - Forsaken Facility](grading-logic/mhs-unit3-point4-grading.md)
  - [Point 5 - Plant the Superfruit Seeds](grading-logic/mhs-unit3-point5-grading.md)
- [Unit 4 - Dig Deeper](grading-logic/mhs-unit4-grading.md)
  - [Point 1 - Well What Have We Here?](grading-logic/mhs-unit4-point1-grading.md)
  - [Point 2 - Power Play- Floors 1 & 2](grading-logic/mhs-unit4-point2-grading.md)
  - [Point 3 - Power Play- Floors 3 & 4](grading-logic/mhs-unit4-point3-grading.md)
  - [Point 4 - Power Play- Floor 5](grading-logic/mhs-unit4-point4-grading.md)
  - [Point 5 - Saving Cadet Anderson](grading-logic/mhs-unit4-point5-grading.md)
  - [Point 6 - Desert Delicacies](grading-logic/mhs-unit4-point6-grading.md)
- [Unit 5 - Rise and Return](grading-logic/mhs-unit5-grading.md)
  - [Point 1 - If I Had a Nickel- Floors 1 & 2](grading-logic/mhs-unit5-point1-grading.md)
  - [Point 2 - If I Had a Nickel- Floors 3 & 4](grading-logic/mhs-unit5-point2-grading.md)
  - [Point 3 - What Happened Here?](grading-logic/mhs-unit5-point3-grading.md)
  - [Point 4 - Water Problems Require Water Solutions](grading-logic/mhs-unit5-point4-grading.md)

## Validating the grading logic

To check the 26 point-grading scripts against a gameplay log dump:

```bash
cd tests
python run_all.py                 # full table + diagnostics
python run_all.py --log PATH.json # validate a new build's log dump
```

Details in [tests/README.md](tests/README.md).
