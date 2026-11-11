# CRUISE 2026-11-11 catch-up: prices, CRU-11 interim, VX-CRU-01 distance, rate sensitivity.
import json, yfinance as yf
out = {}
t = ["CCL","RCL","NCLH","SPY","XLY","^FVX","^TNX","^TYX","^IRX"]
d = yf.download(t, start="2026-10-01", end="2026-11-12", auto_adjust=False, progress=False)
c, a = d["Close"], d["Adj Close"]
days = ["2026-11-06","2026-11-09","2026-11-10"]
out["closes"] = {k: {s: round(float(c.loc[k, s]), 3) for s in t} for k in days}
out["pct_change"] = {k: {s: round(float((c[s].pct_change()*100).loc[k]), 2) for s in ["CCL","RCL","NCLH","SPY","XLY"]} for k in days[1:]}
out["intraday_1111_note"] = "11/11 bars are intraday (read ~10:13 ET) and bond market closed; not used for grades"
out["intraday_1111"] = {s: round(float(c[s].iloc[-1]), 3) for s in ["CCL","RCL","NCLH"]}
ref = 33.99
out["vx01"] = {k: round((float(c.loc[k,"CCL"])/ref-1)*100, 2) for k in days}
out["vx01_minus10_line"] = round(ref*0.90, 4); out["vx01_minus20_line"] = round(ref*0.80, 4); out["vx01_minus35_line"] = round(ref*0.65, 4)
b = a.loc["2026-10-02"]
for k in days:
    n = (float(a.loc[k,"NCLH"])/float(b["NCLH"])-1)*100; r = (float(a.loc[k,"RCL"])/float(b["RCL"])-1)*100
    out.setdefault("cru11", {})[k] = {"NCLH": round(n,2), "RCL": round(r,2), "spread_pp": round(n-r,2)}
out["cru11_base_adj"] = {"NCLH": float(b["NCLH"]), "RCL": float(b["RCL"])}
out["ust"] = {k: {s: round(float(c.loc[k, s]),3) for s in ["^IRX","^FVX","^TNX","^TYX"]} for k in ["2026-10-15"]+days}
# Rate sensitivity from 10-Q primaries (figures typed from the filing text, cited in RESULT.md)
nclh_1pp = 18.2          # $M/yr per +1pp SOFR, 10-Q Item 3, 9/30/26
nclh_var_pct = 12
nclh_total = 15497.999   # $M scheduled principal incl. exchangeables + finance leases, 9/30/26
nclh_q3_int = 170.544    # $M Q3 interest expense, net
nclh_ttm_ebitda = 2699.038
revolver_repaid = 376.3  # $M 10/15 (KB-CRU-158)
var_impl = nclh_1pp/0.01
out["nclh"] = {"var_balance_implied_M": round(var_impl,1),
  "var_pct_x_total_M": round(nclh_total*nclh_var_pct/100,1),
  "per_25bp_M": round(nclh_1pp/4,2), "per_50bp_M": round(nclh_1pp/2,2),
  "post_oct_var_M_inferred": round(var_impl-revolver_repaid,1),
  "post_oct_per_25bp_M": round((var_impl-revolver_repaid)*0.0025,2),
  "per_25bp_pct_of_q3_annualized_interest": round(nclh_1pp/4/(nclh_q3_int*4)*100,2),
  "per_25bp_pct_of_ttm_ebitda": round(nclh_1pp/4/nclh_ttm_ebitda*100,3),
  "maturities_M": {"rem2026":238.600,"2027":1105.695,"2028":1346.141,"2029":1370.035,"2030":4134.290,"2031":1875.062,"thereafter":5428.176},
  "per_100bp_on_2027_maturities_M": round(1105.695*0.01,1),
  "exchangeables_2027_coupon_reset_to_8_75_M": round(216.2*(0.0875-0.0164),1)}
rcl_var, rcl_usd_var, rcl_total = 1412, 1216, 22872
out["rcl"] = {"var_pct": round(rcl_var/rcl_total*100,2), "usd_var_per_1pp_M_inferred": round(rcl_usd_var*0.01,1),
  "maturities_M": {"rem2026":579,"2027":2371,"2028":3211,"2029":1134,"2030":1084}}
ccl_total = 24559
out["ccl"] = {"floating_pct": 15, "usd_floating_pct": 5, "eur_floating_pct": 10,
  "usd_floating_M_inferred": round(ccl_total*0.05,0), "usd_per_1pp_M_inferred": round(ccl_total*0.05*0.01,1),
  "maturities_M": {"rem2026":301,"2027":2517,"2028":3961,"2029":3631,"2030":2885}}
json.dump(out, open("calculations.json","w"), indent=1)
print(json.dumps(out, indent=1))
