"""Dialogue export lookup: (conv,node) -> dict(title,text,cond,script); conv -> title.

Reads the Unity Dialogue System export kept in the grading repo (2026-09-21, aligned with build 20260914-).
"""
import csv, os, pickle, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
EXPORT = os.path.normpath(os.path.join(HERE, "..", "..", "..", "grading-logic",
                                       "original-score-rubric-table-and-dialogue-database",
                                       "2026-09-21-MHSDialogueExport.csv"))
CACHE = os.path.join(tempfile.gettempdir(), "mhs-bug-forensics-cache")
os.makedirs(CACHE, exist_ok=True)


def _load():
    cp = os.path.join(CACHE, "dlg.pkl")
    if os.path.exists(cp):
        return pickle.load(open(cp, "rb"))
    rows = list(csv.reader(open(EXPORT, encoding="utf-8-sig")))
    convs, nodes = {}, {}
    sec = None
    hdr = None
    for row in rows:
        if not row:
            continue
        if row[0] in ("Conversations", "DialogueEntries", "Actors", "Items", "Locations", "Variables", "OutgoingLinks", "Database", "Global User Script"):
            sec = row[0]; hdr = None; continue
        if sec == "Conversations":
            if row[0] == "ID": hdr = row; continue
            if row[0] == "Number": continue
            if hdr and row[0].isdigit():
                convs[int(row[0])] = row[1]
        elif sec == "DialogueEntries":
            if row[0] == "entrytag": hdr = row; continue
            if row[0] == "Text": continue
            if hdr and len(row) > 12:
                d = dict(zip(hdr, row))
                try:
                    nodes[(int(d["ConvID"]), int(d["ID"]))] = {"title": d["Title"], "menu": d["MenuText"], "text": d["DialogueText"], "cond": d["Conditions"], "script": d["Script"]}
                except ValueError:
                    pass
        elif sec == "OutgoingLinks":
            pass
    out = (convs, nodes)
    pickle.dump(out, open(cp, "wb"))
    return out
CONVS, NODES = _load()
def txt(c, n, maxlen=90):
    d = NODES.get((int(c), int(n)))
    if not d:
        return "<not in export>"
    t = d["text"] or d["menu"] or ("[" + d["title"] + "]")
    return t.replace("\n", " ")[:maxlen]
