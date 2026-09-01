"""Phase 1a — parse the 26 production grading markdown files into a
machine-readable dependency specification.

Output: outputs/progress-point-dependencies.json

The production script fence is treated as *currently implemented behavior*
(the audit object), never as ground truth. For every dependency we record
where it came from (event-keys table / production fence / header), its role,
and its expectation class from config/dependency-semantics.yaml.
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib

STRICT_DLG = re.compile(r"DialogueNodeEvent:\d+:\d+")
STRICT_QST = re.compile(r"quest(?:Active|Finish)Event:\d+")
FILE_RE = re.compile(r"mhs-unit(\d+)-point(\d+)-grading\.md$")


def _section(text, heading_re):
    """Return the body of the first section whose heading matches, up to the
    next heading of the same-or-higher level or a --- rule."""
    m = re.search(heading_re, text)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r"\n(?:#{1,3} |---\s*\n)", text[start:])
    return text[start: start + nxt.start()] if nxt else text[start:]


def _first_fence(section):
    if not section:
        return None
    m = re.search(r"```(?:js|javascript|python)?\s*\n(.*?)```", section, re.S)
    return m.group(1) if m else None


def _keys_in(text):
    if not text:
        return []
    return sorted(set(STRICT_DLG.findall(text)) | set(STRICT_QST.findall(text)))


def _window_part(raw):
    """Parse '- **Start:** Previous `X` (exclusive)' fragments.

    `key` is only set when the backticked token is a real eventKey
    (DialogueNodeEvent/questEvent). Anchors described in prose (e.g. the
    2026-09-01 U4P1/U4P2 eventType+data soil-key-close anchor) keep raw only —
    a stray backticked word like `Finished` must not become a phantom anchor."""
    if raw is None:
        return None
    m = re.search(r"(Previous|Latest|First)?\s*`([^`]+)`\s*\((exclusive|inclusive)\)?", raw)
    if not m or not (STRICT_DLG.fullmatch(m.group(2)) or STRICT_QST.fullmatch(m.group(2))):
        return {"raw": raw}
    return {
        "raw": raw,
        "which": (m.group(1) or "").lower() or None,
        "key": m.group(2),
        "bound": m.group(3),
    }


def parse_file(path, semantics):
    fn = os.path.basename(path)
    m = FILE_RE.search(fn)
    unit, point = int(m.group(1)), int(m.group(2))
    pp_id = f"U{unit}P{point}"
    text = open(path, encoding="utf-8").read()

    activity = None
    ma = re.search(r"\*\*Activity:\*\*\s*(.+)", text)
    if ma:
        activity = ma.group(1).strip()

    trig_start = trig_end = None
    ms = re.search(r"\*\*Trigger\(Start\) Event:\*\*\s*`([^`]+)`", text)
    me = re.search(r"\*\*Trigger\(End\) Event:\*\*\s*`([^`]+)`", text)
    if ms:
        trig_start = ms.group(1)
    if me:
        trig_end = me.group(1)

    # Grading rule prose: first non-empty paragraph after '## Grading Rule'
    rule_sec = _section(text, r"## Grading Rule\s*\n")
    rule_prose = None
    outcome_rows = []
    if rule_sec:
        for para in rule_sec.split("\n\n"):
            p = para.strip()
            if p and not p.startswith("|") and not p.startswith(">"):
                rule_prose = re.sub(r"\s+", " ", p)
                break
        for line in rule_sec.split("\n"):
            mm = re.match(r"\|\s*\*\*(\w+)\*\*\s*\|\s*(.+?)\s*\|\s*$", line)
            if mm:
                outcome_rows.append({"outcome": mm.group(1), "condition": mm.group(2)})

    # Attempt window
    win = None
    mw = re.search(
        r"### Attempt Window \(Production\)\s*\n+- \*\*Start:\*\* (.*?)\n- \*\*End:\*\* (.*?)\n",
        text,
    )
    if mw:
        win = {"start": _window_part(mw.group(1)), "end": _window_part(mw.group(2))}

    # Event Keys table
    ek_sec = _section(text, r"## Event Keys\s*\n")
    event_keys = []
    if ek_sec:
        for line in ek_sec.split("\n"):
            mm = re.match(r"\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$", line)
            if not mm:
                continue
            role, keycell = mm.group(1), mm.group(2)
            if role in ("Role",) or set(role) <= set("-: "):
                continue
            key = keycell.strip("`").strip()
            kind = lib.parse_event_key(key)[0] if (STRICT_DLG.match(key) or STRICT_QST.match(key)) else "other"
            expectation = (
                semantics.get("pp_overrides", {}).get(pp_id, {}).get(key)
                or semantics["role_semantics"].get(role, "counted_evidence")
            )
            event_keys.append(
                {"role": role, "key": key, "kind": kind, "expectation": expectation}
            )

    # Production script (main section only — reason-code fences are separate)
    prod_sec = _section(text, r"## Production Script[^\n]*\n")
    prod_code = _first_fence(prod_sec)
    prod_keys = _keys_in(prod_code)

    # Resolve `const NAME = "literal";` so filters written via variables
    # (eventType: EVENT_TYPE, "data.X": START_STATUS) are captured too.
    consts = dict(re.findall(r'const\s+([A-Za-z_]\w*)\s*=\s*"([^"]*)"', prod_code or ""))

    def _resolve(tok):
        tok = tok.strip()
        if tok.startswith('"') and tok.endswith('"'):
            return tok[1:-1]
        return consts.get(tok)

    prod_event_types = sorted(
        {v for v in (_resolve(t) for t in re.findall(r"eventType:\s*([^,\n}]+)", prod_code or "")) if v}
    )
    data_filters = set()
    for field, raw in re.findall(r'"data\.([\w ]+)":\s*([^,\n}]+)', prod_code or ""):
        val = _resolve(raw)
        if val is not None:
            data_filters.add((field, val))
    for field, val in re.findall(r'data\.([\w ]+?)\s*===\s*"([^"]*)"', prod_code or ""):
        data_filters.add((field, val))
    data_filters = sorted(data_filters)
    data_fields = sorted(
        {f for f, _ in data_filters}
        | set(re.findall(r'"data\.([\w ]+)"\s*:', prod_code or ""))
        | set(re.findall(r"\.data\.(\w+)", prod_code or ""))
    )

    # Analytics script keys (for doc-vs-production comparisons)
    ana_sec = _section(text, r"## Analytics Script\s*\n")
    ana_keys = _keys_in(_first_fence(ana_sec))

    reason_codes = re.findall(r"### ([A-Z][A-Z0-9_]+)\s*\n", text)

    all_keys = sorted(
        set(prod_keys)
        | {ek["key"] for ek in event_keys if ek["kind"] != "other"}
        | ({trig_start} if trig_start else set())
        | ({trig_end} if trig_end else set())
    )

    return {
        "pp_id": pp_id,
        "alt_ids": [f"U{unit}.C{point}"],
        "unit": unit,
        "point": point,
        "activity": activity,
        "grading_file": os.path.relpath(path, lib.REPO_ROOT).replace("\\", "/"),
        "trigger_start": trig_start,
        "trigger_end": trig_end,
        "grading_rule_prose": rule_prose,
        "outcome_table": outcome_rows,
        "attempt_window": win,
        "event_keys": event_keys,
        "production": {
            "has_script": prod_code is not None,
            "event_keys": prod_keys,
            "event_types": prod_event_types,
            "data_filters": [{"field": f, "value": v} for f, v in data_filters],
            "data_fields": data_fields,
            "script": prod_code,
        },
        "analytics_event_keys": ana_keys,
        "reason_codes": reason_codes,
        "all_referenced_event_keys": all_keys,
        "warnings": [],
    }


def main():
    lib.utf8_stdout()
    cfg = lib.load_config()
    import yaml

    with open(os.path.join(lib.AUDIT_DIR, "config", "dependency-semantics.yaml"), encoding="utf-8") as f:
        semantics = yaml.safe_load(f)

    files = sorted(
        glob.glob(os.path.join(lib.repo_path(cfg["grading_dir"]), "mhs-unit*-point*-grading.md"))
    )
    specs = []
    for path in files:
        spec = parse_file(path, semantics)
        # sanity warnings
        if not spec["production"]["has_script"]:
            spec["warnings"].append("no Production Script fence found")
        if spec["attempt_window"] is None and spec["unit"] != 1 and spec["pp_id"] not in ("U2P2", "U2P3"):
            spec["warnings"].append("no Attempt Window block found")
        table_keys = {ek["key"] for ek in spec["event_keys"] if ek["kind"] != "other"}
        missing_from_table = [k for k in spec["production"]["event_keys"] if k not in table_keys
                              and k not in (spec["trigger_start"], spec["trigger_end"])]
        if missing_from_table:
            spec["warnings"].append(
                f"production script uses keys absent from Event Keys table: {missing_from_table}"
            )
        specs.append(spec)

    specs.sort(key=lambda s: (s["unit"], s["point"]))
    out = lib.out_path(cfg, "progress-point-dependencies.json")
    lib.write_json(out, {"generated_from": cfg["grading_dir"], "progress_points": specs})
    print(f"Wrote {out} ({len(specs)} progress points)")
    for s in specs:
        flag = " !! " + "; ".join(s["warnings"]) if s["warnings"] else ""
        print(
            f"  {s['pp_id']:<5} keys(table)={len(s['event_keys']):>2} "
            f"keys(prod)={len(s['production']['event_keys']):>2} "
            f"eventTypes={s['production']['event_types']}{flag}"
        )


if __name__ == "__main__":
    main()
