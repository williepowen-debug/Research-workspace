#!/usr/bin/env python3
"""Oil roll guard — resolves a continuous oil ticker to its named contract and FAILS CLOSED if it rolled inside the window.

WHY THIS EXISTS (2026-09-18, SAM). On 2026-09-18 SAM published "Brent -7.5% in three
sessions" into STATUS.md and NEXUS_BRIEF.md. `BZ=F` had stepped Nov `BZX26` -> Dec `BZZ26`
inside that window, so a $4.42 contract spread was reported as an economic decline; the
matched-contract move was -4.48% (Dec) / -5.20% (Nov). TERRY caught the identical roll on the
identical series the same day.

The rule against this was ALREADY WRITTEN, in SAM's CLAUDE.md DO-NOT list AND in the very
STATUS cell that broke it ("never compared across rolls"). It did not fire, because a rule in
a list only fires when a writer remembers to consult it. PROME's count: the seventeenth fleet
instance of correct-rule/absent-wiring. So this check fires on the COMPARISON instead.

⛔ FAIL-CLOSED BY DESIGN. If a date cannot be resolved to a named contract, this reports
UNRESOLVED and exits non-zero. It never reports "no roll" from a failed resolution — an
unresolved window and a clean window must not share an exit code.

TWO MODES, AND THE REASON IS ITSELF A LESSON:
  * INTERROGATION (default, --start/--end): "is this window safe to quote?" A roll exits 2.
  * --boot: a daily heartbeat. Reports the front contract and any roll in the lookback, and
    exits 0 when resolution SUCCEEDED, roll or not. Only UNRESOLVED/UNAVAILABLE exits 2.

Why the split: a roll is a normal monthly event, so a 7-day boot lookback would show one for
about a week every month. A guard that shows red every day for a known-good reason trains its
reader to skip it — which is how this desk already read past `grade_8_14_branch.py` for days,
and is the same desensitization recorded in [[finding_loosening_a_check_to_kill_a_false_alarm_
inverts_the_failure_direction]]. Boot reports the BASIS; the exit code is spent only on the
thing that is actually wrong.
"""
import argparse, sys
from datetime import date, timedelta

MONTH_CODE = {1:'F',2:'G',3:'H',4:'J',5:'K',6:'M',7:'N',8:'Q',9:'U',10:'V',11:'X',12:'Z'}
ROOTS = {'BZ=F':'BZ', 'CL=F':'CL'}
TOL = 0.02          # absolute $ tolerance for matching continuous close to a named contract
N_CANDIDATES = 7    # months forward from window start


def candidates(root, start):
    out = []
    y, m = start.year, start.month
    for _ in range(N_CANDIDATES):
        out.append((f"{root}{MONTH_CODE[m]}{y % 100:02d}.NYM", y, m))
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return out


def closes(ticker, start, end):
    import yfinance as yf
    try:
        h = yf.Ticker(ticker).history(start=start.isoformat(),
                                      end=(end + timedelta(days=1)).isoformat())
    except Exception:
        return {}
    return {i.date(): float(c) for i, c in zip(h.index, h['Close'])} if len(h) else {}


def check(ticker, start, end, verbose=False, boot=False):
    root = ROOTS.get(ticker)
    if not root:
        print(f"UNKNOWN ticker {ticker}: no contract root registered. Cannot resolve — FAIL CLOSED.")
        return 2
    cont = closes(ticker, start, end)
    if not cont:
        print(f"UNAVAILABLE: no continuous data for {ticker} in {start}..{end}. FAIL CLOSED.")
        return 2
    named = {}
    for sym, y, m in candidates(root, start):
        c = closes(sym, start, end)
        if c:
            named[sym] = c
    if not named:
        print(f"UNAVAILABLE: no named contracts resolved for {ticker}. FAIL CLOSED.")
        return 2

    resolved, unresolved = {}, []
    for d in sorted(cont):
        hits = [s for s, c in named.items() if d in c and abs(c[d] - cont[d]) <= TOL]
        if len(hits) == 1:
            resolved[d] = hits[0]
        elif not hits:
            unresolved.append((d, 'no candidate within tolerance'))
        else:
            unresolved.append((d, f'ambiguous: {",".join(sorted(hits))}'))

    print(f"OIL ROLL CHECK — {ticker}  {start}..{end}")
    if verbose:
        for d in sorted(cont):
            print(f"    {d}  {cont[d]:>8.2f}  {resolved.get(d,'UNRESOLVED')}")

    if unresolved:
        print(f"  🔴 UNRESOLVED on {len(unresolved)} session(s) — a roll can NOT be excluded:")
        for d, why in unresolved[:5]:
            print(f"      {d}: {why}")
        print("  ⛔ Do NOT quote a percentage change across this window. FAIL CLOSED.")
        return 2

    seq = [resolved[d] for d in sorted(resolved)]
    contracts = sorted(set(seq))
    if len(contracts) > 1:
        rolls = [(d, seq[i-1], seq[i]) for i, d in enumerate(sorted(resolved)) if i and seq[i] != seq[i-1]]
        print(f"  {'🟠' if boot else '🔴'} ROLL {'in lookback' if boot else 'DETECTED'} — the continuous series changed contract inside this window.")
        for d, a, b in rolls:
            print(f"      {d}: {a} -> {b}")
        d0, d1 = min(resolved), max(resolved)
        print(f"  ⛔ A % change from {d0} to {d1} on {ticker} MIXES CONTRACTS and is not a price move.")
        print("  ✅ Matched-contract changes over the same window:")
        for sym in contracts:
            c = named[sym]
            if d0 in c and d1 in c:
                print(f"      {sym}: {c[d0]:.2f} -> {c[d1]:.2f} = {(c[d1]/c[d0]-1)*100:+.2f}%")
            else:
                print(f"      {sym}: incomplete over the window — no matched change asserted")
        cc = cont[d1]/cont[d0]-1
        print(f"      {ticker} (continuous, NOT a price move): {(cc)*100:+.2f}%")
        if boot:
            print(f"  ➡️  QUOTE THE NAMED CONTRACT: front is now {seq[-1]}. Basis note, not a failure.")
            return 0
        return 2

    print(f"  ✅ NO ROLL — single contract {contracts[0]} across all {len(seq)} session(s).")
    d0, d1 = min(resolved), max(resolved)
    print(f"     {ticker} {d0}->{d1}: {cont[d0]:.2f} -> {cont[d1]:.2f} = {(cont[d1]/cont[d0]-1)*100:+.2f}% (basis-clean)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--ticker', default=None, help='BZ=F or CL=F (default: both)')
    p.add_argument('--start', default=None, help='YYYY-MM-DD')
    p.add_argument('--end', default=None, help='YYYY-MM-DD')
    p.add_argument('--days', type=int, default=10, help='lookback when --start omitted')
    p.add_argument('--verbose', action='store_true')
    p.add_argument('--boot', action='store_true',
                   help='daily heartbeat: report basis, exit 0 unless resolution FAILS')
    a = p.parse_args()
    end = date.fromisoformat(a.end) if a.end else date.today()
    start = date.fromisoformat(a.start) if a.start else end - timedelta(days=a.days)
    tickers = [a.ticker] if a.ticker else ['BZ=F', 'CL=F']
    rc = 0
    for t in tickers:
        r = check(t, start, end, a.verbose, a.boot)
        rc = max(rc, r)
    print("\nA non-zero exit means the window is NOT safe to quote as a percentage change."
          if not a.boot else
          "\nBoot mode: a roll is reported as BASIS, not failure; non-zero here means UNRESOLVED.")
    return rc


if __name__ == '__main__':
    sys.exit(main())
