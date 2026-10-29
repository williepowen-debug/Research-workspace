#!/usr/bin/env python3
"""Replay of Table 1 2026E cells in output/2026-10-22_hyperscaler-ai-funding-gap-ig-capacity.md.
Method recovered verbatim from the 10/22 working script (session 6ad84bf0, sub-agent ac065..., calc.py);
the 10/22 scratchpad died with the session, so this file is the durable recipe (DEWEY rule 8d).
All $M. Inputs: quarterly values decumulated from SEC XBRL companyconcept (filed facts) and the filed
cash-flow statements; MSFT and GOOGL re-verified 2026-10-29 (see erratum in the report).
2026E = filed year-to-date actuals + remaining quarters, OCF at TTM/4 per quarter, payouts and FL
principal at the LATEST-QUARTER rate. MSFT period = calendar 2026 (guide ~$175B is a CY2026 figure
that already counts finance leases at signing, so FL principal is NOT subtracted on the headline)."""
def proj(ocf_ytd, n_rem, ttm_ocf, capex, fl_ytd, fl_lq, ret_ytd, ret_lq, add_fl):
    ocf = ocf_ytd + n_rem * ttm_ocf / 4
    fl = (fl_ytd + n_rem * fl_lq) if add_fl else 0
    ret = ret_ytd + n_rem * ret_lq
    return ocf, fl, ret, ocf - capex - fl - ret
rows = {
 # name: (ocf_ytd, n_rem, ttm_ocf, capex, fl_ytd, fl_lq, ret_ytd, ret_lq, add_fl)
 "MSFT CY26 headline ($175B incl FL at signing)": (46679+55441, 2, 182935, 175000, 0, 0, 6756+6758+4627+4579, 6758+4579, False),
 "GOOGL CY26 ($200B mid)": (45790+39069, 2, 185675, 200000, 840, 318, 5231, 2689, True),
 "AMZN CY26 ($220B)": (26032+45387, 2, 161403, 220000, 863, 395, 0, 0, True),
 "META CY26 ($140B mid)": (96873, 1, 133087, 140000, 0, 0, 4060, 1361, False),
 "ORCL FY27 gross ($92.5B mid)": (23103, 3, 46940, 92500, 0, 0, 1565, 1565, False),
}
tot = 0
for k, a in rows.items():
    ocf, fl, ret, gap = proj(*a); tot += gap
    print(f"{k:48s} OCF {ocf:9,.0f}  capex {a[3]:9,.0f}  FL {fl:7,.0f}  payouts {ret:8,.0f}  GAP {gap:9,.0f}")
print(f"{'SUM (mixed basis)':48s} {tot:,.0f}")
# MSFT cash basis: hold FY26 finance-lease ROU additions (24,608) out of the guide; subtract FL principal
ocf, _, ret, _ = proj(*rows["MSFT CY26 headline ($175B incl FL at signing)"])
cash_ppe = 175000 - 24608; flp = (839+922) + 2*922
print(f"MSFT CY26 cash basis: OCF {ocf:,.0f} - cash P&E {cash_ppe:,.0f} - FL principal {flp:,.0f} - payouts {ret:,.0f} = {ocf-cash_ppe-flp-ret:,.0f}")
print(f"SUM with MSFT on cash basis: {tot - proj(*rows['MSFT CY26 headline ($175B incl FL at signing)'])[3] + (ocf-cash_ppe-flp-ret):,.0f}")
