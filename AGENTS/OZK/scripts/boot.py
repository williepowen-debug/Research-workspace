#!/usr/bin/env python3
"""
OZK Boot Kit — v0.2
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
    ("2026-10-21", True,  "🔴", "Q3 2026 earnings + call — mgmt's self-set \"~92 day\" RaDD report-back"),
    ("2026-10-31", True,  "🟡", "Affinius Capital $2.7B bond maturity (OZK exposure UNVERIFIED)"),
    ("2026-11-05", False, "🟠", "FFIEC JWT EXPIRES — renewal is a Will action (PWS login); blocks the Q3 pull"),
    ("2026-11-07", True,  "🟠", "Q3 2026 Call Report (REPDTE 20260930) — LOG-ONLY, Z6 never re-grades"),
]
# Sync note (2026-08-23): the two 2026-10/11 rows and the JWT row were absent here while present in
# CALENDAR.md — this list is hand-synced, so it silently lags. The Jul-21 earnings + Jul-31 Horton
# rows above are PAST and are kept deliberately: the countdown filters them, and deleting resolved
# catalysts destroys the record of what this kit was watching.

# Standing threshold lines — resolve at the next quarterly print (not live-computable here).
# (text, as_of_print, next_resolver_iso) — next_resolver_iso is the print that RESOLVES this line.
# ⚠️ Every row carries its own next-resolver DATE so a passed one is flagged, not printed as forward.
#    v0.2 shipped these as bare strings hardcoding "Next: Q2 Jul-21" and kept printing it with Q1
#    figures for 5 weeks after Q2 graded (found 2026-08-28 sweep). CATALYSTS filters past rows; this
#    list had no date at all, so it could not.
STANDING_WATCH = [
    ("NCO ≤55bps kill-line (Invalidation §2) — Q2'26 printed 0.69%, ABOVE the kill line (OZK-05 TRUE)",
     "Q2 2026", "2026-10-21"),
    ("Past-due >$550M or >2.0% — Q2'26 $298M/0.92% (OZK-06 FALSE, improved from $465M/1.41%)",
     "Q2 2026", "2026-10-21"),
    ("IQHQ specific reserve — none at Q2 (OZK-08 FALSE); mgmt self-set “~92d” report-back → Q3 call",
     "Q2 2026", "2026-10-21"),
]

# OZK price bands (STATUS Signal Dashboard).
BAND_RED2 = 40.0   # <$40 → REGINALD, PROME, FORGE 🔴
BAND_RED1 = 45.0   # <$45 → REGINALD, PROME 🔴
BIG_MOVE = 3.0     # |daily %| beyond this = flag


def last_expected_session(today):
    """Most recent weekday on/before `today` — the newest date a live quote could carry.

    Weekday-only. Exchange holidays are NOT modeled, so on the session after a holiday
    this reports one day stale rather than none. That direction is deliberate: the check
    over-warns and never under-warns (`finding_measurement_bias_sign_is_fixed_harm_direction_is_not`).
    """
    d = today
    while d.weekday() >= 5:
        d = d.fromordinal(d.toordinal() - 1)
    return d


def run_fetch(tickers, today=None):
    """Call FORGE fetch.py price --json.

    Returns (data_or_None, diag) where diag is a dict the caller MUST render:
      mode   : LIVE | STALE | EMPTY | BADJSON | RC | TIMEOUT | OSERR
      asof   : served vintage (str) when the payload carries one
      lag    : trading days between served vintage and the last expected session
      rc     : the child's exit code
      stderr : the child's stderr, VERBATIM and never suppressed

    §8 CHECK_STANDARD contract (DAEDALUS 2026-08-17, ratified; adopted here 2026-08-23).
    The pre-fix version JSON-parsed stdout and discarded stderr AND the exit code, so every
    failure mode collapsed to one "price fetch failed" line, and — the sharper half — a
    STALE-BUT-PARSEABLE payload rendered as live prices with no vintage. On THIS wrapper that
    is not merely cosmetic: boot.py compares the served price against the <$45 / <$40 bands
    that page REGINALD, PROME and FORGE, so a stale payload can fire a cross-agent escalation
    off a months-old quote. Counterfactual runs of the pre-fix code are recorded in
    `AGENTS/OZK/inbox/processed/2026-08-17_from-DAEDALUS_*` disposition (MEMORY Findings).
    """
    today = today or datetime.now().date()
    diag = {"mode": None, "asof": None, "lag": None, "rc": None, "stderr": ""}
    try:
        out = subprocess.run(
            [sys.executable, str(FETCH), "price", *tickers, "--json"],
            capture_output=True, text=True, timeout=45,
        )
    except subprocess.TimeoutExpired:
        diag["mode"] = "TIMEOUT"
        return None, diag
    except OSError as e:
        diag["mode"], diag["stderr"] = "OSERR", str(e)
        return None, diag

    diag["rc"] = out.returncode
    diag["stderr"] = (out.stderr or "").strip()

    # Branch on the exit code we used to throw away — BEFORE trusting stdout.
    if out.returncode != 0:
        diag["mode"] = "RC"
        return None, diag
    if not out.stdout.strip():
        diag["mode"] = "EMPTY"
        return None, diag
    try:
        data = json.loads(out.stdout)
    except json.JSONDecodeError as e:
        diag["mode"], diag["stderr"] = "BADJSON", (diag["stderr"] + f" | {e}").strip(" |")
        return None, diag

    # Served vintage — the half that made a stale payload indistinguishable from a live one.
    asof = None
    for t in tickers:
        v = (data.get(t) or {}).get("asof")
        if v:
            asof = v
            break
    if asof:
        diag["asof"] = asof
        try:
            served = datetime.strptime(asof, "%Y-%m-%d").date()
            diag["lag"] = trading_days(served, last_expected_session(today))
        except ValueError:
            diag["lag"] = None
    diag["mode"] = "LIVE" if diag["lag"] == 0 else ("STALE" if diag["lag"] else "LIVE")
    if asof is None:
        diag["mode"] = "STALE"          # no vintage served => cannot certify live
    return data, diag


def render_fetch_diag(diag):
    """Print the source-mode banner + relay stderr unconditionally. Returns True if usable."""
    m = diag["mode"]
    if m == "LIVE":
        print(f"  📡 SOURCE: LIVE {diag['asof']}  (fetch.py rc=0)")
    elif m == "STALE":
        vint = diag["asof"] or "vintage NOT SERVED"
        lag = f", {diag['lag']} trading day(s) behind" if diag["lag"] else ""
        print(f"  🟠 SOURCE: CACHED/STALE {vint}{lag}  (fetch.py rc={diag['rc']})")
        print("     ⚠️  Prices below are NOT current. Do NOT read a band breach off them —")
        print("         the <$45/<$40 bands page REGINALD/PROME/FORGE. Re-pull before citing.")
    else:
        why = {"EMPTY": "no stdout", "BADJSON": "stdout was not JSON",
               "RC": f"fetch.py exited rc={diag['rc']}", "TIMEOUT": "timed out after 45s",
               "OSERR": "could not start fetch.py"}.get(m, m)
        print(f"  ⚠️  PRICE FETCH FAILED — {why}")
        print("     run manually: .venv/bin/python3 FORGE/tools/market-data/fetch.py price OZK")
    if diag["stderr"]:
        for line in diag["stderr"].splitlines():
            print(f"     [fetch.py stderr] {line}")
    return m in ("LIVE", "STALE")


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

    print(f"\n{'#'*72}\n#{'OZK BOOT SEQUENCE — v0.2 (§8)':^70}#\n#{now:^70}#\n{'#'*72}")

    # ---- PRICES ----
    section("LIVE PRICES  (FORGE fetch.py)")
    data, fetch_diag = run_fetch(COHORT, today=today)
    ozk_line = None
    usable = render_fetch_diag(fetch_diag)
    stale = fetch_diag["mode"] == "STALE"
    if not (data and usable):
        pass
    else:
        ozk = data.get("OZK")
        if ozk:
            p, chg = ozk["price"], ozk.get("change_pct", 0)
            flags = []
            if p < BAND_RED2:   flags.append("🔴🔴 <$40 BAND (→REGINALD/PROME/FORGE)")
            elif p < BAND_RED1: flags.append("🔴 <$45 BAND (→REGINALD/PROME)")
            if abs(chg) >= BIG_MOVE: flags.append(f"⚠️ big move {chg:+.1f}%")
            if stale and flags:
                flags = [f"⛔ SUPPRESSED (stale data): {f}" for f in flags]
            vtag = f"  [{fetch_diag['asof'] or 'no vintage'}]"
            ozk_line = f"  OZK  ${p:>8.2f}  ({chg:+.2f}%){vtag}   {'  '.join(flags) if flags else '🟢 no band breach'}"
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
    for text, as_of, nxt in STANDING_WATCH:
        d = datetime.strptime(nxt, "%Y-%m-%d").date()
        if d < today:
            # The resolver has PASSED and this line was never re-based -> say so loudly.
            print(f"  \u26a0\ufe0f STALE  • {text}")
            print(f"           \u21b3 resolver {nxt} PASSED {(today - d).days}d ago and this line "
                  f"still reads as of {as_of} \u2014 re-base it against the print that resolved it.")
        else:
            print(f"  • {text}")
            print(f"      [as of {as_of} \u00b7 resolves {nxt}, {(d - today).days}d]")

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
    # ⚠️ NEVER key freshness on st_mtime: git sync restamps it, so on the machine that pulled,
    #    every file reads FRESH -> the check fails FALSE-NEGATIVE, exactly when it matters.
    #    ([[finding_mtime_is_corrupted_by_git_sync]]; found in this kit 2026-08-28.)
    #    Order: git-commit vintage first, mtime last-resort, and the BASIS is always printed.
    for fname in ("STATUS.md", "CALENDAR.md"):
        f = OZK_DIR / fname
        if not f.exists():
            continue
        basis, stamp = "mtime(last-resort)", datetime.fromtimestamp(f.stat().st_mtime)
        try:
            out = subprocess.run(
                ["git", "log", "-1", "--format=%at", "--", str(f.relative_to(REPO_ROOT))],
                cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=10)
            if out.returncode == 0 and out.stdout.strip():
                basis, stamp = "git-commit", datetime.fromtimestamp(int(out.stdout.strip()))
        except Exception:
            pass
        age = (datetime.now() - stamp).days
        dirty = ""
        try:
            ds = subprocess.run(["git", "status", "--porcelain", "--",
                                 str(f.relative_to(REPO_ROOT))],
                                cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=10)
            if ds.returncode == 0 and ds.stdout.strip():
                dirty = "  (uncommitted edits in tree)"
        except Exception:
            pass
        flag = " \u26a0\ufe0f STALE" if age > 7 else ""
        print(f"  {fname:<14} {age:>3}d old{flag}   [basis: {basis}]{dirty}")

    # Ledger staleness is a SEPARATE object from doc age (workbook/*.tsv, content-vintage first).
    # OZK had zero calls to the fleet tool before 2026-08-28.
    led = REPO_ROOT / "scripts" / "ledger_staleness.py"
    if led.exists():
        try:
            r = subprocess.run([sys.executable, str(led), "OZK", "--quiet"],
                               cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=30)
            body = (r.stdout or "").strip()
            print(f"\n  ledgers (workbook/*.tsv, via scripts/ledger_staleness.py):")
            print("\n".join(f"    {ln}" for ln in body.splitlines()) if body
                  else "    all ledgers current vs STATUS")
            if (r.stderr or "").strip():
                print(f"    [stderr] {r.stderr.strip()[:200]}")
        except Exception as e:
            print(f"\n  ledgers: \u26a0\ufe0f check FAILED ({type(e).__name__}) \u2014 run "
                  f"scripts/ledger_staleness.py OZK by hand")

    print(f"\n{'='*72}\n  Boot brief complete. Full detail: --verbose\n{'='*72}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
