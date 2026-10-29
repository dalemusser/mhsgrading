"""Every session that reloads straight into 'Which Watershed?' (questActiveEvent:25 within 15 s of a
gameStartEvent): which dialogue nodes replay, whether conversation 21 finishes, whether the Classifier
conversation (8) ever starts, and how many InputEvents follow."""
from mhslog import *

print("frozen post-reload Q25 sessions:")
for nm in ALL_NAMES:
    T = load_any(nm)["timed"]
    for k, r in enumerate(T):
        if r["key"] != "questActiveEvent:25" or k == 0:
            continue
        j = k - 1
        while j > 0 and T[j]["et"] != "gameStartEvent" and (r["ts"] - T[j]["ts"]).total_seconds() < 15:
            j -= 1
        if T[j]["et"] != "gameStartEvent":
            continue
        e = next((q["i"] for q in T[k:] if q["et"] == "gameStartEvent"), len(T) - 1)
        S = T[k:e]
        nodes = [dlg(q)[18:] for q in S if q["et"] == "DialogueEvent" and q["data"].get("dialogueEventType") == "DialogueNodeEvent"]
        n51 = next((q for q in S if dlg(q) == "DialogueNodeEvent:21:51"), None)
        fin = None
        if n51:
            fin = next((q for q in S if q["et"] == "DialogueEvent" and q["data"].get("dialogueEventType") == "DialogueFinishEvent" and q["ts"] >= n51["ts"]), None)
        conv8 = sum(1 for q in S if dlg(q).startswith("DialogueNodeEvent:8:"))
        inp = sum(1 for q in S if q["et"] == "InputEvent")
        pos = [q["data"]["position"] for q in S if q["et"] == "PlayerPositionEvent"]
        lp = pos[-1] if pos else {"x": 0, "y": 0, "z": 0}
        print(f"  {nm[:22]:22s} load {r['ts']:%m-%d %H:%M:%S} nodes={nodes} "
              + (f"Finish+{(fin['ts'] - n51['ts']).total_seconds():.1f}s" if fin else "noFinish")
              + f" conv8Nodes={conv8} inputs={inp} len={(S[-1]['ts'] - r['ts']).total_seconds() / 60:.1f}min"
              + f" lastPos=({lp['x']:.0f},{lp['y']:.0f},{lp['z']:.0f}) buffered={sum(lagged(q) for q in S)}/{len(S)}")
