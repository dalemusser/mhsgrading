"""'Saving Cadet Anderson' (quest 36): conversation-82 node sequence per player, with fountain interaction,
Pause presses, reloads and Anderson-Base scene entry marked."""
from mhslog import *

for name in ALL_NAMES + list(CONTROLS):
    T = load_any(name)["timed"]
    a = [r["i"] for r in T if r["key"] == "questActiveEvent:36"]
    if not a:
        continue
    i = a[0]
    f = next((r["i"] for r in T if r["key"] == "questFinishEvent:36"), len(T) - 1)
    seq = []
    for r in T[i:f + 1]:
        if r["et"] == "DialogueEvent" and r["data"].get("dialogueEventType") == "DialogueNodeEvent":
            c, n = cn(r)
            if c == 82:
                seq.append(str(n))
        elif r["et"] == "ObjectInterEvent" and "fountain" in str(r["data"]).lower():
            seq.append("FOUNTAIN")
        elif r["et"] == "gameStartEvent":
            seq.append("|RELOAD|")
        elif r["et"] == "InputEvent" and r["data"].get("actionType") == "Pause":
            seq.append("PAUSE")
        elif r["et"] == "questEvent" and r["key"] in ("questActiveEvent:36", "questFinishEvent:36"):
            seq.append(r["key"].replace("questActiveEvent:", "A").replace("questFinishEvent:", "F"))
        elif r["et"] == "DEBUGMenu" and r["scene"] == "Unit 4 Dev - Anderson Base" and seq and seq[-1] != "BASE":
            seq.append("BASE")
    print(f"{name[:22]:22s} {T[i]['ts']:%m-%d %H:%M} -> {T[f]['ts']:%m-%d %H:%M} "
          f"buffered={sum(lagged(r) for r in T[i:f + 1])}/{f - i + 1}: {' '.join(seq)[:330]}")
