"""Print a narrative window: python window.py <name> <start_i> <end_i> [--pos] [--all]"""
import sys, json
from mhslog import *
from dlgdb import txt, CONVS

NOISE_INPUT = {"Move", "Jump", "Sprint", "Hoverboard", "Ascend", "Descend"}

def narrate(T, a, b, show_pos=False, show_all=False, out=print):
    buf = []
    def flush():
        if buf:
            kinds = {}
            for r in buf:
                k = r["data"].get("actionType") + ("/D" if r["data"].get("playerOrDrone") == "Drone" else "")
                kinds[k] = kinds.get(k, 0) + 1
            out(f'{"":>6} {buf[0]["ts"].strftime("%H:%M:%S")}-{buf[-1]["ts"].strftime("%H:%M:%S")}   ... {len(buf)} inputs {kinds}')
            buf.clear()
    pos_last = None
    prev = None
    for r in T[a:b + 1]:
        et = r["et"]
        if prev is not None:
            gap = (r["ts"] - prev).total_seconds()
            if gap > 120:
                flush(); out(f'        ---- gap {gap/60:.1f} min ----')
        prev = r["ts"]
        if not show_all and et in ("PuzzlePieceVisibleEvent", "gameWindowFocusEvent", "gameWindowUnfocusEvent"):
            continue
        if et == "PlayerPositionEvent":
            if show_pos:
                flush(); out(fmt(r))
            continue
        if et == "InputEvent" and r["data"].get("actionType") in NOISE_INPUT and not show_all:
            buf.append(r); continue
        flush()
        line = fmt(r, 120)
        if et == "DialogueEvent" and r["data"].get("dialogueEventType") == "DialogueNodeEvent":
            c, n = cn(r)
            line += "  «" + txt(c, n, 80) + "»"
        elif et == "DialogueEvent":
            line += f'  [{CONVS.get(r["data"].get("conversationId"), "?")}]'
        out(line)
    flush()

if __name__ == "__main__":
    name, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    T = load_any(name)["timed"]
    narrate(T, a, min(b, len(T) - 1), "--pos" in sys.argv, "--all" in sys.argv)
