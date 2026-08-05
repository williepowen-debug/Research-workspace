#!/usr/bin/env python3
"""VIOLET VX term-structure history builder — 2013 → current, FREE.

⚠️ THIS EXISTS BECAUSE MY RECORDED BLOCKER WAS WRONG (2026-07-30).

On the morning of 7/30 I concluded, and wrote into KB-VIO-152, `SCRATCH`,
`NEXUS_BRIEF` and the thesis CHANGELOG, that:

    "CBOE serves settlement ONE REQUEST PER DATE and only a ~12-MONTH ROLLING
     WINDOW … extending H3 needs a DIFFERENT SOURCE (CBOE DataShop / a vendor
     VX continuous series), and that is the blocker to solve before any
     re-attempt."

**That was false, and it was false in the expensive direction — it nearly bought
a paid data subscription for something CBOE gives away.** The mistake was that I
audited *the endpoint I already knew* (`/settlement/csv/?dt=`, which really is a
~12-month rolling per-DATE feed) and generalised from it to "no free source
exists." I never checked whether CBOE published the same data on a different
axis. It does:

    https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{EXPIRY}.csv

**Keyed on the CONTRACT's expiry date, not on a trade date** — one file per
expired contract, carrying that contract's ENTIRE life with a real `Settle`
column. My first probe missed it only because I guessed an arbitrary date
(`2020-01-02`) that was never a VX expiry, got a 403, and stopped.

**The lesson, and it is `finding_audit_resolution_path_before_reattempt` landing
on me: a long-open question is usually blocked by the PATH, not by missing data
— and "I checked the endpoint" is not "I checked the source."** Verified depth:
2013 files return 200, 2012 and earlier 403 — matching CBOE's own page text
("CFE Price and Volume Detail … from 2013 to Current", free).

WHAT IT BUILDS
  `workbook/VX_TERM_HISTORY.tsv` — one row per (trade_date, contract) with the
  settle, plus a derived per-date front-month panel (M1/M2 + days-to-expiry).
  ~160 monthly contracts ≈ one request each, so a full build is ~1 minute and a
  refresh is incremental.

⚠️ MONTHLIES ONLY, deliberately. VX weeklies have their own files, but the
front-month series this feeds (H3, the basis work) was built on monthlies and
mixing tenor conventions mid-series is exactly the specification error thesis
v3.8 is about. Weeklies are a separate, later extension — not a silent addition.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/vx_history.py --build      # full 2013→now — USE THIS

⚠️ `--build` REWRITES the ledger from `--from-year`; **it is not an incremental
append**, and the flag reads as though it were. `--build --from-year 2026`
replaced 28,555 rows with 1,933 and exited 0 with a success line (2026-08-04,
recovered from git). A truncation guard now refuses any build producing <90% of
the existing row count unless `--allow-shrink` is passed. **To refresh, just run
`--build` with no year.**
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import sys
import urllib.error
import urllib.request
from pathlib import Path

VIOLET_DIR = Path(__file__).resolve().parents[1]
LEDGER = VIOLET_DIR / "workbook" / "VX_TERM_HISTORY.tsv"
BASE = "https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_"
HDRS = {"User-Agent": "Mozilla/5.0",
        "Referer": "https://www.cboe.com/us/futures/market_statistics/historical_data/"}
FIRST_YEAR = 2013  # verified: 2013 = 200, 2012 = 403


def vx_monthly_expiry(year: int, month: int) -> dt.date:
    """Wednesday 30 days prior to the 3rd Friday of the FOLLOWING month."""
    ny, nm = (year + 1, 1) if month == 12 else (year, month + 1)
    d = dt.date(ny, nm, 1)
    fridays = [d + dt.timedelta(i) for i in range(31)
               if (d + dt.timedelta(i)).month == nm and (d + dt.timedelta(i)).weekday() == 4]
    return fridays[2] - dt.timedelta(days=30)


def fetch_contract(expiry: dt.date) -> list[dict] | None:
    url = f"{BASE}{expiry.isoformat()}.csv"
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers=HDRS), timeout=30).read()
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return None
    out = []
    for r in csv.DictReader(io.StringIO(raw.decode("utf-8", "replace"))):
        td, settle = (r.get("Trade Date") or "").strip(), (r.get("Settle") or "").strip()
        if not td or not settle:
            continue
        try:
            s = float(settle)
        except ValueError:
            continue
        if s <= 0:          # 0.00 = contract listed but not yet trading
            continue
        try:
            d = dt.datetime.fromisoformat(td).date()
        except ValueError:
            continue
        out.append({"trade_date": d, "expiry": expiry, "settle": s,
                    "dte": (expiry - d).days})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--from-year", type=int, default=FIRST_YEAR,
                    help="REWRITES the ledger from this year — this is NOT an incremental append")
    ap.add_argument("--allow-shrink", action="store_true",
                    help="permit a build that produces <90%% of the existing row count")
    a = ap.parse_args(argv)
    if not a.build:
        ap.print_help()
        return 0

    today = dt.date.today()
    expiries = [vx_monthly_expiry(y, m)
                for y in range(a.from_year, today.year + 2)
                for m in range(1, 13)]
    expiries = [e for e in expiries if e <= today + dt.timedelta(days=400)]

    rows, ok, miss = [], 0, 0
    for i, e in enumerate(expiries):
        got = fetch_contract(e)
        if got:
            rows.extend(got); ok += 1
        else:
            miss += 1
        if i % 25 == 0:
            print(f"  … {i}/{len(expiries)} contracts ({ok} ok, {miss} miss)", file=sys.stderr)
    print(f"  fetched {ok} contracts ({miss} unavailable), {len(rows)} contract-days",
          file=sys.stderr)
    if not rows:
        print("NO DATA — aborting rather than truncating the ledger", file=sys.stderr)
        return 1

    # ⚠️ TRUNCATION GUARD (added 2026-08-04, after it happened to me).
    # `--build` REWRITES the whole ledger from `--from-year`; it does NOT append.
    # So `--build --from-year 2026`, which reads like "just refresh the recent
    # part", silently replaced 28,555 rows (2013→) with 1,933 (2025-04→) — a
    # 93% data loss that exited rc=0 with a cheerful success line. The existing
    # `if not rows` guard only catches TOTAL failure; partial truncation is the
    # far likelier and quieter version. Recovered from git; guarded here so the
    # next caller cannot repeat it.
    if LEDGER.exists():
        prior = max(0, sum(1 for _ in LEDGER.open()) - 1)
        if prior and len(rows) < prior * 0.9 and not a.allow_shrink:
            print(f"🔴 REFUSING TO WRITE — this build produces {len(rows)} rows but the "
                  f"existing ledger has {prior}.", file=sys.stderr)
            print(f"   `--build` REWRITES from --from-year (currently {a.from_year}); it does not append. "
                  f"Omit --from-year for the full history, or pass --allow-shrink if the "
                  f"shrink is genuinely intended.", file=sys.stderr)
            return 1

    rows.sort(key=lambda r: (r["trade_date"], r["expiry"]))
    with LEDGER.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["trade_date", "expiry", "dte", "settle"])
        for r in rows:
            w.writerow([r["trade_date"], r["expiry"], r["dte"], f"{r['settle']:.4f}"])

    days = sorted({r["trade_date"] for r in rows})
    print(f"✓ {LEDGER.name}: {len(rows)} rows · {len(days)} trade days · "
          f"{days[0]} → {days[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
