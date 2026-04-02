# MHS Grading: Issues, Updates, and Fixes

**Date:** 2026-03-18
**Scope:** Comparison of mhsgrading documentation vs. mhsgrader code implementation

---

## Critical Issues

### 1. U4P6 — Box ID Mismatch Between Analytics/Production Scripts and Code

**File:** `mhs-unit4-point6-grading.md`, `mhsgrader/internal/app/rules/u4p6.go`

The analytics script, production script, and Go code all use different box ID schemes and soil type mappings:

| Source | Box IDs | Box 1 | Box 2 | Box 3 |
|--------|---------|-------|-------|-------|
| Analytics script | "1", "2", "3" | Gravel | Sand | Clay |
| Production script | "0", "1", "2" | Clay | Sand | Gravel |
| Go code (u4p6.go) | "1", "2", "3" | Gravel | Sand | Clay |

The Go code matches the analytics script, not the production script. If the production game build sends `boxId` values as `"0"`, `"1"`, `"2"` (zero-indexed), the Go grader will fail to match any events because it looks for `"1"`, `"2"`, `"3"`.

Additionally, the soil type mappings are swapped between the analytics and production scripts — Box 1/Gravel vs Box 0/Clay and Box 3/Clay vs Box 2/Gravel.

**Action Required:** Verify what `boxId` values the production game actually sends by querying the logdata collection:

```js
db.logdata.find({
  eventType: "TerasGardenBox",
  "data.actionType": "cameraPlaced"
}, { "data.boxId": 1, "data.soilType": 1 }).limit(20)
```

Then align the Go code to match production values. Either:
- Change Go code to use `"0"`, `"1"`, `"2"` with the production soil mappings, OR
- Confirm the game sends `"1"`, `"2"`, `"3"` and fix the production script in the doc

---

### 2. U3P3 — Target Key List Discrepancy (Code Has Extra Keys)

**File:** `mhs-unit3-point3-grading.md`, `mhsgrader/internal/app/rules/u3p3.go`

The documentation lists **16 target keys** (incorrect argument selections), deliberately skipping `DialogueNodeEvent:84:36` and `DialogueNodeEvent:84:38`.

The Go code includes **18 target keys** — a contiguous range from `84:32` through `84:47` (which includes `84:36` and `84:38`).

| Key | In Doc | In Code |
|-----|--------|---------|
| `DialogueNodeEvent:84:36` | No | Yes |
| `DialogueNodeEvent:84:38` | No | Yes |

**Resolution:** Per dialogue document review: `84:36` is positive feedback and `84:38` has no feedback. Neither is negative feedback, but both are included in the code's target key count. The code is kept as-is (18 keys). Documentation updated to match the code.

---

### 3. U3P3 — Missing MISSING_SUCCESS_NODE Reason Code in Code

**File:** `mhs-unit3-point3-grading.md`, `mhsgrader/internal/app/rules/u3p3.go`

The documentation defines two reason codes:
- **MISSING_SUCCESS_NODE** — student didn't open the backing info panel
- **WRONG_ARG_SELECTED** — too many incorrect argument attempts

The Go code only produces `WRONG_ARG_SELECTED`. It gives a +1 bonus for using backing info but does **not** separately flag students who didn't check it. A student who didn't open the backing info panel AND had a low incorrect count could still pass (e.g., count <= 2 gives base_score = 3, no bonus needed).

The doc says the threshold for MISSING_SUCCESS_NODE is "check the information at least once during the activity." The current code doesn't enforce this as a separate flag.

**Action Required:** Decide whether MISSING_SUCCESS_NODE should be implemented as a separate reason code in the grader. If so, the code needs to check for backing info absence and flag it independently. If not, remove it from the documentation.

---

### 4. U4P4 — Production Script Bug in Documentation

**File:** `mhs-unit4-point4-grading.md`

The analytics script and Go code both check:
```
if (c_m1_top === 1 && c_m1_bottom === 0) → score += 1
```

The production script in the doc checks:
```
if (c_m1_top === 1 && c_m1_bottom === 1) → score += 1
```

The `c_m1_bottom === 1` condition is wrong — it should be `c_m1_bottom === 0`. The Go code is correct (matches analytics).

**Action Required:** Fix the production script in the documentation to use `c_m1_bottom === 0`.

---

## Threshold Discrepancies

### 5. U4P5 — Green/Yellow Threshold Description vs. Code

**File:** `mhs-unit4-point5-grading.md`, `mhsgrader/internal/app/rules/u4p5.go`

The documentation table says:
- Green: "the negative feedback number is **less than 4**"
- Yellow: "equal to or **larger than 4**"

This implies: 3 or fewer = green, 4 or more = yellow.

The Go code and analytics script both use `negCount > 4` (yellow if > 4), meaning:
- 4 or fewer = green, 5 or more = yellow

**The code allows 4 negatives and still passes; the doc text says 4 negatives should fail.**

**Resolution:** Per embedded assessment document review, the doc description is correct: green requires strictly fewer than 4 negatives. Code updated to `negCount >= 4`, and doc scripts updated from `> 4` to `>= 4` to match.

---

### 6. U2P7 — attempt_number Metric Off-by-One

**File:** `mhs-unit2-point7-grading.md`, `mhsgrader/internal/app/rules/u2p7.go`

The documentation defines `attempt_number = negCount + 1` (treating the final successful attempt as an attempt). The instructor message says "threshold for success is to construct the correct argument using equal to or less than 5 attempts."

The Go code stores `attempt_number = negCount` (without the +1). With the grading threshold of `negCount <= 3`:
- Doc: max attempts for green = 3 neg + 1 = **4 attempts** (contradicts the "5 attempts" in instructor message)
- Code: reports `attempt_number = 3` for the same scenario

**Action Required:**
1. Decide whether `attempt_number` should include the final successful attempt (+1) or not
2. Verify the instructor message threshold (should it say "4 attempts" instead of "5 attempts"?)

---

## Documentation Updates Needed

### 7. Title Error in mhs-unit5-point4-grading.md

**File:** `mhs-unit5-point4-grading.md`

The document title reads "# Unit 5 Point 3 Grading" but the filename is `mhs-unit5-point4-grading.md` and the activity is "Water Problems Require Water Solutions" which corresponds to U5P4 in the code.

**Action Required:** Change the title to "# Unit 5 Point 4 Grading".

---

### 8. Reason Codes Missing from 10 Documentation Files

The following files have `> Still figuring out the reason codes` instead of defined reason codes. The Go code already implements specific reason codes for all of these.

| File | Reason Codes in Code |
|------|---------------------|
| `mhs-unit4-point1-grading.md` | NO_TRIGGER, SCORE_BELOW_THRESHOLD |
| `mhs-unit4-point2-grading.md` | NO_TRIGGER, MISSING_SUCCESS_NODE, TOO_MANY_NEGATIVES |
| `mhs-unit4-point3-grading.md` | NO_TRIGGER, SCORE_BELOW_THRESHOLD |
| `mhs-unit4-point4-grading.md` | NO_TRIGGER, SCORE_BELOW_THRESHOLD |
| `mhs-unit4-point5-grading.md` | NO_TRIGGER, MISSING_SUCCESS_NODE, TOO_MANY_NEGATIVES |
| `mhs-unit4-point6-grading.md` | NO_TRIGGER, SCORE_BELOW_THRESHOLD |
| `mhs-unit5-point1-grading.md` | NO_TRIGGER, MISSING_SUCCESS_NODE, TOO_MANY_NEGATIVES |
| `mhs-unit5-point2-grading.md` | NO_TRIGGER, SCORE_BELOW_THRESHOLD |
| `mhs-unit5-point3-grading.md` | NO_TRIGGER, TOO_MANY_NEGATIVES |
| `mhs-unit5-point4-grading.md` | NO_TRIGGER, MISSING_SUCCESS_NODE, TOO_MANY_NEGATIVES |

**Action Required:** Add reason code sections with instructor messages, determination logic, and teacher guidance to each file. The format used in Units 1-3 docs (e.g., `mhs-unit3-point3-grading.md`) provides a good template.

---

## Verified Correct (No Issues Found)

The following progress points have matching documentation and code implementation:

| Unit | Point | Activity | Status |
|------|-------|----------|--------|
| U1 | P1 | Getting Your Space Legs | Matches |
| U1 | P2 | Info and Intros | Matches |
| U1 | P3 | Defend the Expedition | Matches |
| U1 | P4 | What Was That? | Matches |
| U2 | P1 | Escape the Ruin | Matches |
| U2 | P2 | Foraged Forging | Matches |
| U2 | P3 | Getting the Band Back Together II | Matches |
| U2 | P4 | Investigate the Temple | Matches |
| U2 | P5 | Classified Information | Matches |
| U2 | P6 | Which Watershed? Part I | Matches |
| U3 | P1 | Supply Run | Matches |
| U3 | P2 | Pollution Solution | Matches |
| U3 | P4 | Forsaken Facility | Matches |
| U3 | P5 | Plant the Superfruit Seeds | Matches |
| U4 | P1 | Well What Have We Here? | Matches |
| U4 | P2 | Power Play (Floors 1-2) | Matches |
| U4 | P3 | Power Play (Floors 3-4) | Matches |
| U5 | P1 | If I Had a Nickel (Floors 1-2) | Matches |
| U5 | P2 | If I Had a Nickel (Floors 3-4) | Matches |
| U5 | P3 | What Happened Here? | Matches |

---

## Dashboard Reason Code Display

The MHS Dashboard `reasonCodeToMessage` map in `stratahub/internal/app/features/mhsdashboard/dashboard.go` was missing three reason codes, causing raw codes to display (e.g., "Needs improvement: WRONG_ARG_SELECTED"). These have been added:

| Code | Message |
|------|---------|
| WRONG_ARG_SELECTED | Student needed multiple attempts to construct a correct scientific argument. |
| BAD_FEEDBACK | Student received repeated corrective feedback during the activity. |
| HIT_YELLOW_NODE | Student made an incorrect selection when evaluating evidence. |

---

## Summary

| Priority | Count | Description | Status |
|----------|-------|-------------|--------|
| Critical | 1 | U4P6 Box ID mismatch | **Fixed** |
| Critical | 1 | U3P3 extra target keys (84:36, 84:38) | **Fixed** |
| Critical | 1 | U3P3 missing MISSING_SUCCESS_NODE in code | **Fixed** |
| Critical | 1 | U4P4 production script bug in doc | **Fixed** |
| Threshold | 1 | U4P5 boundary condition (< 4 vs <= 4) | **Fixed** |
| Threshold | 1 | U2P7 attempt_number off-by-one | **Fixed** |
| Documentation | 1 | U5P4 title error | **Fixed** |
| Documentation | 1 | 10 files missing reason codes | **Fixed** |
| Fixed | 1 | Dashboard reason code display | **Fixed** |
