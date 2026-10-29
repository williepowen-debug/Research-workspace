#!/usr/bin/env python3
"""Per-bank borrowing screen — WHO borrowed, quarter over quarter (FDIC BankFind, public, no login).

Answers the question the Fed's weekly H.8 aggregate cannot: is a rise in banks' borrowings spread
across many banks (system-level funding of loan growth) or concentrated in a few (bank-specific
strain)? Classification rule is FROZEN in reports/2026-10-28_borrowing-screen_FROZEN_rule.md
(verify its sha256 before a graded run; never edit the thresholds below without a new frozen doc).

Fields (FDIC risview, $ thousands; verified 2026-10-28: Amerant OTHBFHLB 6/30/26 = 702,608, matching
the ~$702M implied by its Q3 release): OTHBOR other borrowed money (FHLB advances, discount window,
other), OTHBFHLB FHLB advances (subset of OTHBOR), FREPP fed funds purchased + repos, DEP deposits,
BRO brokered deposits, ASSET total assets. Borrowings = OTHBOR + FREPP (the H.8 'borrowings' scope).

Usage (repo root):
  .venv/bin/python3 AGENTS/REGINALD/scripts/borrowing_screen.py --prior 20260630 --current 20260930 [--out DIR]
  .venv/bin/python3 AGENTS/REGINALD/scripts/borrowing_screen.py --prior 20260331 --current 20260630 --dry-run
Exit: 0 = screen ran on a complete quarter · 2 = route failed or the quarter is not fully posted
(fewer than MIN_ROWS institutions) — grade nothing from that run.
"""
import argparse, json, os, sys, urllib.request, urllib.parse
from datetime import datetime, timedelta

API = "https://api.fdic.gov/banks/financials"
FIELDS = "CERT,NAME,REPDTE,ASSET,DEP,OTHBOR,OTHBFHLB,FREPP,BRO,BKCLASS,RSSDID,STNAME"
MIN_ROWS = 4000                       # Q2-2026 posted 4,313; fewer means a partial posting
COMMERCIAL = {"N", "NM", "SM"}        # H.8 covers commercial banks; savings classes reported separately
TOP_EXCLUDED = 25                     # H.8 'large' = 25 largest domestically chartered; screen = the rest
# --- FROZEN thresholds (reports/2026-10-28_borrowing-screen_FROZEN_rule.md) ---
CONC_TOP_N = 10
CONC_SHARE = 0.50                     # top-10 increases >= 50% of all increases -> CONCENTRATED
BROAD_SHARE = 0.25                    # top-10 increases < 25% -> BROAD; otherwise MIXED
FLAG_MIN_K = 100_000                  # bank flag: borrowings up >= $100M ...
FLAG_MIN_PCT = 0.25                   # ... and >= 25% of prior borrowings (or prior zero) ...
MERGER_GROWTH = 0.20                  # assets up >= 20% in the quarter -> probable acquirer: inherited borrowings, not new
#                                       ... and deposits down quarter over quarter
COHORT_RSSD = {107244: "OZK", 3138146: "WAL", 2652092: "EGBN", 276579: "ZION", 1929247: "SSB",
               3303298: "CFG", 3938186: "BKU", 34537: "SBCF", 83638: "AMTB", 694904: "FLG",
               501105: "MTB", 12311: "HBAN", 229801: "VLY", 2354985: "CUBI"}


def fetch(repdte):
    rows, offset = [], 0
    while True:
        q = urllib.parse.urlencode({"filters": f"REPDTE:{repdte}", "fields": FIELDS, "limit": 10000,
                                    "offset": offset, "format": "json"})
        with urllib.request.urlopen(f"{API}?{q}", timeout=120) as r:
            d = json.load(r)
        batch = [x["data"] for x in d.get("data", [])]
        rows += batch
        if len(batch) < 10000:
            return rows, d.get("meta", {}).get("index", {}).get("createTimestamp")
        offset += 10000


def num(v):
    return float(v) if v not in (None, "") else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prior", required=True)
    ap.add_argument("--current", required=True)
    ap.add_argument("--out")
    ap.add_argument("--dry-run", action="store_true", help="label output as an instrument test, not a graded run")
    a = ap.parse_args()
    try:
        p_rows, p_idx = fetch(a.prior)
        c_rows, c_idx = fetch(a.current)
    except Exception as e:
        print(f"ROUTE FAILED: {e}"); return 2
    if len(p_rows) < MIN_ROWS or len(c_rows) < MIN_ROWS:
        print(f"INCOMPLETE: prior {len(p_rows)} rows, current {len(c_rows)} rows (< {MIN_ROWS}); "
              f"FDIC index {c_idx}. Quarter not fully posted — grade nothing."); return 2
    P = {r["CERT"]: r for r in p_rows}; C = {r["CERT"]: r for r in c_rows}
    com_prior = sorted((r for r in p_rows if r.get("BKCLASS") in COMMERCIAL), key=lambda r: -num(r["ASSET"]))
    top = {r["CERT"] for r in com_prior[:TOP_EXCLUDED]}
    recs = []
    for cert in set(P) & set(C):
        p, c = P[cert], C[cert]
        bp, bc = num(p["OTHBOR"]) + num(p["FREPP"]), num(c["OTHBOR"]) + num(c["FREPP"])
        recs.append(dict(cert=cert, name=c["NAME"], state=c.get("STNAME"), cls=c.get("BKCLASS"),
                         rssd=c.get("RSSDID"), asset=num(c["ASSET"]), asset_p=num(p["ASSET"]), bor_p=bp, bor_c=bc, dbor=bc - bp,
                         dfhlb=num(c["OTHBFHLB"]) - num(p["OTHBFHLB"]), ddep=num(c["DEP"]) - num(p["DEP"]),
                         dep_p=num(p["DEP"]), dbro=num(c["BRO"]) - num(p["BRO"]),
                         small=(c.get("BKCLASS") in COMMERCIAL and cert not in top)))
    for r in recs:
        r["merger"] = r["asset_p"] > 0 and r["asset"] / r["asset_p"] - 1 >= MERGER_GROWTH
    exits = [P[k] for k in set(P) - set(C)]
    small_all = [r for r in recs if r["small"]]
    small = [r for r in small_all if not r["merger"]]
    mergers = sorted((r for r in small_all if r["merger"]), key=lambda r: -r["dbor"])
    up = sorted((r for r in small if r["dbor"] > 0), key=lambda r: -r["dbor"])
    gross_up = sum(r["dbor"] for r in up)
    top_share = sum(r["dbor"] for r in up[:CONC_TOP_N]) / gross_up if gross_up else float("nan")
    verdict = ("CONCENTRATED" if top_share >= CONC_SHARE else "BROAD" if top_share < BROAD_SHARE else "MIXED")
    flags = [r for r in small if r["dbor"] >= FLAG_MIN_K and (r["bor_p"] == 0 or r["dbor"] / r["bor_p"] >= FLAG_MIN_PCT)
             and r["ddep"] < 0]
    flags.sort(key=lambda r: -r["dbor"])
    B = lambda k: k / 1e6
    L = []
    tag = "DRY RUN (instrument test, not a graded run)" if a.dry_run else "GRADED RUN"
    L.append(f"# Borrowing screen {a.prior} -> {a.current} — {tag}")
    L.append(f"Run {datetime.now().astimezone().isoformat(timespec='seconds')}; FDIC index prior {p_idx}, current {c_idx}; "
             f"rows {len(p_rows)}/{len(c_rows)}; matched {len(recs)}; small commercial universe {len(small)} "
             f"(commercial classes {sorted(COMMERCIAL)}, excluding the {TOP_EXCLUDED} largest by prior assets and {len(mergers)} probable "
             f"acquirers with assets up >= {MERGER_GROWTH*100:.0f}%; {len(exits)} institutions in the prior quarter are gone from the current one).\n")
    L.append(f"**Aggregate (small commercial):** borrowings {B(sum(r['bor_p'] for r in small)):.1f} -> "
             f"{B(sum(r['bor_c'] for r in small)):.1f} $B (net {B(sum(r['dbor'] for r in small)):+.1f}); "
             f"FHLB net {B(sum(r['dfhlb'] for r in small)):+.1f}; deposits net {B(sum(r['ddep'] for r in small)):+.1f}; "
             f"brokered net {B(sum(r['dbro'] for r in small)):+.1f}. Banks with borrowings up: {len(up)} of {len(small)}.")
    L.append(f"**Concentration:** top {CONC_TOP_N} increases = {top_share*100:.1f}% of gross increases "
             f"({B(gross_up):.1f} $B) -> **{verdict}** (frozen: >= {CONC_SHARE*100:.0f}% CONCENTRATED, < {BROAD_SHARE*100:.0f}% BROAD).")
    big25 = [r for r in recs if r["cert"] in top]
    L.append(f"Context, 25 largest commercial: borrowings net {B(sum(r['dbor'] for r in big25)):+.1f} $B; "
             f"savings institutions net {B(sum(r['dbor'] for r in recs if r['cls'] not in COMMERCIAL)):+.1f} $B.\n")
    hdr = "| Bank | State | Assets $B | Borrowings $B prior -> now | Change $M | FHLB change $M | Deposits change $M | Brokered change $M |"
    row = lambda r: (f"| {r['name']} | {r['state']} | {B(r['asset']):.1f} | {B(r['bor_p']):.2f} -> {B(r['bor_c']):.2f} | "
                     f"{r['dbor']/1e3:+,.0f} | {r['dfhlb']/1e3:+,.0f} | {r['ddep']/1e3:+,.0f} | {r['dbro']/1e3:+,.0f} |")
    L.append("## Largest 20 increases (small commercial)\n" + hdr + "\n|---|---|---|---|---|---|---|---|")
    L += [row(r) for r in up[:20]]
    L.append(f"\n## Probable acquirers excluded (assets up >= {MERGER_GROWTH*100:.0f}% in the quarter; borrowings inherited) — "
             f"net {B(sum(r['dbor'] for r in mergers)):+.1f} $B\n" + hdr + "\n|---|---|---|---|---|---|---|---|")
    L += [row(r) for r in mergers[:15]]
    ex_b = sum(num(x['OTHBOR']) + num(x['FREPP']) for x in exits)
    L.append(f"\nInstitutions gone between quarters (absorbed or failed): {len(exits)}, prior borrowings {B(ex_b):.2f} $B.")
    L.append(f"\n## Flagged: borrowings up >= $100M and >= 25%, deposits down ({len(flags)} banks)\n" + hdr + "\n|---|---|---|---|---|---|---|---|")
    L += [row(r) for r in flags[:40]]
    L.append("\n## Cohort (14 names; bank level; listed whether small or large)\n" + hdr + "\n|---|---|---|---|---|---|---|---|")
    L += [row(r) for r in sorted((r for r in recs if r["rssd"] and int(r["rssd"]) in COHORT_RSSD), key=lambda r: -r["asset"])]
    L.append("\nA flag is a lead to read the bank's own filing, not a signal: the aggregate 'borrowing up + deposits down' "
             "pattern showed no track record since 1985 (reports/2026-10-28_small-bank-borrowing-deep-dive.md §10).")
    text = "\n".join(L)
    print(text)
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        open(os.path.join(a.out, f"borrowing_screen_{a.prior}_{a.current}.md"), "w").write(text + "\n")
        with open(os.path.join(a.out, f"borrowing_screen_{a.prior}_{a.current}.tsv"), "w") as f:
            keys = ["cert", "name", "state", "cls", "rssd", "small", "merger", "asset_p", "asset", "bor_p", "bor_c", "dbor", "dfhlb", "ddep", "dep_p", "dbro"]
            f.write("\t".join(keys) + "\n")
            for r in sorted(recs, key=lambda r: -r["dbor"]):
                f.write("\t".join(str(r[k]) for k in keys) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
