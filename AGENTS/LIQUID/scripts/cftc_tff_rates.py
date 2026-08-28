#!/usr/bin/env python3
"""
LIQUID — CFTC TFF (Traders in Financial Futures) rates-complex positioning.

Built 2026-08-23 to adjudicate KB-BND-092 (was the 7/27 5Y auction's thin cover a
basis-trade withdrawal?) and to discharge GATE-LIQ-076 leg-(a), overdue since 7/25.

WHY THIS EXISTS: BOND's question is TENOR-LOCAL — "5Y-specific levered position
unwound" vs "nothing happened in funding." The rates complex has a tenor-local
instrument for exactly that: LEVERAGED FUND net position in UST 5Y NOTE futures,
read ALONGSIDE 2Y/10Y/Bond so a 5Y-specific move is separable from a complex-wide one.
A blended or single-tenor read cannot answer it — cf. KB-LIQ-095, an aggregate
cannot see a change in the mix.

BASIS (declare it when citing):
  - Source: CFTC TFF futures-only. Weekly file  https://www.cftc.gov/dea/newcot/FinFutWk.txt
            History (YTD)         https://www.cftc.gov/files/dea/history/fut_fin_txt_2026.zip
  - RAW FILES, NOT Socrata -- Socrata lags (auto-memory finding_cftc_cot_raw_file_beats_socrata_lag).
  - As-of date is a TUESDAY; the file publishes Friday ~15:30 ET. An as-of date is
    NOT the release date -- never label a Friday number with the Friday.
  - Net = Leveraged Fund Long - Leveraged Fund Short. SPREADING is reported separately
    and is EXCLUDED from net by construction; a spread-heavy book can move net without
    changing gross risk, so read Spread alongside Net, never net alone.
  - The weekly file may be one as-of date AHEAD of the YTD history archive. This script
    merges both and prefers the weekly for overlapping dates.

USAGE:
  .venv/bin/python3 AGENTS/LIQUID/scripts/cftc_tff_rates.py                # last 8 as-of dates
  .venv/bin/python3 AGENTS/LIQUID/scripts/cftc_tff_rates.py --since 2026-07-01
  .venv/bin/python3 AGENTS/LIQUID/scripts/cftc_tff_rates.py --contracts "UST 5Y NOTE,SOFR-3M"
"""
import argparse, io, sys, urllib.request, zipfile, csv

WK  = "https://www.cftc.gov/dea/newcot/FinFutWk.txt"
YY  = "https://www.cftc.gov/files/dea/history/fut_fin_txt_2026.zip"
UA  = {"User-Agent": "Mozilla/5.0 (LIQUID-Research)"}

# Column indices, verified 2026-08-23 against the file's own accounting identity
# (Tot_Rept_Long == sum of the four Long legs + the four Spread legs). Do not
# reorder blind -- re-verify the identity if CFTC changes the layout.
I_DATE, I_OI = 2, 7
I_LF_L, I_LF_S, I_LF_SP = 14, 15, 16
I_D_L, I_D_S = 8, 9
I_TR_L, I_TR_S = 20, 21

DEFAULT_CONTRACTS = ["UST 2Y NOTE", "UST 5Y NOTE", "UST 10Y NOTE",
                     "ULTRA UST 10Y", "UST BOND", "ULTRA UST BOND", "SOFR-3M"]


def _get(url, binary=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
        d = r.read()
    return d if binary else d.decode("utf-8", "replace")


def load_rows():
    """Merge YTD history + current weekly. Returns {(contract, date): row}.

    ⚠️ EXCHANGE-COLLISION GUARD, added 2026-08-28 (KB-LIQ-116) after a live near-miss.
    The key deliberately STRIPS the exchange ("SOFR-3M - CHICAGO MERCANTILE EXCHANGE"
    -> "SOFR-3M"), which was safe for every prior week because SOFR-3M futures existed
    on exactly ONE exchange. On the as-of 2026-08-25 file, FMX FUTURES EXCHANGE listed
    its own SOFR-3M contract (OI 167,749 vs CME's 13,036,905) and, keyed identically,
    it SILENTLY OVERWROTE the CME row. The tool then reported LF net -7,967 against the
    prior week's -2,530,893 = a w/w "cover" of +2,522,926, which would have FIRED
    GATE-LIQ-076's W1 leg (>300,000) by more than 8x, on a gate whose fire routes a
    joint write-up to PROME and NEXUS. Nothing in the output looked wrong.
    We now keep the FULL market name in a side index and FAIL LOUD on any collision
    rather than let last-row-wins pick the venue.
    """
    out = {}
    seen = {}          # stripped name -> {full market name: (date, open interest)}
    try:
        z = zipfile.ZipFile(io.BytesIO(_get(YY, binary=True)))
        name = [n for n in z.namelist() if n.lower().endswith(".txt")][0]
        text = z.read(name).decode("utf-8", "replace")
        rows = list(csv.reader(io.StringIO(text)))
        if rows and rows[0][0].startswith("Market_and_Exchange"):
            rows = rows[1:]                       # history file carries a header
        for r in rows:
            if len(r) > I_TR_S:
                k = r[0].split(" - ")[0].strip()
                seen.setdefault(k, {})[r[0].strip()] = (r[I_DATE], r[I_OI])
                out[(k, r[I_DATE])] = r
                out[(r[0].strip(), r[I_DATE])] = r
        src_hist = f"history OK ({len(rows)} rows)"
    except Exception as e:                        # FAIL LOUD, never silently thin
        src_hist = f"history FAILED: {e}"
    try:
        rows = list(csv.reader(io.StringIO(_get(WK))))
        n = 0
        for r in rows:
            if len(r) > I_TR_S and r[0].startswith('"') is False:
                k = r[0].split(" - ")[0].strip()
                seen.setdefault(k, {})[r[0].strip()] = (r[I_DATE], r[I_OI])
                out[(k, r[I_DATE])] = r
                out[(r[0].strip(), r[I_DATE])] = r; n += 1
        src_wk = f"weekly OK ({n} rows)"
    except Exception as e:
        src_wk = f"weekly FAILED: {e}"
    return out, src_hist, src_wk, seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default=None, help="YYYY-MM-DD as-of floor")
    ap.add_argument("--last", type=int, default=8, help="last N as-of dates (ignored with --since)")
    ap.add_argument("--contracts", default=",".join(DEFAULT_CONTRACTS))
    a = ap.parse_args()

    rows, s1, s2, seen = load_rows()
    if not rows:
        print("FATAL: no CFTC rows loaded. " + s1 + " | " + s2); sys.exit(3)
    contracts = [c.strip() for c in a.contracts.split(",") if c.strip()]

    print("=" * 100)
    print("  LIQUID — CFTC TFF rates-complex, LEVERAGED FUND positioning")
    print("  Source: CFTC raw files (NOT Socrata).  " + s1 + " | " + s2)
    print("  As-of dates are TUESDAYS; files publish Fri ~15:30 ET. Net EXCLUDES spreading.")
    print("=" * 100)

    # ---- F1 EXCHANGE-COLLISION CHECK (KB-LIQ-116) — run BEFORE any number is printed ----
    _collided = False
    for c in contracts:
        venues = seen.get(c, {})
        if len(venues) > 1 and ' - ' not in c:
            _collided = True
            print("\n  " + "!" * 92)
            print(f"  🔴 INSTRUMENT-FAULT — '{c}' matches {len(venues)} MARKETS. Keyed identically, LAST ROW WINS,")
            print(f"     so the figures below may be the WRONG VENUE. Rows are NOT comparable across exchanges.")
            for full, (d, oi) in sorted(venues.items(), key=lambda kv: -int(kv[1][1] or 0)):
                print(f"       · {full:<52} latest {d}  OI {int(oi or 0):>12,}")
            print(f"     ⇒ RE-RUN with the FULL market name, e.g. --contracts \"{max(venues, key=lambda f: int(venues[f][1] or 0))}\"")
            print("     ⛔ DO NOT GRADE A GATE OFF A COLLIDED ROW.")
            print("  " + "!" * 92)
    if _collided:
        print("\n  (continuing, but every collided contract above is UNSAFE for grading)\n")

    for c in contracts:
        dates = sorted(d for (k, d) in rows if k == c)
        if not dates:
            print("\n  " + c + ": NO ROWS — contract name not matched (check spelling against the file)")
            continue
        sel = [d for d in dates if d >= a.since] if a.since else dates[-a.last:]
        print("\n  " + c + "   (" + str(len(dates)) + " as-of dates in file; showing " + str(len(sel)) + ")")
        print("    {:<12} {:>12} {:>12} {:>12} {:>12} {:>11} {:>12}".format(
            "as-of", "LevF Long", "LevF Short", "LevF NET", "w/w ΔNET", "LevF Spread", "Open Int"))
        prev = None
        for d in sel:
            r = rows[(c, d)]
            L, S, SP = int(r[I_LF_L]), int(r[I_LF_S]), int(r[I_LF_SP])
            net = L - S
            dn = "" if prev is None else "{:+,}".format(net - prev)
            print("    {:<12} {:>12,} {:>12,} {:>12,} {:>12} {:>11,} {:>12,}".format(
                d, L, S, net, dn, SP, int(r[I_OI])))
            prev = net
    print("\n" + "=" * 100)


if __name__ == "__main__":
    main()
