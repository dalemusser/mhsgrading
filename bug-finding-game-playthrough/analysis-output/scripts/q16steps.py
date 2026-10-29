"""Detect 'Supply Run' (quest 16) milestones per Unit-3 session."""
import sys
from mhslog import *

def D(k): return lambda r: dlg(r) == "DialogueNodeEvent:" + k
STEPS = [
    ("10:1amb", D("10:1")), ("10:224vid", D("10:224")), ("10:4talk", D("10:4")), ("10:15deal", D("10:15")),
    ("Q16act", lambda r: r["key"] == "questActiveEvent:16"), ("10:16", D("10:16")),
    ("10:206wrongway", D("10:206")), ("10:207", D("10:207")), ("10:205upstream", D("10:205")),
    ("11:1crateDANI", D("11:1")), ("11:10", D("11:10")), ("11:11map", D("11:11")),
    ("OBJ:PlaceOnHoverboard", lambda r: r["et"] == "ObjectInterEvent" and "Hoverboard" in str(r["data"].get("actionType"))),
    ("OBJ:GrabCrate", lambda r: r["et"] == "ObjectInterEvent" and "Grab Crate" in str(r["data"].get("actionType"))),
    ("OBJ:other", lambda r: r["et"] == "ObjectInterEvent" and "Crate" not in str(r["data"].get("actionType"))),
    ("10:29coming", D("10:29")), ("10:30ok", D("10:30")), ("10:31wrong", D("10:31")), ("10:32wrongLast", D("10:32")),
    ("10:195", D("10:195")), ("11:22", D("11:22")), ("10:198", D("10:198")), ("Q16fin", lambda r: r["key"] == "questFinishEvent:16"),
    ("Q17act", lambda r: r["key"] == "questActiveEvent:17"), ("DEVconv12", lambda r: dlg(r).startswith("DialogueNodeEvent:12:")),
]

def sessions(T):
    out, cur = [], []
    for r in T:
        if r["et"] == "gameStartEvent" and cur:
            out.append(cur); cur = []
        cur.append(r)
    if cur: out.append(cur)
    return out

for name in (sys.argv[1:] or ALL_NAMES + list(CONTROLS)):
    T = load_any(name)["timed"]
    print("=" * 100); print(name)
    for S in sessions(T):
        u3 = [r for r in S if r["scene"] == "Unit 3 Dev"]
        if not u3: continue
        # stop at first Q17 activation in this session to keep it focused
        hits = []
        for lab, fn in STEPS:
            rs = [r for r in u3 if fn(r)]
            if rs:
                hits.append(f"{lab}x{len(rs)}" if len(rs) > 1 else lab)
        lagfrac = sum(1 for r in u3 if lagged(r)) / len(u3)
        print(f" {u3[0]['ts'].strftime('%m-%d %H:%M')}-{u3[-1]['ts'].strftime('%H:%M')} n={len(u3)} buffered={lagfrac:.0%}: " + ", ".join(hits))
