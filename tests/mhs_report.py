"""
Shared reporting / assertion plumbing for the per-point grading tests.

Every `test_uXpY.py` file defines:

    META = {"unit": 1, "point": 3, "name": "...", "expected": "yellow"}

    def grade(coll, pid) -> str           # "green" | "yellow" (production logic)
    def diagnose(coll, pid) -> dict        # reason-code findings (why yellow / mismatch)

and ends with:

    if __name__ == "__main__":
        from mhs_report import run_standalone
        run_standalone(__name__)

`run_standalone` loads the shipped log, runs the production grader, compares it
against the expected dashboard color, and—if they differ, or the point is
yellow—prints the reason diagnostics so we can see *why* and decide whether the
production color logic needs to change.
"""

import importlib
import sys

from mhs_harness import load_collection, default_player_id

# Windows consoles default to cp1252; make sure em-dashes/bullets render.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def evaluate(module, coll=None, pid=None):
    """Run one point's grader + diagnostics. Returns a result dict."""
    if coll is None:
        coll = load_collection()
    if pid is None:
        pid = default_player_id(coll)

    meta = module.META
    expected = meta["expected"].lower()
    actual = module.grade(coll, pid).lower()
    passed = actual == expected

    diag = {}
    # Surface reasons whenever the point is (or should be) yellow, or whenever
    # production disagrees with the expected dashboard color.
    if hasattr(module, "diagnose") and (actual == "yellow" or expected == "yellow" or not passed):
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
    tag = "PASS" if res["passed"] else "FAIL"
    head = (
        f"[{tag}] U{res['unit']}P{res['point']} — {res['name']}\n"
        f"       expected={res['expected']:<6} actual={res['actual']:<6}"
    )
    lines = [head]
    if res["diagnostics"]:
        if res["passed"] and res["actual"] == "yellow":
            lines.append("       reason(s) for yellow (expected):")
        elif not res["passed"]:
            lines.append("       MISMATCH — possible cause(s):")
        for k, v in res["diagnostics"].items():
            lines.append(f"         - {k}: {v}")
    return "\n".join(lines)


def run_standalone(module_name):
    module = importlib.import_module(module_name) if isinstance(module_name, str) else module_name
    # When called as __main__, importlib can't re-import; use sys.modules.
    if isinstance(module_name, str) and module_name == "__main__":
        module = sys.modules["__main__"]
    res = evaluate(module)
    print(format_result(res))
    sys.exit(0 if res["passed"] else 1)
