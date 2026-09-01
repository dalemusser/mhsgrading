"""Phase 1b — extract per-progress-point assessment intent from the two
source documents:

  * Progress-Points.docx           (PP name/description/color rules/log marks)
  * MHS-2.0-Embedded-Assessment-Working-Doc.docx  (topic/task/score formulas)

Output: outputs/source-doc-intent.json

These documents carry the *assessment intent*. Their technical identifiers
(dialogue tags, quest IDs) are historical claims to be verified — they are
extracted verbatim plus parsed into structured references, never assumed
current.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib

PP_ID_RE = re.compile(r"^U(\d)\.C(\d)\b")

# quest marker inside a log-mark cell, tolerating the docs' loose quoting
QUEST_MARK_RE = re.compile(
    r"quest(?:EventType)?[^A-Za-z]{0,6}.{0,4}(questActiveEvent|questFinishEvent)"
    r".{0,40}?questID[^0-9]{0,6}(\d+)",
    re.S,
)
DLG_MARK_RE = re.compile(
    r"conversationId[^0-9]{0,6}(\d+)[^0-9]{1,20}nodeId[^0-9]{0,6}(\d+)", re.S
)
EVENTKEY_RE = re.compile(r"(DialogueNodeEvent:\d+:\d+|quest(?:Active|Finish)Event:\d+)")
# 'conv-node' dialogue tags like 70-7, 68-29; also "70-33|25" variants
PAIR_RE = re.compile(r"\b(\d{1,3})-(\d{1,3})(?:\|(\d{1,3}))?\b")


def parse_markers(cell):
    """Parse a Progress Log Mark cell into structured start/end markers."""
    if not cell:
        return {}
    out = {}
    # Split on Start:/End: labels when present
    parts = re.split(r"\b(Start|End)\s*:", cell)
    if len(parts) >= 3:
        for label, body in zip(parts[1::2], parts[2::2]):
            markers = []
            for m in QUEST_MARK_RE.finditer(body):
                markers.append(f"{m.group(1)}:{m.group(2)}")
            for m in DLG_MARK_RE.finditer(body):
                markers.append(f"DialogueNodeEvent:{m.group(1)}:{m.group(2)}")
            for m in EVENTKEY_RE.finditer(body):
                if m.group(1) not in markers:
                    markers.append(m.group(1))
            out[label.lower()] = markers
    return out


def dialogue_pairs(cell, known_convs):
    """Extract conv-node dialogue tags from a cell, keeping only pairs whose
    conversation ID is a known conversation (filters out '3-4 attempts')."""
    pairs = []
    for m in PAIR_RE.finditer(cell or ""):
        conv, node = int(m.group(1)), int(m.group(2))
        if conv in known_convs:
            pairs.append([conv, node])
            if m.group(3):
                pairs.append([conv, int(m.group(3))])
    # dedupe, keep order
    seen, out = set(), []
    for p in pairs:
        t = tuple(p)
        if t not in seen:
            seen.add(t)
            out.append(p)
    return out


def parse_progress_points_docx(cfg, known_convs):
    path = lib.repo_path(cfg["progress_points_docx"])
    items = lib.docx_paragraphs(path)
    tables = lib.docx_tables(path)
    # unit heading immediately precedes its table in document order
    unit_for_table = {}
    current_unit = None
    for kind, val in items:
        if kind == "p":
            m = re.match(r"^Unit\s+(\d)\b", val or "")
            if m:
                current_unit = int(m.group(1))
        elif kind == "tbl":
            unit_for_table[val] = current_unit

    pps = {}
    extras = []
    for ti, rows in enumerate(tables):
        unit = unit_for_table.get(ti)
        for row in rows:
            cells = [c.strip() for c in row]
            if not cells or not cells[0]:
                continue
            m = PP_ID_RE.match(cells[0])
            if not m:
                if cells[0] and not cells[0].startswith("Name"):
                    extras.append({"table": ti, "unit": unit, "row_head": cells[0][:60]})
                continue
            u, c = int(m.group(1)), int(m.group(2))
            pp_id = f"U{u}P{c}"
            cells += [""] * (8 - len(cells))
            rec = {
                "doc_id": cells[0],
                "unit": u,
                "name": cells[1],
                "description": cells[2],
                "checkpoint": cells[3],
                "color_determination": cells[4],
                "progress_log_mark_raw": cells[5],
                "ea_color_log_mark_raw": cells[6],
                "arg_attempt_log_mark_raw": cells[7],
                "markers": parse_markers(cells[5]),
                "color_rule_dialogue_tags": dialogue_pairs(cells[6], known_convs),
            }
            pps[pp_id] = rec
    return pps, extras


def parse_ea_docx(cfg, known_convs):
    path = lib.repo_path(cfg["ea_working_doc_docx"])
    tables = lib.docx_tables(path)
    recs = {}
    extras = []
    for rows in tables:
        for row in rows:
            cells = [c.strip() for c in row]
            if not cells or not cells[0]:
                continue
            m = PP_ID_RE.match(cells[0])
            if not m:
                if cells[0] not in ("Checkpoint",):
                    extras.append({"row_head": cells[0][:60]})
                continue
            u, c = int(m.group(1)), int(m.group(2))
            pp_id = f"U{u}P{c}"
            cells += [""] * (8 - len(cells))
            recs.setdefault(pp_id, []).append(
                {
                    "doc_id": cells[0],
                    "ea_item": cells[1],
                    "topic": cells[2],
                    "task": cells[3],
                    "dashboard": cells[4],
                    "student_action_scoring": cells[5],
                    "log_tag_raw": cells[6],
                    "score_formula_raw": cells[7],
                    "log_tag_dialogue_tags": dialogue_pairs(cells[6], known_convs),
                }
            )
    return recs, extras


def main():
    lib.utf8_stdout()
    cfg = lib.load_config()
    conversations, _entries = lib.load_dialogue_export(cfg)
    known_convs = set(conversations)

    pp_intent, pp_extras = parse_progress_points_docx(cfg, known_convs)
    ea_intent, ea_extras = parse_ea_docx(cfg, known_convs)

    merged = {}
    for pp_id in sorted(set(pp_intent) | set(ea_intent)):
        merged[pp_id] = {
            "progress_points_doc": pp_intent.get(pp_id),
            "ea_working_doc": ea_intent.get(pp_id),
        }

    out = lib.out_path(cfg, "source-doc-intent.json")
    lib.write_json(
        out,
        {
            "sources": {
                "progress_points_docx": cfg["progress_points_docx"],
                "ea_working_doc_docx": cfg["ea_working_doc_docx"],
            },
            "progress_points": merged,
            "unmatched_rows": {"progress_points_docx": pp_extras, "ea_doc": ea_extras},
        },
    )
    print(f"Wrote {out}")
    print(f"  Progress-Points.docx rows: {len(pp_intent)} PPs (+{len(pp_extras)} non-PP rows)")
    print(f"  EA working doc rows: {len(ea_intent)} PPs (+{len(ea_extras)} non-PP rows)")
    missing_pp = [k for k in merged if not merged[k]["progress_points_doc"]]
    missing_ea = [k for k in merged if not merged[k]["ea_working_doc"]]
    if missing_pp:
        print(f"  WARN: no Progress-Points row for {missing_pp}")
    print(f"  (EA doc typically covers scored points only; not in EA doc: {missing_ea})")
    for pp_id, rec in sorted(merged.items()):
        d = rec["progress_points_doc"]
        if d:
            print(
                f"  {pp_id:<5} {d['name'][:34]:<36} markers={d['markers']} "
                f"tags={d['color_rule_dialogue_tags'][:6]}{'...' if len(d['color_rule_dialogue_tags'])>6 else ''}"
            )


if __name__ == "__main__":
    main()
