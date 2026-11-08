#!/usr/bin/env python3
"""How much of a classroom export is affected by the September stale-payload issue?

Definition (same as the audit's `stale_risk_records`): a game record on a build
without the delivery envelope (no `session_id`) whose serverTimestamp - timestamp
exceeds STALE_DELAY_S. Crash reports have no client timestamp and are excluded.

Writes one CSV per view (student, unit, event type) and prints the validation
figures: direct eventKey-vs-payload checks, the puzzle `data.timestamp` check,
whether a later same-type record existed before upload, and threshold/clock
sensitivity.

With --keyed-unaffected, records that carry an eventKey (DialogueEvent nodes and
questEvent) are counted as unaffected, because the key holds their identity.

Usage:
    python build-log-qa/scripts/stale_payload_impact.py --input <export.jsonl> --out <dir> [--keyed-unaffected]
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

STALE_DELAY_S = 5.0  # same value as mhs_log_audit.field_quality.STALE_DELAY_S


def scene_to_units(scene):
    """Same rule as mhs_log_audit.config.scene_to_units."""
    return [int(m) for m in re.findall(r"[Uu]nit\s*(\d+)", scene or "")]


def parse_ts(s):
    if not isinstance(s, str) or not s:
        return np.nan
    s = s.rstrip("Z")
    if "." in s:
        head, frac = s.split(".")
        s = head + "." + (frac + "000000")[:6]
    try:
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc).timestamp()
    except ValueError:
        return np.nan


def to_int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def key_matches(et, key, d):
    """Does `data` agree with eventKey? None when the record has no usable key."""
    if not key or not isinstance(d, dict):
        return None
    parts = key.split(":")
    if et == "DialogueEvent" and parts[0] == "DialogueNodeEvent" and len(parts) == 3:
        return (to_int(parts[1]), to_int(parts[2])) == (to_int(d.get("conversationId")), to_int(d.get("nodeId")))
    if et == "questEvent" and len(parts) >= 2:
        return to_int(parts[1]) == to_int(d.get("questID"))
    return None


def load(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            d = r.get("data")
            et = r.get("eventType")
            legacy = "session_id" not in r
            sts = parse_ts((r.get("serverTimestamp") or {}).get("$date"))
            rows.append((
                bool(r.get("eventKey")), r["user_id"], et, r.get("sceneName"), r.get("version"), legacy,
                parse_ts(r.get("timestamp")), sts,
                hashlib.md5(json.dumps(d, sort_keys=True).encode()).hexdigest()[:12] if legacy and et != "crash" else None,
                key_matches(et, r.get("eventKey"), d) if legacy else None,
                parse_ts(d.get("timestamp")) if et == "PuzzlePieceVisibleEvent" and isinstance(d, dict) else np.nan,
                f'{d.get("timestamp")}|{d.get("pieceId")}|{d.get("actionType")}'
                if et == "PuzzlePieceVisibleEvent" and legacy and isinstance(d, dict) else None,
            ))
    return pd.DataFrame(rows, columns=["has_key", "uid", "et", "scene", "ver", "legacy", "ts", "sts",
                                       "dhash", "key_ok", "dts", "ptriple"])


def pct(a, b):
    return round(100 * a / b, 2) if b else np.nan


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--keyed-unaffected", action="store_true",
                    help="count records with an eventKey as not affected")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    raw = load(a.input)
    n_crash = int((raw.et == "crash").sum())
    df = raw[raw.et != "crash"].copy()
    df["delay"] = df.sts - df.ts
    df["late"] = df.legacy & (df.delay > STALE_DELAY_S)
    df["flag"] = df.late & ~df.has_key if a.keyed_unaffected else df.late
    df["unit"] = df.scene.map(lambda s: (lambda u: f"Unit {u[0]}" if len(u) == 1 else "No unit (menu, transition, cutscene)")(scene_to_units(s or "")))
    df["created"] = df.uid.map(lambda u: datetime.fromtimestamp(int(u[:8], 16), timezone.utc).strftime("%Y-%m-%d"))

    # Was a later record of the same type written before this one reached the server?
    df = df.sort_values(["uid", "et", "ts"], kind="stable")
    g = df.groupby(["uid", "et"], sort=False)
    nxt = g.ts.shift(-1)
    df["exposed"] = nxt.notna() & (nxt <= df.sts)
    leg = df[df.legacy].copy()
    leg["same_prev"] = leg.dhash == leg.groupby(["uid", "et"], sort=False).dhash.shift(1)

    # ---- by student ----------------------------------------------------------
    s = df.groupby("uid").agg(account_created=("created", "first"), records=("et", "size"),
                              sept_records=("legacy", "sum"), late=("late", "sum"), flagged=("flag", "sum"))
    s["pct_of_all_records"] = (100 * s.flagged / s.records).round(2)
    s["pct_of_sept_records"] = (100 * s.flagged / s.sept_records.where(s.sept_records > 0)).round(2)
    s["over_1_day_late"] = df[df.flag & (df.delay > 86400)].groupby("uid").size().reindex(s.index, fill_value=0)
    s = s.sort_values("pct_of_all_records", ascending=False)
    s.to_csv(out / "by_student.csv")

    # ---- by unit -------------------------------------------------------------
    def unit_row(x):
        per = x.groupby("uid").flag.agg(["sum", "size"])
        return pd.Series({
            "records": len(x), "sept_records": int(x.legacy.sum()), "late": int(x.late.sum()), "flagged": int(x.flag.sum()),
            "pct_of_all_records": pct(x.flag.sum(), len(x)), "pct_of_sept_records": pct(x.flag.sum(), x.legacy.sum()),
            "students_played": len(per), "students_flagged": int((per["sum"] > 0).sum()),
            "student_units_1_to_10pct": int(((100 * per["sum"] / per["size"] >= 1) & (100 * per["sum"] / per["size"] < 10)).sum()),
            "student_units_10pct_plus": int((100 * per["sum"] / per["size"] >= 10).sum()),
        })
    u = df.groupby("unit").apply(unit_row, include_groups=False)
    tot = unit_row(df).rename("All records")
    pd.concat([u, tot.to_frame().T]).to_csv(out / "by_unit.csv")
    uc = df.groupby(["created", "unit"]).apply(unit_row, include_groups=False)
    uc.to_csv(out / "by_unit_and_account_group.csv")

    # ---- by event type -------------------------------------------------------
    rows = []
    for et, x in df.groupby("et"):
        l = leg[leg.et == et]
        lf, lo = l[l.late], l[~l.late]
        rows.append({
            "event_type": et, "records": len(x), "sept_records": len(l), "late": int(x.late.sum()),
            "keyed_records": int(x.has_key.sum()), "flagged": int(x.flag.sum()),
            "pct_of_all_records": pct(x.flag.sum(), len(x)), "pct_of_sept_records": pct(x.flag.sum(), len(l)),
            "share_of_all_flagged": pct(x.flag.sum(), df.flag.sum()),
            "students_flagged": l[l.flag].uid.nunique(),
            "flagged_with_later_same_type_before_upload": int(l[l.flag].exposed.sum()),
            "distinct_payloads_on_sept": l.dhash.nunique(),
            "repeat_prev_payload_on_time": round(lo.same_prev.mean(), 3) if len(lo) else np.nan,
            "repeat_prev_payload_late": round(lf.same_prev.mean(), 3) if len(lf) else np.nan,
            "keyed_late": int(lf.key_ok.notna().sum()), "keyed_late_wrong": int((lf.key_ok == False).sum()),  # noqa: E712
            "keyed_on_time": int(lo.key_ok.notna().sum()), "keyed_on_time_wrong": int((lo.key_ok == False).sum()),  # noqa: E712
        })
    e = pd.DataFrame(rows).sort_values("flagged", ascending=False)
    e.to_csv(out / "by_event_type.csv", index=False)

    # ---- printed summary -----------------------------------------------------
    pd.set_option("display.width", 250, "display.max_columns", 40, "display.max_rows", 200)
    print(f"records {len(raw):,}  game {len(df):,}  crash excluded {n_crash}  students {df.uid.nunique()}")
    print(f"sept records {int(df.legacy.sum()):,}; students on Sept {leg.uid.nunique()}; flagged {int(df.flag.sum()):,}; "
          f"students flagged {(s.flagged > 0).sum()}")
    print("non-envelope versions:", leg.ver.value_counts().to_dict())
    print(f"flagged % all {pct(df.flag.sum(), len(df))}; % Sept {pct(df.flag.sum(), df.legacy.sum())}")

    print("\n-- per student, % of all records")
    p = s.pct_of_all_records
    print(p.describe().round(2).to_dict())
    print("flagged-only:", p[s.flagged > 0].describe().round(2).to_dict())
    bins = {"none: never on Sept": int((s.sept_records == 0).sum()),
            "none: on Sept, no flagged": int(((s.sept_records > 0) & (s.flagged == 0)).sum()),
            "only keyed late records": int(((s.late > 0) & (s.flagged == 0)).sum()),
            ">0-<0.1": int(((s.flagged > 0) & (p < .1)).sum()), "0.1-<1": int(((p >= .1) & (p < 1)).sum()),
            "1-<5": int(((p >= 1) & (p < 5)).sum()), "5-<10": int(((p >= 5) & (p < 10)).sum()), "10+": int((p >= 10).sum())}
    print(bins)
    print(s.groupby("account_created").agg(students=("flagged", "size"), any_flagged=("flagged", lambda v: (v > 0).sum()),
                                           sept=("sept_records", "sum"), records=("records", "sum"), flagged=("flagged", "sum"),
                                           median_pct=("pct_of_all_records", "median"), max_pct=("pct_of_all_records", "max"),
                                           over_1pct=("pct_of_all_records", lambda v: (v >= 1).sum())))
    print("top 10\n", s.head(10)[["records", "sept_records", "flagged", "pct_of_all_records", "pct_of_sept_records"]])
    print("median pct of Sept records (flagged students):", s[s.flagged > 0].pct_of_sept_records.median(),
          "max", s.pct_of_sept_records.max())

    print("\n-- by unit\n", pd.concat([u, tot.to_frame().T]).to_string())
    print("\n-- by unit x group\n", uc[["records", "sept_records", "flagged", "pct_of_all_records", "pct_of_sept_records", "students_played", "students_flagged"]].to_string())
    print("\n-- by event type\n", e.to_string())

    print("\n-- exposure: flagged with later same-type before upload:", int(df[df.flag].exposed.sum()), "of", int(df.flag.sum()))
    constant = set(e[e.distinct_payloads_on_sept <= 1].event_type)
    print("constant-payload types:", sorted(constant), "flagged in them:", int(df[df.flag & df.et.isin(constant)].shape[0]))
    fx = df[df.flag & df.exposed & ~df.et.isin(constant)]
    print("flagged, exposed, payload can vary:", len(fx), "students", fx.uid.nunique())

    pz = leg[leg.et == "PuzzlePieceVisibleEvent"].copy()
    pz["ahead"] = pz.dts - pz.ts
    grp = pz.groupby(["uid", "ptriple"]).ts
    pz["span"] = grp.transform("max") - grp.transform("min")
    pz["copied"] = (pz.ahead > .02) & (pz.span > .02)
    for nm, x in (("flagged", pz[pz.flag]), ("on time", pz[~pz.flag])):
        print(f"puzzle {nm}: n={len(x):,} payload time >20ms after record time={(x.ahead > .02).sum():,} ({(x.ahead > .02).mean():.1%}); "
              f"identical payload also on a different-time record={x.copied.sum():,} ({x.copied.mean():.1%})")

    print("\n-- sensitivity")
    for th in (5, 10, 30, 60, 300, 3600, 86400):
        x = leg[(leg.delay > th) & (~leg.has_key if a.keyed_unaffected else True)]
        print(f">{th}s: {len(x):,} records ({pct(len(x), len(df))}% of all), {x.uid.nunique()} students")
    leg["day"] = pd.to_datetime(leg.ts, unit="s").dt.date
    off = leg.groupby(["uid", "day"]).delay.transform("median")
    corr = off.where(off.abs() < 30, 0.0)   # a median beyond 30 s is a late-upload day, not a clock offset
    still = ((leg.delay - corr) > STALE_DELAY_S) & (~leg.has_key if a.keyed_unaffected else True)
    print("clock-corrected flagged:", int(still.sum()), "; lost:", int((leg.flag & ~still).sum()),
          "; gained:", int((~leg.flag & still).sum()))
    ud = leg.groupby(["uid", "day"]).delay.median()
    print("user-days", len(ud), "with |offset| 2-30 s:", int(((ud.abs() > 2) & (ud.abs() < 30)).sum()), "with median >=30 s:", int((ud >= 30).sum()))
    ok = df[~df.legacy]
    print("fixed builds: late >5s", int((ok.delay > 5).sum()), "; keyed mismatches: see load (legacy only)")


if __name__ == "__main__":
    main()
