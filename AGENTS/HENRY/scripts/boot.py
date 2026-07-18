#!/usr/bin/env python3
"""
HENRY Boot Kit (v1) — consolidated boot brief.

Read-only by design: it DISPLAYS live state, it does NOT write STATUS.md
(writing the dashboard back is the analyst's job at write-back). NOTE: the old
refresh_status.py was RETIRED 2026-06-15 to archive/retired/ (stale writer —
hardcoded narrative; do not resurrect — see MAINTENANCE.md).

Four components (all from existing materials):
  (a) LIVE TAPE       — fetch.py real-time/last quotes (not a pre-open period=1d bar)
  (b) GAMMA           — gamma_flip.py free-tier SPX dealer-gamma flip / net GEX / walls (14d, fast)
  (c) CREDIT          — credit_monitor.py (HY/CCC/BB + CCC-BB bifurcation)
  (d) PREDICTIONS-DUE — scan workbook/PREDICTIONS.tsv for OPEN/ACTIVE rows due ≤ today

Usage:
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py --quick     # skip credit + gamma (slower external pulls)
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py --verbose   # full credit_monitor output
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py --selftest  # assert the due-scan logic fires

Note (per Prome/ORC 6/15): boot.py does NOT prevent spawn-cadence staleness gaps —
no kit runs while HENRY is asleep. Its payoff is (1) a clean live pull that can't be
mislabeled a session-boundary stale snapshot, and (2) the predictions-due scan.
"""

import json
import re
import subprocess
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
HENRY_DIR = SCRIPTS_DIR.parent
WORKSPACE = HENRY_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"
FETCH_PY = WORKSPACE / "FORGE" / "tools" / "market-data" / "fetch.py"
CREDIT_MONITOR = SCRIPTS_DIR / "credit_monitor.py"
PREDICTIONS_TSV = HENRY_DIR / "workbook" / "PREDICTIONS.tsv"

# Full HENRY tape: index/vol/rates/banks/alts/energy/fx
TICKERS = [
    "^GSPC", "^VIX", "^VIX9D", "^VIX3M", "^VVIX", "^SKEW",
    "^TNX", "TLT", "KRE", "WAL", "APO", "ARES", "BZ=F", "JPY=X",
]
LABEL = {
    "^GSPC": "SPX", "^VIX": "VIX", "^VIX9D": "VIX9D", "^VIX3M": "VIX3M",
    "^VVIX": "VVIX", "^SKEW": "SKEW", "^TNX": "10Y", "TLT": "TLT",
    "KRE": "KRE", "WAL": "WAL", "APO": "APO", "ARES": "ARES",
    "BZ=F": "Brent", "JPY=X": "USD/JPY",
}

# Statuses that mean "still live / resolvable"
OPEN_STATUSES = {"ACTIVE", "OPEN"}


def _py():
    return str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable


def run(cmd, timeout=90):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout, cwd=str(WORKSPACE))
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return 1, "", f"TIMEOUT after {timeout}s"
    except Exception as e:  # noqa: BLE001
        return 1, "", str(e)


# ---------------------------------------------------------------- (a) LIVE TAPE
def live_tape():
    print(f"\n{'─'*64}\n  (a) LIVE TAPE   ·   pulled {datetime.now():%Y-%m-%d %H:%M:%S} local")
    print(f"{'─'*64}")
    code, out, err = run([_py(), str(FETCH_PY), "price"] + TICKERS + ["--json"])
    if code != 0:
        print(f"  ⚠️  fetch.py failed: {err[:300]}")
        return
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        print(f"  ⚠️  could not parse fetch.py output:\n{out[:300]}")
        return
    for t in TICKERS:
        info = data.get(t, {})
        if not info or "error" in info:
            print(f"  {LABEL.get(t, t):<8} {'—':>12}   (no quote)")
            continue
        px = info.get("price")
        chg = info.get("change_pct", info.get("changePercent"))
        chg_s = f"{chg:+.2f}%" if isinstance(chg, (int, float)) else ""
        try:
            px_s = f"{float(px):,.2f}"
        except (TypeError, ValueError):
            px_s = str(px)
        print(f"  {LABEL.get(t, t):<8} {px_s:>12}   {chg_s}")
    print("\n  ⚠️  real-time/last quote — stamp THIS timestamp in STATUS, not 'close'.")


# -------------------------------------------------------------------- (b) GAMMA
def gamma(asof=None):
    print(f"\n{'─'*64}\n  (b) GAMMA  ·  SPX dealer-gamma flip (gamma_flip.py, free-tier)\n{'─'*64}")
    try:
        if str(SCRIPTS_DIR) not in sys.path:
            sys.path.insert(0, str(SCRIPTS_DIR))
        from gamma_flip import compute_gamma_flip
        r = compute_gamma_flip(asof=asof, horizon=14)  # boot-fast; flip stable vs 35d (7,521 vs 7,522)
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠️  gamma_flip failed: {str(e)[:200]}")
        return
    if "error" in r:
        print(f"  ⚠️  {r['error']}")
        return
    spot, flip, g0 = r["spot"], r["flip"], r["gex_at_spot"]
    if flip:
        rel = spot - flip
        side = "BELOW → NEG-gamma, dealers AMPLIFY" if rel < 0 else "ABOVE → POS-gamma, dealers dampen"
        print(f"  SPX {spot:,.2f} · flip ~{flip:,.0f} · spot {rel:+,.0f}pts {side}")
    else:
        print(f"  SPX {spot:,.2f} · no flip in ±10% band · regime {r['regime']}")
    pw, cw = r["put_wall"], r["call_wall"]
    pw_note = " (SPX THROUGH it)" if pw and spot < pw else ""
    print(f"  Net GEX {g0/1e9:+.1f}B/1% · put wall {pw:,.0f}{pw_note} · call wall {cw:,.0f}"
          f"   [{r['horizon']}d, {r['n_contracts']} contracts]")
    print("  (free-tier: sign+flip robust, $B assumption-dependent · gamma_flip.py --days 35 for the definitive read)")


# ------------------------------------------------------------------- (c) CREDIT
def credit(verbose=False):
    print(f"\n{'─'*64}\n  (c) CREDIT  ·  FRED bifurcation (credit_monitor.py)\n{'─'*64}")
    if not CREDIT_MONITOR.exists():
        print("  ⚠️  credit_monitor.py not found")
        return
    code, out, err = run([_py(), str(CREDIT_MONITOR)])
    if code != 0 and not out:
        print(f"  ⚠️  credit_monitor failed: {err[:300]}")
        return
    if verbose:
        print(out)
    else:
        for line in out.splitlines():
            if any(m in line for m in ("BB", "HY", "CCC", "GAP", "HYG", "flag", "✓", "🔴", "🟠", "🟡")):
                print(f"  {line.strip()}")


# ----------------------------------------------------- (d) PREDICTIONS-DUE SCAN
def _parse_deadline(resdate):
    """Return ('rolling'|date|None, raw). For a date range, deadline = end date."""
    low = resdate.lower()
    if "rolling" in low:
        return "rolling", resdate
    isos = re.findall(r"\d{4}-\d{2}-\d{2}", resdate)
    if isos:
        ds = [date.fromisoformat(x) for x in isos]
        return max(ds), resdate  # end of range = the deadline
    return None, resdate  # unparseable (e.g. "Apr 30", "5/28-6/02")


def _classify(rows, today):
    """rows: list of (id, status, resdate). Returns due/upcoming/rolling/unparseable."""
    due, upcoming, rolling, unparseable = [], [], [], []
    horizon = today + timedelta(days=7)
    for pid, status, resdate in rows:
        if status.strip().upper() not in OPEN_STATUSES:
            continue
        dl, raw = _parse_deadline(resdate)
        if dl == "rolling":
            rolling.append((pid, raw))
        elif dl is None:
            unparseable.append((pid, raw))
        elif dl <= today:
            due.append((pid, dl, raw))
        elif dl <= horizon:
            upcoming.append((pid, dl, raw))
    return due, upcoming, rolling, unparseable


def _read_rows():
    if not PREDICTIONS_TSV.exists():
        return None
    rows = []
    lines = PREDICTIONS_TSV.read_text().strip().split("\n")
    for line in lines[1:]:
        c = line.split("\t")
        if len(c) >= 4:
            rows.append((c[0], c[2], c[3]))
    return rows


def predictions_due(today=None):
    today = today or date.today()
    print(f"\n{'─'*64}\n  (d) PREDICTIONS-DUE SCAN  ·  as of {today}\n{'─'*64}")
    rows = _read_rows()
    if rows is None:
        print("  ⚠️  PREDICTIONS.tsv not found")
        return
    due, upcoming, rolling, unparseable = _classify(rows, today)
    if due:
        print("  🔴 DUE — resolve now (OPEN/ACTIVE, deadline ≤ today):")
        for pid, dl, raw in due:
            print(f"     {pid:<8} deadline {dl}  [{raw}]")
    else:
        print("  ✓ none overdue.")
    if upcoming:
        print("  🟠 UPCOMING (≤7d):")
        for pid, dl, raw in upcoming:
            print(f"     {pid:<8} resolves {dl}  ({(dl - today).days}d)  [{raw}]")
    if rolling:
        print("  🟡 ROLLING watch: " + ", ".join(p for p, _ in rolling))
    if unparseable:
        print("  ⚠️  unparseable resolve-date (check manually): "
              + ", ".join(f"{p}[{r}]" for p, r in unparseable))


def selftest():
    """Assert the due-scan fires on a row like HEN-32 (resolve 6/10, ACTIVE)."""
    today = date(2026, 6, 15)
    fake = [
        ("HEN-XX", "ACTIVE", "2026-06-10"),                 # must be DUE
        ("HEN-YY", "ACTIVE", "2026-06-17-to-2026-06-19"),   # upcoming
        ("HEN-ZZ", "ACTIVE", "rolling"),                    # rolling
        ("HEN-DN", "MISS",   "2026-06-10"),                 # closed → ignored
    ]
    due, upcoming, rolling, _ = _classify(fake, today)
    ok = (
        any(p == "HEN-XX" for p, *_ in due)
        and not any(p == "HEN-DN" for p, *_ in due)
        and any(p == "HEN-YY" for p, *_ in upcoming)
        and "HEN-ZZ" in [p for p, _ in rolling]
    )
    print(f"  selftest: due={[p for p,*_ in due]} upcoming={[p for p,*_ in upcoming]} "
          f"rolling={[p for p,_ in rolling]}")
    print("  ✅ PASS — due-scan surfaces an ACTIVE/past-deadline row (and ignores closed)."
          if ok else "  ❌ FAIL")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv:
        return selftest()
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv
    t0 = time.time()
    now = datetime.now()
    print(f"\n{'='*64}\n  HENRY BOOT KIT (v1)   ·   {now:%A, %B %d, %Y  %H:%M}\n{'='*64}")
    live_tape()
    if not quick:
        gamma()
        credit(verbose=verbose)
    else:
        print("\n  (b) GAMMA + (c) CREDIT — skipped (--quick)")
    predictions_due()
    print(f"\n{'='*64}\n  boot brief done in {time.time()-t0:.1f}s   "
          f"(--verbose full credit · --quick skip gamma+credit · --selftest)\n{'='*64}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
