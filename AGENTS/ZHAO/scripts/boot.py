#!/usr/bin/env python3
"""
ZHAO Boot Sequence — China-macro monitor & staleness guard

Single-command replacement for the manual boot refresh. Pulls live figures,
band-checks them against the VX ledger, and — the point of this script —
FLAGS ANY TRACKED FIGURE THAT HAS GONE STALE, so a 2.5-month drift like the
one found on 2026-07-04 surfaces at boot instead of never.

Sections (printed most-actionable first):
  [1] LIVE PULL        — USD/CNY, USD/KRW, Brent (yfinance) + inline band check
  [2] KEY-FIGURE AGE   — the load-bearing rows (China/Belgium TIC, HIBOR, PMI…)
                         with days-since-update; anything > STALE_DAYS is 🔴
  [3] TIC RELEASE WATCH— computes whether a newer TIC print should exist
  [4] CATALYST DOCKET  — upcoming/overdue dated events (maintained list)
  [5] OPEN PREDICTIONS — from PREDICTIONS.tsv
  [6] LEDGER STALENESS — count + oldest rows across all of VX.tsv

MUST be run with the repo venv (yfinance lives there, not system python3):
  .venv/bin/python AGENTS/ZHAO/scripts/boot.py
  .venv/bin/python AGENTS/ZHAO/scripts/boot.py --quick    # skip network pull
"""

import re
import sys
from datetime import date, datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
ZHAO_DIR = SCRIPTS_DIR.parent
WORKSPACE = ZHAO_DIR.parent.parent            # Research-workspace/
WORKBOOK = ZHAO_DIR / "workbook"
VX_TSV = WORKBOOK / "VX.tsv"
PRED_TSV = WORKBOOK / "PREDICTIONS.tsv"

STALE_DAYS = 21          # a live indicator older than this is flagged
KEY_STALE_DAYS = 14      # tighter bar for the load-bearing figures

# --- live tickers: (label, yfinance symbol, band fn -> (emoji, band) ) ---
def _cny_band(v):
    if v > 7.40: return ("🔴", "RED >7.40")
    if v > 7.30: return ("🟠", "ORANGE >7.30")
    if v < 7.20: return ("🟢", "green <7.20")
    return ("🟡", "watch 7.20-7.30")

def _krw_band(v):
    if v > 1500: return ("🔴", "RED >1500 (BoK selling)")
    if v > 1480: return ("🟠", "ORANGE >1480")
    if v > 1450: return ("🟡", "yellow >1450")
    return ("🟢", "green <1450")

def _brent_band(v):
    # transmission input, no formal ZHAO band; context only
    if v > 100: return ("🟠", "energy-shock zone >$100")
    return ("🟢", "normal")

LIVE = [
    ("USD/CNY", "CNY=X", _cny_band),
    ("USD/KRW", "KRW=X", _krw_band),
    ("Brent",   "BZ=F",  _brent_band),
]

# --- load-bearing rows to age-check, by VX id ---
KEY_FIGURES = [
    ("China TIC",   "VX-ZHAO-1.02"),
    ("Belgium TIC", "VX-ZHAO-1.01"),
    ("USD/CNY",     "VX-ZHAO-2.01"),
    ("USD/KRW",     "VX-ZHAO-2.05"),
    ("HK Agg Bal",  "VX-ZHAO-2.03"),
    ("HIBOR-SOFR",  "VX-ZHAO-2.04"),
    ("China PMI",   "VX-ZHAO-4.01"),
    ("PBOC rate",   "VX-ZHAO-6.06"),
]

# --- maintained catalyst docket (update as events pass) ---
CATALYSTS = [
    ("2026-07-16", "BoK policy meeting — possible hike (CPI 3.2%)"),
    ("2026-07-17", "TIC May 2026 data (~mid-month) — verify China/Belgium <$650B"),
    ("2026-11-10", "US-China reciprocal-tariff suspension expiry"),
    ("2026-12-01", "SEC cash-clearing mandate"),
]

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}


def today():
    # date.today() is allowed here (real script run), unlike in workflow sandboxes
    return date.today()


def _read_tsv(path):
    if not path.exists():
        return [], []
    rows = path.read_text(encoding="utf-8").splitlines()
    if not rows:
        return [], []
    header = rows[0].split("\t")
    body = [r.split("\t") for r in rows[1:] if r.strip()]
    return header, body


def _age_days(datestr):
    try:
        d = datetime.strptime(datestr.strip(), "%Y-%m-%d").date()
        return (today() - d).days
    except Exception:
        return None


def _vx_index():
    header, body = _read_tsv(VX_TSV)
    idx = {}
    for r in body:
        if len(r) >= 9:
            idx[r[0]] = {"name": r[1], "value": r[2], "status": r[3],
                         "updated": r[8]}
    return idx, body


def section_live(quick):
    print("\n[1] LIVE PULL (yfinance)")
    if quick:
        print("    (skipped — --quick)")
        return
    try:
        import warnings
        warnings.filterwarnings("ignore")
        import yfinance as yf
    except ModuleNotFoundError:
        print("    ⚠️  yfinance not found — run with .venv/bin/python "
              "(NOT system python3). See memory finding_market_data_venv_invocation.")
        return
    for label, sym, band in LIVE:
        try:
            hist = yf.Ticker(sym).history(period="5d")
            price = float(hist["Close"].iloc[-1])
            emoji, note = band(price)
            print(f"    {label:9s} {price:>10.2f}  {emoji} {note}")
        except Exception as e:
            print(f"    {label:9s} {'n/a':>10s}  ⚠️ fetch failed ({type(e).__name__})")


def section_key_ages():
    print(f"\n[2] KEY-FIGURE AGE  (🔴 if > {KEY_STALE_DAYS}d)")
    idx, _ = _vx_index()
    for label, vid in KEY_FIGURES:
        row = idx.get(vid)
        if not row:
            print(f"    {label:12s} — VX id {vid} MISSING")
            continue
        age = _age_days(row["updated"])
        flag = "🔴 STALE" if (age is not None and age > KEY_STALE_DAYS) else "✓"
        agestr = f"{age}d" if age is not None else "?"
        print(f"    {label:12s} {row['value'][:14]:14s} "
              f"upd {row['updated']} ({agestr:>4s}) {flag}")


def section_tic_watch():
    print("\n[3] TIC RELEASE WATCH")
    idx, _ = _vx_index()
    # infer the data-month from the China-TIC row's source-ish 'updated' + value note
    header, body = _read_tsv(VX_TSV)
    china = next((r for r in body if r and r[0] == "VX-ZHAO-1.02"), None)
    src = china[9] if china and len(china) > 9 else ""
    m = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})", src)
    if not m:
        print("    (could not parse latest TIC data-month from VX source)")
        return
    data_month, data_year = MONTHS[m.group(1)], int(m.group(2))
    t = today()
    # TIC for month M releases ~mid month M+2. Expected latest available:
    exp_idx = (t.year * 12 + t.month) - (2 if t.day >= 16 else 3)
    have_idx = data_year * 12 + data_month
    print(f"    Latest logged: {m.group(1)} {data_year}  "
          f"(China ${idx.get('VX-ZHAO-1.02', {}).get('value','?')}B)")
    if exp_idx > have_idx:
        gap = exp_idx - have_idx
        print(f"    🔴 A newer TIC print should be out (~{gap} month(s) ahead) — PULL IT.")
    else:
        print("    ✓ up to date with the release schedule.")


def section_catalysts():
    print("\n[4] CATALYST DOCKET  (±30d)")
    t = today()
    shown = False
    for ds, label in sorted(CATALYSTS):
        try:
            d = datetime.strptime(ds, "%Y-%m-%d").date()
        except Exception:
            continue
        delta = (d - t).days
        if -3 <= delta <= 30:
            tag = "🔴 OVERDUE" if delta < 0 else (f"in {delta}d" if delta else "TODAY")
            print(f"    {ds}  {tag:>10s}  {label}")
            shown = True
    if not shown:
        print("    (nothing within ±30d — extend CATALYSTS list if that seems wrong)")


def section_predictions():
    print("\n[5] OPEN PREDICTIONS")
    header, body = _read_tsv(PRED_TSV)
    if not body:
        print("    (none)")
        return
    # PREDICTIONS.tsv: Pred_ID, Date_Made, Prediction, Confidence, Timeframe, Status, ...
    for r in body:
        if len(r) >= 6 and r[5].strip().upper() == "OPEN":
            print(f"    {r[0]:8s} {r[3]:>5s}  {r[2][:60]}")


def section_ledger_staleness():
    print(f"\n[6] LEDGER STALENESS  (VX rows > {STALE_DAYS}d)")
    header, body = _read_tsv(VX_TSV)
    aged = []
    for r in body:
        if len(r) >= 9:
            age = _age_days(r[8])
            if age is not None and age > STALE_DAYS:
                aged.append((age, r[0], r[1]))
    if not aged:
        print("    ✓ all VX rows fresh.")
        return
    aged.sort(reverse=True)
    print(f"    {len(aged)} of {len(body)} rows stale. Oldest:")
    for age, vid, name in aged[:8]:
        print(f"      {age:>4d}d  {vid:14s} {name}")
    if len(aged) > 8:
        print(f"      … +{len(aged) - 8} more")


def main():
    quick = "--quick" in sys.argv
    print("=" * 60)
    print(f"ZHAO BOOT BRIEF — {today().isoformat()}")
    print("=" * 60)
    section_live(quick)
    section_key_ages()
    section_tic_watch()
    section_catalysts()
    section_predictions()
    section_ledger_staleness()
    print("\n" + "=" * 60)
    print("Boot brief complete. Refresh any 🔴, then proceed with STATUS.md.")
    print("=" * 60)


if __name__ == "__main__":
    main()
