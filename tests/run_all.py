"""
Run every per-point grading test against the shipped log dump and compare the
production color to the expected dashboard color.

Usage:
    python run_all.py            # run all 26 points, print table + diagnostics
    python run_all.py --quiet    # table only (no per-reason diagnostics)

The point order and expected colors come from the project spec:
    Green, Green, Yellow, Green,                 (U1 P1-4)
    Green, Yellow, Green, Green, Green, Green, Yellow,   (U2 P1-7)
    Green, Green, Yellow, Green, Green,          (U3 P1-5)
    Green, Green, Green, Green, Green, Green,     (U4 P1-6)
    Green, Green, Green, Green                    (U5 P1-4)
"""

import importlib
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from mhs_harness import load_collection, default_player_id
from mhs_report import evaluate, format_result

# (module name, expected color) in dashboard order.
POINTS = [
    ("test_u1p1", "green"),
    ("test_u1p2", "green"),
    ("test_u1p3", "yellow"),
    ("test_u1p4", "green"),
    ("test_u2p1", "green"),
    ("test_u2p2", "yellow"),
    ("test_u2p3", "green"),
    ("test_u2p4", "green"),
    ("test_u2p5", "green"),
    ("test_u2p6", "green"),
    ("test_u2p7", "yellow"),
    ("test_u3p1", "green"),
    ("test_u3p2", "green"),
    ("test_u3p3", "yellow"),
    ("test_u3p4", "green"),
    ("test_u3p5", "green"),
    ("test_u4p1", "green"),
    ("test_u4p2", "green"),
    ("test_u4p3", "green"),
    ("test_u4p4", "green"),
    ("test_u4p5", "green"),
    ("test_u4p6", "green"),
    ("test_u5p1", "green"),
    ("test_u5p2", "green"),
    ("test_u5p3", "green"),
    ("test_u5p4", "green"),
]

EXPECTED_LIST = [c for _, c in POINTS]


def _arg_value(flag):
    if flag in sys.argv:
        i = sys.argv.index(flag)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return None


def main():
    quiet = "--quiet" in sys.argv
    # Point at a different log dump for a new weekly build: --log PATH
    log_path = _arg_value("--log")
    coll = load_collection(log_path)
    pid = default_player_id(coll)
    print(f"Loaded {len(coll.docs)} log records | player = {pid}\n")

    results = []
    for mod_name, expected in POINTS:
        module = importlib.import_module(mod_name)
        # The expected color lives in each module's META; assert the runner's
        # list agrees with it so the two never drift apart.
        assert module.META["expected"].lower() == expected, (
            f"{mod_name}: META expected {module.META['expected']} != runner {expected}"
        )
        res = evaluate(module, coll, pid)
        results.append(res)

    # Table
    print(f"{'POINT':<7} {'ACTIVITY':<42} {'EXP':<7} {'GOT':<7} RESULT")
    print("-" * 78)
    for res in results:
        pt = f"U{res['unit']}P{res['point']}"
        tag = "PASS" if res["passed"] else "**FAIL**"
        name = (res["name"][:40] + "..") if len(res["name"]) > 42 else res["name"]
        print(f"{pt:<7} {name:<42} {res['expected']:<7} {res['actual']:<7} {tag}")

    passed = sum(1 for r in results if r["passed"])
    failed = [r for r in results if not r["passed"]]
    print("-" * 78)
    print(f"\nSummary: {passed}/{len(results)} points match the expected dashboard color.")

    actual_seq = ", ".join(r["actual"].capitalize() for r in results)
    expected_seq = ", ".join(c.capitalize() for c in EXPECTED_LIST)
    print(f"\nExpected: {expected_seq}")
    print(f"Actual:   {actual_seq}")

    # Diagnostics: always show for yellow points (the reason) and for any FAIL.
    if not quiet:
        interesting = [r for r in results if r["diagnostics"]]
        if interesting:
            print("\n" + "=" * 78)
            print("DIAGNOSTICS (reasons for yellow / causes of mismatch)")
            print("=" * 78)
            for res in interesting:
                print(format_result(res))
                print()

    if failed:
        print("=" * 78)
        print(f"{len(failed)} MISMATCH(ES) — production color != expected:")
        for r in failed:
            print(f"  - U{r['unit']}P{r['point']} ({r['name']}): "
                  f"expected {r['expected']}, production gave {r['actual']}")
        print("These points' production color logic (or the log data feeding them) "
              "should be reviewed.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
