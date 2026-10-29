"""Hung-conversation scan: a DialogueNode whose node has outgoing links, followed by >=60 s with NO further
DialogueEvent while the player keeps producing >=10 InputEvents and the session continues (no gameStart)."""
import csv
from mhslog import *
from dlgdb import EXPORT
rows = list(csv.reader(open(EXPORT, encoding="utf-8-sig")))
li = [i for i, r in enumerate(rows) if r and r[0] == "OutgoingLinks"][0]
OUT = {}
for r in rows[li + 3:]:
    if r and len(r) >= 4:
        OUT.setdefault((int(r[0]), int(r[1])), []).append((int(r[2]), int(r[3])))
for name in ALL_NAMES + list(CONTROLS):
    T = load_any(name)["timed"]
    hits = []
    for k, r in enumerate(T):
        if not (r["et"] == "DialogueEvent" and r["data"].get("dialogueEventType") == "DialogueNodeEvent"):
            continue
        c, n = cn(r)
        outs = [x for x in OUT.get((c, n), []) if x[0] != -1]
        if not outs:
            continue
        # find next dialogue event
        nxt = None; inputs = 0; interacts = 0; restart = False
        for j in range(k + 1, len(T)):
            q = T[j]
            if q["et"] == "gameStartEvent" or q["scene"] != r["scene"]:
                break
            if q["et"] == "DialogueEvent":
                nxt = q; break
            if q["et"] == "InputEvent":
                inputs += 1
                if q["data"].get("actionType") == "Interact": interacts += 1
        end_t = (nxt or T[min(j, len(T) - 1)])["ts"]
        silence = (end_t - r["ts"]).total_seconds()
        if silence >= 60 and inputs >= 10:
            hits.append((r["ts"].strftime("%m-%d %H:%M:%S"), r["scene"][:18], f"{c}:{n}", outs[:3], round(silence / 60, 1), inputs, interacts, dlg(nxt)[18:] if nxt else "session-end", "BUF" if lagged(r) else ""))
    print("==", name, len(hits))
    for h in hits: print("   ", h)
