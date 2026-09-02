"""Phase 3 — reconcile every dialogue-based grading/rubric reference against
the dialogue databases and the current playthrough.

For each (conversationId, nodeId) referenced by production grading logic or
the source documents:
  1. resolve its text in Dialogue-ID-Texts.xlsx        (historical mapping)
  2. resolve its text in 2026-06-10-MHSDialogueExport  (freshest dialogue DB)
  3. compare the two texts (same ID → same dialogue?)
  4. check whether the key fired in the audited playthrough
  5. if the ID vanished from the export, look for the same text elsewhere
     (relocation candidates are *reported*, never silently substituted)

Outputs: outputs/dialogue-reconciliation.json / .csv
"""

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib

STATUSES = [
    "EXACT_MATCH",
    "TEXT_MATCH_DIFFERENT_ID",
    "ID_EXISTS_DIFFERENT_TEXT",
    "EXPECTED_DIALOGUE_NOT_OBSERVED",
    "DIALOGUE_REMOVED_OR_CHANGED",
    "AMBIGUOUS",
    "NOT_APPLICABLE",
]


def effective_export_text(entry):
    if not entry:
        return ""
    return entry.get("dialogue_text") or entry.get("menu_text") or ""


def main():
    lib.utf8_stdout()
    cfg = lib.load_config()
    min_chars = int(cfg.get("text_match_min_chars", 15))

    deps = lib.read_json(lib.out_path(cfg, "progress-point-dependencies.json"))
    intent = lib.read_json(lib.out_path(cfg, "source-doc-intent.json"))
    inv = lib.read_json(lib.out_path(cfg, "current-log-inventory.json"))

    xlsx = lib.load_dialogue_xlsx(cfg)
    conversations, export = lib.load_dialogue_export(cfg)

    observed = {}
    for key, rec in inv["event_keys"].items():
        kind, conv, node = lib.parse_event_key(key)
        if kind == "dialogue":
            observed[(conv, node)] = rec

    # ---- collect references -------------------------------------------------
    refs = defaultdict(lambda: {"pps": set(), "sources": set(), "roles": set()})
    for pp in deps["progress_points"]:
        for k in pp["all_referenced_event_keys"]:
            kind, conv, node = lib.parse_event_key(k)
            if kind != "dialogue":
                continue
            r = refs[(conv, node)]
            r["pps"].add(pp["pp_id"])
            r["sources"].add("grading")
        for ek in pp["event_keys"]:
            kind, conv, node = lib.parse_event_key(ek["key"])
            if kind == "dialogue":
                refs[(conv, node)]["roles"].add(f"{pp['pp_id']}:{ek['role']}")
    for pp_id, rec in intent["progress_points"].items():
        d = rec.get("progress_points_doc") or {}
        for label, markers in (d.get("markers") or {}).items():
            for mk in markers:
                kind, conv, node = lib.parse_event_key(mk)
                if kind == "dialogue":
                    r = refs[(conv, node)]
                    r["pps"].add(pp_id)
                    r["sources"].add("docs")
                    r["roles"].add(f"{pp_id}:doc-{label}-marker")
        for conv, node in d.get("color_rule_dialogue_tags") or []:
            r = refs[(conv, node)]
            r["pps"].add(pp_id)
            r["sources"].add("docs")
        ea = rec.get("ea_working_doc") or []
        for row in ea:
            for conv, node in row.get("log_tag_dialogue_tags") or []:
                r = refs[(conv, node)]
                r["pps"].add(pp_id)
                r["sources"].add("docs")

    # reverse text index over the export for relocation search
    text_index = defaultdict(list)
    for (conv, node), entry in export.items():
        t = lib.norm_text(effective_export_text(entry))
        if len(t) >= min_chars:
            text_index[t].append((conv, node))

    # ---- classify -----------------------------------------------------------
    rows = []
    for (conv, node), meta in sorted(refs.items()):
        xlsx_text = xlsx.get((conv, node))
        entry = export.get((conv, node))
        export_text = effective_export_text(entry) if entry else None
        in_xlsx = (conv, node) in xlsx
        in_export = entry is not None
        obs = observed.get((conv, node))
        obs_count = obs["count"] if obs else 0

        nx, ne = lib.norm_text(xlsx_text or ""), lib.norm_text(export_text or "")
        if in_xlsx and in_export and nx and ne:
            # xlsx cells are sometimes truncated; accept prefix agreement
            text_agrees = nx == ne or (len(nx) >= min_chars and ne.startswith(nx))
        else:
            # one or both sides blank/missing: no basis for a text verdict
            text_agrees = None

        relocation = []
        if in_xlsx and not in_export and len(nx) >= min_chars:
            for cand in text_index.get(nx, []):
                c_obs = observed.get(cand)
                relocation.append(
                    {"conv": cand[0], "node": cand[1],
                     "observed_count": c_obs["count"] if c_obs else 0}
                )

        evidence = []
        if in_xlsx:
            evidence.append(f"xlsx[{conv},{node}]={ (xlsx_text or '')[:60] !r}")
        if in_export:
            evidence.append(f"export[{conv},{node}]={ (export_text or '')[:60] !r}")
        if obs:
            ex = obs["examples"][0]
            evidence.append(
                f"observed x{obs_count}, e.g. _id={ex['_id']} ts={ex['timestamp']} ({ex['_src']})"
            )

        if not in_xlsx and not in_export:
            # Node-ID gaps are normal in Unity dialogue DBs (deleted nodes
            # leave holes) — a referenced ID in such a gap is a dead key that
            # can never fire in the current dialogue database.
            status = "DIALOGUE_REMOVED_OR_CHANGED"
            note = ("dead reference: not present in the historical xlsx NOR the "
                    "2026-06-10 export — key cannot fire unless the live DB "
                    "differs from both sources")
            confidence = "MEDIUM"
        elif in_export:
            if text_agrees is False:
                status = "ID_EXISTS_DIFFERENT_TEXT"
                note = "xlsx text and 2026-06-10 export text differ for the same ID"
                confidence = "MEDIUM"
            else:
                if obs_count > 0:
                    status = "EXACT_MATCH"
                    note = "ID exists in current dialogue DB and fired in this playthrough"
                    confidence = "HIGH" if text_agrees else "MEDIUM"
                else:
                    status = "EXPECTED_DIALOGUE_NOT_OBSERVED"
                    note = ("ID exists in current dialogue DB but did not fire in this "
                            "playthrough (may be conditional dialogue)")
                    confidence = "MEDIUM"
        else:  # in_xlsx only — gone from the freshest DB export
            if relocation:
                status = "TEXT_MATCH_DIFFERENT_ID"
                note = (f"node absent from 2026-06-10 export but identical text exists at "
                        f"{[(r['conv'], r['node']) for r in relocation]} — candidate remap, NOT auto-applied")
                confidence = "MEDIUM"
            else:
                status = "DIALOGUE_REMOVED_OR_CHANGED"
                note = "node absent from 2026-06-10 export; no text match found elsewhere"
                confidence = "MEDIUM" if len(nx) >= min_chars else "LOW"

        rows.append(
            {
                "conversationId": conv,
                "nodeId": node,
                "event_key": f"DialogueNodeEvent:{conv}:{node}",
                "conversation_title": conversations.get(conv, ""),
                "referenced_by": ";".join(sorted(meta["pps"])),
                "reference_sources": ";".join(sorted(meta["sources"])),
                "roles": ";".join(sorted(meta["roles"])),
                "in_xlsx": in_xlsx,
                "in_export": in_export,
                "xlsx_text": (xlsx_text or "")[:200],
                "export_text": (export_text or "")[:200],
                "text_agrees": text_agrees,
                "observed_count": obs_count,
                "relocation_candidates": relocation,
                "status": status,
                "confidence": confidence,
                "note": note,
                "evidence": evidence,
            }
        )

    out_json = lib.out_path(cfg, "dialogue-reconciliation.json")
    lib.write_json(out_json, {"reference_count": len(rows), "rows": rows})
    out_csv = lib.out_path(cfg, "dialogue-reconciliation.csv")
    lib.write_csv(
        out_csv,
        [
            {**r, "relocation_candidates": ";".join(f"{c['conv']}:{c['node']}(x{c['observed_count']})"
                                                     for c in r["relocation_candidates"]),
             "evidence": " || ".join(r["evidence"])}
            for r in rows
        ],
        ["event_key", "conversation_title", "referenced_by", "reference_sources", "roles",
         "in_xlsx", "in_export", "text_agrees", "observed_count", "status", "confidence",
         "xlsx_text", "export_text", "relocation_candidates", "note", "evidence"],
    )

    from collections import Counter

    by_status = Counter(r["status"] for r in rows)
    print(f"Wrote {out_json}")
    print(f"Wrote {out_csv} ({len(rows)} dialogue references)")
    for s in STATUSES:
        if by_status.get(s):
            print(f"  {s:<32} {by_status[s]}")


if __name__ == "__main__":
    main()
