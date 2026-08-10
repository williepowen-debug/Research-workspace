#!/usr/bin/env python3
"""
warrisk_row_staleness.py — PER-ROW expiry check for workbook/WARRISK.tsv.

WHY THIS EXISTS (2026-08-10 self-audit item 3, Will-approved via PROME):
    Boot step 5a-2 grades the FILE's `# Last real data refresh:` content clock at
    --days 7. That is a FILE-scoped gate, and the risk it protects is LEG-scoped.

    Measured consequence on the day this was written: all five WARRISK rows carried
    `Stale_By = 2026-08-03` and were SEVEN DAYS PAST THEIR OWN DECLARED EXPIRY, and
    three legs had not been refreshed since 2026-07-23 (18 days) —

        * Southern Red Sea      >1%     As_Of 2026-07-23
        * Bab el-Mandeb AWRP    ~0.5%   As_Of 2026-07-23
        * West Coast Saudi      0.1%    As_Of 2026-07-23   <-- the REGISTERED FALSIFIER

    The WC-Saudi row is labelled in the file's own Role column as
    "🎯 REGISTERED FALSIFIER" and described as "the cheapest early warning on the
    whole board" — it prices ORIGIN risk with transit stripped out, i.e. it is the
    leg that would show premium-regime converting to supply-loss regime. It is also
    the leg beneath the derived 75-100x spread that FALCON exported to HAWK's
    cross-war synthesis on 2026-08-10.

    All the attention flowed to the headline Hormuz leg — which IS re-pulled, and
    whose data clock is correctly NOT advanced while no newer primary exists — while
    three legs including the falsifier expired silently behind a green-looking file gate.

    ⇒ A FILE-SCOPED FRESHNESS CHECK CANNOT PROTECT LEG-SCOPED RISK.

WHAT IT DOES NOT DO:
    It does not widen any gate, relax any threshold, or advance any clock. It reads
    and reports. The fix for a stale leg is a RE-PULL, never a wider tolerance.
    Editing this file — or WARRISK.tsv's prose — does not make data fresh.

USAGE:  python3 "$(git rev-parse --show-toplevel)/AGENTS/FALCON/scripts/warrisk_row_staleness.py"
        [--asof YYYY-MM-DD]   # override "today" for testing

EXIT:   0 = every row within its declared Stale_By
        1 = one or more rows PAST their own Stale_By  (advisory — surface at boot)
        2 = file unreadable / schema not as expected
"""
import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path


def repo_root() -> Path:
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=15)
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip())
    except Exception:
        pass
    return Path(__file__).resolve().parents[3]


def parse_date(s: str):
    s = (s or "").strip()
    if not s:
        return None
    # tolerate trailing prose in a date cell, e.g. "2026-07-13 (FALCON's stale carry)"
    head = s[:10]
    try:
        return dt.date.fromisoformat(head)
    except ValueError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", default=None)
    args = ap.parse_args()

    today = parse_date(args.asof) or dt.date.today()
    path = repo_root() / "AGENTS" / "FALCON" / "workbook" / "WARRISK.tsv"

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        print(f"WARRISK per-row check: CANNOT READ {path} — {e}", file=sys.stderr)
        return 2

    rows = [ln for ln in lines if ln.strip() and not ln.lstrip().startswith("#")]
    if not rows:
        print("WARRISK per-row check: no data rows found", file=sys.stderr)
        return 2

    header = rows[0].split("\t")
    try:
        i_metric = header.index("Metric")
        i_leg = header.index("Leg")
        i_val = header.index("Value")
        i_asof = header.index("As_Of")
        i_stale = header.index("Stale_By")
        i_role = header.index("Role")
    except ValueError as e:
        print(f"WARRISK per-row check: unexpected schema — {e}", file=sys.stderr)
        return 2

    expired, ok, undated = [], [], []
    for ln in rows[1:]:
        c = ln.split("\t")
        if len(c) <= i_role:
            continue
        asof = parse_date(c[i_asof])
        stale = parse_date(c[i_stale])
        rec = {
            "leg": c[i_leg].strip(),
            "val": c[i_val].strip(),
            "asof": asof,
            "stale": stale,
            "role": c[i_role].strip(),
            "metric": c[i_metric].strip(),
        }
        if stale is None:
            undated.append(rec)
        elif today > stale:
            expired.append(rec)
        else:
            ok.append(rec)

    print(f"WARRISK per-row expiry check — as of {today} "
          f"({len(rows)-1} rows: {len(expired)} EXPIRED, {len(ok)} current, "
          f"{len(undated)} undated)")

    # Falsifier/anchor rows first — a stale falsifier is worse than a stale display row.
    def rank(r):
        role = r["role"].upper()
        return (0 if "FALSIFIER" in role else 1 if "ANCHOR" in role else 2,
                r["stale"] or dt.date.max)

    for r in sorted(expired, key=rank):
        over = (today - r["stale"]).days
        age = (today - r["asof"]).days if r["asof"] else "?"
        flag = "🎯 " if "FALSIFIER" in r["role"].upper() else ""
        print(f"  ⚠️ EXPIRED +{over}d  {flag}{r['leg'][:44]:44} "
              f"value={r['val'][:14]:14} As_Of={r['asof']} (age {age}d)  role={r['role'][:26]}")

    for r in undated:
        print(f"  ?  NO Stale_By   {r['leg'][:44]:44} value={r['val'][:14]:14} As_Of={r['asof']}")

    for r in sorted(ok, key=rank):
        left = (r["stale"] - today).days
        print(f"  ok  {left:+3d}d left  {r['leg'][:44]:44} value={r['val'][:14]:14} As_Of={r['asof']}")

    if expired:
        print("  → Re-pull the EXPIRED legs at primaries, then update Value + As_Of + "
              "Prior_* and recompute the derived spread row. DO NOT widen Stale_By to "
              "silence this, and DO NOT advance the file's data clock without a "
              "re-pulled figure.")
        if any("FALSIFIER" in r["role"].upper() for r in expired):
            print("  🔴 A REGISTERED FALSIFIER LEG IS EXPIRED — that is the leg whose whole "
                  "purpose is to fire before the headline leg moves. Treat as first-action.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
