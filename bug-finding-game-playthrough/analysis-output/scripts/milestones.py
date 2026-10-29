"""Per-student milestone timeline: sessions, scene changes, quests, EndOfUnit, DEBUG menu, crashes, gaps."""
import collections, sys, json
from mhslog import *

targets = sys.argv[1:] or [SHORT[f] for f in FILES]
for f in FILES:
    if SHORT[f] not in targets:
        continue
    L = load(f)
    T = L["timed"]
    print("=" * 110)
    print(SHORT[f])
    prev_scene = None
    prev_ts = None
    for r in T:
        et = r["et"]
        gap = (r["ts"] - prev_ts).total_seconds() if prev_ts else 0
        show = False
        tag = ""
        if r["scene"] != prev_scene:
            show, tag = True, f"SCENE {prev_scene} -> {r['scene']}"
        if et in ("questEvent", "EndOfUnit", "gameStartEvent", "DEBUGMenu", "crash"):
            show = True
        if gap > 600:
            print(f"        ---- gap {gap/60:.1f} min ----")
        if show:
            print(fmt(r, 140), ("   <" + tag + ">") if tag else "")
        prev_scene = r["scene"]
        prev_ts = r["ts"]
    for r in L["untimed"]:
        print("   UNTIMED", r["et"], json.dumps(r["data"])[:200], "server", r["sts"])
