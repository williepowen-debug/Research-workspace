#!/usr/bin/env python3
"""⛔ SUPERSEDED 2026-09-26 by scripts/cre_loss_bridge.py (this version did not net reserves held, mixed bases, and carried three anchors CREED showed wrong). Kept for the record only.

CRE loss scenarios for the 2026-09-26 top-3 CRE-vulnerability report (FLG / OZK / EGBN).

ILLUSTRATIVE, NOT A FORECAST. Every pool balance is a disclosed 6/30/2026 figure (source in POOLS);
every loss rate is an ASSUMPTION stated here with its anchor, so a reader can change it and re-run.
Loss rate = bundled (probability of default x loss given default) on the CURRENT carrying balance,
i.e. loss IN ADDITION to write-downs already taken. Tax 25% (assumption). Capital math treats the
scenario loss as wholly incremental provision (conservative: it ignores that part of today's ACL
already provides for these pools) and shows it with and without two years of pre-provision revenue.
"""
TAX = 0.25
BANKS = {
  "FLG": dict(acl=869, ppnr=196, cet1=7937, rwa=60323, floor=10.5,
    src="10-Q Q2-26 risk-rating tables (acc 0000910073-26-000068); ACL/CET1/RWA Call Report 6/30/26; "
        "PPNR = Call Report H1-26 (pretax RIAD4301 + provision RIADJJ33) x2; floor = FLG's own 10.5% CET1 target",
    pools=[  # (name, balance $M, base loss, stress loss, anchor)
      ("MF nonaccrual", 2132, .08, .20, "NYC >=50% RR nonaccrual already carries ~20.5% charged-off+reserved; BCB NJ/NY problem-pool sale <=79% of face"),
      ("CRE nonaccrual", 471, .08, .20, "same anchor as MF nonaccrual"),
      ("MF substandard (accruing)", 4182, .05, .15, "criticized NYC RR at 78% LTV / 1.01x DSCR; 2027 resets at ~3.9% coupon vs ~8% market (mods cut from 8.03%)"),
      ("CRE substandard (accruing)", 991, .05, .15, "office ACL 3.0%; Chicago/LA office sales -61% to -72% vs peak (CREED, secondary)"),
      ("MF special mention", 2757, .01, .05, "+33.5% in H1; migration rate unknown"),
      ("CRE special mention", 376, .01, .05, ""),
      ("MF pass", 17860, .0, .005, "rent freeze reaches the DSCR review in Q2-2028; stress only"),
    ]),
  "OZK": dict(acl=462, ppnr=1026, cet1=5301, rwa=44919, floor=10.0,
    src="OZK desk STATUS (Q2-26 10-Q filed with FDIC, cert 110) for pools; OREO = Call Report RCON2150 $288.1M "
        "(OZK desk $292.7M bank-wide); ACL = Call Report RCON3123 (company ACL $617.8M incl. unfunded); floor 10% assumption",
    pools=[
      ("Nonaccrual (4 RESG + other)", 300, .10, .30, "$257.8M carries $0 allowance = already marked to collateral; Boston lab vacancy 26.4%"),
      ("Foreclosed property (OREO)", 288, .10, .25, "carried at fair value less cost; H1 inflows $241.6M vs sales $6.9M = marks untested by sales"),
      ("Substandard accruing", 73, .10, .25, ""),
      ("Special mention", 616, .03, .12, "5 RESG credits $529.2M incl. $147M condo at 105.6% LTV"),
      ("RaDD life-science (pass-rated)", 555, .0, .20, "extension+recap in negotiation; stress only"),
    ]),
  "EGBN": dict(acl=121, ppnr=126, cet1=1211, rwa=8098, floor=10.0,
    src="Q2-26 10-Q/deck (acc 0001050441-26-000096 / -000088); PPNR = Call Report H1-26 x2 (company TTM $96.2M); floor 10% as in dossier",
    pools=[
      ("Substandard HFI (incl. $111M nonaccrual)", 460, .165, .396, "EGBN's own realized exit haircut: Q2-26 16.5% (base), FY-25 39.6% (stress)"),
      ("Special mention", 274, .02, .10, "downgrades into criticized $160M (Q1) -> $216M (Q2)"),
      ("MF maturing 2026H2 not already criticized (approx.)", 200, .0, .05, "MF DSCR 1.0x, MF ACL $6.7M; balance approximate (of $404.6M maturing, criticized share unknown)"),
    ]),
}

def run():
    for tk, b in BANKS.items():
        print(f"\n== {tk}  (ACL ${b['acl']}M · PPNR ${b['ppnr']}M/yr · CET1 ${b['cet1']}M = {100*b['cet1']/b['rwa']:.2f}% · floor {b['floor']}%)")
        print(f"   sources: {b['src']}")
        for case, i in (("BASE", 2), ("STRESS", 3)):
            L = sum(p[1] * p[i] for p in b["pools"])
            c0 = b["cet1"] - L * (1 - TAX)
            c2 = c0 + 2 * b["ppnr"] * (1 - TAX)
            excess = b["cet1"] - b["floor"] / 100 * b["rwa"]
            print(f"   {case:6} loss ${L:,.0f}M = {L/b['acl']:.2f}x ACL · {L/b['ppnr']:.1f} yrs PPNR · "
                  f"{L*(1-TAX)/excess:.2f}x CET1 excess over {b['floor']}% · pro-forma CET1 {100*c0/b['rwa']:.2f}% "
                  f"(no PPNR) / {100*c2/b['rwa']:.2f}% (+2yr PPNR)")
        for p in b["pools"]:
            print(f"     - {p[0]}: ${p[1]:,}M x {p[2]:.1%} / {p[3]:.1%}  [{p[4]}]")

if __name__ == "__main__":
    run()
