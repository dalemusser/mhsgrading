"""
Shared reporting / assertion plumbing for the per-point grading tests.

Every `test_uXpY.py` file defines:

    META = {"unit": 1, "point": 3, "name": "..."}

    def grade(coll, pid) -> str           # "green" | "yellow" (production logic)
    def diagnose(coll, pid) -> dict        # reason-code findings (why yellow / mismatch)

and ends with:

    if __name__ == "__main__":
        from mhs_report import run_standalone
        run_standalone(__name__)

Expected colors live in `config/fixtures.yaml` (per fixture log), not in the
test modules: the same rubric implementation is expected to give different
colors on different playthroughs. `run_standalone` loads the default fixture,
runs the production grader, compares it against the fixture's expected color,
and—if they differ, or the point is yellow—prints the reason diagnostics so we
can see *why* and decide whether the production color logic needs to change.
"""

import importlib
import sys

from mhs_harness import load_collection, default_player_id, resolve_fixture

# Windows consoles default to cp1252; make sure em-dashes/bullets render.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def evaluate(module, coll, pid, expected):
    """Run one point's grader + diagnostics. Returns a result dict.

    `expected` is the fixture's expected color, or None for an ad-hoc log with
    no known expectation (then `passed` is None and no comparison is made).
    """
    meta = module.META
    expected = expected.lower() if expected else None
    actual = module.grade(coll, pid).lower()
    passed = None if expected is None else (actual == expected)

    diag = {}
    # Surface reasons whenever the point is (or should be) yellow, or whenever
    # production disagrees with the expected dashboard color.
    if hasattr(module, "diagnose") and (
        actual == "yellow" or expected == "yellow" or passed is False
    ):
        try:
            diag = module.diagnose(coll, pid) or {}
        except Exception as exc:  # diagnostics must never mask the grade result
            diag = {"diagnose_error": repr(exc)}

    return {
        "unit": meta["unit"],
        "point": meta["point"],
        "name": meta.get("name", ""),
        "expected": expected,
        "actual": actual,
        "passed": passed,
        "diagnostics": diag,
    }


def format_result(res):
    if res["passed"] is None:
        head = (
            f"[----] U{res['unit']}P{res['point']} — {res['name']}\n"
            f"       actual={res['actual']:<6} (no expected color for this log)"
        )
    else:
        tag = "PASS" if res["passed"] else "FAIL"
        head = (
            f"[{tag}] U{res['unit']}P{res['point']} — {res['name']}\n"
            f"       expected={res['expected']:<6} actual={res['actual']:<6}"
        )
    lines = [head]
    if res["diagnostics"]:
        if res["passed"] and res["actual"] == "yellow":
            lines.append("       reason(s) for yellow (expected):")
        elif res["passed"] is False:
            lines.append("       MISMATCH — possible cause(s):")
        for k, v in res["diagnostics"].items():
            lines.append(f"         - {k}: {v}")
    return "\n".join(lines)


def run_standalone(module_name):
    """Run one point against the default fixture (used by `python test_uXpY.py`).
    Exit code 0 = production color matches the fixture's expected color."""
    module = importlib.import_module(module_name) if isinstance(module_name, str) else module_name
    # When called as __main__, importlib can't re-import; use sys.modules.
    if isinstance(module_name, str) and module_name == "__main__":
        module = sys.modules["__main__"]

    fixture_id, log_path, entry = resolve_fixture()
    coll = load_collection(log_path)
    pid = default_player_id(coll)
    pp_id = f"U{module.META['unit']}P{module.META['point']}"
    expected = (entry.get("expected") or {}).get(pp_id)
    print(f"Fixture {fixture_id} | player = {pid}"
          + (" (adapted from user_id)" if coll.player_field_source != "playerId" else ""))

    res = evaluate(module, coll, pid, expected)
    print(format_result(res))
    sys.exit(0 if res["passed"] else 1)
