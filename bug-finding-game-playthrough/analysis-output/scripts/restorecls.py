"""For every reload: restore type vs. whether the preceding session's records were buffered (offline)."""
from mhslog import *
def sessions(T):
    out, cur = [], []
    for r in T:
        if r["et"] == "gameStartEvent" and cur:
            out.append(cur); cur = []
        cur.append(r)
    if cur: out.append(cur)
    return out
for name in ALL_NAMES:
    T = load_any(name)["timed"]
    S = sessions(T)
    state = {}
    for k, s in enumerate(S):
        # restore = quest events in first 20 s after first gameplay-scene record
        g = [r for r in s if r["scene"] not in ("MainMenu", "Transition")]
        if k > 0 and g:
            t0 = g[0]["ts"]
            em = [r["key"].replace("questActiveEvent:", "A").replace("questFinishEvent:", "F") for r in g if r["et"] == "questEvent" and (r["ts"] - t0).total_seconds() <= 20]
            prev = S[k - 1]
            pg = [r for r in prev if r["scene"] not in ("MainMenu", "Transition")]
            if pg:
                last_q = [r["key"].replace("questActiveEvent:", "A").replace("questFinishEvent:", "F") for r in pg if r["et"] == "questEvent"][-3:]
                buf = sum(lagged(r, 60) for r in pg) / len(pg)
                tail = pg[-20:]
                tailbuf = sum(lagged(r, 60) for r in tail) / len(tail)
                same_scene = pg[-1]["scene"] == g[0]["scene"]
                if em or last_q:
                    print(f"{name[:20]:20s} {g[0]['ts'].strftime('%m-%d %H:%M')} {g[0]['scene'][:22]:22s} restored={em} | prev lastQ={last_q} prevBuffered={buf:.0%} prevTailBuffered={tailbuf:.0%} sameScene={same_scene}")
