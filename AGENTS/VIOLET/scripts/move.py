#!/usr/bin/env python3
"""VIOLET MOVE (rates-vol) fetch — investing.com PRIMARY, yfinance CROSS-CHECK.

WHY THIS EXISTS (KB-VIO-177, built 2026-08-04)
----------------------------------------------
**I carried "confirm-3 BROKEN" for five sessions while MOVE was above its line
every one of them.** yfinance froze at 70.88 [2026-07-17] and served a lone 8/3
bar; the true path was 74.18 → 77.09 → **83.02 (episode high)** → 80.48. The
KB-VIO-123 tree grades on that confirm, so a frozen feed silently biased my whole
convergence read WEAKER for a week.

⚠️ THE POLICY EXISTED AND NOTHING IMPLEMENTED IT. `CANARY_MAP.md` has carried
*"investing.com primary; yf ^MOVE unreliable as sole source"* since 2026-07-30 —
as **prose**. There was no MOVE script at all: every read was ad hoc, through the
one source the map already called unreliable. Same class as
`finding_mechanize_the_cap_not_the_ritual` — a documented rule with no mechanism
is performed as often as someone remembers, i.e. never.

⚠️ AND MY OWN KB HELD THE FIX. KB-VIO-131 registered *this series, this failure,
this resolution path* (investing.com's historical table) weeks earlier. On 8/4 I
re-derived the pathology from scratch, filed it as KB-VIO-176, and **cited
KB-VIO-131 as precedent while not executing the precedent's own remedy.**
Citing a prior finding is not applying it. This script is the applying.

SOURCE ORDER, and why it is this way round
------------------------------------------
  PRIMARY    investing.com `__NEXT_DATA__` JSON — structured, ~22 sessions of
             daily history, parses without a browser. Verified 8/4: it carried
             the 7/30 and 7/31 bars yfinance did not have AT ALL.
  CROSS-CHECK yfinance `^MOVE` — retained ONLY to disagree with. It is known to
             return a stale window with no staleness signal, so it can never
             promote a value; it can only raise a flag.

⚠️ FAIL-SAFE DIRECTION IS PART OF THE SPEC (thesis v3.8/v3.9). If the primary is
unreachable we print LOUDLY and fall back to the cross-check **labelled
`[UNCORROBORATED — known-unreliable source]`**. We never silently serve the
cross-check as if it were the primary — that is exactly the failure this script
was built to end. "Cannot verify" keeps data and labels it; only "confirmed
stale" may drop it.

⚠️ AND THE CROSS-CHECK IS NOT AN INDEPENDENT WITNESS WHEN IT AGREES. On 8/4 both
paths returned 80.48 for 8/3 — that looked like corroboration and was not: they
were one upstream in two coats. What made the 8/4 read trustworthy was that
investing.com carried bars yfinance **lacked**, plus a MECHANISTIC check (10Y
peaked 4.74 the same session MOVE peaked 83.02). Agreement on a shared bar is
weak evidence; coverage the other source lacks is strong.

REGISTERED LINES (levels live here; state lives in STATUS)
---------------------------------------------------------
  F1  > 72.41   KB-VIO-116 fire condition
  confirm-3 > 75-76  KB-VIO-123 crack-vs-fade tree leg
  (GATE-VIO-116 re-open — REMOVED 2026-09-04; gate RESOLVED 7/16, KB-VIO-219)
  N1  < 66      stand-down

Exit codes: 0 = primary served a fresh bar; 1 = primary failed AND we fell back
to the labelled cross-check (with --strict); 2 = no source returned anything.
"""
from __future__ import annotations
import argparse, json, re, sys, urllib.request
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "workbook" / "MOVE.tsv"
URL = "https://www.investing.com/indices/ice-bofaml-move-historical-data"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/125 Safari/537.36"}

# ⛔ "GATE-VIO-116 re-open > 71.00" WAS REMOVED 2026-09-04 (KB-VIO-219).
# GATE-VIO-116 RESOLVED 2026-07-16 (F3 fired) and holds no live legs — it is not
# even a row in PROME/GATES.tsv any more. This tool printed a re-open leg for it
# at every boot for ~7 weeks: a RESOLVED gate rendered as a live threshold, which
# is the one direction that manufactures work rather than hiding it. Flagged 9/2,
# carried as a known defect, removed today.
# ⚠️ F1 (72.41) is a DIFFERENT line and STAYS — it is the live MOVE re-arm
# referenced by SIGNAL_INTAKE § ACTIVE THRESHOLDS (re-armed 2026-09-01), and it
# shares the KB-VIO-116 id with the retired gate. The shared id is exactly why
# the dead leg survived this long: it read as a sibling of a live line.
LINES = [("F1 (KB-VIO-116)", 72.41, "above"),
         ("confirm-3 (KB-VIO-123)", 75.5, "above"),
         ("N1 stand-down", 66.0, "below")]


def fetch_primary(timeout: int = 30) -> list[tuple[str, float]]:
    """investing.com historical table via __NEXT_DATA__. Returns [(iso_date, close)] newest-first."""
    html = urllib.request.urlopen(
        urllib.request.Request(URL, headers=UA), timeout=timeout).read().decode("utf-8", "replace")
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.S)
    if not m:
        raise RuntimeError("__NEXT_DATA__ block absent — investing.com markup changed")
    blob = json.loads(m.group(1))
    try:
        rows = blob["props"]["pageProps"]["state"]["historicalDataStore"]["historicalData"]["data"]
    except (KeyError, TypeError) as e:
        raise RuntimeError(f"historicalDataStore path moved: {e}")
    out = []
    for r in rows:
        ts = r.get("rowDateTimestamp") or ""
        close = (r.get("last_close") or "").replace(",", "")
        if ts[:10] and close:
            try:
                out.append((ts[:10], float(close)))
            except ValueError:
                continue
    if not out:
        raise RuntimeError("parsed 0 usable rows")
    return sorted(out, key=lambda x: x[0], reverse=True)


def fetch_crosscheck() -> tuple[str, float] | None:
    """yfinance ^MOVE. KNOWN-UNRELIABLE — may only flag, never promote."""
    try:
        import yfinance as yf
        h = yf.Ticker("^MOVE").history(period="5d")
        if len(h) == 0:
            return None
        return (h.index[-1].date().isoformat(), float(h["Close"].iloc[-1]))
    except Exception:
        return None


def read_ledger() -> dict[str, str]:
    if not LEDGER.exists():
        return {}
    rows = LEDGER.read_text().splitlines()
    return {ln.split("\t")[0]: ln for ln in rows[1:] if ln.strip()}


def write_ledger(new: list[tuple[str, float, str, str]]) -> tuple[int, int]:
    """Upsert by date. Returns (added, updated)."""
    header = "date\tclose\tsource\tcross_check\n"
    existing = read_ledger()
    added = updated = 0
    for d, c, src, xc in new:
        line = f"{d}\t{c:.2f}\t{src}\t{xc}"
        if d not in existing:
            existing[d] = line; added += 1
        elif existing[d] != line:
            existing[d] = line; updated += 1
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(header + "\n".join(existing[k] for k in sorted(existing)) + "\n")
    return added, updated


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--boot", action="store_true", help="concise output for boot.py")
    ap.add_argument("--strict", action="store_true", help="exit 1 if the primary failed")
    ap.add_argument("--history", type=int, default=0, help="print the last N sessions")
    a = ap.parse_args()

    primary, perr = [], None
    try:
        primary = fetch_primary()
    except Exception as e:
        perr = f"{type(e).__name__}: {e}"

    xc = fetch_crosscheck()

    if not primary:
        print(f"  🔴 MOVE PRIMARY FAILED — {perr}")
        if xc:
            print(f"  ⚠️  FALLBACK [UNCORROBORATED — known-unreliable source]: {xc[1]:.2f} [{xc[0]}] via yfinance ^MOVE.")
            print(f"      Do NOT bank a threshold on this. yfinance froze at 70.88 for 17 sessions in Jul-2026 (KB-VIO-177).")
            return 1 if a.strict else 0
        print("  🔴 NO SOURCE RETURNED A VALUE — MOVE is dark. Escalate; do not infer.")
        return 2

    d, c = primary[0]
    prev = primary[1] if len(primary) > 1 else None

    # cross-check: agreement on a shared bar is WEAK; disagreement is the signal
    pm = dict(primary)
    if xc and xc[0] in pm:
        delta = abs(pm[xc[0]] - xc[1])
        xc_state = "agrees" if delta < 0.005 else f"DISAGREES by {delta:.2f}"
    elif xc:
        xc_state = f"stale ({xc[0]}, primary has {d})"
    else:
        xc_state = "unavailable"

    added, updated = write_ledger([(dd, cc, "investing.com", xc_state if dd == d else "") for dd, cc in primary])

    chg = f"{c - prev[1]:+.2f}" if prev else "n/a"
    print(f"  MOVE [{d}]: {c:.2f}  ({chg} vs {prev[0] if prev else '—'})   [PRIMARY investing.com]")
    if xc_state.startswith("DISAGREES"):
        print(f"  🔴 CROSS-CHECK {xc_state} — yfinance says {xc[1]:.2f}. PRIMARY WINS; investigate before citing.")
    elif not a.boot:
        print(f"     cross-check (yfinance, known-unreliable): {xc_state}")

    for name, lvl, side in LINES:
        met = c > lvl if side == "above" else c < lvl
        mark = "✅" if met else "⬜"
        print(f"     {mark} {name:26s} {side} {lvl:>6.2f}   margin {c - lvl:+6.2f}")

    if a.history:
        print(f"\n     last {a.history} sessions:")
        for dd, cc in primary[:a.history]:
            print(f"       {dd}  {cc:7.2f}")

    if added or updated:
        print(f"  ✓ MOVE.tsv: +{added} new, {updated} updated ({len(read_ledger())} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
