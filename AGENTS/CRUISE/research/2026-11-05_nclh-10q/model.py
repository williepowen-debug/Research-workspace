#!/usr/bin/env python3
"""NCLH funding re-run on 9/30/26 actuals. Same method and endpoint (12/31/27) as the
9/19 and 10/14 papers. Endpoint test only: no interim cash trough. USD millions."""
import json, pathlib
FY25=2089.7; M9_26=1706.36; H1_26=1414.038; M9_25=1630.636; H1_25=1394.072
cash=256.508; avail=1100.0          # 10-Q Note 2; avail is rounded ("$1.1 billion")
rev_repaid=380.0; commit_add=315.0  # 10-Q Note 7; 8-K 10/15 said ~376.3
bridge=950.0-(950.0-941.7)-525.0-rev_repaid-42.2   # net proceeds less principal uses
growth=1100+3100; eca=600+2000; other_26=100; other_27=400  # other_27 is an ASSUMPTION
amort=238.600+1105.695              # 10-Q schedule, rem-2026 + 2027; incl. 216.2 exchangeables
uses=growth-eca+other_26+other_27+amort-bridge
def ocf(g):
    fy26=FY25*(1+g); return (fy26-M9_26)+FY25*(1+g)**2
def left(g,extra=0.0,room=None):
    room=avail+rev_repaid+commit_add if room is None else room
    return room+cash-(uses+extra-ocf(g))
def be(extra=0.0,room=None):
    lo,hi=-0.6,0.2
    for _ in range(200):
        m=(lo+hi)/2
        if left(m,extra,room)>0: hi=m
        else: lo=m
    return (lo+hi)/2
R_full=avail+rev_repaid+commit_add; R_ex=avail+rev_repaid
out={"inputs":{"cash":cash,"revolver_available_rounded":avail,"revolver_repaid_10Q":rev_repaid,
 "commitment_add_conditional":commit_add,"october_bridge":round(bridge,1),"growth_capex":growth,"eca":eca,
 "other_capex_rem26":other_26,"other_capex_fy27_ASSUMED":other_27,"amortisation":round(amort,1),"uses_before_ocf":round(uses,1)},
 "q3_ocf":{"q3_26":round(M9_26-H1_26,1),"q3_25":round(M9_25-H1_25,1)},
 "scenarios":{}}
for g in (0.02,0.0,-0.05,-0.10,-0.15,-0.20):
    out["scenarios"][f"{g:+.0%}"]={"ocf_window":round(ocf(g),1),"left_with_315":round(left(g),1),"left_ex_315":round(left(g,room=R_ex),1),
      "left_ex_315_after_175_interest":round(left(g,175,R_ex),1)}
out["breakeven_g"]={"with_315":round(be(),4),"ex_315":round(be(room=R_ex),4),
  "ex_315_after_175_interest":round(be(175,R_ex),4)}
fy27_be=FY25*(1+out["breakeven_g"]["ex_315"])**2
out["breakeven_fy27_ocf_ex_315"]=round(fy27_be,0)
# Free Liquidity bridge to 11/17 (ESTIMATE; conservative excludes the 315 layer)
fl_oct=cash+avail+rev_repaid+bridge
q4_ocf_flat=FY25-M9_26
q4_net=(1100-600)+100+238.6-42.2-q4_ocf_flat
out["free_liquidity_est"]={"after_october_deal_ex_315":round(fl_oct,0),"after_october_deal_with_315":round(fl_oct+commit_add,0),
 "q4_net_need_whole_quarter_flat_ocf":round(q4_net,0),"worst_case_whole_q4_need_by_11_17_ex_315":round(fl_oct-q4_net,0),
 "margin_over_800_worst_case":round(fl_oct-q4_net-800,0)}
# Net funded debt / capitalization, 9/30/26
debt_c=1134.959+13951.544; debt_p=15497.999; eq=3148.948
for k,d in (("carrying",debt_c),("principal",debt_p)):
    tn=d-cash
    out[f"nfd_cap_{k}"]={"with_addback_7409":round(tn/(tn+eq+7409.044),3),"without_addback":round(tn/(tn+eq),3),
      "addback_needed_for_0.80":round(tn/0.80-tn-eq,0)}
# Operating cash flow composition, 9M
wc26=42.669-53.394-19.689+30.353+54.461-36.597; wc25=-32.046-6.322+13.360+49.584-72.590+13.877
out["ocf_9m"]={"delta":round(M9_26-M9_25,1),"working_capital_26":round(wc26,1),"working_capital_25":round(wc25,1),
 "delta_wc":round(wc26-wc25,1),"delta_cash_earnings":round((M9_26-wc26)-(M9_25-wc25),1)}
out["deposit_cash_line"]={"h1_26":481.997,"h1_25":708.135,"q3_26":round(-36.597-481.997,1),"q3_25":round(13.877-708.135,1),
 "gap_h1":round(481.997-708.135,1),"gap_9m":round(-36.597-13.877,1)}
print(json.dumps(out,indent=1))
pathlib.Path(__file__).with_name("calculations.json").write_text(json.dumps(out,indent=1)+"\n")
