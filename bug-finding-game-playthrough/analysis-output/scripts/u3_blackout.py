"""Unit-3 sessions that load with Supply Run (quest 16) re-activated: dialogue-event count, Interact presses,
closest approach to Tera's camp. A 'blackout' = zero DialogueEvents for the whole session."""
import math, collections
from mhslog import *

TERA = (330, 175)   # x, z of Tera's camp (where 10:16 fires in every log)


def sessions(T):
    out, cur = [], []
    for r in T:
        if r["et"] == "gameStartEvent" and cur:
            out.append(cur); cur = []
        cur.append(r)
    if cur:
        out.append(cur)
    return out


for name in ALL_NAMES:
    T = load_any(name)["timed"]
    for S in sessions(T):
        u3 = [r for r in S if r["scene"] == "Unit 3 Dev"]
        if not u3 or not any(r["key"] == "questActiveEvent:16" for r in u3[:30]):
            continue
        d = [r for r in u3 if r["et"] == "DialogueEvent"]
        pos = [r["data"]["position"] for r in u3 if r["et"] == "PlayerPositionEvent"]
        dt = min((math.hypot(p["x"] - TERA[0], p["z"] - TERA[1]) for p in pos), default=None)
        inter = sum(1 for r in u3 if r["et"] == "InputEvent" and r["data"].get("actionType") == "Interact")
        first = [(r["ts"].strftime("%H:%M:%S"), dlg(r)[18:] or r["data"].get("conversationId")) for r in d[:4]]
        print(f"{name[:22]:22s} {u3[0]['ts']:%m-%d %H:%M} dur={(u3[-1]['ts'] - u3[0]['ts']).total_seconds() / 60:5.1f}m "
              f"dialogueEvents={len(d):3d} interacts={inter:3d} minDistTera={dt and round(dt)} first={first}")
