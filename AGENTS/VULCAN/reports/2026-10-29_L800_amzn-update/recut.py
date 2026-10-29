#!/usr/bin/env python3
"""VULCAN re-cut of DEWEY's 2026E funding-gap cells on DEWEY's OWN method, with Q3 2026 actuals.
Method (verbatim from AGENTS/DEWEY/research/2026-10-29_L800-replay/replay.py): 2026E = filed year-to-date
actuals + remaining quarters, OCF at TTM/4 per quarter, payouts and finance-lease principal at the
latest-quarter rate. All $M. Each Q3 input is cited in the comment beside it; 'derived' = 9M minus H1.
Run: python3 -I recut.py  (also replays DEWEY's 10/22 cells first as a control)."""
import sys
def proj(ocf_ytd, n_rem, ttm_ocf, capex, fl_ytd, fl_lq, ret_ytd, ret_lq, add_fl):
    ocf = ocf_ytd + n_rem * ttm_ocf / 4
    fl = (fl_ytd + n_rem * fl_lq) if add_fl else 0
    ret = ret_ytd + n_rem * ret_lq
    return ocf, fl, ret, ocf - capex - fl - ret

base = {  # DEWEY 10/22 inputs, copied from replay.py (control: must print -186,456)
 "MSFT": (46679+55441, 2, 182935, 175000, 0, 0, 6756+6758+4627+4579, 6758+4579, False),
 "GOOGL": (45790+39069, 2, 185675, 200000, 840, 318, 5231, 2689, True),
 "AMZN": (26032+45387, 2, 161403, 220000, 863, 395, 0, 0, True),
 "META": (96873, 1, 133087, 140000, 0, 0, 4060, 1361, False),
 "ORCL": (23103, 3, 46940, 92500, 0, 0, 1565, 1565, False),
}
ctl = sum(proj(*a)[3] for a in base.values())
assert round(ctl) == -186456, ctl
print(f"CONTROL DEWEY 10/22 sum {ctl:,.0f} (expected -186,456)")

MSFT_Q3_OCF, MSFT_Q3CY25_OCF = 58000, 45057            # MSFT 8-K Ex99.1 10/28 (Q1 FY27; prior-year Q1 FY26)
MSFT_Q3_RET = 6757 + 4379                               # dividends + buybacks, Q1 FY27 (8-K/10-Q 10/28)
MSFT_Q3_FLP = 1000                                      # finance-lease principal Q1 FY27
GOOGL_Q3_OCF, GOOGL_Q3_25_OCF = 42290, 48414            # GOOGL 8-K Ex99.1 10/28
GOOGL_FL_9M, GOOGL_DIV_9M = 1950, 8167                  # DEWEY XBRL packets 10/29 (10-Q acc 0001652044-26-000084)
GOOGL_PREF_Q3 = 234                                     # DividendsPreferredStockCash Q3 (DEWEY 10/29), sensitivity only

new = dict(base)
new["MSFT"] = (46679+55441+MSFT_Q3_OCF, 1, 182935-MSFT_Q3CY25_OCF+MSFT_Q3_OCF, 170000, 0, 0,
               6756+6758+4627+4579+MSFT_Q3_RET, MSFT_Q3_RET, False)  # CY2026 ~$170B (Hood, call 10/28, T2)
new["GOOGL"] = (45790+39069+GOOGL_Q3_OCF, 1, 185675-GOOGL_Q3_25_OCF+GOOGL_Q3_OCF, 200000,
                GOOGL_FL_9M, GOOGL_FL_9M-840, GOOGL_DIV_9M, GOOGL_DIV_9M-5231, True)
AMZN = None  # filled after the print: (ocf_9m, 1, ttm_ocf, capex_2026, fl_9m, fl_q3, 0, 0, True)
if len(sys.argv) > 1:
    AMZN = tuple(float(x) for x in sys.argv[1:8]) ; AMZN = (AMZN[0], 1, AMZN[1], AMZN[2], AMZN[3], AMZN[4], AMZN[5], AMZN[6], True)
    new["AMZN"] = AMZN
tot = 0
for k in new:
    o, f, r, g = proj(*new[k]); b = proj(*base[k])[3]; tot += g
    tag = "" if new[k] is not base[k] else "  (unchanged: DEWEY 10/22)"
    print(f"{k:6s} OCF {o:9,.0f} capex {new[k][3]:9,.0f} FL {f:7,.0f} payouts {r:8,.0f} GAP {g:9,.0f}  (DEWEY {b:9,.0f}){tag}")
print(f"SUM mixed basis {tot:,.0f}  (DEWEY {ctl:,.0f})")
o, _, r, g = proj(*new["MSFT"])
cash = o - (170000-24608) - (839+922+MSFT_Q3_FLP+MSFT_Q3_FLP) - r
print(f"MSFT CY26 cash basis {cash:,.0f} (DEWEY -5,762; FY26 FL ROU additions 24,608 held out of the guide)")
print(f"SUM with MSFT on cash basis {tot - g + cash:,.0f}")
print(f"GOOGL sensitivity if preferred dividends are outside the ordinary tag: {proj(*new['GOOGL'])[3] - 2*GOOGL_PREF_Q3:,.0f} (Q3 actual + Q4 at Q3 rate)")
