import math
from mhslog import *
C1 = (305, -59, -104)
def dist(p): return math.sqrt((p["x"]-C1[0])**2 + (p["y"]-C1[1])**2 + (p["z"]-C1[2])**2)
def sessions(T):
    out, cur = [], []
    for r in T:
        if r["et"] == "gameStartEvent" and cur:
            out.append(cur); cur = []
        cur.append(r)
    if cur: out.append(cur)
    return out
print("session | buffered | minDist(crate1) | posSamples<=25u | Interact presses while <=25u | 10:205 | 11:1 | crateOBJ | 10:16 | Q16state")
for name in ALL_NAMES + list(CONTROLS):
    T = load_any(name)["timed"]
    for S in sessions(T):
        u3 = [r for r in S if r["scene"] == "Unit 3 Dev"]
        if not u3: continue
        if not any(r["key"] == "questActiveEvent:16" for r in u3) and not any(dlg(r).startswith("DialogueNodeEvent:10:") for r in u3): continue
        pos = [r for r in u3 if r["et"] == "PlayerPositionEvent"]
        buf = sum(1 for r in u3 if lagged(r)) / len(u3)
        if not pos: continue
        dmin = min(dist(r["data"]["position"]) for r in pos)
        near = [r for r in pos if dist(r["data"]["position"]) <= 25]
        # interacts within 6 s of a near position sample
        near_ts = [r["ts"] for r in near]
        inter = [r for r in u3 if r["et"] == "InputEvent" and r["data"].get("actionType") == "Interact"]
        ni = sum(1 for r in inter if any(abs((r["ts"] - t).total_seconds()) <= 6 for t in near_ts))
        has = lambda k: sum(1 for r in u3 if dlg(r) == "DialogueNodeEvent:" + k)
        nobj = sum(1 for r in u3 if r["et"] == "ObjectInterEvent" and "Crate" in str(r["data"].get("actionType")))
        st = "fin" if any(r["key"] == "questFinishEvent:16" for r in u3) else ("act" if any(r["key"] == "questActiveEvent:16" for r in u3) else "-")
        print(f"{name[:22]:22s} {u3[0]['ts'].strftime('%m-%d %H:%M')} | {buf:4.0%} | {dmin:7.1f} | {len(near):3d} | {ni:3d} | {has('10:205')} | {has('11:1')} | {nobj} | {has('10:16')} | {st}")
