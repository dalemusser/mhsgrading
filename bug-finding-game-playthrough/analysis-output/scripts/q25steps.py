"""Detect 'Which Watershed?' (quest 25) milestones per session for each player."""
import sys
from mhslog import *

STEPS = [
    ("Q25act", lambda r: r["key"] == "questActiveEvent:25"),
    ("ClsIntro8:12", lambda r: dlg(r) == "DialogueNodeEvent:8:12"),
    ("Cls26pos", lambda r: dlg(r) == "DialogueNodeEvent:26:141"),
    ("Cls26neg", lambda r: dlg(r) == "DialogueNodeEvent:26:138"),
    ("Cls26:136done", lambda r: dlg(r) == "DialogueNodeEvent:26:136"),
    ("18:121retrained", lambda r: dlg(r) == "DialogueNodeEvent:18:121"),
    ("18:130", lambda r: dlg(r) == "DialogueNodeEvent:18:130"),
    ("Anderson19:32", lambda r: dlg(r) == "DialogueNodeEvent:19:32"),
    ("Tera21:76", lambda r: dlg(r) == "DialogueNodeEvent:21:76"),
    ("Jasper23:38", lambda r: dlg(r) == "DialogueNodeEvent:23:38"),
    ("Drone23:42", lambda r: dlg(r) == "DialogueNodeEvent:23:42"),
    ("scanOcean", lambda r: r["et"] == "ObjectInterEvent" and r["data"].get("objectName") == "Eastern Ocean"),
    ("scanE*", lambda r: r["et"] == "ObjectInterEvent" and str(r["data"].get("objectName", "")).startswith("Eastern River")),
    ("scanW*", lambda r: r["et"] == "ObjectInterEvent" and str(r["data"].get("objectName", "")).startswith("Western River")),
    ("18:169table", lambda r: dlg(r) == "DialogueNodeEvent:18:169"),
    ("18:284", lambda r: dlg(r) == "DialogueNodeEvent:18:284"),
    ("Toppo20:35", lambda r: dlg(r) == "DialogueNodeEvent:20:35"),
    ("20:43/44/45", lambda r: dlg(r) in ("DialogueNodeEvent:20:43", "DialogueNodeEvent:20:44", "DialogueNodeEvent:20:45")),
    ("20:46", lambda r: dlg(r) == "DialogueNodeEvent:20:46"),
    ("20:63argOpen", lambda r: dlg(r) == "DialogueNodeEvent:20:63"),
    ("argSessOpen", lambda r: r["et"] == "argumentationEvent" and "Close" not in str(r["data"].get("actionType", ""))),
    ("argSubmit", lambda r: r["et"] == "argumentationAnswerEvent"),
    ("argSessClose", lambda r: r["et"] == "argumentationEvent" and "Close" in str(r["data"].get("actionType", ""))),
    ("27:x", lambda r: dlg(r).startswith("DialogueNodeEvent:27:") and dlg(r) != "DialogueNodeEvent:27:0"),
    ("27:7ok", lambda r: dlg(r) == "DialogueNodeEvent:27:7"),
    ("Q25fin", lambda r: r["key"] == "questFinishEvent:25"),
    ("20:64", lambda r: dlg(r) == "DialogueNodeEvent:20:64"),
    ("Q54act", lambda r: r["key"] == "questActiveEvent:54"),
    ("Q54fin", lambda r: r["key"] == "questFinishEvent:54"),
    ("EOU2", lambda r: r["et"] == "EndOfUnit" and r["data"].get("Unit") == "2"),
]

def sessions(T):
    """split at gameStartEvent"""
    out, cur = [], []
    for r in T:
        if r["et"] == "gameStartEvent" and cur:
            out.append(cur); cur = []
        cur.append(r)
    if cur: out.append(cur)
    return out

def run(name):
    T = load_any(name)["timed"]
    first = next((r["i"] for r in T if r["key"] == "questActiveEvent:25"), None)
    if first is None:
        print(name, "no quest 25"); return
    u2 = [r for r in T[first:] if (r["scene"] or "").startswith("Unit 2") or r["scene"] in ("MainMenu", "Transition")]
    # stop at first Unit 3+ scene
    end = next((r["i"] for r in T[first:] if (r["scene"] or "").startswith(("Unit 3", "Unit 4", "Unit 5"))), T[-1]["i"] + 1)
    W = T[first - 50:end]
    print("=" * 100); print(name, "Q25 window idx", first, "->", end - 1, T[first]["ts"], "->", T[end - 1]["ts"])
    for s_i, S in enumerate(sessions(W)):
        hits = []
        for lab, fn in STEPS:
            rs = [r for r in S if fn(r)]
            if rs:
                hits.append(f"{lab}x{len(rs)}@{rs[0]['ts'].strftime('%H:%M:%S')}" if len(rs) > 1 else f"{lab}@{rs[0]['ts'].strftime('%H:%M:%S')}")
        print(f" sess{s_i} {S[0]['ts'].strftime('%m-%d %H:%M')}–{S[-1]['ts'].strftime('%H:%M')} n={len(S)}: " + ", ".join(hits))

if __name__ == "__main__":
    for n in (sys.argv[1:] or ALL_NAMES + list(CONTROLS)):
        run(n)
