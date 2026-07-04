#!/usr/bin/env python3
"""
OZK Boot Kit — v0.1
One-command boot brief: live prices + catalyst countdown + threshold / inbox / staleness flags.

Usage:
  (cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/OZK/scripts/boot.py)
  ... --verbose        # full cohort price table + all catalysts (no horizon filter)
  ... --horizon 60     # catalyst look-ahead window in days (default 120)

Self-contained v0.1: inlines the catalyst list + standing threshold lines (kept in sync with
CALENDAR.md and STATUS.md Signal Dashboard by hand). Reuses FORGE fetch.py for live prices —
does NOT reimplement yfinance. Future (DAEDALUS market-agent blueprint conformance): decompose
into catalyst_countdown.py reading a machine-readable CATALYSTS.tsv + an FDIC-EFR insider fetcher.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

OZK_DIR = Path(__file__).resolve().parent.parent          # AGENTS/OZK
REPO_ROOT = OZK_DIR.parent.parent                          # repo root
FETCH = REPO_ROOT / "FORGE" / "tools" / "market-data" / "fetch.py"

# OZK + the regional-bank cohort OZK references (REGINALD owns the cohort canonically).
COHORT = ["OZK", "KRE", "WAL", "ZION", "EGBN", "SSB", "CFG", "VLY", "FLG"]

# Inlined catalysts — keep in sync with CALENDAR.md. (~ = modeled/undisclosed exact date.)
# (iso_date, modeled?, priority, label)
CATALYSTS = [
    ("2026-07-21", False, "🔴", "OZK Q2 2026 earnings (after close; call Jul 22 8:30am ET)"),
    ("2026-07-31", True,  "🟠", "Campus at Horton post-foreclosure leasing update (late Jul)"),
    ("2026-08-31", True,  "🔴", "IQHQ RaDD loan MATURITY (Aug 2026 — exact date undisclosed)"),
    ("2026-10-01", False, "🔴", "$350M sub notes reprice (2.75% → SOFR+209; Tier 2 -20%)"),
    ("2026-10-31", True,  "🟡", "Affinius Capital $2.7B bond maturity (OZK exposure UNVERIFIED)"),
]

# Standing threshold lines — resolve at the next quarterly print (not live-computable here).
STANDING_WATCH = [
    "NCO ≤55bps kill-line (Invalidation §2) — Q1'26 printed 0.56%, 1bp above. Next: Q2 Jul-21.",
    "Past-due >$550M or >2.0% — Q1'26 $487.5M/1.48%. Next: Q2 Jul-21.",
    "IQHQ specific reserve — any positive at Q2 = Scenario B firing early → REGINALD/BROCK/PROME 🔴.",
]

# OZK price bands (STATUS Signal Dashboard).
BAND_RED2 = 40.0   # <$40 → REGINALD, PROME, FORGE 🔴
BAND_RED1 = 45.0   # <$45 → REGINALD, PROME 🔴
BIG_MOVE = 3.0     # |daily %| beyond this = flag


def run_fetch(tickers):
    """Call FORGE fetch.py price --json. Returns dict or None on failure."""
    try:
        out = subprocess.run(
            [sys.executable, str(FETCH), "price", *tickers, "--json"],
            capture_output=True, text=True, timeout=45,
        )
        return json.loads(out.stdout) if out.stdout.strip() else None
    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError):
        return None


def trading_days(start, end):
    if end <= start:
        return 0
    d, cur = 0, start
    while cur < end:
        cur = cur.fromordinal(cur.toordinal() + 1)
        if cur.weekday() < 5:
            d += 1
    return d


def section(title):
    print(f"\n{'='*72}\n  {title}\n{'='*72}")


def main():
    verbose = "--verbose" in sys.argv
    horizon = 120
    if "--horizon" in sys.argv:
        i = sys.argv.index("--horizon")
        if i + 1 < len(sys.argv):
            horizon = int(sys.argv[i + 1])

    today = datetime.now().date()
    now = datetime.now().strftime("%A, %B %d, %Y  %H:%M")

    print(f"\n{'#'*72}\n#{'OZK BOOT SEQUENCE — v0.1':^70}#\n#{now:^70}#\n{'#'*72}")

    # ---- PRICES ----
    section("LIVE PRICES  (FORGE fetch.py)")
    data = run_fetch(COHORT)
    ozk_line = None
    if not data:
        print("  ⚠️  price fetch failed — run manually: "
              ".venv/bin/python3 FORGE/tools/market-data/fetch.py price OZK")
    else:
        ozk = data.get("OZK")
        if ozk:
            p, chg = ozk["price"], ozk.get("change_pct", 0)
            flags = []
            if p < BAND_RED2:   flags.append("🔴🔴 <$40 BAND (→REGINALD/PROME/FORGE)")
            elif p < BAND_RED1: flags.append("🔴 <$45 BAND (→REGINALD/PROME)")
            if abs(chg) >= BIG_MOVE: flags.append(f"⚠️ big move {chg:+.1f}%")
            ozk_line = f"  OZK  ${p:>8.2f}  ({chg:+.2f}%)   {'  '.join(flags) if flags else '🟢 no band breach'}"
            print(ozk_line)
        if verbose:
            print("  " + "-" * 50)
            for t in COHORT:
                if t == "OZK" or t not in data:
                    continue
                d = data[t]
                arrow = "🟢" if d.get("change_pct", 0) >= 0 else "🔴"
                print(f"  {arrow} {t:<6} ${d['price']:>8.2f}  ({d.get('change_pct',0):+.2f}%)")
        else:
            peers = [f"{t} {data[t]['change_pct']:+.1f}%" for t in COHORT[1:] if t in data]
            print("  cohort: " + " · ".join(peers))

    # ---- CATALYST COUNTDOWN ----
    section(f"CATALYST COUNTDOWN  ({horizon}-day horizon; ~ = modeled date)")
    rows = []
    for iso, modeled, pri, label in CATALYSTS:
        d = datetime.strptime(iso, "%Y-%m-%d").date()
        cal = (d - today).days
        if cal < 0:
            continue
        if not verbose and cal > horizon:
            continue
        rows.append((cal, trading_days(today, d), modeled, pri, iso, label))
    rows.sort()
    if not rows:
        print("  (none within horizon — use --verbose)")
    for cal, td, modeled, pri, iso, label in rows:
        soon = "⏰ " if cal <= 14 else "   "
        mark = "~" if modeled else " "
        print(f"  {soon}{pri} {mark}{iso}  ({cal:>3}d / {td:>3} trading)  {label}")

    # ---- STANDING WATCH ----
    section("STANDING WATCH  (resolve at next quarterly print)")
    for w in STANDING_WATCH:
        print(f"  • {w}")

    # ---- INBOX ----
    section("INBOX  (unprocessed)")
    inbox = sorted(p for p in (OZK_DIR / "inbox").glob("*.md"))
    if not inbox:
        print("  (empty — nothing to process)")
    else:
        print(f"  {len(inbox)} unprocessed:")
        for p in inbox:
            print(f"    - {p.name}")

    # ---- STALENESS ----
    section("STALENESS")
    for fname in ("STATUS.md", "CALENDAR.md"):
        f = OZK_DIR / fname
        if f.exists():
            age = (datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)).days
            flag = " ⚠️ STALE" if age > 7 else ""
            print(f"  {fname:<14} {age:>3}d old{flag}")

    print(f"\n{'='*72}\n  Boot brief complete. Full detail: --verbose\n{'='*72}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
