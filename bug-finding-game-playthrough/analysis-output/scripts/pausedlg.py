"""Pause presses during an open conversation: did the conversation continue?"""
import csv
from mhslog import *
from dlgdb import EXPORT
rows = list(csv.reader(open(EXPORT, encoding="utf-8-sig")))
li = [i for i, r in enumerate(rows) if r and r[0] == "OutgoingLinks"][0]
OUT = {}
for r in rows[li + 3:]:
    if r and len(r) >= 4:
        OUT.setdefault((int(r[0]), int(r[1])), []).append((int(r[2]), int(r[3])))
res = []
for name in ALL_NAMES + list(CONTROLS):
    T = load_any(name)["timed"]
    for k, r in enumerate(T):
        if r["et"] != "InputEvent" or r["data"].get("actionType") != "Pause" or lagged(r):
            continue
        # last dialogue node before pause within 20 s
        prev = None
        for j in range(k - 1, max(0, k - 300), -1):
            if T[j]["et"] == "DialogueEvent":
                prev = T[j]; break
        if not prev or (r["ts"] - prev["ts"]).total_seconds() > 20 or prev["data"].get("dialogueEventType") != "DialogueNodeEvent":
            continue
        c, n = cn(prev)
        has_out = bool([x for x in OUT.get((c, n), []) if x[0] != -1])
        # next dialogue event after pause
        nxt = next((T[j] for j in range(k + 1, min(len(T), k + 400)) if T[j]["et"] == "DialogueEvent"), None)
        gap = (nxt["ts"] - r["ts"]).total_seconds() if nxt else None
        cont = nxt is not None and gap is not None and gap < 30 and (nxt["data"].get("dialogueEventType") in ("DialogueNodeEvent", "DialogueFinishEvent"))
        res.append((name, r["ts"], f"{c}:{n}", has_out, dlg(nxt) if nxt else None, gap, cont))
for x in res:
    print(f"{x[0][:22]:22s} {x[1].strftime('%m-%d %H:%M:%S')} lastNode={x[2]:7s} nodeHasOutLinks={x[3]!s:5s} next={x[4]} after {x[5] if x[5] is None else round(x[5],1)}s continued<30s={x[6]}")
