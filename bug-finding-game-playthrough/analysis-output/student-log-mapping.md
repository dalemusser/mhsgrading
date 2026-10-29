# Student → Gameplay Log Mapping

*First-pass forensic investigation, 2026-10-06. Done before any bug analysis, as the protocol requires.*

## Method

- The ten files under `players-logs-met-bugs/` are named `<class>.<first>.<last>.stratalog.logdata.json`.
- Each was matched to the tracker's `Students` field by class/site code (`lawyer2`, `lawyer5`, `meyer1`, `meyer2`) and fuzzy name comparison.
- File contents were then checked for identity consistency:
  - exactly one `user_id` per file;
  - account-creation batch, decoded from the `user_id` ObjectId timestamp;
  - class-period session start times.
- The logs contain **no student names**, so name identity rests on the filename alone. Contents can only confirm that the file behaves like a member of the named class.

## Mapping

| Issue | Student listed in tracker | Matched log filename | Confidence | Reason for match |
|---|---|---|---|---|
| QA 1693, QA 1694 | Lawyer2 / **Reed** Henggeler | `lawyer2.read.henggeler.stratalog.logdata.json` | **High** (spelling flag) | Class code and surname exact. First name `read` vs `Reed` is almost certainly a filename typo. Only Lawyer2/Henggeler file. One `user_id` (`6aa36157…`, created 2026-09-11 with the Lawyer batch). All 29 sessions start in the Lawyer2 period (13:xx UTC), the same as Isabella's. |
| QA 1693, QA 1694 | Lawyer2 / Isabella Ruminer | `lawyer2.isabella.ruminer.stratalog.logdata.json` | **High** | Exact name and class. One `user_id` (`6aad4a5d…`). 19 of 21 sessions start in the Lawyer2 period. *Note:* this account was created on 2026-09-18, a week after the rest of the Lawyer batch (2026-09-11), so it was probably added late; no evidence of a second account. |
| QA 1694 | Lawyer5 / Corah Thompson | `lawyer5.corah.thompson.stratalog.logdata.json` | **High** | Exact name and class. `user_id 6aa36227…768`. 20 of 25 sessions start in the Lawyer5 period (15:xx UTC). |
| QA 1694 | Lawyer5 / Molli Kelme | `lawyer5.molli.kelme.stratalog.logdata.json` | **High** | Exact name and class. `user_id 6aa36227…75c`, same creation batch as Corah. 22 of 24 sessions in the Lawyer5 period. |
| QA 1697 | Meyer1 / Katelyn Ballman | `meyer1.katelyn.ballman.stratalog.logdata.json` | **High** | Exact name and class. Meyer1 batch (`6aa47d6a…`). |
| QA 1697 | Meyer1 / Taye Roschen | `meyer1.taye.roschen.stratalog.logdata.json` | **High** | Exact name and class. Meyer1 batch. |
| QA 1697 | Meyer2 / Liv Brinkman | `meyer2.liv.brinkman.stratalog.logdata.json` | **High** | Exact name and class. Meyer2 batch (`6aa480ec…`). |
| QA 1697 | Meyer2 / Mae Schuller | `meyer2.mae.schuller.stratalog.logdata.json` | **High** | Exact name and class. Meyer2 batch. |
| QA 1697 | Meyer2 / Walton **Gronvall** | `meyer2.walton.gronrall.stratalog.logdata.json` | **Medium-High** (spelling flag) | First name exact and class code matches. Surname differs by one letter (`gronrall` vs `Gronvall`). Only Walton file and only Meyer2 file left unmatched. Meyer2 batch `user_id`. The tracker text "…Mae Schuller. Walton Gronvall" is read as Walton belonging to Meyer2; the stray period makes that slightly ambiguous. |
| U4 Saving Cadet Anderson | Meyer1 / Ella Preble | `meyer1.ella.preble.stratalog.logdata.json` | **High** | Exact name and class. Meyer1 batch. |

## Inventory checks

| Check | Result |
|---|---|
| Missing student logs | **None.** Every student named in the four issue files has exactly one log. |
| Ambiguous matches | None that change the analysis. The two spelling differences are flagged above. |
| Duplicate candidate logs | None. Each file holds exactly one `user_id` and no `user_id` appears in two files. |
| Apparent naming typos | `read` → **Reed** (Henggeler). `gronrall` → **Gronvall** (Walton). |
| Students in several issues | Reed Henggeler and Isabella Ruminer appear in QA 1693 **and** QA 1694. |
| Students with several sessions / days | **All of them.** Each file covers several days: 5–29 game starts (`gameStartEvent`) over 3–12 days, between 2026-09-18 and 2026-10-05. Session boundaries were derived from `gameStartEvent`. |
| Build | Every gameplay record carries `version: "20260914-"`, the same truncated string as the internal playthroughs 09-14-26-3 and 09-23-26. A silent build change behind that string cannot be ruled out (see cross-issue summary). Crash records carry an app-wrapper version `2.8.1` throughout. |
| Device | All ten files report the same device class: `UnityWebGL`, ANGLE/Intel ADL-N GPU, 1366×768, PWA. These are almost certainly school Chromebooks. |

## Controls used

No unaffected classmates' logs were supplied. The controls are:

1. **Ella Preble** (`meyer1`). She is a same-classroom, same-build student who completed Unit 2 and Unit 3 normally, which makes her the control for QA 1693, 1694 and 1697. She is also the U4 case.
2. **The five Meyer students** (Katelyn, Taye, Liv, Mae, Walton). They were skipped from Unit 2 to Unit 3 like the Lawyer students, but did **not** hit the Supply Run problem. They serve as the "skipped but not affected" group the QA 1694 file asks for.
3. **Two complete internal playthroughs** on the same `20260914-` version string: `playthrough-logs-and-results/09-14-26-3` and `09-23-26`. They provide the reference event sequences.
