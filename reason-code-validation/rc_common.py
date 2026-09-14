"""
Shared plumbing for the reason-code validation suite.

Each `grading-logic/mhs-unitX-pointY-grading.md` file ends with a
"## Reason Codes" section: one `### CODE_NAME` per reason code, an
`**Instructor Message:**` template with `{variable}` placeholders, and a
"Corresponding Script" (mongosh JS) that returns
`{ triggered: <bool>, <variable>: <value>, ... }` for the latest attempt
window. When a point is yellow, the dashboard pop-up shows the message of every
triggered code with its variables filled in.

This suite validates those scripts the same way `rubric-validation/` validates
the color scripts: every Corresponding Script is transcribed 1:1 into a Python
module `rc_uXpY.py` (running on the same in-memory Mongo-like harness), executed
against a fixture log, and checked against:

  1. the fixture's expected triggered codes + variable values
     (`config/expectations.yaml`);
  2. the production color from `rubric-validation/test_uXpY.grade()` —
     a yellow cell must trigger at least one code and a green cell none
     (the scripts recompute the color formula, so the pop-up and the cell can
     never disagree; this check proves it on real data);
  3. the markdown itself — the module's code set must match the `###`
     headings, and every `{placeholder}` in the Instructor Message must be
     supplied by the script's return object (no unresolved placeholders).

Module contract (every `rc_uXpY.py`):

    META = {"unit": 2, "point": 1, "name": "...", "doc": "mhs-unit2-point1-grading.md"}
    CODES = {"SOLVED_WITH_ASSIST": solved_with_assist, ...}   # ordered as in the markdown
    def attempt_window(coll, pid) -> (start_id, end_id) | None  # the scripts' window
    def <code>(coll, pid) -> {"triggered": bool, <variable>: value, ...}

The query layer (`mhs_harness`) and the color graders (`test_uXpY`) are imported
from `../rubric-validation/` — nothing there is modified; this folder only reads
from it, the same way `grading-readiness-audit/` does.
"""

import importlib
import os
import re
import sys

SUITE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SUITE_DIR)
RUBRIC_DIR = os.path.join(REPO_ROOT, "rubric-validation")
GRADING_DIR = os.path.join(REPO_ROOT, "grading-logic")
EXPECTATIONS_YAML = os.path.join(SUITE_DIR, "config", "expectations.yaml")

if RUBRIC_DIR not in sys.path:
    sys.path.insert(0, RUBRIC_DIR)

import mhs_harness  # noqa: E402  (from rubric-validation/)
from mhs_harness import GAME, OID_MIN, latest_trigger_window  # noqa: E402,F401

# Windows consoles default to cp1252; make sure em-dashes/bullets render.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Dashboard order: points per unit.
UNIT_POINTS = {1: 4, 2: 7, 3: 5, 4: 6, 5: 4}
POINTS = [(u, p) for u in sorted(UNIT_POINTS) for p in range(1, UNIT_POINTS[u] + 1)]

PLACEHOLDER_RE = re.compile(r"\{([a-z][a-z0-9_]*)\}")
CODE_HEADING_RE = re.compile(r"^### ([A-Z][A-Z0-9_]+)\s*$")


# --------------------------------------------------------------------------
# Query helpers shared by the per-point modules (keep the transcriptions terse
# and visibly identical to the JS).
# --------------------------------------------------------------------------

def gt_lte(win):
    """`_id: { $gt: windowStartId, $lte: windowEndId }` (the common filter)."""
    return {"_id": {"$gt": win[0], "$lte": win[1]}}


def gte_lte(win):
    """`_id: { $gte: startId, $lte: endId }` (U2P2 / U2P3 style)."""
    return {"_id": {"$gte": win[0], "$lte": win[1]}}


def _key_query(pid, keys, extra):
    q = {"game": GAME, "playerId": pid}
    if isinstance(keys, (list, tuple)):
        q["eventKey"] = {"$in": list(keys)}
    else:
        q["eventKey"] = keys
    q.update(extra or {})
    return q


def count_keys(coll, pid, keys, extra=None):
    """`db.logdata.countDocuments({game, playerId, eventKey: {$in: keys}, ...extra})`."""
    return coll.count_documents(_key_query(pid, keys, extra))


def has_keys(coll, pid, keys, extra=None):
    """`db.logdata.findOne({...}) !== null`."""
    return coll.find_one(_key_query(pid, keys, extra)) is not None


def latest(coll, pid, key, extra=None):
    """`findOne({game, playerId, eventKey: key, ...extra}, {sort: {_id: -1}})`."""
    return coll.find_one(_key_query(pid, key, extra), sort={"_id": -1})


def earliest(coll, pid, key, extra=None):
    """`findOne({...}, {sort: {_id: 1}})`."""
    return coll.find_one(_key_query(pid, key, extra), sort={"_id": 1})


def start_end_window(coll, pid, start_key, end_key, strict=True):
    """Distinct start/end anchors: latest START and latest END, END must follow
    START. `strict=True` mirrors the guard `latestEnd._id <= latestStart._id`
    (U2P6, U3P4, U4P4); `strict=False` mirrors `latestEnd._id < latestStart._id`
    (U4P6, U5P1, U5P2, U5P3). Returns (start_id, end_id) or None."""
    s = latest(coll, pid, start_key)
    e = latest(coll, pid, end_key)
    if not s or not e:
        return None
    if strict and e["_id"] <= s["_id"]:
        return None
    if not strict and e["_id"] < s["_id"]:
        return None
    return s["_id"], e["_id"]


def js_round(x):
    """JavaScript `Math.round` (half rounds toward +Infinity), unlike Python's
    banker's rounding."""
    import math
    return int(math.floor(x + 0.5))


# --------------------------------------------------------------------------
# Fixture / expectation manifest
# --------------------------------------------------------------------------

def load_expectations(path=None):
    import yaml  # deferred so the modules stay import-safe without pyyaml

    with open(path or EXPECTATIONS_YAML, encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
    if not manifest.get("fixtures"):
        raise SystemExit(f"No fixtures defined in {path or EXPECTATIONS_YAML}")
    return manifest


def resolve_fixture(fixture_id=None, manifest=None):
    """Return (fixture_id, absolute log path, fixture entry)."""
    manifest = manifest or load_expectations()
    fixture_id = fixture_id or manifest.get("default_fixture")
    entry = (manifest.get("fixtures") or {}).get(fixture_id)
    if entry is None:
        known = ", ".join(sorted(manifest.get("fixtures") or {}))
        raise SystemExit(f"Unknown fixture '{fixture_id}' (known: {known})")
    log = entry["log"]
    if not os.path.isabs(log):
        log = os.path.join(REPO_ROOT, log)
    return fixture_id, log, entry


def load_collection(path):
    return mhs_harness.load_collection(path)


def default_player_id(coll):
    return mhs_harness.default_player_id(coll)


# --------------------------------------------------------------------------
# Markdown: the Reason Codes section of a grading file
# --------------------------------------------------------------------------

def parse_reason_codes(doc_name):
    """Parse `grading-logic/<doc_name>`'s "## Reason Codes" section.

    Returns {"codes": [(code, message), ...] in document order,
             "guidance": "<Teacher Guidance text or ''>",
             "no_codes_note": "<blockquote text>" or None}.
    """
    path = os.path.join(GRADING_DIR, doc_name)
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Locate the section.
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## Reason Codes")
    except StopIteration:
        raise ValueError(f"{doc_name}: no '## Reason Codes' section")
    section = lines[start + 1:]
    end = next((i for i, l in enumerate(section) if l.startswith("## ")), len(section))
    section = section[:end]

    codes, guidance, note = [], [], None
    current, in_code_block, in_guidance = None, False, False
    for line in section:
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        m = CODE_HEADING_RE.match(line)
        if m:
            current, in_guidance = m.group(1), False
            codes.append([current, None])
            continue
        if line.startswith("### "):
            current = None
            in_guidance = line.strip().rstrip(":").lower().endswith("teacher guidance")
            continue
        if line.startswith("#### "):
            continue
        if in_guidance:
            guidance.append(line)
            continue
        if current and "**Instructor Message:**" in line:
            msg = line.split("**Instructor Message:**", 1)[1].strip()
            codes[-1][1] = msg
            continue
        if note is None and line.startswith("> No reason codes"):
            note = line[1:].strip()

    for code, msg in codes:
        if msg is None:
            raise ValueError(f"{doc_name}: reason code {code} has no **Instructor Message:** line")
    return {
        "codes": [(c, m) for c, m in codes],
        "guidance": "\n".join(guidance).strip(),
        "no_codes_note": note,
    }


def placeholders(message):
    """Ordered, de-duplicated `{variable}` names used by a message template."""
    seen = []
    for name in PLACEHOLDER_RE.findall(message):
        if name not in seen:
            seen.append(name)
    return seen


def render_message(message, variables):
    """Fill `{variable}` placeholders. Unknown placeholders are left in place
    (and reported by the placeholder check)."""
    def sub(m):
        name = m.group(1)
        if name in variables:
            v = variables[name]
            return "" if v is None else str(v)
        return m.group(0)
    return PLACEHOLDER_RE.sub(sub, message)


# --------------------------------------------------------------------------
# Evaluation of one point
# --------------------------------------------------------------------------

def load_modules(unit, point):
    """(reason-code module, color-grading module) for a point."""
    rc = importlib.import_module(f"rc_u{unit}p{point}")
    color = importlib.import_module(f"test_u{unit}p{point}")
    return rc, color


def evaluate_point(rc, color_mod, coll, pid, expectation=None):
    """Run every reason-code script of one point and all consistency checks.

    `expectation` is the fixture entry for this point ({"codes": [...],
    "variables": {CODE: {var: value}}}) or None for an ad-hoc log.
    """
    meta = rc.META
    unit, point = meta["unit"], meta["point"]
    pp_id = f"U{unit}P{point}"
    doc = parse_reason_codes(meta["doc"])
    md_codes = [c for c, _ in doc["codes"]]
    md_messages = dict(doc["codes"])
    module_codes = list(rc.CODES.keys())

    checks = []  # (name, ok, detail)

    # 1) Code set: module must transcribe exactly the markdown's codes.
    if md_codes == module_codes:
        checks.append(("code-set", True, ", ".join(md_codes) or "no reason codes"))
    else:
        checks.append(("code-set", False,
                       f"markdown has [{', '.join(md_codes)}] but module has "
                       f"[{', '.join(module_codes)}]"))

    # 2) Production color (from rubric-validation) and the attempt window.
    color = color_mod.grade(coll, pid).lower()
    window = rc.attempt_window(coll, pid)
    has_window = window is not None

    # 3) Run the scripts.
    code_results = {}
    triggered = []
    for code, fn in rc.CODES.items():
        try:
            raw = fn(coll, pid) or {}
        except Exception as exc:  # a crashing script is a finding, not a crash
            checks.append((f"script:{code}", False, f"raised {exc!r}"))
            code_results[code] = {"triggered": None, "variables": {}, "message": None,
                                  "error": repr(exc)}
            continue
        if "triggered" not in raw:
            checks.append((f"script:{code}", False, "return object has no `triggered`"))
        is_trig = bool(raw.get("triggered"))
        variables = {k: v for k, v in raw.items() if k != "triggered"}
        template = md_messages.get(code, "")
        needed = placeholders(template)
        missing = [n for n in needed if n not in variables]
        if missing:
            checks.append((f"placeholders:{code}", False,
                           f"message uses {{{'}, {'.join(missing)}}} but the script does not return it"))
        else:
            checks.append((f"placeholders:{code}", True,
                           "uses " + ", ".join(needed) if needed else "no placeholders"))
        rendered = render_message(template, variables) if template else None
        code_results[code] = {
            "triggered": is_trig,
            "variables": variables,
            "message": rendered,
            "extra_variables": [k for k in variables if k not in needed],
        }
        if is_trig:
            triggered.append(code)

    # 4) Pop-up <-> cell consistency.
    if not rc.CODES:
        checks.append(("color-consistency", True,
                       f"n/a (no reason codes; production color {color})"))
    elif not has_window:
        ok = not triggered
        checks.append(("color-consistency", ok,
                       "no attempt window → no pop-up expected; production color "
                       f"{color} (dashboard shows the not-reached state)"
                       + ("" if ok else f" — but triggered: {', '.join(triggered)}")))
    else:
        want_trig = color == "yellow"
        ok = want_trig == bool(triggered)
        checks.append(("color-consistency", ok,
                       f"production {color}; triggered [{', '.join(triggered) or '-'}]"
                       + ("" if ok else
                          (" — YELLOW CELL WITHOUT A REASON CODE" if want_trig
                           else " — GREEN CELL WITH A TRIGGERED REASON CODE"))))

    # 5) Fixture expectations.
    expected_codes = None
    if expectation is not None:
        expected_codes = list(expectation.get("codes") or [])
        unknown = [c for c in expected_codes if c not in rc.CODES]
        if unknown:
            checks.append(("expected-codes", False,
                           f"expectation names unknown code(s): {', '.join(unknown)}"))
        elif sorted(expected_codes) == sorted(triggered):
            checks.append(("expected-codes", True,
                           f"[{', '.join(expected_codes) or '-'}]"))
        else:
            checks.append(("expected-codes", False,
                           f"expected [{', '.join(expected_codes) or '-'}], "
                           f"got [{', '.join(triggered) or '-'}]"))
        for code, exp_vars in (expectation.get("variables") or {}).items():
            got = (code_results.get(code) or {}).get("variables") or {}
            diffs = []
            for var, exp_val in (exp_vars or {}).items():
                if var not in got:
                    diffs.append(f"{var}: not returned (expected {exp_val!r})")
                elif not _values_equal(got[var], exp_val):
                    diffs.append(f"{var}: expected {exp_val!r}, got {got[var]!r}")
            if diffs:
                checks.append((f"expected-variables:{code}", False, "; ".join(diffs)))
            else:
                checks.append((f"expected-variables:{code}", True,
                               ", ".join(f"{k}={v!r}" for k, v in (exp_vars or {}).items())))

    passed = all(ok for _, ok, _ in checks)
    return {
        "pp": pp_id,
        "unit": unit,
        "point": point,
        "name": meta.get("name", ""),
        "doc": meta["doc"],
        "color": color,
        "has_window": has_window,
        "triggered": triggered,
        "expected_codes": expected_codes,
        "codes": code_results,
        "guidance": doc["guidance"],
        "checks": [{"name": n, "ok": ok, "detail": d} for n, ok, d in checks],
        "passed": passed,
    }


def _values_equal(got, exp):
    if isinstance(exp, float) or isinstance(got, float):
        try:
            return abs(float(got) - float(exp)) < 1e-6
        except (TypeError, ValueError):
            return False
    return got == exp


# --------------------------------------------------------------------------
# Printing
# --------------------------------------------------------------------------

def format_point(res, show_all_codes=False):
    """Human-readable block for one point: status line, checks, and the
    rendered instructor message(s)."""
    tag = "PASS" if res["passed"] else "FAIL"
    lines = [f"[{tag}] {res['pp']} — {res['name']}",
             f"       production color = {res['color']}"
             + ("" if res["has_window"] else "  (no attempt window)")
             + f" | triggered = [{', '.join(res['triggered']) or '-'}]"
             + (f" | expected = [{', '.join(res['expected_codes']) or '-'}]"
                if res["expected_codes"] is not None else "")]
    for chk in res["checks"]:
        if not chk["ok"]:
            lines.append(f"       ✗ {chk['name']}: {chk['detail']}")
    for code, cr in res["codes"].items():
        if cr.get("error"):
            lines.append(f"       {code}: ERROR {cr['error']}")
            continue
        if not (cr["triggered"] or show_all_codes):
            continue
        state = "TRIGGERED" if cr["triggered"] else "not triggered"
        vars_str = ", ".join(f"{k}={v!r}" for k, v in cr["variables"].items()) or "-"
        lines.append(f"       {code} [{state}]  {vars_str}")
        if cr["triggered"] and cr["message"]:
            lines.append(_wrap(cr["message"], indent=11, width=88))
    return "\n".join(lines)


def _wrap(text, indent, width):
    import textwrap
    pad = " " * indent
    return "\n".join(textwrap.wrap(text, width=width, initial_indent=pad + "» ",
                                   subsequent_indent=pad + "  "))


def run_standalone(module_name):
    """`python rc_uXpY.py` — evaluate one point against the default fixture."""
    rc = sys.modules["__main__"] if module_name == "__main__" else importlib.import_module(module_name)
    fixture_id, log_path, entry = resolve_fixture()
    coll = load_collection(log_path)
    pid = default_player_id(coll)
    color_mod = importlib.import_module(f"test_u{rc.META['unit']}p{rc.META['point']}")
    pp_id = f"U{rc.META['unit']}P{rc.META['point']}"
    expectation = (entry.get("expected") or {}).get(pp_id)
    print(f"Fixture {fixture_id} | player = {pid}"
          + (" (adapted from user_id)" if coll.player_field_source != "playerId" else ""))
    res = evaluate_point(rc, color_mod, coll, pid, expectation)
    print(format_point(res, show_all_codes=True))
    sys.exit(0 if res["passed"] else 1)
