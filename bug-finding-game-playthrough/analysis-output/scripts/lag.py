"""Quantify data-vs-eventKey mismatch for DialogueNodeEvents and server-upload lag, per session."""
import collections, statistics
from mhslog import *

def sessions(T):
    out, cur = [], []
    for r in T:
        if r["et"] == "gameStartEvent" and cur:
            out.append(cur); cur = []
        cur.append(r)
    if cur: out.append(cur)
    return out

for name in ALL_NAMES + list(CONTROLS):
    T = load_any(name)["timed"]
    dn = [r for r in T if r["et"] == "DialogueEvent" and r["data"].get("dialogueEventType") == "DialogueNodeEvent"]
    withkey = [r for r in dn if r["key"]]
    mism = [r for r in withkey if r["key"] != f'DialogueNodeEvent:{r["data"].get("conversationId")}:{r["data"].get("nodeId")}']
    # classify mismatches: START pattern (key ends :0) vs other
    start_pat = [r for r in mism if r["key"].endswith(":0")]
    stale = collections.Counter(f'{r["data"].get("conversationId")}:{r["data"].get("nodeId")}' for r in mism if not r["key"].endswith(":0"))
    lags = [(r["sts"] - r["ts"]).total_seconds() for r in T if r["sts"]]
    big = sum(1 for x in lags if x > 300)
    print(f"{name:28s} dlgNodes={len(dn)} withKey={len(withkey)} mismatch={len(mism)} (startPat={len(start_pat)}) staleTop={stale.most_common(3)} | lag>5min: {big}/{len(lags)} median={statistics.median(lags):.1f}s max={max(lags)/3600:.1f}h")
