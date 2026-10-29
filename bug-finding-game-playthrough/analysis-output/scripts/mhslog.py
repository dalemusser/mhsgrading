"""Shared loader for the bug-forensics pass. Read-only on the source logs.

Paths are relative to this file: logs in ../../players-logs-met-bugs, controls in
../../../playthrough-logs-and-results. Parsed logs are cached (pickle) in the system
temp directory, never next to the source logs.
"""
import json, os, pickle, tempfile
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LOGDIR = os.path.normpath(os.path.join(HERE, "..", "..", "players-logs-met-bugs"))
CACHE = os.path.join(tempfile.gettempdir(), "mhs-bug-forensics-cache")
os.makedirs(CACHE, exist_ok=True)

FILES = sorted(f for f in os.listdir(LOGDIR) if f.endswith(".json"))
SHORT = {f: f.replace(".stratalog.logdata.json", "") for f in FILES}


def parse_ts(s):
    if not s:
        return None
    s = s.rstrip("Z")
    if "." in s:
        a, b = s.split(".")
        s = a + "." + b[:6]
    try:
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
    except Exception:
        return None


def load(fname):
    """Return list of dict records sorted by client timestamp (tiebreak _id).
    Records without a timestamp (crash) get ts=None and are kept separately."""
    short = SHORT.get(fname, fname)
    cp = os.path.join(CACHE, short + ".pkl")
    if os.path.exists(cp):
        with open(cp, "rb") as fh:
            return pickle.load(fh)
    with open(os.path.join(LOGDIR, fname), encoding="utf-8") as fh:
        raw = json.load(fh)
    recs = []
    for r in raw:
        ts = parse_ts(r.get("timestamp"))
        sts = parse_ts((r.get("serverTimestamp") or {}).get("$date"))
        recs.append({
            "oid": r["_id"]["$oid"],
            "ts": ts,
            "sts": sts,
            "et": r.get("eventType"),
            "scene": r.get("sceneName"),
            "ver": r.get("version"),
            "uid": r.get("user_id"),
            "key": r.get("eventKey"),
            "data": r.get("data") or {},
            "dev": r.get("device") or {},
        })
    timed = [r for r in recs if r["ts"] is not None]
    untimed = [r for r in recs if r["ts"] is None]
    timed.sort(key=lambda r: (r["ts"], r["oid"]))
    for i, r in enumerate(timed):
        r["i"] = i
    out = {"timed": timed, "untimed": untimed, "n_raw": len(raw)}
    with open(cp, "wb") as fh:
        pickle.dump(out, fh)
    return out


def cn(r):
    """(conv, node) for a DialogueNodeEvent, preferring eventKey (data payload is stale in buffered uploads)."""
    k = r.get("key")
    if k and k.startswith("DialogueNodeEvent:"):
        _, c, n = k.split(":")
        return int(c), int(n)
    d = r["data"]
    return d.get("conversationId"), d.get("nodeId")


def dlg(r):
    d = r["data"]
    if r["et"] == "DialogueEvent":
        if d.get("dialogueEventType") == "DialogueNodeEvent":
            c, n = cn(r)
            return f"DialogueNodeEvent:{c}:{n}"
        return f'{d.get("dialogueEventType","")}:{d.get("conversationId","")}:'
    return ""


def lagged(r, s=60):
    return r["sts"] is not None and (r["sts"] - r["ts"]).total_seconds() > s


def brief(r, maxlen=160):
    d = dict(r["data"])
    et = r["et"]
    if et == "DialogueEvent":
        et_ = d.get("dialogueEventType", "")
        et_ = et_[:-5] if et_.endswith("Event") else et_
        if et_ == "DialogueNode":
            c, n = cn(r)
            s = f"DialogueNode {c}:{n}"
        else:
            s = f'{et_} {d.get("conversationId","")}:' + ("(buffered)" if lagged(r) else "")
        rest = {k: v for k, v in d.items() if k not in ("dialogueEventType", "conversationId", "nodeId")}
        if rest:
            s += " " + json.dumps(rest, ensure_ascii=False)
    elif et == "questEvent":
        s = r["key"] or json.dumps(d)
    elif et == "PlayerPositionEvent":
        p = d.get("position", {})
        s = f'pos x={p.get("x",0):.1f} y={p.get("y",0):.1f} z={p.get("z",0):.1f}'
    else:
        s = json.dumps(d, ensure_ascii=False)
    s = s.replace("\n", " ")
    return s[:maxlen]


def fmt(r, maxlen=160):
    t = r["ts"].strftime("%m-%d %H:%M:%S.%f")[:-3] if r["ts"] else "NO-TS"
    return f'{r.get("i","-"):>6} {t} | {str(r["scene"])[:26]:<26} | {r["et"][:22]:<22} | {brief(r, maxlen)}'


MEANINGFUL_EXCLUDE = {"PlayerPositionEvent", "PuzzlePieceVisibleEvent", "gameWindowFocusEvent", "gameWindowUnfocusEvent"}


def meaningful(recs):
    return [r for r in recs if r["et"] not in MEANINGFUL_EXCLUDE]


# Internal successful playthroughs on the same "20260914-" version string, used as controls.
CTRL_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "..", "playthrough-logs-and-results"))
CONTROLS = {
    "ctrl.091426-3": os.path.join(CTRL_DIR, "09-14-26-3", "wenyi091426-3.stratalog.logdata.json"),
    "ctrl.092326": os.path.join(CTRL_DIR, "09-23-26", "wenyi09232026.stratalog.logdata.json"),
}


def load_any(name):
    """name = student short name or control key."""
    if name in CONTROLS:
        cp = os.path.join(CACHE, name + ".pkl")
        if os.path.exists(cp):
            return pickle.load(open(cp, "rb"))
        with open(CONTROLS[name], encoding="utf-8") as fh:
            raw = json.load(fh)
        recs = []
        for r in raw:
            recs.append({"oid": r["_id"]["$oid"], "ts": parse_ts(r.get("timestamp")),
                         "sts": parse_ts((r.get("serverTimestamp") or {}).get("$date")),
                         "et": r.get("eventType"), "scene": r.get("sceneName"), "ver": r.get("version"),
                         "uid": r.get("user_id"), "key": r.get("eventKey"), "data": r.get("data") or {},
                         "dev": r.get("device") or {}})
        timed = sorted([r for r in recs if r["ts"]], key=lambda r: (r["ts"], r["oid"]))
        for i, r in enumerate(timed):
            r["i"] = i
        out = {"timed": timed, "untimed": [r for r in recs if not r["ts"]], "n_raw": len(raw)}
        pickle.dump(out, open(cp, "wb"))
        return out
    for f in FILES:
        if SHORT[f] == name:
            return load(f)
    raise KeyError(name)


ALL_NAMES = [SHORT[f] for f in FILES]
