"""At every gameStartEvent->gameplay scene load, compare tracked quest state before the reload with
quest events emitted in the first 15 s after the scene loads."""
import sys
from mhslog import *

def run(name, verbose=True):
    T = load_any(name)["timed"]
    state = {}   # quest -> 'active'/'finished'
    rows = []
    i = 0
    n = len(T)
    while i < n:
        r = T[i]
        if r["et"] == "gameStartEvent":
            # find scene load
            j = i + 1
            while j < n and (T[j]["scene"] in ("MainMenu", "Transition")) and T[j]["et"] != "gameStartEvent":
                j += 1
            if j >= n or T[j]["et"] == "gameStartEvent":
                i = j if j < n else n; continue
            load_r = T[j]
            t0 = load_r["ts"]
            emitted = []
            k = j
            while k < n and (T[k]["ts"] - t0).total_seconds() <= 15 and T[k]["et"] != "gameStartEvent":
                if T[k]["et"] == "questEvent":
                    emitted.append(T[k]["key"].replace("questActiveEvent:", "A").replace("questFinishEvent:", "F"))
                k += 1
            active_before = sorted([q for q, s in state.items() if s == "active"], key=int)
            # classify
            reacts = [e[1:] for e in emitted if e.startswith("A")]
            regress = [q for q in reacts if state.get(q) == "finished"]
            unit_before = None
            rows.append((load_r["ts"], load_r["scene"], active_before, emitted, regress))
            # don't skip; continue scanning from j so emitted quest events also update state
            i = j
            continue
        if r["et"] == "questEvent":
            q = r["data"].get("questID") or r["key"].split(":")[1]
            state[q] = "active" if "Active" in r["key"] else "finished"
        i += 1
    if verbose:
        print("=" * 100); print(name)
        for ts, sc, ab, em, rg in rows:
            flag = ("  REGRESS(finished->re-activated): " + ",".join(rg)) if rg else ""
            print(f'  {ts.strftime("%m-%d %H:%M:%S")} load {sc[:24]:<24} activeBefore={ab[-4:]} emitted={em}{flag}')
    return rows

if __name__ == "__main__":
    for nm in (sys.argv[1:] or ALL_NAMES + list(CONTROLS)):
        run(nm)
