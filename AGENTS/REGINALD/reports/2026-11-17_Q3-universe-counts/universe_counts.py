#!/usr/bin/env python3
"""Q3 2026 full-universe counts from the FFIEC CDR bulk Call Report files (single period, TSV).

Usage: universe_counts.py <dir_q1> <dir_q2> <dir_q3>
Each dir holds the unzipped "FFIEC CDR Call Bulk All Schedules MMDDYYYY.zip".

(a) Friedberg "95 of 4,295" like-for-like test, plan: reports/2026-11-01_Q3-call-report_VLY-EGBN-HBAN/REPORT.md section 4
    A  existing unrealized securities loss / equity (GAAP 3210 and tangible 3210-2143), pretax and after 21% tax
    B  additional loss from a rate shock, duration PROXY from RC-B Memo 2 maturity/repricing buckets (assumptions below)
    C  actual quarterly equity decline, 3210 Q2 -> Q3
    D  A relative to CET1 (RC-R P859), with the AOCI opt-out election (P838) shown
(e) performing modifications to borrowers in financial difficulty (RC-C Memo HK25) UP while
    loans 30-89 days past due (RC-N 1406) DOWN, Q2->Q3, with Q1->Q2 beside it.
Values are in $ thousands as filed. RCFD (031 filers) is used when present, else RCON.
"""
import csv, glob, os, statistics, sys

csv.field_size_limit(10**9)


def por(d):
    """IDRSSD -> institution name from the bulk POR file (the official filer list)."""
    f = glob.glob(os.path.join(d, "FFIEC CDR Call Bulk POR *.txt"))[0]
    with open(f, encoding="latin-1", newline="") as fh:
        rows = csv.reader(fh, delimiter="\t"); next(rows)
        return {r[0].strip().strip('"'): r[5].strip() for r in rows if r and r[0].strip()}


def load(d):
    """Return {rssd: {code: value_str}} merged across every schedule file in dir d, POR filers only."""
    keep = por(d)
    out = {}
    for f in glob.glob(os.path.join(d, "FFIEC CDR Call Schedule *.txt")):
        with open(f, encoding="latin-1", newline="") as fh:
            rows = csv.reader(fh, delimiter="\t")
            codes = [c.strip('"') for c in next(rows)]
            next(rows)  # description row
            for r in rows:
                if not r or not r[0].strip().strip('"'):
                    continue
                rssd = r[0].strip().strip('"')
                if rssd not in keep:
                    continue
                rec = out.setdefault(rssd, {})
                for c, v in zip(codes[1:], r[1:]):
                    v = v.strip().strip('"')
                    if v != "" and c not in rec:
                        rec[c] = v
    return out


def num(rec, item, prefixes=("RCFD", "RCON")):
    for p in prefixes:
        v = rec.get(p + item)
        if v not in (None, ""):
            try:
                return float(v)
            except ValueError:
                return None
    return None


# B: duration proxy per RC-B Memo 2 bucket (years). Judgment, stated, not measured.
DUR = {
    # Treasury/agency/other non-MBS debt by remaining maturity or next repricing
    "A549": 0.1, "A550": 0.6, "A551": 1.9, "A552": 3.7, "A553": 7.5, "A554": 13.0,
    # residential mortgage pass-throughs by remaining maturity or repricing (prepayment-shortened)
    "A555": 0.1, "A556": 0.6, "A557": 1.9, "A558": 3.5, "A559": 5.5, "A560": 6.5,
    # other MBS by expected average life
    "A561": 1.5, "A562": 5.0,
}


def measures(rec):
    eq = num(rec, "3210")
    intang = num(rec, "2143") or 0.0
    afs_c, afs_f = num(rec, "1772"), num(rec, "1773")
    htm_c, htm_f = num(rec, "1754"), num(rec, "1771")
    if eq is None:
        return None
    ul = 0.0
    have = False
    if afs_c is not None and afs_f is not None:
        ul += afs_c - afs_f; have = True
    if htm_c is not None and htm_f is not None:
        ul += htm_c - htm_f; have = True
    dv = sum((num(rec, k) or 0.0) * d for k, d in DUR.items())  # $k-years
    cet1 = num(rec, "P859", ("RCFA", "RCOA"))
    optout = rec.get("RCOAP838") or rec.get("RCFAP838")
    cblr = rec.get("RCOALE74") or rec.get("RCFALE74")
    return dict(eq=eq, teq=eq - intang, ul=ul if have else None, dv=dv, cet1=cet1,
                optout=optout, cblr=cblr,
                hk25=num(rec, "HK25"), pd3089=num(rec, "1406"), loans=num(rec, "2122"),
                assets=num(rec, "2170"),
                ni=num(rec, "4340", ("RIAD",)), oci=num(rec, "B511", ("RIAD",)),
                div=(num(rec, "4460", ("RIAD",)) or 0) + (num(rec, "4470", ("RIAD",)) or 0))


def count_ge(vals, thr):
    return sum(1 for v in vals if v is not None and v >= thr)


def main():
    q1, q2, q3 = (load(d) for d in sys.argv[1:4])
    M = {k: {r: measures(rec) for r, rec in q.items()} for k, q in (("q1", q1), ("q2", q2), ("q3", q3))}
    print(f"filers: q1 {len(q1)}  q2 {len(q2)}  q3 {len(q3)}")

    print("\n(a) A: existing unrealized securities loss as a share of equity")
    for k in ("q2", "q3"):
        rows = [m for m in M[k].values() if m and m["ul"] is not None]
        pos = [m for m in rows if m["eq"] > 0]
        tpos = [m for m in rows if m["teq"] > 0]
        for tax, f in (("pretax", 1.0), ("after 21% tax", 0.79)):
            g = [m["ul"] * f / m["eq"] for m in pos]
            t = [m["ul"] * f / m["teq"] for m in tpos]
            print(f"  {k} {tax:14s}: GAAP equity >=20%: {count_ge(g, .20)} of {len(pos)} "
                  f"({count_ge(g, .20)/len(pos):.1%}) | tangible >=20%: {count_ge(t, .20)} of {len(tpos)} "
                  f"({count_ge(t, .20)/len(tpos):.1%}) | median GAAP {statistics.median(g):.1%}")
        neg = sum(1 for m in rows if m["eq"] <= 0)
        print(f"  {k} equity <= 0 excluded: {neg}; filers with no securities lines: {sum(1 for m in M[k].values() if m and m['ul'] is None)}")

    print("\n(a) B: additional loss from a parallel rate shock, duration proxy (stated buckets)")
    rows = [m for m in M["q3"].values() if m and m["eq"] > 0]
    for bp in (100, 200, 300):
        g = [m["dv"] * bp / 10000 / m["eq"] for m in rows]
        g2 = [((m["ul"] or 0) + m["dv"] * bp / 10000) / m["eq"] for m in rows]
        print(f"  q3 +{bp}bp: shock loss alone >=20% of equity: {count_ge(g, .20)} of {len(rows)} ({count_ge(g, .20)/len(rows):.1%}) "
              f"| existing + shock >=20%: {count_ge(g2, .20)} ({count_ge(g2, .20)/len(rows):.1%})")

    names = por(sys.argv[3])
    for a, b in (("q1", "q2"), ("q2", "q3")):
        print(f"\n(a) C: actual equity decline {a} -> {b} (3210); quarter flows = RI-A YTD differences")
        both = [(r, M[a][r], M[b][r]) for r in M[b] if r in M[a] and M[a][r] and M[b][r] and M[a][r]["eq"] > 0]
        ch = [(c["eq"] - p["eq"]) / p["eq"] for _, p, c in both]
        hits = [(r, p, c) for r, p, c in both if (c["eq"] - p["eq"]) / p["eq"] <= -0.20]
        # main driver of the decline: the largest negative of quarter net income, OCI, dividends (as negative), residual
        drv = {"net loss": 0, "OCI": 0, "dividends": 0, "other (capital, merger, treasury)": 0}
        for r, p, c in hits:
            d_eq = c["eq"] - p["eq"]
            q_ni = (c["ni"] or 0) - (p["ni"] or 0) if a != "q1" or True else 0
            q_oci = (c["oci"] or 0) - (p["oci"] or 0)
            q_div = -((c["div"] or 0) - (p["div"] or 0))
            rest = d_eq - q_ni - q_oci - q_div
            k = min((("net loss", q_ni), ("OCI", q_oci), ("dividends", q_div), ("other (capital, merger, treasury)", rest)), key=lambda x: x[1])[0]
            drv[k] += 1
        print(f"  matched {len(both)}; declines >=20%: {len(hits)} ({len(hits)/len(both):.2%}); >=10%: {sum(1 for x in ch if x <= -.10)}; median {statistics.median(ch):.2%}")
        print(f"  largest single driver among the >=20% declines: {drv}")
        big = sorted(hits, key=lambda h: -h[1]["eq"])[:8]
        print("  largest by prior equity: " + "; ".join(f"{names.get(r, r)[:34]} {(c['eq']-p['eq'])/p['eq']:.1%} ({p['eq']/1e3:,.1f}M -> {c['eq']/1e3:,.1f}M)" for r, p, c in big))

    print("\n(a) D: unrealized loss (after tax) vs CET1, Q3")
    rows = [m for m in M["q3"].values() if m and m["ul"] is not None and m["cet1"] and m["cet1"] > 0]
    g = [m["ul"] * .79 / m["cet1"] for m in rows]
    hitrows = [m for m, x in zip(rows, g) if x >= .20]
    oo = sum(1 for m in hitrows if m["optout"] == "1")
    print(f"  CET1 reported: {len(rows)}; >=20% of CET1: {len(hitrows)} ({len(hitrows)/len(rows):.1%}); "
          f"of those, AOCI opt-out = 1: {oo} (their AFS AOCI is excluded from CET1, so the loss is not a regulatory capital hit unless realized); "
          f"opt-out across all CET1 reporters: {sum(1 for m in rows if m['optout'] == '1')}")
    cb = sum(1 for m in M["q3"].values() if m and m["cblr"] == "1")
    print(f"  community bank leverage ratio opt-in filers (P838/LE74 read as filed): {cb}")

    print("\n(e) performing modifications (HK25) UP while 30-89 past due (1406) DOWN")
    for a, b in (("q1", "q2"), ("q2", "q3")):
        pairs = [(M[a][r], M[b][r]) for r in M[b] if r in M[a] and M[a][r] and M[b][r]]
        clean = [(p, c) for p, c in pairs if None not in (p["hk25"], c["hk25"], p["pd3089"], c["pd3089"])]
        hit = [(p, c) for p, c in clean if c["hk25"] > p["hk25"] and c["pd3089"] < p["pd3089"]]
        tl = sum(c["loans"] or 0 for _, c in clean)
        hl = sum(c["loans"] or 0 for _, c in hit)
        mods_up = sum(1 for p, c in clean if c["hk25"] > p["hk25"])
        pd_dn = sum(1 for p, c in clean if c["pd3089"] < p["pd3089"])
        print(f"  {a}->{b}: matched {len(pairs)}, both items reported {len(clean)}; HK25 up {mods_up}; 1406 down {pd_dn}; "
              f"BOTH: {len(hit)} ({len(hit)/len(clean):.1%} of banks, {hl/tl:.1%} of loans); "
              f"system HK25 {sum(p['hk25'] for p,_ in clean)/1e6:.2f}B -> {sum(c['hk25'] for _,c in clean)/1e6:.2f}B, "
              f"1406 {sum(p['pd3089'] for p,_ in clean)/1e6:.2f}B -> {sum(c['pd3089'] for _,c in clean)/1e6:.2f}B")


if __name__ == "__main__":
    main()
