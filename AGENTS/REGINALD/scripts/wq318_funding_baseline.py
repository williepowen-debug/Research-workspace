#!/usr/bin/env python3
"""WQ-318 funding-vs-nonbank baseline — FUNDING legs from the FFIEC Call Report (bank level).

Built 2026-10-07 for DOCKET L527 (Will-approved WQ-318, 9/28). One basis for all six banks
(the Call Report), so the cross-bank columns are comparable; holding-company 10-Q figures are a
DIFFERENT basis and are carried separately in the report, never merged here.

Columns (all $K unless a pct):
  ib_dep_cost_pct  = annualised quarterly interest on deposits / RC-K quarterly-average IB deposits
                     interest: RI 2.a  = RIAD4508 + RIAD0093 + RIADHK03 + RIADHK04 (+ RIAD4172 foreign)
                     RI is YEAR-TO-DATE -> quarter = YTD(q) - YTD(q-1) within the calendar year
                     average:  RC-K    = RCON3485 + RCONB563 + RCONHK16 + RCONHK17 (+ RCFN3404 foreign)
                     annualised by 365 / days-in-quarter
  ib_dep_cost_pe_pct = same interest / average of period-end RC 13.a.(2) IB deposits (q-1, q) — CROSS-CHECK basis
  rck_avg_to_pe_ib = RC-K average / period-end IB; a value far from 1.0 flags a definitional gap between the two
  nib_share_pct    = RC 13.a.(1) NIB / (NIB + IB)  [RCON6631 / (RCON6631 + RCON6636), + RCFN foreign]
  uninsured_pct    = RC-O Memo 2 RCON5597 / RC 13.a RCON2200 (domestic offices only — RC-O basis)
  brokered_pct     = RC-E Memo 1.b RCON2365 / RCON2200 ; reciprocal = RC-E Memo 1.g RCONJH83 (shown, not netted)
  fhlb_adv_K       = RC-M 5.a.(1)(a)-(d) RCONF055..F058, RCFD prefix on 031 filers (FHLB advances by remaining maturity)
  other_borr_K     = RC-M 5.c RCON3190 (TOTAL other borrowed money, INCLUDES FHLB advances)
  ffp_repo_K       = RC 14.a RCONB993 + 14.b RCONB995 / RCFDB995 (031)
  wholesale_pct    = (other_borr_K + ffp_repo_K) / total liabilities (RC 21, RCON2948 or RCFD2948)
  fhlb_pct_liab    = fhlb_adv_K / total liabilities
Zero != unknown: a missing MDRM is written as blank and named in `missing`, never coerced to 0.

Reuses the CDR client in mi3_cohort_screen.py (creds/facsimile/parse). Cache /tmp/mi3/fac.
Run:  .venv/bin/python3 AGENTS/REGINALD/scripts/wq318_funding_baseline.py
"""
import csv, sys, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mi3_cohort_screen as m   # noqa: E402

BANKS = [("CUBI", 2354985), ("CFG", 3303298), ("WAL", 3138146), ("OZK", 107244),
         ("FLG", 694904), ("EGBN", 2652092)]
QUARTERS = ["6/30/2025", "9/30/2025", "12/31/2025", "3/31/2026", "6/30/2026"]
OUT = m.ROOT / "AGENTS/REGINALD/workbook/FUNDING_COHORT_2026Q2.tsv"

INT_DOM = ["RIAD4508", "RIAD0093", "RIADHK03", "RIADHK04"]
INT_FOR = ["RIAD4172"]
AVG_DOM = ["RCON3485", "RCONB563", "RCONHK16", "RCONHK17"]
AVG_FOR = ["RCFN3404"]
FHLB = ["RCONF055", "RCONF056", "RCONF057", "RCONF058"]


def g(d, k):
    return d.get(k)


def ssum(d, keys, missing, required=True):
    vals = [d.get(k) for k in keys]
    if any(v is None for v in vals):
        absent = [k for k, v in zip(keys, vals) if v is None]
        if required:
            missing.extend(absent)
            return None
        return sum(v for v in vals if v is not None)
    return sum(vals)


def qdays(q):
    mth, day, yr = (int(x) for x in q.split("/"))
    end = dt.date(yr, mth, day)
    start_m = mth - 2
    start = dt.date(yr, start_m, 1)
    return (end - start).days + 1


def main():
    u, t = m.creds()
    rows = []
    for tk, rssd in BANKS:
        data = {}
        for q in QUARTERS:
            txt = m.facsimile(u, t, rssd, q)
            if not txt:
                sys.exit(f"FETCH FAILED {tk} {rssd} {q} — nothing written")
            data[q] = m.parse(txt)
        for i, q in enumerate(QUARTERS):
            d = data[q]
            missing = []
            foreign = any(k in d for k in ("RCFN3404", "RIAD4172", "RCFN6631"))
            ytd = ssum(d, INT_DOM, missing)
            if ytd is not None and foreign:
                ytd += sum(d.get(k, 0) for k in INT_FOR)
            # quarter interest = YTD difference within calendar year
            if q.startswith("3/31"):
                qint = ytd
            elif i == 0:
                qint = None   # 6/30/2025 needs 3/31/2025 YTD; not pulled (baseline row only)
            else:
                prev = data[QUARTERS[i - 1]]
                pm = []
                pytd = ssum(prev, INT_DOM, pm)
                if pytd is not None and foreign:
                    pytd += sum(prev.get(k, 0) for k in INT_FOR)
                qint = (ytd - pytd) if (ytd is not None and pytd is not None) else None
            avg = ssum(d, AVG_DOM, missing)
            if avg is not None and foreign:
                avg += sum(d.get(k, 0) for k in AVG_FOR)
            cost = round(qint * 365 / qdays(q) / avg * 100, 2) if (qint is not None and avg) else None
            # cross-check basis: average of period-end IB deposits (RC 13.a.(2)) at q-1 and q
            ib_now = d.get("RCON6636")
            ib_prev = data[QUARTERS[i - 1]].get("RCON6636") if i > 0 else None
            pe_avg = (ib_now + ib_prev) / 2 if (ib_now is not None and ib_prev is not None) else None
            cost_pe = round(qint * 365 / qdays(q) / pe_avg * 100, 2) if (qint is not None and pe_avg) else None
            rck_ratio = round(avg / ib_now, 3) if (avg and ib_now) else None
            nib = g(d, "RCON6631"); ib = g(d, "RCON6636")
            if nib is not None and foreign:
                nib += d.get("RCFN6631", 0); ib = (ib or 0) + d.get("RCFN6636", 0)
            nibs = round(nib / (nib + ib) * 100, 2) if (nib is not None and ib is not None) else None
            dep = g(d, "RCON2200")
            unins = g(d, "RCON5597")
            brok = g(d, "RCON2365"); recip = g(d, "RCONJH83")
            # 031 filers (CFG, FLG) report RC-M 5 and RC 14.b on the RCFD (consolidated) prefix
            fhlb = ssum(d, FHLB, [], required=True)
            if fhlb is None:
                fhlb = ssum(d, [k.replace("RCON", "RCFD") for k in FHLB], missing)
            ob = g(d, "RCON3190") if "RCON3190" in d else g(d, "RCFD3190")
            ffp = sum(d.get(k) or 0 for k in ("RCONB993", "RCONB995", "RCFDB995"))
            liab = g(d, "RCON2948") if "RCON2948" in d else g(d, "RCFD2948")
            for k, v in (("RCON6631", nib), ("RCON2200", dep), ("RCON5597", unins), ("RCON2365", brok),
                         ("RCON3190", ob), ("2948", liab)):
                if v is None:
                    missing.append(k)
            pct = lambda a, b: round(a / b * 100, 2) if (a is not None and b) else None
            rows.append({
                "Ticker": tk, "RSSD": rssd, "Quarter": q, "filer_form": "031" if foreign else "041",
                "q_int_dep_K": qint, "avg_ib_dep_K": avg, "ib_dep_cost_pct": cost, "ib_dep_cost_pe_pct": cost_pe, "rck_avg_to_pe_ib": rck_ratio,
                "nib_K": nib, "ib_K": ib, "nib_share_pct": nibs,
                "dep_dom_K": dep, "uninsured_K": unins, "uninsured_pct": pct(unins, dep),
                "brokered_K": brok, "brokered_pct": pct(brok, dep), "reciprocal_K": recip,
                "fhlb_adv_K": fhlb, "other_borr_K": ob, "ffp_repo_K": ffp, "total_liab_K": liab,
                "wholesale_pct": pct((ob or 0) + (ffp or 0), liab) if ob is not None else None,
                "fhlb_pct_liab": pct(fhlb, liab),
                "missing": ",".join(sorted(set(missing))) or "-",
            })
    now = dt.datetime.now().strftime("%Y-%m-%d")
    hdr = [
        f"# Last real data refresh: {now} — FFIEC CDR REST/JWT RetrieveFacsimile/SDF, bank-level Call Report, "
        "6 banks x 5 quarters (6/30/25-6/30/26), ALL rows at the FFIEC primary. Written by scripts/wq318_funding_baseline.py.",
        "# PURPOSE: WQ-318 (DOCKET L527) funding legs on ONE basis. Bank-level Call Report != holdco 10-Q; do not mix. "
        "Formulas + MDRMs in the script docstring. Blank = not reported / not derivable (named in `missing`), never 0.",
        "# Cadence: ONE-OFF baseline for WQ-318 (Will: 'no new recurring study'). Q3 re-read only as part of the WQ-318 "
        "observation list grade; not a scheduled refresh.",
    ]
    with open(OUT, "w", newline="") as fh:
        for h in hdr:
            fh.write(h + "\n")
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if v is None else v) for k, v in r.items()})
    print(f"wrote {OUT} rows={len(rows)}")
    for r in rows:
        if r["Quarter"] in ("6/30/2026",):
            print(r["Ticker"], r["filer_form"], "cost", r["ib_dep_cost_pct"], "nib", r["nib_share_pct"],
                  "unins", r["uninsured_pct"], "brok", r["brokered_pct"], "whsl", r["wholesale_pct"],
                  "fhlb", r["fhlb_pct_liab"], "miss", r["missing"])


if __name__ == "__main__":
    main()
