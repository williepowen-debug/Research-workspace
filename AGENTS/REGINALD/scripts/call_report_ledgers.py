#!/usr/bin/env python3
"""Quarterly refresh of NDFI_COHORT, ACL_ROLLFORWARD_COHORT and RUNWAY_COHORT.

Built 2026-11-07: the three ledgers were hand-built on 8/20 and had no builder.
Reuses mi3_cohort_screen.py for creds, COHORT and the FFIEC facsimile fetch.

    python3 AGENTS/REGINALD/scripts/call_report_ledgers.py --quarter 9/30/2026          # reproduce, no write
    python3 AGENTS/REGINALD/scripts/call_report_ledgers.py --quarter 9/30/2026 --write  # append and rewrite

Before any write it recomputes every existing row from the primary and prints
each difference. A difference blocks the write unless --accept-diffs names why.

BASIS, kept exactly as built 8/20 so the series continue:
  NDFI  loans, item 9.a and Memo 10 prefer RCON (domestic offices at FFIEC 031
        filers); RC-L 1.e.3 and RC-N M9 are RCFD at those filers (consolidated).
  ACL   chargeoffs_K = RIADC079, RI-B Part II charge-offs. It EXCLUDES RIAD5523,
        write-downs on transfer. identity_ties = B522 + 4605 + 4230 - C079 == 3123,
        which omits RIAD5523 and RIADC233. The Notes column carries both and the
        full identity for every row that fails the as-built test.
  RUNWAY per-quarter = YTD differenced, Q1 = YTD; TTM = four quarters; runway = ACL / TTM.
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import mi3_cohort_screen as m  # noqa: E402

W = Path(__file__).resolve().parents[1] / "workbook"
NDFI, ACL, RUNWAY = W / "NDFI_COHORT.tsv", W / "ACL_ROLLFORWARD_COHORT.tsv", W / "RUNWAY_COHORT.tsv"
RSSD = {t: r for t, r, *_ in m.COHORT}


def key(q):
    return dt.datetime.strptime(q, "%m/%d/%Y")


def read(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    head = [x for x in lines if x.startswith("#")]
    body = [x for x in lines if not x.startswith("#")]
    cols = body[0].split("\t")
    return head, cols, [dict(zip(cols, b.split("\t"))) for b in body[1:]]


def write(path, head, cols, rows):
    text = "\n".join(head + ["\t".join(cols)] + ["\t".join(r[c] for c in cols) for r in rows]) + "\n"
    path.write_bytes(text.encode("utf-8"))


def fetch(creds, rssd, q):
    sdf = m.facsimile(creds[0], creds[1], rssd, q)
    if sdf is None:
        sys.exit(f"facsimile missing: RSSD {rssd} {q}")
    return m.parse(sdf)


def one(d, code, prefixes=("RCON", "RCFD")):
    for p in prefixes:
        if p + code in d:
            return d[p + code]
    return None


def s(v):
    return "UNKNOWN" if v is None else str(v)


def pct(a, b):
    return "UNKNOWN" if a is None or not b else f"{100 * a / b:.2f}"


def ndfi_row(base, d, q):
    r = dict(base)
    loans, total = one(d, "2122"), one(d, "J454")
    ma, mb, mc, md, me = [one(d, "PV0" + str(i)) for i in (5, 6, 7, 8, 9)]
    pc = None if mb is None or mc is None else mb + mc
    r.update(Quarter=q, TotalLoans_K=s(loans), NDFI_total_K=s(total), NDFI_pct_loans=pct(total, loans),
             M10a_mortgage_K=s(ma), M10b_business_K=s(mb), M10c_privateequity_K=s(mc),
             M10d_consumer_K=s(md), M10e_other_K=s(me), PC_NDFI_K=s(pc), PC_NDFI_pct_loans=pct(pc, loans),
             Unfunded_NDFI_K=s(one(d, "PV11")), NDFI_nonaccrual_K=s(one(d, "PV25")),
             NDFI_30_89_K=s(one(d, "PV23")), NDFI_90plus_K=s(one(d, "PV24")), Notes=base.get("Notes", ""))
    return r


def acl_row(t, q, d):
    begin, rec, prov, co, end = [d.get(k) for k in ("RIADB522", "RIAD4605", "RIAD4230", "RIADC079", "RIAD3123")]
    wd, adj = d.get("RIAD5523", 0), d.get("RIADC233", 0)
    tie = begin + rec + prov - co == end
    full = begin + rec + prov - co - wd + adj == end
    return {"Ticker": t, "Quarter": q, "ACL_begin_K": str(begin), "recoveries_K": str(rec),
            "provision_K": str(prov), "chargeoffs_K": str(co), "ACL_end_K": str(end),
            "CO_over_prov": f"{co / prov:.2f}" if prov > 0 else "UNDEFINED-prov<=0",
            "identity_ties": "YES" if tie else "NO",
            "Notes": "" if tie else f"writedowns_5523={wd} adj_C233={adj} full_identity={'YES' if full else 'NO'}"}


def runway_rows(acl):
    out = []
    for t in sorted({r["Ticker"] for r in acl}):
        rows = sorted([r for r in acl if r["Ticker"] == t], key=lambda r: key(r["Quarter"]))
        flows, prior = [], None
        for r in rows:
            d = key(r["Quarter"])
            co, pv = int(r["chargeoffs_K"]), int(r["provision_K"])
            if d.month == 3:
                pc, pp, basis = co, pv, "Q1=YTD"
            elif prior is not None and key(prior["Quarter"]).year == d.year:
                pc, pp, basis = co - int(prior["chargeoffs_K"]), pv - int(prior["provision_K"]), "YTD-diff"
            else:
                pc, pp, basis = None, None, "UNKNOWN-no-prior-in-year"
            flows.append((pc, r["identity_ties"]))
            row = {"Ticker": t, "Quarter": r["Quarter"], "ACL_K": r["ACL_end_K"], "per_chargeoffs_K": s(pc),
                   "per_provision_K": s(pp), "basis": basis, "TTM_chargeoffs_K": "", "runway_years": "",
                   "window_has_nontie": "", "quarter_ties": r["identity_ties"]}
            win = flows[-4:]
            if len(win) == 4 and all(x[0] is not None for x in win):
                ttm = sum(x[0] for x in win)
                row["TTM_chargeoffs_K"] = str(ttm)
                row["runway_years"] = f"{int(r['ACL_end_K']) / ttm:.4f}" if ttm > 0 else ""
                row["window_has_nontie"] = "YES" if any(x[1] == "NO" for x in win) else "no"
            out.append(row)
            prior = r
    return out


def diff(label, old, new, cols):
    n = 0
    for c in cols:
        if old.get(c, "") != new.get(c, ""):
            n += 1
            print(f"  DIFF {label} {old.get('Ticker')} {old.get('Quarter')} {c}: ledger {old.get(c)!r} primary {new.get(c)!r}")
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quarter", required=True)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--accept-diffs", default="", help="reason, required to write over a reproduction difference")
    a = ap.parse_args()
    q, creds, diffs = a.quarter, m.creds(), 0

    h_n, c_n, n_rows = read(NDFI)
    prev = max({r["Quarter"] for r in n_rows}, key=key)
    fresh = []
    for r in [x for x in n_rows if x["Quarter"] == prev]:
        diffs += diff("NDFI", r, ndfi_row(r, fetch(creds, int(r["RSSD"]), prev), prev), c_n)
        fresh.append(ndfi_row(r, fetch(creds, int(r["RSSD"]), q), q))

    h_a, c_a, a_rows = read(ACL)
    checked = []
    for r in a_rows:
        new = acl_row(r["Ticker"], r["Quarter"], fetch(creds, RSSD[r["Ticker"]], r["Quarter"]))
        diffs += diff("ACL", r, new, [c for c in c_a if c not in ("recoveries_K", "Notes")])
        new["CO_over_prov"], new["identity_ties"] = r["CO_over_prov"], r["identity_ties"]
        checked.append(new)
    a_new = checked + [acl_row(t, q, fetch(creds, RSSD[t], q)) for t in sorted(RSSD)
                       if not any(x["Ticker"] == t and x["Quarter"] == q for x in checked)]

    h_r, c_r, r_rows = read(RUNWAY)
    built = {(x["Ticker"], x["Quarter"]): x for x in runway_rows(a_new)}
    for r in r_rows:
        diffs += diff("RUNWAY", r, built[(r["Ticker"], r["Quarter"])], c_r)

    print(f"reproduction differences: {diffs}; prior NDFI quarter {prev}; new NDFI rows {len(fresh)}; "
          f"ACL rows {len(a_new)}; RUNWAY rows {len(built)}")
    if not a.write:
        return 0
    if diffs and not a.accept_diffs:
        sys.exit("differences found: not written; pass --accept-diffs '<reason>' after reading them")
    if any(r["Quarter"] == q for r in n_rows):
        sys.exit(f"{q} already in NDFI ledger: not written")
    write(NDFI, h_n, c_n, n_rows + fresh)
    write(ACL, h_a, c_a, sorted(a_new, key=lambda r: (r["Ticker"], r["Quarter"])))
    write(RUNWAY, h_r, c_r, sorted(built.values(), key=lambda r: (r["Ticker"], key(r["Quarter"]))))
    print("written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
