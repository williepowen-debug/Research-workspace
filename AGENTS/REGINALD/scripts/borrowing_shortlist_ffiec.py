#!/usr/bin/env python3
"""Early Q3 read of WHO borrowed — FFIEC CDR Call Reports for a target list, before the FDIC posts.

Companion to scripts/borrowing_screen.py (full universe, FDIC, ~mid/late Nov). This pulls 9/30/2026
Call Reports from the FFIEC CDR (REST/JWT; token expires 2026-11-05) for:
  the 14 cohort banks + the Q2 dry run's flagged banks and 20 largest increases (Will's short list)
  + the 100 largest small commercial banks by Q2 assets (coverage extension, ~58% of borrowings).
Baseline (6/30/2026) = the FDIC dry-run TSV. The cohort is ALSO pulled from FFIEC for 6/30 and must
equal the FDIC figures (route check). Flags use the FROZEN thresholds in borrowing_screen.py and
reports/2026-10-28_borrowing-screen_FROZEN_rule.md. Concentration needs the full universe and is
NOT computed here.

MDRMs (verified 2026-10-28 against FDIC for Amerant and Western Alliance, 6/30/2026, exact):
  borrowings = 3190 other borrowed money + B993 fed funds purchased + B995 repos (RCFD, else RCON)
  FHLB = F055+F056+F057+F058 · deposits = RCON2200 + RCFN2200 (if filed) · assets = 2170 · brokered = RCON2365
A bank whose 9/30 report is not yet available is listed PENDING (not filed, or route error); re-run
to fill it — successful pulls are cached in /tmp/mi3/fac and not re-fetched.

Usage (repo root): .venv/bin/python3 AGENTS/REGINALD/scripts/borrowing_shortlist_ffiec.py [--out DIR]
Exit: 0 = ran (some banks may be PENDING) · 2 = route check failed (cohort 6/30 FFIEC != FDIC) or creds missing.
"""
import argparse, csv, os, sys
from datetime import datetime
sys.path.insert(0, os.path.dirname(__file__))
import mi3_cohort_screen as m
import borrowing_screen as bs

ROOT = str(m.ROOT)
DRY = os.path.join(ROOT, "AGENTS/REGINALD/domain/sources/2026-10-28_boot/borrowing_screen_dryrun/borrowing_screen_20260331_20260630.tsv")
PRIOR, CUR = "6/30/2026", "9/30/2026"


def first(d, codes):
    for p in ("RCFD", "RCON"):
        if all(p + c in d for c in codes):
            return sum(d[p + c] for c in codes)
    return None


def extract(d):
    b = first(d, ["3190"])
    ff = d.get("RCONB993", d.get("RCFDB993", 0))
    rp = d.get("RCFDB995", d.get("RCONB995", 0))
    dep = d.get("RCON2200")
    if dep is not None:
        dep += d.get("RCFN2200", 0)
    return dict(bor=None if b is None else b + ff + rp, fhlb=first(d, ["F055", "F056", "F057", "F058"]),
                dep=dep, asset=first(d, ["2170"]), bro=d.get("RCON2365"))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out"); a = ap.parse_args()
    user, tok = m.creds()
    R = list(csv.DictReader(open(DRY), delimiter="\t"))
    F = lambda r, k: float(r[k])
    by_rssd = {int(r["rssd"]): r for r in R if r["rssd"] not in ("", "None")}
    small = [r for r in R if r["small"] == "True" and r["merger"] == "False"]
    flagged = [r for r in small if F(r, "dbor") >= bs.FLAG_MIN_K and (F(r, "bor_p") == 0 or F(r, "dbor") / F(r, "bor_p") >= bs.FLAG_MIN_PCT) and F(r, "ddep") < 0]
    top20 = sorted((r for r in small if F(r, "dbor") > 0), key=lambda r: -F(r, "dbor"))[:20]
    big100 = sorted(small, key=lambda r: -F(r, "asset"))[:100]
    src = {}
    for rs in bs.COHORT_RSSD: src.setdefault(rs, set()).add("cohort")
    for r in flagged: src.setdefault(int(r["rssd"]), set()).add("Q2-flag")
    for r in top20: src.setdefault(int(r["rssd"]), set()).add("Q2-top20")
    for r in big100: src.setdefault(int(r["rssd"]), set()).add("top100-assets")
    # route check: cohort 6/30 via FFIEC must equal FDIC (bor_c of the Q1->Q2 dry run = 6/30 level)
    bad = []
    for rs in bs.COHORT_RSSD:
        sdf = m.facsimile(user, tok, rs, PRIOR)
        r = by_rssd.get(rs)
        if sdf is None or r is None:
            bad.append((bs.COHORT_RSSD[rs], "no 6/30 data")); continue
        x = extract(m.parse(sdf))
        if x["bor"] is None or abs(x["bor"] - F(r, "bor_c")) > 1 or abs((x["dep"] or 0) - (F(r, "dep_p") + F(r, "ddep"))) > 1:
            bad.append((bs.COHORT_RSSD[rs], f"FFIEC bor {x['bor']} dep {x['dep']} vs FDIC bor {F(r,'bor_c'):.0f} dep {F(r,'dep_p')+F(r,'ddep'):.0f}"))
    if bad:
        print("ROUTE CHECK FAILED (cohort 6/30 FFIEC != FDIC):"); [print("  ", b) for b in bad]; return 2
    rows, pending = [], []
    for rs, tags in src.items():
        r = by_rssd.get(rs)
        sdf = m.facsimile(user, tok, rs, CUR)
        if sdf is None:
            pending.append((r["name"] if r else str(rs), ",".join(sorted(tags)))); continue
        x = extract(m.parse(sdf))
        bp, dp = F(r, "bor_c"), F(r, "dep_p") + F(r, "ddep")
        flag = (x["bor"] is not None and x["bor"] - bp >= bs.FLAG_MIN_K and (bp == 0 or (x["bor"] - bp) / bp >= bs.FLAG_MIN_PCT)
                and x["dep"] is not None and x["dep"] - dp < 0)
        rows.append(dict(name=r["name"], state=r["state"], tags=",".join(sorted(tags)), asset=x["asset"], bor_p=bp, bor_c=x["bor"],
                         dbor=None if x["bor"] is None else x["bor"] - bp, ddep=None if x["dep"] is None else x["dep"] - dp,
                         fhlb=x["fhlb"], bro=x["bro"], flag=flag))
    rows.sort(key=lambda r: -(r["dbor"] or 0))
    cov_q2 = sum(F(by_rssd[rs], "bor_c") for rs in src if rs in by_rssd)
    tot_q2 = sum(F(r, "bor_c") for r in small)
    L = [f"# Borrowing short list, FFIEC Call Reports {PRIOR} -> {CUR}",
         f"Run {datetime.now().astimezone().isoformat(timespec='seconds')}. List {len(src)} banks "
         f"(holding {cov_q2/tot_q2*100:.0f}% of Q2 small-bank borrowings); **filed {len(rows)}, PENDING {len(pending)}**. "
         f"Route check passed: 14 cohort banks' 6/30 FFIEC figures equal FDIC. Flags = frozen rule; concentration NOT computed (needs full universe).\n"]
    if rows:
        fb = sum(r["dbor"] or 0 for r in rows); fd = sum(r["ddep"] or 0 for r in rows)
        L.append(f"**Filed banks so far:** borrowings net {fb/1e6:+.2f} $B, deposits net {fd/1e6:+.2f} $B; flagged {sum(r['flag'] for r in rows)}.\n")
        L.append("| Bank | State | List | Assets $B | Borrowings $B 6/30 -> 9/30 | Change $M | Deposits change $M | FHLB 9/30 $B | Brokered 9/30 $B | Flag |\n|---|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            L.append(f"| {r['name']} | {r['state']} | {r['tags']} | {(r['asset'] or 0)/1e6:.1f} | {r['bor_p']/1e6:.2f} -> {(r['bor_c'] or 0)/1e6:.2f} | "
                     f"{(r['dbor'] or 0)/1e3:+,.0f} | {(r['ddep'] or 0)/1e3:+,.0f} | {(r['fhlb'] or 0)/1e6:.2f} | {(r['bro'] or 0)/1e6:.2f} | {'⚑' if r['flag'] else ''} |")
    L.append(f"\n**PENDING ({len(pending)})** — re-run after filing; Call Reports are due 10/30, the FFIEC token expires 11/05: " + "; ".join(f"{n} ({t})" for n, t in sorted(pending)))
    text = "\n".join(L); print(text)
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        open(os.path.join(a.out, "borrowing_shortlist_Q3.md"), "w").write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
