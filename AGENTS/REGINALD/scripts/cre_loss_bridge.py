#!/usr/bin/env python3
"""CRE loss bridge — exposed loans -> additional loss -> reserves already held -> earnings -> capital.

Built 2026-09-26 for reports/2026-09-26_CRE_top3_loss_bridge.md. SUPERSEDES scripts/cre_loss_scenarios.py,
which (a) did not net reserves already held against the stressed pools, (b) mixed bank and company bases, and
(c) carried three anchors CREED showed to be wrong (OZK RaDD 20%, FLG office comps, EGBN 39.6% on a MF-heavy pool).

RULES (each is a double-count guard):
  1. ONE BASIS PER BANK, named in BASIS. FLG: the 10-Q = the bank (holdco merged into the bank Oct-2025).
     EGBN: HOLDING COMPANY (the listed security) for capital and earnings; loans and ACL are identical at both levels.
     OZK: Bank OZK is the registrant; loans-only ACL ($461.5M); the $156.3M unfunded-commitment reserve is NOT used.
  2. POOLS ARE MUTUALLY EXCLUSIVE and carried at AMORTIZED COST, i.e. already NET of prior charge-offs, so a
     loss rate here is an ADDITIONAL loss on what is still on the books. Losses recognised earlier never re-enter.
     FLG's deck pool "NYC >=50% RR criticized $4.4B" is a SUBSET of the 10-Q grade tables — split out once, never
     stressed twice. EGBN substandard INCLUDES nonaccrual, so nonaccrual is carved out of it. HFS loans (at fair
     value, with executed sale contracts) are excluded.
  3. RESERVES ALREADY HELD are credited pool by pool: the SPECIFIC allowance where disclosed or derived, plus a
     PRO-RATA share of the segment's COLLECTIVE allowance (ASSUMPTION: no bank discloses collective ACL by grade).
     Credit per pool is capped at that pool's loss (no reserve release is assumed). A conservative variant credits
     SPECIFIC ONLY.
  4. OREO (foreclosed property) has NO allowance: write-downs run through non-interest EXPENSE, so they get no
     reserve credit.
  5. Capital: incremental after-tax hit on CET1, RWA unchanged, NO earnings offset (conservative), then shown
     against retained earnings (PPNR less dividends) in years. Tax 25% (assumption).
  6. Every CAPITAL CONCLUSION IS CONDITIONAL ON COVERAGE (the pools included) AND THE RATES. Losses outside the
     pools listed under EXCLUDED are not in the numbers.
Loss rates are ASSUMPTIONS with the anchor written beside each. Change them and re-run; nothing here is a forecast.
"""
TAX = 0.25

# pool: (name, balance $M, reserve_specific, reserve_collective, base, stress, channel, anchor)
BANKS = {
  "FLG": dict(
    basis="10-Q Q2-26 (acc 0000910073-26-000068) = bank; pools Note 5 risk grades; ACL Note 6; NYC RR split deck s15/16",
    cet1=7937, rwa=60312, ppnr=143, payout=50, buyback=250, floors=((10.5, "FLG's own CET1 target"), (7.0, "4.5% min + 2.5% buffer")),
    pools=[
      ("MF nonaccrual, NYC >=50% rent-regulated", 1737, 76, 0, .08, .20, "ACL",
       "already ~17.5% of original balance recognised (CREED fix); +8%/+20% takes total to ~24%/~34%; BCB NJ/NY problem pool sold <=79% of face"),
      ("MF nonaccrual, other", 395, 7, 0, .08, .20, "ACL", "same as above; specific ~$7M DERIVED (83 - 76)"),
      ("CRE nonaccrual", 471, 30, 0, .10, .25, "ACL", "ASSUMPTION ONLY - no market anchor (parent CRE mix 40% industrial / 22% office)"),
      ("MF SM+SS accruing, NYC >=50% RR", 2665, 0, 134, .05, .15, "ACL",
       "78% LTV / 1.01x DSCR; 49% reset within 18m; 2027 coupons ~3.9% vs ~8% reset; $2M cumulative charge-offs so far"),
      ("MF SM+SS accruing, other", 4274, 0, 41.2, .03, .10, "ACL", "ASSUMPTION; less rent-regulation; collective 0.96% pro-rata DERIVED"),
      ("CRE SM+SS accruing", 1367, 0, 21.6, .03, .10, "ACL", "ASSUMPTION ONLY; collective 1.58% pro-rata"),
      ("MF pass, NYC >=50% RR", 4089, 0, 48, .0, .01, "ACL", "rent freeze (0% renewals from 10/1/26) reaches FLG's DSCR review in Q2-2028"),
      ("MF pass, other", 13771, 0, 132.8, .0, .005, "ACL", "stress only"),
      ("CRE pass", 6406, 0, 101.4, .0, .0, "ACL", "not stressed"),
    ],
    excluded="C&I $18.6B incl. NDFI $3.46B (no line disclosed as CRE-fund lending); construction is inside the CRE totals; losses on future migrations beyond these rates; securities/AOCI",
  ),
  "EGBN": dict(
    basis="HOLDING COMPANY: Q2-26 10-Q (acc 0001050441-26-000096) grids + deck (acc -000088); CET1 $1,186.8M / RWA ~$8,140M (holdco)",
    cet1=1186.8, rwa=8140, ppnr=96.2, payout=1.2, buyback=0, floors=((10.0, "illustrative management-style level (no stated target on file)"), (7.0, "4.5% min + 2.5% buffer")),
    pools=[
      ("Office pass", 456.1, 0, 32.9, .02, .08, "ACL", "~89% of LTVs on pre-6/30/25 appraisals; EGBN re-appraisals -14% to -29%; loss sits in the 80%-LTV tail"),
      ("Office SM", 10.8, 0, 0.8, .05, .20, "ACL", "LTV 47% on a fresh 3/18/26 appraisal"),
      ("Office SS accruing", 32.0, 0, 2.3, .15, .40, "ACL", "Fairfax $22.1M at 96% LTV, matures 9/25/26"),
      ("Office nonaccrual", 34.3, 3.0, 0, .10, .35, "ACL", "DC loan already written to ~40% LTV"),
      ("MF pass", 408.6, 0, 4.2, .005, .03, "ACL", "appraisals imply a 3.5% cap rate (6.0% debt yield x 58% LTV); $404.6M of MF matures 2026H2"),
      ("MF SM", 79.2, 0, 0.8, .05, .15, "ACL", "DSCR 0.67-0.89"),
      ("MF SS accruing (ex $35.4M paid off after 6/30)", 158.6, 0, 1.7, .133, .30, "ACL",
       "base = EGBN's own H1-26 non-office exit haircut 13.3%; stress = -35% value on 84-88% LTV loans (PG apt DSCR 0.63; DC apt DSCR 0.15)"),
      ("MF nonaccrual", 10.9, 0, 0, .20, .40, "ACL", "MF specific allowance not disclosed (<= $6.1M); MF ACL total $6.7M allocated pro-rata above"),
      ("Other IPCRE pass (hotel $373M, retail, mixed-use, industrial, other)", 1328.7, 0, 18.1, .0, .01, "ACL", "hotels hold the largest 2026 maturity share nationally (30%, CREED/MBA, secondary)"),
      ("Other IPCRE SM", 92.1, 0, 1.25, .03, .10, "ACL", "ASSUMPTION"),
      ("Other IPCRE SS accruing", 54.4, 0, 0.74, .133, .30, "ACL", "non-office haircut 13.3%"),
      ("Other IPCRE nonaccrual", 31.7, 3.0, 0, .133, .30, "ACL", "segment ACL $23.1M: specific 0-6.1 undisclosed split with MF, 3.0 assumed; collective 20.1 pro-rata (1.36%)"),
      ("Owner-occupied CRE criticized (SM+SS+NA)", 64.6, 0, 0.7, .08, .20, "ACL", "ASSUMPTION; operating-business risk"),
      ("Construction pass", 461.2, 0, 3.9, .0, .02, "ACL", "84% of construction matures within a year"),
      ("Construction criticized (SM+SS+NA)", 62.0, 0.07, 0.5, .08, .25, "ACL", "ASSUMPTION"),
    ],
    excluded="owner-occupied CRE pass $1.60B; C&I $1.54B incl. $152.7M of CRE booked as C&I (MI3); HFS $49.7M at fair value with executed contracts; post-6/30 migrations",
  ),
  "OZK": dict(
    basis="Bank OZK (registrant = bank): Q2-26 10-Q filed with the FDIC + Call Report RSSD 107244; loans-only ACL $461.5M",
    cet1=5300.5, rwa=44916, ppnr=1082.6, payout=220.1, buyback=200, floors=((10.0, "illustrative (no stated target on file)"), (7.0, "4.5% min + 2.5% buffer")),
    pools=[
      ("Boston 10 Prospect nonaccrual (life-sci)", 169.3, 0, 0, .30, .50, "ACL",
       "$0 allowance; 91% LTV on a Nov-25 appraisal; Concord analog appraisal -32% in 13m. UPSIDE CASE: the $330M pending sale (unreconciled with a ~$186M appraisal) closes -> $0"),
      ("Baltimore land nonaccrual", 40.0, 0, 0, .0, .15, "ACL", "33% cushion on a fresh appraisal that fell 20% YoY"),
      ("The Jack, Seattle office nonaccrual", 25.9, 0, 0, .05, .40, "ACL", "100% of a Dec-25 appraisal; OZK's own Seattle office exit cleared at 58% of appraisal"),
      ("Wauwatosa hotel nonaccrual", 16.7, 0, 0, .0, .15, "ACL", "hard-deposit sale contract at or above carrying"),
      ("Other nonaccrual", 48.5, 13.7, 0, .10, .25, "ACL", "ASSUMPTION; composition not disclosed (may include non-CRE)"),
      ("OREO office (Seattle, Santa Monica, Atlanta)", 137.5, 0, 0, .152, .402, "EXP",
       "carried at 89-100% of appraisal vs OZK's own office exits at 58-80% of appraisal"),
      ("OREO life-sci (Seattle, Chicago)", 96.0, 0, 0, .05, .275, "EXP", "already near office-conversion value"),
      ("OREO LA land", 54.5, 0, 0, .0, .30, "EXP", "LOI at/above carrying; 3 years in OREO, one failed buyer"),
      ("Tahoe substandard accruing", 29.4, 7.3, 0, .10, .25, "ACL", "ASSUMPTION"),
      ("Special mention (5 RESG credits $529.2M + other)", 616.2, 0, 8.4, .03, .12, "ACL",
       "incl. a condo at 105.6% LTV (commitment $147M); collective 1.37% pro-rata"),
      ("RaDD life-science, pass-rated", 555.0, 0, 7.6, .0, .65, "ACL",
       "OZK desk severity 65-70% (AGENTS/OZK/STATUS.md:117; ~3.3% leased; interest from reserves); base 0 = extension/recap in negotiation"),
    ],
    excluded="pass RESG book (~$14.7B construction + non-owner-occupied less named credits); RaDD's ~$360M UNFUNDED commitment (only $555M funded is in the pool); the $430M debt-on-debt book (indirect CRE, first charge-offs $42.4M YTD) except where already nonaccrual; the $40.4M C&I hardship loan",
  ),
}


def bridge(b, case_i, collective=True):
    loss = reserve = 0.0
    for name, bal, spec, coll, base, stress, ch, _ in b["pools"]:
        l = bal * (base if case_i == 4 else stress)
        loss += l
        if ch == "ACL":
            reserve += min(l, spec + (coll if collective else 0))
    hit = loss - reserve
    cet1_after = b["cet1"] - hit * (1 - TAX)
    return loss, reserve, hit, cet1_after


def run():
    for tk, b in BANKS.items():
        exposed = sum(p[1] for p in b["pools"])
        print(f"\n== {tk} — basis: {b['basis']}")
        print(f"   exposed pools ${exposed:,.0f}M · CET1 ${b['cet1']:,}M = {100*b['cet1']/b['rwa']:.2f}% · PPNR TTM ${b['ppnr']}M · payouts ${b['payout']}M/yr")
        for case, i in (("BASE", 4), ("STRESS", 5)):
            for coll in (True, False):
                loss, res, hit, c1 = bridge(b, i, coll)
                retained = b["ppnr"] - b["payout"]
                print(f"   {case:6} {'spec+coll' if coll else 'spec only'}: loss ${loss:,.0f}M − reserves credited ${res:,.0f}M = "
                      f"new P&L hit ${hit:,.0f}M = {hit/b['ppnr']:.1f}y PPNR / {hit/retained:.1f}y retained · CET1 → {100*c1/b['rwa']:.2f}% "
                      + " · ".join(f"{100*c1/b['rwa']-f:+.2f}pp vs {f}%" for f, _ in b["floors"])
                      + (f" · if the ${b['buyback']}M authorised buyback is also executed: {100*(c1-b['buyback'])/b['rwa']:.2f}%" if b['buyback'] else ""))
        for p in b["pools"]:
            print(f"     - {p[0]}: ${p[1]:,}M (spec {p[2]}, coll {p[3]}) × {p[4]:.1%}/{p[5]:.1%} [{p[6]}] {p[7]}")
        print(f"   EXCLUDED (capital conclusions do not cover these): {b['excluded']}")


if __name__ == "__main__":
    run()
