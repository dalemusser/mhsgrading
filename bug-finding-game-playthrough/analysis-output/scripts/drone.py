"""Drone-phase reconstruction: from 23:42 (launch) to next gameStart / Unit-3 scene / Q25 finish."""
import sys
from mhslog import *
from dlgdb import txt
for name in (sys.argv[1:] or ALL_NAMES + list(CONTROLS)):
    T = load_any(name)["timed"]
    starts = [r["i"] for r in T if dlg(r) == "DialogueNodeEvent:23:42"]
    print("=" * 100); print(name, "launches at", [T[i]["ts"].strftime("%m-%d %H:%M:%S") for i in starts])
    for s in starts:
        seq = []
        last = s
        for r in T[s:]:
            if r["et"] == "gameStartEvent" or r["key"] == "questFinishEvent:25" or not (r["scene"] or "").startswith("Unit 2"):
                seq.append(f'  END: {r["et"]} {r["key"] or ""} {r["scene"]} {r["ts"].strftime("%m-%d %H:%M:%S")}')
                break
            last = r["i"]
            if r["et"] == "ObjectInterEvent":
                seq.append(f'  {r["ts"].strftime("%H:%M:%S")} OBJ {r["data"].get("actionType")} | {r["data"].get("objectName")}')
            elif r["et"] == "DialogueEvent" and r["data"].get("dialogueEventType") == "DialogueNodeEvent":
                c, n = cn(r)
                if c in (18, 20, 19, 21, 23, 27):
                    seq.append(f'  {r["ts"].strftime("%H:%M:%S")} DLG {c}:{n} «{txt(c, n, 70)}»')
            elif r["et"] in ("questEvent", "TopographicMapEvent", "DaniEvent", "chatEvent", "DEBUGMenu"):
                seq.append(f'  {r["ts"].strftime("%H:%M:%S")} {r["et"]} {r["key"] or json.dumps(r["data"])[:80]}')
        # count inputs drone vs player
        W = T[s:last + 1]
        nd = sum(1 for r in W if r["et"] == "InputEvent" and r["data"].get("playerOrDrone") == "Drone")
        npl = sum(1 for r in W if r["et"] == "InputEvent" and r["data"].get("playerOrDrone") == "Player")
        print(f" launch {T[s]['ts'].strftime('%H:%M:%S')}: drone inputs={nd} player inputs={npl} duration={(W[-1]['ts']-W[0]['ts']).total_seconds()/60:.1f}min")
        # compress repeated identical lines
        prev = None; rep = 0
        for line in seq:
            core = line[11:] if line.startswith("  ") and line[2:10].count(":") == 2 else line
            if core == prev:
                rep += 1; continue
            if rep:
                print(f"      (x{rep+1})"); rep = 0
            print(line); prev = core
        if rep: print(f"      (x{rep+1})")
